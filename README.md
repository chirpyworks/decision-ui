# Decision UI

**Stop building dashboards. Build decision interfaces.**

Decision UI is a portable design skill for AI coding agents. It teaches Claude Code, Codex, Cursor, Copilot, Gemini CLI and compatible agents to turn data-heavy products into interfaces that help people decide what to do next.

Most generated dashboards start with the same ingredients: six KPI cards, a line chart, a donut, a table, and a filter bar. The result may look complete while still making the user do the actual thinking.

Decision UI changes the order.

```
Attention → Comparison → Cause → Impact → Action → Verification
```

A metric is evidence. A dashboard is not the decision.

## What changes

Without Decision UI, an agent tends to ask:

> What metrics and charts should this page contain?

With Decision UI, it must ask:

> Who is deciding what, within what time horizon, and what evidence changes that decision?

That produces different interfaces: fewer equal-weight cards, more explicit priority, better comparisons, diagnostic drill-downs, meaningful chart selection, visible uncertainty, and actions connected to outcomes.

## Project status

Decision UI is currently **pre-1.0**. The public contract is still being validated across agents. Breaking changes are possible until v1.0.0.

The skill follows the open Agent Skills `SKILL.md` format and is designed for progressive disclosure: the core method stays compact while detailed chart and anti-pattern guidance lives in `references/`.

## Install

After the standalone repository is published and the clean-install gate passes:

```bash
npx skills add chirpyworks/decision-ui
```

The current `skills` installer recognizes Claude Code, Codex, Cursor, Gemini CLI and GitHub Copilot targets. Decision UI's own behavioral smoke tests for those agents are tracked separately and must pass before v1.0.

See [INSTALL.md](INSTALL.md) for target-specific commands and the verification matrix.

Or fork the repository and customize `house-style.md` for your team.

The core skill is intentionally model-agnostic Markdown. No API key. No runtime service. No telemetry.

## Before / after field study

Open the [SaaS retention comparison](examples/saas-retention-before-after.html) locally in a browser. It uses the exact facts in the [benchmark prompt](evals/prompts/saas-retention.md) for both views. The example isolates information hierarchy; it is a designed demonstration, not a measured agent benchmark or evidence of faster decisions.

The metric-first view presents the same cohort and retention data as an overview. The decision-first view foregrounds the 15.3-point mid-market cohort gap, the $38–52k exposure range, the next investigation and a proposed verification plan. Neither view invents account-level causes or outcomes.

## Use it for

- SaaS and product analytics
- operations and manufacturing software
- finance and risk consoles
- internal tools and admin products
- BI and executive reporting
- observability and incident interfaces
- any UI where the user must decide, prioritize, diagnose or act

## Four operating modes

### BUILD
Create a new decision interface from a brief, dataset, schema or product requirement.

### AUDIT
Review an existing dashboard or UI. Return the highest-impact structural problems before visual polish.

### REFRAME
Keep the underlying data and business goal, but replace a metric-first information architecture with a decision-first one.

### CHART
Choose or critique a visualization from the question being answered, not from chart fashion.

## The core test

Before drawing the page, complete this sentence:

> **The user opens this view because they need to decide ______ before ______.**

If that sentence cannot be completed, do not design the dashboard yet.

## Default hierarchy

1. **Attention** — what requires action now?
2. **Comparison** — compared with what baseline, target, cohort or prior period?
3. **Cause** — what explains the change?
4. **Impact** — what happens if nothing changes?
5. **Action** — what can the user do next?
6. **Verification** — did the action improve the outcome?

Not every screen needs all six layers. Every layer that appears must earn its space.

## Anti-card-wall rule

Do not convert every metric, status or sentence into a card.

A card is justified when its boundary carries meaning: independent state, action, ownership, comparison or reusable interaction. Otherwise use layout, typography, spacing and alignment to create hierarchy.

## Chart rule

Choose charts by analytical question.

- Change over time → line / area / event timeline
- Compare categories → sorted bar / dot plot
- Target vs actual → bullet / variance bar
- Contribution to change → waterfall
- Rank causes → Pareto
- Distribution → histogram / box plot
- Relationship → scatter
- Flow → Sankey only when path magnitude matters
- Schedule → Gantt / interval timeline
- Process state → event or state timeline
- Exact lookup → table, not a chart

See `references/chart-selection.md`.

## Fork this for your team

The project is designed to be forked.

Edit only `house-style.md` to add your:
- density preference
- typography
- visual tone
- chart library
- component system
- domain-specific thresholds
- accessibility requirements
- review gates

Keep the core methodology upstream-compatible, then pull improvements without losing your house rules.

## What Decision UI is not

It is not a component library, chart library, analytics backend, design token package, or a substitute for domain knowledge.

It is a **decision architecture layer** for the agent building those things.

## Repository structure

```
SKILL.md
house-style.md
references/
  decision-flow.md
  chart-selection.md
  anti-patterns.md
  accessibility.md
evals/
  cases.md
  manifest.json
  prompts/
examples/
site/
  index.html
scripts/
  validate.py
INSTALL.md
BENCHMARK.md
CONTRIBUTING.md
SECURITY.md
SUPPORT.md
CODE_OF_CONDUCT.md
LICENSE
```

## Validation

Run the lightweight repository check:

```bash
python scripts/validate.py .
```

Before a stable release, the package must also pass the official `skills-ref validate` check and install smoke tests on the supported agent matrix.

Behavior changes should be evaluated with [BENCHMARK.md](BENCHMARK.md), with raw prompts and outputs preserved.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) before changing the core method. Community expectations are in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), support expectations are in [SUPPORT.md](SUPPORT.md), and security-sensitive reports should follow [SECURITY.md](SECURITY.md).

The project intentionally requires no credentials, telemetry, network access, or executable runtime for its core behavior.

## License

MIT. Fork it, adapt it, ship it.
