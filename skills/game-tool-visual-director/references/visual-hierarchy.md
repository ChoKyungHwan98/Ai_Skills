# Visual hierarchy

Use this reference when the screen feels “off,” dense, or visually flat, and the cause is not yet clear.

## Diagnose attention, not taste

At the target viewport, look away, then glance for 1–3 seconds. Record the first item noticed and what the viewer can recognize. Compare both with the Visual Intent. Repeat at a normal reading distance and at a narrow viewport if that viewport matters. Do not assume that a large element communicates the right idea; a large chart with no framing can dominate while conveying no takeaway.

Separate these questions:

| Question | Signal of failure | Useful change |
| --- | --- | --- |
| What is this screen for? | The title names a feature, but the task, active state, or decision is unclear. | Give the relevant first-glance target a clear lead. |
| Where should I look first? | Several cards have equal size, contrast, and heading weight. | Give one region clear priority; reduce emphasis elsewhere. |
| Why should I believe the conclusion? | Evidence is far from the claim or hidden in tooltips. | Place the relevant measure, comparison, and caveat beside the claim. |
| What should I do next? | Controls compete with evidence or appear before context. | Put the primary action near the decision; move setup controls to a calmer area. |
| What can wait? | Metadata and details occupy prime space. | Move them below, collapse them, or expose them on demand. |

## Translate vague feedback

- “뭔가 이상해” (“Something feels off”): identify the first three attention targets, the visual relationship among them, and the expected reading path. Name the mismatch, such as a decorative summary overpowering the actual recommendation.
- “직관적이지 않아” (“It isn't intuitive”): check whether labels match the user's mental model, the next action is visible, controls are close to their effect, and state or consequences are clear.
- “시각화가 부족해” (“There isn't enough visualization”): find the comparison, trend, distribution, or relationship currently buried in prose or numbers. A chart is justified only if it answers that question faster or more accurately.
- “폴리싱해줘” (“Polish it”): diagnose hierarchy and structure first. If the structure is sound or already accepted, inspect the [surface layers](surface-polish.md) together and improve the ones that visibly weaken the screen.
- “정보만 모아둔 것 같아” (“It feels like a pile of information”): locate the missing conclusion, grouping, prioritization, or decision path. Consolidate or remove repetitive cards.

These are hypotheses to test against the actual screen, not automatic diagnoses.

## Trace consequential diagnoses

When a finding drives a structural change or its cause needs explanation, keep observation separate from interpretation:

```text
Observation: What is visible in the inspected screen and state?
User impact: What does this delay, obscure, or make harder for the viewer?
Hypothesis: Why might the observed design cause that impact?
Change to test: What change should produce a clearer result in the next render?
```

Use this trace for major decisions, not every minor alignment or spacing issue. Do not present a hypothesis as an observed fact.

## Build an attention order

Prefer a reading sequence of: conclusion or current state; the comparison that supports it; the control or next action; deeper evidence and caveats. This is a useful default, not a fixed layout. A data-entry editor may need the active object and action first; an incident screen may need a warning and its scope first.

Make hierarchy with semantic choices before visual effects: content order, area, grouping, proximity, alignment, and concise labels. Then use typography, contrast, color, and whitespace to reinforce it. Color should carry a stable meaning; status colors must not be the only way to read state.

Keep tertiary material available without giving it equal weight. A table can remain dense when scanning exact values is the job. Do not force spaciousness at the cost of comparison or useful working context.

## Control emphasis deliberately

- **Primary:** The conclusion, current state, or active object the viewer must recognize first. Give it the strongest position, enough size, and clear separation from surrounding material.
- **Secondary:** The evidence and action that make the primary message useful. Keep them close enough to be understood together, with lower emphasis than the primary item.
- **Tertiary:** Definitions, raw records, metadata, and rare actions. Keep them legible and reachable, but away from the first-glance path.

Position establishes reading order; size signals priority; contrast and isolation decide what wins a glance. Typography distinguishes a conclusion from a label or explanation. Use color for meaning and selective emphasis, not as the only carrier of status. If several regions are large, high contrast, isolated, and brightly colored, they compete: reduce emphasis on the less important regions rather than making the intended lead louder still.

## Reduce text dependency

Replace prose that explains a visible comparison with a direct label, reference line, annotated data point, or aligned values. Put a claim near its evidence so the viewer can verify it without searching. Keep short explanations for causes, assumptions, and uncertainty that the visual cannot express. Test the 1–3 second impression again with body copy unread: the viewer should still grasp the first-glance target.
