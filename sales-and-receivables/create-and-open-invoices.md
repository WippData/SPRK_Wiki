# Create and Open Invoices

Build invoices from customers and items, save them in the right status, and reopen them later when you need to review or update the details.

## Purpose

Use this workflow when you need to create a new customer invoice, decide whether it should stay in draft or move to open status, and return to existing invoices from the invoice list.

## Prerequisites

- A customer record exists, or you are ready to add one from the invoice drawer.
- The invoice amount can be built from one or more lines.
- Your company is ready to use invoices in receivables workflows.
- You know which receivables account should carry the invoice when it opens.
- If the customer uses saved payment terms, you are ready to review the filled due date before saving.

## Create a new invoice

1. Open `Invoices`.
2. Select `New`.
3. Complete the invoice header:
   - `Invoice #`
   - `Customer`
   - `AR Account`
   - `Date`
   - `Payment Terms`, if needed
   - `Due Date`
   - `Status`
   - `Memo`
   - `Tax rate`, if needed
4. If the customer already has default payment terms, review the terms and due date that SPRK fills in for you.
5. Recheck the due date any time you change the customer, invoice date, or negotiated payment timing for this invoice.
6. Add one or more invoice lines.
7. Use `SKU` or `Description` to pull matching item details into the line when available.
8. If the customer or item does not exist yet, create it inline from the invoice drawer and continue without leaving the page.
9. Review quantity, unit price, and extended amount on each line.
10. Decide how the invoice should be saved:
   - `Draft` keeps the invoice unposted.
   - `Open` moves the invoice into an active receivables state.
11. If you choose `Open`, confirm `AR Account`, due date, and lines one more time before saving.
12. Save the invoice.
13. Review the invoice list to confirm the expected status, total, and balance.

## Open an existing invoice

1. Open `Invoices`.
2. Find the invoice in the list.
3. Use the row action for `View` when you only need to review the invoice.
4. Use the row action for `Edit` when you need to update the invoice details.
5. Confirm the invoice number, customer, date, due date, status, total, and balance before making changes.

## Expected Result

The invoice appears in the invoice list with the expected number, customer, totals, balance, and status. Reopened invoices can be reviewed in view mode or updated in edit mode.

## Common Mistakes

- Leaving the invoice in `Draft` when you expected it to move into the active receivables workflow.
- Choosing `Paid` in the invoice status field and assuming that is the same as recording a payment.
- Leaving `AR Account` blank when you expect the invoice to move into an open receivables state.
- Forgetting that `Customer` is required.
- Skipping a review of the due date after customer terms or invoice dates change.
- Assuming customer payment terms are always correct for exceptions, rush jobs, or negotiated one-off dates.
- Changing an existing invoice without checking its current balance and status first.

## Related Articles

- [Set up receivables defaults before invoicing](./set-up-receivables-defaults-before-invoicing.md)
- [Configure customer payment terms and credit](./configure-customer-payment-terms-and-credit.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
- [Manage customers](./manage-customers.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)

## Info

- App sections: `invoices`
- Last validated: 2026-05-31
- Screenshot status: `planned`
