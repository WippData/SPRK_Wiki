# Review and Classify Bank Transactions

Categorize pending bank or credit card transactions, use splits or check matching when needed, and confirm the entries that should post to the general ledger.

## Purpose

Use this workflow when imported or manually entered bank activity needs review before SPRK posts it to the general ledger.

## Prerequisites

- A bank or credit card account is available on the Banking page.
- The transaction already exists in the selected account as a pending row.
- The offset account or split accounts you want to use are available.

## Steps

1. Open `Banking`.
2. Select the bank or credit card account you want to review.
3. Stay on the `Pending` tab.
4. Filter the transaction list if needed by description, amount, date, amount type, category, or rule status.
5. For each transaction you want to review, confirm the basic details such as date, description, amount, and optional check number.
6. If needed, assign an optional `Vendor`.
7. In `Categorize To`, choose the account that should receive the non-bank side of the entry.
8. If one account is not enough, select `Split` and build the allocation:
   - Use `%` style splits when the transaction should be distributed by percentage.
   - Use amount-based splits when you know the fixed amounts.
   - If amount-based splits do not cover the full transaction, SPRK requires a balance account for the remainder.
9. If the transaction should be tied to an existing check, use `Find Check` and match the transaction before you confirm it.
10. Confirm the transaction:
   - Use the row-level primary action for one transaction.
   - Or select several rows, use `Apply to selected` if helpful, then choose `Confirm selected`.
11. Review the transaction after confirmation. It leaves `Pending` and appears under `Categorized`.

## Expected Result

The reviewed transaction is confirmed and removed from the pending queue. Current general ledger impact as of 2026-05-02:

- Confirming a transaction creates a journal entry linked to that bank transaction.
- The selected bank or credit card account is always the bank-side line of the entry.
- For money received, SPRK debits the selected bank or credit card account and credits the chosen target account or split accounts.
- For money spent, SPRK credits the selected bank or credit card account and debits the chosen target account or split accounts.
- Split confirmations post the same bank-side line plus multiple offset lines, with amount splits using the balance account for any remainder.
- Matching a transaction to a check does not post the ledger by itself. When you confirm the matched bank transaction, SPRK also marks the linked check as cleared.

## Common Mistakes

- Confirming without selecting a category or valid split.
- Using the wrong bank account card and then confirming a transaction into the wrong cash account.
- Assuming vendor assignment changes the account distribution. Vendor assignment is separate from the chosen offset account.
- Forgetting that a matched check still needs confirmation from the bank transaction workflow.

## Related Articles

- [Understand the banking page](./understand-the-banking-page.md)
- [Create and manage rules](./create-and-manage-rules.md)
- [Import bank transactions](./import-bank-transactions.md)

## Info

- App sections: `banking`
- Last validated: 2026-05-02
- Screenshot status: `not-started`
