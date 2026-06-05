# View Available Reports

Open the Reports page, move between the available report tabs, set the date controls that apply to each tab, and run the report you want to review.

## Purpose

Use this workflow when you want to see which reports are available in SPRK and run the one that fits the review you need.

## Prerequisites

- You are signed in to SPRK.
- The correct active company is selected.
- The company has posted activity if you expect the report to show balances or transactions.

## Steps

1. Open `Reports` from the left sidebar.
2. Confirm the page header shows `Reports`.
3. Review the report tabs currently exposed on the page. SPRK currently supports report views for:
   - `Trial Balance`
   - `Income Statement`
   - `Balance Sheet`
   - `Cash Flow (Indirect)`
   - `Tax Forms`
   - `Reconciliation`
   - Transaction-detail views such as `General Ledger` and `Account Detail` are also available.
4. Select the tab you want to run.
5. Set the date controls required for that tab:
   - Range-based reports use a period preset and date range.
   - As-of reports use an as-of style date.
   - `Income Statement` also supports compare-period controls and optional grouping.
   - `Tax Forms` requires a tax-form selection before you run it.
   - `Reconciliation` requires an account and posted statement period.
   - `General Ledger` adds filters for `Account Type`, `Account SubType`, `Accounts`, `Vendor`, `Text`, `Group By`, and optional `Include opening balance`.
6. Select `Run`.
7. Review the table and any summary cards that appear for the selected report.
   - In `General Ledger`, use `Group By` when you want the results collapsed by `Account Type`, `SubType`, or `Type & SubType` before you expand to account-level detail.
8. If needed, use `Export` to save the current report rows or `Print` to open the print workflow for the active report.

## Expected Result

The selected report loads in the main table area with the date context and controls that match that report type. Current general ledger impact as of 2026-06-04:

- Opening a report tab does not post anything to the ledger.
- Running a report reads posted data for the active company but does not change balances.
- Export and print are output actions only and do not create journal entries.
- Reconciliation reports are review outputs for posted reconciliation sessions and do not create new ledger activity.

## Common Mistakes

- Forgetting to confirm the active company before running the report.
- Expecting every report tab to use the same date controls.
- Assuming a blank report means the report is broken, when it may mean there is no activity for the selected period.
- Treating `Export` as a way to move data back into SPRK. It is an outbound file action for the current report result.

## Related Articles

- [Review financial results inside the product](./review-financial-results-inside-the-product.md)
- [Export transactions from reports](./export-transactions-from-reports.md)
- [Use report drilldown behavior](./use-report-drilldown-behavior.md)
- [View and print bank reconciliation reports](../reconciliation/view-and-print-bank-reconciliation-reports.md)
- [Interpret report navigation without accounting advice](./interpret-report-navigation-without-accounting-advice.md)

## Info

- App sections: `reports`
- Last validated: 2026-06-05
- Screenshot status: `blocked`
