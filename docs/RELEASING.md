# Releasing Decision UI

Decision UI uses semantic versioning with release candidates before the stable contract.

## Source of truth

The version must agree in:
- `skills/decision-ui/SKILL.md` → `metadata.version`
- `package.json` → `version`
- `evals/manifest.json` → `skill_version`
- `CHANGELOG.md`

The repository validator rejects version drift across these files.

## Release candidate gate

Before an RC is tagged:

1. `python3 scripts/validate.py .` passes.
2. Agent Skills reference validation passes in CI.
3. Candidate installation passes for the five supported installer targets.
4. Public-default-branch installation passes after merge.
5. Static Pages routes pass the local HTTP smoke test.
6. GitHub Pages deploy succeeds.
7. No internal project identifiers, credentials, or unsupported evidence claims are present.
8. Designed demonstrations remain labelled as demonstrations.
9. Measured behavior claims link to raw paired results under `evals/results/`.

## Stable v1.0 gate

v1.0 additionally requires:
- at least one recorded client-level behavior verification,
- at least one published paired benchmark run,
- no open P0/P1 correctness issue,
- current compatibility table,
- reviewed release notes.

A stable release must not be used to imply identical behavior across clients.

## Release notes structure

Use:

### What changed
Rules or product surface changes.

### Evidence
Validation, installer, behavior, and benchmark evidence. Keep them distinct.

### Compatibility
Any client/path/version change.

### Known limitations
What is still unverified or intentionally out of scope.

## Tagging

Tag format:
- prerelease: `v0.1.0-rc.N`
- stable: `v1.0.0`

Create the GitHub release from the exact validated main commit. Do not tag an unmerged feature branch.
