# Manage Items for Invoicing

Define reusable products and services so invoice and bill lines can be built faster and with more consistent descriptions, pricing, and account defaults.

![Items list showing Item Number / SKU column and search label](../screenshots/sales-and-receivables/items-item-number-sku-step-01.png)

## When To Use This

Use this workflow when you want invoice lines to reuse prepared item records instead of retyping descriptions, prices, and sales defaults each time.

## Before You Start

- You can open the `Items` page.
- You know whether the record should be set up as a service, product, or other item type.
- You know whether the company should show items as `Item number + description` or `Description only`.

## Steps

1. Open `Items`.
2. Choose the setup path that fits the job:
   - Use `New` to create one item from the drawer.
   - Use `Import` if you already maintain item data in a spreadsheet or CSV file.
   - Use `More` > `Enable Grid Mode` when you need to edit several items together, or turn on `Grid Edit default` in `Preferences` if you want supported pages to open that way automatically.
3. Enter the core item details:
   - `Item type`
   - `Item Number / SKU`
   - `Description`
   - `Unit price`
   - `Unit of measure`
4. Fill in the extra pricing and tax fields when they matter for your workflow:
   - `Buy price`
   - `Sell price`
   - `Tax code`
5. If your accounting setup uses account defaults, review:
   - `Income account` is the income account credited when the item is used on an invoice.
   - `Expense/COGS account` is an optional default for the item's cost side.
6. Confirm the `Active` setting, then save the item.
7. If you import items, review any mapped income or expense accounts before you rely on those records in invoices.
8. Use the page search when you need to find an item later by item number, SKU, or description.
9. Use the saved item later from invoice line selectors so invoice entry stays more consistent.
10. Use item row actions when you want to start a document directly from an item:
   - `Create Invoice` opens an invoice drawer with the selected item ready for invoice-line review.
   - `Create Bill` opens a bill drawer with the selected item ready for bill-line review where that workflow is available.
   - Review the customer or vendor, account, price or cost, quantity, tax, and status before saving. The shortcut starts the document; it does not post it by itself.
11. Use Grid Edit when repeated item cleanup will be faster than opening each record individually, then review the changed-cell count before selecting `Apply Changes`.

## Item Identification Mode

Company setup can control how supported item labels appear:

- `Item number + description` shows item numbers beside descriptions where the current workflow supports it.
- `Description only` hides item numbers from supported item selectors, invoice drawers, and line-entry helpers.

This is a presentation setting. It does not delete the item number from the item record, change the item's income or expense accounts, or change posting behavior.

## Items And Inventory

Choosing `Product` as the `Item type` or filling in `Expense/COGS account` does not, by itself, create inventory quantities, an inventory asset balance, or automatic cost-of-goods-sold entries. The item stores reusable invoice or bill defaults. If you track inventory outside SPRK, use your accountant's approved journal and supporting schedule rather than assuming the item record is a perpetual inventory system.

## What Happens Next

The item becomes available for invoice entry, item-started invoices or bills where available, and future lines can reuse its saved description, pricing, unit-of-measure, and account defaults.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| An item exists, but no invoice has posted | Whether you have created and opened an invoice using the item | Item setup supplies defaults; the invoice workflow creates the receivable and income posting |
| An item number is hidden | The company `Item identification` mode | Choose `Item number + description` if your team wants item numbers displayed |
| Inventory quantities or asset balances are missing | Whether you expected `Product` or `Expense/COGS account` to turn on inventory accounting | Maintain the approved inventory schedule and entries separately |

## Related

- [Set up receivables defaults before invoicing](./set-up-receivables-defaults-before-invoicing.md)
- [Manage customers](./manage-customers.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
- [Use grid edit for bulk record maintenance](../dashboard-and-navigation/use-grid-edit-for-bulk-record-maintenance.md)
