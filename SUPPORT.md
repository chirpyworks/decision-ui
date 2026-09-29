# Support

Decision UI is an open-source methodology and agent skill. Support is community-based.

## Use an issue when

- a prompt reliably produces behavior that contradicts the skill,
- an install or validation step is broken,
- a reference contains an analytical error,
- an example teaches a misleading comparison,
- an agent compatibility regression can be reproduced.

Include:
- the smallest reproducible prompt,
- agent and model environment,
- Decision UI version or commit,
- observed result,
- expected decision behavior.

Do not include secrets, customer data, proprietary prompts, or internal company information.

## Use a rule proposal when

You have a reusable failure mode that should change the core method or references. A proposal should include a test prompt, not only a preference.

## Security

Do not use a public issue for a security-sensitive report. Follow `SECURITY.md`.

## What is not guaranteed

Decision UI cannot guarantee:
- factual correctness of source data,
- domain expertise the agent was not given,
- causal conclusions unsupported by evidence,
- accessibility compliance without implementation review,
- identical behavior across models and agent versions.

The skill is intended to improve decision architecture, not replace product, domain, engineering, analytics, or accessibility review.
