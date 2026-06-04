# Create and Manage Rules

Build rules that prefill GL account choices for repeated bank transaction patterns, then manage scope, priority, and imported rule sets from the Rules page.

## Purpose

Use this workflow when the same bank or credit card transactions appear repeatedly and you want SPRK to prepare those rows more consistently before you confirm them.

## Prerequisites

- At least one bank or credit card account exists.
- The destination accounts you want rules to use are available.
- You know the text pattern or amount pattern that should trigger the rule.

## Steps

1. Open `Rules` to manage rules centrally.
   - If you are already reviewing a pending bank transaction, you can also start from the row-level rule action in `Banking`.
2. Choose the rules tab that matches the result you want:
   - `Expense / COGS` for spending-side categorization patterns.
   - `Income` for deposit-side categorization patterns.
3. Select `New`.
4. Enter a clear `Rule name`.
5. In `Apply to accounts`, either:
   - leave the field blank to let the rule apply across all bank and credit card accounts, or
   - choose the specific bank or credit card accounts where the pattern should apply.
6. Choose the match logic:
   - `All conditions (AND)` means every condition must match.
   - `Any condition (OR)` means any one condition can match.
7. Add one or more conditions. The current rule builder supports:
   - `Description`
   - `Amount (Spent)`
   - `Amount (Received)`
8. Choose the operator and value for each condition.
   - Text operators include contains, does not contain, starts with, ends with, is, and is not.
   - Numeric operators include `>`, `<`, and `between`.
   - For `between`, enter the range as `min,max`.
9. Choose the categorization result:
   - Use `GL Account` when one destination account is enough.
   - Add split rows when the same pattern should be distributed across multiple accounts.
10. If you use a split rule:
   - Choose `%` when the split should total exactly `100%`.
   - Choose `$` when the rule should use fixed amounts.
   - For `$` splits, set `Balance to` so SPRK knows where any remaining amount should go.
11. Save the rule.
12. Review the rule list and adjust priority when multiple rules could match the same pattern.
   - Drag rows to reorder them.
   - Use the row-level reorder action if you want to move a rule to the top, bottom, or a specific position.
   - Use `Reorder rule` when you want to move a rule by name and target position.
13. If you already maintain rules in a spreadsheet, use `Import` to preview and load a rules file.
   - The current import flow accepts `.xlsx` and `.xls`.
   - Review the preview and any reported issues before confirming the import.
   - Legacy imported condition fields can still match when their capitalization differs, but new setup should use the visible current labels, including `GL Account`.
14. Edit, disable, or delete rules as your transaction patterns change.

## Expected Result

The rule is saved and becomes available when SPRK evaluates pending bank transactions. Current general ledger impact as of 2026-05-23:

- Creating, editing, reordering, importing, disabling, or deleting rules does not post to the general ledger.
- Rules can prefill GL account/category choices or split instructions for pending bank transactions.
- A general ledger entry is created only later, when the bank transaction itself is confirmed from the Banking workflow.

## Common Mistakes

- Assuming rule creation or rule import confirms existing pending transactions automatically.
- Leaving overlapping rules in the wrong order and then getting the wrong suggestion first.
- Forgetting that a blank `Apply to accounts` scope means the rule can apply across all bank and credit card accounts.
- Using percent splits that do not total exactly `100%`.
- Using fixed-amount splits without setting `Balance to`.
- Making the description match too broad and catching unrelated transactions.

## Related Articles

- [Understand the banking page](./understand-the-banking-page.md)
- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Import bank transactions](./import-bank-transactions.md)

## Info

- App sections: `banking`, `rules`
- Last validated: 2026-06-04
- Screenshot status: `blocked`
