# Behavior Verification

Decision UI separates three claims:

1. **Format conformance** — the skill follows the Agent Skills format.
2. **Installer compatibility** — the skill can be installed into a client target.
3. **Behavior verification** — the client actually loads the skill and produces materially different decision reasoning.

Only the third claim requires real client evidence.

## Minimum evidence

A behavior-verification submission should record:

- client and exact version,
- model and version where applicable,
- operating system,
- Decision UI version or commit,
- installation method,
- exact activation prompt,
- evidence that the skill or referenced files loaded,
- raw or reproducible output,
- known limitations or ambiguities.

Do not submit screenshots alone when raw text/output can be preserved.

## Strong evidence

The strongest evidence is a paired run using the same:

- client,
- client version,
- model/version,
- prompt,
- tools,
- permissions,
- input data,
- fresh context.

Run once without Decision UI and once with Decision UI installed.

Preserve both raw outputs before scoring.

## Benchmark cases

Use the exact prompts under:

`evals/prompts/`

Score with D1–D11 from `BENCHMARK.md`.

Do not rewrite the prompt between baseline and Decision UI runs.

## Evidence strength

### Level A — Activation evidence

Shows the client loaded Decision UI or its references.

Useful for:
- confirming discovery/loading behavior,
- identifying compatibility failures.

Not sufficient for:
- output-quality claims.

### Level B — Single-run behavior evidence

Shows a client output that follows Decision UI behavior.

Useful for:
- confirming plausible activation,
- identifying missing/overreaching rules.

Not sufficient for:
- claiming the skill caused the difference.

### Level C — Paired benchmark evidence

Same environment, same prompt, baseline vs Decision UI, raw outputs preserved.

Useful for:
- regression testing,
- criterion-by-criterion comparison,
- limited client-specific behavior claims.

Still not sufficient for:
- universal superiority claims,
- user-outcome claims,
- decision-time improvement claims.

## Publication rule

Behavior evidence may be merged into `evals/results/` only when:

- raw outputs are preserved,
- metadata is complete,
- the prompt is reproducible,
- the Decision UI revision is pinned,
- scores are per criterion,
- ambiguities are recorded,
- no private/customer data is included.

Designed examples under `examples/` remain separate from measured evidence.

## Compatibility wording

Allowed after one valid Level C run:

> Decision UI behavior was verified in [client/version] for the recorded benchmark case(s).

Not allowed:

> Decision UI works identically across all clients.

Not allowed:

> Decision UI improves decision quality.

Those require broader evidence than this project currently collects.
