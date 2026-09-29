# Accessibility Reference

Decision clarity fails when critical information or actions are inaccessible.

## State and priority

Never encode critical state by color alone.

Combine color with a durable cue when meaning matters:
- text,
- an icon with an accessible label,
- ordering,
- pattern or shape,
- explicit severity or status text.

## Keyboard and focus

Critical decision paths must be usable without a pointing device.

Check:
- logical tab order,
- visible focus,
- no keyboard traps,
- controls reachable in the same decision order as the visual hierarchy,
- dialogs return focus predictably,
- essential information is not hover-only.

## Charts

A chart must not be the only place where decision-critical meaning exists.

For important charts:
- provide a concise text summary of the main finding,
- expose units and comparison basis,
- distinguish missing data from zero,
- avoid color-only series identification,
- use direct labels when they reduce legend lookup,
- keep annotations legible at zoom and high text scaling.

When exact values matter, provide an accessible table or equivalent data view.

## Tables

Use real table semantics for tabular data.

Preserve:
- meaningful headers,
- row and column relationships,
- clear selected or expanded states,
- understandable loading and empty states.

Do not recreate a table from generic containers when a semantic table fits the task.

## Motion

Motion may explain state transition but must not carry unique meaning.

Respect reduced-motion preferences. Avoid:
- continuous decorative motion,
- large parallax movement,
- animation that delays urgent actions,
- flashing or rapid status changes.

## Text and density

Accessibility does not require making expert interfaces artificially sparse.

Prefer:
- readable type,
- sufficient contrast,
- clear grouping,
- zoom and reflow support,
- explicit labels,
- separation between metadata and primary decision text.

## Responsive and zoom behavior

At narrow widths or high zoom:
- preserve the primary decision,
- preserve critical comparison context,
- keep actions reachable,
- prevent horizontal clipping of meaning,
- move dense evidence into focused views when necessary.

## Review question

For every critical signal and action ask:

> Can a user perceive, understand, navigate and act on this without relying on one sensory cue or one input method?

If not, the interface is not ready.
