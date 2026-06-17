# Sample Files

This repository does not currently publish tracked import sample files.

Use the in-app template downloads first, such as `Download Template` in `Ledger` import or `Download Import Template` in `Banking`. Public sample files should only be added here after the team approves the asset convention, repository-size impact, renderer/download behavior, and sanitization rules.

## Proposed Convention

- Put public examples under `sample-files/imports/<workflow>/`.
- Use tiny, generic data with obvious labels such as `Sample Import Training`.
- Include one valid file and one intentionally invalid diagnostic file only when the UI can preview the invalid file safely.
- Do not include real customer, vendor, employee, bank, card, address, tax, payroll, or client data.
- Do not add proprietary QuickBooks sample exports unless rights and sanitization are confirmed.

## Current Public Guidance

- Bank import examples should be validated against the current Banking template and preview path before publication.
- Journal import examples should be validated against the server-side preview and batch commit workflow before publication.
- Invoice, bill, customer, vendor, item, rules, and company-wizard examples should match current visible templates before publication.
- If downloads must live outside this repository, link to the approved release artifact or support-download location from the relevant wiki article.
