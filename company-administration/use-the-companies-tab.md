# Use the Companies Tab

Open the Companies tab to review active and archived companies, refresh the list, and reach creation or maintenance actions.

![SPRK Companies tab showing active company filters, the company table, and row-level maintenance actions](../screenshots/company-administration/companies-tab-step-01.png)

## Purpose

Use this workflow when you need a central place to review companies and reach the actions for selecting, editing, archiving, deleting, or adding a company.

## Prerequisites

- You are signed in to SPRK.
- At least one company exists in the workspace.

## Steps

1. Open `Companies` from the `System` section in the sidebar.
2. Review the company table on the `Companies` tab.
3. Use the filter control to switch between `Active`, `Archived`, and `All`.
4. Select `Refresh` if you need to reload the list.
5. Use `New Company` for a blank company, or open the menu next to it for import and demo options.
6. Use the row actions to select the active company, edit a company, archive or unarchive it, or permanently delete an archived company.

## Expected Result

You can see the publicly supported company management actions in one place, including the active company marker and company-level action buttons. Current general ledger impact as of 2026-05-04:

- Viewing or refreshing the company list does not create, edit, or delete a journal entry.
- Switching which company is selected changes app context only.
- Opening company creation or maintenance actions does not post to the general ledger until you later create accounting transactions inside that company.

## Common Mistakes

- Looking for company maintenance under `Preferences` or another settings tab.
- Assuming archived companies disappear from filters permanently.
- Using the `New Company` menu when you only meant to switch the active company.

## Related Articles

- [Understand active company behavior](./understand-active-company-behavior.md)
- [Add a company from the sidebar flow](./add-a-company-from-the-sidebar-flow.md)
- [Review company-level maintenance actions](./review-company-level-maintenance-actions.md)
- [Switch between companies](../company-setup-and-migration/switch-between-companies.md)

## Info

- App sections: `companies`
- Last validated: 2026-05-04
- Screenshot status: `captured`
