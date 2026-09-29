# Benchmark Results

This directory is for published **raw paired runs**, not curated showcase examples.

A benchmark result is eligible for publication only when the baseline and Decision UI runs use:
- the same client and client version,
- the same model/version where applicable,
- the same benchmark prompt,
- fresh context for each run,
- the same available tools and permissions,
- no manual editing before scoring.

## Directory convention

```
evals/results/
  <date>-<client>-<model>/
    metadata.json
    <case-id>/
      baseline.md
      decision-ui.md
      score.json
```

## metadata.json

Record at minimum:

```json
{
  "date": "YYYY-MM-DD",
  "client": "example-client",
  "client_version": "x.y.z",
  "model": "model-name",
  "model_version": "version-or-null",
  "decision_ui_version": "0.1.0-rc.2",
  "decision_ui_commit": "<sha>",
  "environment": "OS / relevant tool context",
  "notes": ""
}
```

## score.json

Use the D1–D11 criteria defined in `BENCHMARK.md`.

```json
{
  "case_id": "saas-retention",
  "scores": {
    "D1": 0,
    "D2": 0,
    "D3": 0,
    "D4": 0,
    "D5": 0,
    "D6": 0,
    "D7": 0,
    "D8": 0,
    "D9": 0,
    "D10": 0,
    "D11": 0
  },
  "scorer_notes": "",
  "ambiguities": []
}
```

Do not publish a total score without the per-criterion matrix and raw outputs.

Designed examples under `examples/` are not benchmark results.
