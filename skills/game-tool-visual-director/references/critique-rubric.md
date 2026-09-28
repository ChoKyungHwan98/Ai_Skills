# Critique rubric

Use this rubric for the initial diagnosis and again on a rendered screenshot after implementation. Record evidence from the actual view rather than assigning a generic aesthetic score.

## Verdict

Give two separate verdicts from the rendered screen:

- **Communication — PASS / NEEDS REVISION / NOT VERIFIED:** Check the first-glance target, reading order, information hierarchy, chart choice, and clarity of the task or decision.
- **Craft — PASS / NEEDS REVISION / NOT VERIFIED:** Check alignment, typography, spacing rhythm, useful density, state clarity, visual coherence, and contextual fit. Use [visual craft](visual-craft.md) when this judgment needs detail.

The overall verdict is **PASS** only when both layers pass and no relevant interaction or accessibility regression remains. A well-structured but visibly unfinished screen needs revision; so does a beautiful screen with the wrong hierarchy. Give the observed reason and the next change to test. Do not use a numeric score or claim PASS from source code alone.

Use NOT VERIFIED when the evidence needed for a dimension is unavailable. A source-only review can identify implementation issues but cannot establish rendered craft. Explain findings through visible details and their effects; do not ask the user to supply design terminology or decide whether the professional criteria pass.

## Review prompts

| Dimension | Ask | Evidence to record |
| --- | --- | --- |
| Information architecture | Can the viewer find the decision, evidence, and details in a sensible order? | Reading path, missing or duplicated sections, unnecessary cards |
| Visualization | Does each visual answer a named question more clearly than a simpler form? | Question, chart choice, labels, scales, missing context |
| Visual hierarchy | What attracts attention first, and is it the intended message? | First glance result, competing elements, primary/secondary/tertiary distinction |
| Interaction | Is the next action clear, and is the effect of controls predictable? | Control placement, states, feedback, progressive disclosure |
| Visual craft | Is the execution coherent and appropriate for the task? | Type, spacing, alignment, density, contrast, color, borders, elevation |

## Explain major findings

When a diagnosis or revision needs a clear rationale, record:

```text
Observation: What the inspected screen shows.
User impact: What becomes harder for this viewer.
Hypothesis: The likely design cause, distinguished from observation.
Change to test: The change and the result to look for after rendering.
```

Use this for consequential findings, not every small flaw. Revisit the hypothesis after rendering; a different-looking screen does not prove the cause was addressed.
When an interaction lens clarifies the cause, add **Relevant principle** between User impact and Hypothesis; do not cite principles mechanically.

## Protect working decisions

If a redesign might erase something useful, record:

```text
Protect: The existing decision to keep.
Reason: The task or context it serves.
```

Useful information density, effective grouping, familiar terminology, clear interaction states, and valuable context should not be removed merely to simplify the screen. Check their survival in the rendered result.

## Rendered-screen pass

1. View the screen at the target viewport without reading every sentence. Write the first thing noticed and what was recognized after 1–3 seconds.
2. Trace the eye from that first point to the evidence and next action. Note jumps, dead ends, and equal-weight competition.
3. Check each chart against its stated analytical question. Look for distorted scales, missing units, weak labels, and decorative visuals.
4. Identify competing elements to remove or de-emphasize if they cause an observed problem, and protect useful existing decisions. Do not manufacture a removal merely to complete the review.
5. Check the target viewport and relevant interaction states, including empty, loading, error, selected, and narrow layouts when those states matter to the task.
6. Give separate Communication and Craft verdicts, including any visible misalignment, type inconsistency, spacing drift, or unsuitable density.

The rendered pass should answer explicitly: What appears first? Is that the intended first-glance target? Can it be recognized without reading the explanation? Are claim and evidence adjacent where relevant? Are elements competing? Does each chart answer a clear question? What can be removed? Does the target viewport work?

## Before / After Proof

When a previous screen exists, compare before and after at the same viewport with the same data and state. Verify whether the first-glance target is clearer, the reading path is shorter, competing emphasis is reduced, the relationship between claim and evidence has improved, and important information has not been lost. Check whether the diagnosed problems were resolved or only the styling changed.

Also check whether craft became more coherent without weakening a protected visual decision, interaction state, or the screen's communication.

A redesign is not an improvement merely because it looks different.

## Prioritize revisions

Classify each finding by consequence, not by how easy it is to fix:

- **Blocking:** The screen suggests the wrong decision, misrepresents data, hides a critical action, or fails at the target viewport.
- **Major:** The first-glance target is hard to grasp, evidence is detached from a claim, competing elements obscure the reading order, or visual execution is plainly inconsistent despite sound structure.
- **Minor:** Meaning is clear, but labeling, spacing, alignment, or finish slows comprehension.

Address blocking and major issues before cosmetic ones. For each revision, state the observed problem, its effect on the viewer, the proposed change, and what the next render should prove. Do not call the work complete because the code compiles or because colors and spacing improved. If a rendered view cannot be inspected, report visual verification as incomplete.
