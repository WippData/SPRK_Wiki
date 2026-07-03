# Troubleshoot Missing Plugins (Beta) Pages

![Plugins settings tab showing supported plugin types and installed plugin status](../screenshots/plugins/plugins-settings-tab-step-01.png)

Use this support path when a Plugin (Beta) should add a page, but the page does not appear in SPRK navigation.

## When To Use This

Use this page after install, upgrade, enablement, or company switching when expected plugin pages are missing.

## Do This First

1. Confirm the active company in the sidebar.
2. Open `Settings` -> `Plugins`.
3. Select `Refresh Installed Plugins`.
4. Confirm the plugin is installed.
5. Confirm the plugin is enabled.
6. Review the plugin card tags:
   - Lifecycle states can include `Enabled`, `Disabled`, `Requires re-enable`, `Blocked`, or `Invalid`.
   - Page visibility states can include available, pilot-only, hidden by capability, or no visible page.
7. If you recently previewed a bundle, confirm the preview was actually installed or upgraded.
8. If the plugin page is company-specific, switch to the intended company and check navigation again.
9. Move away from the current page and back again after changing plugin state.
10. For plugin-provided reports, also check the Reports page after the installed-plugin list has refreshed. Installed status alone does not guarantee a report source.

## Details To Capture

- Plugin name and version.
- Whether the plugin is installed, enabled, disabled, or missing from inventory.
- Active company.
- App version shown in the sidebar footer.
- Any preview warning or install message.
- Any lifecycle, page-visibility, or blocked-action message on the installed plugin card.
- Whether the sidebar shows a `Plugins` group.
- Whether the expected surface is a sidebar page, a list or transaction page, or a report source.

## What This Changes

Troubleshooting visibility does not post transactions. Installing or enabling a plugin makes pages available; users still need to complete a workflow before accounting data changes.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| The plugin was previewed but no page appears | Whether the preview was installed or upgraded | Install or upgrade the plugin before expecting pages. |
| The plugin is disabled | Installed plugin state | Enable the plugin before checking navigation. |
| The plugin shows `Pilot only`, `Hidden by capability`, or no visible page | Page-visibility state on the plugin card | Treat the plugin as installed without a visible public page until the state changes. |
| The plugin shows `Blocked`, `Invalid`, or `Requires re-enable` | Lifecycle state and card message | Resolve that state before expecting navigation or report visibility. |
| The page appears in one company but not another | Active company and company availability controls | Switch to the intended company and review plugin availability. |
| Preview warnings remain | Visible preview warning | Resolve the warning before installing or upgrading. |
| The page still does not appear | Installed state, enabled state, active company, and page-visibility message | Contact support with the details above. |

## Related

- [Install and manage Plugins (Beta)](./install-and-manage-plugins.md)
- [Control Plugins (Beta) by company](./control-plugin-availability-by-company.md)
- [Use the Plugins (Beta) settings tab](./use-the-plugins-settings-tab.md)
- [Collect the right details before contacting support](../support-and-troubleshooting/collect-the-right-details-before-contacting-support.md)
