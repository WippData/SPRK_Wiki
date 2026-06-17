# Understand Authenticated Shared Backend Service Mode

Use this support-facing article to describe the opt-in Windows shared-backend deployment model without changing the normal standalone desktop story.

## Purpose

Use this article when support or deployment owners need to explain a packaged SPRK client that attaches to a local shared backend service.

## Key Points

- Shared backend service mode is an opt-in packaged Windows deployment model, not the default standalone app path.
- In service mode, the backend can publish local runtime metadata with an origin and bearer token.
- Packaged desktop clients attach the token to API requests only when that runtime token is present.
- The release boundary is local desktop attachment. Do not describe this as cloud hosting, browser access, LAN sharing, or general remote access.
- The storage model still expects one SQLite owner. Do not imply multiple independent backend writers or hosted multi-user firm administration.
- If the runtime descriptor or token is missing, a packaged client may fail to attach even when the local service is running.

## Troubleshooting Details to Collect

- Operating system and packaged app version.
- Whether the user expected normal standalone mode or service mode.
- Whether the local service is running.
- Whether the packaged client can load company data.
- Any visible connection or authorization error.
- Support Activity Log output with tokens and local secret values redacted.

## Expected Result

Support can explain the service-mode boundary without exposing secrets or expanding the public capability claim. Current general ledger impact as of 2026-06-17:

- Runtime attachment does not post accounting activity by itself.
- Normal accounting changes still occur only through the app workflows the user performs after the client is connected.

## Common Mistakes

- Treating service mode as a browser, cloud, or cross-machine feature.
- Publishing bearer tokens, runtime descriptor contents, or local filesystem paths in screenshots.
- Assuming service mode permits multiple database owners.
- Applying service-mode troubleshooting to a normal standalone macOS app session.

## Related Articles

- [Sign in to SPRK](../getting-started/sign-in-to-sprk.md)
- [Use the Support tab](./use-the-support-tab.md)
- [Collect the right details before contacting support](./collect-the-right-details-before-contacting-support.md)

## Info

- App sections: `support`, `desktop runtime`
- Last validated: 2026-06-17
- Screenshot status: `not required`
