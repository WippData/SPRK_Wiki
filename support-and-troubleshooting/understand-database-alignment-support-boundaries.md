# Understand Database Alignment Support Boundaries

Use this article when balances, source documents, bank rows, reports, or reconciliation history appear inconsistent and you need a support-safe response.

## Purpose

Use this workflow when you suspect data is out of alignment, such as a report total not matching a source document, a linked journal not appearing where expected, or an import/reversal result looking inconsistent.

## Steps

1. Stop making corrective edits until you have captured the visible issue.
2. Confirm the active company, page, date range, account, and document number involved.
3. Re-run or refresh the page if the issue may be a stale view.
4. Compare the source workflow to the review workflow:
   - invoice or bill list versus payment history
   - Banking row versus linked journal
   - Reconcile row versus reconciliation report
   - Ledger row versus report drilldown
   - import preview versus posted results
5. Capture screenshots of the mismatch if they do not expose sensitive client data.
6. Open `Support` and download the `Support Activity Log`.
7. Contact support with the company name, workflow, affected record identifiers, date range, visible error or mismatch, recent import/reversal/edit actions, and support log.

## Expected Result

Support receives enough context to investigate without asking you to mutate data first. Current general ledger impact as of 2026-06-17:

- Refreshing pages, collecting screenshots, and downloading the support log do not post accounting activity.
- Do not use manual journal entries, deletes, import retries, or direct source-document edits as a first response to suspected alignment issues unless support or your accounting policy directs that correction.
- Supported reversal, void, payment, and edit-policy workflows preserve history better than ad hoc cleanup.

## Common Mistakes

- Creating a manual journal to force reports to match before identifying the source mismatch.
- Retrying imports repeatedly without preserving the first duplicate or diagnostic message.
- Deleting a source record when the correct path is reversal, voiding, unmatching, or support review.
- Reporting an issue without the company, date range, account, document number, or support log.

## Related Articles

- [Collect the right details before contacting support](./collect-the-right-details-before-contacting-support.md)
- [Collect import run details for support](./collect-import-run-details-for-support.md)
- [Review document payment history and linked journals](../ledger-and-chart-of-accounts/review-document-payment-history-and-linked-journals.md)
- [Edit linked ledger and bank activity](../ledger-and-chart-of-accounts/edit-linked-ledger-and-bank-activity.md)

## Info

- App sections: `support`, `ledger`, `banking`, `reports`, `reconcile`
- Last validated: 2026-06-17
- Screenshot status: `not required`
