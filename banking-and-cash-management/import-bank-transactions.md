# Import Bank Transactions

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
3. In the upload area, click to choose a file or drag one file onto the drop zone. The Banking page currently accepts:
   - `CSV`
   - `XLSX`
   - `XLSM`
   - `OFX`
   - `QFX`
   - `QBO`
4. Review the import preview.
   - The preview title shows the parsed import type when SPRK detects one.
   - The preview shows how many rows were parsed before you confirm anything.
   - You can filter the preview by description, date, and transaction type if you want to inspect a subset of the imported rows.
5. If the money direction looks backwards, turn on `Swap spent/received` before confirming the preview.
6. Confirm the import preview.
7. Return to the `Pending` tab and review the imported transactions for the selected account.
8. Categorize and confirm the transactions you want posted to the general ledger.

## Expected Result

The imported rows are added to the selected account's pending bank register and are ready for review. Current general ledger impact as of 2026-05-21:

- Selecting the destination account does not post anything to the general ledger.
- Opening the preview and changing the `Swap spent/received` option do not post anything to the general ledger.
- Confirming the import preview only loads or updates pending bank transactions for later review.
- The general ledger is affected later, when each pending transaction is confirmed from the Banking workflow.

## Common Mistakes

- Importing while the wrong bank or credit card account is selected.
- Forgetting that SPRK will not let you import until an account is chosen.
- Skipping the preview and missing a spent-versus-received reversal issue.
- Treating imported rows as final postings rather than as pending items still waiting for review.
- Assuming closing the preview has the same effect as confirming it.

## Related Articles

- [Understand the banking page](./understand-the-banking-page.md)
- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Create and manage rules](./create-and-manage-rules.md)

## Info

- App sections: `banking`
- Last validated: 2026-05-21
- Screenshot status: `not-started`
