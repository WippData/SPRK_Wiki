---
title: Expenses and Payables
summary: Set up vendors, enter bills, work with checks, and understand the current general ledger impact of payables workflows in SPRK.
audience: End users
app_sections:
  - vendors
  - bills
  - checks
workflow_type: reference
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Vendors.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Bills.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Checks.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/bills.go
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/checks.go
last_validated: 2026-05-02
screenshot_status: not-started
owner: codex
---

## Purpose

Use this section when you need to maintain vendor records, recognize amounts owed to vendors, pay those amounts, or track check activity tied to those payables workflows.

## Prerequisites

- You are signed in to SPRK.
- An active company is selected.
- Your company accounting setup includes an Accounts Payable account and the cash or bank accounts you plan to use for payments.

## Steps

1. Choose the workflow that matches your goal:
   - [Manage vendors](./manage-vendors.md)
   - [Create and manage bills](./create-and-manage-bills.md)
   - [Work with checks](./work-with-checks.md)
   - [Review common payables workflows](./review-common-payables-workflows.md)

## Expected Result

You can move from vendor setup into bill entry, payment, and check tracking with a clear view of when SPRK creates a payables-related ledger impact and when it is only storing reference or operational status data.

## Common Mistakes

- Creating a bill before the vendor and expense accounts are ready.
- Assuming every payables page posts the ledger in the same way.
- Treating check tracking as the same thing as bill payment posting without verifying the current workflow.

## Related Articles

- [Manage vendors](./manage-vendors.md)
- [Create and manage bills](./create-and-manage-bills.md)
- [Work with checks](./work-with-checks.md)
- [Review common payables workflows](./review-common-payables-workflows.md)
