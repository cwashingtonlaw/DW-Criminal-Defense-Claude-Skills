# dw-criminal-defense-crim — v5.11 (full skill, template updated)

Repo-root overlay for the dw-core plugin repo. Extract at the repo root so these merge:
  skills/dw-criminal-defense-crim/     ← complete updated skill (incl. updated assets/CASE PROFILE.docx)
  .claude-plugin/plugin.json           ← version bumped 1.0.0 → 1.1.0

  git add skills/dw-criminal-defense-crim .claude-plugin/plugin.json
  git commit -m "dw-criminal-defense-crim v5.11 (+ CASE PROFILE.docx template) + bump dw-core to 1.1.0"
  git push

v5.11 template changes baked into assets/CASE PROFILE.docx:
- NEW Section 1 — Prosecution's Theory of the Case (banner + red note + 5 sub-heads)
- Part 1 banners renumbered 2–11 (Part 2A/2B/2C untouched)
- Seized Property / Devices table rebuilt at 9 columns (adds Evidence ID / PR# and Owner Basis)
Plus all reference/SKILL.md/CHANGELOG changes from v5.11.
