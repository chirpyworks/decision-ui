# Evaluation Cases

Use these prompts to evaluate whether an agent follows Decision UI rather than producing a generic dashboard.

## Case 01 — SaaS retention

Prompt: Design a dashboard for a SaaS product team tracking retention.

Pass if:
- actor and decision are established,
- retention risk is prioritized before a metric grid,
- cohorts/segments are used for diagnosis,
- churn/retention comparisons are explicit,
- actions connect to affected cohorts.

Fail if:
- MRR/ARR/DAU cards are added without relevance,
- donut charts appear for decoration.

## Case 02 — Factory operations

Prompt: Build a plant dashboard with OEE, downtime, scrap and output.

Pass if:
- current attention/risk is primary,
- OEE is evidence, not the whole decision,
- downtime cause and production impact are connected,
- operator/manager actions are visible.

## Case 03 — Executive revenue

Prompt: Create an executive revenue dashboard.

Pass if:
- time horizon and decision are established,
- plan/forecast/actual comparison is primary,
- revenue variance is decomposed,
- secondary metrics do not compete equally.

## Case 04 — Incident monitoring

Prompt: Design an incident dashboard for an SRE team.

Pass if:
- unresolved, high-consequence incidents dominate,
- timeline/state and blast radius are visible,
- ownership and next action are clear,
- stale telemetry is distinct.

## Case 05 — Existing card wall audit

Prompt: Audit a dashboard with 12 KPI cards and 8 charts.

Pass if:
- critique starts with decision/hierarchy problems,
- findings are prioritized,
- the answer does not begin with color or corner radius.

## Case 06 — Mobile reconstruction

Prompt: Make this analytics dashboard mobile responsive.

Pass if:
- the sequence is recomposed,
- primary decision/action remains early,
- dense evidence is collapsed or moved.

Fail if:
- agent only stacks all desktop modules vertically.

## Case 07 — Gauge request

Prompt: Show SLA performance as a gauge.

Pass if:
- agent checks whether bands/thresholds change action,
- proposes a better form if the gauge adds no value.

## Case 08 — Exact lookup

Prompt: Show 200 customer accounts with plan, ARR, health, owner and renewal date.

Pass if:
- table is accepted as primary representation,
- prioritization/sorting supports decisions,
- charts are not added just to make the page feel visual.

## Case 09 — Forecast uncertainty

Prompt: Show next-quarter demand forecast.

Pass if:
- forecast uncertainty/range is considered when material,
- plan/capacity comparison is explicit.

## Case 10 — Empty state

Prompt: There are no active risks.

Pass if:
- the state communicates “no action required,”
- it does not fabricate alerts or fill space with unrelated KPIs.

## Case 11 — Permissions

Prompt: A viewer can see risk but cannot approve the recommended action.

Pass if:
- unavailable action is explained,
- escalation/handoff path is shown,
- UI does not present a misleading active control.

## Case 12 — Data freshness

Prompt: Some upstream data stopped 47 minutes ago.

Pass if:
- stale data is not silently mixed with current values,
- trust impact is visible near affected decisions,
- verification is blocked or qualified where necessary.

## Case 13 — Accessibility

Prompt: The dashboard uses red and green status dots, hover tooltips and clickable chart marks for all investigation paths.

Pass if:
- status receives a non-color cue,
- essential information is not hover-only,
- keyboard/focus behavior is considered,
- critical chart meaning has a text/table equivalent where appropriate.

## Case 14 — Causal uncertainty

Prompt: Conversion dropped after a new release. Design a view explaining why.

Pass if:
- temporal association is not presented as proven causation,
- competing explanations can remain visible,
- evidence strength or uncertainty is represented when material,
- the diagnostic path supports verification.

Fail if:
- the release is labeled the cause solely because it occurred first.
