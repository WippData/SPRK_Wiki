# Understand Import and Migration Boundaries

Use SPRK import paths with the right expectations: some imports have strong preview and retry guardrails, while others still need careful review after import.

![Import Wizard showing starter templates, download templates action, and upload guidance](../screenshots/company-setup-and-migration/import-wizard-starter-templates-step-01.png)

## When To Use This

Use this article when you are planning a client migration, comparing import options, or deciding how much post-import review a file needs.

## Key Points

- Bank import has the strongest public review path: choose an account, import a file, review pending rows, resolve categories/vendors where available, watch duplicate warnings, then confirm selected rows.
- Journal import uses the `Ledger` import path with a preview before posting. Preview alone does not post.
- Invoice and bill imports can support grouped document data where available, but review them carefully because each import path has its own confirmation and correction expectations.
- The Import Wizard is the broadest setup path for mixed company data. Direct `QuickBooks Online ZIP` and `QuickBooks Desktop IIF` paths are narrower and should not be described as perfect historical migrations.
- Company File export/import is the SPRK-to-SPRK handoff path once the source company already exists in SPRK.
- After any import, review chart of accounts, opening balances, customers, vendors, items, unpaid invoices, unpaid bills, bank activity, reconciliation status, and reports.

## Steps

1. Decide whether you are importing setup data, bank activity, journals, documents, or a complete SPRK company file.
2. Prefer the most specific import path for the data:
   - `Banking` for bank and card transactions.
   - `Ledger` for journal-entry files.
   - `Companies` or the Import Wizard for company setup and migration files.
   - `Backups` > `Company file` for a SPRK company handoff.
3. Download the visible template or starter file when SPRK offers one.
4. Preview before confirming whenever the product exposes a preview.
5. Capture visible diagnostics, duplicate warnings, row counts, and file type if the import does not behave as expected.
6. Run a post-import review before relying on reports or balances.

## What Happens Next

You can choose an import path without over-reading its guarantees.

- Preview and template-download steps do not post entries.
- Confirmed bank rows, opened invoices or bills, and committed journal batches can affect the ledger according to their workflow.
- Failed or blocked previews should not be treated as posted accounting activity.
- Direct QuickBooks imports are setup aids, not a promise that every historical QuickBooks transaction type is recreated perfectly.

## If Something Looks Wrong

- Assuming every import path has the same duplicate review, confirmation, or correction options.
- Treating a public sample or downloaded template as a required production format instead of a starting point.
- Skipping post-import review because the file uploaded successfully.
- Using Company File language for ordinary bank, journal, invoice, or bill imports.

## Related

- [Use the Import Wizard](./use-the-import-wizard.md)
- [Import bank transactions](../banking-and-cash-management/import-bank-transactions.md)
- [Prepare and review ledger imports and exports](../ledger-and-chart-of-accounts/understand-ledger-import-and-export-behavior.md)
- [Export and import Company Files](../backups-and-data-safety/export-and-import-company-files.md)
- [Collect import run details for support](../support-and-troubleshooting/collect-import-run-details-for-support.md)
