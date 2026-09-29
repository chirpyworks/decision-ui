# Example — SaaS Retention

Interactive visual comparison: [before / after](saas-retention-before-after.html). This is a designed illustration using the supplied facts, not a raw agent-with/without-skill benchmark result.

## Brief

A B2B SaaS product team needs a weekly retention view. Data:
- net retention: 96.8%, down 2.4 points
- churn: 4.9%, up 1.1 points
- mid-market incomplete-setup cohort retention: 79.4%
- mid-market activated cohort retention: 94.7%
- enterprise retention: 97.9%
- 146 mid-market accounts have incomplete setup
- estimated MRR exposed at next renewal: $38k–$52k

## Weak framing

A generic dashboard may start with equal KPI cards for MRR, retention, churn, active users, NPS and expansion, then add charts by category.

The screen reports the business but does not foreground the weekly decision.

## Decision framing

**Decision contract**

> The product team opens this view to decide which retention intervention to prioritize this week before the affected mid-market accounts reach renewal.

**Primary hierarchy**

1. Attention — retention decline is concentrated in incomplete-setup mid-market accounts.
2. Comparison — 79.4% vs 94.7% activated peers.
3. Diagnostic evidence — incomplete-setup accounts retain 15.3 points below activated mid-market peers; the supplied data does not prove causality.
4. Impact — $38k–$52k MRR exposed, presented as a range.
5. Action — review the 146 incomplete-setup accounts and choose an intervention appropriate to product-team authority.
6. Verification — define an appropriate observation window from product context, then track setup completion and subsequent retention.

## Deliberately removed

- duplicate summary cards that repeat the same cohort facts.
- decorative donut charts.
- equal-weight KPI tiles.
- any metric not present in the supplied data.

## Visualization choice

Use a comparison table or dot/bar comparison for cohort retention. Use a trend only if time movement is part of the decision. Do not add chart variety merely to fill space.
