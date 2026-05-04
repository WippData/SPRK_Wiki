---
title: Import Bank Transactions
summary: Bring bank or credit card activity into SPRK from a supported file format, review the preview, and load the transactions into the pending queue for later confirmation.
audience: End users
app_sections:
  - banking
workflow_type: daily-ops
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Banking.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/bank/hooks.ts
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/bank.go
last_validated: 2026-05-02
screenshot_status: not-started
owner: codex
---

## Purpose

Use this workflow when you have external bank or credit card activity in a file and want to load it into SPRK for review.

## Prerequisites

- The destination bank or credit card account exists in SPRK.
- Your file is one of the formats accepted by the Banking page.
- You are ready to review imported transactions before posting them.

## Steps

1. Open `Banking`.
2. Select the bank or credit card account that should receive the imported activity.
3. In the upload area, choose or drop one file. The Banking page currently accepts:
   - `CSV`
   - `XLSX`
   - `XLSM`
   - `OFX`
   - `QFX`
   - `QBO`
4. Review the import preview.
5. If the preview indicates the sign should be reversed, use the reverse option before confirming the import.
6. Confirm the import preview.
7. Return to the `Pending` tab and review the imported transactions.
8. Categorize and confirm the transactions you want posted to the general ledger.

## Expected Result

The imported rows are added to the selected account's pending bank register and are ready for review. Current general ledger impact as of 2026-05-02:

- Importing a file does not create a journal entry by itself.
- Confirming the import preview only loads or updates pending bank transactions.
- The general ledger is affected later, when each pending transaction is confirmed from the Banking workflow.

## Common Mistakes

- Importing into the wrong selected bank or credit card account.
- Skipping the preview and missing a sign reversal issue.
- Treating imported rows as final posting rather than as pending items still waiting for review.

## Related Articles

- [Understand the banking page](./understand-the-banking-page.md)
- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Create and manage rules](./create-and-manage-rules.md)
