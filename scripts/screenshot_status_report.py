#!/usr/bin/env python3
"""Report the customer-guide screenshot review queue from support metadata."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / ".github" / "support-index.json"
MARKER = re.compile(r"<!-- Screenshot status: ([^>]+) -->")


def main() -> int:
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    guides = [
        guide
        for topic in index["topics"]
        for group in topic["groups"]
        for guide in group["guides"]
    ]
    current: list[str] = []
    review: list[str] = []
    missing: list[str] = []
    for guide in guides:
        source = guide["source"]
        text = (ROOT / source).read_text(encoding="utf-8")
        if "![" not in text:
            continue
        match = MARKER.search(text)
        if not match:
            missing.append(source)
        elif match.group(1).startswith("Current"):
            current.append(source)
        else:
            review.append(source)

    print(f"Current: {len(current)}")
    print(f"Review needed: {len(review)}")
    print(f"Missing status: {len(missing)}")
    if review:
        print("\nScreenshot review queue:")
        for source in review:
            print(f"- {source}")
    if missing:
        print("\nMissing status markers:")
        for source in missing:
            print(f"- {source}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
