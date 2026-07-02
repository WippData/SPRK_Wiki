# Before You Import

![Import wizard showing starter template download options](../screenshots/company-setup-and-migration/import-wizard-starter-templates-step-01.png)

Use this import preparation checklist before bringing company, list, bank, or ledger data into SPRK.

## When To Use This

Use this page before importing from QuickBooks, a spreadsheet, a bank file, or another source that will create or prepare records in SPRK.

## Before You Start

- The correct company exists in SPRK.
- You know the source system and file type.
- You know whether the import is for setup data, ledger entries, bank transactions, customers, vendors, items, or rules.
- You have time to review the import preview before confirming anything.

## Steps

1. Confirm the active company before selecting any import file.
2. Export or preserve a copy of the source data before changing it.
3. Review the source file before importing.
   - Remove duplicate rows you do not want in SPRK.
   - Confirm dates use the intended year and format.
   - Confirm account names or codes match the accounts you want in SPRK.
   - Confirm vendor and customer names are consistent.
4. Decide whether accounts, customers, vendors, and items should already exist in SPRK before the import.
5. Download the current SPRK template when the import page offers one.
6. Use the workflow-specific import page for the kind of file you have.
   - Use company import paths for QuickBooks migration files.
   - Use `Banking` for bank and credit card transactions.
   - Use `Ledger` for journal-entry imports.
   - Use `Rules` for banking rule imports.
   - Use `Invoices` or `Bills` for grouped document-line imports when those pages expose import.
7. Review the preview, totals, dates, accounts, names, and warnings before confirming.
8. Stop if the preview shows missing accounts, ambiguous names, invalid dates, out-of-balance entries, or unexpected totals.
9. For invoice or bill imports, confirm the routing columns before posting:
   - Invoice files can use `Receive to`, `Default Income Account`, and `Line Income Account`.
   - Bill files can use `Pay from`, `Default Expense Account`, and `Line Account`.
   - Control-account routing keeps documents on the accrual path; cash, bank, or credit-card settlement routing imports paid-now documents.
   - Do not combine control-account routing and settlement-account routing for the same document.
10. For rules imports, remember that generic `Conditions` and `Actions` can be plain text or JSON, but the preview must still contain valid rows before confirmation.
11. For journal imports, review code-plus-name account labels and any preview-filled date values before committing the batch.
12. After import, review the affected list, ledger, banking queue, or report before continuing with more imports.

## What Happens Next

A clean import prep process reduces duplicate records, wrong accounts, wrong dates, and cleanup work after migration.

- Previewing an import does not mean the data has posted.
- Confirming an import can create records, pending transactions, or journal entries depending on the workflow.
- Grouped invoice and bill imports can create posted documents when their status and account routing call for it.
- Empty previews, duplicate document numbers, unresolved accounts, missing customers or vendors, nonpositive quantities, or invalid routing should be fixed in the source file before confirmation.
- If the preview is unclear, stop and resolve the source file before committing.

## If Something Looks Wrong

- Do not import into the wrong active company.
- Do not assume spreadsheet column names are close enough; use the current template when available.
- Do not ignore preview warnings because the file came from a familiar source system.
- Do not import a full file repeatedly unless SPRK explicitly identifies it as safe to retry.
- Do not use bank imports for journal-entry activity or ledger imports for bank-feed review.
- Do not assume paid-now invoice or bill imports behave like open AR/AP documents. Review `Receive to` or `Pay from`.

## Related

- [Import from QuickBooks Online ZIP](./import-from-quickbooks-online-zip.md)
- [Import from QuickBooks Desktop IIF](./import-from-quickbooks-desktop-iif.md)
- [Use the Import Wizard](./use-the-import-wizard.md)
- [Import bank transactions](../banking-and-cash-management/import-bank-transactions.md)
- [Prepare and review ledger imports and exports](../ledger-and-chart-of-accounts/understand-ledger-import-and-export-behavior.md)
- [Create and manage rules](../banking-and-cash-management/create-and-manage-rules.md)
