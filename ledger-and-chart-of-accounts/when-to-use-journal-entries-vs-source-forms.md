# When to Use a Journal Entry

Use this page to choose whether an accounting event belongs in invoices, bills, checks, banking, or a manual journal entry.

Journal entries affect the ledger, but they do not manage customer invoices, vendor bills, payment history, or bank review by themselves.

## Use This Page When

Use this guide before posting a manual journal entry for activity that may belong on an invoice, bill, payment, check, or bank transaction instead.

## Choose This Path If

| Goal | Use | Check First |
|---|---|---|
| Bill a customer | [Create and open invoices](../sales-and-receivables/create-and-open-invoices.md) | The invoice should carry customer balance, status, due date, revenue lines, and payment history. |
| Record a customer sale that is paid immediately | [Create and open invoices](../sales-and-receivables/create-and-open-invoices.md) with a settlement account in `Receive to` | The sale should settle directly instead of remaining as an open receivable. |
| Receive money from an existing customer invoice | [Receive invoice payments](../sales-and-receivables/receive-invoice-payments.md) | The payment belongs to an open invoice and should reduce the customer balance. |
| Enter a vendor bill | [Create and manage bills](../expenses-and-payables/create-and-manage-bills.md) | The bill should carry vendor balance, due date, expense lines, and payment history. |
| Record a vendor bill that is paid immediately | [Create and manage bills](../expenses-and-payables/create-and-manage-bills.md) with a settlement account in `Pay from` | The bill should settle directly instead of remaining as an open payable. |
| Pay a vendor by check | [Work with checks](../expenses-and-payables/work-with-checks.md) or the bill payment action | The payment should stay connected to vendor, bank, and payment records. |
| Classify imported bank activity | [Review and classify bank transactions](../banking-and-cash-management/review-and-classify-bank-transactions.md) | The row is waiting in Banking and should stay connected to bank review and reconciliation. |
| Record accruals, reclasses, owner entries, allocations, or accountant adjustments | [Record journal entries](./record-journal-entries.md) | The event does not belong to a customer, vendor, payment, check, or bank-review workflow. |
| Correct an existing accounting record | [Common accountant corrections](./common-accountant-corrections.md) | The original source, posting state, payment state, and audit trail are understood before choosing a correction path. |

## Before You Commit

- Before posting a journal entry, confirm the real-world event you are recording.
- Check whether a customer, vendor, bank transaction, check, invoice, bill, or payment record already exists for the event.
- Review control-account routing before posting directly to Accounts Receivable or Accounts Payable.
- Confirm the date, amount, account, customer, vendor, and supporting document before posting, paying, reversing, or correcting.
- If the original record should remain visible and offset, use the supported reversal or correction workflow instead of overwriting the history.

## What Not To Assume

- A journal entry does not update invoice status, bill status, customer balance detail, vendor balance detail, or payment history by itself.
- Source workflows are not the right place for pure accountant adjustments that do not involve a customer, vendor, bank transaction, check, item, or payment record.
- A bank statement row waiting in Banking should not be replaced with a manual journal unless you intentionally want separate ledger activity outside bank review.
- `Receive to` on invoices and `Pay from` on bills choose the document's posting path. They should not be recreated with a separate manual journal unless the source workflow is intentionally not being used.
- Control accounts may be restricted from manual journal entry so AR and AP activity stays tied to source workflows.

## Related

- [Record journal entries](./record-journal-entries.md)
- [Common accountant corrections](./common-accountant-corrections.md)
- [Create and open invoices](../sales-and-receivables/create-and-open-invoices.md)
- [Create and manage bills](../expenses-and-payables/create-and-manage-bills.md)
- [Review and classify bank transactions](../banking-and-cash-management/review-and-classify-bank-transactions.md)
