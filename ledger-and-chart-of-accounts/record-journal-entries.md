---
title: Record Journal Entries
summary: Create balanced manual journal entries in the `Ledger` page, save reusable templates when needed, and understand how posting affects the general ledger.
audience: End users
app_sections:
  - ledger
workflow_type: daily-ops
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/JournalEntries.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/journal.go
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/safe/journalEntry.go
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/settings/howTo.ts
last_validated: 2026-05-02
screenshot_status: not-started
owner: codex
---

## Purpose

Use this workflow when you need to record a manual journal entry directly in the ledger.

## Prerequisites

- An active company is selected.
- The accounts you need already exist in `Chart of Accounts`.
- You know the posting date, memo, and debit and credit lines you want to record.

## Steps

1. Open `Ledger`.
2. Select `New`, or use the `Create from Template` menu if you already have a saved journal-entry template.
3. Enter the journal header details, including the date and memo.
4. Add each journal line with the correct account and amount.
5. If your company uses dimensions or classes, complete those fields on the related lines.
6. Confirm the entry is balanced before saving:
   - every line must use either debit or credit, not both
   - totals must match before the save action is allowed
7. Select `Create` to post the entry.
8. If you expect to reuse the same layout later, use the save-template option from the journal entry drawer.
9. Review the new entry in the ledger table and use search or filters to find it again later.

## Expected Result

A balanced journal entry is posted to the ledger and appears in the journal-entry list. Current general ledger impact as of 2026-05-02:

- Saving a manual journal entry creates a new journal entry record and posts each entered debit and credit line to the general ledger.
- SPRK blocks unbalanced entries from being saved.
- If the entry is off by a very small rounding amount within the current tolerance, SPRK can auto-adjust one line and note that adjustment in the memo before saving.

## Common Mistakes

- Trying to save an entry when debit and credit totals do not match.
- Entering both debit and credit on the same line.
- Assuming the ledger page is only for review. In the current product it is also the manual journal-entry posting page.

## Related Articles

- [Understand the chart of accounts structure](./understand-the-chart-of-accounts-structure.md)
- [Understand ledger import and export behavior](./understand-ledger-import-and-export-behavior.md)
- [Understand audit-sensitive ledger behavior](./understand-audit-sensitive-ledger-behavior.md)
