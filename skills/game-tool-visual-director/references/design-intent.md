# Design intent

Use when choosing or interpreting visual direction. The user's ability to provide references or describe aesthetics is not a prerequisite. Take responsibility for a concrete recommendation while keeping product decisions and explicit constraints authoritative.

## Start from evidence already available

Inspect the current render, the task it supports, useful interaction patterns, tokens, README, and prior decisions. Infer what must remain visible and what should lead. The product supplies design inputs even when the user says only “뭔가 이상해.” Distinguish inferred intent from confirmed facts; do not invent an audience, brand, or analytical conclusion.

Separate a missing design preference from a missing product fact. With a visible review dashboard and a known investigation task, choose type, spacing, and emphasis yourself. If the same screen could be a public report or a daily operational console and context cannot resolve that consequential difference, ask who uses it and for what task. Do not ask the user to translate that answer into a style.

## Translate the reaction into a treatment

Words such as “깔끔하게,” “고급스럽게,” or “촌스러워” describe reactions, not implementation details. Locate their likely visible causes. A dense comparison table can feel cleaner through aligned values and quieter secondary labels without losing rows. A sound dashboard can feel unfinished because its chart annotations, controls, and headings use unrelated visual treatments.

When describing a significant issue, connect three things: what is visible, why that is a problem here, and the treatment to test. Avoid giving the user a list of abstract virtues such as “improve hierarchy, consistency, and polish.”

## Make one concrete recommendation

Choose a coherent direction across the parts that need change. Use the following as design decisions, not a mandatory questionnaire or output form:

| Decision | Specify in this screen |
| --- | --- |
| First impression | What should be recognized first and what the product should feel like during this task |
| Typography | Which content leads, which labels recede, and how values align; inspect Korean and Latin glyphs when relevant |
| Color and surfaces | Which roles use emphasis, how data and selection remain distinct, and where surface separation helps |
| Composition and density | What remains visible for comparison, where space helps grouping, and what existing layout is protected |
| Chart or object treatment | How marks, labels, annotations, connections, and controls express the important relationships |
| Interaction | How selection, focus, and feedback support repeated work; use motion only when it serves the task |

Name actual treatments: a stronger selected-topic label, aligned numeric rows, quieter quadrant fills, or consistent annotation boundaries. When source is available, choose concrete font, color, spacing, and component values before implementation and test them in the real render. A list of token names or adjectives is not a finished direction.

Prefer a recommendation over an unranked menu. For surface polish, [surface polish](surface-polish.md) derives that recommendation from the screen and project rules even when no taste file exists. If the user asks you to decide, decide within scope and explain briefly. For reversible choices, implement the recommended treatment and let the visible result support feedback. Offer concrete alternatives only when they illuminate a meaningful tradeoff or the user asks for them.

### Example without a user reference

A review-analysis screen already has a clear takeaway, a priority scatter chart, and a topic inspector. The complaint topic is selected, but its small label barely differs from ordinary topics and its supporting values are hard to scan. The user says: “디자인은 잘 몰라. 지금 구성은 유지하고 보기 좋게 해줘.”

A suitable recommendation is: “지도와 오른쪽 상세 패널은 유지하겠습니다. 선택한 주제의 이름과 수치를 더 또렷하게 묶고, 배경 구획은 차분하게 낮추겠습니다. 불만의 붉은색은 유지하면서 선택 표시를 따로 넣어, 어떤 주제를 보고 있는지 바로 알 수 있게 하겠습니다.”

This chooses a visible treatment and preserves a useful composition without asking for a palette or named style. It remains a hypothesis until the resulting screen is inspected; it is not a prescription for every dashboard.

## Use references as optional research

When the existing product provides enough evidence, proceed without an external reference. When a reference would resolve a real design question, find relevant examples with available tools and inspect the actual page or image. Extract task-relevant traits, such as compact navigation or precise label hierarchy, rather than copying a product's appearance. If research is unavailable, use the current screen and state the limitation; do not send the research burden back to the user.

Honor references the user does provide, including what they want to avoid. An external reference should not overwrite useful density, semantic colors, accepted charts, or an established product direction. A preference inferred from one screen is not a permanent design rule for other products.

## Make feedback easy

Explain choices in terms the user can see: “선택한 항목이 더 잘 보입니다” or “수치를 세로로 맞춰 비교하기 쉽게 했습니다.” Technical details can support implementation, but do not make them the user's means of evaluating the design. Show actual output when available and accept reactions such as “아직 밋밋해” as useful evidence to diagnose, rather than requiring a more professional critique.
