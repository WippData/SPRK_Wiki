#!/usr/bin/env python3
"""Lightweight QA checks for SPRK wiki Markdown.

By default this checks every public Markdown file. Pass explicit paths to
check a focused set. ``--all`` remains as an explicit alias for the default.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / ".private" / "wiki-page-inventory.md"

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
        if line.strip() != "## If Something Looks Wrong":
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

    for path in targets:
        text = read(path)
        issues.extend(check_banned_terms(path, text))
        issues.extend(check_troubleshooting_table(path, text))
        issues.extend(check_links(path, text))
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
