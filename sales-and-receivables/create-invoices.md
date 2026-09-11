# Create an Invoice

<!-- Screenshot status: Review needed -->

Create a customer invoice and choose whether it should stay open or be recorded as paid now.

![New invoice drawer showing Receive to, income routing, and sales-tax payable account](../screenshots/sales-and-receivables/invoice-routing-fields-step-01.png)

## When to use this

- You need to enter a new customer invoice.
- You need the invoice to stay in `Draft`, move to `Open`, or settle immediately.
- You need to review customer terms, due date, item details, and income accounts before saving.

## Before you start

- A customer record exists, or you are ready to add one from the invoice drawer.
- The invoice amount can be built from one or more lines.
- Your company is ready to use invoices in receivables workflows.
- You know whether `Receive to` should use an Accounts Receivable control account or a cash, bank, or credit-card settlement account.
- If the invoice includes sales tax, an active liability account is available for the amount you will owe the tax agency.
- If the customer uses saved payment terms, review the filled due date before saving.

## Steps

1. Open `Invoices`.
2. Select `New`.
3. Complete the invoice header:
   - `Invoice #`
   - `Customer`
   - `Receive to`
   - `Default income account`
   - `Date`
   - `Payment Terms`, if needed
   - `Due Date`
   - `Status`
   - `Memo`
   - `Tax rate`, if needed
   - `Sales tax payable account`, which appears when the tax rate is greater than zero
4. If company `Invoice defaults` are configured, review the starting payment terms, due date, and workflow status before you continue.
   - `Default invoice payment terms` can seed a new invoice when no customer or invoice value is already supplied.
   - `New invoice workflow` can start new invoices as `Draft` or `Open`, depending on company setup.
5. If the selected customer already has saved payment terms, review the `Payment Terms` value SPRK fills in for you.
6. Review the resulting `Due Date` before saving.
   - Common terms such as `Due on receipt`, `Due upon receipt`, `EOM`, `x/y net N`, and `Net N` can calculate due dates.
   - Treat unusual freeform terms as values to review manually.
   - If you need an exception for this invoice, replace the default due date before you save.
7. Choose `Receive to` carefully:
   - Use an Accounts Receivable control account when the customer will pay later.
   - Use a cash, bank, or credit-card settlement account only when the invoice is being recorded as paid immediately.
   - These are two different choices: open receivable or paid now.
8. Add one or more invoice lines.
9. Use `Item Number / SKU` or `Description` to pull matching item details into the line when available.
   - In companies set to `Description only`, supported item-entry helpers may show descriptions without item numbers.
10. Review quantity, unit price, line `Income account`, and extended amount on each line.
    - `Default income account` fills blank line income accounts when the drawer supports that fallback.
    - The line-level `Income account` is the posting source for that line.
11. If the invoice includes sales tax, review `Sales tax payable account`.
    - SPRK starts with the company default when one is configured.
    - You can choose another active liability account for this invoice.
    - The saved invoice keeps that selection even if the company default changes later.
12. If the customer or item does not exist yet, create it inline from the invoice drawer and continue without leaving the page.
13. Decide how the invoice should be saved:
    - `Draft` keeps the invoice unposted.
    - A taxed draft can be saved before a payable account is selected.
    - `Open` moves the invoice into an active receivables state when `Receive to` is an Accounts Receivable control account.
    - Choosing a settlement account in `Receive to` can route the invoice through the paid-now path instead of leaving an open receivable.
    - SPRK will not post a taxed Open or paid-now invoice until `Sales tax payable account` is selected.
14. If you choose `Open`, confirm `Receive to`, due date, lines, and any sales-tax account one more time before saving.
15. Save the invoice.
16. Review the invoice list to confirm the expected status, total, balance, terms, and due date.

## What Happens When You Save

The invoice appears in the invoice list with the expected number, customer, totals, balance, payment timing, and status.

- `Draft` stores the invoice without posting.
- `Open` with an Accounts Receivable control account moves the invoice into the receivables workflow.
- A settlement account in `Receive to` routes the invoice through the paid-now path instead of leaving an open receivable.
- Line-level `Income account` values receive the invoice subtotal when the invoice posts.
- When the invoice has sales tax, SPRK credits that tax to the selected liability account instead of including it in revenue.

## If something looks wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| The invoice stayed in `Draft` | Whether `Status` was set to `Draft` before saving | Edit the invoice and choose the intended workflow status before saving again |
| The invoice did not stay open as a receivable | Whether `Receive to` used a settlement account instead of an Accounts Receivable control account | Use the receivables route when the customer still owes the balance |
| The due date looks wrong | Customer terms, invoice date, and any manual due date | Correct the date before sending or relying on the invoice |
| Revenue looks routed to the wrong account | The line-level `Income account` values | Correct line accounts before saving or use a posted correction path if already posted |
| SPRK asks for a sales-tax payable account | The invoice has tax and is being saved as `Open` or paid-now | Choose the active liability account used to hold collected sales tax until it is remitted |
| Item numbers are missing from entry helpers | The company `Item identification` setting | Use description-based selection when the company is set to `Description only` |

## Related

- [Create and open invoices](./create-and-open-invoices.md)
- [Review and edit invoices](./review-and-edit-invoices.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Set up receivables defaults before invoicing](./set-up-receivables-defaults-before-invoicing.md)
- [Manage customers](./manage-customers.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)
