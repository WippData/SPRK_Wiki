# Understand When An Upgrade Prompt May Appear

![License tab showing usage limits and plan details](../screenshots/licensing/usage-limits-step-01.png)

SPRK may show an upgrade or add-license prompt when you try to create another real company after using the free company allowance.

## When To Use This

Use this workflow when you want to understand the most common point where SPRK asks for a license so you can decide whether to add a key or change your setup plan.

## Before You Start

- You are signed in to SPRK.
- You already have one real company, or you are planning to add another one.

## Steps

1. Open `Companies` from the `System` section if you want to review how many real companies already exist.
2. Open `License` from the `System` section to review the current license status.
3. If you try to create another real company after the free allowance has been used, review the prompt that asks you to add a license or buy one through Stripe.
4. If you already have a valid license, enter or update the saved license details in `License` and save them.
5. Return to the company-creation flow after the license details have been saved.

## What Happens Next

You understand that the clearest published upgrade prompt appears around additional real company creation, and that adding a valid license removes that setup barrier without changing historical accounting data.

- Seeing an upgrade prompt does not create a journal entry.
- Saving a license key changes tenant access and company-creation eligibility only.
- Buying a license through the external Stripe link is outside the in-app general ledger workflow unless you separately record that purchase in your books.

## If Something Looks Wrong

- Assuming the prompt means your existing company is locked or your books were changed.
- Counting `Demo Company` as the free real company.
- Treating a licensing prompt as an accounting transaction instead of an access-control message.

## Related

- [View license information](./view-license-information.md)
- [Understand usage limits and prompts](./understand-usage-limits-and-prompts.md)
- [Create your first company](../company-setup-and-migration/create-your-first-company.md)
- [Switch between companies](../company-setup-and-migration/switch-between-companies.md)
