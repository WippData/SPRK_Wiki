# Troubleshoot Plugin Pages That Do Not Appear

![Plugins settings tab showing installed runtime plugin entries](../screenshots/plugins-and-runtime/plugins-settings-tab-step-01.png)

Check installed status, runtime support, active company context, and preview warnings when a plugin page does not appear in SPRK navigation.

## Purpose

Use this workflow when a plugin is expected to add a page or action, but the page does not appear after install, upgrade, enablement, or company switching.

## Prerequisites

- You are signed in to SPRK.
- You know the plugin name or bundle you expected to use.
- You can open `Settings` and select the `Plugins` tab.
- You can identify the active company in the sidebar.

## Steps

1. Confirm the active company in the sidebar.
2. Open `Settings`.
3. Select the `Plugins` tab.
4. In `Installed Plugins`, select `Refresh Installed Plugins`.
5. If the inventory says `No plugins are installed yet.`, install the plugin before expecting runtime pages.
6. If the plugin is installed but disabled, enable it when that action is available.
7. If you recently selected a bundle, review the preview status before installing or upgrading.
8. Stop and resolve any preview error, including:
   - minimum app version mismatch
   - bundle size or file-count limit failure
   - manifest JSON size failure
   - unsafe bundle paths
   - declared extension `sha256` mismatch
9. Confirm the plugin declares a public runtime extension type. Public runtime pages currently support `new_page` extensions for list and transaction pages.
10. If the plugin declares backend pilot extension types or requires network, file, or secret capabilities, do not expect it to appear as a public runtime page.
11. If the plugin page is company-scoped, switch to the intended company and reopen navigation.
12. If the installed plugin row exposes company availability controls, confirm the plugin is available for the active company.
13. If the plugin was just disabled, expect its public pages to disappear from the sidebar `Plugins` group.
14. Move away from the current page and back again, or refresh installed plugins, if you just changed plugin status.
15. If the page still does not appear, collect the plugin name, plugin version, active company, app version, and any preview warning before contacting support.

## Expected Result

You can usually identify whether the missing page is caused by no installed plugin, a disabled plugin, a failed preview, an unsupported runtime extension, a capability-limited plugin, or the wrong active company. Current general ledger impact as of 2026-06-17:

- Troubleshooting plugin visibility does not post transactions.
- Installing or enabling a plugin does not post transactions by itself.
- Disabling a plugin removes its public runtime pages from navigation.
- Opening a plugin list page does not post transactions.
- A plugin transaction page can post only when the user completes the posting action defined by that extension, such as confirming a transaction.

## Common Causes

- The plugin was previewed but not installed.
- The plugin is installed but disabled.
- The plugin requires a newer app version.
- The extension type is not shown in the public runtime.
- The plugin requires network, file, or secret capabilities and is installable only for testing.
- The plugin page is company-scoped and the wrong company is active.
- The installed plugin row has company availability settings that exclude the active company.
- The plugin was uninstalled after validation; in that case, `Installed Plugins` returns to `No plugins are installed yet.`

## Common Mistakes

- Treating `Preview Plugin` as the same thing as install.
- Assuming every installed plugin adds a visible page.
- Looking for company-scoped plugin pages without checking the active company.
- Ignoring preview warnings because the bundle came from a trusted source.
- Contacting support without the plugin name, version, active company, and app version.

## Related Articles

- [Install and manage plugins](./install-and-manage-plugins.md)
- [Control plugin availability by company](./control-plugin-availability-by-company.md)
- [Use the Plugins settings tab](./use-the-plugins-settings-tab.md)
- [Collect the right details before contacting support](../support-and-troubleshooting/collect-the-right-details-before-contacting-support.md)

## Info

- App sections: `plugins`, `settings`
- Last validated: 2026-06-17
- Screenshot status: `captured`
