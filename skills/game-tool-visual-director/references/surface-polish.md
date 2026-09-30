# Surface polish

Use when the composition is accepted and the user wants the screen to feel more finished, less flat, or less dated. Start with the rendered screen, its actual task, and the project's design rules. This route improves the visual execution of a working screen; it does not authorize changing its data definitions, chart scale, layout, or copy.

## Decide without an aesthetic interview

If the project has a taste record, use it with the current design rules and the user's latest direction. If there is none, recommend a coherent treatment from the screen and task. The user need not choose brightness, mood, fonts, colors, or effects before work starts. A consequential unresolved product fact may warrant one focused question. If a direction change requires a mockup under project rules, show that mockup before implementation; make a clear recommendation the user can react to.

Do not create or update a taste file automatically. Record durable preferences there only when the project already uses one or the user requests a reusable design record. [Taste presets](taste-presets.md) are optional examples when the project lacks an established direction, never a target to copy wholesale.

## Audit the surface, then choose changes

Inspect these eight layers together so an obvious weakness is not missed. For each relevant layer, note the visible problem, a candidate treatment, and whether changing it would help this task. No change is a valid decision when the layer already works. Apply related changes together; avoid a long series of tiny edits that never improve the whole screen.

| Layer | Look for | Possible treatment when justified |
| --- | --- | --- |
| Canvas and light | Is the page flat or does the canvas compete with the evidence? | A restrained surface tone or separation; ambient light only if project rules and the screen support it. |
| Surfaces and elevation | Are groups clear without excessive boxes or borders? | Align card edges and use one coherent border/shadow system; preserve host-app conventions. |
| Type and readability | Can Hangul, values, labels, and explanations be scanned at the real viewport? | Clarify type roles, align numerals, fix wrapping, and increase weak text contrast. |
| Color | Do data, controls, and states keep distinct meanings? | Map semantic roles to the product palette and test actual foreground/background pairs. |
| Data marks | Are important marks legible without distorting axes, size, or color meaning? | Improve mark, label, and selection treatment; preserve chart definitions and positions. |
| Details | Do annotations or callouts help interpretation? | Refine a consequential label or callout; omit decorative marks without a job. |
| Emphasis | Is the intended conclusion or selected item strongest? | Quiet competing elements and strengthen only the evidence that should lead. |
| Motion and response | Does feedback help repeated use without delay? | Improve affected hover/focus/selection states; add motion only for a useful state or relationship. |

For layers you change, choose concrete values and check how they work together across the rendered screen; “improve typography and color” is not a treatment. Values in a project-approved design system or [taste preset](taste-presets.md) can help, but preset values are examples to test, not universal targets. Do not add glows, gradients, texture, floating cards, or entrance animation just to satisfy a layer. A project's explicit bans, accessibility checks, and existing visual language outrank preset examples. If a proposed treatment conflicts with a project rule, choose a compliant treatment or present the conflict for a product decision; do not silently rewrite the rule.

## Implement and inspect

State the intended visible changes briefly, then implement the relevant layers. Use the [style inventory](../scripts/style-inventory.js) if it works on the target page and its measurements answer a specific question. Run project-required checks and compare new findings with the unchanged baseline. Screenshots at the project's required viewports and live checks of affected states determine whether the treatment works; token counts, contrast calculations, and passing builds alone do not establish visual craft.

Keep chart transformations separate from surface work. If most points cluster on a count axis, inspect the data and the user's comparison task before proposing a labeled log scale or another representation. A scale change needs its own explanation and verification; it is not an automatic spacing fix.

Show before and after when available. Explain the visible result in ordinary language and invite a simple reaction such as “좋다 / 과하다 / 약하다” or a pointed region. If a round stalls, compare a few meaningfully different treatments in a preview when the project allows it; recommend one rather than asking the user to invent a style.

When the user supplies a reference and asks what makes it work, name the useful technique and apply its principle within the project's own visual system. Do not copy the reference's brand or assume every part of it suits the product.
