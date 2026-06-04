# Use the Import Wizard

Build a new company from uploaded files, copied data, and manual settings when a simple one-file import is not enough.

![Import Wizard showing starter templates, required columns, recommended columns, and the Download Templates action](../screenshots/company-setup-and-migration/import-wizard-starter-templates-step-01.png)

## Purpose

Use the Import Wizard when your migration spans multiple files or when you want to mix uploaded files, copied data from an existing company, and manual settings in one guided flow.

## Prerequisites

- You can open `Settings` → `Companies`.
- You know the new company name you want to create.
- If you plan to upload files, they are ready in supported formats such as CSV, IIF, XLS, or XLSX.
- If you plan to copy data from an existing company, that company already exists in SPRK.

## Steps

1. Open `Settings` → `Companies`.
2. Open the menu attached to `New Company`.
3. Select `Import Wizard`.
4. Enter the new `Company name`.
5. In `Upload files`, review the starter help block before you assign anything.
6. Use `Download Templates` if you want starter files that match the wizard's current upload expectations.
7. Add one or more files in the `Upload files` area if you are importing source files.
   - The wizard can accept multiple files in the same run.
   - SPRK can auto-assign uploaded files to likely data types, but you should still review each assignment before creating the company.
8. If you want to reuse existing SPRK data, choose an `Existing company (optional)` as the default copy source.
9. In `Finalize your configuration`, choose a source for each data type:
   - file upload
   - existing company
   - manual settings, where offered
10. Review the data types carefully. Common categories include accounts, customers, vendors, items, trial balance, journal entries, invoices, bills, payments, and settings.
11. Select `Review & Create Company`.
12. On the confirmation step, verify the files and sources that will be used.
13. Create the company and wait for the wizard to finish.
14. Review the new company before using it for live work.

## Expected Result

SPRK creates a new company using the combination of files, copied data, and settings you selected in the wizard.

## Common Mistakes

- Starting the wizard without a company name. The review action is disabled until a name is entered.
- Skipping `Download Templates` when you need a starter format for a data type you have not prepared before.
- Uploading operational files such as invoices or bills without also bringing in foundation data like a chart of accounts or a trial balance.
- Assuming the wizard’s auto-assignment is final. Review each data type before creating the company.
- Forgetting that settings can be entered manually if no source file exists for them.

## Related Articles

- [Create your first company](./create-your-first-company.md)
- [Import from QuickBooks Online ZIP](./import-from-quickbooks-online-zip.md)
- [Import from QuickBooks Desktop IIF](./import-from-quickbooks-desktop-iif.md)
- [Switch between companies](./switch-between-companies.md)

## Info

- App sections: `companies`
- Last validated: 2026-06-04
- Screenshot status: `captured`
