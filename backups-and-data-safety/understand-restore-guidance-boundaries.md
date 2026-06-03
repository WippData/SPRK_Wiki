# Understand Restore Guidance Boundaries

Use caution when discussing restore workflows, because the validated public `Backups` tab currently shows backup settings and an on-demand backup action, not a restore workflow.

## Purpose

Use this article when you want to know what SPRK publicly exposes today for backup-related recovery guidance.

## Prerequisites

- You are signed in to SPRK.
- You can open `Preferences` and review the `Backups` tab.

## Steps

1. Open `Preferences`.
2. Select the `Backups` tab.
3. Review the controls that are publicly visible: the automatic backup switch, schedule field, backup location field, status area, and `Run Backup Now`.
4. Confirm whether a restore button, restore wizard, or restore instructions are visible in the product.
5. If no public restore workflow is visible, keep user guidance limited to backup creation, backup location review, and support escalation for recovery questions.

## Expected Result

You can describe the current public boundary accurately: SPRK exposes backup configuration and manual backup creation in the validated `Backups` tab, but no restore workflow was visible in the public UI validation completed on 2026-05-07. Current general ledger impact as of 2026-05-07:

- Describing recovery boundaries does not affect the books.
- The absence of a public restore action means no restore-related posting flow was validated from the current UI.
- Backup and restore guidance should never be described as changing ledger balances unless a future public workflow explicitly proves that behavior.

## Common Mistakes

- Publishing restore steps that were not validated in the current public product.
- Assuming a backup file can be restored from the same screen without a visible restore control.
- Blending support guidance with product steps that the user cannot currently perform.

## Related Articles

- [Review backup settings visible in the product](./review-backup-settings-visible-in-the-product.md)
- [Understand backup schedule behavior](./understand-backup-schedule-behavior.md)
- [Understand database alignment and recovery escalation](../support-and-troubleshooting/understand-database-alignment-and-recovery-escalation.md)

## Info

- App sections: `backups`
- Last validated: 2026-06-03
- Screenshot status: `not-started`
