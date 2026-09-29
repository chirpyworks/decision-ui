# House Style

This file is the intentional fork surface.

Keep `SKILL.md` close to upstream. Put team-specific choices here so your fork can pull methodology updates without repeatedly resolving the core skill.

## Visual character

- Tone: restrained, precise, product-native
- Density: medium-high for expert tools; reduce only when comprehension improves
- Radius: use selectively; do not round every container
- Depth: prefer hierarchy and surface contrast before shadow
- Motion: explain state change; never animate merely to make the page feel alive

## Typography

Define your product fonts and type scale here.

Default principle:
- display size for one primary decision or state,
- compact labels for metadata,
- tabular numerals for comparable metrics,
- avoid oversized KPI typography when magnitude is not the primary message.

## Color

Define semantic roles, not a rainbow palette.

Recommended roles:
- neutral structure,
- selected / active,
- attention,
- critical,
- positive recovery,
- uncertainty / stale,
- comparison baseline.

Never rely on hue alone for critical state.

## Data visualization

Preferred chart library: project choice.

House constraints:
- direct labels when practical,
- visible units,
- comparable scales,
- restrained gridlines,
- explicit target/baseline,
- no 3D charts,
- no donut/pie when precise comparison matters,
- no gauge unless a threshold or operating band is the actual question.

## Components

List the design system or component library used by your team.

Do not let the component library determine the information architecture.

## Domain rules

Add domain-specific thresholds, terms, permissions, or compliance constraints here.

Examples:
- stale after N minutes,
- critical threshold source,
- approval authority,
- required audit information,
- default comparison period.

## Review gate

Before merging a data-heavy page, verify:
- the primary decision is obvious,
- the baseline is visible,
- priority is not encoded only by color,
- every chart has a question,
- every alert has a next action or a clear reason it does not,
- empty/error/stale states are designed,
- mobile preserves the decision rather than the desktop geometry.
