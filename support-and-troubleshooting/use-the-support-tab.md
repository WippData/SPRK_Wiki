# Use the Support tab

Open the Support tab to download a troubleshooting log, clear the current session log, review contact options, check for updates when your app supports them, review release notes before restarting, and open support resources.

## Purpose

Use this workflow when you need the main support tools inside SPRK, including the activity log, current contact details, update actions, release-note access when updater controls are available, the bug-reporting link, and built-in help topics.

## Prerequisites

- You can open the `Support` settings tab in SPRK.
- You are working in the company session where the issue occurred.
- If you want to share a session log, reproduce the issue first so the current session contains the relevant actions.

## Steps

1. Open `Support`.
2. In `Support Activity Log`, review whether the current session has captured actions.
3. Select `Download Log` if you need a text file to share with support.
4. Select `Clear Log` only if you want to remove the current session history and start fresh.
5. Review the `Contact` card for the available support channels. The current Support tab lists email and Discord.
6. If your installed app exposes update controls, review the visible update actions first:
   - Use `Release Notes` when it is shown and you want to read what changed before restarting or comparing builds.
   - The release-notes modal can reflect the installed version, a downloaded update version, or the latest public release, depending on which updater state is visible in your build.
7. If your installed app exposes update controls, use `Download Latest Version` to check for and download an available update.
8. If an update finishes downloading and the app shows it is ready, use `Install & Restart` to apply it.
9. If release notes do not load, use the visible fallback link to the public releases page instead of treating the Support workflow as blocked.
10. Use `View or Submit Bugs` if you need the known-issues and bug-submission page.
11. Expand `How To Guides` if you want quick in-product help topics before contacting support.

## Expected Result

You can reach the product's visible support actions from one tab and leave with the log file, contact method, update action, release-note reference, bug-reporting path, or help topic you need. Current general ledger impact as of 2026-05-25:

- Opening the Support tab does not create or change any journal entry.
- Downloading or clearing the support log does not affect the general ledger.
- Contact links, release-note views, update actions, bug-reporting links, and help topics do not post transactions or change account balances.

## Common Mistakes

- Clearing the support log before downloading the session details you wanted to keep.
- Expecting the support log to include activity from earlier sessions instead of the current app session.
- Assuming update controls will always appear. They are only visible when the installed app supports in-app updates.
- Assuming release notes must load inside SPRK before you can continue. The current flow can fall back to the public releases page.
- Looking for channels or guided-session actions that are not currently visible. Use the options shown in the current Support tab.

## Related Articles

- [Collect the right details before contacting support](./collect-the-right-details-before-contacting-support.md)
- [Troubleshoot common navigation or workflow confusion](./troubleshoot-common-navigation-or-workflow-confusion.md)
- [Understand company-aware navigation](../dashboard-and-navigation/understand-company-aware-navigation.md)
- [User-facing release change summaries](../faq-glossary-and-release-changes/user-facing-release-change-summaries.md)

## Info

- App sections: `support`
- Last validated: 2026-05-25
- Screenshot status: `blocked`
