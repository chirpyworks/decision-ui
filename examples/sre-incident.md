# Example — SRE Incident Response

## Brief

An SRE team has:
- 5 active alerts
- elevated API latency
- 2.8% error rate
- one deployment 18 minutes before the error increase
- one telemetry source has been stale for 11 minutes
- 42% of affected requests originate from one region

## Weak framing

Alert count, latency, error rate, CPU, memory and request volume appear as equal tiles with red/green status.

## Decision framing

**Decision contract**

> The incident commander opens this view to decide whether to rollback, isolate or continue diagnosis before user impact expands.

**Primary hierarchy**

1. Attention — current user-impacting incident.
2. Comparison — latency/error vs SLO and pre-deployment baseline.
3. Diagnostic path — deployment event, regional concentration and competing evidence.
4. Trust state — stale telemetry is visible next to any inference it weakens.
5. Action — rollback, assign investigation, isolate region, or hold based on evidence and authority.
6. Verification — error/latency recovery and residual regional impact.

## Deliberately removed

- infrastructure metrics unrelated to the current hypothesis.
- alert-count hero card.
- color-only severity encoding.

## Visualization choice

Use event timeline + service/error trend aligned in time. Use tables for active incidents and ownership. Avoid a network graph unless topology itself changes the decision.
