# dw-criminal-defense — Changelog

## v5.4 (May 2026)
- **Major refactor:** SKILL.md reduced from 844 lines to a slim workflow spine following the `dw-forensic-dump-analyzer` structural model.
- **NEW reference files:**
  - `references/case-tables-write-protocol.md` — extracted from SKILL.md
  - `references/case-profile-procedure.md` — extracted Phase 1 Step 3 detailed procedure (operating modes, Part 1/2A/2B/2C field detail, LWOP population workflow, Refresh Mode merge rules, XML edit procedure)
  - `references/defense-shield-procedure.md` — extracted Phase 3 Step 3 detailed procedure
  - `references/quick-reference.md` — Cowork action types, Case Tables sheet reference, phase quick map, specialist skill routing table
- **Linked previously orphaned references:** `color-coding.md` and `folder-structure-and-naming.md` are now properly pointed to from SKILL.md.
- **DELETED orphaned references:** `case-tables-sheet-reference.md` (outdated duplicate of Quick Reference) and `textexpander-snippets.md` (content lives in `dw-shared-protocols`).
- **DELETED `scripts/master-trial-advocate-playbook.md`:** stale (referenced 9 reports; current count is 8 since v5.2) and never integrated into the workflow.
- **DELETED `assets/legacy/`:** archived Calcasieu PDO standalone LWOP forms (`LWOP Homicide Review Sheet - FOR TYPING.docx`, `LWOP Sex Offense Review Sheet - FOR TYPING.docx`) removed. The merge into Part 2A/2B of `000 - Case Profile.docx` is recorded in the v5.3 changelog entry below; originals are preserved in firm template archives and GitHub history.
- **Fixed stale skill reference:** Phase 1 Step 2e now correctly routes to `dw-transcript-router` (parish-based pipeline selection). The original referenced a non-existent `casedev:transcription` skill.
- **Changelog moved** from the bottom of SKILL.md to this file.
- **No functional/workflow changes** — this is a structural refactor only. All procedures, field schemas, and routing rules preserved.

## v5.3 (April 2026)
- **MERGED:** `dw-lwop-populator` is now part of this skill. The standalone populator skill has been retired.
- **NEW reference files:** `references/lwop-field-maps.md` and `references/lwop-extraction-patterns.md` (both moved from the populator's `references/` folder).
- **NEW assets/legacy/ folder:** archives the two original Calcasieu PDO standalone templates (`LWOP Homicide Review Sheet - FOR TYPING.docx`, `LWOP Sex Offense Review Sheet - FOR TYPING.docx`) for reference. They are no longer used as the output substrate.
- **Phase 1 Step 3 expanded:** absorbs the populator's full workflow — extraction priority order, source-priority rules, formatting conventions, attorney-only field handling, field-completeness checklist, completion notes.
- **NEW: Refresh Mode** added as a sub-mode of Phase 1 Step 3. Handles late-discovery updates that previously triggered standalone populator runs. Strict merge rules preserve all attorney-entered content; Refresh Log entry appended to the document on each refresh.
- **Trigger phrases added** to skill description: "fill out the LWOP sheet," "LWOP review," "District Defender review," "life without parole worksheet," "refresh the Case Profile."
- **Documentation patch** for Part 1 Section 5 (Prior Criminal History): explicit format guidance for LWOP cases (`MM-DD-YYYY — Offense Name (Disposition)`) vs. non-LWOP narrative form.
- **HIPAA spelling normalized** throughout (legacy templates retained "HIPPA" typo; v5.3 references and unified template use "HIPAA").

## v5.2 (April 2026)
- Consolidated former Initial Case Profile, Criminal Defense Cover, and standalone LWOP review sheet into single `000 - Case Profile.docx` with Part 1 + Part 2A/2B/2C.
- Report 8 (Witness Table) removed — witness data is captured in `Case Tables.xlsx` during Phase 1 Step 4.
- Former Report 9 renumbered to Report 8.
- Bundled resources: 8 report prompt templates, output path convention, `Case Tables.xlsx` master template, Evidence Placeholder template, `generate_placeholders.py` script.
