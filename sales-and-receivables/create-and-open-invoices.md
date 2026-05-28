# Create and Open Invoices

Build invoices from customers and items, save them in the right status, and reopen them later when you need to review or update the details.

## Purpose

Use this workflow when you need to create a new customer invoice, decide whether it should stay in draft or move to open status, and return to existing invoices from the invoice list.

## Prerequisites

- A customer record exists, or you are ready to add one from the invoice drawer.
- The invoice amount can be built from one or more lines, with or without existing item records.
- Your company is ready to use invoices in receivables workflows.

## Create a new invoice

1. Open `Invoices`, then select `New`.
2. Review `Invoice #`. SPRK fills the next available invoice number automatically, but you can override it if needed.
3. Choose `Customer`. If the customer does not exist yet, use the invoice drawer option to add a new customer without leaving the workflow.
4. Review `Date`, `Payment Terms`, and `Due Date`.
5. If the customer already has default terms, confirm the terms and due date that SPRK fills in for you.
6. If you change the invoice date or payment terms, review the due date again because SPRK recalculates it from those values.
7. Add `Memo` or `Tax rate` if needed.
8. Add one or more invoice lines.
9. Use `SKU` or `Description` to pull matching item details into the line when available. If the item does not exist yet, use the line-level option to add a new item from the drawer.
10. Review quantity, unit price, extended amount, and invoice totals.
11. Decide how the invoice should be saved:
   - `Draft` keeps the invoice unposted.
   - `Open` posts the invoice to active receivables.
12. Save the invoice.
13. Review the invoice list to confirm the expected status, total, and balance.

## Open an existing invoice

1. Open `Invoices`.
2. Find the invoice in the list. If needed, narrow the list by searching for the invoice number, customer, or memo, or by filtering on customer or status.
3. Use the row action for `View` when you only need to review the invoice.
4. Use the row action for `Edit` when you need to update the invoice details.
5. Confirm the invoice number, customer, date, due date, status, total, and balance before making changes.

## Expected Result

The invoice appears in the invoice list with the expected number, customer, totals, balance, and status. Reopened invoices can be reviewed in view mode or updated in edit mode.

## Common Mistakes

- Leaving the invoice in `Draft` when you expected it to move into the active receivables workflow.
- Choosing `Paid` in the invoice status field and assuming that is the same as recording a payment.
- Forgetting that `Customer` is required.
- Treating the auto-filled invoice number as locked when you actually need to override it.
- Skipping a review of the due date after customer terms or invoice dates change.
- Changing an existing invoice without checking its current balance and status first.

## Related Articles

- [Receive invoice payments](./receive-invoice-payments.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
- [Manage customers](./manage-customers.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)

## Info

- App sections: `invoices`
- Last validated: 2026-05-28
- Screenshot status: `not-started`
