# Installation and Compatibility

Decision UI is a single Agent Skills-compatible skill. Its core behavior is Markdown-only and does not require an API key, runtime service, package install, or network access after installation.

## Recommended installer

The current `skills` CLI supports repository-based installation:

```bash
npx skills add chirpyworks/decision-ui
```

For a specific agent:

```bash
npx skills add chirpyworks/decision-ui -a claude-code
npx skills add chirpyworks/decision-ui -a codex
npx skills add chirpyworks/decision-ui -a cursor
npx skills add chirpyworks/decision-ui -a gemini-cli
npx skills add chirpyworks/decision-ui -a github-copilot
```

For a non-interactive global install:

```bash
npx skills add chirpyworks/decision-ui -g -a claude-code -y
```

The standalone repository now exists. Treat the install commands as pre-1.0 until the clean-install smoke test passes.

## Installer compatibility vs project verification

These are different claims.

| Agent | Installer currently recognizes target | Decision UI behavior smoke test |
|---|---:|---:|
| Claude Code | Yes | Pending |
| Codex | Yes | Pending |
| Cursor | Yes | Pending |
| Gemini CLI | Yes | Pending |
| GitHub Copilot | Yes | Pending |

“Installer recognizes target” means the current `skills` CLI exposes a target path for that agent. It does **not** mean Decision UI has completed behavioral QA on that agent.

## Manual installation

If your agent supports the Agent Skills directory convention, place this repository in the agent's skills directory so that the final directory name is exactly:

```
decision-ui/
  SKILL.md
  references/
  ...
```

The skill name in `SKILL.md` must match the containing directory name.

## Verify

Local repository validation:

```bash
python scripts/validate.py .
```

Official Agent Skills validation:

```bash
skills-ref validate /path/to/decision-ui
```

The official validation result is authoritative for specification conformance.

## Remove

When installed through the `skills` CLI, use its remove command for the target agent rather than deleting arbitrary shared directories manually.
