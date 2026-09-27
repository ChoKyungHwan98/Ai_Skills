# Dashboard and tool patterns

Use these patterns to propose structure after the task or decision and first-glance target are clear. They are starting arrangements, not templates to impose on every screen.

## Reason about grouping

Start with context already available in the product, screen, data, and user request. Group and order information by the user's task and language rather than by implementation boundaries. Consider frequency of use, expertise, time pressure, and existing product constraints only where they change the grouping, density, or reading order. Explain the reason for a proposed group. Ask for missing context only when different answers would lead to meaningfully different structures; do not turn these factors into a fixed interview.

## Conclusion → evidence → explanation → details

When a screen supports one main decision, lead with the conclusion, then the comparison or observation that proves it. Explain the cause or implication next; leave exact records, definitions, and exceptions in details. If the evidence is uncertain, say so in the conclusion rather than burying the caveat below.

## Overview → drill-down

Use an overview to locate the issue, opportunity, or item worth inspecting. Keep the scope and selection visible as the viewer drills into a chart, category, or record. The detail view should answer a sharper question without forcing the viewer to reconstruct the overview context.

## Decision dashboard

Lead with a conclusion or current state, then its strongest comparison. Place the action near the conclusion. Put detailed breakdowns and raw records below. Use when the viewer must decide what to do now, such as which build to pursue or which metric needs attention. A grid of equal KPI cards usually weakens this pattern because it avoids choosing a lead.

## Comparison workspace

Keep candidates in a shared visual frame with aligned metrics, stable ordering, and visible selection criteria. Show the tradeoff that changes the decision, not every attribute at equal weight. Provide exact values in a table or details panel when needed. Useful for game loadouts, planning scenarios, investment options, or model outputs.

## Prioritization view

Show what should be addressed first and why. Rank by a stated measure or combine impact and effort only when both are defined. Put blockers, dependencies, and uncertainty close to the ranked items. Make the next action visible without giving every candidate equal visual weight.

## Diagnostic dashboard

Lead with the abnormal state and its scope. Follow with the time trend, affected segments, and evidence that helps isolate a cause. Separate observed facts from hypotheses. Let the viewer move from symptom to segment to records while retaining time range and filters.

## Editor or planning canvas

Prioritize the active object, its current state, and the next edit. Keep tools near what they affect. Put validation, dependencies, and consequences where they can be seen before committing a change. A side panel can hold contextual details; an inspector that repeats all canvas information adds noise. Preserve working context while revealing complexity progressively.

## Analytical exploration

Make filters and definitions visible enough that the result is interpretable. Keep the main visual and its takeaway together. Support drill-down from summary to records without losing the selected scope. Use this when the viewer is investigating rather than following a single prescribed recommendation.

## AI-assisted productivity

Separate user input, generated suggestion, supporting evidence, and approval or edit action. Make provenance and uncertainty legible when they affect trust. Put the next useful action close to the suggestion. Long explanations can be disclosed after a short, inspectable summary; a confidence badge alone is rarely sufficient evidence.

## Structural moves

- Merge cards when they express parts of one decision or comparison.
- Remove a card when it repeats an already visible fact without adding context or action.
- Enlarge the evidence that carries the first-glance target; shrink setup or metadata.
- Move secondary analysis below the primary content, or behind a deliberate detail control.
- Use annotation to connect a visible data point to its implication.
- Keep dense tables when exact scanning is central; improve sorting and emphasis instead of converting every row into a card.
- Preserve meaningful navigation and task state when changing layout.

Before implementation, describe the proposed top-to-bottom or left-to-right reading order and explain why each major region occupies its space. Check the intended desktop and narrow viewports; a hierarchy that depends on side-by-side panels may collapse in the wrong order.
