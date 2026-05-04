---
title: Reconciliation
summary: Start a reconciliation window, match or unmatch transactions when needed, finish only when the difference is zero, and understand that reconciliation changes cleared status rather than creating new ledger entries.
audience: End users
app_sections:
  - reconcile
workflow_type: reference
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Reconcile.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/reconciliation/hooks.ts
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/reconcile.go
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/bank.go
last_validated: 2026-05-02
screenshot_status: not-started
owner: codex
---

## Purpose

Use this section when you need to reconcile a bank or credit card account against a statement, manage matched check links during that review, and understand what reconciliation changes in SPRK.

## Prerequisites

- You are signed in to SPRK.
- An active company is selected.
- At least one bank or credit card account exists.
- The transactions you want to clear are already confirmed in SPRK.

## Steps

1. Choose the workflow that matches your goal:
   - [Start a reconciliation](./start-a-reconciliation.md)
   - [Match and unmatch transactions](./match-and-unmatch-transactions.md)
   - [Finish a reconciliation](./finish-a-reconciliation.md)
   - [Resolve common reconciliation exceptions](./resolve-common-reconciliation-exceptions.md)

## Expected Result

You can open a reconciliation window with the right statement values, clear the correct confirmed transactions, manage check matching where needed, and finish with a zero difference.

## Common Mistakes

- Trying to reconcile pending bank transactions instead of confirmed ones.
- Treating reconciliation as a way to reclassify account coding instead of confirming statement agreement.
- Expecting reconciliation to create a new general ledger entry. In the current flow, it records reconciliation status on existing transactions and stores a posted reconciliation record.

## Related Articles

- [Start a reconciliation](./start-a-reconciliation.md)
- [Match and unmatch transactions](./match-and-unmatch-transactions.md)
- [Finish a reconciliation](./finish-a-reconciliation.md)
- [Resolve common reconciliation exceptions](./resolve-common-reconciliation-exceptions.md)
