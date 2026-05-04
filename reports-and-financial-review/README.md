---
title: Reports and Financial Review
summary: Open the Reports area, choose the right report tab, run date-based financial views, drill into supporting detail when available, and understand that report actions do not change the general ledger.
audience: End users
app_sections:
  - reports
workflow_type: reference
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/pages/Reports.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/reports/ReportsPage.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-backend/internal/core/reports.go
last_validated: 2026-05-04
screenshot_status: not-started
owner: codex
---

## Purpose

Use this section when you need to open financial reports in SPRK, move between report tabs, review balances or activity for a date or period, and understand what report actions do and do not change.

## Prerequisites

- You are signed in to SPRK.
- `Demo Company` or another intended active company is selected before you run the report.
- The transactions you expect to review have already been posted in SPRK.

## Steps

1. Choose the workflow that matches your goal:
   - [View available reports](./view-available-reports.md)
   - [Use report drilldown behavior](./use-report-drilldown-behavior.md)
   - [Review financial results inside the product](./review-financial-results-inside-the-product.md)
   - [Interpret report navigation without accounting advice](./interpret-report-navigation-without-accounting-advice.md)

## Expected Result

You can move through the Reports area, run the available report tabs with the correct date controls, review totals and detail, and export or print the results when needed. Current general ledger impact as of 2026-05-04:

- Running a report does not create, edit, or delete a journal entry.
- Exporting or printing a report does not create, edit, or delete a journal entry.
- Opening a drilldown view only displays supporting entries that already exist in the ledger.

## Common Mistakes

- Running a report under the wrong active company.
- Treating a report as a posting workflow instead of a read-only review workflow.
- Expecting export, print, or drilldown to fix underlying transaction or account coding.

## Related Articles

- [View available reports](./view-available-reports.md)
- [Use report drilldown behavior](./use-report-drilldown-behavior.md)
- [Review financial results inside the product](./review-financial-results-inside-the-product.md)
- [Interpret report navigation without accounting advice](./interpret-report-navigation-without-accounting-advice.md)
