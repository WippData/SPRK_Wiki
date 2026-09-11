# SPRK Wiki Authoring Guide

This repository is the public help center for SPRK. Write for a business owner or bookkeeper who is looking at the app and wants a calm, practical guide from a friendly accountant. The root `README.md` is the canonical public SPRK Support homepage; keep it focused on customer goals and link it only to existing public help pages. This `AGENTS.md` file is contributor guidance, not a public help article; public-page inventories and QA ingestion must exclude it.

## Sources of truth

Check facts in this order:

1. `Accounting_Contract.md` in the SPRK workspace for accounting and audit behavior.
2. The current frontend for visible labels, page locations, available actions, and screen order.
3. The current backend for posting, matching, reconciliation, persistence, and correction behavior.
4. A current SPRK walkthrough and screenshot for what a user actually sees.
5. Existing wiki text only as historical context; it is not proof that a workflow is still correct.

Read the accounting contract before changing guidance about journals, invoices, bills, checks, payments, Banking, reconciliation, reports, imports, voids, or reversals. If the contract and current app differ, describe the current app accurately and flag the gap for product review. Do not invent a future workflow.

## Voice and screen directions

- Sound like a friendly accountant helping someone work through the screen.
- Start with the direct sidebar destination when one exists.
- Use the exact current screen label in backticks. Do not paraphrase button, field, drawer, modal, tab, menu, or status names.
- Explain the accounting result in plain language. Avoid engineering terms, internal implementation details, and vague assurances.
- Keep `Confirm` or `Verify` instructions only when they name a specific value, account, date, status, balance, or action the reader can see.
- Distinguish `Banking` work on pending rows from `Reconcile` work on confirmed activity.

## Screenshots

- Never fabricate or retouch a product state.
- Reuse an older screenshot only when the controls and workflow it teaches still look substantially the same.
- Replace an outdated screenshot in place when it serves the same article and purpose; preserving the file path preserves public links.
- Use a new, descriptive filename under the relevant `screenshots/` category only for a genuinely new view.
- Crop out Codex, the desktop, other apps, private company data, and unrelated window chrome. Run `python3 scripts/screenshot_quality_check.py` before handoff.
- Screenshot verification is image-level metadata under `.github/support-qa/screenshots/`, not an article-level HTML comment. Existing `Screenshot status` comments are legacy hints, not proof; remove them as each guide and its images are formally reviewed. New or unverified screenshots belong in the metadata review queue; run `python3 scripts/screenshot_status_report.py` to list it.
- Screenshot QA requires Pillow. If the default Python does not have it, install the tested version with `python3 -m pip install -r scripts/requirements-screenshots.txt` or use an existing Python environment with that version.

## Invisible QA metadata

Every public document, repository-reference Markdown file, and PNG under `screenshots/` must have one JSON sidecar under `.github/support-qa/`. These files are internal evidence records. They must never appear in the website, in-app help, customer search, or the publication allowlist.

- Document metadata lives at `.github/support-qa/documents/<document-path>.json`. It records the customer objective, intended audiences, content type, accounting risk, product areas, product-source evidence, walkthroughs, screenshot purposes, and verification decision.
- Screenshot metadata lives at `.github/support-qa/screenshots/<path-below-screenshots>.json`. It records immutable file facts, every article placement, the screenshot's instructional purpose, its capture recipe, the UI state it must show, product-version provenance, and privacy/relevance review.
- Do not infer verification. Existing content may remain `needs-review` only while its source file is unchanged from `.github/support-qa/review-baseline.json`. That baseline is append-prohibited. A new or materially changed document or screenshot must satisfy the full `verified` contract.
- A screenshot capture recipe must name the app area, screen and route; prerequisites; navigation path; exact clicks/selections/entries; subject type and state; UI labels or values expected in the image; crop requirements; and safe test-data profile.
- High-risk accounting guidance requires verified frontend source, backend source, `Accounting_Contract.md`, and a passed current-app walkthrough. Moderate-risk guidance requires frontend, backend, and walkthrough evidence.
- When a Markdown image is added, removed, moved to another section, or given new alt text, update both the document and screenshot sidecars. Shared screenshots list every placement and purpose.

See `.github/support-qa/README.md` and the JSON schemas for the authoring and phased-review process. Run `python3 scripts/support_qa.py` after every documentation or screenshot change.

## URL compatibility

Existing Markdown and image paths are public URLs. Do not rename, move, case-change, or delete them without explicit user permission. Prefer editing the existing article. When a genuinely new page is necessary, add it and link it from the relevant section index. If the user explicitly approves a future URL change, the same change must also preserve the old URL through a compatibility page or redirect.

## Support index metadata

`.github/support-index.json` is the strict publication allowlist and shared navigation contract for the website and in-app help. It owns topic and guide order, customer-facing labels and summaries, search aliases, visibility, homepage fallback groups, and generated guide-footer behavior. Array order is display order. Keep stable guide IDs equal to the source path without `.md`, and do not add a guide to the website or in-app help unless it is listed in this file.

`.github/support-index.schema.json` documents the supported contract. Topic visibility supports `website`, `inApp`, `search`, and `topicDirectory`; guide visibility supports `website`, `inApp`, `search`, and `topicIndex`. Omitted visibility values mean visible. Authored `Related` sections remain part of each Markdown guide; the shared site footer may add previous/next, topic, home, and contact links without replacing those article-specific links.

The root `README.md` is the readable fallback for the support homepage. Its featured headings and guide links must match `home.featuredGroups` exactly. Topic `README.md` files are readable fallbacks for the topic pages. The practice-file README is for direct repository use and stays outside publication metadata, navigation, and search. Individual practice files remain reachable from the guides that explain them.

## Validation dates

Add or update `<!-- Last validated against SPRK source: YYYY-MM-DD -->` only after checking the current owning source and end-to-end workflow. Tone-only edits do not earn a new validation date. Screenshot validation is separate: mark a screenshot current only after viewing or capturing the relevant state in the current app. Do not blanket-backfill dates.

## Required checks

Before handoff, run:

```bash
git diff --check
python3 -m unittest scripts/test_support_qa.py
python3 scripts/support_qa.py
python3 scripts/wiki_qa.py
python3 scripts/screenshot_quality_check.py
python3 scripts/screenshot_status_report.py
```
