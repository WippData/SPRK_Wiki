# Receive Invoice Payments

Record customer payments from the invoice list so SPRK updates the balance and posts the cash or bank side of the transaction.

## Purpose

Use this workflow when a customer has paid an invoice and you want SPRK to reduce the receivable and update the invoice status correctly.

## Prerequisites

- The invoice already exists.
- The invoice is not already fully paid.
- A deposit account is available in the `Deposit to` selector.
- Your company has a default Accounts Receivable account configured for receivables workflows.
- The invoice is in an active receivables state such as `Open` or `Partial`.

## Steps

1. Open `Invoices`.
2. Find the invoice you want to collect against.
3. Select the dollar action for that invoice.
4. In `Receive payment`, complete:
   - `Payment date`
   - `Amount`
   - `Deposit to`
   - `Reference #`, if needed
   - `Memo`
5. Select `Record payment`.
6. If the payment is less than the remaining balance, confirm the partial-payment prompt.
7. Return to the invoice list and confirm the updated `Balance` and `Status`.
8. If you need collection follow-up for other invoices from the same customer, return to that customer record or aging report after the payment is recorded.

## Expected Result

SPRK records the payment, reduces the invoice balance, and updates the status:

- fully paid invoices become `Paid`
- partially paid invoices become `Partial`

Customer payment terms and credit settings can help you review receivables before collection, but they do not replace this payment workflow.

## Common Mistakes

- Editing the invoice status to `Paid` instead of using `Receive payment`.
- Assuming customer credit settings or invoice terms collect the payment automatically.
- Forgetting to choose `Deposit to`.
- Entering an amount greater than the remaining balance.
- Expecting a disabled dollar action on a paid invoice to reopen payment entry.

## Related Articles

- [Configure customer payment terms and credit](./configure-customer-payment-terms-and-credit.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)

## Info

- App sections: `invoices`
- Last validated: 2026-05-30
- Screenshot status: `planned`
