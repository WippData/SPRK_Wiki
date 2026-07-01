# Review and Classify Bank Transactions

Categorize pending bank or credit card transactions, use splits or check matching when needed, and confirm the entries that should post to the general ledger.

![Banking actions strip showing Apply vendor or customer and the Vendor or Customer grid column](../screenshots/banking-and-cash-management/banking-filters-gl-account-step-01.png)

## When To Use This

Use this workflow when imported or manually entered bank activity needs review before SPRK posts it to the general ledger.

## Before You Start

- A bank or credit card account is available on the Banking page.
- The transaction already exists in the selected account as a pending row.
- The offset account or split accounts you want to use are available. Nonposting accounts and restricted control accounts may be visible in `Chart of Accounts` but omitted from posting-oriented Banking selectors.

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
6. If the transaction came from a file import, remember that likely-duplicate warnings appeared before the row entered `Pending`. Recheck any suspicious imported row before you categorize or confirm it.
7. For each transaction you want to review, confirm the basic details such as date, description, amount, and optional check number.
   - Imported party hints such as `Imported: <name>` mean the bank row still needs vendor or customer review.
8. Review any suggestion already shown on the row:
   - Some rows may already have a GL account/category suggestion from a rule.
   - If a selected vendor has a default expense account, SPRK can also fill the GL account/category automatically when no manual category, split, or rule already controls the row.
9. If needed, assign or change the optional party.
   - Current Banking party selectors can group choices under `Vendors` and `Customers`.
   - Money-out review usually points to vendors; money-in review can point to customers.
   - Assigning a customer from Banking is not the same thing as matching an invoice payment. Use `Match bank transaction` when the row should be applied to an open invoice.
10. In `GL Account`, choose the account that should receive the non-bank side of the entry.
   - If you are working directly in the review grid, the same choice may still appear under a `Category` column.
11. If one account is not enough, select `Split` and build the allocation:
   - Use `Percent` when the split should total exactly `100%`.
   - Use `Amount` when the split lines should total the full transaction amount.
   - Save the split only after the total is complete.
12. If a pending bank row should be matched to an open invoice, open bill, or existing check, use `Match bank transaction` when it is available.
   - Money-in rows can suggest open invoices.
   - Money-out rows can suggest open bills.
   - Eligible check rows can match an existing check.
   - Compare document type, candidate number, party name, date, due date when shown, open amount, bank amount, and difference before confirming.
   - Action labels describe the posting path: `Receive Payment & Confirm`, `Receive Partial & Confirm`, `Pay Bill & Confirm`, `Pay Partial & Confirm`, or `Match Check`.
   - Ambiguous exact matches can show a review warning instead of auto-selecting one candidate, and overpayments are not actionable from this path.
13. If the transaction should be tied only to an existing check from the older check-matching flow, use `Find Check` and match the transaction before you confirm it.
14. For bank-to-bank, bank-to-cash, or bank-to-credit-card pairings, look for transfer language rather than check or document matching language. SPRK labels those register-account pairings as `Transfer`.
15. Confirm the transaction:
   - Use the row-level primary action for one transaction.
   - Or select several rows, use the bulk account or party tools if helpful, then choose `Confirm Selected`.
   - In current bulk party workflows, the selector prompt can read `Apply vendor or customer`, and the button can read `Apply party`.
   - SPRK requires each selected row to have either a GL account/category, a saved split, or a matched check before it can confirm.
   - In the standard `Pending` table, use the checkbox column to choose rows for the bulk toolbar.
   - In Banking Grid Edit, use the row-number column when the build exposes row selection there; the Banking toolbar can then show selected-row actions such as `Confirm Selected`.
   - If selected rows have unapplied draft Grid Edit changes, the in-grid action can read `Confirm & Apply Selected`, which applies the draft edits before attempting confirmation.
16. Review the transaction after confirmation. It leaves `Pending` and appears under `Categorized`.
17. If the confirmed transaction later needs to be reversed, open the linked journal entry from `Reconcile` where the row shows an enabled `Journal` action.
18. Use Grid Edit on supported Banking tables when repeated classification cleanup will be faster than opening one row at a time:
   - Draft Grid Edit changes are not the same as confirmation.
   - Apply pending Grid Edit changes before you run Banking bulk actions such as applying an account, applying a party, deleting rows, or selecting categorized rows.
   - The Banking Grid Edit confirm flow can apply draft edits as part of `Confirm & Apply Selected`, but other bulk actions still expect the grid edits to be clean.
   - If SPRK blocks a bulk action while the changed-cell counter is still active, review the edits, choose `Apply Changes`, and then run the bulk action after the grid is clean.
   - Review the final rows carefully before confirming transactions.
19. If a transfer confirmation stops for review, compare the candidate transfer details before choosing:
   - `Use existing transfer` when the row is the missing counterpart to the existing transfer.
   - `Create separate transfer` when the nearby same-amount transfer is unrelated or risky to reuse.
   - Cancel if the candidate is already reconciled, belongs to another statement period, or does not match your source evidence.
20. If a confirmed row in `Categorized` needs its accounting link repaired, use `Resolve` on that confirmed row.
   - `Resolve GL link` can show the current linked journal, suggested existing GL lines, and a `Create GL transaction` path when the row has enough categorization to build a balanced entry.
   - Suggested GL lines are review candidates, not automatic matches. Compare account, amount, date, memo, and source context before linking.
   - `Remove link` removes the journal association from the bank row. It does not delete the confirmed bank row, unconfirm it, unreconcile it, or clear statement metadata.
   - `Create GL and link` uses the bank row details to create a linked journal only after the row has a valid target account or split.

## What Happens Next

The reviewed transaction is confirmed and removed from the pending queue.

- Changing a vendor or customer, changing `GL Account` or the grid's `Category` column, saving draft splits, and matching a check do not post to the general ledger by themselves.
- Confirming a transaction creates or links the journal-entry result for that bank transaction.
- `Match bank transaction` confirms eligible document payments only from pending, unreconciled, non-excluded rows that do not already have a linked journal entry, matched check, or linked payment.
- Invoice matching is for money-in transactions. Bill matching is for money-out transactions. Partial matching is allowed only when the bank amount is less than or equal to the document open balance.
- Linked journal entries can be opened and reversed from `Reconcile` when the row shows the `Journal` action.
- The selected bank or credit card account remains the bank-side line of the confirmed entry.
- For money received, SPRK debits the selected bank or credit card account and credits the chosen target account or split accounts.
- For money spent, SPRK credits the selected bank or credit card account and debits the chosen target account or split accounts.
- Split confirmations post the same bank-side line plus the offset split lines you saved.
- If the transaction was matched to a check first, confirming the bank transaction also clears the linked check.
- Matching to an invoice or bill from Banking records the related customer receipt or bill payment as part of the confirm path. It does not silently accept overpayments.
- Confirmed bank rows can carry either vendor or customer identity into linked journals and later review. A bank row does not need both party types.
- A row with saved categorization can be ready to confirm even if a transient draft category cell is blank in the current Grid Edit session. Review the visible saved row state before assuming it is uncategorized.
- Confirmed rows can later be resolved without returning them to `Pending` when the visible `Resolve` action is available.
- Removing a GL link preserves the bank row and its reconciled state. Creating or linking GL from `Resolve` changes the accounting trail, so review it like any other posting-sensitive correction.
- A later imported opposite side of a transfer can be adopted into an existing transfer or excluded as a duplicate counterpart instead of creating a second journal entry for the same transfer.
- Ambiguous transfer evidence can require an explicit transfer-review choice instead of silently adopting or changing an existing transfer.
- Likely-duplicate warnings during import do not post, delete, or skip a transaction by themselves. They are a pre-confirm review signal before the row reaches `Pending`.

## If Something Looks Wrong

- Confirming without selecting a category, saving a valid split, or matching the correct check.
- Using the wrong bank account card and then confirming a transaction into the wrong cash account.
- Assuming a likely-duplicate warning means SPRK has already removed or posted the imported row.
- Assuming a row suggestion from a rule or vendor setup means the transaction has already posted.
- Expecting a vendor default to override a manual GL account/category or saved split you already chose.
- Expecting an incomplete split total to save in the current split editor.
- Forgetting that a matched check still needs confirmation from the bank transaction workflow.
- Treating a bank-to-bank transfer as a document match. Register-account pairings use `Transfer` wording.
- Assuming transfer duplicate review depends only on matching description text. Linked transfer metadata can matter when SPRK recognizes a counterpart.
- Trying to confirm or bulk-update selected Banking rows before applying draft Grid Edit changes.
- Treating customer assignment as invoice matching. Customer assignment adds party context; invoice matching applies a payment to an open invoice.
- Using `Resolve` as though it were a pending-row categorization action. It belongs to confirmed rows that need GL-link review.
- Removing a GL link and expecting the bank row to disappear. The row stays confirmed unless you use a separate supported correction path.
- Reusing a transfer candidate without checking whether it is reconciled or already tied to different source evidence.

## Business Scenario: Classify, Transfer, And Confirm Bank Activity

Use this scenario to train bank reviewers on the difference between a draft classification, a confirmed banking post, and a bank-to-bank transfer.

- Sample files:
  - [03-bank-review-classify-confirm.csv](../sample-files/v1-validation/03-bank-review-classify-confirm.csv)
  - [04-bank-transfer-counterpart-adoption.csv](../sample-files/v1-validation/04-bank-transfer-counterpart-adoption.csv)
- Evidence:

![Banking grid with a draft category before applying changes](../screenshots/v1-validation/banking-grid-classification-draft.png)

![Banking grid after applying the classification and preparing to confirm](../screenshots/v1-validation/banking-grid-confirm-ready.png)

![Transfer row categorized to the savings account before confirmation](../screenshots/v1-validation/banking-transfer-category-draft.png)

![Confirmed transfer toast after posting the bank-to-bank transaction](../screenshots/v1-validation/banking-transfer-confirmed-toast.png)

The walkthrough confirmed that Grid Edit changes remain draft until applied, categorized rows can be confirmed in bulk, and transfer wording is visible when the offset account is another cash or bank account.

## Related

- [Choose bank and credit card accounts](./choose-bank-and-credit-card-accounts.md)
- [Understand the banking page](./understand-the-banking-page.md)
- [Create and manage rules](./create-and-manage-rules.md)
- [Import bank transactions](./import-bank-transactions.md)
- [Set up vendor default expense accounts](../expenses-and-payables/set-up-vendor-default-expense-accounts.md)
- [Edit linked ledger and bank activity](../ledger-and-chart-of-accounts/edit-linked-ledger-and-bank-activity.md)
- [Use grid edit for bulk record maintenance](../dashboard-and-navigation/use-grid-edit-for-bulk-record-maintenance.md)
