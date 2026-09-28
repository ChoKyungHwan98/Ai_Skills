# Surface polish

Use when the composition is accepted and the request is to polish, "포장", refine the look, or fix a screen that feels flat (밋밋해), dated (올드해), or cheap. The surface layer is part of the work here, not decoration: once hierarchy works, background, surfaces, type, color, data marks, details, emphasis, and motion decide whether the screen feels finished.

A vague "폴리싱해줘" must not end with one or two property changes. Cover every layer below in one pass, or state why a layer needs no change.

## 0. Settle the direction once

Look for the project's taste file (for example `design/taste.md`, or the path the project docs name). If it exists, follow it and do not ask again.

If it does not exist, recommend first: choose the direction that best fits the screen, task, and existing product choices. Then offer it once as at most three multiple-choice questions in one turn, with the recommended option marked: brightness (bright / dark / both), mood (premium and calm / soft and friendly / game-like immersion / futuristic glass), and effect intensity (subtle / pronounced). If the user says to decide (“네가 정해”), skips the questions, or cannot be asked, proceed with the recommendation; the questions never block work. Do not ask a non-designer to describe design in words. Start from the matching preset in [taste presets](taste-presets.md), then write the answers (or "recommended, not chosen") and the values into the taste file.

## 1. Audit all eight layers

Measure the rendered screen with [style inventory](../scripts/style-inventory.js) and inspect it visually. Record each layer as now → change → value.

| Layer | Controls | Check | Typical failure |
| --- | --- | --- | --- |
| 1. Canvas and light (바탕과 빛) | Page tone, ambient light, texture, translucent chrome | Tinted neutral instead of pure white; large soft glows at the edges (opacity ≤ 40%); texture barely visible (≈3%) | Flat white everywhere; borders as the only separation |
| 2. Surface and elevation (표면과 그림자) | Cards, radii, borders, shadows, elevation levels | Cards separated by gaps; one radius family (controls ≈10px, cards ≈16–18px); hairline borders (≈6% ink); 2–3 layered shadows tinted with the canvas hue, strongest layer ≤ 16%; 1px top highlight; three elevation levels (raised cards, low chips, floating tooltips) | One hard grey shadow; dividers everywhere |
| 3. Type and readability (글꼴과 가독성) | Scale, sizes, weights, line length, numerals, Hangul wrapping | ≤ 8 sizes and none under 13px; body 15–16px at line-height 1.6–1.75; Hangul body letter-spacing 0 (tighten only headings ≥ 24px); `word-break: keep-all`; paragraphs ≤ ≈72 characters; tabular numerals for columns and axes, proportional for hero numbers; section labels in secondary ink, not the faintest grey | Words split mid-word; 12px grey metadata; a dozen sizes |
| 4. Color (색감) | Hue roles, neutrals, filled controls, semantic zones | Each hue has a fill color and a darker text color (≥ 4.5:1 on its background); vivid fills defined in OKLCH with a hex fallback; neutrals tinted toward the canvas hue (three text steps plus one line color); one dark filled control per view; semantic zones the viewer relies on stay readable at a glance | Muted crimson and navy that read as dated; four black buttons; saturated color on large blocks |
| 5. Data marks (데이터 마크) | Bars, points, scale spread, ratio bars, stat tiles | Bars: vertical tonal gradient (lighter top to base hue), rounded data end (8–10px), square baseline, faint track, width capped (≈24–32px). Points sized to the plot (r ≈7 context, r ≈10 highlight on a ≈1000px plot): context points as hollow rings tinted by their zone, highlighted points solid with a white ring and a soft same-hue disc; no glossy sphere gradients. Marks should spread across the plot: when a skewed count axis crowds most marks into one side, use a labeled log scale. Ratio bars 8–12px with rounded ends; key numbers in tinted stat tiles | Flat solid fills; dots too small for the plot; most marks crammed into a quarter of the plot; glossy or skeuomorphic markers; bars filling the slot |
| 6. Details (디테일) | Keyword marks, halos, label chips, callouts, quotes, dividers | Each detail attaches to content: a marker band under key words, a soft halo on the selected mark, label chips with shadow instead of bordered boxes, fading dividers, a tinted callout for AI summaries, a quote chip | Ornaments with no meaning, such as a decorative logo square |
| 7. Emphasis contrast (강약 조절) | What is loudest | One strongest element per region; only the key bar at full strength, others one lighter step; value labels colored only for the emphasized item | Every element equally loud after polish |
| 8. Motion and response (움직임과 반응) | Entrance, hover, feedback | Bars grow on entrance (≤ 600ms, ≈60ms stagger); hovering a mark dims context marks to ≈40% but never the highlighted or selected marks and their labels; tooltip ≈160ms; hit target larger than the mark; controls lift 1px on hover; `prefers-reduced-motion` removes motion | Dimming everything, including what the viewer is reading |

Keep structure, data values, coordinates, encodings, and copy unchanged unless the user asks. The values above are defaults for a bright analytical screen; the taste file overrides them, and the project's own design rules and detectors override both. Read the project's agent instructions and design docs first. If they ban a treatment, such as colored glow shadows, thin border plus wide shadow, or gradients outside data marks, use the nearest allowed form: neutral shadows, borderless cards, or tonal data marks only. Translucent chrome with backdrop blur can defeat pixel-based contrast checks, so keep navigation chrome opaque when the project runs one. When an approved direction conflicts with a documented project rule, apply it only if the user chose it, update the rule's document in the same change, and tell the user what changed.

## 2. Write the treatment as layer instructions

State each layer as one instruction with concrete values, such as: "Data marks: vertical gradient #FF95A3 → #F43F5E, top radius 10px, square baseline, track #F1F5F9, bar width ≤ 30px, soft glow under the key bar only." This format is also what a user can paste into another tool.

## 3. Implement, measure, render

Apply all layers in one pass. Run the project's own checks (for example `npx impeccable detect`) on files and on the rendered page, and compare against the unchanged base so pre-existing findings are not mistaken for new ones. Run the style inventory before and after at the same viewport, data, and selection. Targets: minimum text size and size count from the taste file, one dark filled control per view, no low-contrast flags (resolve "unresolved" pairs by hand), no Hangul mid-word breaks, and gradient rather than flat data fills when the data-mark layer applies. Capture before and after screenshots, and check hover and entrance states live. The inventory counts; the rendered screen decides.

## 4. Report for a quick reaction

The user may not be a designer. Show before and after, list the layers in plain words, and name any technique the user may want to reuse. Ask for one reaction: 좋다 / 과하다 / 약하다, or a pointer to a region. "과하다" lowers the intensity values one step (opacity, shadow spread, saturation); "약하다" raises them. A specific complaint maps to its layer. Record accepted and rejected choices in the taste file.

## 5. Break a plateau

If a round changes only one or two layers, the before and after look like the same design, or the user says "제자리" or "별로" without specifics, stop local tweaks. Build a preview that toggles each layer on the same screen, or two or three variants that differ in visual language, and let the user choose. Choosing is easier than describing.

## 6. Answer "이거 뭐라고 해?"

When the user shows a reference and asks what makes it work, name the technique and its parameters, such as data-mark styling with a tonal gradient, rounded data end, and track. Apply the principle to the user's own palette and layout; do not copy the reference's colors, layout, or brand. Add the named technique to the taste file vocabulary.
