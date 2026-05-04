---
title: Banking and Cash Management
summary: Import bank activity, review pending transactions, confirm ledger posting, and use rules to speed up repeated categorization work in SPRK.
audience: End users
app_sections:
  - banking
  - rules
workflow_type: reference
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Banking.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Rules.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/bank.go
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/rules.go
last_validated: 2026-05-02
screenshot_status: not-started
owner: codex
---

## Purpose

Use this section when you need to bring bank or credit card activity into SPRK, categorize imported transactions, confirm what should post to the general ledger, or build rules for repeated transaction patterns.

## Prerequisites

- You are signed in to SPRK.
- An active company is selected.
- At least one bank or credit card account exists in your chart of accounts.
- The expense, income, asset, liability, or equity accounts you plan to categorize to are available.

## Steps

1. Choose the workflow that matches your goal:
   - [Understand the banking page](./understand-the-banking-page.md)
   - [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
   - [Create and manage rules](./create-and-manage-rules.md)
   - [Import bank transactions](./import-bank-transactions.md)

## Expected Result

You can move from imported bank activity to reviewed and confirmed ledger posting, while keeping rule setup separate from the actual posting step.

## Common Mistakes

- Assuming imported transactions post to the general ledger immediately.
- Creating rules and expecting them to confirm transactions automatically.
- Confirming transactions before checking the selected bank account, category, split, or vendor details.

## Related Articles

- [Understand the banking page](./understand-the-banking-page.md)
- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Create and manage rules](./create-and-manage-rules.md)
- [Import bank transactions](./import-bank-transactions.md)
