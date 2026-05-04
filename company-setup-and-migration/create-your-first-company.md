---
title: Create Your First Company
summary: Create a company from the Companies tab and set the core accounting options that SPRK uses for day-to-day work.
audience: End users
app_sections:
  - companies
workflow_type: setup
source_refs:
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/settings/companies/companies.tsx
  - /Users/nathancunningham/Code/SPRK_Desktop-frontend/src/features/settings/companies/companySettingOptions.ts
last_validated: 2026-05-01
screenshot_status: not-started
owner: codex
---

## Purpose

Use this workflow when you want to start a new company in SPRK without importing it from another accounting system.

## Prerequisites

- You can open `Settings` → `Companies`.
- You have permission to create a company in your current workspace.
- You know the company display name you want to use.
- You know whether you want SPRK to start with default accounts or a blank chart.

## Steps

1. Open `Settings` → `Companies`.
2. Select `New Company`.
3. In the `New Company` drawer, complete the core fields:
   - `Company Display name` is required.
   - `Legal name` is optional if it is different from the display name.
   - `Currency` sets the default reporting currency.
   - `Country (ISO)` is the two-letter country code shown in the form, such as `US`.
4. Leave `Accounts setup` turned on if you want SPRK to seed default accounts. Turn it off only if you want to start with a blank chart.
5. Review optional accounting settings if they matter for your rollout:
   - `Posting Cutoff Date`
   - `Fiscal Year End`
   - `Required account fields`
   - `Dimensions`
   - `Default Accounts Receivable`
   - `Default Accounts Payable`
6. Select `Create`.
7. Confirm that the new company appears in the companies list and becomes the active company after creation.

## Expected Result

The new company is added to the `Companies` table and becomes available as the active company across the app.

## Common Mistakes

- Leaving `Company Display name` blank. The create action is not meant to succeed without it.
- Turning off `Accounts setup` without planning how the chart of accounts will be created afterward.
- Setting the wrong `Country (ISO)` format. Use the short country code shown by the product, not the full country name.
- Ignoring default receivable or payable account settings when your team needs invoices or bills immediately after setup.

## Related Articles

- [Import from QuickBooks Online ZIP](./import-from-quickbooks-online-zip.md)
- [Import from QuickBooks Desktop IIF](./import-from-quickbooks-desktop-iif.md)
- [Use the Import Wizard](./use-the-import-wizard.md)
- [Switch between companies](./switch-between-companies.md)
