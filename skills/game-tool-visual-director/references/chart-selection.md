# Chart selection

Use this reference when deciding whether an existing chart earns its space or which representation answers a new analytical question.

## Start with the question

State the viewer's question in one sentence. Identify the task: compare, rank, show change, show distribution, relate variables, locate a pattern, inspect exact values, or communicate one status. If the question is unclear, fix the framing before picking a chart.

| Analytical question | Strong starting representation | Watch for |
| --- | --- | --- |
| Which option is largest or best? | Ranked horizontal bars; dot plot for compact comparisons | Sorting, consistent baseline, long labels, meaningful differences |
| How far above or below a target? | Diverging bars or dot plot with reference line | Explicit target and signed units |
| How has a measure changed? | Line chart; small multiples for several series | Time interval, missing periods, smoothing that hides volatility |
| Where are values concentrated? | Histogram; box or dot plot when individual values matter | Bin choice, sample size, outliers |
| Are two measures related? | Scatter plot | Sufficient points, useful axes, overplotting, correlation claims |
| How do parts contribute to a whole? | Sorted bars, stacked bars, or a simple part-to-whole display | Whether shares sum to the same whole and precise comparison is needed |
| Which combinations are high or low? | Heatmap or matrix | Comparable scale, legible cells, accessible legend |
| Which items meet two thresholds? | Quadrant only when thresholds have real meaning; show the measures and topic count per zone when useful. A project may call its documented mention-volume × dissatisfaction view an IPA matrix; preserve its defined axes and zone names. | Arbitrary lines, misleading names, or claiming mention frequency is measured importance without explaining that proxy |
| What exact values or many attributes matter? | Table with sorting, highlighting, or in-cell bars | Scanability, units, sticky labels, overflow |
| What is the current state or single recommendation? | KPI, text plus number, annotation, or no chart | Missing comparison, context, or uncertainty |
| How do small groups differ on the same measure? | Small multiples | Shared scales and consistent ordering |

A donut can work for a few meaningful parts of one whole when approximate share is enough. Use bars or a table if people must compare similar slices precisely. Cards are containers, not evidence; a card is useful only when it establishes a meaningful unit or interaction.

## Reject common misuses

- **Scatter plot:** Do not use it for a handful of named options when the task is simply ranking them. Use it when the position on both quantitative axes matters; label meaningful outliers directly.
- **Donut:** Do not use it for many slices, similar slices that require precise comparison, or values that are not parts of one whole.
- **Quadrant:** Do not draw crosshairs at arbitrary midpoints or assign strategic labels without defensible thresholds. If no threshold changes the decision, a scatter plot or ordered table may be clearer.
- **No chart:** Use a concise statement, KPI with context, annotated number, or table when there is no meaningful pattern to encode visually. Do not add a chart merely to make the screen look analytical.

Prefer direct labels over repeated legend lookups when labels fit. Use annotations for the few data points or thresholds that explain the conclusion; avoid annotating every mark.

## Keep the representation honest

- Define the measure, unit, population, time window, and source when these affect interpretation.
- Show a comparison, threshold, or prior value when a standalone number cannot support the intended conclusion.
- Keep bar baselines at zero. If another scale is necessary for a non-bar chart, label it clearly and check for exaggerated differences.
- Use consistent scales in small multiples when visual comparison is the purpose.
- Distinguish zero, missing, unavailable, and filtered-out values.
- Show uncertainty and sample size when they materially affect a recommendation.
- Do not imply causation from a scatter plot or trend from two isolated points.
- Put the takeaway next to the data that supports it; label important points directly when possible.

## Game and planning tool examples

- Choosing a build from several candidates: ranked bars for one weighted score, a dot plot for multiple comparable metrics, or a table when tradeoffs and exact values matter.
- Evaluating a balance change: diverging bars for before/after deltas across roles, with a threshold or confidence marker if relevant.
- Finding bottlenecks in a progression plan: a timeline or ordered table with annotated dependencies; a scatter plot is useful only if the relationship between two quantitative variables is the question.
- Inspecting portfolio allocation: bars for precise allocation comparison, a trend for exposure over time, and a table for holdings or exact figures.
- Reviewing AI output quality: status plus cited evidence and a list of issues; do not invent a score chart when no defensible metric exists.
