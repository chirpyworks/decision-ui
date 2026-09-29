# Contributing to Decision UI

Thank you for improving Decision UI.

Decision UI is a decision-architecture skill, not a general-purpose UI style guide. Contributions should make agents better at prioritization, comparison, diagnosis, action, verification, state handling, or truthful data visualization.

## Before opening a change

For a rule change, answer:

1. What failure mode does this prevent?
2. What user decision becomes easier?
3. Is the rule broadly reusable, or should it live in `skills/decision-ui/house-style.md`?
4. Can the behavior be evaluated with a concrete prompt?
5. Does the change increase context cost without enough benefit?

## Contribution types

### Core method

Changes to `skills/decision-ui/SKILL.md` require:
- a clearly described failure mode,
- at least one new or updated eval,
- no dependency on a specific design system,
- no product-specific proprietary logic.

### Reference material

Changes under `skills/decision-ui/references/` should remain focused and directly loadable from the core skill.

### Evaluation cases

Good evals expose a meaningful failure boundary. Prefer prompts where a generic dashboard pattern would produce the wrong product behavior.

### House-style examples

Team-specific preferences belong in `skills/decision-ui/house-style.md` or examples, not in the core method.

### Client behavior verification

Installer compatibility and behavior verification are tracked separately. If you test Decision UI in Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, or another Agent Skills client, use the behavior-verification issue template and include reproducible evidence.

Paired benchmark contributions should preserve the raw baseline and Decision UI outputs under `evals/results/` using the format in `evals/results/README.md`.

## Pull request checklist

- [ ] I can state the decision problem this change improves.
- [ ] I updated or added eval coverage when behavior changed.
- [ ] I did not add secrets, customer data, proprietary prompts, or private project material.
- [ ] Local links resolve.
- [ ] `skills/decision-ui/SKILL.md` remains under 500 lines.
- [ ] Frontmatter follows the Agent Skills specification.
- [ ] The change does not force a particular visual aesthetic when decision clarity is the real requirement.
- [ ] Examples distinguish fact, assumption, and synthetic data.

## Quality standard

Do not optimize for more rules. Optimize for fewer rules that reliably change agent behavior.

A contribution may be rejected even if it is visually appealing when it:
- creates decorative complexity,
- duplicates an existing rule,
- overfits one product,
- weakens analytical truthfulness,
- adds unsupported causal claims,
- or makes the skill harder to activate correctly.

## Development

The core skill has no runtime dependency.

For structural validation, use the official Agent Skills reference validator when available:

```bash
skills-ref validate skills/decision-ui
```

The repository also includes a lightweight local validator:

```bash
python3 scripts/validate.py .
```

## Conduct

Be specific, evidence-oriented, and respectful. Critique the contribution, not the contributor.

## Community forks

If your adaptation is organization-specific, keep it in a fork rather than pushing local preferences into the shared core.

Use [docs/FORK_RECIPES.md](docs/FORK_RECIPES.md) for practical examples. Meaningful public adaptations can be submitted through the **Fork showcase** issue template and may be listed in [SHOWCASE.md](SHOWCASE.md).

A showcase listing is not an endorsement or quality certification.
