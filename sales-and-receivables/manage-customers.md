# Manage Customers

Create and maintain customer records so invoicing, payment follow-up, and customer-specific receivables workflows start from clean setup data.

## Purpose

Use this workflow when you need to add, update, search, import, or review customer records before creating invoices or receiving customer payments.

## Prerequisites

- You can open the `Customers` page.
- You know the customer name.
- If you plan to use customer defaults for invoicing, you know the income account, payment terms, or credit settings you want to apply.
- You understand whether this customer should use standard terms, restricted credit handling, or manual review before invoicing.

## Steps

1. Open `Customers`.
2. Decide how you want to work with the list:
   - Use `New` to add one customer from the drawer.
   - Use `Import` if you already have customer data in a spreadsheet or CSV file.
   - Use `More` and enable grid mode if you want to make several edits in one pass.
3. When creating or editing a single customer, complete the core record details:
   - `Name` is required.
   - `Company`, `Email`, and `Phone` support billing and follow-up workflows.
   - Address fields help complete the customer profile when you need them.
4. If you want invoices for this customer to start from a consistent sales setup, set `Default Income Account`.
5. If you track customer payment expectations, open `Payments & Credit` and review the available settings:
   - `Credit limit`
   - `Credit status`
   - `Terms`
6. Decide whether this customer needs setup beyond the basic record:
   - Keep the record simple if you only need contact details.
   - Add payment terms when invoices should usually follow a standard due-date pattern.
   - Add credit settings when your team wants a visible review signal before opening new invoices.
7. Save the customer.
8. Use the page tools to manage or review the list after setup:
   - Search by name, company, email, or phone.
   - Filter for `Active` or `Inactive` customers when cleaning up the list.
   - Open row actions for an existing customer when you want to create an invoice, create a payment, or jump into that customer's `AR Aging` report.
9. If the customer will be invoiced often, pair this setup with saved item records and invoice account review before the first live invoice.

## Expected Result

The customer is saved and available for invoice selection, payment workflows, search, import cleanup, and customer-specific receivables follow-up.

## Common Mistakes

- Skipping the customer record and trying to build invoice workflows from inconsistent free-typed names.
- Ignoring active and inactive status when cleaning up an older customer list.
- Setting a default income account without confirming it is the correct income-type account for your setup.
- Forgetting to maintain terms or credit settings when those defaults matter for invoice creation and follow-up.
- Treating `Credit status` as a payment record. It is a setup signal, not the same thing as receiving money.
- Assuming customer setup alone finishes receivables preparation. Review item setup, invoice account review, and due-date defaults before opening invoices.

## Related Articles

- [Set up receivables defaults before invoicing](./set-up-receivables-defaults-before-invoicing.md)
- [Configure customer payment terms and credit](./configure-customer-payment-terms-and-credit.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Use global search](../dashboard-and-navigation/use-global-search.md)

## Info

- App sections: `customers`
- Last validated: 2026-05-31
- Screenshot status: `planned`
