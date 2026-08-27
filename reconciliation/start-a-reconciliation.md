# Start a Reconciliation

Open the reconciliation workflow for a bank or credit card account, review the statement dates and balances that SPRK locks or derives, and start the clearing session correctly.

<!-- Last validated against SPRK source: 2026-08-27 -->

## When To Use This

Use this workflow when you are ready to begin reconciling one bank or credit card account against a statement.

For an enabled balance-sheet account that is not a bank register, use [Reconcile general ledger accounts](./reconcile-general-ledger-accounts.md).

## Before You Start

- An active company is selected.
- The bank or credit card account you want to reconcile already exists.
- You are ready to confirm that the selected account matches the statement you are holding, even if SPRK opens a saved default account automatically.
- The transactions you expect to clear have already been confirmed in SPRK.
- For a first-time reconciliation, you know whether the account opened at zero or needs a ledger entry for its opening balance.

## Steps

1. Open `Reconcile`.
2. In the account picker near the page header, choose the bank or credit card account you want to reconcile.
   - If SPRK opens a saved default account automatically, confirm that it matches the statement before you continue.
3. Select `Start`.
4. Review the `Start reconciliation` window:
   - If SPRK finds a prior reconciliation for that account, the `Statement opening date` and `Statement opening balance` fields are locked from the last posted reconciliation before the selected statement ending date.
   - If SPRK does not find a prior reconciliation, choose `Start at $0 — New account` or `Use a Ledger Entry to establish the opening balance` under `How should this account start?`.

![First reconciliation choices for a new bank account](../screenshots/reconciliation/first-reconciliation-start-methods-step-01.png)
5. For `Start at $0 — New account`, enter `Account opened on`; `Starting balance` stays at $0. For the ledger-entry method, choose `Opening balance journal entry` or use `Create Opening Balance` to make the balanced entry first.
6. If this is not the first reconciliation, enter or confirm the `Statement ending date`.
   - Use the calendar control or type the date directly in the order set by your `Preferences` date format.
7. If this is not the first reconciliation, enter the `Statement ending balance`:
   - Use a positive number for bank accounts.
   - Use a negative number for credit accounts.
8. Select the modal action to continue:
   - `Start` begins a normal reconciliation session when a prior reconciliation exists.
   - The first-time action establishes the chosen opening anchor and continues the reconciliation workflow.

## How SPRK Determines The Beginning Balance

SPRK uses reconciliation history to set the beginning balance for a normal reconciliation. It does not recalculate the beginning balance from every general-ledger line each time you open the reconciliation page.

- For the first reconciliation, the source is either a nonposting $0 opening anchor or the selected `Opening balance journal entry`.
- For later reconciliations, the source is the last posted reconciliation for the same account before the selected statement ending date.
- The `Statement opening date` and `Statement opening balance` are locked from that prior posted reconciliation record. They are carried forward as reconciliation history, not edited directly in the start window.
- Starting or finishing reconciliation does not create a journal entry, and selecting an opening-balance journal entry for the first anchor does not create a duplicate ledger posting.
- If a journal entry that affects an earlier period is later edited or reversed, financial reports can change according to that ledger correction, while posted reconciliation history continues to show the values recorded for that statement period.
- Use [Resolve common reconciliation exceptions](./resolve-common-reconciliation-exceptions.md) when the opening balance looks wrong.

## What Happens Next

The reconciliation workflow is initialized with statement dates and balances for the selected account.

- Starting a normal reconciliation session does not create a new general ledger entry.
- The page loads confirmed transactions for the selected account and preselects those that fall inside the statement window.
- Eligible unreconciled confirmed rows can still appear for manual selection even when their transaction date is after the statement ending date. Use statement evidence to decide whether a later-dated row belongs on the current statement.
- The $0 opening choice does not create a journal entry. Choosing an existing opening-balance entry does not post it a second time. Both choices establish reconciliation history for later periods.

## If Something Looks Wrong

| What You See | What To Check | What To Do Next |
|---|---|---|
| The first opening balance is wrong | Whether you chose $0 or the correct `Opening balance journal entry` | Return to the start choices before establishing the first reconciliation |
| Later-dated rows still appear | Whether they are confirmed, unreconciled activity for the account | Select only the rows supported by the current statement |

## Practice And Examples

Use the practice file and screenshots to review selected statement rows, a zero difference, and posting the reconciliation.

- Practice file: [reconciliation-statement-items.csv](../sample-files/practice/reconciliation-statement-items.csv)

![Reconciliation selected rows with a zero difference before posting](../screenshots/v1-validation/reconciliation-zero-difference-selected-rows.png)

![Reconciliation completion confirmation after posting](../screenshots/v1-validation/reconciliation-complete-toast.png)

Selected statement rows can tie to the entered ending balance. Posting the reconciliation creates history for later report review.

## Related

- [Choose bank and credit card accounts](../banking-and-cash-management/choose-bank-and-credit-card-accounts.md)
- [Finish a reconciliation](./finish-a-reconciliation.md)
- [Reconcile general ledger accounts](./reconcile-general-ledger-accounts.md)
- [Match and unmatch transactions](./match-and-unmatch-transactions.md)
- [View and print bank reconciliation reports](./view-and-print-bank-reconciliation-reports.md)
- [Resolve common reconciliation exceptions](./resolve-common-reconciliation-exceptions.md)
- [Create a starting balance](../company-setup-and-migration/create-a-starting-balance.md)
- [Use the Preferences tab](../preferences-and-personalization/use-the-preferences-tab.md)
