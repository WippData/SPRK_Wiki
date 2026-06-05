# Use the Plugins Settings Tab

Open the `Plugins` settings tab to review installed plugins, refresh plugin inventory, and preview a plugin bundle before installing or upgrading it.

## Purpose

Use this workflow when you need to understand whether plugin settings are available in your workspace, see which plugins are already installed, or validate a `.zip` plugin bundle before it changes the app runtime.

## Prerequisites

- You are signed in to SPRK.
- Your tenant is licensed for plugin access.
- You have confirmed the active company before reviewing settings. Plugin access is tenant-scoped, but the visible app session still runs inside the active company context.
- If you plan to preview a bundle, you already have the plugin `.zip` file from a trusted source.

## Steps

1. Open `Settings`.
2. Select the `Plugins` tab.
3. Review `Installed Plugins`.
4. Select `Refresh Installed Plugins` if you need to reload the current inventory.
5. In `Plugin bundle (.zip)`, choose `Select Plugin Bundle` when you want to validate a plugin archive.
6. Confirm the selected file is the plugin `.zip` you intended to review.
7. Select `Preview Plugin` after a bundle is selected.
8. Review manifest details, extensions, warnings, and validation issues before you install or upgrade anything.
9. Use enable, disable, uninstall, install, or upgrade actions only after the preview and installed-plugin status match what you expected.

## Expected Result

You can review the tenant's installed plugin inventory and inspect a plugin bundle before installing or upgrading it. Current general ledger impact as of 2026-06-05:

- Opening the `Plugins` tab does not create or edit journal entries.
- Refreshing installed plugins reports plugin state only and does not post transactions.
- Previewing a plugin bundle validates plugin metadata before install or upgrade; preview alone does not add a runtime page or change account balances.
- Installing a plugin can make new app surfaces available, but it does not necessarily make every declared extension visible in the public SPRK runtime.

## Runtime and Bundle Guardrails

SPRK separates plugin installation from public runtime visibility:

- Public runtime pages currently support `new_page` extensions for list and transaction-page experiences.
- Pilot-only extension types and plugins that require network, file, or secret capabilities may be installable for backend testing without appearing as public runtime pages.
- An installed plugin can therefore be present in inventory while still being invisible in normal app navigation.

Bundle preview validates package constraints before install or upgrade. Treat these limits as preparation checks when building or receiving a plugin bundle:

- Maximum uploaded bundle size: `10 MiB`.
- Maximum expanded bundle size: `25 MiB`.
- Maximum file count: `100` files.
- Maximum individual file size: `5 MiB`.
- Maximum manifest JSON size: `1 MiB`.
- Bundle paths must stay inside the plugin archive and avoid unsafe path traversal.
- Declared extension files must match their `sha256` values.

## Common Mistakes

- Assuming the `Plugins` tab is a company-level accounting setting. It is tenant access and runtime configuration, not a company ledger workflow.
- Assuming `installed` always means visible in app navigation. Some plugin types are backend-only or pilot-only in the public runtime.
- Installing or upgrading a bundle before reading preview warnings.
- Treating plugin preview as a replacement for source and publisher trust checks.
- Looking for installed-plugin actions when no plugins are installed yet. In an empty tenant, the page shows an empty inventory and the bundle preview area.

## Related Articles

- [Plugins and Runtime](./README.md)
- [View license information](../licensing/view-license-information.md)
- [Use the Support tab](../support-and-troubleshooting/use-the-support-tab.md)
- [Understand personalization boundaries and saved behavior](../preferences-and-personalization/understand-personalization-boundaries-and-saved-behavior.md)

## Info

- App sections: `plugins`, `settings`
- Last validated: 2026-06-05
- Screenshot status: `blocked`
