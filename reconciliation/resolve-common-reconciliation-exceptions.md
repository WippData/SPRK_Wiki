# Resolve Common Reconciliation Exceptions

Diagnose the most common reasons a reconciliation cannot start or finish cleanly, including first-time setup issues, date-window issues, and nonzero differences.

## Purpose

Use this article when reconciliation stops with a validation error, an unexpected difference, or a transaction-selection problem.

## Prerequisites

- You are working in `Reconcile`.
- You know which bank or credit card account and statement period you are trying to reconcile.

## Steps

1. If SPRK says `Select the opening balance journal entry`, start with the first-time setup path:
   - Choose the journal entry that represents the account's opening balance anchor.
   - Confirm that the selected entry belongs to the account you are reconciling.
2. If SPRK says the difference must be zero, compare the summary bar to the statement:
   - Remove transactions that do not belong on the statement.
   - Add missing confirmed transactions that do belong on the statement.
   - Verify the ending balance sign, especially for credit accounts.
3. If a transaction is missing from the reconciliation table, confirm that it is:
   - In the selected account
   - Already confirmed
   - Dated on or before the statement ending date
   - Not already reconciled
4. If a match is wrong, use `Unmatch` before finishing the reconciliation and choose the correct check again if needed.
5. If SPRK reports that a transaction is already reconciled, remove it from your current plan and confirm whether it was cleared in an earlier statement period.
6. If the transaction coding is wrong and the row has an enabled `Journal` action, open the linked journal entry and reverse it before adding the corrected activity.
7. If the opening balance looks unexpected, confirm whether SPRK is carrying forward the ending balance from the last posted reconciliation before the current statement ending date.
8. If a reconciliation report appears blank, confirm that the selected account has a posted reconciliation period. The Reports `Reconciliation` tab shows a no-posted-reconciliations message when there is no posted history for the account.

## Expected Result

You can identify whether the issue is caused by account selection, transaction status, statement setup, linked journal activity, or the first-time opening balance path. Current transaction and general ledger impact as of 2026-05-29:

- Troubleshooting steps do not create new general ledger entries by themselves.
- Correcting a reconciliation issue usually means adjusting transaction selection, dates, balances, or match state before posting the reconcile record.
- If you must change original transaction coding on a row with a linked journal entry, reversing from the linked journal creates a separate reversal entry and then preserves or corrects the bank row based on whether it was already reconciled.

## Common Mistakes

- Trying to solve a reconciliation difference by leaving incorrect transactions selected.
- Using reconciliation to fix posting mistakes that should be corrected in the original banking, invoice, bill, or journal-entry workflow.
- Forgetting that already reconciled transactions cannot be reused in a later statement period.
- Reversing a linked journal without checking whether the correction date belongs in the current statement period.

## Related Articles

- [Start a reconciliation](./start-a-reconciliation.md)
- [Match and unmatch transactions](./match-and-unmatch-transactions.md)
- [Finish a reconciliation](./finish-a-reconciliation.md)
- [View and print bank reconciliation reports](./view-and-print-bank-reconciliation-reports.md)
- [Edit linked ledger and bank activity](../ledger-and-chart-of-accounts/edit-linked-ledger-and-bank-activity.md)

## Info

- App sections: `reconcile`
- Last validated: 2026-06-05
- Screenshot status: `partial`
