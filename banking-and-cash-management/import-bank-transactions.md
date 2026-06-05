# Import Bank Transactions

Bring bank or credit card activity into SPRK from a supported file format, review duplicate warnings in the preview, and load only the selected rows into the pending queue for later confirmation.

## Purpose

Use this workflow when you have external bank or credit card activity in a file and want to load it into SPRK for review.

## Prerequisites

- The destination bank or credit card account exists in SPRK.
- You are signed in to SPRK and have an active company selected.
- You are ready to choose the specific bank or credit card account that should receive the import.
- Your file is one of the formats accepted by the Banking page: `.csv`, `.xlsx`, `.xlsm`, `.ofx`, `.qfx`, or `.qbo`.
- You are ready to review imported transactions before posting them.

## Steps

1. Open `Banking`.
2. Select the bank or credit card account that should receive the imported activity.
   - If no account is selected, SPRK keeps the importer disabled and prompts you to choose an account first.
   - If a default account opens automatically, confirm that it matches the account for the file you are about to import.
3. Choose how to start the import:
   - Use the header `Import` action to open the `Bank Transaction Import Template` modal.
   - Or use the upload area beside the account cards to click or drag one supported file directly.
4. In the template modal, review the file guidance before you choose `Import File`:
   - Accepted formats are `.csv`, `.xlsx`, `.xlsm`, `.ofx`, `.qfx`, and `.qbo`.
   - Spreadsheet-style imports use required columns `Date`, `Description`, and `Amount`.
   - Recommended spreadsheet columns are `Debit`, `Credit`, `Check #`, and `Memo`.
   - `OFX`, `QFX`, and `QBO` files do not use spreadsheet columns.
   - `Download Template` gives you a starter spreadsheet layout when you do not already have a prepared file.
5. Select the import file.
6. Review the import preview before confirming anything.
   - The preview title shows the parsed import type when SPRK detects one.
   - The preview shows how many rows were parsed and how many rows are currently selected for import.
   - Rows that appear to match existing activity in the selected account can be marked `Possible duplicate`.
   - Rows that are ready to import can be marked `Ready`.
   - Rows you exclude from the batch can be marked `Skipped`.
   - You can filter the preview by description, date, and transaction type if you want to inspect a subset of the imported rows.
7. Use row-level review controls before confirming the preview:
   - Choose `Skip` for a row you do not want to add to pending review.
   - Choose `Restore` if you skipped a row and decide to include it after all.
   - Watch the selected-row count so you know how many non-skipped rows will be imported.
8. If the money direction looks backwards, turn on `Swap spent/received` before confirming the preview.
9. Confirm the import preview.
10. Return to the `Pending` tab and review the imported transactions for the selected account.
11. Categorize and confirm the transactions you want posted to the general ledger.

## Expected Result

The imported rows are added to the selected account's pending bank register and are ready for review. Current general ledger impact as of 2026-05-21:

- Selecting the destination account does not post anything to the general ledger.
- Opening the preview and changing the `Swap spent/received` option do not post anything to the general ledger.
- Confirming the import preview only loads or updates the selected, non-skipped rows as pending bank transactions for later review.
- The general ledger is affected later, when each pending transaction is confirmed from the Banking workflow.

## Common Mistakes

- Importing while the wrong bank or credit card account is selected.
- Forgetting that SPRK will not let you import until an account is chosen.
- Skipping the preview and missing a spent-versus-received reversal issue.
- Ignoring a `Possible duplicate` warning without checking whether the row already exists in the selected account.
- Assuming skipped rows will still be added to `Pending`.
- Treating imported rows as final postings rather than as pending items still waiting for review.
- Assuming closing the preview has the same effect as confirming it.

## Related Articles

- [Choose bank and credit card accounts](./choose-bank-and-credit-card-accounts.md)
- [Understand the banking page](./understand-the-banking-page.md)
- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Create and manage rules](./create-and-manage-rules.md)

## Info

- App sections: `banking`
- Last validated: 2026-06-04
- Screenshot status: `blocked`
