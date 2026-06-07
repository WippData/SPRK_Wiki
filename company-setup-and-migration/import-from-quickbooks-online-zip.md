# Import from QuickBooks Online ZIP

![Import Wizard showing accepted import files and data-type mapping](../screenshots/company-setup-and-migration/import-wizard-starter-templates-step-01.png)

Create a company in SPRK by importing a QuickBooks Online ZIP export from the Companies page.

## Purpose

Use this workflow when you already exported company data from QuickBooks Online and want SPRK to create or import the company from that ZIP package.

## Prerequisites

- You can open `Settings` → `Companies`.
- You have a QuickBooks Online export saved as a `.zip` file.
- You have room to create another company in your workspace.

## Steps

1. Open `Settings` → `Companies`.
2. Open the menu attached to `New Company`.
3. Select `Import from QBO (ZIP)`.
4. In the file picker, choose the QuickBooks Online `.zip` export.
5. Wait for SPRK to finish the import and refresh the companies list.
6. Confirm that the imported company appears in the `Companies` table.
7. If needed, select the new company so it becomes the active company across the app.
8. Review imported records before moving into daily work, especially chart of accounts, customers, and vendors.

## Expected Result

SPRK imports the QuickBooks Online ZIP and adds the imported company to the companies list.

## Common Mistakes

- Choosing a file that is not a QuickBooks Online ZIP export.
- Using the QBO import path for a QuickBooks Desktop IIF file.
- Skipping the post-import review and assuming every record mapped exactly as expected.
- Expecting this workflow to load every possible historical workflow automatically. Review the imported company before production use.

## Related Articles

- [Create your first company](./create-your-first-company.md)
- [Import from QuickBooks Desktop IIF](./import-from-quickbooks-desktop-iif.md)
- [Use the Import Wizard](./use-the-import-wizard.md)
- [Switch between companies](./switch-between-companies.md)

## Info

- App sections: `companies`
- Last validated: 2026-05-01
- Screenshot status: `captured`
