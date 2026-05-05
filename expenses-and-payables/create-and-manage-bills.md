# Create and Manage Bills

Enter vendor bills, decide whether they stay in draft or post to Accounts Payable, and record bill payments from the Bills page.

## Purpose

Use this workflow when you need to enter a vendor bill, recognize the payable, and record payment against the bill from inside SPRK.

## Prerequisites

- A vendor record exists.
- The expense or other posting accounts for the bill lines are available.
- Your company has an Accounts Payable account configured.
- If you plan to record payment, the cash or bank account you want to pay from is available.

## Steps

1. Open `Bills`.
2. Select `New`.
3. Complete the bill header:
   - `Bill #`
   - `Vendor`
   - `Date`
   - `Due date`
   - `Status`
   - `Terms`, if needed
4. Add one or more bill lines.
5. For each line, choose the `Account` that should receive the expense or other debit.
6. Complete the line description, quantity, unit cost, and review the calculated amount.
7. Add `Tax total` or `Memo` if needed.
8. Decide how the bill should be saved:
   - `Draft` stores the bill without posting Accounts Payable.
   - `Open` stores the bill and posts the payable based on the current bills workflow.
9. Save the bill.
10. Review the bill list to confirm the expected `Status`, `Total`, and `Balance`.
11. When you are ready to record payment, use the dollar action for the bill.
12. In `Record payment`, complete:
   - `Payment date`
   - `Amount`
   - `Paid from`
   - `Reference #`, if needed
   - `Memo`
13. Record the payment and confirm the updated balance and status in the bill list.

## Expected Result

The bill is saved and appears in the bill list. Current general ledger impact as of 2026-05-02:

- Saving a bill as `Draft` does not post a journal entry.
- Saving a bill as `Open`, or updating a bill from a non-open status to `Open`, posts one recognition entry:
  - Debit each bill line `Account` for that line amount.
  - Credit `Accounts Payable` for the total bill amount.
- Recording a bill payment posts a separate payment entry:
  - Debit `Accounts Payable`.
  - Credit the selected `Paid from` account.
- Full payment changes the bill to `Paid`. A smaller payment leaves the bill as `Partial`.

## Common Mistakes

- Leaving a bill in `Draft` when you expected the payable to post.
- Choosing the wrong expense account on the bill line and then assuming SPRK will correct the ledger impact later.
- Recording a payment without checking the remaining balance first.
- Entering a payment amount larger than intended. Review overpayments carefully before recording them.
- Assuming delete or void behavior reverses prior ledger impact automatically. This article documents bill creation and payment behavior only.

## Related Articles

- [Manage vendors](./manage-vendors.md)
- [Work with checks](./work-with-checks.md)
- [Review common payables workflows](./review-common-payables-workflows.md)

## Info

- App sections: `bills`
- Last validated: 2026-05-02
- Screenshot status: `not-started`
