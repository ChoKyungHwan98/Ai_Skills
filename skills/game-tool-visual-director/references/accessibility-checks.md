# Accessibility and production quality checks

Use the relevant checks when a redesign affects controls, meaning, data views, or responsive layout. This guards the changed screen's quality; it is not a full accessibility audit or a universal component checklist.

## Interaction and state

- Are selected, hover, pressed, and disabled states distinguishable and consistent where they exist?
- Do loading, error, and empty states explain what is happening and what the viewer can do next?
- Do ambiguous controls have understandable labels or help, and do controls behave as their appearance suggests?
- Can interactive charts, canvases, or controls be focused and selected through relevant input methods, including keyboard use when applicable?

## Responsive information

- When panels stack, does the first-glance target still precede its supporting context and next action?
- Are overflow, long labels, and dense tables handled without silently hiding important values?
- Do charts remain readable at the target narrow viewport, or change representation while preserving the analytical question?
- Is the visual reading order still logical in navigation and focus order?

## Data, color, and motion

- Do numeric values align for comparison, and are labels and long text legible without an inconsistent type hierarchy?
- Does color have stable semantic meaning, with important states distinguishable without color alone?
- When chart meaning or exact values would otherwise be lost, is a useful text summary or table available?
- Does motion communicate a state change or relationship? Remove decorative motion that delays repeated professional work.

Check only what the change can affect. Use platform and accessibility standards when a numerical threshold is actually needed; do not invent a universal value here. A screenshot cannot prove keyboard, assistive-technology, or motion behavior. Inspect the live interaction or code when relevant and mark unverified behavior honestly.
