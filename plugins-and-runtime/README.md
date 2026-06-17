# Plugins and Runtime

![Plugins settings tab showing runtime configuration](../screenshots/plugins-and-runtime/plugins-settings-tab-step-01.png)

Review plugin settings, understand which installed plugins can appear inside SPRK, and use bundle preview before installing or upgrading a plugin package.

## In This Section

- [Use the Plugins settings tab](./use-the-plugins-settings-tab.md)
- [Install and manage plugins](./install-and-manage-plugins.md)
- [Control plugin availability by company](./control-plugin-availability-by-company.md)
- [Troubleshoot plugin pages that do not appear](./troubleshoot-plugin-pages-that-do-not-appear.md)

## Current Runtime Boundaries

The `Plugins` tab separates plugin inventory from public runtime visibility. An installed plugin can be present in `Installed Plugins` while some of its declared capabilities remain unavailable in normal navigation.

Public runtime pages currently support `new_page` extensions for list and transaction pages. Backend pilot extension types and plugins that require network, file, or secret capabilities can be installed for testing, but they are not shown in the app runtime.

Plugin bundles are uploaded as `.zip` files and previewed before install or upgrade. The preview area validates bundle limits, paths, manifest JSON size, and declared extension hashes before any runtime change is applied.

When a compatible `new_page` plugin is installed and enabled, SPRK adds a `Plugins` group to the sidebar for its public pages. Disabling the plugin removes those runtime pages from navigation. Uninstall is available only after the plugin is disabled, and the uninstall confirmation removes installed plugin metadata and company-state records.

## Related Foundation Workflows

- [View license information](../licensing/view-license-information.md)
- [Use the Support tab](../support-and-troubleshooting/use-the-support-tab.md)
- [Understand personalization boundaries and saved behavior](../preferences-and-personalization/understand-personalization-boundaries-and-saved-behavior.md)
- [Understand company-aware navigation](../dashboard-and-navigation/understand-company-aware-navigation.md)

## Info

- App sections: `plugins`, `settings`
- Last validated: 2026-06-17
- Screenshot status: `captured`
