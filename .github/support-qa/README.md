# Support QA metadata

This directory contains internal QA evidence for SPRK Support. It is intentionally excluded from publishing and customer search.

## What is enforced now

- Every in-scope Markdown file and PNG has exactly one schema-valid sidecar.
- The sidecar path and identity match the source path.
- Markdown image placements match both sides of the document-to-screenshot relationship, including section, alt text, and purpose.
- PNG hashes and dimensions match the actual files.
- New or materially changed sources cannot remain `needs-review` after the frozen baseline. `.github/support-qa/review-baseline.json` is append-prohibited and exists only to let the original migration queue remain honest.
- Hard-forbidden internal language fails. Discouraged vocabulary can decrease but cannot exceed the baseline.

The baseline deliberately does not claim that existing prose or screenshots have been validated. Mechanically derived facts are recorded; unknown product evidence and capture history remain `needs-review`.

## Document review

Edit `.github/support-qa/documents/<document-path>.json`. Confirm the objective, audience, tone, content type, risk, and every screenshot purpose. Add evidence using immutable 40-character source refs and run the documented customer task in a current SPRK build.

A verified task or troubleshooting guide needs at least one passed walkthrough. Moderate-risk guidance also needs verified frontend and backend evidence. High-risk guidance additionally needs verified Accounting Contract evidence. Record evidence and walkthroughs as each check is completed, even while the document remains `needs-review`; only set `verification.status` to `verified` after its conditional schema requirements are complete.

## Screenshot review or recapture

Edit `.github/support-qa/screenshots/<path-below-screenshots>.json`. A complete capture plan records:

1. The app area, screen, and route.
2. Required starting data and other preconditions.
3. The sidebar, page, tab, menu, drawer, or modal path used to arrive there.
4. Every click, selection, entry, filter, or wait needed to create the state.
5. Whether the subject is a page, modal, drawer, table, report, menu, popover, form, confirmation, or another allowed type.
6. The exact state and UI labels, values, columns, or messages the image must show.
7. What the crop must include and exclude.
8. The safe test-data profile used for the capture.

After capture, record the app version, frontend and backend refs, runtime target, platform, viewport, data profile, capture method, and independent privacy review. This provenance can be saved while other checks are still open. Confirm every listed article use is visually relevant before setting the screenshot to `verified`. Update `fileFacts` after replacing a bitmap in place.

## Phased migration

Work one customer journey at a time. Verify its guides and shared screenshots together, then remove each item from the review queue by completing its evidence. Do not change validation dates for tone-only edits, and do not mark an old screenshot verified merely because it exists or decodes successfully.

Run:

```bash
python3 -m unittest scripts/test_support_qa.py
python3 scripts/support_qa.py
python3 scripts/wiki_qa.py --all
python3 scripts/screenshot_quality_check.py
```
