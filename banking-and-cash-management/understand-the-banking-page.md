# Understand the Banking Page

Learn how the Banking page is organized so you can choose the right bank or credit card account, import activity into that account, review pending transactions, and confirm what should post to the general ledger.

## Purpose

Use this article when you want a high-level map of the Banking page before importing or categorizing transactions.

## Prerequisites

- You are signed in to SPRK.
- An active company is selected.
- Your company has at least one bank or credit card account if you want to review real transaction activity.

## Steps

1. Open `Banking`.
2. Review the page header:
   - The page title is `Bank & Credit Import`.
   - `New` lets you enter a bank transaction manually.
   - `Refresh` reloads the current account activity and pending suggestions.
3. Use the account cards near the top of the page to choose the bank or credit card account you want to work in:
   - SPRK can open a saved default account automatically when one is already set for the active company.
   - If no account is active yet, choose one before you import or review activity.
   - Each card stays tied to one account, so imports and transaction review happen in the account you selected.
   - A badge on the card shows how many pending transactions still need review for that account.
   - `Default on open` marks the account SPRK will try to open first next time.
4. If the account you need is missing, add the bank or credit card account before continuing:
   - Some chooser views can offer an add-account path without leaving the current workflow.
   - The account must exist in the active company before you can import or reconcile activity into it.
5. Use the upload area beside the account cards to import one file at a time for the selected account:
   - You can click the uploader or drag a file onto it.
   - Importing only adds or updates pending transactions for the selected account.
6. Review the `Transactions` area:
   - Filters support description, amount, date, amount type, categorized-to account, rule-applied status, and class filters when dimensions are enabled.
   - `Pending` shows transactions that still need review before posting.
   - `Categorized` shows transactions that were already confirmed.
7. In the `Pending` tab, use the row-level fields and actions:
   - `Vendor` is optional.
   - `Categorize To` selects the account for the other side of the journal entry.
   - `Split` lets you allocate one transaction across multiple accounts.
   - `Find Check` appears when check matching is supported for the selected account.
   - The primary action confirms the transaction once it is ready.
8. Use the bulk controls above the table when you want to apply one account, apply one vendor, confirm several transactions, or delete several transactions at once.

## Expected Result

You understand where to select the account, where imported files enter the workflow, and which parts of the page only prepare transactions versus which step actually posts to the general ledger. Current ledger impact as of 2026-05-20:

- Viewing the Banking page does not post anything to the general ledger.
- Selecting an account or saving a default account does not post anything to the general ledger.
- Selecting accounts, filtering, importing files, editing categories, assigning vendors, creating splits, and matching checks on the page are preparation steps only.
- General ledger posting happens when a pending transaction is confirmed.

## Common Mistakes

- Working in the wrong bank or credit card account card before importing or confirming transactions.
- Treating the `Categorized` tab as the place where edits are staged. It reflects transactions that are already confirmed.
- Assuming a rule-based suggestion means the transaction has already posted.
- Forgetting that importing into the wrong selected account sends the pending rows into that account's workflow.
- Relying on the wrong saved default account when you switch between multiple bank or credit card accounts.

## Related Articles

- [Choose bank and credit card accounts](./choose-bank-and-credit-card-accounts.md)
- [Review and classify bank transactions](./review-and-classify-bank-transactions.md)
- [Create and manage rules](./create-and-manage-rules.md)
- [Import bank transactions](./import-bank-transactions.md)

## Info

- App sections: `banking`
- Last validated: 2026-05-30
- Screenshot status: `captured`
