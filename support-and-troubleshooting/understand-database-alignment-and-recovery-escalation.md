# Understand Database Alignment and Recovery Escalation

Use this guidance when SPRK appears internally inconsistent and you need to preserve evidence, stop risky follow-up work, and escalate safely.

## Purpose

Use this article when balances, linked records, reconciliation state, import history, or report outputs appear out of alignment and you need a calm next-step plan.

## When To Use This Guidance

Use this escalation path if you notice issues such as:

- a report total that no longer matches the underlying transaction history you expect
- a bank transaction, journal entry, reconciliation session, or import run that appears linked incorrectly or only partly updated
- a reversal, restore question, or import result that seems to have left related records out of sync
- a page state that suggests the same accounting event both did and did not happen

## Steps

1. Stop making additional accounting changes in the affected company until you understand whether the issue is only visual or reflects saved data.
2. Write down the company, page, workflow, approximate time, and the first visible sign that something looked wrong.
3. Capture evidence before cleanup:
   - note the visible balance, status, or record link that seems inconsistent
   - note which report, register, import, reconciliation, or ledger view showed the issue
   - keep any downloaded files, import files, or backup-related details that were part of the workflow
4. Open `Support` and use `Download Log` so the current session activity is preserved for review.
5. Do not clear the support log, rerun the same risky workflow repeatedly, or manually edit database files outside SPRK.
6. If the issue appeared after an import, reconciliation, restore question, reversal, or other ledger-sensitive workflow, say that explicitly in your support request.
7. If recent backup information is available, preserve the backup location details and timing so support can understand your recovery options.
8. Contact support with the evidence package and describe the issue as a suspected alignment problem, not a confirmed corruption diagnosis unless support verifies that conclusion.

## Expected Result

You stop new work soon enough to preserve the audit trail, collect the details support needs, and avoid making the suspected inconsistency harder to investigate. Current general ledger impact as of 2026-06-03:

- Following this escalation path does not create, edit, or delete a journal entry by itself.
- Downloading logs, preserving backup details, and documenting symptoms do not repair or repost accounting data on their own.
- Recovery direction should come from current support guidance, not from ad hoc database edits or unsupported restore assumptions.

## Common Mistakes

- Continuing to post, reconcile, import, or reverse more activity before you preserve the first symptoms.
- Clearing the support log before you save the session details tied to the issue.
- Treating a visible mismatch as proof of database corruption before support reviews the evidence.
- Trying to fix the issue by editing SQLite files, replacing files manually, or reusing old backups without support direction.
- Assuming a public restore wizard exists if you cannot see one in the current product.

## Related Articles

- [Use the Support tab](./use-the-support-tab.md)
- [Collect the right details before contacting support](./collect-the-right-details-before-contacting-support.md)
- [Understand restore guidance boundaries](../backups-and-data-safety/understand-restore-guidance-boundaries.md)
- [Understand audit-sensitive ledger behavior](../ledger-and-chart-of-accounts/understand-audit-sensitive-ledger-behavior.md)

## Info

- App sections: `support`, `backups`, `ledger`, `reconcile`, `banking`
- Last validated: 2026-06-03
- Screenshot status: `not-started`
