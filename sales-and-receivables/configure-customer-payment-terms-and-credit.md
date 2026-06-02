# Configure Customer Payment Terms and Credit

Set customer-level payment and credit defaults before invoicing so due dates, receivables follow-up, and review expectations stay more consistent.

## Purpose

Use this page when you want a customer record to carry standard payment terms, a visible credit review status, or a credit limit before your team starts creating invoices.

## When To Use This Setup

- Set payment terms when most invoices for the customer should start from the same due-date pattern.
- Set a credit status when your team needs a visible reminder to pause, review, or use a stricter collection approach before opening invoices.
- Set a credit limit when you want the customer record to show an internal receivables threshold for review.

## Prerequisites

- You can open `Customers`.
- The customer record already exists, or you are ready to create it.
- You know whether the customer should use standard terms such as `Net 15`, `Net 30`, or `Due on receipt`.

## Steps

1. Open `Customers`.
2. Create a new customer or edit an existing one.
3. Open `Payments & Credit`.
4. Review `Terms` first:
   - Use this field when the customer usually follows the same payment window.
   - SPRK can use the customer terms to fill `Payment Terms` and `Due Date` when you start a new invoice for that customer.
5. Review `Credit Status` next:
   - Choose the status that best matches how your team wants to review future invoices.
   - Common visible options include `Approved`, `Credit Hold`, `Cash Only`, `On Hold`, and `Review Required`.
6. Review `Credit Limit` if you want the customer record to show a reference amount for receivables review.
7. Save the customer.
8. When creating an invoice later, confirm the filled `Payment Terms` and `Due Date` instead of assuming they are always correct for that specific job.
9. Use the customer row action for `AR Aging` when you need to review open balances for that customer after invoices are posted.

## Expected Result

The customer record keeps payment and credit defaults together, new invoices can start with the customer terms already filled in, and receivables follow-up stays easier to review by customer.

## Downstream Effects

- Customer terms can prefill invoice `Payment Terms` and help SPRK calculate a due date from the invoice date.
- Invoice-level terms still need review because a one-off invoice may need a different due date than the customer default.
- Receivables aging can show terms and overdue timing alongside the customer balance, which helps with collection follow-up.
- Recording a payment is still a separate workflow. Changing terms or credit settings does not reduce an invoice balance.

## Common Mistakes

- Treating customer terms as permanent invoice instructions without reviewing the actual invoice date and due date.
- Using `Paid` or another invoice status change instead of the payment workflow when money is collected.
- Assuming a credit status blocks or approves customer activity automatically. Use it as a visible control point unless your team has verified a stronger workflow around it.
- Forgetting to revisit older customer defaults after payment expectations change.

## Related Articles

- [Manage customers](./manage-customers.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)

## Info

- App sections: `customers`, `invoices`, `reports`
- Last validated: 2026-05-30
- Screenshot status: `planned`
