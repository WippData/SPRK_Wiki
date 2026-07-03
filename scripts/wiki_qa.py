#!/usr/bin/env python3
"""Lightweight QA checks for SPRK wiki Markdown.

By default this checks changed public Markdown files. Pass explicit paths to
check a focused set, or use --all to check every public Markdown file.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


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
        target_path = target.split("#", 1)[0]
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
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
    return issues


def should_skip_link(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("tel:")
        or lowered.startswith("#")
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
        targets = changed_markdown_files()

    inventory_text = read(INVENTORY) if INVENTORY.exists() else ""
    issues: list[str] = []

    for path in targets:
        text = read(path)
        issues.extend(check_banned_terms(path, text))
        issues.extend(check_troubleshooting_table(path, text))
        issues.extend(check_links(path, text))
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
