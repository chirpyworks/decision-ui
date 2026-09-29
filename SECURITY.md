# Security Policy

Decision UI is primarily Markdown instructions and static references. It does not require credentials, network access, telemetry, or runtime code to provide its core behavior.

## Supported versions

Security fixes are applied to the latest released version.

## Report a vulnerability

Please do not open a public issue for:
- exposed credentials,
- malicious instruction injection,
- unsafe executable content,
- supply-chain compromise,
- private-data disclosure.

Use GitHub's private vulnerability reporting feature once the standalone repository is public.

## Trust model

Treat any third-party fork as untrusted until reviewed.

Before installing a fork:
- inspect `SKILL.md`,
- inspect every script,
- inspect external links and install commands,
- confirm no unexpected network or credential requirements were added.

## Project security constraints

The canonical Decision UI skill should not:
- request secrets,
- exfiltrate user data,
- require broad shell permissions,
- silently install packages,
- make network requests,
- instruct an agent to weaken repository security,
- embed private product or customer data.

Any future executable helper must be optional, self-contained, documented, and independently reviewable.
