# Install and Manage Plugins (Beta)

![Plugins settings tab showing installed plugin entries](../screenshots/plugins/plugins-settings-tab-step-01.png)

Preview a trusted plugin, install or upgrade it when SPRK accepts the preview, and manage installed Plugins (Beta).

## When To Use This

Use this workflow when your firm receives a plugin, needs to upgrade an installed plugin, or needs to remove a plugin from normal use.

## Before You Start

- Confirm the plugin source is trusted.
- Confirm your workspace has plugin access.
- Keep users out of plugin-owned workflows while you install, upgrade, disable, or uninstall.
- Confirm the active company before testing company-specific plugin pages.

## Steps

1. Open `Settings` -> `Plugins`.
2. Select `Refresh Installed Plugins`.
3. If you are installing or upgrading, choose `Select Plugin Bundle`.
4. Select the trusted plugin file.
5. Select `Preview Plugin`.
6. Review the plugin name, publisher, version, description, warnings, and available action.
7. If the preview is not ready, stop and resolve the issue before installing or upgrading.
8. If the preview is ready and the install or upgrade action is available, continue.
9. Refresh `Installed Plugins`.
10. Confirm the plugin appears with the expected status.
11. If the plugin should add pages, look for the `Plugins` group in the sidebar.
12. To remove a plugin from use, disable it first.
13. If uninstall becomes available after disablement, use it only when you intend to remove the installed plugin record from SPRK.

## What Happens When You Install Or Disable

Installing or enabling a plugin can make plugin pages available in navigation. Disabling a plugin removes its visible pages from navigation. Uninstalling removes the installed plugin from the workspace.

These actions do not post accounting activity by themselves. A plugin may affect accounting later only if a user completes a posting workflow inside that plugin.

## If Something Looks Wrong

- If the plugin does not appear after installation, refresh installed plugins.
- If uninstall is not available, disable the plugin first.
- If expected pages are missing, confirm the plugin is enabled and the intended company is active.
- If users should not use the plugin yet, leave it disabled until setup is complete.

## Related

- [Use the Plugins (Beta) settings tab](./use-the-plugins-settings-tab.md)
- [Control Plugins (Beta) by company](./control-plugin-availability-by-company.md)
- [Troubleshoot missing Plugins (Beta) pages](./troubleshoot-plugin-pages-that-do-not-appear.md)
