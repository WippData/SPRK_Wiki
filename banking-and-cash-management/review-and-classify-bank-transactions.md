# Review and Classify Bank Transactions

<!-- Last validated: 2026-07-15 (SPRK 0.4.10, Demo Company) -->
<!-- Screenshot status: Current; related Banking reconciliation and rule-draft screenshots captured 2026-07-15 -->

Use this banking review front door to choose the right workflow before classifying, matching, confirming, transferring, or resolving bank activity.

![Banking actions strip showing Apply vendor or customer and the Vendor or Customer grid column](../screenshots/banking-and-cash-management/banking-filters-gl-account-step-01.png)

## Use This Page When

Banking review can create ledger entries, apply payments, clear checks, and affect later reconciliation. Start here when pending or confirmed bank activity needs a decision before you continue.

## Choose This Path If

| Goal | Use | Check First |
|---|---|---|
| Assign account, split, vendor, or customer details to pending rows | [Classify bank transactions](./classify-bank-transactions.md) | Selected bank account, pending row details, target account, split total, and party |
| Match money received or spent to a source document or check | [Match bank transactions](./match-bank-transactions.md) | Candidate invoice, bill, or check; party; date; amount; and difference |
| Review a bank-to-bank or bank-to-cash movement | [Review bank transfers](./review-bank-transfers.md) | Both accounts, amount, date, memo, candidate transfer, and reconciliation state |
| Repair the accounting link for a confirmed row | [Resolve confirmed bank transactions](./resolve-confirmed-bank-transactions.md) | Confirmed row, linked journal, reconciliation state, and supporting detail |
| Import new bank rows into pending review | [Import bank transactions](./import-bank-transactions.md) | Selected account, file columns, duplicates, and pending review state |
| Create or import rules for repeated patterns | [Create and manage rules](./create-and-manage-rules.md) | Rule scope, order, conditions, actions, and account resolution |

## Before You Commit

- Confirm the selected bank or credit card account before editing or confirming rows.
- Treat `Pending` as review state and `Categorized` as confirmed state.
- Confirming a bank row can create or link accounting activity.
- Matching from Banking can record invoice receipts, bill payments, or check clearing as part of confirmation.
- Transfer review can reuse an existing counterpart or create a separate transfer, so compare the candidate carefully.
- Resolving a confirmed row can change the accounting trail without returning the row to pending review.

## What Not To Assume

- A rule suggestion or vendor default does not mean the bank row has posted.
- A saved vendor default can prevent the same default-expense prompt from repeating for that vendor later in the same bulk-confirm run. Continue reviewing each row; prompt suppression is not confirmation.
- A row-level rule draft can begin with the full normalized description. Narrow it before saving when the text is too broad or too transaction-specific.
- Customer assignment is not the same thing as matching an invoice payment.
- Likely-duplicate warnings during import do not post, delete, or skip a transaction by themselves.
- Grid Edit draft changes are not the same thing as confirmation.
- Removing a GL link does not delete, unconfirm, or unreconcile the bank row.

## Practice And Examples

- Practice reference: [bank-review-classify-confirm.csv](../sample-files/practice/bank-review-classify-confirm.csv)

## Related

- [Choose bank and credit card accounts](./choose-bank-and-credit-card-accounts.md)
- [Understand the banking page](./understand-the-banking-page.md)
- [Use grid edit for bulk record maintenance](../dashboard-and-navigation/use-grid-edit-for-bulk-record-maintenance.md)
- [Start a reconciliation](../reconciliation/start-a-reconciliation.md)
