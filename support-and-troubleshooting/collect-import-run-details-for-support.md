# Collect Import Run Details for Support

Gather visible import context after a failed, partial, duplicate, or confusing import without changing the source data again.

![Support tab showing the Support Activity Log, contact options, and bug-reporting link](../screenshots/support-and-troubleshooting/collect-support-details-step-01.png)

## When To Use This

- An import preview does not match what you expected.
- An import confirmation creates unexpected records, pending rows, documents, or journal entries.
- Duplicate warnings, unresolved names, account issues, or validation messages need review.
- You need to contact support with the details of a specific import attempt.

## Do This First

1. Stop before confirming another import attempt unless support asks you to retry.
2. Note the active company and import page.
3. Record whether you only previewed the file or confirmed it.
4. If you confirmed an import, write down what changed afterward: pending bank rows, journal entries, documents, accounts, vendors, or reports.
5. Open `Support` and download the `Support Activity Log`.

## Details To Capture

- Active company.
- Import page or workflow.
- File type, such as `.csv`, `.xlsx`, `.qbo`, `.qfx`, `.ofx`, `.iif`, or `.zip`.
- Destination account when the import is account-specific, such as a bank or credit-card account.
- Row or entry counts.
- Duplicate warnings.
- Unresolved accounts, customers, vendors, or items.
- Validation messages.
- Whether any rows were selected or skipped.
- Whether the import was preview-only or confirmed.
- What changed after confirmation.
- Support Activity Log.

## What To Avoid

- Do not retry the same file repeatedly before capturing warnings.
- Do not make manual cleanup entries before saving the original mismatch details.
- Do not describe hidden technical fields that are not visible in SPRK.
- Do not assume invoice, bill, bank, journal, and company imports have identical correction behavior.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| The import failed but the details are vague | Page, file type, visible message, and preview result | Capture the specific visible context before contacting support |
| Duplicate warnings disappeared after retrying | Whether the first preview details were saved | Stop and collect the current preview and support log |
| The result changed after confirmation | Which records, rows, documents, or journals changed | Record the changed area before attempting cleanup |
| The import type is unclear | Whether it was bank, journal, invoice, bill, company, or rule import | Use the workflow name support can trace |

## Practice And Examples

- Practice file: [import-run-details-support.csv](../sample-files/practice/import-run-details-support.csv)

![Support tab showing support activity log, contact information, release controls, and guide sync context](../screenshots/v1-validation/support-log-guides-sync.png)

## Related

- [Collect the right details before contacting support](./collect-the-right-details-before-contacting-support.md)
- [Before you import](../company-setup-and-migration/before-you-import.md)
- [Import bank transactions](../banking-and-cash-management/import-bank-transactions.md)
- [Prepare and review ledger imports and exports](../ledger-and-chart-of-accounts/understand-ledger-import-and-export-behavior.md)
