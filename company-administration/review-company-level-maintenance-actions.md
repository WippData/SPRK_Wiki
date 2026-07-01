# Review Company-Level Maintenance Actions

Edit company details, archive or unarchive companies, and understand when permanent delete is available.

![Companies tab filtered to Archived companies with edit, archive, and delete maintenance actions visible](../screenshots/company-administration/company-maintenance-actions-step-01.png)

## When To Use This

Use this workflow when you need to maintain company settings after a company already exists.

## Before You Start

- You can open `Companies` from the `System` section.
- The company you want to maintain is visible in the list.

## Steps

1. Open `Companies`.
2. Find the company you want to maintain.
3. Use `Edit` to update company-level details such as display name, legal name, phone, email, address, currency, country, posting cutoff date, fiscal year end, required account fields, dimensions, accounting edit permissions, default A/R and A/P accounts, invoice settings, or item presentation settings.
   - Workspace or tenant accounting edit-policy defaults can prefill new company setup when those defaults exist, but explicit values saved on the company control that company.
   - If `Required account fields` is set to `Name`, supported account lists and pickers can hide account codes and sort by account name.
   - If `Control accounts` is exposed, selected accounts should be posted through their source workflow; SPRK can hide or block those accounts in new manual journal-entry account choices.
4. Review invoice-facing company settings when your team prints customer invoices:
   - `Sales / Invoicing` stores `Default invoice payment terms` and `New invoice workflow`.
   - Company phone, email, address, city, state, postal code, country, and `Payment Instructions` can feed the customer-standard printed invoice layout.
5. Review `Item identification` when users report that item numbers are visible or hidden in item and invoice workflows:
   - `Item number + description` keeps item numbers visible beside descriptions where supported.
   - `Description only` hides item numbers from supported selectors and line helpers without deleting them from item records.
6. Use `Settings` -> `Defaults` when you want to store tenant-level defaults for future companies or bulk-apply required-account-field and edit-policy defaults to selected active companies.
7. Use the archive action to move a company out of the active list when you no longer want it used day to day.
8. If needed, switch to the `Archived` or `All` filter to review archived companies.
9. Unarchive a company if it needs to become active again.
10. Permanently delete a company only after it has been archived first.
11. If SPRK warns that the company has journal entries, keep it archived instead of expecting permanent delete to succeed.

## What Happens Next

You can maintain company settings and lifecycle state without guessing which actions are reversible.

- Editing company settings changes setup values but does not create a journal entry by itself.
- A posting cutoff date can restrict which dates are allowed for future posted entries, but changing the cutoff does not repost prior activity automatically.
- Changing `Required account fields` affects account setup and visible account presentation. It does not delete existing account codes or change posted balances.
- Changing `Control accounts` changes future manual-journal availability for selected accounts. It does not delete accounts or rewrite existing posted lines.
- Changing `Sales / Invoicing` defaults can affect new invoice starting terms, due dates, and workflow status. It does not rewrite already posted invoices.
- Changing company contact fields or `Payment Instructions` can affect future printed customer invoices. It does not post accounting activity.
- Changing `Item identification` affects visible item labels in supported workflows. It does not delete item numbers, item accounts, or posted invoice lines.
- `Defaults` bulk apply changes required account fields and accounting edit permissions on selected active companies while preserving unrelated company accounting settings.
- Archiving or unarchiving a company changes availability in the company list and selector; it does not create, edit, or delete journal entries.
- Permanent deletion is limited to archived companies, and companies with journal-entry activity are blocked from deletion.

## If Something Looks Wrong

- Trying to delete an active company before archiving it.
- Assuming a company with accounting activity can always be removed permanently.
- Treating setup edits as though they rewrite prior transactions automatically.
- Assuming a missing manual-journal account picker option means the account is inactive. It may be configured as a control account.
- Assuming hidden item numbers were removed from item records. Review `Item identification` before editing item master data.
- Assuming company invoice defaults change historical invoice postings. They seed future workflow values only.

## Related

- [Use the Companies tab](./use-the-companies-tab.md)
- [Manage default company settings](./manage-default-company-settings.md)
- [Set up and use dimensions or classes](./set-up-and-use-dimensions-or-classes.md)
- [Understand the chart of accounts structure](../ledger-and-chart-of-accounts/understand-the-chart-of-accounts-structure.md)
- [Understand audit-sensitive ledger behavior](../ledger-and-chart-of-accounts/understand-audit-sensitive-ledger-behavior.md)
