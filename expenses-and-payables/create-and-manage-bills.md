# Create and Manage Bills

![New bill drawer for entering vendor bill details](../screenshots/expenses-and-payables/new-bill-drawer-step-01.png)

![New bill drawer showing Pay from, default expense account, and line account](../screenshots/expenses-and-payables/bill-routing-fields-step-01.png)

![Bill row actions for payment history and linked journal review](../screenshots/expenses-and-payables/bill-payment-history-actions-step-01.png)

Enter vendor bills, decide whether they stay in draft, post through Accounts Payable, or settle immediately, and record bill payments from the Bills page.

## When To Use This

Use this workflow when you need to enter a vendor bill, recognize the payable, and record payment against the bill from inside SPRK.

## Before You Start

- A vendor record exists.
- The expense or other posting accounts for the bill lines are available.
- You know whether this bill should use an Accounts Payable control account or a cash, bank, or credit-card settlement account in `Pay from`.
- If you plan to record payment, the cash or bank account you want to pay from is available.

## Steps

1. Open `Bills`.
2. Select `New`.
3. Complete the bill header:
   - `Bill #`
   - `Vendor`
   - `Pay from`
   - `Default expense account`
   - `Date`
   - `Due date`
   - `Status`
   - `Terms`, if needed
4. Choose `Pay from` carefully:
   - Use an Accounts Payable control account when the bill should stay on the open accrual path.
   - Use a cash, bank, or credit-card settlement account only when the bill is being recorded as paid immediately.
   - Payables control routing and settlement-account routing are alternative paths, not two fields to combine on the same bill.
5. Add one or more bill lines.
6. For each line, choose the `Account` that should receive the expense or other debit.
   - `Default expense account` fills blank line accounts when the drawer supports that fallback.
   - The line-level `Account` is the posting source for that line.
7. Complete the line description, quantity, unit cost, and review the calculated amount.
8. Add `Tax total` or `Memo` if needed.
9. Decide how the bill should be saved:
   - `Draft` stores the bill without posting Accounts Payable.
   - `Open` stores the bill and posts the payable when `Pay from` is an Accounts Payable control account.
   - Choosing a settlement account in `Pay from` can route the bill through the paid-now path instead of leaving an open payable.
10. Save the bill.
   - If you edit and save a bill that has already posted, SPRK can show `Save Posted Bill` before it changes the posting.
   - Review the available strategy before continuing: `Post adjustment journal entry`, `Reverse and repost`, or `Edit existing journal entry`.
   - Adjustment dates can use `Today`, `Original posting date`, or `Custom date`.
   - Reversal dates can use `Original posting date`, `Today`, or `Custom date`; repost dates can use `Document date`, `Today`, or `Custom date`.
   - Changes to `Pay from`, line accounts, default expense account, dates, totals, or posted status are accounting-sensitive once the bill has posted.
11. Review the bill list to confirm the expected `Status`, `Total`, and `Balance`.
12. When you are ready to record payment, use the dollar action for the bill.
13. In `Record payment`, complete:
   - `Payment date`
   - `Amount`
   - `Pay from`
   - `Reference #`, if needed
   - `Memo`
14. Record the payment and confirm the updated balance and status in the bill list.
15. To review later, use the row action menu for `View payment history` or `View linked journal entries`.

## Available Bill Actions

The row action menu changes based on the bill's status, balance, and posting history. Use the visible actions on the bill row rather than assuming every bill supports the same correction path. Common actions include recording a payment, matching a payment, viewing linked journal entries, viewing payment history, voiding eligible posted bills, and deleting eligible draft records.

If you need to correct a posted bill or bill payment, prefer the supported correction action SPRK shows for that record. Do not delete a source record just to force the ledger to match.

## Void an Eligible Bill

Use `Void bill` when a posted bill should be reversed while preserving the original bill and posting history.

1. Open the bill row action menu.
2. Choose `Void bill` only when the action is enabled.
   - The action can appear on posted-like bills.
   - It is enabled only when the bill is still `Open` and its full balance still equals its total.
   - Draft, partial, paid, and already voided bills are not valid void targets.
3. In the `Void bill` modal, choose the void posting date:
   - `Today`
   - `Original bill date`
   - `Custom date`
4. Enter a reason.
5. Confirm `Void bill` after reviewing the bill and date.

## Banking Match Path

When the vendor payment first appears as a pending money-out row in `Banking`, use `Match bank transaction` when available. SPRK can suggest open bills, show the candidate number, vendor, dates, open amount, bank amount, and difference, then use `Pay Bill & Confirm` or `Pay Partial & Confirm` when the bank amount is eligible. Overpayments are not actionable from that Banking match path.

## Import Bill Files

Use bill import when you already have grouped vendor bill rows in a spreadsheet or CSV and want SPRK to create documents after preview.

- Grouped rows can use visible headers such as `Vendor Name`, `Due Date`, `Account ID`, `Memo`, `Status`, `Terms`, `Currency`, `Tax Total`, `Amount`, and `Line Amount`.
- Account-routing headers can include `Pay from`, `Default Expense Account`, and `Line Account`.
- `Pay from` follows the same routing rule as the drawer: an Accounts Payable control account keeps the imported bill on the accrual path, while a non-control cash, bank, or credit-card settlement account imports as paid-now.
- `Default Expense Account` fills blank line accounts; `Line Account` remains the posting source of truth.
- SPRK expects a vendor, at least one line, valid line account details, positive quantities, and non-duplicate bill numbers.
- Imports that try to mix payables control routing and settlement-account routing for the same bill are rejected instead of silently guessing the posting path.

## What Happens Next

The bill is saved and appears in the bill list.

- Saving a bill as `Draft` does not post a journal entry.
- Saving a bill as `Open`, or updating a bill from a non-open status to `Open`, posts one recognition entry when `Pay from` is an Accounts Payable control account:
  - Debit each bill line `Account` for that line amount.
  - Credit the selected Accounts Payable control account for the total bill amount.
- Saving a paid-now bill with a cash, bank, or credit-card settlement account in `Pay from` posts directly between the bill line accounts and that settlement account.
- Recording a bill payment posts a separate payment entry:
  - Debit the payable account carried by the open bill.
  - Credit the selected `Pay from` account.
- Full payment changes the bill to `Paid`. A smaller payment leaves the bill as `Partial`.
- Saving changes to an already posted bill follows the posted-save strategy you choose when SPRK prompts. `Edit existing journal entry` can be unavailable when company policy or prior adjustment history does not allow it.
- Viewing payment history or linked journal entries does not post by itself.
- A successful `Void bill` posts a reversal journal entry, sets the bill status to `Void`, zeroes the bill balance, and records void details instead of deleting the bill.
- If a bill has active payments, SPRK blocks voiding or recognition-journal reversal until those payments are reversed or unapplied.
- Reversing a bill-payment journal through a supported source-document confirmation can deactivate the payment application and reopen the bill balance.

## If Something Looks Wrong

- Leaving a bill in `Draft` when you expected the payable to post.
- Choosing the wrong expense account on the bill line and then assuming SPRK will correct the ledger impact later.
- Choosing a cash or bank settlement account in `Pay from` when you meant to keep an unpaid vendor balance open.
- Assuming `Default expense account` posts by itself. Review line-level `Account` values before saving.
- Assuming a vendor default expense account replaces bill-line account review. Bill lines still need direct review before you open the bill.
- Recording a payment without checking the remaining balance first.
- Entering a payment amount larger than intended. Review overpayments carefully before recording them.
- Assuming delete or correction behavior reverses prior ledger impact automatically. Review the visible action and its confirmation before continuing.
- Trying to delete a posted bill. Only draft bills with no posted ledger impact can be deleted; posted bills need void or correction workflows.
- Trying to void a partially paid or paid bill directly. Reverse or unapply active payments first.
- Treating `Save Posted Bill` as a routine draft save. It is an audit-sensitive choice about how SPRK should preserve or adjust the posted entry.

## Business Scenario: Bill Review, Payment Trail, And Grouped Import

Use this scenario to train staff on bill detail review, bill action menus, payment history, linked journals, and the grouped-line CSV import claim for vendor bills.

- Sample files:
  - [13-ap-vendor-bill-payment.csv](../sample-files/v1-validation/13-ap-vendor-bill-payment.csv)
  - [14-bill-import-grouped-lines.csv](../sample-files/v1-validation/14-bill-import-grouped-lines.csv)
- Evidence:

![Bill detail showing vendor, dates, total, status, and balance](../screenshots/v1-validation/bill-open-detail.png)

![Bill actions menu showing payment, journal, history, and void options](../screenshots/v1-validation/bill-actions-menu-payment-journal-void.png)

![Bill payment history showing payment activity](../screenshots/v1-validation/bill-payment-history.png)

![Bill grid filtered to V1 imported bills showing grouped-line CSV import results](../screenshots/v1-validation/bill-import-grouped-lines-success-v0.3.57.png)

Validation note: the grouped bill import walkthrough passed in SPRK v0.3.57. The screenshot shows the two expected open bills created from [14-bill-import-grouped-lines.csv](../sample-files/v1-validation/14-bill-import-grouped-lines.csv).

## Related

- [Manage vendors](./manage-vendors.md)
- [Set up vendor default expense accounts](./set-up-vendor-default-expense-accounts.md)
- [Work with checks](./work-with-checks.md)
- [Review common payables workflows](./review-common-payables-workflows.md)
- [Review document payment history and linked journals](../ledger-and-chart-of-accounts/review-document-payment-history-and-linked-journals.md)
