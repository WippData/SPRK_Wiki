# Understand Invoice General Ledger Impact

Understand how invoice creation, receivables account review, customer and item defaults, customer terms, Open status recognition, aging review, and payment receipt affect the general ledger and receivables review in SPRK.

## Purpose

Use this article when you need to understand what SPRK currently posts to the general ledger during invoice creation and payment receipt, and what setup defaults do not change about that posting pattern.

## Prerequisites

- You understand the difference between `Draft`, `Open`, `Partial`, and `Paid` invoice statuses.
- You have access to the invoice workflow and, if needed, the Ledger page for validation.

## Steps

1. Treat `Draft` and `Open` as different accounting states.
2. Use `Open` when you want SPRK to recognize the receivable.
3. Review the invoice `AR Account` before the invoice moves to `Open`.
4. Treat customer `Terms`, invoice `Due Date`, and item defaults as setup and timing data, not as the posting trigger.
5. Use `Receive payment` when cash or bank has actually been collected.
6. Verify the resulting status and balance in `Invoices`.
7. If you need to validate the posting, inspect the related activity in `Ledger`.
8. If you need collection follow-up, use receivables aging to review invoice terms, due dates, and overdue timing after the invoice is already posted.

## Expected Result

Invoice posting behavior as of 2026-05-31:

- Creating an invoice as `Draft` does not post a journal entry.
- Creating an invoice as `Open`, or updating an existing invoice from a non-open status to `Open`, posts one recognition journal entry.
- Recording a payment through `Receive payment` posts a separate payment journal entry and updates the invoice balance.

Current invoice recognition entry when an invoice becomes `Open`:

- Debit `Accounts Receivable` for the full invoice total
- Credit a single income account for the full invoice total

Current payment entry when a payment is recorded:

- Debit the selected `Deposit to` account
- Credit `Accounts Receivable`

Customer terms, customer credit settings, and item defaults affect setup and follow-up, but they do not change the basic journal pattern above. Their main downstream effect is on invoice terms, due-date defaults, data consistency, and receivables aging review.

Current aging behavior:

- If an invoice has invoice-level terms, aging can show those terms for that invoice.
- If an invoice does not carry its own terms, aging can fall back to the customer default terms.
- Aging review can show terms and overdue timing alongside the customer balance, which helps with collection follow-up.

Current status behavior when a payment is recorded:

- payment equals remaining balance: invoice becomes `Paid`
- payment is less than remaining balance: invoice becomes `Partial`
- payment greater than remaining balance: blocked

## Common Mistakes

- Marking an invoice `Paid` by editing status instead of using `Receive payment`. The payment posting logic is tied to the payment workflow, not a manual status change.
- Assuming customer payment terms or credit settings change the journal entry pattern. They do not.
- Assuming item-level income account selections currently drive the invoice journal entry. SPRK currently credits one resolved income account for the whole invoice.
- Assuming customer or item defaults automatically replace the need to review the receivables account on each invoice.
- Assuming tax is posted to a separate liability account. The current invoice recognition logic credits the full total to the income side.
- Assuming customer credit settings automatically stop or post invoice activity. Use them as setup and review signals unless your workflow has been validated otherwise.
- Assuming void handling is part of this documented flow. This article only documents create/open and payment behavior.

## Related Articles

- [Set up receivables defaults before invoicing](./set-up-receivables-defaults-before-invoicing.md)
- [Configure customer payment terms and credit](./configure-customer-payment-terms-and-credit.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)

## Info

- App sections: `invoices`, `ledger`, `reports`
- Last validated: 2026-05-31
- Screenshot status: `planned`
