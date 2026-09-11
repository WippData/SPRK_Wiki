# Import from QuickBooks Desktop IIF

<!-- Screenshot status: Review needed -->

![Import Wizard showing accepted IIF and spreadsheet file formats](../screenshots/company-setup-and-migration/import-wizard-starter-templates-step-01.png)

Create or import a company in SPRK from a QuickBooks Desktop IIF export using the Companies page.

## When to use this

Use this guide when your source data comes from QuickBooks Desktop and you exported it as an `.iif` file.

## Before you start

- You can open `Companies` from the left sidebar.
- You exported the source data from QuickBooks Desktop as an `.iif` file.
- You have room to create another company in your workspace.

## Steps

1. In QuickBooks Desktop, export the data you want to migrate as an IIF file.
2. In SPRK, open `Companies` from the left sidebar.
3. Open the menu attached to `New Company`.
4. Select `Import from QBD (IIF)`.
5. In the file picker, choose the `.iif` export.
6. Wait for SPRK to complete the import and refresh the list.
7. Confirm that the imported company appears in the `Companies` table.
8. Review the imported company before daily use, with extra attention to chart of accounts, customers, and vendors.
9. Review customer billing addresses after import when the source file includes QuickBooks `BADDR1` through `BADDR5` fields:
   - SPRK can preserve the first billing line as address line 1.
   - Remaining non-city billing lines can be kept in address line 2.
   - A final `City, ST ZIP` line can populate city, state, and postal code when it is parseable.
   - Clean up any customer whose address did not follow that pattern before sending customer-facing invoices.

## What happens next

SPRK imports the QuickBooks Desktop IIF file and adds the resulting company to the companies list.


## Related

- [Create your first company](./create-your-first-company.md)
- [Import from QuickBooks Online ZIP](./import-from-quickbooks-online-zip.md)
- [Use the Import Wizard](./use-the-import-wizard.md)
- [Switch between companies](./switch-between-companies.md)
