# Export and Import Company Files

![Backups tab showing Company file export and import controls for Demo Company](../screenshots/backups-and-data-safety/company-file-controls-step-01.png)

Use `Company file` actions when you need to move or preserve one company without including every other company in the local SPRK database.

## When To Use This

Use this workflow when a firm needs a company-level transfer, support needs a complete company package for review, or you want a company-specific transfer path that is separate from routine device backups.

## Before You Start

- You are signed in to SPRK.
- The active company in the sidebar is the company you intend to export or import around.
- You understand whether you are only exporting a file or preparing to replace/import company data.

## Steps

1. Confirm the active company in the sidebar.
2. Open `Backups` from the `Settings` section.
3. Review routine backup controls separately from the `Company file` card.
4. In `Company file`, confirm the active company name shown by SPRK.
5. Use `Export Company File` when you need a non-destructive company-level file for transfer or safekeeping.
6. Use `Import Company File` only when you are ready to review a company-file import path.
7. If SPRK shows an import preview, read the company identity, validation messages, and any replace warning before continuing.
8. Do not confirm a replace/import step unless you are working in the intended company and have a current backup or exported company file.

## What Happens Next

You can distinguish a company-level transfer from device backup settings.

- Exporting a company file creates an outbound company package. It does not post, reverse, or edit journal entries.
- Importing or replacing from a company file can change which company data is available after the workflow completes, so treat confirmation steps as data-management actions rather than accounting entries.
- Routine backups still protect the local database for all companies; a company file is narrower and intentionally company-scoped.


## Practice And Examples

Use these files to practice the company-scoped export/import path in a disposable or training company. Review the import preview and replacement warning before choosing `Replace company`.

- Practice files:
  - [company-file-export-practice.csv](../sample-files/practice/company-file-export-practice.csv)
  - [company-file-import-preview-replace.csv](../sample-files/practice/company-file-import-preview-replace.csv)
  - [company-file-import-preview-replace.sprkcompany.zip](../sample-files/practice/company-file-import-preview-replace.sprkcompany.zip)

![Backups page showing Company File export and import controls](../screenshots/v1-validation/backups-company-file-and-close-policy.png)

![Company File import preview showing table count, export timestamp, and replace warning](../screenshots/v1-validation/company-file-import-preview-replace-warning.png)

The preview shows the table count, export timestamp, and replacement warning so you can stop before replacing company data.

## Related

- [Review backup settings visible in the product](./review-backup-settings-visible-in-the-product.md)
- [Understand restore guidance boundaries](./understand-restore-guidance-boundaries.md)
- [Understand import and migration boundaries](../company-setup-and-migration/understand-import-and-migration-boundaries.md)
- [Collect the right details before contacting support](../support-and-troubleshooting/collect-the-right-details-before-contacting-support.md)
