# Review Financial Results Inside the Product

Run financial reports in SPRK, compare periods where supported, and review balances and activity inside the app without treating the report itself as accounting advice.

## Purpose

Use this workflow when you want to review company results in SPRK by period, as of a date, or by supporting report category.

## Prerequisites

- You are signed in to SPRK with the correct active company selected.
- The transactions and journal entries you expect to review are already posted.
- You know the time period or date you want to evaluate.

## Steps

1. Open `Reports`.
2. Choose the report that matches your review goal:
   - `Income Statement` for period-based income and expense review.
   - `Balance Sheet` for balances as of a date.
   - `Trial Balance` for account balances as of a date.
   - `Cash Flow (Indirect)` for period-based cash-movement review.
   - `Reconciliation` for posted bank or credit card reconciliation report output.
   - `General Ledger` for filtered transaction detail by type, subtype, account, vendor, or text.
   - `Account Detail` for transaction detail on one selected account.
3. Set the period or date controls for the selected report. You can use the calendar controls or type dates directly when the field is editable; typed dates should follow your saved `Preferences` date order.
4. If you are on `Income Statement`, add a compare period when you want side-by-side period review.
5. If you are on `Income Statement`, use `Group By` when you want the report split by month, quarter, or year.
6. Select `Run`.
7. Review the summary totals and report rows shown on the page.
   - In `General Ledger`, use `Group By` when you want account-type, subtype, or nested type-and-subtype sections before expanding account detail.
8. If something looks unusual, use drilldown where available to inspect the supporting entries instead of guessing from the summary alone.

## Expected Result

You can review current report totals and detailed lines directly in SPRK for the selected company and period. Current general ledger impact as of 2026-06-05:

- Report totals reflect posted activity already stored in SPRK.
- Running or rerunning the report does not create, reverse, or reclassify any journal entry.
- Compare-period and grouping views reorganize the display only; they do not change source transactions.
- Running a reconciliation report reads a posted reconciliation period for the selected account; it does not reopen or change that reconciliation.

## Common Mistakes

- Using the wrong report for the question you are trying to answer.
- Comparing periods without checking that the date ranges match your intent.
- Typing date shortcuts without confirming they match your selected date-format order.
- Treating report output as a substitute for reviewing the underlying entries when a balance looks unexpected.
- Assuming a report review changes the ledger automatically. Any correction still has to happen through the relevant transaction or journal-entry workflow.

## Related Articles

- [View available reports](./view-available-reports.md)
- [Export transactions from reports](./export-transactions-from-reports.md)
- [Use report drilldown behavior](./use-report-drilldown-behavior.md)
- [View and print bank reconciliation reports](../reconciliation/view-and-print-bank-reconciliation-reports.md)
- [Interpret report navigation without accounting advice](./interpret-report-navigation-without-accounting-advice.md)
- [Use the Preferences tab](../preferences-and-personalization/use-the-preferences-tab.md)

## Info

- App sections: `reports`
- Last validated: 2026-06-05
- Screenshot status: `blocked`
