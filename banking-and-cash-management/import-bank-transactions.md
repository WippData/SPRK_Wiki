# Import Bank Transactions

![Bank transaction import template modal](../screenshots/banking-and-cash-management/bank-transaction-import-template-step-01.png)

Bring bank or credit card activity into SPRK from a supported file format, review the preview, and load the transactions into the pending queue for later confirmation.

## Purpose

Use this workflow when you have external bank or credit card activity in a file and want to load it into SPRK for review.

## Prerequisites

- The destination bank or credit card account exists in SPRK.
- You are signed in to SPRK and have an active company selected.
- You are ready to choose the specific bank or credit card account that should receive the import.
- Your file is one of the formats accepted by the Banking page.
- You are ready to review imported transactions before posting them.

## Steps

1. Open `Banking`.
2. Select the bank or credit card account that should receive the imported activity.
   - If no account is selected, SPRK keeps the importer disabled and prompts you to choose an account first.
   - If a default account opens automatically, confirm that it matches the account for the file you are about to import.
3. Choose `Import` in the page header, or use the upload area beside the account cards if you already have the file ready.
4. In the `Bank Transaction Import Template` modal, review the file guidance before you select a file:
   - Accepted formats are `.csv`, `.xlsx`, `.xlsm`, `.ofx`, `.qfx`, and `.qbo`.
   - Spreadsheet imports require `Date`, `Description`, and `Amount`.
   - Spreadsheet imports can also include `Debit`, `Credit`, `Check #`, and `Memo`.
   - `OFX`, `QFX`, and `QBO` files do not use the spreadsheet columns.
   - `Download Template` gives you a starter spreadsheet layout.
5. Choose `Import File`, then select one supported file.
6. Review the import preview.
   - The preview title shows the parsed import type when SPRK detects one.
   - The preview shows how many rows were parsed before you confirm anything.
   - The preview can show how many rows are selected for import before anything is added to `Pending`.
   - Rows that appear to match existing activity can show a likely-duplicate warning. Treat this as a review prompt, not as proof that the row is definitely a duplicate.
   - Use row-level `Skip` when a row should not be imported. Use `Restore` if you skipped a row and decide it should be included after all.
   - You can filter the preview by description, date, and transaction type if you want to inspect a subset of the imported rows.
7. If the money direction looks backwards, turn on `Swap spent/received` before confirming the preview.
8. Confirm the import preview.
9. Return to the `Pending` tab and review the imported transactions for the selected account.
10. Categorize and confirm the transactions you want posted to the general ledger.

## Expected Result

The imported rows are added to the selected account's pending bank register and are ready for review. Current general ledger impact as of 2026-06-05:

- Selecting the destination account does not post anything to the general ledger.
- Opening the preview and changing the `Swap spent/received` option do not post anything to the general ledger.
- Confirming the import preview only loads or updates selected, non-skipped rows as pending bank transactions for later review.
- The general ledger is affected later, when each pending transaction is confirmed from the Banking workflow.

## Common Mistakes

- Importing while the wrong bank or credit card account is selected.
- Forgetting that SPRK will not let you import until an account is chosen.
- Ignoring likely-duplicate warnings in the preview instead of comparing the row to existing bank activity.
- Forgetting that skipped preview rows are excluded from the import unless you restore them before confirming.
- Skipping the preview and missing a spent-versus-received reversal issue.
- Treating imported rows as final postings rather than as pending items still waiting for review.
- Assuming closing the preview has the same effect as confirming it.

## Related Articles

- [Choose bank and credit card accounts](./choose-bank-and-credit-card-accounts.md)
- [Understand the banking page](./understand-the-banking-page.md)
- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Create and manage rules](./create-and-manage-rules.md)

## Info

- App sections: `banking`
- Last validated: 2026-06-05
- Screenshot status: `captured`
