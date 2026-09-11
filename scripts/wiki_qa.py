#!/usr/bin/env python3
"""Lightweight QA checks for SPRK wiki Markdown.

By default this checks every public Markdown file. Pass explicit paths to
check a focused set. ``--all`` remains as an explicit alias for the default.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

from support_qa import check_support_qa


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / ".private" / "wiki-page-inventory.md"
SUPPORT_INDEX = ROOT / ".github" / "support-index.json"
SUPPORT_INDEX_SCHEMA = ROOT / ".github" / "support-index.schema.json"
PRACTICE_README = "sample-files/practice/README.md"
EXPECTED_TOPIC_IDS = [
    "getting-started",
    "using-sprk",
    "company-setup",
    "customers-invoices-payments",
    "vendors-bills-checks",
    "banking",
    "reconcile",
    "reports",
    "month-end",
    "accounts-journals",
    "company-settings",
    "preferences",
    "backups",
    "plugins",
    "licensing",
    "faq-glossary",
    "help",
]
TOPIC_VISIBILITY_KEYS = {"website", "inApp", "search", "topicDirectory"}
GUIDE_VISIBILITY_KEYS = {"website", "inApp", "search", "topicIndex"}

BANNED_PUBLIC_PATTERNS = [
    "Business Scenario",
    "Evidence:",
    "Validation note",
    "walkthrough confirmed",
    "The walkthrough confirmed",
    "Use this scenario",
    "source evidence",
    "source-backed",
    "current build",
    "fixture",
    "ticket",
    "handoff",
    "backend",
    "manifest",
    "runtime",
    "sha256",
    "per-line linkage",
    "direct synchronization",
    "normalized amount",
    "source-document-owned",
    "current live flow",
]

RETIRED_FILLER = [
    "The result looks ready, but a key check is unresolved",
    "The result does not match what you expected",
    "You are about to take an action that may affect the result",
    "The action is unavailable or does not complete",
    "The page does not show the expected result",
    "The entered value or selection does not produce the expected result",
    "Verify the visible SPRK state before continuing",
    "Review the visible state and use the related workflow before continuing",
    "Confirm the visible company, page, and workflow state before continuing",
    "Use the specific workflow or control named on this page",
    "Use the visible navigation or related workflow named on this page",
    "Review the visible state before continuing",
    "Go back to that check before continuing",
    "Complete the missing value or review step before continuing",
    "Return to the workflow this page supports",
]

OBSOLETE_SUPPORT_PATTERNS = [
    "Discord",
    "View or Submit Bugs",
    "public releases page",
    "bug submission",
    "bug-report",
    "release notes",
    "release-note",
]

TROUBLESHOOTING_TABLE = "| What You See | What To Check | What To Do Next |"
GENERIC_TROUBLESHOOTING_LABELS = {
    "Something appears ready or safe based on an assumption",
    "One workflow, field, or result appears interchangeable with another",
    "A required review step may have been missed",
    "SPRK does not do what you expected",
    "The wrong workflow or page may be in use",
    "The result may not match the workflow you intended",
}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def run_git(args: list[str]) -> list[str]:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def public_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if is_public_path(path.relative_to(ROOT).as_posix())
    )


def changed_markdown_files() -> list[Path]:
    changed = run_git(["diff", "--name-only", "--diff-filter=ACMRT"])
    untracked = run_git(["ls-files", "--others", "--exclude-standard"])
    paths: list[Path] = []
    for name in changed + untracked:
        if not name.endswith(".md"):
            continue
        if not is_public_path(name):
            continue
        path = ROOT / name
        if path.exists():
            paths.append(path)
    return sorted(set(paths))


def is_public_path(rel: str) -> bool:
    return not (
        rel.startswith(".git/")
        or rel.startswith(".private/")
        or rel.startswith(".github/")
        or rel.startswith(".agents/")
        or rel.startswith(".codex/")
        or rel == "AGENTS.md"
        or rel.endswith("/AGENTS.md")
    )


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_banned_terms(path: Path, text: str) -> list[str]:
    issues: list[str] = []
    for pattern in BANNED_PUBLIC_PATTERNS:
        start = 0
        while True:
            index = text.find(pattern, start)
            if index == -1:
                break
            issues.append(
                f"{path.relative_to(ROOT)}:{line_number(text, index)} banned public term: {pattern}"
            )
            start = index + len(pattern)
    lowered = text.lower()
    for pattern in RETIRED_FILLER + OBSOLETE_SUPPORT_PATTERNS:
        index = lowered.find(pattern.lower())
        if index != -1:
            issues.append(
                f"{path.relative_to(ROOT)}:{line_number(text, index)} retired public wording: {pattern}"
            )
    if "sample-files/v1-validation" in text:
        index = text.find("sample-files/v1-validation")
        issues.append(
            f"{path.relative_to(ROOT)}:{line_number(text, index)} old sample path: sample-files/v1-validation"
        )
    return issues


def check_troubleshooting_table(path: Path, text: str) -> list[str]:
    issues: list[str] = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().lower() != "## if something looks wrong":
            continue
        section = []
        for next_line in lines[i + 1 :]:
            if next_line.startswith("## "):
                break
            section.append(next_line.strip())
        if TROUBLESHOOTING_TABLE not in section:
            issues.append(
                f"{path.relative_to(ROOT)}:{i + 1} troubleshooting section missing required table header"
            )
        for offset, row in enumerate(section, start=i + 2):
            if not row.startswith("|") or row.startswith("|---") or row == TROUBLESHOOTING_TABLE:
                continue
            cells = [cell.strip() for cell in row.split("|")[1:-1]]
            if len(cells) == 3 and cells[0] == cells[1]:
                issues.append(
                    f"{path.relative_to(ROOT)}:{offset} duplicated troubleshooting symptom/check cells: {cells[0]}"
                )
            if len(cells) == 3 and cells[0] in GENERIC_TROUBLESHOOTING_LABELS:
                issues.append(
                    f"{path.relative_to(ROOT)}:{offset} generic troubleshooting symptom: {cells[0]}"
                )
    return issues


def check_links(path: Path, text: str) -> list[str]:
    issues: list[str] = []
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        target = target.strip("<>")
        if not target or should_skip_link(target):
            continue
        target_path, _, fragment = target.partition("#")
        target_path = unquote(target_path.split("?", 1)[0])
        resolved = path.resolve() if not target_path and fragment else (path.parent / target_path).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            issues.append(
                f"{path.relative_to(ROOT)}:{line_number(text, match.start())} link leaves repo: {target}"
            )
            continue
        if not resolved.exists():
            issues.append(
                f"{path.relative_to(ROOT)}:{line_number(text, match.start())} missing relative link target: {target}"
            )
            continue
        if fragment and resolved.suffix.lower() == ".md":
            anchors = markdown_anchors(read(resolved))
            if unquote(fragment).lower() not in anchors:
                issues.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, match.start())} missing Markdown anchor: {target}"
                )
    return issues


def check_related_links(path: Path, text: str) -> list[str]:
    if "## Related" not in text:
        return []
    section = text.split("## Related", 1)[1].split("\n## ", 1)[0]
    seen: set[str] = set()
    issues: list[str] = []
    for match in LINK_RE.finditer(section):
        target = match.group(1).strip()
        if should_skip_link(target):
            continue
        if target in seen:
            issues.append(f"{path.relative_to(ROOT)}: duplicate link in Related: {target}")
        seen.add(target)
    return issues


def markdown_anchors(text: str) -> set[str]:
    """Return GitHub-style heading anchors, including duplicate suffixes."""

    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        label = re.sub(r"<[^>]+>", "", match.group(1)).lower()
        label = re.sub(r"[`*_~]", "", label)
        label = re.sub(r"[^\w\- ]", "", label, flags=re.UNICODE)
        base = re.sub(r"\s+", "-", label.strip())
        occurrence = counts.get(base, 0)
        counts[base] = occurrence + 1
        anchors.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return anchors


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def normalized_relative_link(source: Path, target: str) -> str | None:
    target = target.strip().strip("<>")
    if not target or should_skip_link(target) or target.startswith("#"):
        return None
    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    try:
        return (source.parent / target).resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return None


def section_links(path: Path, text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    in_section = False
    links: list[str] = []
    for line in lines:
        if line == f"## {heading}":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section:
            continue
        for match in LINK_RE.finditer(line):
            if line[: match.start()].rstrip().endswith("!"):
                continue
            normalized = normalized_relative_link(path, match.group(1))
            if normalized:
                links.append(normalized)
    return links


def check_visibility(
    value: object, allowed: set[str], location: str
) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, dict):
        return [f"{location}: visibility must be an object"]
    issues: list[str] = []
    unknown = set(value) - allowed
    if unknown:
        issues.append(f"{location}: unsupported visibility keys: {sorted(unknown)}")
    for key, flag in value.items():
        if not isinstance(flag, bool):
            issues.append(f"{location}: visibility.{key} must be boolean")
    return issues


def check_support_index() -> list[str]:
    issues: list[str] = []
    for path in (SUPPORT_INDEX, SUPPORT_INDEX_SCHEMA):
        if not path.exists():
            issues.append(f"{path.relative_to(ROOT)}: required file is missing")
    if issues:
        return issues

    try:
        index = json.loads(read(SUPPORT_INDEX))
    except (json.JSONDecodeError, OSError) as exc:
        return [f".github/support-index.json: invalid JSON: {exc}"]
    try:
        schema = json.loads(read(SUPPORT_INDEX_SCHEMA))
    except (json.JSONDecodeError, OSError) as exc:
        return [f".github/support-index.schema.json: invalid JSON: {exc}"]

    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        issues.append(".github/support-index.schema.json: expected JSON Schema draft 2020-12")
    if index.get("schemaVersion") != 1:
        issues.append(".github/support-index.json: schemaVersion must be 1")
    if set(index) != {"schemaVersion", "home", "navigation", "topics"}:
        issues.append(".github/support-index.json: unexpected or missing top-level keys")

    topics = index.get("topics")
    if not isinstance(topics, list):
        return issues + [".github/support-index.json: topics must be an array"]
    topic_ids = [topic.get("id") for topic in topics if isinstance(topic, dict)]
    if topic_ids != EXPECTED_TOPIC_IDS:
        issues.append(
            ".github/support-index.json: topic IDs/order must match the approved 17-topic order"
        )

    guide_ids: set[str] = set()
    guide_sources: set[str] = set()
    topic_overviews: set[str] = set()
    topic_paths: set[str] = set()
    seen_topic_ids: set[str] = set()

    for topic_index, topic in enumerate(topics):
        location = f".github/support-index.json:topics[{topic_index}]"
        if not isinstance(topic, dict):
            issues.append(f"{location}: topic must be an object")
            continue
        required = {"id", "path", "overview", "title", "summary", "groups"}
        allowed_topic = required | {"visibility"}
        missing = required - set(topic)
        if missing:
            issues.append(f"{location}: missing keys: {sorted(missing)}")
            continue
        if set(topic) - allowed_topic:
            issues.append(f"{location}: unsupported keys: {sorted(set(topic) - allowed_topic)}")
        if topic["id"] in seen_topic_ids:
            issues.append(f"{location}: duplicate topic id: {topic['id']}")
        seen_topic_ids.add(topic["id"])
        topic_path = topic["path"]
        overview = topic["overview"]
        if topic_path in topic_paths:
            issues.append(f"{location}: duplicate topic path: {topic_path}")
        topic_paths.add(topic_path)
        if overview in topic_overviews:
            issues.append(f"{location}: duplicate topic overview: {overview}")
        topic_overviews.add(overview)
        overview_path = ROOT / overview
        if not overview_path.is_file():
            issues.append(f"{location}: overview does not exist: {overview}")
        elif first_heading(read(overview_path)) != topic["title"]:
            issues.append(f"{overview}: H1 must match manifest title {topic['title']!r}")
        if not isinstance(topic["summary"], str) or not topic["summary"].strip():
            issues.append(f"{location}: summary must be non-empty")
        issues.extend(check_visibility(topic.get("visibility"), TOPIC_VISIBILITY_KEYS, location))

        seen_topic_links: set[str] = set()
        expected_topic_links: list[str] = []
        seen_group_ids: set[str] = set()
        for group_index, group in enumerate(topic["groups"]):
            group_location = f"{location}.groups[{group_index}]"
            if not isinstance(group, dict) or set(group) != {"id", "title", "guides"}:
                issues.append(f"{group_location}: group must contain id, title, and guides")
                continue
            if group["id"] in seen_group_ids:
                issues.append(f"{group_location}: duplicate group id: {group['id']}")
            seen_group_ids.add(group["id"])
            expected_group_links: list[str] = []
            for guide_index, guide in enumerate(group["guides"]):
                guide_location = f"{group_location}.guides[{guide_index}]"
                if not isinstance(guide, dict):
                    issues.append(f"{guide_location}: guide must be an object")
                    continue
                required_guide = {"id", "source", "title", "summary"}
                allowed_guide = required_guide | {"aliases", "visibility"}
                missing_guide = required_guide - set(guide)
                if missing_guide:
                    issues.append(f"{guide_location}: missing keys: {sorted(missing_guide)}")
                    continue
                if set(guide) - allowed_guide:
                    issues.append(
                        f"{guide_location}: unsupported keys: {sorted(set(guide) - allowed_guide)}"
                    )
                guide_id = guide["id"]
                source = guide["source"]
                if guide_id != source.removesuffix(".md"):
                    issues.append(f"{guide_location}: id must be source path without .md")
                if guide_id in guide_ids:
                    issues.append(f"{guide_location}: duplicate guide id: {guide_id}")
                guide_ids.add(guide_id)
                if source in guide_sources:
                    issues.append(f"{guide_location}: duplicate guide source: {source}")
                guide_sources.add(source)
                if source in seen_topic_links:
                    issues.append(f"{overview}: duplicate guide link: {source}")
                seen_topic_links.add(source)
                source_path = ROOT / source
                if not source_path.is_file():
                    issues.append(f"{guide_location}: source does not exist: {source}")
                else:
                    source_text = read(source_path)
                    if first_heading(source_text) != guide["title"]:
                        issues.append(f"{source}: H1 must match manifest title {guide['title']!r}")
                if not isinstance(guide["summary"], str) or not guide["summary"].strip():
                    issues.append(f"{guide_location}: summary must be non-empty")
                aliases = guide.get("aliases", [])
                if not isinstance(aliases, list) or any(not isinstance(alias, str) for alias in aliases):
                    issues.append(f"{guide_location}: aliases must be an array of strings")
                elif len(set(aliases)) != len(aliases):
                    issues.append(f"{guide_location}: aliases must be unique")
                issues.extend(check_visibility(guide.get("visibility"), GUIDE_VISIBILITY_KEYS, guide_location))
                if guide.get("visibility", {}).get("topicIndex", True):
                    expected_topic_links.append(source)
                    expected_group_links.append(source)
            if overview_path.is_file():
                actual_group_links = [
                    source
                    for source in section_links(overview_path, read(overview_path), group["title"])
                    if source.startswith(f"{topic_path}/") and source.endswith(".md")
                ]
                if actual_group_links != expected_group_links:
                    issues.append(
                        f"{overview}: {group['title']!r} links must match visible manifest guides and order"
                    )

        if overview_path.is_file():
            actual_topic_links = []
            for match in LINK_RE.finditer(read(overview_path)):
                source = normalized_relative_link(overview_path, match.group(1))
                if source is not None and source.startswith(f"{topic_path}/") and source.endswith(".md"):
                    actual_topic_links.append(source)
            if actual_topic_links != expected_topic_links:
                issues.append(
                    f"{overview}: local guide links must match visible manifest guides and order"
                )

    customer_guides = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*.md")
        if is_public_path(path.relative_to(ROOT).as_posix())
        and path.name != "README.md"
    }
    if guide_sources != customer_guides:
        for source in sorted(customer_guides - guide_sources):
            issues.append(f"{source}: guide is missing from support-index allowlist")
        for source in sorted(guide_sources - customer_guides):
            issues.append(f"{source}: manifest source is not a customer guide")

    home = index.get("home", {})
    expected_home_keys = {"source", "title", "summary", "featuredGroups", "topicDirectoryLabel"}
    if set(home) != expected_home_keys:
        issues.append(".github/support-index.json: home has unexpected or missing keys")
    home_path = ROOT / home.get("source", "")
    if not home_path.is_file():
        issues.append(".github/support-index.json: home.source must exist")
    else:
        home_text = read(home_path)
        if first_heading(home_text) != home.get("title"):
            issues.append(f"{home['source']}: H1 must match home.title")
        prose_lines = [
            line for line in home_text.splitlines()[1:] if line and not line.startswith("#")
        ]
        if prose_lines and prose_lines[0] == home.get("summary"):
            issues.append(f"{home['source']}: fallback intro must not duplicate the hero summary")
        featured_ids: list[str] = []
        for group in home.get("featuredGroups", []):
            expected_sources = [f"{guide_id}.md" for guide_id in group.get("guideIds", [])]
            featured_ids.extend(group.get("guideIds", []))
            actual_sources = section_links(home_path, home_text, group.get("title", ""))
            if actual_sources != expected_sources:
                issues.append(
                    f"{home['source']}: links under {group.get('title')!r} must match manifest order"
                )
        if len(featured_ids) != 18 or len(set(featured_ids)) != 18:
            issues.append(".github/support-index.json: homepage must feature 18 unique guides")
        for guide_id in featured_ids:
            if guide_id not in guide_ids:
                issues.append(f".github/support-index.json: unknown homepage guide id: {guide_id}")

    navigation = index.get("navigation", {})
    if set(navigation) != {"guideFooter"}:
        issues.append(".github/support-index.json: navigation must contain only guideFooter")
    footer = navigation.get("guideFooter", {})
    expected_footer_keys = {
        "enabled", "previousNext", "showTopicLink", "showHomeLink", "contactGuideId"
    }
    if set(footer) != expected_footer_keys:
        issues.append(".github/support-index.json: guideFooter has unexpected or missing keys")
    if footer.get("enabled") is not True or footer.get("previousNext") != "within-topic":
        issues.append(".github/support-index.json: guide footer must enable within-topic previous/next")
    if footer.get("showTopicLink") is not True or footer.get("showHomeLink") is not True:
        issues.append(".github/support-index.json: guide footer must link to topic and home")
    if footer.get("contactGuideId") not in guide_ids:
        issues.append(".github/support-index.json: contactGuideId must identify a guide")

    if PRACTICE_README in guide_sources or PRACTICE_README in topic_overviews:
        issues.append(f"{PRACTICE_README}: practice README must stay outside publication metadata")
    return issues


def should_skip_link(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("tel:")
        or lowered.startswith("app://")
    )


def check_inventory(path: Path, inventory_text: str) -> list[str]:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("sample-files/practice/") and rel != "sample-files/practice/README.md":
        return []
    if f"`{rel}`" not in inventory_text:
        return [f"{rel}: missing from .private/wiki-page-inventory.md"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Markdown files or directories to check")
    parser.add_argument("--all", action="store_true", help="check every public Markdown file")
    args = parser.parse_args()

    if args.all:
        targets = public_markdown_files()
    elif args.paths:
        targets = []
        for raw in args.paths:
            path = (ROOT / raw).resolve()
            if path.is_dir():
                targets.extend(p for p in path.rglob("*.md") if is_public_path(p.relative_to(ROOT).as_posix()))
            elif path.exists() and path.suffix == ".md" and is_public_path(path.relative_to(ROOT).as_posix()):
                targets.append(path)
        targets = sorted(set(targets))
    else:
        targets = public_markdown_files()

    inventory_text = read(INVENTORY) if INVENTORY.exists() else ""
    issues: list[str] = []
    issues.extend(check_support_index())
    issues.extend(check_support_qa(ROOT))

    for path in targets:
        text = read(path)
        issues.extend(check_banned_terms(path, text))
        issues.extend(check_troubleshooting_table(path, text))
        issues.extend(check_links(path, text))
        issues.extend(check_related_links(path, text))
        if inventory_text:
            issues.extend(check_inventory(path, inventory_text))

    if issues:
        for issue in issues:
            print(issue)
        print(f"\n{len(issues)} wiki QA issue(s) found.")
        return 1

    print(f"wiki QA passed for {len(targets)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
