# Visualization craft for game planning tools

Use when an accepted analytical screen needs better visual execution. Work from its rendered appearance and existing product direction. The checks below guide choices, not a mandatory theme or fixed component kit.

## Make the visual choices concrete

Describe the observed weakness and the change to test: for example, labels compete with the takeaway, supporting text is too faint, or a selected point is hard to distinguish. Record a short treatment note covering color roles, type roles, chart layers, and one or two protected decisions. If the direction is unresolved, compare a small number of palette/type candidates on the same chart, with the same data and layout.

## Color: assign roles before values

Audit the current canvas, surfaces, text, controls, state colors, and data meanings. Map these roles to existing tokens where possible:

| Role | Check in an analytical screen |
| --- | --- |
| Canvas and chart surface | A useful separation without tinting every section |
| Main and secondary text | Readable hierarchy across labels, annotations, and explanation |
| Controls and focus | Actions remain recognizable beside strongly colored data |
| Positive, negative, warning, unknown | Stable meanings, with text or shape cues |
| Unselected and selected marks | Selection is visible without changing the data meaning |
| Axes, grid, thresholds, separators | Reference layers help reading without competing with evidence |

Use categorical colors for distinct groups, sequential colors for ordered magnitude, and diverging colors for deviation from a defensible reference. Avoid making a selected negative mark look positive merely because the interface accent is blue. A neutral control treatment may help preserve the chart's semantic colors; it is a contextual choice.

External palettes are starting candidates. Evaluate them against existing brand decisions, information density, supported themes, and actual text/background pairs. Preserve neutral grays and familiar fonts when they serve the product. A new hue alone is not a visual direction.

Measure changed color pairs using computed foreground and background colors. For ordinary text, use the 4.5:1 threshold; for qualifying large text, use 3:1. Essential non-text visual information has a 3:1 requirement against adjacent colors, with scope and exceptions described in the W3C references in [sources](upstream-sources.md). Check the unrounded result. Passing one pair is not a complete accessibility verdict.

For opaque sRGB hex pairs, the [contrast helper](../scripts/contrast.py) provides a repeatable check. Resolve alpha layers, gradients, images, and other color spaces before using it; do not feed a nominal background that differs from the actual rendered surface.

```powershell
# Run from the skill directory; these are a calculation example, not a palette prescription.
python scripts/contrast.py "#1E293B" "#F8FAFC"
```

## Typography: define a few roles

Distinguish the takeaway, panel title, topic label, numeric value, axis/tick, and supporting note. Similar roles should share a treatment; differences should express importance rather than introduce unrelated fonts or weights. Favor alignment and weight before shrinking all supporting content to make it fit.

For Korean interfaces, inspect actual Hangul, Latin game names, numerals, punctuation, and long topic names in the proposed font stack. A Latin font pairing from a catalog does not establish Korean glyph quality. Keep explicit units and appropriate precision; use tabular numerals where their alignment improves comparison. Check at the actual viewport and normal viewing scale.

## Charts: control the layers

Let marks and the selected evidence lead; keep grid lines and quadrant fills subordinate. Use enough ticks to locate values without producing a dense lattice. Threshold lines need a stated meaning. Do not change scales, thresholds, clipping, or numeric precision solely to create an attractive pattern.

Anchor a compact annotation near a consequential mark, with a clear topic and useful value. Keep the chosen point distinguishable while reading that annotation. Boundaries should clarify grouping or selection; avoid stacking a strong grid, strong regions, dark outlines, and loud annotations at once.

### Overlap without false positions

- Preserve actual x/y coordinates and the meaning of size/color encodings.
- Move labels first and reserve space for important labels. If leaders are needed, connect labels to the real mark clearly; do not leave tiny unexplained segments.
- If reducing mark sizes, use a consistent rule that preserves the size encoding. Do not make unequal bubbles equal without deliberately changing and explaining that encoding.
- For genuinely dense marks, provide an explicit cluster inspector or topic list with each item's values. A cluster proxy must look like a group, not a shifted individual data point. Exact positions must remain inspectable when positional comparison matters.
- Check hit targets, z-order, and cycling/list selection so every close topic is reachable. A readable screenshot alone cannot establish this behavior.

## States and rhythm

Align repeated label/value rows and use gaps to distinguish related items from section boundaries. Preserve useful comparison density; neither more whitespace nor more rounded cards is an automatic improvement.

Inspect hover, focus, selection, and loading when changed. Keep feedback immediate enough for repeated use. Motion should clarify a state or relationship and remain interruptible; it must not delay topic inspection or decorate a static chart. Use live interaction to judge it.

## Finish with evidence

Compare the real before/after at matched viewport, data, filters, and selection. Record which visible weakness improved, what useful decision survived, and what remains unresolved. Check functional/data invariants separately, then give Communication and Craft verdicts using the [critique rubric](critique-rubric.md).
