#!/usr/bin/env python3
"""Fixture-based tests for the hidden Support QA validator."""

from __future__ import annotations

import base64
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import support_qa


PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)
PURPOSE = "Show the customer which control confirms the completed task."


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


class Fixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        repository = Path(__file__).resolve().parents[1]
        metadata = root / ".github/support-qa"
        (metadata / "schemas").mkdir(parents=True)
        shutil.copy2(
            repository / ".github/support-qa/schemas/document.schema.json",
            metadata / "schemas/document.schema.json",
        )
        shutil.copy2(
            repository / ".github/support-qa/schemas/screenshot.schema.json",
            metadata / "schemas/screenshot.schema.json",
        )
        policy = json.loads(
            (repository / ".github/support-qa/policy.json").read_text(encoding="utf-8")
        )
        policy["coverageBaseline"]["documents"]["expected"] = 4
        policy["coverageBaseline"]["screenshots"]["expected"] = 2
        policy["coverageBaseline"]["screenshots"]["referencedAssetsAtBaseline"] = 1
        policy["coverageBaseline"]["screenshots"]["publishedPlacementsAtBaseline"] = 1
        policy["coverageBaseline"]["screenshots"]["retainedUnreferencedAtBaseline"] = 1
        for rule in policy["language"]["discouragedWordRatchet"]:
            rule["maximumOccurrences"] = 0
            rule["maximumDocuments"] = 0
        write_json(metadata / "policy.json", policy)

        self.index = {
            "schemaVersion": 1,
            "home": {
                "source": "README.md",
                "title": "Support",
                "summary": "Friendly help",
                "featuredGroups": [],
                "topicDirectoryLabel": "Topics",
            },
            "navigation": {"guideFooter": {}},
            "topics": [
                {
                    "id": "topic",
                    "path": "topic",
                    "overview": "topic/README.md",
                    "title": "Topic",
                    "summary": "Topic help",
                    "groups": [
                        {
                            "id": "tasks",
                            "title": "Tasks",
                            "guides": [
                                {
                                    "id": "topic/guide",
                                    "source": "topic/guide.md",
                                    "title": "Guide",
                                    "summary": "Do a useful task",
                                }
                            ],
                        }
                    ],
                }
            ],
        }
        write_json(root / ".github/support-index.json", self.index)
        self.write(root / "README.md", "# Support\n")
        self.write(root / "topic/README.md", "# Topic\n")
        self.write(
            root / "topic/guide.md",
            "# Guide\n\n## Steps\n\n"
            "![Helpful task confirmation](../screenshots/topic/shot.png)\n",
        )
        self.write(root / "sample-files/practice/README.md", "# Practice Files\n")
        self.write(root / "AGENTS.md", "# Internal instructions\n")

        for name in ("shot.png", "retained.png"):
            path = root / "screenshots/topic" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(PNG_1X1)

        self.write_document_sidecar("README.md", "home", "support-home")
        self.write_document_sidecar("topic/README.md", "topic", "getting-started")
        self.write_document_sidecar(
            "topic/guide.md",
            "guide",
            "getting-started",
            screenshot_uses=[
                {
                    "file": "screenshots/topic/shot.png",
                    "section": "Steps",
                    "altText": "Helpful task confirmation",
                    "purpose": PURPOSE,
                }
            ],
        )
        self.write_document_sidecar(
            "sample-files/practice/README.md",
            "repository-reference",
            "practice-files",
            content_type="reference",
        )
        self.write_screenshot_sidecar(
            "screenshots/topic/shot.png",
            "referenced",
            uses=[
                {
                    "document": "topic/guide.md",
                    "section": "Steps",
                    "altText": "Helpful task confirmation",
                    "purpose": PURPOSE,
                }
            ],
        )
        self.write_screenshot_sidecar(
            "screenshots/topic/retained.png", "retained-unreferenced", uses=[]
        )
        self.write_review_baseline()

    @staticmethod
    def write(path: Path, value: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")

    def write_document_sidecar(
        self,
        source: str,
        role: str,
        product_area: str,
        *,
        screenshot_uses: list[dict[str, str]] | None = None,
        content_type: str = "task",
    ) -> Path:
        value = {
            "schemaVersion": 1,
            "source": source,
            "role": role,
            "objective": "Help a customer complete the documented task safely.",
            "audiences": ["bookkeeper"],
            "contentType": content_type,
            "toneProfile": "sprk-friendly-accountant-v1",
            "accountingRisk": "none",
            "productAreas": [product_area],
            "fileFacts": {
                "sha256": hashlib.sha256((self.root / source).read_bytes()).hexdigest()
            },
            "sourceEvidence": [],
            "walkthroughs": [],
            "screenshotUses": screenshot_uses or [],
            "verification": {
                "status": "needs-review",
                "reason": "The baseline metadata still requires a current product review.",
                "requiredChecks": ["objective", "tone"],
            },
        }
        path = self.root / ".github/support-qa/documents" / f"{source}.json"
        write_json(path, value)
        return path

    def write_screenshot_sidecar(
        self, file: str, usage_status: str, *, uses: list[dict[str, str]]
    ) -> Path:
        value = {
            "schemaVersion": 1,
            "file": file,
            "usageStatus": usage_status,
            "fileFacts": {
                "format": "png",
                "width": 1,
                "height": 1,
                "sha256": hashlib.sha256(PNG_1X1).hexdigest(),
            },
            "capturePlan": {
                "completeness": "review-required",
                "reason": "The existing image needs a reproducible capture plan.",
                "requiredDetails": ["capture-plan", "current-product-check"],
            },
            "uses": uses,
            "verification": {
                "status": "needs-review",
                "reason": "The existing image requires a current visual review.",
                "knownGaps": ["capture-provenance", "current-product-check"],
            },
        }
        if usage_status == "retained-unreferenced":
            value["retentionReason"] = "Existing public path retained until compatibility review."
        relative = Path(file).relative_to("screenshots")
        path = self.root / ".github/support-qa/screenshots" / f"{relative.as_posix()}.json"
        write_json(path, value)
        return path

    def write_review_baseline(self) -> None:
        documents = {
            path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in self.root.rglob("*.md")
            if path.name != "AGENTS.md" and ".github" not in path.parts
        }
        screenshots = {
            path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (self.root / "screenshots").rglob("*.png")
        }
        write_json(
            self.root / ".github/support-qa/review-baseline.json",
            {
                "schemaVersion": 1,
                "frozenAt": "2026-09-11",
                "documents": dict(sorted(documents.items())),
                "screenshots": dict(sorted(screenshots.items())),
            },
        )


class SupportQATest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.fixture = Fixture(self.root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_complete_fixture_passes(self) -> None:
        self.assertEqual([], support_qa.check_support_qa(self.root))

    def test_manual_schema_fallback_also_passes(self) -> None:
        with mock.patch.object(support_qa, "jsonschema", None):
            self.assertEqual([], support_qa.check_support_qa(self.root))

    def test_changed_needs_review_source_must_be_verified(self) -> None:
        self.fixture.write(self.root / "README.md", "# Support\n\nA new customer-facing sentence.\n")
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("source changed after its review baseline" in issue for issue in issues))

    def test_changed_needs_review_screenshot_must_be_verified(self) -> None:
        path = self.root / "screenshots/topic/shot.png"
        path.write_bytes(PNG_1X1 + b"changed")
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("source changed after its review baseline" in issue for issue in issues))
        self.assertTrue(any("fileFacts.sha256" in issue for issue in issues))

    def test_source_absent_from_review_baseline_must_be_verified(self) -> None:
        path = self.root / ".github/support-qa/review-baseline.json"
        value = json.loads(path.read_text())
        del value["documents"]["topic/guide.md"]
        write_json(path, value)
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("new source cannot use needs-review" in issue for issue in issues))

    def test_missing_sidecar_fails_exact_coverage(self) -> None:
        (self.root / ".github/support-qa/documents/topic/guide.md.json").unlink()
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("missing document sidecar" in issue for issue in issues))
        self.assertTrue(any("document sidecars: expected exactly 4, found 3" in issue for issue in issues))

    def test_file_facts_and_markdown_associations_are_checked(self) -> None:
        document_path = self.root / ".github/support-qa/documents/topic/guide.md.json"
        document = json.loads(document_path.read_text())
        document["screenshotUses"][0]["altText"] = "Incorrect alternate text"
        write_json(document_path, document)
        screenshot_path = self.root / ".github/support-qa/screenshots/topic/shot.png.json"
        screenshot = json.loads(screenshot_path.read_text())
        screenshot["fileFacts"]["sha256"] = "0" * 64
        write_json(screenshot_path, screenshot)
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("missing screenshotUse" in issue for issue in issues))
        self.assertTrue(any("fileFacts.sha256" in issue for issue in issues))

    def test_nearest_heading_and_reference_status_are_checked(self) -> None:
        document_path = self.root / ".github/support-qa/documents/topic/guide.md.json"
        document = json.loads(document_path.read_text())
        document["screenshotUses"][0]["section"] = "Wrong section"
        write_json(document_path, document)
        screenshot_path = self.root / ".github/support-qa/screenshots/topic/shot.png.json"
        screenshot = json.loads(screenshot_path.read_text())
        screenshot["usageStatus"] = "retained-unreferenced"
        screenshot["retentionReason"] = "Incorrectly retained despite a live Markdown placement."
        write_json(screenshot_path, screenshot)
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("section='Steps'" in issue for issue in issues))
        self.assertTrue(any("usageStatus must be 'referenced'" in issue for issue in issues))

    def test_duplicate_sidecar_identity_is_rejected(self) -> None:
        original = self.root / ".github/support-qa/documents/topic/guide.md.json"
        duplicate = self.root / ".github/support-qa/documents/topic/duplicate.md.json"
        write_json(duplicate, json.loads(original.read_text()))
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("duplicate source 'topic/guide.md'" in issue for issue in issues))

    def test_needs_review_can_record_completed_evidence_incrementally(self) -> None:
        path = self.root / ".github/support-qa/documents/topic/guide.md.json"
        value = json.loads(path.read_text())
        value["sourceEvidence"] = [
            {
                "kind": "frontend-source",
                "status": "verified",
                "repository": "WippData/SPRK_Desktop-frontend",
                "path": "src/features/example.tsx",
                "ref": "a" * 40,
                "supports": ["ui-labels"],
            }
        ]
        write_json(path, value)
        self.assertEqual([], support_qa.check_support_qa(self.root))

    def test_verified_screenshot_requires_complete_plan_and_provenance(self) -> None:
        path = self.root / ".github/support-qa/screenshots/topic/shot.png.json"
        value = json.loads(path.read_text())
        value["verification"] = {
            "status": "verified",
            "verifiedAt": "2026-09-11",
            "verifiedBy": "Reviewer",
            "expectedUiConfirmed": True,
            "purposeConfirmed": True,
        }
        write_json(path, value)
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("provenance" in issue for issue in issues))
        self.assertTrue(any("capturePlan" in issue or "too few items" in issue for issue in issues))

    def test_verified_high_risk_document_requires_full_evidence(self) -> None:
        path = self.root / ".github/support-qa/documents/topic/guide.md.json"
        value = json.loads(path.read_text())
        value["accountingRisk"] = "high"
        value["verification"] = {
            "status": "verified",
            "verifiedAt": "2026-09-11",
            "verifiedBy": "Reviewer",
            "objectiveMet": True,
            "toneReviewed": True,
        }
        value["sourceEvidence"] = [
            {
                "kind": "frontend-source",
                "status": "verified",
                "repository": "WippData/SPRK_Desktop-frontend",
                "path": "src/features/example.tsx",
                "ref": "a" * 40,
                "supports": ["ui-labels"],
            }
        ]
        write_json(path, value)
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("sourceEvidence" in issue or "walkthroughs" in issue for issue in issues))

    def test_language_and_publication_isolation_are_checked(self) -> None:
        self.fixture.write(
            self.root / "topic/guide.md",
            "# Guide\n\nThe backend workflow is described here.\n\n## Steps\n\n"
            "![Helpful task confirmation](../screenshots/topic/shot.png)\n",
        )
        index = json.loads((self.root / ".github/support-index.json").read_text())
        index["home"]["summary"] = ".github/support-qa must stay hidden"
        write_json(self.root / ".github/support-index.json", index)
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("hard-forbidden customer phrase: backend" in issue for issue in issues))
        self.assertTrue(any("language.workflow" in issue for issue in issues))
        self.assertTrue(any("hidden QA metadata" in issue for issue in issues))

    def test_discouraged_plural_counts_but_link_destination_does_not(self) -> None:
        self.fixture.write(
            self.root / "topic/guide.md",
            "# Guide\n\nThese workflows help [Open SPRK](https://example.invalid/state).\n\n"
            "## Steps\n\n![Helpful task confirmation](../screenshots/topic/shot.png)\n",
        )
        issues = support_qa.check_support_qa(self.root)
        self.assertTrue(any("language.workflow" in issue for issue in issues))
        self.assertFalse(any("language.state" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
