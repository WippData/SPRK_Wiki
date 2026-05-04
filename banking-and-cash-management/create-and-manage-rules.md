---
title: Create and Manage Rules
summary: Build rules that suggest transaction categories based on descriptions or amounts, then maintain rule priority and scope from the Rules page.
audience: End users
app_sections:
  - banking
  - rules
workflow_type: setup
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Banking.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Rules.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/rules/ruleDrawer.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/rules/drawerConfig.ts
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/rules.go
last_validated: 2026-05-02
screenshot_status: not-started
owner: codex
---

## Purpose

Use this workflow when you want SPRK to suggest the same category or split treatment for repeated bank transaction patterns.

## Prerequisites

- At least one bank or credit card account exists.
- The destination accounts you want rules to apply are available.
- You know the text pattern or amount pattern that should trigger the rule.

## Steps

1. Open `Rules` to manage rules centrally, or open `Banking` and use the row-level create rule action on a pending transaction to start from a real example.
2. Select `New` if you are creating the rule from the Rules page.
3. Enter a `Rule name`.
4. In `Apply to accounts`, leave the field blank to let the rule work across all bankish accounts, or choose specific bank or credit card accounts.
5. Choose the match logic:
   - `All conditions (AND)` requires every condition to match.
   - `Any condition (OR)` allows any one condition to match.
6. Add one or more conditions. Current fields support:
   - `Description`
   - `Amount (Spent)`
   - `Amount (Received)`
7. Choose the condition operator and value:
   - Text operators include contains, does not contain, starts with, ends with, is, and is not.
   - Numeric operators include `>`, `<`, and `between`, where `between` uses `min,max`.
8. Choose how the transaction should be categorized:
   - Use `Categorize to` for one target account.
   - Or add split rows and choose a split type.
9. If you use amount-based splits and the split lines will not consume the full amount every time, choose `Balance to` for the remainder.
10. Save the rule.
11. Review the rule list and adjust rule priority if needed:
   - Drag rows to reorder them.
   - Or use `Reorder rule`.
12. Edit, deactivate, or delete rules as your transaction patterns change.

## Expected Result

The rule is saved and becomes available when SPRK evaluates pending bank transactions. Current general ledger impact as of 2026-05-02:

- Creating, editing, reordering, activating, deactivating, importing, or deleting rules does not post to the general ledger.
- Rules suggest or prefill categorization for pending transactions.
- A general ledger entry is created only when the bank transaction itself is later confirmed from the Banking workflow.

## Common Mistakes

- Assuming rule creation confirms existing pending transactions automatically.
- Creating overlapping rules without checking priority order.
- Using a text condition that is too broad and catches unrelated transactions.
- Forgetting that split rules need valid totals or a balance account when using fixed amounts.

## Related Articles

- [Understand the banking page](./understand-the-banking-page.md)
- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Import bank transactions](./import-bank-transactions.md)
