# Print Invoices

Print customer-facing invoice copies and review invoice template settings before sending output to a customer.

![Invoice Template modal showing company contact fields, payment instructions, and print controls](../screenshots/sales-and-receivables/invoice-template-settings-step-01.png)

## When To Use This

- You need to print or save customer-facing invoice output.
- You need to review the company-wide invoice print layout.
- You need to confirm whether SKU, sales tax, quantities, prices, dates, or totals should appear.

## Before You Start

- Confirm the active company.
- Confirm the invoice number, customer, date, total, and balance.
- Review the invoice before printing if the customer-facing copy will be sent outside your firm.

## Steps

1. Open `Invoices`.
2. Use the row action `Print` when you want to print directly from the invoice list without opening edit mode first.
3. Use `More` > `Invoice Template` when you need to change the company-wide print layout.
4. Review the visible print settings before saving:
   - `Header Information`
   - `Show Sales Tax`
   - `Show SKU`
   - `Show Qty/Price`
   - `Show Date on Lines`
   - `Show Totals`
5. Leave settings on when you want the full customer-facing layout.
6. Use the switches and choices for specific presentation needs:
   - `Header Information` controls the company header block. Invoice metadata and `Bill To` details remain part of the invoice layout.
   - `Show Sales Tax` controls the sales-tax total line.
   - `Show SKU` controls the SKU column.
   - `Show Qty/Price` controls quantity and unit-price columns together.
   - `Show Date on Lines` can use `None`, `Due Date`, or `Invoice Date` as one shared date column for invoice lines.
   - `Show Totals` can place totals `Under Table` or at the `Bottom of Page`.
7. Review the printed preview before sending it to a customer.

![Invoice Template Show Totals menu with Under Table and Bottom of Page options](../screenshots/sales-and-receivables/invoice-template-totals-options-step-02.png)

## What This Changes

Printing and template review change customer-facing output. They do not record a payment, change invoice balance, or edit ledger posting by themselves. When no print settings have been saved yet, SPRK uses the full printable layout.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| A printed invoice is missing SKU or line details | `Show SKU`, `Show Qty/Price`, and `Show Date on Lines` | Update the template setting before printing again |
| Totals appear in the wrong place | `Show Totals` | Choose `Under Table` or `Bottom of Page` |
| The company header does not look right | `Header Information` and company contact details | Review company and invoice template settings before sending the invoice |
| The printout does not show payment history | Whether you are expecting internal review detail | Use payment history or linked journal review inside SPRK instead |

## Related

- [Create and open invoices](./create-and-open-invoices.md)
- [Review and edit invoices](./review-and-edit-invoices.md)
- [Manage default company settings](../company-administration/manage-default-company-settings.md)
