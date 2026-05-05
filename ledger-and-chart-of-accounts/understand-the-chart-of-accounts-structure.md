# Understand the Chart of Accounts Structure

Review how SPRK organizes accounts by code, parent-child hierarchy, type, subtype, and active status so you can maintain a usable account list without changing posted balances.

## Purpose

Use this article when you need to understand how accounts are grouped, created, edited, imported, exported, or deactivated in the `Chart of Accounts` page.

## Prerequisites

- An active company is selected.
- You know whether you are adding a brand-new account, reorganizing an existing one, or reviewing the current structure.

## Steps

1. Open `Chart of Accounts`.
2. Review the page header tools:
   - `New` opens the account form.
   - `Refresh` reloads the list.
   - `Export` downloads the current chart as `chart-of-accounts.csv`.
   - `Import` accepts `.csv`, `.txt`, `.iif`, `.xls`, or `.xlsx` files.
3. Use the search field to find accounts by code or name.
4. Use the grouping controls to regroup the list and the expand or collapse controls to change how much of the hierarchy is visible.
5. Review the account list structure:
   - Accounts are sorted by code.
   - Child accounts can be linked by a saved parent account or inferred from account codes when the code structure supports it.
   - Filters let you narrow by `Type`, `Subtype`, and `Status`.
6. Select `New` or the edit pencil for an existing row when you need to maintain an account record.
7. When creating or editing an account, fill in the fields SPRK supports publicly:
   - `Code`
   - `Name`
   - `Type`
   - optional `Subtype`
   - optional parent account
   - optional description, bank number, or notes
8. Use status carefully:
   - Active accounts remain available for normal use.
   - Deleting an account from this page sets it inactive instead of removing its history.

## Expected Result

You can organize the account list into a clearer structure and keep accounts available for downstream workflows. Current general ledger impact as of 2026-05-02:

- Creating, editing, importing, exporting, or deactivating accounts from `Chart of Accounts` does not post a journal entry by itself.
- These actions change account setup and availability, not existing account balances.
- Export produces a file only and does not change ledger data.

## Common Mistakes

- Expecting `Delete` to erase prior history. SPRK marks the account inactive instead.
- Importing parent relationships without valid `parentId` values.
- Treating subtype as required for every account when the page only exposes it as an optional field.

## Related Articles

- [Record journal entries](./record-journal-entries.md)
- [Understand ledger import and export behavior](./understand-ledger-import-and-export-behavior.md)
- [Understand audit-sensitive ledger behavior](./understand-audit-sensitive-ledger-behavior.md)

## Info

- App sections: `chart`
- Last validated: 2026-05-02
- Screenshot status: `not-started`
