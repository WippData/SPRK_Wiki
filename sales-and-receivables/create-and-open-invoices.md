# Create and Open Invoices

Build invoices from customers and items, then move them to Open status when you want SPRK to post the receivable.

## Purpose

Use this workflow when you need to create a customer invoice and decide whether it should stay in draft or post to receivables immediately.

## Prerequisites

- A customer record exists.
- The invoice amount can be built from one or more lines.
- Your company has an Accounts Receivable setup that supports invoice posting.

## Steps

1. Open `Invoices`.
2. Select `New`.
3. Complete the invoice header:
   - `Invoice #`
   - `Customer`
   - `Date`
   - `Due Date`
   - `Status`
   - `Memo`
   - `Tax rate`, if needed
4. Add one or more invoice lines.
5. Use `SKU` or `Description` to pull item details into the line when available.
6. Review quantity, unit price, and extended amount on each line.
7. Decide how the invoice should be saved:
   - `Draft` keeps the invoice unposted.
   - `Open` posts the receivable based on the current invoice workflow.
8. Save the invoice.
9. Review the invoice list to confirm the expected status, total, and balance.

## Expected Result

The invoice is created and appears in the invoice list. If you saved it as `Open`, the receivable posting logic runs. If you saved it as `Draft`, the invoice exists but does not post to the ledger yet.

## Common Mistakes

- Leaving the invoice in `Draft` when you expected the receivable to post immediately.
- Choosing `Paid` directly in the status field and assuming that is the same as recording a payment.
- Forgetting that a valid customer is required.
- Creating an `Open` invoice before verifying the amount and tax values.

## Related Articles

- [Receive invoice payments](./receive-invoice-payments.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
- [Manage customers](./manage-customers.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)

## Info

- App sections: `invoices`
- Last validated: 2026-05-02
- Screenshot status: `not-started`
