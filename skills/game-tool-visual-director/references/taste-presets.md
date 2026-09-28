# Taste presets and the project taste file

A taste file records the direction a user chose, so later polish passes converge on the same target instead of restarting. Keep it in the project, not in this skill. A preset is a starting point for one combination of direction answers; the project's existing tokens and the user's reactions override it.

## Taste file template

```markdown
# Taste

Direction: <brightness> · <mood> · <intensity>   (chosen <date>)
Protected: <structure, charts, copy, or colors the user wants kept>

## Values
Canvas and light:
Surface and elevation:
Type and readability:
Color (fill / text per hue, neutrals):
Data marks:
Details:
Emphasis:
Motion:

## Reactions
- <date> 좋다 / 과하다 / 약하다: <layer or region> → <what changed>

## Vocabulary
- <named technique>: <what it means here>
```

## Preset: bright · premium and calm · subtle (밝게 · 고급스럽고 차분하게 · 은은하게)

Reviewed on the review-dashboard mockup in `evals/cases/surface-polish` (see its case file for reactions and limits). Values are for a light analytical desktop screen.

| Layer | Values |
| --- | --- |
| Canvas and light | Canvas #F5F6F8; white glow top-left (900×520px, fading to 0 by 65%); cool violet-blue glow top-right `rgba(206,216,255,.42)`; faint lavender glow bottom `rgba(236,228,255,.35)`; fractal noise at ≈3% multiply; sidebar `rgba(255,255,255,.55)` with 14px backdrop blur and a 6% ink hairline; no rule under the top bar. Where a pixel-based contrast detector runs, keep the sidebar and top bar opaque |
| Surface and elevation | Cards 20px apart, radius 18px, border `rgba(15,23,42,.06)`; shadow `inset 0 1px 0 rgba(255,255,255,.9), 0 1px 1px rgba(40,52,110,.035), 0 3px 8px rgba(40,52,110,.035), 0 24px 48px -24px rgba(40,52,110,.16)`. Use neutral `rgba(15,23,42,…)` at a strongest layer of 14% where colored shadows are flagged, and drop the border when the project bans thin borders with wide shadows; controls radius 10px with a 1px, 5% shadow; primary button gradient #2B3342 → #121826 with a 14% white top highlight; no dividers inside cards, spacing instead |
| Type and readability | Hangul: Pretendard or Noto Sans KR; numerals: Manrope. Sizes 13 · 14 · 15 · 16 · 18 · 24 · 36 · 44px only. Headline 36px/700, letter-spacing −2.5%; panel title 24px; hero numbers 44px, proportional figures. Body 16px, line-height 1.6, letter-spacing 0; summaries ≤ 72 characters wide; `word-break: keep-all`; section labels 13px/600 in #475569 |
| Color | Neutrals #0F172A (text), #475569 (secondary), #64748B (muted), #E2E8F0 (line). Fix/negative: fill #F43F5E (`oklch(64.5% .246 16.4)`), text #E11D48, text on its tint #BE123C, tint #FFF1F3. Keep/positive: fill #4263EB (`oklch(55% .215 268)`), text #3B5BDB, tint #EEF2FF. One dark filled button per view; search button #F1F5F9; selected tab as a white chip. Quadrant zones visibly tinted: rose 13% → 7% and blue 12% → 6% diagonal gradients, neutral columns #F6F8FB |
| Data marks | Key bar gradient #FF95A3 → #F43F5E → #E8354F, top radius 8–10px, square baseline, width ≤ 30px, track #F1F5F9, glow `0 10px 22px -8px` at 75% of the hue, omitted where colored glows are banned; other bars one step lighter (#FFC9D1 → #FB9AA8) without glow. Ratio bar 10px, rounded, horizontal gradient. Scatter context points r 7px as hollow rings (white fill, 2.5px stroke: #F7849A in complaint-dominant zones, #8A9FF8 in praise-dominant zones); highlighted points r 10px solid with a 3px white ring over a same-hue 12% disc (r 24px), plus a 55% ring at r 16.5px when selected; no glossy sphere gradients. Mention-count x-axis on a log scale (ticks 20 · 40 · 80 · 160, labeled 로그 눈금); label chips flip to the left near the right edge. Key counts as two tinted stat tiles |
| Details | Marker band behind headline keywords (lower third, hue at 13–14%); soft halo r ≈40px behind highlighted points; white label chips (radius 12px, soft shadow) with a colored dot and ink text; fading dividers in panels; AI summary in a violet-blue tinted callout with ✦; quote chip with a large, faint opening mark. No decorative logo marks |
| Emphasis | Only the key bar and its value in full color; everything else one step quieter |
| Motion | Bars grow 0.6s `cubic-bezier(.2,.8,.2,1)`, 60ms stagger; hover dims context marks to 40%, never highlighted marks or labels; dark tooltip after 160ms; buttons lift 1px; all motion off under `prefers-reduced-motion` |

## Other starting points (not yet reviewed)

Confirm these with a layer-toggle preview before recording them.

- **Dark · game-like immersion:** canvas #0D1117 with a faint top glow, surfaces separated by lightness rather than borders, vivid fills that keep ≥ 4.5:1 text steps on the dark surface, restrained halos on highlighted marks, and numerals in a display face.
- **Bright · soft and friendly:** canvas #F2F4F6, white cards with radius ≈20px and wide soft shadows, large numbers, a single saturated blue accent, and generous spacing.
- **Futuristic glass:** translucent surfaces with backdrop blur over a gently colored canvas, 1px light borders, and cool gradients. Check contrast on the composed background, never the nominal one.
