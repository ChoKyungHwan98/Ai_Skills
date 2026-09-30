# Changes

## 4.1.1 — candidate — 2026-10-01

- Make surface polish evidence-led: inspect all eight layers but change only those that weaken the actual screen, preserving useful working treatments.
- Stop default taste questions and automatic taste-file creation when the user delegates design judgment. Keep presets as optional examples.
- Separate chart-scale changes from styling; a skewed distribution alone does not authorize changing an accepted axis to log.
- Respect project rules requiring a design mockup before a direction change, and do not silently rewrite conflicting rules.
- Add a project-grounded preflight and focused regression scenarios. No claim of improved UI output is made without a candidate run on the actual application.

## 4.1.0 — candidate — 2026-09-28

Combines 3.3.0 (design ownership without references) and 4.0.0 (surface polish route).

- Keep the 3.3 scope-aware four-step workflow and add the surface polish route to it.
- Settle a surface direction by recommending first: offer at most three multiple-choice questions once with the recommendation marked, and proceed with the recommendation when the user says “네가 정해”, skips, or cannot be asked. Taste never blocks work.

## 4.0.0 — candidate — 2026-09-28

- Add a surface polish route: once the composition is accepted, a polish pass treats all eight layers (canvas and light, surface and elevation, type and readability, color, data marks, details, emphasis contrast, motion) with concrete values. Changing one or two properties no longer counts as a polish.
- Settle direction with at most three multiple-choice questions, record it in a project taste file, and start from a reviewed preset (bright, premium and calm, subtle).
- Switch to a layer-toggle preview or variants when rounds plateau. Name the technique when the user shows a reference, and apply it without copying.
- Reframe the gradient and shadow caution: they never fix hierarchy, but they are a required surface layer once hierarchy works.
- Add `scripts/style-inventory.js`, a browser-evaluated count of text sizes, colors, contrast flags, Hangul mid-word breaks, borders, shadows, dark filled controls, and chart-mark fills.
- Spread crowded scatter marks with a labeled log scale for skewed count axes, and use zone-tinted hollow rings for context points with solid highlighted points.
- Let project rules and detectors override presets: neutral shadows where colored glows are flagged, opaque chrome where contrast is measured by pixels, and a documented rule change when an approved direction conflicts. Name volume × dissatisfaction quadrants as an IPA matrix with its standard zones.
- Add regression scenarios 21–29 and the surface-polish reference case with before and after renders and user feedback.

Evidence comes from a mockup the user reviewed, not from a candidate run against the real application. An old/candidate comparison is still pending.

## 3.3.0 — candidate — 2026-09-28

- Make design judgment the agent's responsibility when the user lacks references, design vocabulary, or a precise problem description.
- Replace the fixed nine-stage workflow with scope-aware inspection, a concrete recommendation, implementation, and rendered review.
- Expand design-intent guidance for deriving visual treatments from the product, explaining choices in ordinary language, and researching references only when useful.
- Add six regression scenarios for vague requests, delegated aesthetic choices, missing product facts, critique boundaries, and unavailable renders.
- Align missing-evidence verdicts with NOT VERIFIED and remove the requirement to find something to remove in every review.
- Correct trial-install instructions for the still-unmerged candidate branch.
- Ignore generated Python bytecode during local-edit checks while preserving full backup integrity and protection for other files in cache folders.

The accompanying screenshot exercise records a recommendation from a historical render, not a candidate implementation or independent old/candidate comparison. Visual improvement remains unverified; retain candidate status.

## 3.2.0 — candidate — 2026-09-28

- Selectively synthesize GitHub practices for semantic colors, typography candidates, component feedback, and old/candidate output evaluation, with pinned source revisions and adaptation boundaries.
- Add analytical-screen craft guidance for Hangul labels, chart layers, selection semantics, and honest overlap treatment without changing accepted composition.
- Add an opaque sRGB contrast helper with explicit scope and unrounded threshold checks.
- Add regression scenarios for imported palettes, selection colors, type coverage, bubble encoding, and fair candidate comparisons.

Source and package checks do not establish that the candidate produces better UI. Historical renders remain reference inputs; an independent old/candidate behavioral comparison is still pending.

## 3.1.0 — candidate — 2026-09-28

- Protect an accepted composition during visual polish; avoid repeating an already answered design interview.
- Preserve true positions in charts when handling overlapping marks.
- Treat tool preferences as task-specific choices, with no permanent skill blacklist or mandatory companion.
- Add regression prompts and rendered reference captures from the review dashboard case.
- Add versioned installation receipts, backup/rollback, local-edit protection, repository checks, and CI.

Packaging and updater tests are separate from behavioral and visual review. This candidate has not been certified by an independent behavioral run.

## 3.0.0 — baseline

Baseline GitHub commit: `a6a97fc0db584a40436ad14d77e111aed5584005`.
Includes design intent, UX heuristics, visual craft, and separate Communication/Craft verdicts. The baseline predates managed installation receipts.
