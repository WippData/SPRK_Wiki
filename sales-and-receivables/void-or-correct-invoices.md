# Void or Correct Invoices

Choose the supported invoice correction path before changing a posted, paid, or void-sensitive invoice.

![Invoice row action menu with Void invoice enabled on an eligible invoice](../screenshots/v1-validation/invoice-void-action-enabled.png)

## When To Use This

- An invoice needs correction after it has moved beyond simple draft entry.
- You need to decide whether to edit, receive or reverse payment, void, or review linked journals.
- You need to preserve invoice and posting history while correcting the customer record.

## Before You Start

- Confirm the active company and invoice number.
- Review invoice status, total, balance, due date, and payment history.
- Review linked journal entries before changing a posted invoice.
- If the invoice has active payments, reverse or unapply payments first where SPRK requires that guardrail.

## Steps

1. Open `Invoices`.
2. Find the invoice.
3. Review the row action menu and choose the visible action that matches the correction:
   - Use `Edit` for supported field changes.
   - Use `Record Payment` or `Match Payment` for payment activity.
   - Use `View payment history` or `View linked journal entries` when you need review before changing the invoice.
   - Use `Void invoice` only when it is visible on an eligible posted-like invoice row.
4. For an eligible unpaid open invoice, confirm the invoice is `Open` and its full balance still equals its total.
5. Do not use the void path for draft, partial, paid, or already voided invoices.
6. In `Void invoice`, choose `Today`, `Original invoice date`, or `Custom date`.
7. Enter a non-empty reason.
8. Confirm only when you intend SPRK to post a reversal, set the invoice to `Void`, zero the invoice balance, and preserve void audit details.

## What Happens When You Void or Correct

`Void invoice` preserves the original invoice and posts reversal history instead of deleting the record. Posted invoice edits follow the posted-save strategy SPRK shows before saving. Payment corrections belong in the payment workflow before the invoice recognition posting can be reversed.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| `Void invoice` is not available | Invoice status, balance, and active payments | Use the visible correction action or clear required payment activity first |
| The invoice has active payments | Payment history and payment applications | Reverse or unapply payments where SPRK requires it before voiding recognition |
| A draft invoice needs removal | Whether the invoice has posted ledger impact | Use the draft action available for that invoice instead of a void workflow |
| A posted edit prompt appears | The posted-save strategy and date choices | Choose the strategy that matches the intended correction |
| The correction would duplicate another adjustment | Existing linked journals and payment history | Stop and review the source workflow before confirming |

## Related

- [Review and edit invoices](./review-and-edit-invoices.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
- [Common accountant corrections](../ledger-and-chart-of-accounts/common-accountant-corrections.md)
