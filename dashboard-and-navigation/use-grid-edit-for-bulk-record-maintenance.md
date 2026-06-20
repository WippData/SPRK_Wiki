# Use Grid Edit for Bulk Record Maintenance

Use Grid Edit when you need to clean up repeated list data faster than opening one drawer at a time.

![Column preferences dialog showing drag handles and move controls for supported list columns](../screenshots/preferences-and-personalization/column-preferences-drag-handles-step-01.png)

## When To Use This

Use this workflow when you want to make the same kind of careful cleanup across several records, especially after an import, during list cleanup, or while reviewing a table before individual drawer edits would be slower.

## Before You Start

- You can open a supported list page such as `Items`, `Customers`, `Vendors`, `Checks`, or a supported `Banking` table.
- The active company shown in the sidebar is the company you intend to review before you make changes.
- You understand which fields should be reviewed carefully before applying bulk edits.

## Good Uses for Grid Edit

- Cleaning up customer, vendor, or item names after setup.
- Filling repeated non-posting fields that were missed during import.
- Reviewing a list for consistent defaults before heavy transaction entry.
- Preparing pending bank rows for review before the final confirm step.

## Use Extra Caution

- Do not bulk edit fields when you are unsure which records belong to the active company.
- Do not treat Grid Edit as a substitute for source-document review.
- Do not change account, vendor, customer, or item fields in bulk without checking the accounting impact.
- In Banking, applying grid edits is not the same as confirming transactions.

## Steps

1. Open a supported list page such as `Items`.
2. Choose how you want the page to open:
   - Turn on `Grid Edit default` in `Preferences` if you want supported pages to start in grid mode automatically.
   - Or open the page normally, select `More`, and choose `Enable Grid Mode` when needed.
3. When the page is in grid mode, confirm the toolbar shows the changed-cell count plus `Discard` and `Apply Changes`.
4. Review the table before editing:
   - Confirm you are on the correct list page.
   - Confirm the visible columns match the fields you want to review.
5. Click directly into the cells you want to update.
6. Make the repeated edits you need across the grid.
7. Watch the changed-cell counter while you work so you know whether there are unapplied edits.
8. Review the edited cells before you continue.
9. Select `Apply Changes` only after the grid reflects the final values you intend to keep.
10. If you want to leave grid mode, select `More` and choose `Disable Grid Mode`.
11. If you want to change which columns stay visible or where they appear, return to the standard list view and open `Column preferences`:
   - Turn optional columns on or off as needed.
   - Drag a column's reorder handle when you want to move it into place quickly.
   - Use the move-up and move-down controls when you prefer button controls or need a steadier one-step move.
   - Leave required columns visible when SPRK keeps them protected.
12. Use row actions in the standard list view when you need a single-record `View`, `Edit`, or delete workflow instead of a table-wide cleanup pass.

## Banking-Specific Selection Behavior

Banking uses Grid Edit for transaction-review cleanup, but Banking also has posting-sensitive bulk actions. Treat those actions separately from ordinary changed-cell tracking:

- The standard Banking `Pending` table uses checkboxes to select rows for actions such as applying an account, applying a vendor, confirming selected rows, or deleting selected rows.
- Banking Grid Edit can expose selected-row actions in the same toolbar, including `Confirm selected`, when row selection is available in that mode.
- Row selection is Banking-specific guidance. Do not assume every Grid Edit table in SPRK supports selected rows or an in-grid confirmation action.
- If the Banking changed-cell counter is active, apply or discard those Grid Edit changes before running bulk account, vendor, confirm, delete, or select-categorized actions.
- Applying Grid Edit changes saves the draft cell edits; confirming a bank transaction is still the step that posts or links the ledger result.

## What Happens Next

You can review and apply repeated list updates from one table instead of opening each record individually.

- Entering or reviewing draft grid changes does not post to the general ledger by itself.
- Applying list edits updates the saved record data for that page, not a new journal-entry workflow.
- On Banking, applying draft Grid Edit changes prepares selected rows for review, but it does not replace the separate transaction confirmation step.
- The accounting impact still depends on the fields and downstream workflows tied to the records you changed.
- Banking confirmation remains a separate posting workflow; apply any draft grid edits before using bulk Banking actions such as confirm selected.

## If Something Looks Wrong

- Using Grid Edit for broad cleanup without first confirming you are on the correct page and company context.
- Applying several edits at once without reviewing the changed-cell count and final cell values.
- Assuming every list page exposes the same columns or the same editing depth.
- Assuming every Grid Edit table supports Banking-style selected-row actions.
- Trying to run Banking bulk actions before applying or discarding draft Grid Edit changes.
- Forgetting that column preferences affect how the list is displayed, not the underlying accounting logic.
- Assuming drag reordering is available on every table; use the visible `Column preferences` controls for the page you are on.
- Looking for `Column preferences` while still in grid mode. In the current Items workflow, that control is visible in the standard list view.

## Related

- [Use the Preferences tab](../preferences-and-personalization/use-the-preferences-tab.md)
- [Understand personalization boundaries and saved behavior](../preferences-and-personalization/understand-personalization-boundaries-and-saved-behavior.md)
- [Manage items for invoicing](../sales-and-receivables/manage-items-for-invoicing.md)
- [Manage customers](../sales-and-receivables/manage-customers.md)
- [Manage vendors](../expenses-and-payables/manage-vendors.md)
- [Work with checks](../expenses-and-payables/work-with-checks.md)
- [Review and classify bank transactions](../banking-and-cash-management/review-and-classify-bank-transactions.md)
- [Before you import](../company-setup-and-migration/before-you-import.md)
