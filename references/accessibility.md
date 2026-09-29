# Accessibility Reference

Decision clarity fails when critical information or actions are inaccessible.

Use this reference for implementation and audit work.

## State and priority

Never encode critical state by color alone.

Combine color with at least one durable cue when meaning matters:
- text,
- icon with accessible label,
- ordering,
- pattern,
- shape,
- border treatment,
- explicit severity or status label.

Do not assume red/green distinctions are universally perceivable or culturally sufficient.

## Keyboard and focus

Interactive decision paths must be usable without a pointing device.

Check:
- logical tab order,
- visible focus,
- no keyboard traps,
- controls reachable in the same decision order as the visual hierarchy,
- dialogs return focus predictably,
- tables and dense controls do not hide essential actions behind hover-only behavior.

## Charts

A chart should not be the only place where critical meaning exists.

For important charts:
- provide a text summary of the main decision-relevant finding,
- expose units and comparison basis,
- distinguish missing data from zero,
- avoid color-only series identification,
- use direct labels when they reduce legend lookup,
- ensure annotations remain legible at zoom and high text scaling.

When exact values matter, provide an accessible table or equivalent data view.

## Tables

Use real table semantics for tabular data.

Preserve:
- meaningful column headers,
- row/column relationships,
- sortable-state announcements where implemented,
- clear selected/expanded states,
- understandable empty and loading states.

Do not recreate tables from visually aligned generic containers when semantic tables fit the task.

## Motion

Motion may explain state transition but must not carry unique meaning.

Respect reduced-motion preferences. Avoid:
- continuous decorative motion,
- large parallax movement,
- animation that delays urgent actions,
- flashing or rapid status changes.

## Text and density

Do not solve accessibility by making every expert interface sparse.

Instead:
- preserve readable type size,
- maintain sufficient contrast,
- use clear grouping,
- allow zoom/reflow,
- keep labels explicit,
- separate metadata from primary decision text.

Expert density and accessibility can coexist when hierarchy is strong.

## Responsive and zoom behavior

At narrow widths or high zoom:
- preserve the primary decision,
- preserve critical comparison context,
- keep actions reachable,
- prevent horizontal clipping of meaning,
- move dense evidence into focused views when needed.

## Accessibility review question

For every critical signal and action ask:

> Can a user perceive, understand, navigate and act on this without relying on one sensory cue or one input method?

If not, the interface is not ready.
