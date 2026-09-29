# Forking Decision UI

Decision UI is intentionally structured so a team can fork it without owning a permanent merge-conflict problem.

## The boundary

Treat these as **upstream method**:
- `skills/decision-ui/SKILL.md`
- `skills/decision-ui/references/`
- shared evals and validator

Treat this as **your local layer**:
- `skills/decision-ui/house-style.md`

You may also add local files such as:
```
skills/decision-ui/references/domain/
evals/local/
examples/local/
```

## What belongs in house style

Good local rules:
- typography and density,
- component library,
- chart implementation stack,
- semantic color tokens,
- stricter accessibility minimums,
- domain vocabulary,
- organization-specific thresholds,
- approval/permission conventions,
- review gates.

Bad local rules:
- credentials,
- private customer data,
- secrets,
- rules that contradict truthful visualization or accessibility,
- instructions to bypass permissions or hide uncertainty.

## Syncing upstream

```bash
git remote add upstream https://github.com/chirpyworks/decision-ui.git
git fetch upstream
```

If local changes stay concentrated in `house-style.md` and local directories, upstream improvements should produce fewer conflicts.

## Contributing back

If a local rule proves broadly useful, open a rule proposal with:
- the recurring failure mode,
- user consequence,
- counterexample,
- evaluation case.

## Practical recipes

See [FORK_RECIPES.md](FORK_RECIPES.md) for product analytics, operations, and finance/risk customization examples.

If your fork is public and meaningfully adapts the method, submit it through the **Fork showcase** issue template for possible listing in the community showcase.
