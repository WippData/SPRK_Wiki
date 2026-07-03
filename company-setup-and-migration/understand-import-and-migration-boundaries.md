# Understand Import and Migration Boundaries

Choose the import or migration path that matches the file type and review risk before relying on imported data.

![Import Wizard showing starter templates, download templates action, and upload guidance](../screenshots/company-setup-and-migration/import-wizard-starter-templates-step-01.png)

## Use This Page When

Use this page when you are planning a client migration, comparing import options, or deciding how much post-import review a file needs.

## Choose This Path If

| Goal | Use | Check First |
|---|---|---|
| Prepare for any import | [Before you import](./before-you-import.md) | Active company, source file, template, preview warnings, and post-import review plan |
| Import mixed setup data into a new company | [Use the Import Wizard](./use-the-import-wizard.md) | Company name, data-type source slots, and setup records |
| Import bank or credit card transactions | [Import bank transactions](../banking-and-cash-management/import-bank-transactions.md) | Selected account, duplicate warnings, party names, and pending review |
| Import journal entries | [Prepare and review ledger imports and exports](../ledger-and-chart-of-accounts/understand-ledger-import-and-export-behavior.md) | Balanced rows, account labels, vendors, dates, and preview totals |
| Import grouped invoices | [Import invoices](../sales-and-receivables/import-invoices.md) | Customers, invoice numbers, line accounts, and `Receive to` routing |
| Import grouped bills | [Import bills](../expenses-and-payables/import-bills.md) | Vendors, bill numbers, line accounts, and `Pay from` routing |
| Move an existing SPRK company file | [Export and import Company Files](../backups-and-data-safety/export-and-import-company-files.md) | Company identity, export file, import preview, and replace warning |

## Before You Commit

- Preview before confirming whenever SPRK exposes a preview.
- Download the visible template or starter file when SPRK offers one.
- Capture visible diagnostics, duplicate warnings, row counts, and file type if the import does not behave as expected.
- Run post-import review before relying on reports or balances.
- For document imports, review control-account routing versus settlement-account routing before confirmation.

## What Not To Assume

- Every import path does not have the same duplicate review, confirmation, or correction options.
- Preview and template-download steps do not post entries.
- Confirmed bank rows, opened invoices or bills, and committed journal batches can affect the ledger according to their workflow.
- Imported documents that use cash, bank, or credit-card settlement routing can post as paid-now activity instead of remaining open AR/AP balances.
- Direct QuickBooks imports are setup aids, not a promise that every historical QuickBooks transaction type is recreated perfectly.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| A file was uploaded successfully but balances look wrong | Whether post-import review was completed | Review setup lists, documents, bank activity, reconciliation status, and reports |
| A template is being treated as the required production format | Whether the template is only a starter | Use it to shape the file, then review preview results |
| Grouped invoice or bill rows are being retried | Duplicate-number errors and previous import results | Resolve duplicates before confirming again |
| Paid-now documents still appear expected as open AR/AP | `Receive to` or `Pay from` routing | Use a control account when the document should stay open |
| Company File wording is used for ordinary imports | Whether the path is a SPRK company transfer | Use workflow-specific import language for bank, journal, invoice, or bill files |

## Related

- [Collect import run details for support](../support-and-troubleshooting/collect-import-run-details-for-support.md)
- [Create your first company](./create-your-first-company.md)
- [Import from QuickBooks Online ZIP](./import-from-quickbooks-online-zip.md)
- [Import from QuickBooks Desktop IIF](./import-from-quickbooks-desktop-iif.md)
