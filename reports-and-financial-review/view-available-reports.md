---
title: View Available Reports
summary: Open the Reports page, move between the available report tabs, set the date controls that apply to each tab, and run the report you want to review.
audience: End users
app_sections:
  - reports
workflow_type: reporting
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Reports.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/reports/ReportsPage.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/reports/reportCatalog.ts
last_validated: 2026-05-04
screenshot_status: not-started
owner: codex
---

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
   - Additional report views such as `General Ledger` and `Account Detail` are also supported by the current Reports page configuration.
4. Select the tab you want to run.
5. Set the date controls required for that tab:
   - Range-based reports use a period preset and date range.
   - As-of reports use an as-of style date.
   - `Income Statement` also supports compare-period controls and optional grouping.
   - `Tax Forms` requires a tax-form selection before you run it.
6. Select `Run`.
7. Review the table and any summary cards that appear for the selected report.
8. If needed, use `Export` to save the current report rows or `Print` to open the print workflow for the active report.

## Expected Result

The selected report loads in the main table area with the date context and controls that match that report type. Current general ledger impact as of 2026-05-04:

- Opening a report tab does not post anything to the ledger.
- Running a report reads posted data for the active company but does not change balances.
- Export and print are output actions only and do not create journal entries.

## Common Mistakes

- Forgetting to confirm the active company before running the report.
- Expecting every report tab to use the same date controls.
- Assuming a blank report means the report is broken, when it may mean there is no activity for the selected period.
- Treating `Export` as a way to move data back into SPRK. It is an outbound file action for the current report result.

## Related Articles

- [Review financial results inside the product](./review-financial-results-inside-the-product.md)
- [Use report drilldown behavior](./use-report-drilldown-behavior.md)
- [Interpret report navigation without accounting advice](./interpret-report-navigation-without-accounting-advice.md)
