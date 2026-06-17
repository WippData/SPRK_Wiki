# Control Plugin Availability by Company

![Plugins settings tab showing installed runtime plugin entries](../screenshots/plugins-and-runtime/plugins-settings-tab-step-01.png)

Review company-scoped plugin behavior so installed plugins appear only where they are intended to be used.

## Purpose

Use this article when a plugin is installed at the tenant level but its pages or actions should be checked against the active company. Company-scoped extensions follow company context, so switching companies can change which plugin data or plugin pages are relevant.

## Prerequisites

- You are signed in to SPRK.
- The plugin is already installed.
- You know which company should use the plugin.
- You understand whether the plugin declares company-scoped extensions.

## Steps

1. Check the company selector in the sidebar and confirm the active company.
2. Open `Settings`.
3. Select the `Plugins` tab.
4. Review `Installed Plugins`.
5. Select `Refresh Installed Plugins` if the status may have changed.
6. Find the plugin row and confirm the plugin is enabled before expecting its public pages to appear.
7. If the installed plugin row exposes company availability controls, set the plugin availability for the intended company.
8. If no company availability controls are shown, treat the plugin as tenant-installed and verify company behavior through the active company context.
9. For an enabled public `new_page` plugin, look for its pages under the sidebar `Plugins` group.
10. Switch to another company and reopen navigation if you need to confirm whether the plugin page appears there.
11. Return to the intended company before entering plugin-owned records or transactions.

## Expected Result

You understand whether plugin behavior is tenant-wide, company-scoped, or controlled by company availability settings exposed on the installed plugin row. Current general ledger impact as of 2026-06-17:

- Refreshing plugin inventory does not post accounting activity.
- Enabling, disabling, or changing availability for a plugin does not create journal entries by itself.
- Disabling an enabled public plugin removes its pages from the sidebar `Plugins` group.
- Opening a company-scoped list page does not post transactions.
- Using a plugin transaction page can post accounting activity if the extension defines a confirm-time posting action.

## Current Runtime Notes

The current public runtime supports `new_page` extensions for list and transaction pages. A plugin manifest can declare extensions with `companyScoped: true` for the `company` target, which means the extension is evaluated inside the active company context.

In the validated sample, SPRK showed tenant-level installed-plugin controls and active-company runtime behavior; no separate per-company availability control was exposed on the installed plugin row.

Backend pilot extension types and plugins that require network, file, or secret capabilities can be installed for testing, but they do not appear as public runtime pages.

## Common Mistakes

- Looking for a plugin page while the wrong company is active.
- Assuming tenant installation means the plugin is enabled or visible for every company.
- Assuming company-scoped plugin data belongs to the same dataset across all companies.
- Forgetting to refresh installed plugins after install, upgrade, disable, or removal.
- Troubleshooting navigation before confirming the plugin is actually installed and enabled.

## Related Articles

- [Install and manage plugins](./install-and-manage-plugins.md)
- [Troubleshoot plugin pages that do not appear](./troubleshoot-plugin-pages-that-do-not-appear.md)
- [Understand company-aware navigation](../dashboard-and-navigation/understand-company-aware-navigation.md)
- [Switch between companies](../company-setup-and-migration/switch-between-companies.md)

## Info

- App sections: `plugins`, `settings`, `companies`
- Last validated: 2026-06-17
- Screenshot status: `captured`
