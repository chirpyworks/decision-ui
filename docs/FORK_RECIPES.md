# Fork Recipes

Decision UI is useful without a fork. Fork it when your team needs persistent rules that should travel with your projects.

The low-conflict rule is simple:

- keep the shared method close to upstream,
- put organization-specific choices in `skills/decision-ui/house-style.md`,
- put genuinely local domain material in local directories.

## Three-minute fork

1. Fork `chirpyworks/decision-ui`.
2. Edit `skills/decision-ui/house-style.md`.
3. Add only the rules your team repeatedly needs.
4. Run:

```bash
python3 scripts/validate.py .
```

5. Keep upstream as a remote so method improvements remain easy to pull.

Do not rewrite `SKILL.md` merely to change typography, density, components, colors, chart libraries or domain vocabulary.

## Recipe 01 — Product analytics team

Useful house-style additions:

- product typography and spacing density,
- preferred table and chart implementation libraries,
- semantic tokens for attention / critical / recovery / stale,
- standard comparison periods,
- cohort naming conventions,
- mobile rules for dense account tables,
- review gate requiring exact denominator and time-window labels.

Local additions might live in:

```
skills/decision-ui/references/domain/product-analytics.md
evals/local/
examples/local/
```

Keep company metrics, customer names and private thresholds out of a public fork.

## Recipe 02 — Operations team

Useful house-style additions:

- expert-density defaults,
- stale-data thresholds,
- event/state timeline conventions,
- escalation and ownership labels,
- operating-band and target conventions,
- permission-aware action patterns,
- rules for shift / day / week horizon changes.

Do not turn operational correlation into root-cause certainty. Keep diagnosis and validated cause distinct.

## Recipe 03 — Finance / risk team

Useful house-style additions:

- numeric precision rules,
- units and currency conventions,
- forecast / plan / actual hierarchy,
- uncertainty-range presentation,
- approval authority and irreversible-action warnings,
- exact-table requirements for audit-sensitive data,
- accessibility rules for loss/gain semantics beyond red/green.

Do not add a universal risk score unless the organization can defend its inputs, weighting and decision meaning.

## What belongs upstream?

A rule is a good upstream candidate when:

- the failure recurs across products or domains,
- the user consequence is clear,
- a counterexample can be stated,
- the behavior can be evaluated,
- it does not depend on one organization's private policy.

Open a rule proposal rather than embedding a broadly reusable improvement only in your fork.

## What should stay local?

Keep these local:

- brand typography,
- component-library preferences,
- internal vocabulary,
- private thresholds,
- approval rules,
- customer-specific logic,
- proprietary domain processes.

## Sync upstream

```bash
git remote add upstream https://github.com/chirpyworks/decision-ui.git
git fetch upstream
git merge upstream/main
```

If local changes stay concentrated in `house-style.md` and local directories, updates should stay manageable.

## Share your fork

If your public fork develops a useful house style, domain pack or evaluation set, submit it to the community showcase using the **Fork showcase** issue template.

A showcase entry is not an endorsement or quality certification. It is a discoverability surface for real adaptations of the method.
