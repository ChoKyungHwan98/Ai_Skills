# Minimal accessibility checks

Use this reference only when a redesign affects meaning, labels, states, interactive visuals, reading order, narrow layouts, or chart access. This is a focused check against regressions in the changed screen, not a full accessibility audit.

- **Meaning beyond color:** Can the viewer distinguish status, category, and emphasis without relying on hue alone?
- **Labels and states:** Are controls, selected items, loading or error states, and their consequences understandable in context?
- **Interactive visuals:** If a chart or canvas can be focused or selected, is that state visible and usable through the relevant input methods?
- **Reading order:** Does the visual sequence remain sensible when navigated in reading or focus order?
- **Narrow layout:** When panels stack or charts simplify, are the first-glance target, its context, and the next action still clear?
- **Chart alternative:** When exact values or the pattern matter beyond the visual rendering, is a useful text summary or table available?

Check only the items affected by the change. A screenshot cannot prove keyboard or assistive-technology behavior; inspect the live interaction or code when those behaviors matter, and mark anything unverified.
