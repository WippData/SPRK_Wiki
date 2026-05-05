# Understand Active Company Behavior

Learn what changes when you select a different active company and what stays separate across companies.

## Purpose

Use this article when you want to understand how SPRK decides which company is active and how that choice affects the rest of the app.

## Key Points

- The active company is shown in the selector at the top of the left sidebar.
- The selected company becomes the default context for pages, search results, reports, and future data entry.
- SPRK remembers the last company you selected and tries to reuse it when that company is still available and not archived.
- If the current company is no longer usable, SPRK falls back to another active company instead of leaving the app without context.

## Expected Result

You can predict which company your work applies to before opening any accounting workflow. Current general ledger impact as of 2026-05-04:

- Changing the active company does not move, merge, or repost existing transactions.
- No journal entry is created, edited, or deleted when you switch companies.
- Future transactions you enter after switching are recorded in the newly active company, not the previous one.

## Common Mistakes

- Assuming the active company only affects the current page.
- Forgetting to re-check the sidebar company name before entering transactions.
- Expecting a company switch to copy activity between companies.

## Related Articles

- [Choose or switch your active company](../getting-started/choose-or-switch-your-active-company.md)
- [Use the Companies tab](./use-the-companies-tab.md)
- [Switch between companies](../company-setup-and-migration/switch-between-companies.md)

## Info

- App sections: `companies`, `dashboard`
- Last validated: 2026-05-04
- Screenshot status: `not-started`
