# Set Up Vendor Default Expense Accounts

Prepare vendor-level expense defaults before you enter repeat payables, checks, or bank classifications so supported workflows start with cleaner coding.

![Vendors list showing the Default Expense Account column](../screenshots/expenses-and-payables/vendor-default-expense-account-step-01.png)

## When To Use This

Use this page when the same vendor usually points to the same expense account and you want SPRK to reuse that setup where the current workflow supports it.

## Why This Matters

- Vendor setup can carry a `Default Expense Account`.
- Clean vendor setup also helps vendor-aware bank imports resolve vendor columns by exact active vendor ID or uniquely matched active vendor name when that workflow is available.
- Supported workflows can reuse that default instead of making you recategorize the same vendor repeatedly.
- The default helps reduce cleanup work later when you review vendor activity and expense reporting.
- A saved default does not replace review. You should still confirm the final account before you save or confirm a transaction.

## Before You Start

- You can open `Vendors`.
- The expense account you want to reuse already exists, is active, and is eligible for posting. Nonposting summary accounts and restricted control accounts may stay visible in `Chart of Accounts` but be omitted from default-account selectors.
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
- In `Bills`, a vendor or header default can help fill blank line accounts, but each bill line still needs review before posting.
- In `Banking`, selecting or changing a vendor can fill the transaction's GL account/category when no manual category, split, or rule already controls the transaction.
- In vendor-aware bank-import preview, exact active vendor IDs and uniquely matched active vendor names can resolve imported vendor columns. Unresolved names stay visible until you choose a vendor, create the unknown vendors from the preview, or leave the row for later review.
- If Banking prompts before saving a placeholder-style vendor default such as `Ask My Accountant`, `Pending`, or `TBD`, review the warning before you let that account become the vendor's reusable default.
- Vendor imports can map or resolve the default expense account during setup review.
- Vendor and customer list columns show readable account labels for saved defaults where the current UI exposes those columns, not raw stored account IDs.

## Where You Should Still Review Manually

- Bills still need line-by-line account review before you save them as `Open`.
- `Default Expense Account` and bill header `Default expense account` are fallback helpers; the bill line `Account` is the posting source.
- A rule can take priority over a vendor default in banking workflows.
- A manual category or saved split should stay in control once you have already chosen a more specific result.
- Mixed-use vendors may need one-off exceptions even when a default is usually helpful.

## What Happens Next

The vendor record carries a reusable expense default, and supported check and banking workflows can start from cleaner coding with less repetitive entry.

## If Something Looks Wrong

- Treating the default as a guarantee that every vendor transaction belongs to one account.
- Assuming the default replaces bill-line review in payables workflows.
- Forgetting to update the vendor when its usual expense category changes.
- Assuming a vendor default overrides a rule or a manual banking category every time.
- Choosing an account without confirming that it is the active expense account you actually want to reuse.
- Looking for a nonposting parent account in the default selector. Choose the posting account that should receive vendor activity.

## Related

- [Manage vendors](./manage-vendors.md)
- [Create and manage bills](./create-and-manage-bills.md)
- [Work with checks](./work-with-checks.md)
- [Review common payables workflows](./review-common-payables-workflows.md)
- [Review and classify bank transactions](../banking-and-cash-management/review-and-classify-bank-transactions.md)
