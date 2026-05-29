# Create a Starting Balance

Create the opening journal entry for a bank or credit account, then use `Reconcile` to establish the formal starting balance that future reconciliations will build from.

## Purpose

Use this workflow when you are setting up a company and need SPRK to recognize the first balance for a bank or credit account before regular reconciliation work begins.

## Prerequisites

- An active company is selected.
- The bank or credit account you want to reconcile already exists in the chart of accounts.
- You know the opening amount and effective date you want to establish.
- You know which offset account your team wants to use for the opening entry.

## Steps

1. Open `Ledger`.
2. Select `New`.
3. Create a manual journal entry dated on the day the opening balance should first appear in SPRK.
4. Add the bank or credit account line that should carry the starting balance.
5. Add the balancing line that offsets the opening amount in the account your team is using for setup.
6. Save the journal entry and confirm it appears in `Ledger`.
7. Open `Reconcile`.
8. In the account picker near the page header, choose the same bank or credit account from the journal entry.
9. Select `Start`.
10. In the `Start reconciliation` window, use `Opening balance journal entry` to choose the journal entry you just created.
11. Confirm that SPRK derives the first reconciliation values from that journal entry:
   - the opening-balance anchor entry appears in the picker by date and description
   - the statement dates are locked from the selected entry
   - the ending balance is populated from the selected entry amount
12. Select `Reconcile` to establish the starting balance for that account.

## Expected Result

SPRK uses the journal entry as the first reconciliation anchor for that account. Current transaction and general ledger impact as of 2026-05-15:

- Saving the journal entry posts the opening balance to the general ledger.
- Selecting that journal entry in `Start reconciliation` does not create a second journal entry.
- Completing the opening reconciliation creates the reconciliation anchor that later statement periods use as their beginning balance reference.

## Common Mistakes

- Creating the opening journal entry in the wrong account and then trying to reconcile a different account.
- Skipping `Reconcile` after saving the journal entry and assuming the starting balance is fully established already.
- Choosing the wrong journal entry in the `Opening balance journal entry` picker when more than one setup entry exists.
- Treating the locked dates and derived balance in the start modal as manual entry fields.

## Related Articles

- [Create your first company](./create-your-first-company.md)
- [Use the Import Wizard](./use-the-import-wizard.md)
- [Start a reconciliation](../reconciliation/start-a-reconciliation.md)
- [Record journal entries](../ledger-and-chart-of-accounts/record-journal-entries.md)

## Info

- App sections: `ledger`, `reconcile`
- Last validated: 2026-05-15
- Screenshot status: `not-started`
