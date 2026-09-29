# Chart Selection by Question

Select the visualization after writing the analytical question in plain language.

| Question | Default | Use when | Avoid |
|---|---|---|---|
| How did it change over time? | Line | continuous or ordered time | bars for dense long series |
| Which category is larger? | Sorted bar / dot | categorical comparison | pie/donut for precise ranking |
| Are we above or below target? | Bullet / variance bar | target is meaningful | gauge with arbitrary zones |
| What caused the change? | Waterfall | additive contributions | stacked bars when net change is the question |
| Which causes dominate? | Pareto | ranked causes + cumulative contribution | unsorted bars |
| How is it distributed? | Histogram / box | spread, skew, outliers | averages alone |
| Are two variables related? | Scatter | correlation / clusters | dual-axis chart unless unavoidable |
| How does composition change over time? | Stacked area / 100% stacked | composition is the question | too many categories |
| How does flow move between stages? | Sankey | path magnitude matters | Sankey for simple process order |
| What happened and when? | Event/state timeline | incidents, machine states, status changes | line chart for categorical state |
| When is work scheduled? | Gantt / interval timeline | start/end, overlap, dependency | calendar heatmap for precise scheduling |
| Where is the issue? | Map | geography changes the decision | maps for non-spatial data |
| What is the exact value? | Table | lookup, many dimensions, audit | chart merely to avoid a table |
| Which option is better across criteria? | Comparison table / matrix | trade-offs | radar chart by default |

## Scale rules

- Use zero baseline for bars unless there is a defensible analytical reason not to.
- Do not truncate scales to exaggerate weak movement.
- Keep comparable small multiples on comparable scales.
- State units and denominators.
- Show missing data distinctly from zero.
- Prefer direct labels when they reduce legend lookup.
- If uncertainty changes the decision, visualize it.

## Color rules

Use color for:
- status,
- selection,
- threshold breach,
- category identity when necessary,
- emphasis.

Do not use color simply because multiple series exist. Start with neutral context, then emphasize the comparison that matters.

## Annotation

Annotate events only when they help explain the change. Avoid turning the chart into a scrapbook of labels.

A good annotation answers “why here?” or “what changed?”
