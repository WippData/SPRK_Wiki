# Understand Backup Schedule Behavior

Review how SPRK schedules automatic backups so you know when the app plans to save backup files for this device.

![SPRK Backups settings showing automatic backup scheduling controls and backup-on-close options](../screenshots/backups-and-data-safety/backup-schedule-behavior-step-01.png)

## Purpose

Use this article when you want to confirm whether automatic backups are enabled and what local time the next daily backup cycle is expected to follow.

## Prerequisites

- You are signed in to SPRK.
- The active company in the sidebar is `Demo Company` for this validated workflow pass.
- You can open `Preferences` from the `Settings` section in the sidebar.

## Steps

1. Confirm the active company shown in the sidebar is `Demo Company`.
2. Open `Preferences`.
3. Select the `Backups` tab.
4. Review the `Enable automatic backups` switch to see whether the schedule is active.
5. Review the `Schedule` field.
6. Treat the displayed time as your local device time.
7. If needed, choose a different time in the time field to change when the daily backup cycle runs.

## Expected Result

You can see whether automatic backups are enabled and what local time SPRK uses for the 24-hour backup cycle. Current general ledger impact as of 2026-05-07:

- Changing the backup schedule does not post, reverse, or edit a journal entry.
- Backup timing changes affect when backup files are created for this device, not company balances.
- Automatic backups protect data copies; they do not reclassify transactions or change account activity.

## Common Mistakes

- Assuming the schedule uses a shared server time instead of the local time shown in the product.
- Treating backup timing as a posting or close-period control.
- Forgetting to confirm the correct active company before validating settings context.

## Related Articles

- [Review backup settings visible in the product](./review-backup-settings-visible-in-the-product.md)
- [Understand restore guidance boundaries](./understand-restore-guidance-boundaries.md)

## Info

- App sections: `backups`
- Last validated: 2026-06-05
- Screenshot status: `captured`
