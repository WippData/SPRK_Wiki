# AP Review Workflow

![Bills list showing bill rows, statuses, and available bill actions](../screenshots/expenses-and-payables/bills-list-step-01.png)

Use this accounts payable review workflow to check vendors, bills, checks, payables aging, and expense detail before reporting.

## When To Use This

Use this workflow before month-end reporting, before paying vendors, or when payables or expense totals do not look right.

## Before You Start

- The correct company is active.
- Vendor records are set up.
- Bills, checks, and vendor payments for the period have been entered through the supported workflows.

## Steps

1. Review vendor records for duplicate or incomplete names.
2. Review vendor default expense accounts for recurring vendors.
3. Open the bills list and review open, paid, voided, or recently entered bills.
4. Confirm bills are coded to the right vendor, date, due date, expense account, and amount.
5. Review checks and payment records that should reduce vendor balances.
6. Run `Payables Aging` if available.
7. Run `Income Statement` and review expense totals for the period.
8. Run `General Ledger` or `Account Detail` when an expense or AP balance needs supporting detail.
9. Correct bill or payment issues in the payables workflow before using journal entries.
10. Use journal entries for accountant adjustments that do not belong to a vendor bill, check, or payment workflow.

## What Happens Next

AP review helps confirm that vendor balances, bill status, payment records, AP aging, and expense reporting agree before reports are finalized.

## If Something Looks Wrong

- Do not use a journal entry to clear a vendor balance before checking bill payment status.
- Do not treat a bank withdrawal as proof that the bill was paid correctly.
- Do not rely on payables aging until bills and payments have been entered.
- Do not apply broad vendor defaults without reviewing unusual purchases.
- Do not review AP without confirming the active company.

## Related

- [Manage vendors](./manage-vendors.md)
- [Set up vendor default expense accounts](./set-up-vendor-default-expense-accounts.md)
- [Create and manage bills](./create-and-manage-bills.md)
- [Work with checks](./work-with-checks.md)
- [Review common payables workflows](./review-common-payables-workflows.md)
- [Review financial results inside the product](../reports-and-financial-review/review-financial-results-inside-the-product.md)
