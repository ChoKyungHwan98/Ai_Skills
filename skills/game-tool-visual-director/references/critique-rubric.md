# Critique rubric

Use this rubric for the initial diagnosis and again on a rendered screenshot after implementation. Record evidence from the actual view rather than assigning a generic aesthetic score.

## Verdict

Record **PASS** only when the rendered screen communicates the intended first-second message, connects it to evidence, supports the decision, and works at the target viewport. Record **NEEDS REVISION** if any of those conditions fail. Do not use a numeric score. Give the observed reason and the next change to test.

## Review prompts

| Dimension | Ask | Evidence to record |
| --- | --- | --- |
| Information architecture | Can the viewer find the decision, evidence, and details in a sensible order? | Reading path, missing or duplicated sections, unnecessary cards |
| Visualization | Does each visual answer a named question more clearly than a simpler form? | Question, chart choice, labels, scales, missing context |
| Visual hierarchy | What attracts attention first, and is it the intended message? | First glance result, competing elements, primary/secondary/tertiary distinction |
| Interaction | Is the next action clear, and is the effect of controls predictable? | Control placement, states, feedback, progressive disclosure |
| Cosmetic styling | Does styling reinforce the established structure? | Type, contrast, spacing, alignment, color semantics |

## Rendered-screen pass

1. View the screen at the target viewport without reading every sentence. Write the first thing noticed and the conclusion retained after 1–3 seconds.
2. Trace the eye from that first point to the evidence and next action. Note jumps, dead ends, and equal-weight competition.
3. Check each chart against its stated analytical question. Look for distorted scales, missing units, weak labels, and decorative visuals.
4. Identify one element to remove or de-emphasize. If nothing can be removed, explain what each prominent element contributes.
5. Check the target viewport and relevant interaction states, including empty, loading, error, selected, and narrow layouts when those states matter to the task.

The rendered pass should answer explicitly: What appears first? Is that the intended message? Can the conclusion be understood without reading the explanation? Are claim and evidence adjacent? Are elements competing? Does each chart answer a clear question? What can be removed? Does the target viewport work?

## Prioritize revisions

Classify each finding by consequence, not by how easy it is to fix:

- **Blocking:** The screen suggests the wrong decision, misrepresents data, hides a critical action, or fails at the target viewport.
- **Major:** The message is hard to grasp, evidence is detached from the conclusion, or competing elements obscure the reading order.
- **Minor:** Meaning is clear, but labeling, spacing, alignment, or finish slows comprehension.

Address blocking and major issues before cosmetic ones. For each revision, state the observed problem, its effect on the viewer, the proposed change, and what the next render should prove. Do not call the work complete because the code compiles or because colors and spacing improved. If a rendered view cannot be inspected, report visual verification as incomplete.
