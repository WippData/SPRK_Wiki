# Create and Open Invoices

Build invoices from customers and items, save them in the right status, and reopen them later when you need to review or update the details.

![New invoice drawer showing Item Number / SKU on invoice lines](../screenshots/sales-and-receivables/invoice-item-number-sku-line-step-02.png)

![Invoice row actions showing payment, linked journal, payment history, and void actions](../screenshots/sales-and-receivables/invoice-payment-history-void-actions-step-01.png)

## When To Use This

Use this workflow when you need to create a new customer invoice, decide whether it should stay in draft or move to open status, and return to existing invoices from the invoice list.

## Before You Start

- A customer record exists, or you are ready to add one from the invoice drawer.
- The invoice amount can be built from one or more lines.
- Your company is ready to use invoices in receivables workflows.
- You know which receivables account should carry the invoice when it opens.
- If the company uses name-only account presentation, account pickers such as `AR Account` can show names without code-first labels.
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
4. If the selected customer already has saved payment terms, review the `Payment Terms` value SPRK fills in for you.
5. Review the resulting `Due Date` before saving:
   - If the invoice does not already have a manual due date, SPRK can calculate one from the invoice date and payment terms.
   - If you need an exception for this invoice, replace the default due date with the agreed date before you save.
6. Recheck the due date any time you change the customer, invoice date, or negotiated payment timing for this invoice.
7. Add one or more invoice lines.
8. Use `Item Number / SKU` or `Description` to pull matching item details into the line when available.
9. If the customer or item does not exist yet, create it inline from the invoice drawer and continue without leaving the page.
10. Review quantity, unit price, and extended amount on each line.
11. Decide how the invoice should be saved:
   - `Draft` keeps the invoice unposted.
   - `Open` moves the invoice into an active receivables state.
12. If you choose `Open`, confirm `AR Account`, due date, and lines one more time before saving.
13. Save the invoice.
   - If you edit and save an invoice that has already posted, SPRK can show `Save Posted Invoice` before it changes the posting.
   - Review the available strategy before continuing: `Post adjustment journal entry`, `Reverse and repost`, or `Edit existing journal entry`.
   - Adjustment dates can use `Today`, `Original posting date`, or `Custom date`.
   - Reversal dates can use `Original posting date`, `Today`, or `Custom date`; repost dates can use `Document date`, `Today`, or `Custom date`.
14. Review the invoice list to confirm the expected status, total, balance, terms, and due date.

## Open an existing invoice

1. Open `Invoices`.
2. Find the invoice in the list.
3. Use the row action for `View` when you only need to review the invoice.
4. Use the row action for `Edit` when you need to update the invoice details.
5. Use the row action menu when you need source-document actions such as `Record Payment`, `Match Payment`, `View linked journal entries`, `View payment history`, or `Void invoice`.
6. Confirm the invoice number, customer, date, due date, status, total, and balance before making changes.

## Void an unpaid open invoice

1. Use `Void invoice` only when it is visible on an eligible posted-like invoice row.
2. Confirm the invoice is `Open` and its full balance still equals its total.
3. Do not use this path for draft, partial, paid, or already voided invoices.
4. In `Void invoice`, choose `Today`, `Original invoice date`, or `Custom date`.
5. Enter a non-empty reason.
6. Confirm only when you intend SPRK to post a reversal, set the invoice to `Void`, zero the invoice balance, and preserve void audit details.

## What Happens Next

The invoice appears in the invoice list with the expected number, customer, totals, balance, payment timing, and status. Reopened invoices can be reviewed in view mode, updated in edit mode, reviewed through payment history, or corrected through supported source-document actions. Posted invoice saves follow the strategy you choose when SPRK prompts, and `Edit existing journal entry` can be unavailable when company policy or prior adjustment history does not allow it.

## If Something Looks Wrong

- Leaving the invoice in `Draft` when you expected it to move into the active receivables workflow.
- Choosing `Paid` in the invoice status field and assuming that is the same as recording a payment.
- Leaving `AR Account` blank when you expect the invoice to move into an open receivables state.
- Forgetting that `Customer` is required.
- Skipping a review of the due date after customer terms or invoice dates change.
- Assuming customer payment terms are always correct for exceptions, rush jobs, or negotiated one-off dates.
- Changing an existing invoice without checking its current balance and status first.
- Treating `Save Posted Invoice` as a routine draft save. It is an audit-sensitive choice about how SPRK should preserve or adjust the posted entry.
- Trying to void an invoice that already has active payments. Reverse or unapply active payments first where the product supports that correction.
- Treating `Void invoice` as delete. It preserves the invoice and creates reversal history.

## Related

- [Set up receivables defaults before invoicing](./set-up-receivables-defaults-before-invoicing.md)
- [Configure customer payment terms and credit](./configure-customer-payment-terms-and-credit.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
- [Review document payment history and linked journals](../ledger-and-chart-of-accounts/review-document-payment-history-and-linked-journals.md)
- [Manage customers](./manage-customers.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)
