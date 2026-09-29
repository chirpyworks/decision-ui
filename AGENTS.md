# AGENTS.md

Repository rules for AI coding agents working on Decision UI.

## Scope

Decision UI is a portable Agent Skill and evidence package, not a dashboard framework.

## Do

- preserve the decision-first hierarchy,
- keep the canonical skill at `skills/decision-ui/SKILL.md`,
- keep detailed material in focused references,
- load the accessibility reference when implementation or audit work requires it,
- distinguish diagnostic evidence from validated causality,
- add or update evals when behavioral rules change,
- preserve a zero-runtime-dependency core,
- use real or clearly labelled synthetic example data,
- never invent facts to make a demo more persuasive,
- keep compatibility claims tied to recorded smoke tests,
- run `python3 scripts/validate.py .`.

## Do not

- add private project rules or internal repository names,
- add credentials or telemetry,
- invent adoption numbers,
- invent benchmark results,
- add chart variety for decoration,
- turn team-specific taste into a universal core rule,
- silently change the license,
- delete evaluation coverage to make a change pass.

## Review order

1. decision correctness,
2. data and causal integrity,
3. visualization integrity,
4. state and interaction integrity,
5. accessibility,
6. compatibility,
7. visual craft.
