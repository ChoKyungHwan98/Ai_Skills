# Inspect the delivered medium

Use only the checks relevant to the artifact and changed decisions. Compare before/after in a matched state when claiming improvement.

| Medium | Inspect the result in context | Common false pass |
| --- | --- | --- |
| Software tool or website | Render at the target viewport and at materially different widths; inspect the primary task, navigation, important states, and affected interactions. For data views, verify labels, units, encodings, and selected state. | A static hero screenshot hides overflow, focus, loading, or distorted chart meaning. |
| Presentation | Render every changed slide, scan the full deck as thumbnails for rhythm, then inspect dense slides at presentation size. Check role of each slide, text legibility, alignment, overflow, imagery, and chart labels. | A PPTX file opens but text substitutes, a chart is tiny, or each slide looks polished alone while the story has no emphasis. |
| Document, report, or printable visual | Render pages at the intended size. Check reading order, headings, page breaks, contrast, tables, citations, and whether key information survives print or export. | Source markup looks correct while pagination or print scaling breaks the composition. |
| Image or static graphic | Inspect at actual delivery dimensions and likely crop; check focal point, text if any, visual balance, and safe areas. | A full-size preview looks fine but the thumbnail or crop loses the subject. |

Record **communication** and **craft** separately as PASS, NEEDS REVISION, or NOT VERIFIED, with a visible reason. Automated tests can support technical correctness but do not replace looking at the output.
