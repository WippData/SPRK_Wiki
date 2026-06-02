# Work With Checks

Create, update, match, unmatch, void, and delete checks while understanding what the current check workflow does and does not post to the ledger.

## Purpose

Use this workflow when you need to track a check, keep its status current, and connect it to related bank activity during reconciliation work.

## Prerequisites

- You can open the `Checks` page.
- A bank account exists for the check.
- You know the payee, date, and amount you want to record.

## Steps

1. Open `Checks`.
2. Select `New`.
3. Complete the check fields:
   - `Vendor`, if you want to reuse a saved vendor record.
   - `Bank Account`
   - `Check #`, if used
   - `Date`
   - `Payee`
   - `Amount`
   - `Offset Account`
   - `Memo`
   - `Status`
4. If the selected vendor already has a saved default expense account and `Offset Account` is still blank, review the filled account before you continue.
5. Save the check as `Draft` if it is not ready to issue yet, or as `Issued` when it should be treated as an active check record.
6. Use the row actions later as needed:
   - `View` to review the record
   - `Edit` to update a draft or issued check
   - `Match` to connect the check to a bank line
   - `Unmatch` to remove that connection when allowed
   - `Void` to mark the check voided
   - `Delete` to remove a draft check
7. Review the `Status`, `Bank`, and `Memo` columns in the list after each action.

## Expected Result

The check is stored and can move through draft, issued, matched, cleared, voided, or deleted states based on the current workflow. Current general ledger impact as of 2026-05-02:

- Creating or editing a check record does not post a separate journal entry in the current `Checks` workflow.
- Matching a check links it to a bank transaction and changes operational status, but that match action is not documented here as creating its own new journal entry.
- Void and delete actions update the check record and matching state, not a separate check-specific posting flow.

## Common Mistakes

- Assuming the `Checks` page is the same as recording a bill payment.
- Treating `Draft` and `Issued` as interchangeable when other team members rely on status.
- Accepting a filled `Offset Account` without confirming it still matches the purpose of this check.
- Trying to delete a non-draft check. The current workflow only allows draft checks to be deleted.
- Assuming voiding a check is the same as clearing it through reconciliation.

## Related Articles

- [Set up vendor default expense accounts](./set-up-vendor-default-expense-accounts.md)
- [Create and manage bills](./create-and-manage-bills.md)
- [Review common payables workflows](./review-common-payables-workflows.md)
- [Manage vendors](./manage-vendors.md)

## Info

- App sections: `checks`
- Last validated: 2026-06-01
- Screenshot status: `planned`
