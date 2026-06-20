# Understand Restore Guidance Boundaries

![Backups settings showing backup path and schedule controls](../screenshots/backups-and-data-safety/backup-settings-audit-step-01.png)

Use caution when discussing recovery workflows. The public `Backups` tab now shows routine backup settings, on-demand backup creation, and Company File export/import controls, but those are still distinct workflows with different risk levels.

## When To Use This

Use this article when you want to know what SPRK publicly exposes today for backup-related recovery guidance.

## Before You Start

- You are signed in to SPRK.
- You can open `Preferences` and review the `Backups` tab.

## Steps

1. Open `Preferences`.
2. Select the `Backups` tab.
3. Review the controls that are publicly visible: the automatic backup switch, schedule field, backup location field, status area, `Run Backup Now`, `Export Company File`, and `Import Company File`.
4. Keep routine backup guidance separate from Company File handoff guidance.
5. Confirm whether a database restore button, restore wizard, or restore-from-backup instructions are visible in the product.
6. If no public database restore workflow is visible, keep restore-from-backup guidance limited to backup creation, backup location review, Company File import where visible, and support escalation for recovery questions.

## What Happens Next

You can distinguish the visible backup and company-file tools from broader recovery work that may require support.

- Describing recovery boundaries does not affect the books.
- Company File import is recovery-adjacent because it can bring in company data, but it should not be described as a general restore-from-backup wizard.
- Backup and restore guidance should never be described as changing ledger balances unless a future public workflow explicitly proves that behavior.

## If Something Looks Wrong

- Following restore steps that are not visible in your installed SPRK app.
- Assuming a backup file can be restored from the same screen without a visible restore control.
- Assuming Company File import and full database restore are the same operation.
- Blending support guidance with product steps that the user cannot currently perform.

## Related

- [Review backup settings visible in the product](./review-backup-settings-visible-in-the-product.md)
- [Understand backup schedule behavior](./understand-backup-schedule-behavior.md)
- [Export and import Company Files](./export-and-import-company-files.md)
