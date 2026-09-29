# Decision UI Benchmark Protocol

The benchmark measures whether Decision UI changes agent behavior in ways that reduce decision effort. It is not a visual beauty score.

## Comparison design

For each case:

1. Use the same agent/model version.
2. Use the same product brief and data.
3. Run once without Decision UI.
4. Run once with Decision UI installed.
5. Preserve raw prompts and raw outputs.
6. Do not manually edit either result before scoring.
7. Record date, agent, model, tool environment and skill version.

## Binary criteria

Score each criterion 0 or 1.

### D1 — Decision contract

Pass when the output identifies or explicitly resolves:
- actor,
- decision,
- time horizon or consequence.

### D2 — Priority

Pass when the screen establishes a clear primary attention target instead of equal-weight information.

### D3 — Comparison

Pass when the primary metric or signal has a meaningful comparison basis: target, baseline, prior period, cohort, plan, forecast or expected range.

### D4 — Diagnostic path

Pass when the interface provides a route from signal to explanatory evidence.

Not every case requires causal certainty. A diagnostic path may present competing hypotheses or segmented evidence.

### D5 — Action path

Pass when a detected problem connects to an action, handoff or explicit statement that no action is available.

### D6 — Verification

Pass when an intervention can be checked against a later state or outcome where the product context supports it.

### D7 — Visualization fit

Pass when chart/table choice matches the analytical question and avoids avoidable perceptual distortion.

### D8 — State integrity

Pass when relevant stale, missing, empty, error, permission or partial-data states are considered.

### D9 — Responsive reconstruction

Only score cases that request responsive/mobile behavior. Pass when the mobile information order is reconstructed rather than merely stacked.

### D10 — Restraint

Pass when irrelevant KPIs, decorative charts and redundant cards are removed or deliberately excluded.

### D11 — Accessibility integrity

Pass when decision-critical state and action do not depend on color alone, hover alone, or a pointing device. Where implementation detail is part of the output, semantic structure, keyboard/focus behavior, and an accessible equivalent for critical chart meaning should be considered.

## Result record

Store published runs under `evals/results/`. A result should include:
- case id,
- date,
- client and client version,
- model and model version where available,
- Decision UI version or commit,
- exact prompt path,
- baseline raw output,
- Decision UI raw output,
- D1–D11 scores,
- scorer notes and ambiguities.

See `evals/results/README.md` for the publication format.

## Reporting

Do not collapse the benchmark to one universal quality number without the raw criteria.

Report:
- per-case criterion matrix,
- pass count by criterion,
- raw output links,
- known ambiguities,
- model/version/date.

Do not claim causal superiority from a tiny sample. The benchmark is a regression and behavior-comparison tool.

## Core benchmark cases

- SaaS retention
- manufacturing operations
- SRE incident response
- executive revenue / forecast

Additional cases should test boundaries, not merely repeat the same structure.
