#!/usr/bin/env python3
"""Validate hidden Support QA metadata against the wiki it describes.

The checks in this file are deliberately independent from the publishing
plugins.  Metadata under ``.github/support-qa`` must describe customer content
without ever becoming part of a publication payload.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote

try:  # CI intentionally works without this optional dependency.
    import jsonschema  # type: ignore
except ImportError:  # pragma: no cover - exercised by fallback-specific tests
    jsonschema = None


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
SUPPORT_QA = Path(".github/support-qa")
SUPPORT_INDEX = Path(".github/support-index.json")
PRACTICE_README = "sample-files/practice/README.md"
EXCLUDED_DOCUMENT_PARTS = {".git", ".github", ".agents", ".codex", ".private"}
IMAGE_RE = re.compile(
    r"!\[([^\]]*)\]\((?:<([^>]+)>|([^\s)]+))(?:\s+(?:\"[^\"]*\"|'[^']*'))?\)"
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


@dataclass(frozen=True)
class ImageUse:
    document: str
    file: str
    section: str
    alt_text: str
    line: int


def _read_json(path: Path, issues: list[str]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        issues.append(f"{path}: required JSON file is missing")
    except (OSError, json.JSONDecodeError) as exc:
        issues.append(f"{path}: could not read valid JSON: {exc}")
    return None


def _relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def _schema_errors(instance: Any, schema: dict[str, Any], label: str) -> list[str]:
    if jsonschema is not None:
        validator = jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        )
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        return [
            f"{label}:{_json_path(error.absolute_path)}: {error.message}"
            for error in errors
        ]
    return _manual_schema_errors(instance, schema, schema, label)


def _json_path(parts: Iterable[Any]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _manual_schema_errors(
    instance: Any,
    schema: dict[str, Any],
    root_schema: dict[str, Any],
    label: str,
    path: str = "$",
) -> list[str]:
    """Small Draft 2020-12 subset covering both repository schemas.

    Keeping this fallback beside the policy prevents a missing optional package
    from silently disabling schema validation in a fresh checkout.
    """

    if "$ref" in schema:
        ref = schema["$ref"]
        if not isinstance(ref, str) or not ref.startswith("#/"):
            return [f"{label}:{path}: unsupported schema reference {ref!r}"]
        target: Any = root_schema
        try:
            for token in ref[2:].split("/"):
                target = target[token.replace("~1", "/").replace("~0", "~")]
        except (KeyError, TypeError):
            return [f"{label}:{path}: unresolved schema reference {ref!r}"]
        return _manual_schema_errors(instance, target, root_schema, label, path)

    issues: list[str] = []
    for child in schema.get("allOf", []):
        issues.extend(_manual_schema_errors(instance, child, root_schema, label, path))
    if "anyOf" in schema:
        candidates = [
            _manual_schema_errors(instance, child, root_schema, label, path)
            for child in schema["anyOf"]
        ]
        if not any(not candidate for candidate in candidates):
            issues.append(f"{label}:{path}: does not match any allowed schema")
    if "oneOf" in schema:
        matched = sum(
            not _manual_schema_errors(instance, child, root_schema, label, path)
            for child in schema["oneOf"]
        )
        if matched != 1:
            issues.append(f"{label}:{path}: must match exactly one allowed schema (matched {matched})")
    if "not" in schema and not _manual_schema_errors(
        instance, schema["not"], root_schema, label, path
    ):
        issues.append(f"{label}:{path}: matches a forbidden schema")

    condition = schema.get("if")
    if condition is not None and not _manual_schema_errors(
        instance, condition, root_schema, label, path
    ):
        issues.extend(
            _manual_schema_errors(instance, schema.get("then", {}), root_schema, label, path)
        )
    elif condition is not None and "else" in schema:
        issues.extend(
            _manual_schema_errors(instance, schema["else"], root_schema, label, path)
        )

    expected_type = schema.get("type")
    type_matches = {
        "object": isinstance(instance, dict),
        "array": isinstance(instance, list),
        "string": isinstance(instance, str),
        "integer": isinstance(instance, int) and not isinstance(instance, bool),
        "number": isinstance(instance, (int, float)) and not isinstance(instance, bool),
        "boolean": isinstance(instance, bool),
        "null": instance is None,
    }
    if expected_type and not type_matches.get(expected_type, False):
        return issues + [f"{label}:{path}: expected {expected_type}"]
    if "const" in schema and instance != schema["const"]:
        issues.append(f"{label}:{path}: must equal {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        issues.append(f"{label}:{path}: value {instance!r} is not allowed")

    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            issues.append(f"{label}:{path}: string is too short")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            issues.append(f"{label}:{path}: string is too long")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            issues.append(f"{label}:{path}: does not match {schema['pattern']!r}")
        if schema.get("format") == "date":
            try:
                date.fromisoformat(instance)
            except ValueError:
                issues.append(f"{label}:{path}: must be an ISO date")
        if schema.get("format") == "date-time":
            try:
                datetime.fromisoformat(instance.replace("Z", "+00:00"))
            except ValueError:
                issues.append(f"{label}:{path}: must be an ISO date-time")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            issues.append(f"{label}:{path}: must be at least {schema['minimum']}")
        if "exclusiveMinimum" in schema and instance <= schema["exclusiveMinimum"]:
            issues.append(f"{label}:{path}: must be greater than {schema['exclusiveMinimum']}")

    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            issues.append(f"{label}:{path}: has too few items")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            issues.append(f"{label}:{path}: has too many items")
        if schema.get("uniqueItems"):
            fingerprints = [json.dumps(value, sort_keys=True) for value in instance]
            if len(fingerprints) != len(set(fingerprints)):
                issues.append(f"{label}:{path}: items must be unique")
        if "items" in schema:
            for index, value in enumerate(instance):
                issues.extend(
                    _manual_schema_errors(
                        value, schema["items"], root_schema, label, f"{path}[{index}]"
                    )
                )
        if "contains" in schema and not any(
            not _manual_schema_errors(value, schema["contains"], root_schema, label, path)
            for value in instance
        ):
            issues.append(f"{label}:{path}: lacks a required matching item")

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                issues.append(f"{label}:{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in sorted(set(instance) - set(properties)):
                issues.append(f"{label}:{path}: unexpected property {key!r}")
        for key, child in properties.items():
            if key in instance:
                issues.extend(
                    _manual_schema_errors(
                        instance[key], child, root_schema, label, f"{path}.{key}"
                    )
                )
    return issues


def _discover_documents(root: Path) -> list[str]:
    documents: list[str] = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if path.name == "AGENTS.md" or any(part in EXCLUDED_DOCUMENT_PARTS for part in rel.parts):
            continue
        documents.append(rel.as_posix())
    return sorted(documents)


def _index_roles(index: dict[str, Any]) -> dict[str, str]:
    roles = {index["home"]["source"]: "home"}
    for topic in index["topics"]:
        roles[topic["overview"]] = "topic"
        for group in topic["groups"]:
            for guide in group["guides"]:
                roles[guide["source"]] = "guide"
    roles[PRACTICE_README] = "repository-reference"
    return roles


def _clean_heading(value: str) -> str:
    return re.sub(r"[`*_~]", "", re.sub(r"<[^>]+>", "", value)).strip()


def _markdown_image_uses(root: Path, document: str, issues: list[str]) -> list[ImageUse]:
    source_path = root / document
    text = source_path.read_text(encoding="utf-8")
    current_heading = "Document introduction"
    uses: list[ImageUse] = []
    for number, line in enumerate(text.splitlines(), start=1):
        heading = HEADING_RE.match(line)
        if heading:
            current_heading = _clean_heading(heading.group(2))
        for match in IMAGE_RE.finditer(line):
            alt_text = match.group(1).strip()
            raw_target = unquote((match.group(2) or match.group(3)).split("#", 1)[0].split("?", 1)[0])
            if raw_target.startswith(("http://", "https://", "data:")):
                continue
            resolved = (source_path.parent / raw_target).resolve()
            try:
                target = resolved.relative_to(root.resolve()).as_posix()
            except ValueError:
                issues.append(f"{document}:{number}: screenshot reference leaves repository: {raw_target}")
                continue
            uses.append(ImageUse(document, target, current_heading, alt_text, number))
    return uses


def _png_facts(path: Path) -> tuple[int, int, str] | None:
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height, hashlib.sha256(data).hexdigest()


def _check_review_baseline(
    root: Path,
    source: str,
    verification: dict[str, Any],
    baseline: dict[str, str],
    label: str,
    issues: list[str],
) -> None:
    if verification.get("status") != "needs-review":
        return
    current_path = root / source
    current_digest = hashlib.sha256(current_path.read_bytes()).hexdigest() if current_path.is_file() else None
    if source not in baseline:
        issues.append(f"{label}: new source cannot use needs-review; complete verification is required")
    elif baseline[source] != current_digest:
        issues.append(
            f"{label}: source changed after its review baseline; complete verification is required"
        )


def _review_baseline(
    root: Path, policy: dict[str, Any], issues: list[str]
) -> tuple[dict[str, str], dict[str, str]]:
    raw_path = policy.get("coverageBaseline", {}).get("reviewBaseline")
    if not isinstance(raw_path, str):
        issues.append("coverageBaseline.reviewBaseline: required path is missing")
        return {}, {}
    value = _read_json(root / raw_path, issues)
    if not isinstance(value, dict):
        return {}, {}
    if set(value) != {"schemaVersion", "frozenAt", "documents", "screenshots"}:
        issues.append(f"{raw_path}: expected schemaVersion, frozenAt, documents, and screenshots")
    if value.get("schemaVersion") != 1:
        issues.append(f"{raw_path}: schemaVersion must be 1")
    try:
        date.fromisoformat(value.get("frozenAt", ""))
    except (TypeError, ValueError):
        issues.append(f"{raw_path}: frozenAt must be an ISO date")

    result: list[dict[str, str]] = []
    for key in ("documents", "screenshots"):
        records = value.get(key)
        if not isinstance(records, dict):
            issues.append(f"{raw_path}: {key} must be an object")
            result.append({})
            continue
        cleaned: dict[str, str] = {}
        for source, digest in records.items():
            if not isinstance(source, str) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                issues.append(f"{raw_path}: invalid {key} baseline entry {source!r}")
                continue
            cleaned[source] = digest
        result.append(cleaned)
    return result[0], result[1]


def _metadata_records(
    root: Path, directory: Path, identity: str, issues: list[str]
) -> tuple[dict[str, tuple[Path, dict[str, Any]]], list[Path]]:
    records: dict[str, tuple[Path, dict[str, Any]]] = {}
    paths = sorted((root / directory).rglob("*.json")) if (root / directory).is_dir() else []
    for path in paths:
        value = _read_json(path, issues)
        if not isinstance(value, dict):
            if value is not None:
                issues.append(f"{_relative(path, root)}: sidecar must contain a JSON object")
            continue
        key = value.get(identity)
        if not isinstance(key, str):
            issues.append(f"{_relative(path, root)}: missing string identity field {identity!r}")
            continue
        if key in records:
            issues.append(
                f"{_relative(path, root)}: duplicate {identity} {key!r}; first declared by "
                f"{_relative(records[key][0], root)}"
            )
            continue
        records[key] = (path, value)
    return records, paths


def _metadata_use_tuple(value: dict[str, Any], document_key: str) -> tuple[str, str, str, str]:
    return (
        str(value.get(document_key, "")),
        str(value.get("section", "")),
        str(value.get("altText", "")),
        str(value.get("purpose", "")),
    )


def _content_for_language(text: str, *, remove_inline_code: bool) -> str:
    def preserve_lines(match: re.Match[str]) -> str:
        return "\n" * match.group(0).count("\n")

    text = re.sub(r"<!--.*?-->", preserve_lines, text, flags=re.DOTALL)
    text = re.sub(
        r"^(?:```|~~~).*?^(?:```|~~~)\s*$",
        preserve_lines,
        text,
        flags=re.DOTALL | re.MULTILINE,
    )
    # Rendered prose contains the label or image alt text, not its destination.
    text = re.sub(
        r"!?\[([^\]]*)\]\((?:<[^>]+>|[^)\s]+)(?:\s+(?:\"[^\"]*\"|'[^']*'))?\)",
        lambda match: match.group(1),
        text,
    )
    if remove_inline_code:
        text = re.sub(r"`[^`\n]+`", "", text)
    return text


def _language_issues(
    root: Path, published_documents: set[str], policy: dict[str, Any]
) -> list[str]:
    issues: list[str] = []
    language = policy.get("language", {})
    for document in sorted(published_documents):
        text = _content_for_language((root / document).read_text(encoding="utf-8"), remove_inline_code=False)
        for phrase in language.get("hardForbiddenPhrases", []):
            match = re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", text, flags=re.IGNORECASE)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                issues.append(f"{document}:{line}: hard-forbidden customer phrase: {phrase}")

    for rule in language.get("discouragedWordRatchet", []):
        word = rule.get("word")
        if not isinstance(word, str):
            continue
        plural = "" if word.lower().endswith("s") else "s?"
        expression = re.compile(
            r"(?<!\w)" + re.escape(word) + plural + r"(?!\w)", re.IGNORECASE
        )
        occurrences = 0
        documents = 0
        for document in sorted(published_documents):
            text = _content_for_language(
                (root / document).read_text(encoding="utf-8"), remove_inline_code=True
            )
            count = len(expression.findall(text))
            occurrences += count
            documents += count > 0
        if occurrences > rule.get("maximumOccurrences", occurrences):
            issues.append(
                f"language.{word}: {occurrences} occurrences exceed ratchet maximum "
                f"{rule['maximumOccurrences']}"
            )
        if documents > rule.get("maximumDocuments", documents):
            issues.append(
                f"language.{word}: {documents} documents exceed ratchet maximum "
                f"{rule['maximumDocuments']}"
            )
    return issues


def check_support_qa(root: Path | str = DEFAULT_ROOT) -> list[str]:
    """Return deterministic Support QA failures for ``root``."""

    root = Path(root).resolve()
    issues: list[str] = []
    meta_root = root / SUPPORT_QA
    policy = _read_json(meta_root / "policy.json", issues)
    index = _read_json(root / SUPPORT_INDEX, issues)
    document_schema = _read_json(meta_root / "schemas/document.schema.json", issues)
    screenshot_schema = _read_json(meta_root / "schemas/screenshot.schema.json", issues)
    if not all(isinstance(value, dict) for value in (policy, index, document_schema, screenshot_schema)):
        return issues
    document_baseline, screenshot_baseline = _review_baseline(root, policy, issues)

    documents = _discover_documents(root)
    screenshots = sorted(
        path.relative_to(root).as_posix() for path in (root / "screenshots").rglob("*.png")
    ) if (root / "screenshots").is_dir() else []
    expected_documents = policy["coverageBaseline"]["documents"]["expected"]
    expected_screenshots = policy["coverageBaseline"]["screenshots"]["expected"]
    if len(documents) != expected_documents:
        issues.append(f"document inventory: expected {expected_documents}, found {len(documents)}")
    if len(screenshots) != expected_screenshots:
        issues.append(f"screenshot inventory: expected {expected_screenshots}, found {len(screenshots)}")

    try:
        roles = _index_roles(index)
    except (KeyError, TypeError) as exc:
        return issues + [f"{SUPPORT_INDEX}: cannot derive publication roles: {exc}"]
    if set(documents) != set(roles):
        for source in sorted(set(documents) - set(roles)):
            issues.append(f"{source}: QA document is not mapped by support-index or repository-reference policy")
        for source in sorted(set(roles) - set(documents)):
            issues.append(f"{source}: support-index document does not exist")

    publication_text = json.dumps(index, sort_keys=True)
    metadata_root = policy["publicationIsolation"]["metadataRoot"]
    if metadata_root in publication_text or "support-qa" in publication_text:
        issues.append(f"{SUPPORT_INDEX}: hidden QA metadata must not appear in publication contract")
    for source in roles:
        if source.startswith(metadata_root + "/"):
            issues.append(f"{SUPPORT_INDEX}: publishes hidden QA source {source}")

    document_records, document_sidecar_paths = _metadata_records(
        root, SUPPORT_QA / "documents", "source", issues
    )
    screenshot_records, screenshot_sidecar_paths = _metadata_records(
        root, SUPPORT_QA / "screenshots", "file", issues
    )
    if len(document_sidecar_paths) != expected_documents:
        issues.append(
            f"document sidecars: expected exactly {expected_documents}, found {len(document_sidecar_paths)}"
        )
    if len(screenshot_sidecar_paths) != expected_screenshots:
        issues.append(
            f"screenshot sidecars: expected exactly {expected_screenshots}, found {len(screenshot_sidecar_paths)}"
        )

    for source in documents:
        expected_path = meta_root / "documents" / f"{source}.json"
        record = document_records.get(source)
        if record is None:
            issues.append(f"{source}: missing document sidecar {_relative(expected_path, root)}")
            continue
        path, value = record
        if path != expected_path:
            issues.append(f"{_relative(path, root)}: sidecar path must be {_relative(expected_path, root)}")
        issues.extend(_schema_errors(value, document_schema, _relative(path, root)))
        if value.get("role") != roles.get(source):
            issues.append(
                f"{_relative(path, root)}: role {value.get('role')!r} must be {roles.get(source)!r}"
            )
        actual_digest = hashlib.sha256((root / source).read_bytes()).hexdigest()
        if value.get("fileFacts", {}).get("sha256") != actual_digest:
            issues.append(f"{_relative(path, root)}: fileFacts.sha256 does not match {source}")
        verification = value.get("verification", {})
        _check_review_baseline(
            root,
            source,
            verification,
            document_baseline,
            _relative(path, root),
            issues,
        )

    for source, (path, _value) in document_records.items():
        if source not in documents:
            issues.append(f"{_relative(path, root)}: sidecar describes out-of-scope document {source}")

    image_uses: list[ImageUse] = []
    for document in documents:
        image_uses.extend(_markdown_image_uses(root, document, issues))
    uses_by_document: dict[str, list[ImageUse]] = defaultdict(list)
    uses_by_file: dict[str, list[ImageUse]] = defaultdict(list)
    for use in image_uses:
        uses_by_document[use.document].append(use)
        uses_by_file[use.file].append(use)

    for source in documents:
        record = document_records.get(source)
        if record is None:
            continue
        path, value = record
        actual = Counter((use.file, use.section, use.alt_text) for use in uses_by_document[source])
        declared = Counter(
            (str(use.get("file", "")), str(use.get("section", "")), str(use.get("altText", "")))
            for use in value.get("screenshotUses", [])
        )
        for item, count in (actual - declared).items():
            issues.append(
                f"{_relative(path, root)}: missing screenshotUse for file={item[0]!r}, "
                f"section={item[1]!r}, altText={item[2]!r} ({count} placement(s))"
            )
        for item, count in (declared - actual).items():
            issues.append(
                f"{_relative(path, root)}: screenshotUse does not match Markdown placement "
                f"file={item[0]!r}, section={item[1]!r}, altText={item[2]!r} ({count} extra)"
            )

    for screenshot in screenshots:
        relative_under_screenshots = Path(screenshot).relative_to("screenshots")
        expected_path = meta_root / "screenshots" / Path(f"{relative_under_screenshots.as_posix()}.json")
        record = screenshot_records.get(screenshot)
        if record is None:
            issues.append(f"{screenshot}: missing screenshot sidecar {_relative(expected_path, root)}")
            continue
        path, value = record
        if path != expected_path:
            issues.append(f"{_relative(path, root)}: sidecar path must be {_relative(expected_path, root)}")
        issues.extend(_schema_errors(value, screenshot_schema, _relative(path, root)))
        facts = _png_facts(root / screenshot)
        if facts is None:
            issues.append(f"{screenshot}: file is not a valid PNG with an IHDR header")
        else:
            width, height, digest = facts
            declared_facts = value.get("fileFacts", {})
            for key, actual in (("format", "png"), ("width", width), ("height", height), ("sha256", digest)):
                if declared_facts.get(key) != actual:
                    issues.append(
                        f"{_relative(path, root)}: fileFacts.{key}={declared_facts.get(key)!r} "
                        f"does not match {actual!r}"
                    )

        actual_uses = uses_by_file.get(screenshot, [])
        expected_status = "referenced" if actual_uses else "retained-unreferenced"
        if value.get("usageStatus") != expected_status:
            issues.append(
                f"{_relative(path, root)}: usageStatus must be {expected_status!r} based on Markdown"
            )
        actual_counter = Counter((use.document, use.section, use.alt_text) for use in actual_uses)
        declared_counter = Counter(
            (str(use.get("document", "")), str(use.get("section", "")), str(use.get("altText", "")))
            for use in value.get("uses", [])
        )
        for item, count in (actual_counter - declared_counter).items():
            issues.append(
                f"{_relative(path, root)}: missing use for document={item[0]!r}, "
                f"section={item[1]!r}, altText={item[2]!r} ({count})"
            )
        for item, count in (declared_counter - actual_counter).items():
            issues.append(
                f"{_relative(path, root)}: use does not match Markdown placement "
                f"document={item[0]!r}, section={item[1]!r}, altText={item[2]!r} ({count} extra)"
            )

        verification = value.get("verification", {})
        _check_review_baseline(
            root,
            screenshot,
            verification,
            screenshot_baseline,
            _relative(path, root),
            issues,
        )
        if verification.get("status") == "verified":
            plan = value.get("capturePlan", {})
            provenance = value.get("provenance", {})
            if plan.get("dataProfile") != provenance.get("dataProfile"):
                issues.append(f"{_relative(path, root)}: capturePlan and provenance dataProfile differ")

    for screenshot, (path, _value) in screenshot_records.items():
        if screenshot not in screenshots:
            issues.append(f"{_relative(path, root)}: sidecar describes missing screenshot {screenshot}")

    # The same purpose belongs on both sides of the document-to-image relation.
    document_declared: Counter[tuple[str, str, str, str, str]] = Counter()
    for source, (_path, value) in document_records.items():
        for use in value.get("screenshotUses", []):
            file, section, alt, purpose = _metadata_use_tuple(use, "file")
            document_declared[(source, file, section, alt, purpose)] += 1
    screenshot_declared: Counter[tuple[str, str, str, str, str]] = Counter()
    for file, (_path, value) in screenshot_records.items():
        for use in value.get("uses", []):
            document, section, alt, purpose = _metadata_use_tuple(use, "document")
            screenshot_declared[(document, file, section, alt, purpose)] += 1
    for relation, count in (document_declared - screenshot_declared).items():
        issues.append(f"metadata relation missing from screenshot sidecar: {relation} ({count})")
    for relation, count in (screenshot_declared - document_declared).items():
        issues.append(f"metadata relation missing from document sidecar: {relation} ({count})")

    published_documents = set(roles) - {PRACTICE_README}
    issues.extend(_language_issues(root, published_documents, policy))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate hidden SPRK Support QA metadata")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)
    issues = check_support_qa(args.root)
    if args.format == "json":
        print(json.dumps({"ok": not issues, "issues": issues}, indent=2))
    elif issues:
        print(f"Support QA failed with {len(issues)} issue(s):")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Support QA passed.")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
