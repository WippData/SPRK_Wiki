---
title: Sales and Receivables
summary: Set up customers and items, create invoices, receive payments, and understand the current general ledger impact of receivables workflows in SPRK.
audience: End users
app_sections:
  - customers
  - items
  - invoices
workflow_type: reference
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Customers.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Items.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Invoices.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/invoices.go
last_validated: 2026-05-02
screenshot_status: not-started
owner: codex
---

## Purpose

Use this section when you need to manage customers, define billable items, issue invoices, collect payments, and understand the accounting impact of those actions.

## Prerequisites

- You are signed in to SPRK.
- An active company is selected.
- Your company accounting setup includes the receivables accounts needed for invoicing and payment workflows.

## Steps

1. Choose the workflow that matches your goal:
   - [Manage customers](./manage-customers.md)
   - [Manage items for invoicing](./manage-items-for-invoicing.md)
   - [Create and open invoices](./create-and-open-invoices.md)
   - [Receive invoice payments](./receive-invoice-payments.md)
   - [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)

## Expected Result

You can move from customer and item setup into invoice creation and payment collection with a clear understanding of what SPRK posts to the general ledger.

## Common Mistakes

- Creating invoices before customer or item setup is ready.
- Assuming a `Draft` invoice has already posted to the ledger.
- Changing an invoice status to `Paid` manually instead of using the payment workflow.
- Assuming line-item income account settings currently drive the invoice journal entry without verifying the backend posting logic.

## Related Articles

- [Manage customers](./manage-customers.md)
- [Manage items for invoicing](./manage-items-for-invoicing.md)
- [Create and open invoices](./create-and-open-invoices.md)
- [Receive invoice payments](./receive-invoice-payments.md)
- [Understand invoice general ledger impact](./understand-invoice-general-ledger-impact.md)
