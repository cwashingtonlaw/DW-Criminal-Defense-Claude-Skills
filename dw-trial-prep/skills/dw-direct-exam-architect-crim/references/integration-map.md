# Integration Map — Upstream Consumers and Downstream Feeds

Read at SKILL.md "Integration" section (after the Quick Reference): downstream trial-notebook integration, upstream products this skill reads, and the Reads-from / Feeds-to list.

---

## Downstream Integration

`dw-trial-notebook-builder-crim` consumes the Direct-Examination Outlines produced by this skill as part of Phase 4 trial tab assembly. The outline `.docx` files in `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Defense Witnesses/` are indexed into the trial notebook's Defense Witnesses tab. The Cowork Analysis summary copies are indexed into the Case Analysis tab. Do not rename or move outline files after generation — `dw-trial-notebook-builder-crim` relies on the canonical filenames and paths.

## Upstream Consumers — This Skill Reads From

- **`dw-witness-statement-analyzer-crim`** — defense-favorable Witness Analysis Cards (key facts, vagueness flags, defense utility assessment for non-defendant defense witnesses)
- **`dw-expert-witness-evaluator-crim`** — defense expert vetting, Daubert-survival prep, qualifications/methodology audit, prior testimony record
- **`dw-case-brain-crim`** — defense theory, charges, parties, case theme, CASE_ROOT
- **`dw-timeline-builder-crim`** — alibi corroboration timeline; defense narrative sequencing; cross-witness time anchors
- **`dw-exhibit-manager-crim`** — exhibit numbers, Bates references, authentication status for sponsored exhibits

If any of these upstream products is missing or stale, prompt the attorney to refresh before drafting.

---

## Reads from / Feeds to

**Reads from:**
- `dw-shared-protocols-crim` (work product marking, output path formula)
- `dw-case-brain-crim` (CASE_ROOT, parties, theme, theory)
- `dw-witness-statement-analyzer-crim` (defense-favorable Analysis Cards)
- `dw-expert-witness-evaluator-crim` (Daubert-survival prep for defense experts)
- `dw-timeline-builder-crim` (alibi/corroboration timeline)
- `dw-exhibit-manager-crim` (exhibit metadata)

**Feeds to:**
- `dw-trial-notebook-builder-crim` (Phase 4 Defense Witnesses tab assembly)
- `dw-jury-instructions-builder-crim` (defense-theory-driven instruction requests anchored on direct testimony)
- `dw-trial-narrative-builder-crim` (closing argument integration — defense witness propositions become closing themes)
