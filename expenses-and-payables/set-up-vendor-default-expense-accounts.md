# Set Up Vendor Default Expense Accounts

Prepare vendor-level expense defaults before you enter repeat payables, checks, or bank classifications so supported workflows start with cleaner coding.

## Purpose

Use this page when the same vendor usually points to the same expense account and you want SPRK to reuse that setup where the current workflow supports it.

## Why This Matters

- Vendor setup can carry a `Default Expense Account`.
- Supported workflows can reuse that default instead of making you recategorize the same vendor repeatedly.
- The default helps reduce cleanup work later when you review vendor activity and expense reporting.
- A saved default does not replace review. You should still confirm the final account before you save or confirm a transaction.

## Prerequisites

- You can open `Vendors`.
- The expense account you want to reuse already exists and is active.
- You know which vendors usually post to the same expense category.

## Setup Workflow

1. Open `Vendors`.
2. Create a vendor or edit an existing one.
3. Review the main contact fields first so the vendor record is easy to find later.
4. In `Default Expense Account`, choose the expense account you usually want to use with this vendor.
5. Save the vendor.
6. Revisit the default later if the vendor starts crossing multiple expense categories often enough that a single default stops being useful.
7. If you import vendor records, review any imported default expense account mappings before relying on them in day-to-day work.

## Where SPRK Can Use This Default

- In `Checks`, selecting a vendor can fill `Offset Account` when that field is still blank.
- In `Banking`, selecting or changing a vendor can fill the transaction's GL account/category when no manual category, split, or rule already controls the transaction.
- If Banking prompts before saving a placeholder-style vendor default such as `Ask My Accountant`, `Pending`, or `TBD`, review the warning before you let that account become the vendor's reusable default.
- Vendor imports can map or resolve the default expense account during setup review.

## Where You Should Still Review Manually

- Bills still need line-by-line account review before you save them as `Open`.
- A rule can take priority over a vendor default in banking workflows.
- A manual category or saved split should stay in control once you have already chosen a more specific result.
- Mixed-use vendors may need one-off exceptions even when a default is usually helpful.

## Expected Result

The vendor record carries a reusable expense default, and supported check and banking workflows can start from cleaner coding with less repetitive entry.

## Common Mistakes

- Treating the default as a guarantee that every vendor transaction belongs to one account.
- Assuming the default replaces bill-line review in payables workflows.
- Forgetting to update the vendor when its usual expense category changes.
- Assuming a vendor default overrides a rule or a manual banking category every time.
- Choosing an account without confirming that it is the active expense account you actually want to reuse.

## Related Articles

- [Manage vendors](./manage-vendors.md)
- [Create and manage bills](./create-and-manage-bills.md)
- [Work with checks](./work-with-checks.md)
- [Review common payables workflows](./review-common-payables-workflows.md)
- [Review and classify bank transactions](../banking-and-cash-management/review-and-classify-bank-transactions.md)

## Info

- App sections: `vendors`, `checks`, `banking`
- Last validated: 2026-06-04
- Screenshot status: `blocked`
