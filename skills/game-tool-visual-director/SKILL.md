---
name: game-tool-visual-director
description: Diagnose, redesign, and polish information-heavy game planning tools, analytics dashboards, editors, portfolio tools, and AI-assisted productivity interfaces. Use when feedback is vague (such as “뭔가 이상해”, “직관적이지 않아”, “시각화가 부족해”, “폴리싱해줘”, “포장해줘”, “밋밋해”, “색이 올드해”, or “정보만 모아둔 것 같아”) or when a screen needs clearer visual direction, information hierarchy, visualization choices, or surface polish such as color, typography, shadows, light, and chart styling. For critique-only requests, stop before implementation.
metadata:
  version: "4.0.0"
---

# Game Tool Visual Director

Treat each screen as a communication problem before treating it as a styling problem. Translate subjective feedback into observable problems and a testable visual intent. A polished screen should help its viewer recognize the relevant conclusion, state, object, relationship, or action and proceed with the task, not merely display all available information.

When the hierarchy already works, visual execution can be the main task. Judge the palette, typography, chart treatment, and product character directly; a correct structure alone is not evidence of finished craft.

## Match the requested scope

Distinguish diagnosis, structural redesign, and visual polish. When the user has accepted the composition or chart type, treat it as a protected decision and focus on its execution; briefly flag any demonstrated data or usability defect without reopening the whole design. Infer established goals from the current screen and conversation instead of repeating a design interview. Follow the user's tool choices for the current task. Use complementary skills only when they materially help; do not turn one task's preference into a permanent tool ban or mandatory dependency.

## Surface polish route

When the composition is accepted and the request is to polish or package the screen, follow [surface polish](references/surface-polish.md) instead of reopening the structure. Read the project taste file, or ask at most three multiple-choice direction questions once and start from [taste presets](references/taste-presets.md). Treat all eight surface layers in one pass with concrete values: canvas and light, surface and elevation, type and readability, color, data marks, details, emphasis contrast, and motion. A polish that changes only one or two layers is incomplete. Measure with the [style inventory](scripts/style-inventory.js) before and after, render, and report in plain words for a one-word reaction. When rounds stop producing visible change, show a layer-toggle preview or variants instead of making further small tweaks.

Offer choices and previews rather than asking a non-designer to describe design in words. When the user shows a reference, name the technique that makes it work and apply the principle in the project's own palette; do not copy the reference.

## 1. Inspect without editing

Inspect the current screenshot or rendered screen, relevant code and layout, available data and definitions, target viewport, and the user's goal. Read existing design context and preserve visual direction the user has already chosen. Identify the viewer and the decision or task the screen supports. If an input is unavailable, state the assumption or limitation; do not invent data or infer the rendered result from code alone. For critique-only work, complete the applicable design and critique stages without implementation.

## 2. Diagnose the communication failure

Describe what currently draws attention first, what should draw attention first, and what competes with it. Look for unnecessary cards, excess text, weak grouping, unsuitable charts, interaction friction, and styling issues. Translate vague reactions into specific, observable causes and effects. Classify findings under information architecture, visualization, visual hierarchy, interaction, and cosmetic styling. Prioritize structural causes before cosmetic symptoms. Use [visual hierarchy](references/visual-hierarchy.md) and [critique rubric](references/critique-rubric.md) when the diagnosis needs sharper criteria; use [UX heuristics](references/ux-heuristics.md) only when task flow or interaction is at issue.

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

For each chart or visual, write the analytical question it must answer. When representation changes are within scope, keep, replace, simplify, or remove it according to that question and the available data. Respect representations the user explicitly wants to retain. Choose the simplest honest form: ranked or diverging bar, dot plot, scatter plot, quadrant, histogram, line chart, heatmap, table, KPI, annotation, small multiples, text plus number, or no chart. Use [chart selection](references/chart-selection.md) for decision rules and data integrity checks. For positional charts, keep marks at their true coordinates when resolving overlap; move labels, adjust mark treatment, or provide explicit cluster inspection rather than silently moving data marks.

## 5. Describe the new structure

Before implementation, describe the screen in reading order: what leads, where its evidence sits, what follows, and what becomes progressively disclosed. For a polish request with accepted composition, confirm that structure briefly and run the surface polish route. For structural redesign, question the existing layout and adjust sections, panels, charts, and density when that clarifies the task. Use [dashboard patterns](references/dashboard-patterns.md) for domain-specific arrangements, without treating them as templates.

## 6. Check design intent when visual direction matters

After the information structure and Visual Intent are clear, use [design intent](references/design-intent.md) if the request concerns visual character or an existing direction needs interpretation. Ground it in the project's current choices and the user's specific references; do not turn vague adjectives into automatic style prescriptions.

For analytical screens, use [visualization craft](references/visualization-craft.md) to translate that direction into color roles, type roles, chart layers, labels, and selection states. Preserve the existing product palette when it works; external palettes are candidates to compare, not automatic replacements.

## 7. Implement when requested

Only after diagnosis, Visual Intent, visualization choice, layout structure, and any relevant design intent are explicit, modify the application. Preserve correct data, definitions, important behavior, and useful existing design decisions. Check chart semantics, labels, units, and interaction states. Use [accessibility and quality checks](references/accessibility-checks.md) when changes affect those concerns. A request for critique or direction alone does not authorize code changes.

## 8. Check UX quality and visual craft

When task flow or controls changed, inspect relevant interaction states with [UX heuristics](references/ux-heuristics.md) and [accessibility and quality checks](references/accessibility-checks.md). After communication and structure are established, use [visual craft](references/visual-craft.md) to judge execution and contextual fit. Do not infer live behavior from a still screenshot.

## 9. Critique the rendered result and revise

Inspect an actual rendered screenshot at the target viewport for a screen critique and after implementation. Use [critique rubric](references/critique-rubric.md) for separate Communication and Craft verdicts; both must pass. When implementation produces an after screen and a previous screen exists, compare them at the same viewport and data/state. If implementation was requested, revise and render again when either layer misses its intent; for critique-only requests, report the findings. If rendering is unavailable, report visual verification as incomplete rather than declaring success from source code.

When evaluating a change to this skill itself, use [visual evaluation](references/visual-evaluation.md) to compare actual outputs from old and candidate versions. See [upstream sources](references/upstream-sources.md) for the selected external practices and adaptation boundaries.

## Avoid

Do not use color, spacing, gradients, or shadows to fix a hierarchy problem; once the hierarchy works, they are a required surface layer, not decoration. Do not put every item in a card, emphasize everything, retain charts or layout by default, add ornaments that attach to no content, stop a polish after one or two property changes, or declare success immediately after coding.
