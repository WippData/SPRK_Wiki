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

## URL compatibility

Existing Markdown and image paths are public URLs. Do not rename, move, case-change, or delete them without explicit user permission. Prefer editing the existing article. When a genuinely new page is necessary, add it and link it from the relevant section index. If the user explicitly approves a future URL change, the same change must also preserve the old URL through a compatibility page or redirect.

## Validation dates

Add or update `<!-- Last validated against SPRK source: YYYY-MM-DD -->` only after checking the current owning source and end-to-end workflow. Tone-only edits do not earn a new validation date. Screenshot validation is separate: mark a screenshot current only after viewing or capturing the relevant state in the current app. Do not blanket-backfill dates.

## Required checks

Before handoff, run:

```bash
git diff --check
python3 scripts/wiki_qa.py
python3 scripts/screenshot_quality_check.py
```
