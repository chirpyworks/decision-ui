# Decision Flow Reference

Use this reference when the page contains monitoring, analytics, operational or management information.

## Attention

Question: **What requires attention now?**

Useful evidence:
- threshold breach,
- change vs baseline,
- abnormal pattern,
- missed commitment,
- deteriorating forecast,
- unresolved exception,
- stale or missing data that blocks confidence.

Do not promote everything unusual. Prioritize by consequence and time sensitivity.

## Comparison

Question: **Compared with what?**

Choose the comparison that changes interpretation:
- target,
- prior period,
- peer/cohort,
- plan,
- SLA,
- capacity,
- expected range,
- forecast,
- control limit.

A number without a meaningful comparison is often decoration.

## Cause

Question: **Why is this happening?**

Support progressive diagnosis:
- segment,
- event,
- component,
- stage,
- cohort,
- location,
- product,
- owner,
- input.

Prefer causal navigation over a generic “view details” dead end.

Do not turn sequence or correlation into causal certainty. Distinguish:
- observed association,
- diagnostic evidence,
- working hypothesis,
- validated cause.

When the evidence is incomplete, the interface should help compare explanations rather than manufacture one.

## Impact

Question: **What is exposed if this continues?**

Translate technical or operational deviation into consequence:
- revenue,
- delivery,
- customer,
- safety,
- compliance,
- throughput,
- inventory,
- capacity,
- cost,
- churn,
- reliability.

Do not manufacture monetary impact when the data cannot support it.

## Action

Question: **What can the actor do now?**

Action must match authority and reversibility.

Examples:
- assign,
- acknowledge,
- pause,
- reroute,
- approve,
- reject,
- investigate,
- schedule,
- contact,
- change plan,
- compare scenarios.

When action is outside the product, show the handoff path and owner.

## Verification

Question: **Did the action work?**

Whenever possible, connect intervention to:
- recovery trend,
- residual risk,
- time to recovery,
- new exception,
- target restoration,
- before/after evidence.

A decision interface is incomplete if it recommends action but cannot later show what happened.
