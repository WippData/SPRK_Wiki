# Use the Preferences Tab

Open `Preferences` to manage app-wide appearance, formatting, update notification, navigation, automation, and getting-started settings.

![Column preferences dialog showing drag handles, visibility checkboxes, and move controls for invoice columns](../screenshots/preferences-and-personalization/column-preferences-drag-handles-step-01.png)

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
4. Review the `Formatting` card:
   - Choose a `Number format`.
   - Choose a `Currency format`.
   - Choose a `Date format`.
   - Choose a `Decimal data entry` style.
5. Review column and list preferences when you need faster table cleanup:
   - Use `Grid Edit default` to choose whether supported list pages start in Grid Edit mode.
   - Open `Column preferences` from supported tables to choose visible optional columns and change their order.
   - Drag a column's reorder handle when you want to move it quickly, or use the move-up and move-down controls when keyboard or button controls are easier.
   - Leave required columns visible when SPRK keeps them protected.
6. Review the `Updates` card and choose the automatic update frequency you want.
7. Review the `Automation` card if you want to adjust supported default-account helpers.
8. Review the `Navigation` card if you want to tailor the sidebar layout later.
9. Review the `Getting started` card if you want the dashboard tour to appear again.
10. Save preferences when you finish if the page does not auto-save the changes you made.

## Expected Result

Your user-level preferences are applied across the SPRK app, including display, formatting, grid-edit startup behavior, and update prompt behavior. Current general ledger impact as of 2026-06-02:

- Changing preferences does not create, edit, or delete a journal entry.
- Display and formatting updates change how information is shown to you, not the underlying transaction amounts.
- Turning on `Grid Edit default` changes how supported pages open for your user profile, not which records exist or how they post.
- Changing column visibility or column order affects your working view on supported tables, not the accounting records behind those rows.
- Resetting the getting-started tour affects onboarding prompts only and does not change company books.

## Common Mistakes

- Treating Preferences as a company setup page instead of a user-level settings area.
- Assuming number or currency display choices recalculate posted balances.
- Assuming `Grid Edit default` changes every page in SPRK instead of supported list pages only.
- Assuming drag reordering in `Column preferences` replaces the move-up and move-down controls; both paths can be available on supported tables.
- Leaving the page before saving after making changes that are not auto-saved.

## Related Articles

- [Customize the sidebar](./customize-the-sidebar.md)
- [Understand personalization boundaries and saved behavior](./understand-personalization-boundaries-and-saved-behavior.md)
- [Use grid edit for bulk record maintenance](../dashboard-and-navigation/use-grid-edit-for-bulk-record-maintenance.md)
- [Choose or switch your active company](../getting-started/choose-or-switch-your-active-company.md)
- [Understand the sidebar and main navigation](../getting-started/understand-the-sidebar-and-main-navigation.md)

## Info

- App sections: `preferences`
- Last validated: 2026-06-04
- Screenshot status: `captured`
