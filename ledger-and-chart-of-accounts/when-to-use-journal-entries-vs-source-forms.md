# When To Use Journal Entries vs Source Forms

![New journal entry drawer showing balanced manual journal entry fields](../screenshots/ledger-and-chart-of-accounts/new-journal-entry-drawer-step-01.png)

Use this page to decide whether an accounting entry belongs in a source workflow such as invoices, bills, checks, banking, or in a manual journal entry.

## When To Use This

Use this guidance before posting a manual journal entry for activity that might belong to AR, AP, banking, or another workflow.

## Quick Decision Table

| Accounting need | Better starting point | Why |
| --- | --- | --- |
| Bill a customer | `Invoices` | Keeps customer balance, invoice status, payment history, and revenue detail together |
| Record a customer sale already paid at creation | `Invoices` with settlement `Receive to` | Posts through the source invoice while settling directly to cash, bank, or credit card |
| Receive money from a customer invoice | `Receive Payment` | Applies payment to AR instead of bypassing the customer balance |
| Enter a vendor bill | `Bills` | Keeps AP aging, vendor balance, payment status, and expense detail together |
| Record a vendor bill already paid at creation | `Bills` with settlement `Pay from` | Posts through the source bill while settling directly to cash, bank, or credit card |
| Pay a vendor by check | `Checks` or bill payment workflow | Keeps payment records connected to vendor and bank activity |
| Classify imported bank activity | `Banking` | Keeps bank review, rules, reconciliation, and ledger posting connected |
| Record accruals, reclasses, owner entries, allocations, or accountant adjustments | `Ledger` journal entry | These usually do not belong to a customer invoice, vendor bill, payment, or bank import row |
| Reverse a manual adjustment | `Ledger` reversal | Preserves history and offsets the original journal |

## Steps

1. Ask what real-world event you are recording.
2. If the event involves a customer invoice or payment, start in receivables.
3. If the event involves a vendor bill or payment, start in payables.
4. If the event came from a bank or credit card statement, start in banking.
5. If the event is an accountant adjustment, accrual, deferral, reclass, allocation, or owner/equity entry, use a journal entry.
6. If the original record already exists, correct it in the source workflow when possible.
7. If the original record needs to remain visible and offset, use a reversal or correcting entry.
8. Rerun reports after the correction so you can confirm both the balance and supporting detail look right.

## Journal Entry Examples

- Accrue an expense at month-end and reverse it next period.
- Reclassify an amount between expense accounts when no source transaction should change.
- Record owner contribution, owner draw, or equity activity.
- Record depreciation, amortization, or allocation entries.
- Correct a manual journal entry with a reversal or adjusting entry.

## Source Form Examples

- Create an invoice for a customer sale.
- Receive a customer payment against an invoice.
- Enter a vendor bill for AP tracking.
- Pay a bill or write a check.
- Confirm a bank transaction imported from a bank statement.

## If Something Looks Wrong

- Do not use journal entries to bypass AR or AP unless you intentionally do not want customer or vendor subledger tracking.
- Do not post directly to control accounts if the company is configured to use source workflows for those accounts.
- Use invoice `Receive to` and bill `Pay from` routing when a source document should post through AR/AP or settle immediately. Do not recreate those source-document postings with a manual journal unless you are intentionally outside the customer or vendor workflow.
- Do not classify bank activity with a journal entry when the transaction is waiting in Banking.
- Do not use source forms for pure accountant adjustments that do not involve a customer, vendor, bank transaction, or item.

## Related

- [Record journal entries](./record-journal-entries.md)
- [Common accountant corrections](./common-accountant-corrections.md)
- [Create and open invoices](../sales-and-receivables/create-and-open-invoices.md)
- [Create and manage bills](../expenses-and-payables/create-and-manage-bills.md)
- [Review and classify bank transactions](../banking-and-cash-management/review-and-classify-bank-transactions.md)
