# Resolve Common Reconciliation Exceptions

![Active reconciliation summary showing cleared balance and difference](../screenshots/reconciliation/reconciliation-active-summary-step-01.png)

Diagnose the most common reasons a reconciliation cannot start or finish cleanly, including first-time setup issues, date-window issues, and nonzero differences.

## When To Use This

Use this article when reconciliation stops with a validation error, an unexpected difference, or a transaction-selection problem.

## Before You Start

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
   - Not already reconciled
   - Not excluded from bank review
   - A row that belongs on the statement you are reconciling
   - If the transaction date is after the statement ending date, verify whether the statement actually cleared it in this period before selecting it.
4. If a match is wrong, use `Unmatch` before finishing the reconciliation and choose the correct check again if needed.
5. If SPRK reports that a transaction is already reconciled, remove it from your current plan and confirm whether it was cleared in an earlier statement period.
6. If the transaction coding is wrong and the row has an enabled `Journal` action, open the linked journal entry and reverse it before adding the corrected activity.
   - If the journal is tied to an invoice or bill, SPRK may ask for source-document confirmation before reversing.
   - Recognition postings can require voiding the invoice or bill with the reversal.
   - Payment postings can require reversing the payment application so the invoice or bill balance reopens correctly.
7. If the confirmed bank row has no journal link, or the link points to the wrong accounting evidence, return to `Banking` > `Categorized` and use `Resolve` where it is visible.
   - Link only to a reviewed existing GL line.
   - Use the create-GL path only when the bank row's category or split is correct.
   - Removing a GL link does not remove the confirmed bank row from reconciliation history.
8. If the opening balance looks unexpected, confirm where it came from:
   - For a first-time reconciliation, verify the selected opening-balance journal entry, posting date, account line, and amount before completing the anchor.
   - For a later reconciliation, compare the current beginning balance to the ending balance on the last posted reconciliation for the same account before the current statement ending date.
   - Do not create an extra journal entry just to force the reconciliation beginning balance to change unless the underlying books are actually wrong.
9. If journal activity that affects a historical opening balance was edited or reversed after reconciliation work started, review both sides of the issue:
   - General-ledger reports follow the supported ledger edit, reversal, or correction.
   - Posted reconciliation history remains the record of what was reconciled for that statement period and is not automatically recalculated from the changed ledger activity.
10. If the wrong first-time opening anchor was selected and it has not been completed, go back through the start flow and choose the correct `Opening balance journal entry`.
11. If the wrong balance is already part of posted reconciliation history, use [Common accountant corrections](../ledger-and-chart-of-accounts/common-accountant-corrections.md) to choose the source-document, journal reversal, or correcting-entry path that matches the accounting error. Then reconcile the correction in the statement period where it belongs.
12. If you are finishing a quiet period with no statement-cleared transactions, verify that the beginning and ending balances support a zero-difference reconciliation before posting.
13. If a reconciliation report appears blank, confirm that the selected account has a posted reconciliation period. The Reports `Reconciliation` tab shows a no-posted-reconciliations message when there is no posted history for the account.

## Correcting Historical Opening-Balance Errors

SPRK does not use reconciliation as a separate ledger-adjustment tool. Correct the books only when the underlying accounting is wrong; otherwise, correct the reconciliation setup before posting or preserve the posted reconciliation evidence with a clear explanation of the historical issue.

- Preserve the prior reconciliation report or export that shows the original posted period.
- Identify the source of the beginning balance: the first-time opening-balance journal entry or the prior posted reconciliation ending balance.
- Keep the bank or credit card statement evidence that proves the expected beginning and ending balances.
- Use [Common accountant corrections](../ledger-and-chart-of-accounts/common-accountant-corrections.md) before changing the books, and use [Edit linked ledger and bank activity](../ledger-and-chart-of-accounts/edit-linked-ledger-and-bank-activity.md) when the issue starts from a reconciled row with a linked journal.
- Include a clear memo, description, or firm workpaper note explaining why the correction was made and which statement period it affects.
- After the correction, review the relevant general-ledger detail, reconciliation history, and bank reconciliation report so the ledger correction and reconciliation evidence can be followed separately.

## What Happens Next

You can identify whether the issue is caused by account selection, transaction status, statement setup, linked journal activity, or the first-time opening balance path.

- Troubleshooting steps do not create new general ledger entries by themselves.
- Correcting a reconciliation issue usually means adjusting transaction selection, dates, balances, status, exclusion state, or match state before posting the reconcile record.
- Reconciliation beginning balances are carried from the first anchor or prior posted reconciliation history.
- If you must change original transaction coding on a row with a linked journal entry, reversing from the linked journal creates a separate reversal entry and then preserves or corrects the bank row based on whether it was already reconciled.
- Confirmed unreconciled rows can appear for review even when their transaction date is after the statement ending date. Select them only when your statement evidence supports that later-dated item clearing in the current period.
- `Resolve` can repair a confirmed bank row's GL link, but it is not a reconciliation finish action and does not clear the row by itself.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| The action is unavailable or does not complete | Trying to solve a reconciliation difference by leaving incorrect transactions selected | Use the supported prerequisite or correction path first |
| The current page does not fit the task | Using reconciliation to fix posting mistakes that should be corrected through [banking review](../banking-and-cash-management/review-and-classify-bank-transactions.md), [invoices](../sales-and-receivables/create-and-open-invoices.md), [bills](../expenses-and-payables/create-and-manage-bills.md), or [journal entries](../ledger-and-chart-of-accounts/record-journal-entries.md) | Return to the workflow this page supports |
| A needed review step is missing | Forgetting that already reconciled transactions cannot be reused in a later statement period | Go back to that check before continuing |
| The result looks ready, but a key check is unresolved | Assuming every selectable row must be dated on or before the statement ending date | Confirmed unreconciled later-dated rows can appear when they may belong to the statement clearing period |
| The result does not match what you expected | Reversing a linked journal without checking whether the correction date belongs in the current statement period | Review the visible state and use the related workflow before continuing |
| The result does not match what you expected | Reversing an invoice-linked or bill-linked journal without reading the source-document impact confirmation | Review the visible state and use the related workflow before continuing |
| You are about to take an action that may affect the result | Posting a quiet-period reconciliation without confirming the zero-difference summary | Confirm the visible company, page, and workflow state before continuing |
| The current page does not fit the task | Using `Resolve` to bypass normal reconciliation selection and finish controls | Return to the workflow this page supports |
| You are about to take an action that may affect the result | Creating a new [journal entry](../ledger-and-chart-of-accounts/record-journal-entries.md) only to change the reconciliation beginning balance when the books themselves are not wrong | Confirm the visible company, page, and workflow state before continuing |

## Related

- [Start a reconciliation](./start-a-reconciliation.md)
- [Match and unmatch transactions](./match-and-unmatch-transactions.md)
- [Finish a reconciliation](./finish-a-reconciliation.md)
- [View and print bank reconciliation reports](./view-and-print-bank-reconciliation-reports.md)
- [Edit linked ledger and bank activity](../ledger-and-chart-of-accounts/edit-linked-ledger-and-bank-activity.md)
- [Common accountant corrections](../ledger-and-chart-of-accounts/common-accountant-corrections.md)
