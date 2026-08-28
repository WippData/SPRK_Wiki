# Review Backup Settings Visible In The Product

Open the `Backups` tab to review the current automatic backup controls, backup location, recent status, on-demand backup action, and visible Company File transfer controls.

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
   - A relative path is resolved by SPRK against its configured backup base directory.
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

You can review and manage the current backup controls that SPRK exposes publicly: enable or disable automatic backups, set the daily time, save a folder path, review the last result, start a manual backup run, and use company-scoped Company File transfer controls.

- Saving a backup location does not create or modify any accounting entry.
- Relative backup locations are not necessarily the final filesystem path shown after a run; SPRK resolves them before writing the backup file.
- Running a backup creates a data copy for safekeeping; it does not post to income, expense, asset, liability, or equity accounts.
- Exporting a Company File creates a company-level package and does not post accounting activity.
- Importing a Company File is a data-management workflow. Review preview and replace language before confirming any import.
- The status area reports backup activity only and does not represent a financial transaction.


## Practice And Examples

Use the example file and screenshots to compare routine backup controls with Company File controls. `Run Backup Now` reports backup status and location; it does not post accounting activity.

- Practice file: [company-file-export-practice.csv](../sample-files/practice/company-file-export-practice.csv)

![Backups page showing backup status, backup path, Run Backup Now, and Company File controls](../screenshots/v1-validation/backups-run-now-location-company-file.png)

![Backups page showing Run Backup Now completed successfully in the user application support backup folder](../screenshots/v1-validation/backup-run-now-success-v0.3.57.png)

## Related

- [Understand backup schedule behavior](./understand-backup-schedule-behavior.md)
- [Export and import Company Files](./export-and-import-company-files.md)
- [Understand restore guidance boundaries](./understand-restore-guidance-boundaries.md)
