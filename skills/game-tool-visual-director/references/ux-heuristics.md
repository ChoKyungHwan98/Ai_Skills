# UX diagnostic lenses

Read only when the viewer struggles to understand or operate the tool, or when a redesign changes task flow. Choose the lenses that explain the observed problem; do not score or run every lens on every screen.

| Lens | Question for an information-heavy tool |
| --- | --- |
| System status | Can the viewer tell what is selected, processing, saved, failed, or incomplete? |
| User terminology | Do labels and groupings match the viewer's working concepts rather than internal implementation names? |
| Control and freedom | Can the viewer back out, revise, or recover from consequential actions? |
| Consistency | Do similar objects, controls, and states behave predictably across the tool? |
| Error prevention | Does the interface expose constraints and consequences before a costly mistake? |
| Recognition over recall | Are needed values, options, and relationships visible where the decision or edit occurs? |
| Expert efficiency | Are frequent actions fast for practiced users without making occasional actions hard to discover? |
| Cognitive load | Is complexity caused by the task itself, or by the layout making viewers reconstruct context? |
| Grouping and proximity | Are related evidence, controls, and results near enough to be read as one unit? |
| Interaction distinction | Can viewers tell controls from static information and see the effect of an action? |
| Progressive disclosure | Are secondary details available when needed without hiding information essential to the current task? |

Do not infer that many visible actions are inherently bad: a dense editor may serve an expert's repeated work. For a consequential finding, connect the lens to the actual screen:

```text
Observation: What the screen or interaction shows.
User impact: What becomes harder for this viewer.
Relevant principle: The lens that explains the issue.
Hypothesis: Why this design causes the impact.
Change to test: What to change and verify in the next pass.
```

Prefer the user's ordinary language in the explanation. Name a principle only when it clarifies the diagnosis; a label alone is not evidence.
