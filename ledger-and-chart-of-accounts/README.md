---
title: Ledger and Chart of Accounts
summary: Use the chart of accounts to organize account structure, record and review manual journal entries in the ledger, and understand which actions do or do not change the general ledger.
audience: End users
app_sections:
  - ledger
  - chart
workflow_type: reference
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/JournalEntries.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/ChartOfAccounts.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/journal.go
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/accounts.go
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/safe/journalEntry.go
last_validated: 2026-05-02
screenshot_status: not-started
owner: codex
---

## Purpose

Use this section when you need to set up or maintain your account list, record manual journal entries, move ledger data in or out of SPRK, or understand which ledger actions are audit-sensitive.

## Prerequisites

- You are signed in to SPRK.
- An active company is selected.
- You understand which accounts should be used before posting a manual journal entry or importing ledger data.

## Steps

1. Choose the workflow that matches your goal:
   - [Understand the chart of accounts structure](./understand-the-chart-of-accounts-structure.md)
   - [Record journal entries](./record-journal-entries.md)
   - [Understand ledger import and export behavior](./understand-ledger-import-and-export-behavior.md)
   - [Understand audit-sensitive ledger behavior](./understand-audit-sensitive-ledger-behavior.md)

## Expected Result

You can maintain account structure, create balanced journal entries, understand when imports or reversals affect the general ledger, and know which actions are display-only or export-only.

## Common Mistakes

- Treating account maintenance as if it posts journal entries. Account setup changes the available account list, not account balances.
- Importing ledger data before confirming account names or IDs line up with your company.
- Assuming every edit is allowed after an entry is saved. Journal edits depend on company rules, and reversals are handled as separate entries.

## Related Articles

- [Understand the chart of accounts structure](./understand-the-chart-of-accounts-structure.md)
- [Record journal entries](./record-journal-entries.md)
- [Understand ledger import and export behavior](./understand-ledger-import-and-export-behavior.md)
- [Understand audit-sensitive ledger behavior](./understand-audit-sensitive-ledger-behavior.md)
