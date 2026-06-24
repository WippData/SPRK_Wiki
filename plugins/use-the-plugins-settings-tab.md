# Use the Plugins (Beta) Settings Tab

![Plugins settings tab showing supported plugin types and installed plugin status](../screenshots/plugins/plugins-settings-tab-step-01.png)

Open the `Plugins` tab to see installed Plugins (Beta), refresh their status, and preview a trusted plugin before installing it.

## When To Use This

Use this page when you need to confirm whether Plugins (Beta) are available in your workspace or inspect a plugin before making it available to users.

## Before You Start

- You are signed in to SPRK.
- Your workspace has plugin access and a valid license for the `Plugins` tab.
- You have the plugin file from a trusted source if you plan to preview one.
- You have confirmed the active company before testing any company-specific plugin.

## Steps

1. Open `Settings`.
2. Select the `Plugins` tab.
3. Review `Installed Plugins`.
4. Select `Refresh Installed Plugins` if the list may be stale.
5. Review the `Supported plugin types` alert.
   - Public runtime pages currently support `new_page` extensions for list and transaction pages.
   - Backend pilot extension types and plugins that need network, file, or secret capabilities can be installed for testing, but they are not shown in the app runtime.
6. To inspect a new plugin, select `Select Plugin Bundle`.
7. Choose the plugin file you intend to review.
8. Review the bundle limits shown on the page before previewing:
   - `10 MiB` upload
   - `25 MiB` expanded contents
   - `100` files
   - `5 MiB` per file
   - `1 MiB` per manifest JSON
   - safe in-bundle paths
   - declared extension `sha256` verification
9. Select `Preview Plugin`.
10. Read the preview details, warnings, and install or upgrade status before continuing.
11. Do not install or upgrade if the preview shows a blocking issue.

## What This Changes

Opening or refreshing the `Plugins` tab is review-only. Installing, enabling, disabling, or uninstalling a plugin changes plugin availability and navigation, not existing ledger balances.

Installed plugin cards can show lifecycle states such as `Enabled`, `Disabled`, `Requires re-enable`, `Blocked`, or `Invalid`, and runtime states such as `Runtime available`, `Pilot only`, `Hidden by capability`, or `No runtime page`.

## If Something Looks Wrong

- If the `Plugins` tab is missing, confirm workspace access and license status.
- If `Installed Plugins` is empty, no plugin pages should appear in navigation yet.
- If preview shows a warning, resolve it before installing or upgrading.
- If a plugin page does not appear after install, refresh installed plugins and confirm the plugin is enabled and shows a runtime state that can appear in the app.
- If a plugin-driven report is expected, remember that report visibility also depends on supported report metadata and runtime availability.

## Related

- [Install and manage Plugins (Beta)](./install-and-manage-plugins.md)
- [Troubleshoot missing Plugins (Beta) pages](./troubleshoot-plugin-pages-that-do-not-appear.md)
- [View license information](../licensing/view-license-information.md)
