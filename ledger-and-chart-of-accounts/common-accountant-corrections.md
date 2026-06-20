# Common Accountant Corrections

![New journal entry drawer showing date, memo, account lines, debit and credit columns, totals, and reversing-entry controls](../screenshots/ledger-and-chart-of-accounts/new-journal-entry-drawer-step-01.png)

Use this page to choose the right correction path when a transaction has the wrong account, date, customer, vendor, payment status, or posting method.

## When To Use This

Use this workflow when review work finds something that needs to be fixed and you need to decide whether to edit the source record, reclassify a bank transaction, reverse a journal entry, or create a new adjusting entry.

## Before You Start

- The correct company is active.
- You know the record or balance that looks wrong.
- You have reviewed the supporting transaction before changing the ledger.
- You know whether the period is still open for normal edits.

## Correction Paths

| Situation | Start Here | Usual Correction |
| --- | --- | --- |
| Bank transaction uses the wrong expense or income account | `Banking` or linked bank detail | Edit the bank classification if the workflow allows it, or correct through the linked source entry |
| Invoice uses the wrong customer, item, amount, or payment status | `Invoices` | Correct the invoice or payment workflow instead of posting a standalone journal first |
| Bill uses the wrong vendor, account, amount, or payment status | `Bills` | Correct the bill or payment workflow where available |
| Check needs review | `Checks` | Edit or void through the check workflow when available |
| Manual journal entry was posted in error | `Ledger` | Reverse the journal or post a correcting journal depending on the situation |
| Month-end accrual should unwind next period | `Ledger` | Use a reversing journal entry |
| Account balance looks wrong on a report | `Reports` drilldown | Review supporting detail before choosing the correction workflow |
| Source data was imported incorrectly | Import workflow and affected records | Review import results, then correct through source pages or support guidance |

## Steps

1. Start from the report, list, or transaction where the issue was found.
2. Drill into supporting detail before posting a correction.
3. Identify the original source workflow.
   - Invoice and payment issues usually belong in receivables workflows.
   - Bill, vendor, and check issues usually belong in payables workflows.
   - Bank classification issues usually belong in banking.
   - Accountant adjustments and accruals usually belong in journal entries.
4. Confirm whether the transaction has been reconciled, paid, voided, or linked to another record.
5. Use reversal when you need to preserve the original posting and create an offsetting entry.
6. Use a correcting journal entry when the adjustment does not belong to a customer, vendor, invoice, bill, payment, or bank transaction workflow.
7. Rerun the relevant report after the correction.
8. Document the reason in the memo, description, or support notes your firm uses.

## What Happens Next

The correction should live in the workflow that best explains the accounting event. This keeps AR, AP, banking, reconciliation, and ledger reports easier to review later.

## If Something Looks Wrong

- Do not use a journal entry to fix an invoice or bill issue until you have reviewed the source workflow.
- Do not edit or exclude reconciled bank activity without understanding the reconciliation impact.
- Do not delete history to make a report look right.
- Do not reverse an entry twice.
- Do not correct the same issue in both the source workflow and a journal entry unless that is intentional.

## Related

- [When to use journal entries vs source forms](./when-to-use-journal-entries-vs-source-forms.md)
- [Record journal entries](./record-journal-entries.md)
- [Understand audit-sensitive ledger behavior](./understand-audit-sensitive-ledger-behavior.md)
- [Review financial results inside the product](../reports-and-financial-review/review-financial-results-inside-the-product.md)
- [AR review workflow](../sales-and-receivables/ar-review-workflow.md)
- [AP review workflow](../expenses-and-payables/ap-review-workflow.md)
