# Set Up Receivables Defaults Before Invoicing

Prepare customer, item, and account defaults before you start entering invoices so receivables activity is easier to review and maintain later.

## Purpose

Use this page when you want invoice entry to start from cleaner defaults instead of rebuilding customer, item, and account choices on each invoice.

## Why This Matters

- Customer setup can carry a `Default Income Account` and standard payment terms.
- Item setup can carry reusable descriptions, pricing, unit-of-measure values, and income account choices.
- Invoice entry can reuse saved customers and items, or create them inline without leaving the invoice drawer.
- Cleaner setup reduces rework when you review open invoices, balances, and receivables aging later.

## Prerequisites

- You can open `Customers`, `Items`, and `Invoices`.
- Your chart of accounts already includes the income accounts and receivables account you expect to use.
- You know whether invoice lines should usually follow customer defaults, item defaults, or a one-off exception for the current job.

## Setup Workflow

1. Review your income and receivables accounts first.
2. Open `Customers` and decide whether the customer needs invoice-related defaults:
   - Set `Default Income Account` when this customer usually points to the same revenue category.
   - Set payment terms when most invoices for the customer follow the same due-date pattern.
3. Open `Items` and create or update the products or services you invoice repeatedly:
   - Save `Item Number / SKU` and `Description` values that users can recognize quickly during invoice entry.
   - Save `Unit price` and `Unit of measure` when those values repeat often.
   - Review `Income account` when you want the item record to carry its own sales default.
4. If you import customers or items, review the imported account mappings before you start invoicing.
5. Open `Invoices` and create a new invoice only after the main defaults are in place.
6. In the invoice drawer, review the header fields before adding lines:
   - `Customer`
   - `AR Account`
   - `Date`
   - `Payment Terms`
   - `Due Date`
7. Use the line selectors to pull saved item details into invoice lines:
   - `Item Number / SKU` can fill matching description and price details.
   - `Description` can fill matching item number/SKU and price details.
8. If the needed customer or item does not exist yet, create it inline from the invoice drawer and continue the invoice without leaving the workflow.
9. Before saving an invoice as `Open`, confirm the receivables account, due date, and line details still match the intended transaction.

## Expected Result

Invoice entry starts from cleaner defaults, repeated customers and items are easier to reuse, and open receivables are easier to review by customer, timing, and account structure.

## Downstream Effects

- Customer terms can fill invoice terms and help calculate a due date.
- The invoice still needs a reviewed `AR Account` before it moves to `Open`.
- Saved item details can reduce manual entry and help keep invoice lines more consistent.
- Customer and item defaults improve setup quality, but they do not replace final invoice review.
- Receivables aging and invoice list review become easier when customer names, due dates, and line details are consistent.

## Common Mistakes

- Starting invoice entry before the chart of accounts is ready for receivables and income activity.
- Assuming customer defaults remove the need to review each invoice header.
- Treating item setup as optional even when the same services or products repeat every week.
- Leaving imported customer or item account mappings unreviewed before opening invoices.
- Assuming inline create is only for customer records. It can also help you add a missing item during invoice entry.

## Related Articles

- [Manage customers](./manage-customers.md)
- [Configure customer payment terms and credit](./configure-customer-payment-terms-and-credit.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
- [Understand the chart of accounts structure](../ledger-and-chart-of-accounts/understand-the-chart-of-accounts-structure.md)

## Info

- App sections: `customers`, `items`, `invoices`, `chart`
- Last validated: 2026-06-04
- Screenshot status: `blocked`
