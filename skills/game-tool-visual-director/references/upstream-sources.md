# Selected upstream practices

Reviewed 2026-09-28. The references are an original synthesis for analytical game-planning interfaces. No upstream skill entrypoint, dataset, script, or CLI is bundled or automatically invoked. Source commits are pinned below so later upstream changes can be evaluated deliberately.

| Source / inspected revision | Selected contribution | Adaptation boundary |
| --- | --- | --- |
| [Impeccable Colorize](https://github.com/pbakaus/impeccable/blob/9d715cc4f5564a990ca8345abfdd5df6dc9b41c8/skill/reference/colorize.md) — Apache-2.0 | Color roles, existing direction, computed contrast, non-color cues | Applied to data semantics; no fixed tint, palette, workflow handoff, or mandatory Impeccable invocation |
| [UI UX Pro Max skill guidance](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/09170eec67eefd46a7ae85de61b40c194020f997/src/ui-ux-pro-max/templates/base/skill-content.md) — MIT | Palette/type candidates, density, shared system with contextual variations | Preserve the game's tool identity and accepted composition; no automatic product-category theme or dependency on its search engine |
| [UI UX Pro Max color catalog](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/09170eec67eefd46a7ae85de61b40c194020f997/src/ui-ux-pro-max/data/colors.csv) and [type catalog](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/09170eec67eefd46a7ae85de61b40c194020f997/src/ui-ux-pro-max/data/typography.csv) — MIT | Examples organized by roles and use context | Reference lookup when candidates are needed; data is not copied. Check Korean glyphs and actual computed contrast independently |
| [Emil Design Engineering](https://github.com/emilkowalski/skills/blob/d16ebe60d09a5ba2afcb7054ede9d0a10c9f6128/skills/emil-design-eng/SKILL.md) — MIT | Component states, responsive feedback, purpose and frequency of motion | Apply only when interactions change; no mandatory animation, press scaling, review format, or blanket implementation rule |
| [Anthropic Skill Creator](https://github.com/anthropics/skills/blob/33375500bcea98d610eb30ce10ac4e59b89c390d/skills/skill-creator/SKILL.md) — [skill-specific Apache-2.0](https://github.com/anthropics/skills/blob/33375500bcea98d610eb30ce10ac4e59b89c390d/skills/skill-creator/LICENSE.txt) | Old/candidate output comparison, optional blind review, actionable feedback | Adapted to available Codex tools; no assumed Claude CLI, mandatory parallel agents, or automatic behavioral PASS |

## Standards used for measured color checks

- [W3C contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): text thresholds, unrounded comparison, underlying colors rather than antialiased screenshot pixels.
- [W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html): essential graphical and control information against adjacent colors, with the criterion's exceptions.
- [W3C relative luminance](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance): the opaque sRGB calculation used in the original `scripts/contrast.py` helper.

When maintaining these references, inspect the specific changed upstream files before updating the pinned revision. Preserve attribution. Any future vendoring requires carrying the applicable license and notices; this integration retains ideas in newly written guidance rather than reproducing upstream packages.
