# Maintaining Ai_Skills

This GitHub repository is the source of truth. Develop here and install a committed snapshot; installed copies are deployment outputs. Preserve existing local edits and keep changes to unrelated projects out of this repository.

For skill changes:

- Read the skill and only the references relevant to the requested change. Keep the entrypoint compact.
- Preserve the user's chosen scope, representations, and design direction. Tool preferences belong to their task or explicitly stated project scope; do not encode permanent bans or mandatory external skills from a single example.
- Turn a demonstrated failure into a focused scenario in `evals/evals.json`. Add rendered artifacts when visual judgment needs them, with capture context and provenance. Do not publish private artifacts without authorization.
- Run `python scripts/check_skills.py` and `python -m unittest discover -s tests -v`. These validate packaging and deployment behavior, not visual quality.
- For a changed visual decision, inspect real rendered output. Record Communication and Craft separately with the rubric. Descriptions and source checks cannot establish a visual PASS.
- Update the skill metadata version, `releases.json`, and `CHANGELOG.md` together. Set changed versions to `candidate`; promote to `stable` only after relevant behavioral evidence has been reviewed and recorded. Do not substitute CI success for behavioral review.
- Use a branch and pull request for GitHub changes. Installing a candidate locally does not authorize merging or releasing it. Publishing, messaging, or scheduled work requires authorization within the current task.

Operational commands and the improvement loop are documented in `docs/maintenance.md`. Use `scripts/manage_skills.py` for managed updates; it backs up the existing installation and refuses to overwrite changed managed files.
