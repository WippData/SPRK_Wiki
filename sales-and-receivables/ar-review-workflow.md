# AR Review Workflow

![Invoices list showing payment actions and invoice status context](../screenshots/sales-and-receivables/invoices-list-payment-action-step-01.png)

Use this accounts receivable review workflow to check customers, invoices, payments, receivables aging, and revenue detail before reporting.

## When To Use This

Use this workflow before month-end reporting, before contacting customers about balances, or when receivables totals on reports do not look right.

## Before You Start

- The correct company is active.
- Customer records and invoice items are set up.
- Customer invoices and payments for the period have been entered or imported through the supported workflows.

## Steps

1. Review customer records for duplicate or incomplete names.
2. Review invoice defaults before entering more invoices.
   - Confirm payment terms.
   - Confirm invoice items and revenue accounts.
3. Open the invoice list and filter or sort for open, overdue, voided, or recently paid invoices.
4. Review invoices that should have been paid.
5. Receive payments against the invoice records when customer money has been received.
6. Review payment history from the invoice or customer context when a balance looks wrong.
7. Run `Receivables Aging` if available.
8. Run `Income Statement` and review revenue totals for the period.
9. Use drilldown or `General Ledger` detail when revenue or AR balances do not match expectations.
10. Correct invoice or payment issues in the receivables workflow before using journal entries.

## What Happens Next

AR review helps confirm that customer balances, invoice status, payment application, AR aging, and revenue reporting are telling the same story.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| A customer balance is being cleared with a journal entry | Whether invoice payment status explains the balance | Review the invoice and payment workflow before posting an adjustment |
| A bank deposit appears to prove an invoice was paid | Whether the payment was applied to the open invoice | Match bank activity only after the receivables workflow is correct |
| Receivables aging looks incomplete | Whether invoices and payments have all been entered | Complete source activity before relying on the aging report |
| Revenue accounts are being changed after posting | Whether posted invoices already used the original account | Review the posting impact before changing account setup |
| AR totals look wrong | Whether the active company is the one under review | Switch to the correct company before continuing |

## Related

- [Manage customers](./manage-customers.md)
- [Set up receivables defaults before invoicing](./set-up-receivables-defaults-before-invoicing.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
- [Review financial results inside the product](../reports-and-financial-review/review-financial-results-inside-the-product.md)
