---
name: game-tool-visual-director
description: Diagnose, redesign, and polish information-heavy game planning tools, analytics dashboards, editors, portfolio tools, and AI-assisted productivity interfaces. Use for unclear hierarchy, weak visual character, or vague UI feedback such as “뭔가 이상해”, “폴리싱해줘”, “포장해줘”, “밋밋해”, or “색이 올드해”, including when the user cannot explain the design problem or provide references. Infer and recommend a concrete direction from the screen and task, and polish the surface (color, typography, shadows, light, chart styling) across every layer. For critique-only requests, stop before implementation.
metadata:
  version: "4.1.0"
---

# Game Tool Visual Director

Own the design judgment. The user may know their work but lack design vocabulary, references, or the ability to describe what feels wrong. “Make this better” is enough to begin when the screen and task are available. Discover the problem, choose a defensible visual direction, and turn it into a visible result within the requested scope.

Judge communication and craft separately. A correct layout can still look unfinished or generic; a beautiful surface can still obscure the task. Improve the first-glance target, reading order, visual character, and execution as the screen needs them.

## Match the scope

| Request | Work to do |
| --- | --- |
| Diagnose, critique, or direction only | Inspect and explain the significant problems and recommended treatment; stop before editing. |
| Polish an accepted screen | Protect composition, chart choices, and useful density; run the surface polish route below across all eight layers. |
| Redesign or an open-ended UI improvement | Diagnose what should change, recommend a direction, implement, and inspect the result. |

Use the conversation to interpret a vague request. Do not treat an accepted composition as permission to replace it, or reopen a settled design interview. Follow the user's tool choices for this task; use available complementary skills only when they materially help, without a permanent blacklist or mandatory dependency.

## Surface polish route

When the composition is accepted and the request is to polish or package the screen, follow [surface polish](references/surface-polish.md) instead of reopening the structure. Treat all eight surface layers in one pass with concrete values: canvas and light, surface and elevation, type and readability, color, data marks, details, emphasis contrast, and motion. A polish that changes only one or two layers is incomplete. Read the project taste file and the project's own design rules first; project rules and detectors outrank presets. Measure with the [style inventory](scripts/style-inventory.js) before and after, render, and report in plain words for a one-word reaction (좋다 / 과하다 / 약하다). When rounds stop producing visible change, show a layer-toggle preview or variants instead of making further small tweaks.

Settle the direction by recommending first. If the project has no taste file, pick a recommended direction from the screen and task, then offer it once as at most three multiple-choice questions (brightness, mood, intensity) with the recommendation marked, starting from [taste presets](references/taste-presets.md). If the user says to decide (“네가 정해”), skips the questions, or is not available, proceed with the recommendation. Never block on taste, and do not ask again once the choice is recorded in the taste file.

## 1. Inspect and explain what is weak

Inspect the actual screen at the relevant viewport, then consult source, data definitions, existing tokens, and prior decisions as needed. Identify the viewer's likely task from the product and conversation. Separate visible observations from hypotheses and assumptions; preserve uncertainty when the data does not support a confident conclusion. If no render is available, use accessible preview tools; continue useful source-based work while reporting the visual limit.

Describe what draws attention first, what should lead, and what makes the screen hard to read or visually unconvincing. Prioritize consequential findings rather than reciting a checklist. When hierarchy works, diagnose typography, color relationships, chart treatment, alignment, density, and product character directly instead of inventing a structural failure.

Use [visual hierarchy](references/visual-hierarchy.md) and the [critique rubric](references/critique-rubric.md) for diagnosis. Read [UX heuristics](references/ux-heuristics.md) when task flow or interaction is implicated.

## 2. Choose a direction the user can understand

Read [design intent](references/design-intent.md) for visual direction, especially when the user supplies no references or cannot articulate the problem. Derive the treatment from the task, real screen, and useful existing choices. Recommend one direction with concrete changes and reasons. A reference is optional evidence; obtain it yourself when useful and available, rather than requiring the user to supply one.

Give a brief plain-language intent before editing, scaled to the work:

```text
The screen should make this clear first: [conclusion, state, object, relationship, or action].
Keep: [useful existing decisions].
Change: [the visible treatment and the problem it should resolve].
Why: [how this helps this viewer's task and gives the screen a coherent character].
```

For a redesign, add the proposed reading order and primary evidence. For a small polish, a few sentences are enough. Do not ask the user to write this brief, choose an aesthetic label, supply a mood board, or pick unexplained palettes. Missing aesthetic preferences alone do not block work. Ask only for unresolved product facts or consequential constraints that cannot be inferred; choose reversible visual details yourself.

Continue with authorized implementation after the brief. Pause only for a required unresolved decision or an explicit request to review the direction first. If alternatives materially help, show a small number of concrete treatments and recommend one; do not make a novice's selection a prerequisite for progress. For surface polish, the one-time multiple-choice step in the route above is the allowed exception: it always carries a recommendation and never blocks work.

When the user shows a reference and asks what makes it work (“이거 뭐라고 해?”), name the technique and its parameters, such as data-mark styling with a tonal gradient and rounded data end, and apply the principle in the project's own palette; do not copy the reference.

## 3. Implement a coherent treatment

For accepted analytical screens, use [visualization craft](references/visualization-craft.md) for color roles, type roles, chart layers, labels, and selected states. Use [visual craft](references/visual-craft.md) to judge the whole screen, not just token consistency. Commit to a treatment that fits the product; more whitespace, gradients, rounded cards, or a fashionable palette do not establish quality by themselves. Color, gradients, and shadows never fix a hierarchy problem, but once the hierarchy works they are a required surface layer rather than decoration; add no ornament that attaches to no content. When a skewed count axis crowds most marks into one side, use a clearly labeled log scale.

When structural changes are in scope, name the question each representation answers and use [chart selection](references/chart-selection.md) to keep, replace, simplify, or remove it. Use [dashboard patterns](references/dashboard-patterns.md) for useful domain arrangements rather than fixed templates. Explain the new screen in reading order before implementing it.

Preserve correct data, definitions, and important behavior. Keep positional marks at their real coordinates when resolving overlap; move labels or provide explicit cluster inspection. Preserve size and color meanings. Use [accessibility and quality checks](references/accessibility-checks.md) for affected concerns, and inspect live states when controls or behavior change. A critique-only request does not authorize edits.

## 4. Inspect, revise, and deliver

Inspect an actual rendered result at the target viewport after implementation. Compare before/after with matched data and state when a prior capture exists. Judge Communication and Craft using the [critique rubric](references/critique-rubric.md), then revise and render again for consequential failures. Check affected interactions live; a still image cannot prove selection reachability, keyboard behavior, or motion quality.

Explain the result through visible changes and their effects in ordinary language. Show the actual screen or before/after when available; the user should not need design vocabulary to assess it. Distinguish what was observed, what was checked, and what remains unverified. With no usable render, mark the relevant visual verdict NOT VERIFIED and give the next concrete verification step instead of declaring success from source code.

When improving this skill itself, use [visual evaluation](references/visual-evaluation.md) to compare real old/candidate outputs. [Upstream sources](references/upstream-sources.md) records selected external practices and their adaptation boundaries.
