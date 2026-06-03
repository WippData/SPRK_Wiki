# Understand Audit-Sensitive Ledger Behavior

Review the current rules around journal-entry edits, reversal entries, and inactive-account handling so you know which ledger changes preserve history and how they affect balances.

## Purpose

Use this article when you need to understand how SPRK preserves history around journal entries and account maintenance.

## Prerequisites

- An active company is selected.
- You understand which existing entry or account you want to review or maintain.

## Steps

1. Treat saved journal entries as posted records, not scratch work.
2. Before editing an existing journal entry, confirm your company allows the kind of change you need:
   - memo edits can be restricted
   - date edits can be restricted
   - line amount edits can be restricted
   - dimension edits can be restricted
   - account changes are not allowed line-by-line in the current edit path
3. If a correction should preserve the original posting trail, use reversal behavior instead of trying to overwrite history.
4. When reversing an entry, choose the posting-date mode that fits the correction:
   - `today`
   - `original`
   - `custom`
5. For a confirmed bank transaction with a linked journal entry, open the journal from `Reconcile` and reverse from the linked journal modal.
6. Remember that a reversal creates a separate entry with flipped debit and credit amounts rather than deleting the original.
7. In `Chart of Accounts`, treat account deletion as deactivation. Prior activity remains part of the company history.

## Expected Result

You understand which maintenance actions keep an audit trail and how they affect balances. Current general ledger impact as of 2026-05-29:

- Reversing a journal entry creates a new journal entry that flips each original debit and credit line, which offsets the original entry in the general ledger.
- SPRK prevents reversing a reversal and prevents reversing the same original entry more than once.
- If a reversal is tied to an unreconciled bank transaction, SPRK excludes the original bank row for audit history.
- If a reversal is tied to a reconciled bank transaction, SPRK creates a confirmed correction bank transaction instead of changing the reconciled row.
- When journal edits are allowed, the saved entry itself is updated and an edit-audit record is stored alongside the before-and-after versions.
- Marking an account inactive does not remove prior ledger activity or create a new journal entry.

## Common Mistakes

- Assuming reversal deletes the original entry. It creates a separate offsetting entry.
- Assuming linked bank reversal always changes the original bank row. Reconciled rows are preserved and corrected with a separate bank transaction.
- Expecting to swap an entry line to a different account during edit. The current edit rules do not allow account changes on existing lines.
- Treating inactive accounts as erased accounts. Inactive status only changes availability for future use.

## Related Articles

- [Record journal entries](./record-journal-entries.md)
- [Edit linked ledger and bank activity](./edit-linked-ledger-and-bank-activity.md)
- [Understand ledger import and export behavior](./understand-ledger-import-and-export-behavior.md)
- [Understand the chart of accounts structure](./understand-the-chart-of-accounts-structure.md)
- [Understand database alignment and recovery escalation](../support-and-troubleshooting/understand-database-alignment-and-recovery-escalation.md)

## Info

- App sections: `ledger`, `chart`
- Last validated: 2026-06-03
- Screenshot status: `captured`
