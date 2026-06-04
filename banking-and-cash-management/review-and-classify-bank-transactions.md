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
   - If a default account opens automatically, confirm that it is the account you meant to review before you edit or confirm transactions.
3. Stay on the `Pending` tab.
4. Confirm that the register belongs to the account you selected:
   - `Pending` and `Categorized` both reflect the selected bank or credit card account only.
   - Switching to another account changes which register you are reviewing.
5. Filter the transaction list if needed:
   - Use `All`, `Expenses`, or `Deposits` to narrow the transaction type.
   - Use the other filters for description, amount, date, GL account/category, rule status, or class values when dimensions are enabled.
6. For each transaction you want to review, confirm the basic details such as date, description, amount, and optional check number.
7. Review any suggestion already shown on the row:
   - Some rows may already have a GL account/category suggestion from a rule.
   - If a selected vendor has a default expense account, SPRK can also fill the GL account/category automatically when no manual category, split, or rule already controls the row.
8. If needed, assign or change the optional `Vendor`.
9. In `GL Account`, choose the account that should receive the non-bank side of the entry.
   - If you are working directly in the review grid, the same choice may still appear under a `Category` column.
10. If one account is not enough, select `Split` and build the allocation:
   - Use `Percent` when the split should total exactly `100%`.
   - Use `Amount` when the split lines should total the full transaction amount.
   - Save the split only after the total is complete.
11. If the transaction should be tied to an existing check, use `Find Check` and match the transaction before you confirm it.
12. Confirm the transaction:
   - Use the row-level primary action for one transaction.
   - Or select several rows, use the bulk account or vendor tools if helpful, then choose `Confirm selected`.
   - SPRK requires each selected row to have either a GL account/category, a saved split, or a matched check before it can confirm.
13. Review the transaction after confirmation. It leaves `Pending` and appears under `Categorized`.
14. If the confirmed transaction later needs to be reversed, open the linked journal entry from `Reconcile` where the row shows an enabled `Journal` action.
15. Use Grid Edit on supported Banking tables when repeated classification cleanup will be faster than opening one row at a time, but review the final rows carefully before confirming transactions.

## Expected Result

The reviewed transaction is confirmed and removed from the pending queue. Current general ledger impact as of 2026-05-29:

- Changing a vendor, changing `GL Account` or the grid's `Category` column, saving draft splits, and matching a check do not post to the general ledger by themselves.
- Confirming a transaction creates or links the journal-entry result for that bank transaction.
- Linked journal entries can be opened and reversed from `Reconcile` when the row shows the `Journal` action.
- The selected bank or credit card account remains the bank-side line of the confirmed entry.
- For money received, SPRK debits the selected bank or credit card account and credits the chosen target account or split accounts.
- For money spent, SPRK credits the selected bank or credit card account and debits the chosen target account or split accounts.
- Split confirmations post the same bank-side line plus the offset split lines you saved.
- If the transaction was matched to a check first, confirming the bank transaction also clears the linked check.

## Common Mistakes

- Confirming without selecting a category, saving a valid split, or matching the correct check.
- Using the wrong bank account card and then confirming a transaction into the wrong cash account.
- Assuming a row suggestion from a rule or vendor setup means the transaction has already posted.
- Expecting a vendor default to override a manual GL account/category or saved split you already chose.
- Expecting an incomplete split total to save in the current split editor.
- Forgetting that a matched check still needs confirmation from the bank transaction workflow.

## Related Articles

- [Choose bank and credit card accounts](./choose-bank-and-credit-card-accounts.md)
- [Understand the banking page](./understand-the-banking-page.md)
- [Create and manage rules](./create-and-manage-rules.md)
- [Import bank transactions](./import-bank-transactions.md)
- [Set up vendor default expense accounts](../expenses-and-payables/set-up-vendor-default-expense-accounts.md)
- [Edit linked ledger and bank activity](../ledger-and-chart-of-accounts/edit-linked-ledger-and-bank-activity.md)
- [Use grid edit for bulk record maintenance](../dashboard-and-navigation/use-grid-edit-for-bulk-record-maintenance.md)

## Info

- App sections: `banking`
- Last validated: 2026-06-04
- Screenshot status: `blocked`
