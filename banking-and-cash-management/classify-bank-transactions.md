# Classify Bank Transactions

Assign account, split, and party details to pending bank or credit card rows before confirming them.

![Banking actions strip showing Apply vendor or customer and the Vendor or Customer grid column](../screenshots/banking-and-cash-management/banking-filters-gl-account-step-01.png)

## When To Use This

- Imported or manually entered bank activity is waiting in `Pending`.
- A row needs a GL account/category, split, vendor, or customer before confirmation.
- You need to confirm one or more banking rows into the general ledger.

## Before You Start

- Select the correct bank or credit card account.
- Stay on the `Pending` tab.
- Confirm the row date, description, amount, and optional check number.
- Make sure the offset account or split accounts you want to use are available. Nonposting accounts and restricted control accounts may be visible in `Chart of Accounts` but omitted from posting-oriented Banking selectors.

## Steps

1. Open `Banking`.
2. Select the bank or credit card account you want to review.
3. Confirm that `Pending` and `Categorized` reflect the selected account only.
4. Filter the list if needed by transaction type, description, amount, date, GL account/category, rule status, or class values when dimensions are enabled.
5. Review any likely-duplicate or imported-party context before classifying the row.
6. Review suggestions already shown on the row:
   - Rule suggestions can fill a GL account/category.
   - Vendor defaults can fill the GL account/category when no manual category, split, or rule already controls the row.
7. If needed, assign or change the optional party.
   - Banking party selectors can group choices under `Vendors` and `Customers`.
   - Money-out review usually points to vendors.
   - Money-in review can point to customers.
   - Customer assignment is not the same thing as invoice matching.
8. In `GL Account`, choose the account that should receive the non-bank side of the entry.
   - If you are working directly in the review grid, the same choice may appear under `Category`.
9. If one account is not enough, select `Split` and build the allocation:
   - Use `Percent` when the split should total exactly `100%`.
   - Use `Amount` when split lines should total the full transaction amount.
   - Save the split only after the total is complete.
10. Confirm the transaction:
    - Use the row-level primary action for one transaction.
    - Or select several rows, use bulk account or party tools if helpful, then choose `Confirm Selected`.
    - In the standard `Pending` table, use the checkbox column to choose rows for the bulk toolbar.
    - In Banking Grid Edit, use the row-number column when the build exposes row selection there.
11. Review the transaction after confirmation. It leaves `Pending` and appears under `Categorized`.

## What Happens When You Confirm

Changing a vendor or customer, changing `GL Account` or `Category`, and saving draft splits do not post by themselves. Confirming a bank transaction creates or links the journal-entry result for that row. The selected bank or credit card account remains the bank-side line of the confirmed entry.

For money received, SPRK debits the selected bank or credit card account and credits the chosen target account or split accounts. For money spent, SPRK credits the selected bank or credit card account and debits the chosen target account or split accounts.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| The row cannot be confirmed | Whether it has a GL account/category, saved split, or matched check | Complete the missing classification before confirming |
| A rule suggestion appears | Whether it is only a suggestion | Review the row before confirming |
| A vendor default filled the category | Whether a manual category, split, or rule should control the row instead | Review the saved row state before confirming |
| A split will not save | Whether percent or amount lines total correctly | Complete the split total before saving |
| Selected rows will not confirm | Whether Grid Edit changes are still pending | Apply or discard draft grid changes before the bulk action |

## Practice And Examples

- Practice reference: [bank-review-classify-confirm.csv](../sample-files/practice/bank-review-classify-confirm.csv)

## Related

- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Match bank transactions](./match-bank-transactions.md)
- [Review bank transfers](./review-bank-transfers.md)
- [Create and manage rules](./create-and-manage-rules.md)
- [Use grid edit for bulk record maintenance](../dashboard-and-navigation/use-grid-edit-for-bulk-record-maintenance.md)
