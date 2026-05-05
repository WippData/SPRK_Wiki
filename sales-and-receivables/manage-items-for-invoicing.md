# Manage Items for Invoicing

Define products and services so invoice lines can be filled quickly and consistently.

## Purpose

Use this workflow when you want invoice lines to populate more quickly and consistently from reusable item records.

## Prerequisites

- You can open the `Items` page.
- You know whether the item is a service, product, or other type.

## Steps

1. Open `Items`.
2. Select `New` to create an item, or use the row actions to view or edit an existing one.
3. Enter the core item details:
   - `Item type`
   - `SKU`
   - `Description`
   - `Unit price`
   - `Unit of measure`
4. If your accounting setup uses them, set:
   - `Income account`
   - `Expense/COGS account`
   - `Tax code`
5. Save the item.
6. Use the item later from the invoice line `SKU` or `Description` selectors when building an invoice.

## Expected Result

The item becomes available for invoice entry, and invoice lines can reuse its SKU, description, and pricing details.

## Common Mistakes

- Skipping item setup and retyping every invoice line manually.
- Assuming item setup alone controls the current invoice journal entry behavior. Review the GL article for the present posting logic.
- Leaving descriptions too vague, which makes invoice lines and reports harder to interpret.

## Related Articles

- [Manage customers](./manage-customers.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)

## Info

- App sections: `items`
- Last validated: 2026-05-02
- Screenshot status: `not-started`
