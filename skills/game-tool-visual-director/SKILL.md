---
name: game-tool-visual-director
description: Diagnose and redesign information-heavy game planning tools, analytics dashboards, editors, portfolio tools, and AI-assisted productivity interfaces. Use when feedback is vague (such as “뭔가 이상해”, “직관적이지 않아”, “시각화가 부족해”, “폴리싱해줘”, or “정보만 모아둔 것 같아”) or when a screen needs clearer visual direction, information hierarchy, or visualization choices. For critique-only requests, stop before implementation.
---

# Game Tool Visual Director

Treat each screen as a communication problem before treating it as a styling problem. Translate subjective feedback into observable problems and a testable visual intent. A polished screen should help its viewer recognize the relevant conclusion, state, object, relationship, or action and proceed with the task, not merely display all available information.

## 1. Inspect without editing

Inspect the current screenshot or rendered screen, relevant code and layout, available data and definitions, target viewport, and the user's goal. Identify the viewer and the decision the screen supports. If an input is unavailable, state the assumption or limitation; do not invent data or infer the rendered result from code alone. For critique-only work, this and the following design stages are the deliverable.

## 2. Diagnose the communication failure

Describe what currently draws attention first, what should draw attention first, and what competes with it. Look for unnecessary cards, excess text, weak grouping, unsuitable charts, interaction friction, and styling issues. Translate vague reactions into specific, observable causes and effects. Classify findings under information architecture, visualization, visual hierarchy, interaction, and cosmetic styling. Prioritize structural causes before cosmetic symptoms. Use [visual hierarchy](references/visual-hierarchy.md) and [critique rubric](references/critique-rubric.md) when the diagnosis needs sharper criteria.

## 3. State Visual Intent before implementation

Present this compact brief to the user before changing the UI:

```text
Viewer:
First-glance target: [the one conclusion, state, object, relationship, or action the viewer should recognize within 1–3 seconds]
Decision or task this screen supports:
Attention order:
1.
2.
3.
4.
Primary evidence:
Secondary evidence:
Remove or de-emphasize:
```

Make the intended message and evidence specific to the screen. Distinguish primary, secondary, and tertiary information. If the evidence does not justify a confident conclusion, make uncertainty part of the message.

Continue after stating Visual Intent unless the goal is unclear, an important product decision or destructive change requires user input, or the user explicitly requested review before implementation.

## 4. Reconsider every representation

For each chart or visual, write the analytical question it must answer. Keep, replace, simplify, or remove it according to that question and the available data. Do not preserve a scatter plot, donut, KPI card, or any other component just because it exists. Choose the simplest honest form: ranked or diverging bar, dot plot, scatter plot, quadrant, histogram, line chart, heatmap, table, KPI, annotation, small multiples, text plus number, or no chart. Use [chart selection](references/chart-selection.md) for decision rules and data integrity checks.

## 5. Describe the new structure

Before implementation, describe the proposed screen in reading order: what leads, where its evidence sits, what follows, and what becomes progressively disclosed. Question the existing layout. Reorder sections, resize panels, merge or remove cards, replace charts, adjust density, and move supporting details below when these changes clarify the decision. Use [dashboard patterns](references/dashboard-patterns.md) for domain-specific arrangements, without treating them as templates.

## 6. Implement when requested

Only after diagnosis, Visual Intent, visualization choice, and layout structure are explicit, modify the application. Preserve correct data, definitions, and important behavior. Check chart semantics, labels, units, interaction states, and accessibility as part of the implementation. A request for critique or direction alone does not authorize code changes.

## 7. Critique the rendered result and revise

Inspect an actual rendered screenshot at the target viewport after implementation. Ask: What appears first? Is it the first-glance target? Can that target be recognized without reading every sentence? Is supporting evidence adjacent? Do elements compete equally? Does every chart answer a question? What can be removed? Does the viewport work? Use [critique rubric](references/critique-rubric.md) to record concrete failures. Revise and render again when the result misses the intent. If rendering is unavailable, report that visual verification is incomplete rather than declaring success from source code.

## Avoid

Do not substitute color, spacing, gradients, or shadows for hierarchy. Do not put every item in a card, emphasize everything, retain charts or layout by default, add decoration without informational purpose, or declare success immediately after coding.
