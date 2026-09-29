# Anti-Patterns

## 1. KPI Card Wall

Symptoms:
- 4–12 equal cards at the top,
- large numbers with small deltas,
- no obvious priority,
- every metric treated as equally actionable.

Fix:
- identify the decision-driving signal,
- group supporting metrics as evidence,
- promote only what changes action.

## 2. Chart Buffet

Symptoms:
- bar, line, donut, area and gauge appear together mainly for visual variety.

Fix:
- write the question above each chart during design,
- remove charts that answer no distinct question,
- reuse the same visual form when the comparison is the same.

## 3. Dashboard Taxidermy

Symptoms:
- many observations,
- no interaction that helps diagnose,
- no action,
- no state transition,
- screenshot looks “complete” but the workflow is dead.

Fix:
- connect signal → evidence → action → verification.

## 4. Red Means Important

Symptoms:
- priority is encoded only by saturated red,
- everything eventually becomes red,
- no explanation of consequence or urgency.

Fix:
- combine severity with text, ordering, iconography, magnitude, deadline or owner where relevant.

## 5. Decorative Gauge

Symptoms:
- semicircle gauge for a percentage,
- arbitrary green/yellow/red bands,
- target is not operationally meaningful.

Fix:
- use bullet/variance bar if target comparison matters,
- use text + trend if the exact value and change matter.

## 6. Comparison Amnesia

Symptoms:
- “42%” is shown with no baseline, target, prior period, cohort or expected range.

Fix:
- select the comparison that changes interpretation.

## 7. Filter Furniture

Symptoms:
- date, team, region, status and segment filters appear because dashboards conventionally have filters.

Fix:
- keep filters that correspond to real analytical questions,
- prefer contextual drill-down for diagnosis.

## 8. Scroll Graveyard

Symptoms:
- important content is appended vertically,
- later sections repeat earlier summaries,
- no progressive disclosure or navigation logic.

Fix:
- establish hierarchy,
- collapse secondary evidence,
- split views by distinct decision when necessary.

## 9. Card-for-Everything

Symptoms:
- every sentence, chart, metric and control is inside a rounded rectangle.

Fix:
- use cards only when the boundary carries semantic or interaction meaning.

## 10. Mobile Shrink Ray

Symptoms:
- desktop grid squeezed into one narrow column,
- primary action appears after several screens of secondary metrics.

Fix:
- reconstruct the sequence around the mobile decision,
- preserve priority and action before supporting evidence.

## 11. False Precision

Symptoms:
- many decimals,
- precise risk scores with weak evidence,
- unexplained algorithmic confidence.

Fix:
- match precision to evidence and decision sensitivity,
- expose uncertainty when it matters.

## 12. Status Without Trust

Symptoms:
- live-looking data with no freshness,
- stale sensor/API values indistinguishable from current data.

Fix:
- surface freshness, missingness and partial-data state wherever trust can change action.
