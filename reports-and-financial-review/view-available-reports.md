# View Available Reports

![Reports page showing available report tabs and controls](../screenshots/reports-and-financial-review/reports-overview-step-01.png)

Open the Reports page, move between the available report tabs, set the date controls that apply to each tab, and run the report you want to review.

## When To Use This

Use this workflow when you want to see which reports are available in SPRK and run the one that fits the review you need.

## Before You Start

- You are signed in to SPRK.
- The correct active company is selected.
- The company has posted activity if you expect the report to show balances or transactions.

## Steps

1. Open `Reports` from the left sidebar.
2. Confirm the page header shows `Reports`.
3. Choose the report that matches your review question:
   - `Trial Balance` for account balances by debit and credit.
   - `Income Statement` for income, expenses, and net income.
   - `Balance Sheet` for assets, liabilities, and equity.
   - `Cash Flow (Indirect)` for cash flow review.
   - `Tax Forms` for tax-form review where available.
   - `General Ledger` for posted transaction detail by account.
   - `Account Detail` for one account's activity.
   - `Expense by Vendor` for vendor spending and 1099-oriented review.
   - `Receivables Aging` for unpaid customer balances.
   - `Payables Aging` for unpaid vendor balances.
   - `Reconciliation` for posted reconciliation reports.
4. Select the tab you want to run. Use the tab overflow menu if a report is not visible in the first row.
5. Set the date controls required for that tab:
   - Range-based reports use a period preset and date range.
   - As-of reports use an as-of style date.
   - Date fields can be selected from the calendar or typed directly. Typed dates should follow your saved `Preferences` date order, and accepted compact entries can normalize to the visible display format.
   - `Income Statement` also supports compare-period controls and optional grouping.
   - `Tax Forms` requires a tax-form selection before you run it.
   - `Expense by Vendor`, aging reports, and `Reconciliation` require the filters shown on their tabs.
   - `General Ledger` adds filters for `Account Type`, `Account SubType`, `Accounts`, `Vendor`, `Text`, `Group By`, and optional `Include opening balance`.
6. Select `Run`.
7. Review the table and any summary cards that appear for the selected report.
   - In `General Ledger`, use `Group By` when you want the results collapsed by `Account Type`, `SubType`, or `Type & SubType` before you expand to account-level detail.
   - On supported statement reports, non-zero summary cards, subtotals, totals, and rows can open supporting-entry drilldown.
   - Visible statement row order follows account code when codes are present and falls back to account name when codes are blank.
8. If needed, use `Export` to save the current report rows or `Print` to open the print workflow for the active report.
9. Treat `Tax Forms` as a review view where visible, not as tax return preparation, tax filing, agency submission, or compliance approval.

## What Happens Next

The selected report loads in the main table area with the date context and controls that match that report type.

- Opening a report tab does not post anything to the ledger.
- Running a report reads posted data for the active company but does not change balances.
- Export and print are output actions only and do not create journal entries.
- The visible `Export` action exports the active report context. Do not assume a separate batch or package export exists unless SPRK shows that action.
- Reconciliation reports are review outputs for posted reconciliation sessions and do not create new ledger activity.
- Tax-form review does not file tax returns, submit agency forms, or replace professional compliance review.

## If Something Looks Wrong

- Forgetting to confirm the active company before running the report.
- Expecting every report tab to use the same date controls.
- Typing report dates in a different order than the date format saved in `Preferences`.
- Assuming a blank report means the report is broken, when it may mean there is no activity for the selected period.
- Treating `Export` as a way to move data back into SPRK. It is an outbound file action for the current report result.
- Treating `Tax Forms` as tax filing or compliance approval instead of report review.

## Related

- [Review financial results inside the product](./review-financial-results-inside-the-product.md)
- [Export transactions from reports](./export-transactions-from-reports.md)
- [Use report drilldown behavior](./use-report-drilldown-behavior.md)
- [View and print bank reconciliation reports](../reconciliation/view-and-print-bank-reconciliation-reports.md)
- [Use the Preferences tab](../preferences-and-personalization/use-the-preferences-tab.md)
