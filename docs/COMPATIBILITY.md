# Compatibility

Decision UI separates **format conformance**, **installation compatibility**, and **behavioral client validation**.

## Format

Canonical skill:

`skills/decision-ui/SKILL.md`

The package passes the pinned Agent Skills reference validator used by project CI.

## Verified installation record

Verified on 2026-09-29 in GitHub Actions using:
- Ubuntu 24.04 runner
- Node.js 22.20.0
- `skills` CLI 1.7.0
- source: `chirpyworks/decision-ui`

| Client target | Installer status | Installed path | Behavior / activation status |
| --- | --- | --- | --- |
| Claude Code | Verified | `.claude/skills/decision-ui/SKILL.md` | Pending client-level behavior test |
| Codex | Verified | `.agents/skills/decision-ui/SKILL.md` | Pending client-level behavior test |
| Cursor | Verified | `.agents/skills/decision-ui/SKILL.md` | Pending client-level behavior test |
| Gemini CLI | Verified | `.agents/skills/decision-ui/SKILL.md` | Pending client-level behavior test |
| GitHub Copilot | Verified | `.agents/skills/decision-ui/SKILL.md` | Pending client-level behavior test |

The verified command form is:

```bash
npx skills@1.7.0 add chirpyworks/decision-ui --skill decision-ui -a <agent> -y
```

Installer success means the skill was resolved from the real public repository and written to the expected target path. It does **not** prove identical activation or output quality across clients.

## Behavioral verification record

Before marking a client behavior-verified, record:
- client name and version,
- model where relevant,
- OS,
- installation method,
- activation prompt,
- whether referenced files loaded,
- observed limitations,
- raw or reproducible evaluation evidence.

Marketing copy must not outrun this table.

## Behavior evidence protocol

See [BEHAVIOR_VERIFICATION.md](BEHAVIOR_VERIFICATION.md) for evidence levels, paired-run requirements, and publication wording.
