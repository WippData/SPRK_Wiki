#!/usr/bin/env python3
"""Report the image-level screenshot review queue from hidden QA metadata."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METADATA = ROOT / ".github" / "support-qa" / "screenshots"


def main() -> int:
    verified: list[str] = []
    review: list[str] = []
    retained: list[str] = []
    invalid: list[str] = []
    for path in sorted(METADATA.rglob("*.json")):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            invalid.append(path.relative_to(ROOT).as_posix())
            continue
        source = record.get("file")
        status = record.get("verification", {}).get("status")
        if not isinstance(source, str) or status not in {"verified", "needs-review"}:
            invalid.append(path.relative_to(ROOT).as_posix())
            continue
        if record.get("usageStatus") == "retained-unreferenced":
            retained.append(source)
        if status == "verified":
            verified.append(source)
        else:
            review.append(source)

    print(f"Verified screenshots: {len(verified)}")
    print(f"Review needed: {len(review)}")
    print(f"Retained but unreferenced: {len(retained)}")
    print(f"Invalid metadata records: {len(invalid)}")
    if review:
        print("\nScreenshot review queue:")
        for source in sorted(review):
            print(f"- {source}")
    if invalid:
        print("\nInvalid screenshot metadata:")
        for source in sorted(invalid):
            print(f"- {source}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
