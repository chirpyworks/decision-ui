# Example — Manufacturing Operations

## Brief

A plant manager sees:
- OEE: 71%
- output: 8.4% below plan
- downtime: 94 minutes
- scrap: 3.1%
- one filler repeatedly stops for 20–45 seconds
- micro-stops account for 58% of lost output in the current shift

## Weak framing

Four large KPI cards for OEE, output, downtime and scrap, followed by unrelated trend charts.

This makes the manager translate symptoms into action manually.

## Decision framing

**Decision contract**

> The plant manager opens this view to decide which loss to attack during the current shift before the production gap becomes unrecoverable.

**Primary hierarchy**

1. Attention — filler micro-stops are the dominant recoverable loss.
2. Comparison — output vs shift plan and expected remaining capacity.
3. Cause evidence — stop frequency, duration distribution and affected state/event sequence.
4. Impact — units at risk by shift end, not OEE alone.
5. Action — inspect/adjust the filler, assign maintenance, or change operating plan based on authority.
6. Verification — compare stop rate and recovered output after intervention.

## Deliberately removed

- OEE as the hero number.
- unrelated energy or inventory metrics.
- a gauge for each percentage.
- plant-layout decoration without decision value.

## Visualization choice

Use an event/state timeline for repeated short stops, Pareto for ranked loss contribution, and plan-vs-actual production trajectory for recoverability.
