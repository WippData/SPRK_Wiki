# Find the Right Payables Guide

<!-- Screenshot status: Review needed -->

This address is kept for existing bookmarks. Use [Choose a bill task](./create-and-manage-bills.md) for bill entry, payment, import, matching, or correction, or [Review bills and vendor balances](./ap-review-workflow.md) for period-end review.

![Bills list showing payable balances and payment actions](../screenshots/expenses-and-payables/bills-list-step-01.png)

## Start here

Choose the task below if you need a more specific guide.

## Choose a payables task

| Goal | Use | Check First |
|---|---|---|
| Add or maintain the payee | [Manage vendors](./manage-vendors.md) | Vendor name, active status, address, and default expense account |
| Set reusable vendor account defaults | [Set up vendor default expense accounts](./set-up-vendor-default-expense-accounts.md) | Whether the default account fits future purchases |
| Enter a vendor bill | [Create bills](./create-bills.md) | Vendor, `Pay from`, line accounts, due date, and status |
| Record a payment on an open bill | [Record bill payments](./record-bill-payments.md) | Bill balance, payment amount, `Pay from`, and bank-match risk |
| Import grouped bill rows | [Import bills](./import-bills.md) | Vendor names, bill numbers, line accounts, and `Pay from` routing |
| Match a bank withdrawal to a bill | [Match bank transactions](../banking-and-cash-management/match-bank-transactions.md) | Pending bank row, open bill, vendor, amount, date, and difference |
| Review or correct a posted bill | [Void or correct bills](./void-or-correct-bills.md) | Bill status, balance, active payments, linked journals, and reversal date |
| Maintain check tracking | [Work with checks](./work-with-checks.md) | Whether the check page is visible and whether the check belongs to reconciliation work |

## Before You Commit

- Choose an Accounts Payable control account in `Pay from` when the bill should stay open until payment.
- Choose a cash, bank, or credit-card settlement account only for a paid-now bill.
- Review line-level bill accounts before opening or importing bills.
- Use bill payment workflows to reduce open vendor balances.
- Review payment history and linked journals before voiding or correcting a bill.

## What Not To Assume

- Vendor setup, bill entry, bill payment, check tracking, and banking match workflows do not create the same accounting result.
- A vendor default expense account does not remove the need to review bill lines.
- Linked journal review is not deletion or unposting.
- Voiding a bill preserves the bill and creates reversal history.
- Not every payable record supports the same correction action; use the action SPRK shows for that record.

## Practice and examples

- Practice file: [bill-void-correction-boundary.csv](../sample-files/practice/bill-void-correction-boundary.csv)

## Related

- [Create and manage bills](./create-and-manage-bills.md)
- [Review document payment history and linked journals](../ledger-and-chart-of-accounts/review-document-payment-history-and-linked-journals.md)
- [Common accountant corrections](../ledger-and-chart-of-accounts/common-accountant-corrections.md)
