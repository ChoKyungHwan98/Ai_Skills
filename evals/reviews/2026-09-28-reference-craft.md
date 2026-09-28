# Reference exercise for visualization craft 3.2.0

## Evidence and scope

Inspected the actual `before-craft.jpg` and `after-craft.jpg` in `evals/cases/review-dashboard` at their 1920×1080 image size. Both show Palworld, 1,343 analyzed reviews, and optimization selected. Capture provenance and comparison limitations are in that case's JSON. These historical renders predate candidate 3.2.0; this is a reference exercise, not an old/candidate run or blind comparison.

Protected decisions: priority-map composition, the adjacent topic inspector, visible data values, and the user's accepted analytical task.

## Communication observations

- The after capture names both axes and provides additional numerical ticks; locating a point relative to a value is more direct than in the before capture.
- Both captures identify optimization as the selected complaint topic. The after capture keeps the red data meaning and adds a separate ring and annotation boundary to identify selection.
- The close price/open-world topics are shown together with separate counts. The after capture explicitly labels them as two nearby topics, which helps distinguish a group treatment from one topic.

Candidate Communication verdict: **NOT VERIFIED**. These observations ground the guide in a real screen but cannot show what candidate 3.2.0 would produce.

## Craft observations

- The before capture gives consequential annotations a small treatment similar to ordinary topic labels. The after capture uses larger, bordered topic/value annotations for optimization and pal design, creating a visible distinction between reading roles.
- The after capture uses a pale rose region for the complaint priority and a pale blue region for the strength priority. The colored data and annotation text remain stronger than those backgrounds.
- The after group inspector aligns the two topic names and their values in rows. The before capture places their small text directly beside a compact group badge.

Candidate Craft verdict: **NOT VERIFIED**. Palette and type choices are visible, but computed color-pair values were not captured with these images; no numerical contrast PASS is asserted.

## Data and interaction

Exact coordinate invariants, original bubble-size meaning, hit target reachability, hover, focus, and keyboard selection: **NOT VERIFIED by these still captures**. Preserve the original data and inspect live interaction when applying the guide to an implementation.

## Maintenance decision

Keep the new reference focused on operational choices illustrated here: type roles, quiet reference layers, semantic selection, readable grouped values, and separate evidence for data/interaction. A fair old/candidate comparison needs new outputs from matched inputs and comparable effort; do not reuse these historical captures as that comparison.
