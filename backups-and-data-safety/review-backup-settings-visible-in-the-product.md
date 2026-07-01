# Review Backup Settings Visible In The Product

Open the `Backups` tab to review the current automatic backup controls, backup location, recent status, on-demand backup action, and visible Company File handoff controls.

![SPRK Backups settings showing status, backup location, Run Backup Now, automatic backup controls, and Company file actions](../screenshots/backups-and-data-safety/company-file-controls-step-01.png)

![SPRK Backups tab showing backup status, resolved backup location, and Company file controls](../screenshots/backups-and-data-safety/backup-location-resolved-step-01.png)

![SPRK Backups tab showing automatic backup schedule and backup-on-close controls](../screenshots/backups-and-data-safety/review-backup-settings-step-02.png)

## When To Use This

Use this workflow when you want to confirm which backup settings are publicly available in the current SPRK app.

## Before You Start

- You are signed in to SPRK.
- Confirm the active company shown in the sidebar before using company-file controls.

## Steps

1. Confirm the active company shown in the sidebar.
2. Open `Backups` from the `Settings` section.
3. Confirm the `Backups` tab is selected.
4. Review the automatic backup switch.
5. Review the daily schedule time shown in local time.
6. Review the `Backup location` field.
7. If you need to change the folder path, enter the new path and save the location.
   - A relative path is resolved by the desktop runtime against its configured backup base directory.
   - The saved field may still reflect the value you entered; review the run result to confirm the final resolved path.
8. Review the `Status` area for the last backup time and result.
9. Use `Run Backup Now` when you want to create an on-demand backup from the current device.
   - A successful manual backup reports the resolved backup path so you can see where the file landed.
   - If path resolution succeeds but the backup fails later, the visible error can still refer to the resolved target path.
10. Review the `Company file` card separately from routine backups:
   - `Export Company File` exports the active company only.
   - `Import Company File` starts the company-file import path.
   - The card shows the active company name so you can confirm the company context before continuing.

## What Happens Next

You can review and manage the current backup controls that SPRK exposes publicly: enable or disable automatic backups, set the daily time, save a folder path, review the last result, start a manual backup run, and use company-scoped Company File handoff controls.

- Saving a backup location does not create or modify any accounting entry.
- Relative backup locations are not necessarily the final filesystem path shown after a run; SPRK resolves them before writing the backup file.
- Running a backup creates a data copy for safekeeping; it does not post to income, expense, asset, liability, or equity accounts.
- Exporting a Company File creates a company-level package and does not post accounting activity.
- Importing a Company File is a data-management workflow. Review preview and replace language before confirming any import.
- The status area reports backup activity only and does not represent a financial transaction.

## If Something Looks Wrong

- Treating the backup folder path as a company record instead of a device-level storage setting.
- Assuming a relative backup path is the exact final folder. Check the latest manual backup result for the resolved runtime location.
- Assuming `Run Backup Now` changes books or confirms pending work.
- Confusing routine backups for all local companies with a company-scoped Company File export.
- Reading the status area as accounting activity rather than backup history.

## Business Scenario: Manual Backup Control

Use this scenario to train staff on where manual backup controls live and how to distinguish routine database backups from Company File handoff.

- Sample file: [22-backup-company-file-export.csv](../sample-files/v1-validation/22-backup-company-file-export.csv)
- Evidence:

![Backups page showing backup status, backup path, Run Backup Now, and Company File controls](../screenshots/v1-validation/backups-run-now-location-company-file.png)

![Backups page showing Run Backup Now completed successfully in the user application support backup folder](../screenshots/v1-validation/backup-run-now-success-v0.3.57.png)

Validation note: this walkthrough was validated in SPRK v0.3.57. `Run Backup Now` completed successfully and reported the backup location under the user's application support backup folder.

## Related

- [Understand backup schedule behavior](./understand-backup-schedule-behavior.md)
- [Export and import Company Files](./export-and-import-company-files.md)
- [Understand restore guidance boundaries](./understand-restore-guidance-boundaries.md)
