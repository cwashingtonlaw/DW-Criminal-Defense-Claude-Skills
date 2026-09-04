# Integration Map — Downstream and Upstream Skills

Read at the SKILL.md "Downstream Integration" and "Upstream Consumers (READS FROM)" sections of `dw-trial-narrative-builder-crim` (and at STEP 1 when pulling upstream inputs).

---

## Downstream Integration

**`dw-trial-notebook-builder-crim`** consumes the Opening Statement, Closing Argument, Theme Tracker, and Rebuttal Anticipation Memo for Phase 4 tab assembly. Specifically:

- **Tab 2 — Opening & Closing:** Opening Statement (.docx), Closing Argument (.docx), Theme Tracker (.xlsx), Rebuttal Anticipation Memo (.docx) — all four documents indexed in the trial notebook table of contents.

The Theme Tracker is the cross-reference index between trial events (witness exits, exhibit introductions) and theme reinforcement — `dw-trial-notebook-builder-crim` uses it to link Tab 2 to the mid-trial tabs (witnesses, exhibits) so the attorney can flip from a theme to the witness/exhibit that reinforced it during trial.

---

## Upstream Consumers (READS FROM)

This skill reads from the following upstream D&W skills. Pull these inputs before asking the attorney:

- **`dw-case-brain-crim`** — defendant identity, charges, docket, court, parish, CASE_ROOT, theory of defense
- **`dw-issue-code-tracker-crim`** — defense's coded issues, used as theme spine candidates
- **`dw-witness-threat-matrix-crim`** — which prosecution witnesses are weakest and worth foreshadowing in opening; which are strongest and need pre-emption
- **`dw-timeline-builder-crim`** — defense timeline, used as the chronological backbone of the opening's story-arc
- **`Case Tables.xlsx` Evidence Table** — Evidence Number, Evidence Name, and Authentication Route / Anticipated Objections (for opening foreshadowing and closing callback)
- **`dw-jury-instructions-builder-crim`** — reasonable-doubt instruction (Cage-compliant), responsive verdict chart, affirmative-defense burden — the closing must mirror these instructions verbatim

If any of these upstream skills have not been run for this case, recommend they be run first:
> *"I recommend running [skill] before drafting the [opening/closing], because [reason]. Want me to flag it?"*

---
