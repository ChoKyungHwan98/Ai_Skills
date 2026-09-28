# Surface polish exercise for 4.0.0

## Evidence and scope

Inspected `surface-now.png` and `surface-after.png` in `evals/cases/surface-polish` at 1920×1080, plus live hover and entrance states in headless Chromium. Both come from `layer-preview.html`, a mockup that redraws the user's review-analysis screen; the case file lists its limits. The user reviewed four published versions of the preview and gave the feedback recorded in the case file. This is a reference exercise that grounds the new guidance. It is not a run of candidate 4.0.0 against 3.2.0.

Protected decisions: the headline claim, the priority matrix with its four zones, the topic inspector, all data values, and the copy.

## Communication

- The reading order is unchanged: claim, then matrix, then inspector. The two highlighted topics lead the matrix before and after.
- The red and blue zones stay readable at a glance, which the user asked for after an earlier round faded them.
- Hovering a context point dims only other context points; the two highlighted topics and their chips stay at full strength.

Verdict for the mockup: **PASS**. Verdict for candidate 4.0.0 behavior: **NOT VERIFIED**.

## Craft

- Dark filled controls drop from three to one, and the remaining one is the report action.
- Text is 13px or larger, the scale uses eight sizes, and Hangul paragraphs no longer break mid-word.
- Bars use a tonal gradient, a rounded data end, a square baseline, and a capped width. Only the key bar carries glow and full color.
- Points are larger relative to the plot. Highlighted points read as lit spheres with a soft halo.
- The inventory flagged one text pair at 4.28:1 on a tinted button during the exercise. It was fixed to #BE123C before the final capture.

Verdict for the mockup: **PASS, pending the user's review of the last version**. Contrast over gradient surfaces (34 unresolved pairs) was checked by eye only.

## Maintenance decision

Encode the eight layers, the three-question direction step, the plateau switch, and the reference-naming step as a surface-polish route. Keep the reviewed values as one preset, and let project taste files override them. Before promoting 4.0.0 to stable, run 3.2.0 and 4.0.0 on the same "폴리싱해줘" request against the real application and compare their rendered outputs.
