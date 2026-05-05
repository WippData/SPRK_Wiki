# Start a Reconciliation

Open the reconciliation workflow for a bank or credit card account, review the statement dates and balances that SPRK locks or derives, and start the clearing session correctly.

## Purpose

Use this workflow when you are ready to begin reconciling one bank or credit card account against a statement.

## Prerequisites

- An active company is selected.
- The bank or credit card account you want to reconcile already exists.
- The transactions you expect to clear have already been confirmed in SPRK.
- For a first-time reconciliation with no prior reconcile history, you know which journal entry should serve as the opening balance anchor for that account.

## Steps

1. Open `Reconcile`.
2. In the account picker near the page header, choose the bank or credit card account you want to reconcile.
3. Select `Start`.
4. Review the `Start reconciliation` window:
   - If SPRK finds a prior reconciliation for that account, the `Statement opening date` and `Statement opening balance` fields are locked from the last posted reconciliation before the selected statement ending date.
   - If SPRK does not find a prior reconciliation, select the `Opening balance journal entry` that should anchor the account's first reconciliation.
5. For a first-time reconciliation, confirm that SPRK derives the opening and ending values from the selected journal entry before continuing.
6. If this is not the first reconciliation, enter or confirm the `Statement ending date`.
7. If this is not the first reconciliation, enter the `Statement ending balance`:
   - Use a positive number for bank accounts.
   - Use a negative number for credit accounts.
8. Select the modal action to continue:
   - `Start` begins a normal reconciliation session when a prior reconciliation exists.
   - `Reconcile` completes the opening anchor flow immediately when this is the first reconciliation and you are using the journal-entry anchor.

## Expected Result

The reconciliation workflow is initialized with statement dates and balances for the selected account. Current transaction and general ledger impact as of 2026-05-02:

- Starting a normal reconciliation session does not create a new general ledger entry.
- The page loads confirmed transactions for the selected account and preselects those that fall inside the statement window.
- A first-time opening anchor also does not create a journal entry. It creates a posted reconciliation record so future reconciliations have an opening balance reference.

## Common Mistakes

- Starting on the wrong bank or credit card account.
- Choosing the wrong opening balance journal entry for the first reconciliation.
- Entering a positive ending balance for a credit account.
- Expecting SPRK to let you edit the opening balance from a prior posted reconciliation.

## Related Articles

- [Finish a reconciliation](./finish-a-reconciliation.md)
- [Match and unmatch transactions](./match-and-unmatch-transactions.md)
- [Resolve common reconciliation exceptions](./resolve-common-reconciliation-exceptions.md)

## Info

- App sections: `reconcile`
- Last validated: 2026-05-02
- Screenshot status: `not-started`
