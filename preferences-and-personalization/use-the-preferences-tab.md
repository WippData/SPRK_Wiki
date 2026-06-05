# Use the Preferences Tab

Open `Preferences` to manage app-wide appearance, formatting, update notification, navigation, automation, and getting-started settings.

## Purpose

Use this workflow when you want to review or change how SPRK looks and behaves for your user profile across the app.

## Prerequisites

- You are signed in to SPRK.
- The active company shown in the sidebar is the company you intend to use while validating context-sensitive pages.

## Steps

1. Confirm the sidebar company selector shows the company you expect before you continue.
2. Open `Preferences` from the `System` section in the sidebar.
3. Review the `Appearance` card:
   - Use the theme toggle to switch between light and dark mode.
   - Adjust `UI scale` if you need larger or smaller interface sizing.
   - Turn on `Grid Edit default` if you want supported list pages to open in Grid Edit mode automatically.
   - Choose `Account dropdown sorting` when you want supported account selectors to be easier to scan. The visible choices are grouped by type then name, grouped by type then code, or flat A-Z.
4. Review the `Formatting` card:
   - Choose a `Number format`.
   - Choose a `Currency format`.
   - Choose a `Date format`.
   - Choose a `Decimal data entry` style.
5. Review the `Updates` card and choose the automatic update frequency you want.
6. Review the `Automation` card if you want to adjust supported default-account helpers.
7. Review the `Navigation` card if you want to tailor the sidebar layout later.
8. Review the `Getting started` card if you want the dashboard tour to appear again.
9. Save preferences when you finish if the page does not auto-save the changes you made.

## Expected Result

Your user-level preferences are applied across the SPRK app, including display, formatting, grid-edit startup behavior, and update prompt behavior. Current general ledger impact as of 2026-06-05:

- Changing preferences does not create, edit, or delete a journal entry.
- Display and formatting updates change how information is shown to you, not the underlying transaction amounts.
- Turning on `Grid Edit default` changes how supported pages open for your user profile, not which records exist or how they post.
- Changing `Account dropdown sorting` changes the order used by supported account page-link dropdowns across the app, not the chart of accounts itself.
- Resetting the getting-started tour affects onboarding prompts only and does not change company books.

## Common Mistakes

- Treating Preferences as a company setup page instead of a user-level settings area.
- Assuming number or currency display choices recalculate posted balances.
- Assuming `Grid Edit default` changes every page in SPRK instead of supported list pages only.
- Assuming account selectors always appear in one fixed order for every user.
- Leaving the page before saving after making changes that are not auto-saved.

## Related Articles

- [Customize the sidebar](./customize-the-sidebar.md)
- [Understand personalization boundaries and saved behavior](./understand-personalization-boundaries-and-saved-behavior.md)
- [Use grid edit for bulk record maintenance](../dashboard-and-navigation/use-grid-edit-for-bulk-record-maintenance.md)
- [Choose or switch your active company](../getting-started/choose-or-switch-your-active-company.md)
- [Understand the sidebar and main navigation](../getting-started/understand-the-sidebar-and-main-navigation.md)

## Info

- App sections: `preferences`
- Last validated: 2026-06-05
- Screenshot status: `blocked`
