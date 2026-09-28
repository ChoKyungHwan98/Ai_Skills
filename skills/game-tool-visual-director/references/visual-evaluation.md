# Evaluating a change to this visual skill

Use when the user asks to improve the skill or determine whether a new version helps. This protocol does not require redoing every UI task twice.

## Compare actual outputs

Choose a few representative requests, including a dense chart, accepted composition needing polish, and overlapping marks. Save the old skill snapshot. Give old and candidate versions the same request, input artifacts, project snapshot, data, viewport, and permitted tools. Keep outputs separate; use comparable effort bounds and record important environment differences.

For a maintained skill, the baseline is its previous version. Use a no-skill baseline only when that answers the user's question. Evaluate the delivered UI and behavior, not whether the response repeats desired wording. For each run, retain the applied version/commit, actual output, captures, relevant interactions, failures, and user feedback.

## Review with the user or a neutral evaluator

Present the outputs without version labels when an unbiased preference comparison would help. Independent review is optional and needs an available, authorized reviewer; otherwise state that the review is not independent. Do not run an unavailable companion CLI or assume permission for delegation or extra external actions.

Ask the reviewer to identify which screen better serves the original request, what visible details caused that judgment, and what useful decisions were lost. Record no preference or mixed results honestly. If the data, viewport, or state differ, fix the comparison or describe the limitation before drawing conclusions.

## Record distinct verdicts

| Dimension | Evidence |
| --- | --- |
| Scope | Accepted structure and explicit product choices survived |
| Data integrity | Coordinates, scales, size/color meaning, units, counts, and filters stayed correct |
| Communication | Reading order and important evidence work in the real screen |
| Craft | Color roles, type hierarchy, labels, alignment, density, and product character improved |
| Interaction | Relevant close-topic selection, hover/focus, and loading states work live |

Use PASS, NEEDS REVISION, or NOT VERIFIED for each relevant dimension, with a concrete reason. CI checks packaging and scripts; its success is not a Craft verdict. Historical reference captures are inputs to judgment, not outputs of a candidate run.

## Iterate and adopt

Record specific feedback and the next change to test. Keep improvements that resolve the demonstrated failure without introducing a scope, data, or usability regression. If the comparison does not show a meaningful gain, revise the guidance or defer it. Keep the version as candidate until relevant behavioral evidence has been reviewed; do not promote it merely because new principles or more reference files were added.
