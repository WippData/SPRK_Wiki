---
title: Review Common Payables Workflows
summary: Use a simple decision path to move from vendor setup to bill recognition, payment, and check tracking without mixing up the accounting effect.
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

Use this article when you want a quick way to choose the right payables workflow before entering data in the wrong place.

## Prerequisites

- You have an active company selected.
- You know whether your next step is setup, payable recognition, payment, or check tracking.

## Steps

1. Start with `Vendors` if the payee does not exist yet.
2. Use `Bills` when you need SPRK to track an amount owed to a vendor.
3. Save the bill as `Draft` if you are still reviewing it, or `Open` if you want SPRK to recognize the payable.
4. Return to `Bills` and use `Record payment` when you are paying an existing bill from a bank or cash account.
5. Use `Checks` when you need to maintain a check record and its status, especially for matching and reconciliation work.
6. If you are unsure whether a step affects the ledger, verify it before saving:
   - Vendor setup: no journal entry
   - Bill opened: debits line accounts and credits Accounts Payable
   - Bill payment: debits Accounts Payable and credits the selected payment account
   - Check record activity: operational tracking only in the current documented flow

## Expected Result

You can choose the right payables page quickly and avoid confusing master-data setup, payable recognition, payment posting, and check-status tracking.

## Common Mistakes

- Using `Checks` when the real task is to reduce an open bill balance.
- Entering a bill as `Open` before verifying the account coding.
- Assuming vendor setup, bill entry, and check tracking all create the same accounting result.

## Related Articles

- [Manage vendors](./manage-vendors.md)
- [Create and manage bills](./create-and-manage-bills.md)
- [Work with checks](./work-with-checks.md)
