# dw-criminal-defense — Changelog

## v5.8 (May 2026)

Asset/reference categorization cleanup — one file moved, no behavioral change.

- **`Evidence_Placeholder_Template.md` moved from `assets/` to `references/`.** The skill-creator rubric defines `assets/` as files used *in* the deliverable (templates, icons, fonts) and `references/` as docs Claude loads into context. The Evidence Placeholder template is a layout *specification* — the actual PDF is generated programmatically by `scripts/generate_placeholders.py`, and the script's layout is hardcoded, not read from the .md file at runtime. The file's only function is as a human-readable spec for Claude (and future maintainers) to understand the expected output format. That makes it a reference, not an asset. SKILL.md updated in two places: the bundled-resources tree (top of file) and the Phase 1 Step 2f inline path.
- **`assets/` is now correctly limited to the two true templates** (`CASE PROFILE.docx` and `Case Tables.xlsx`) — both of which are copied into the case folder and become the working deliverables.

## v5.7 (May 2026)

Closes the v5.5 follow-up backlog — three coordinated changes to `references/case-profile-procedure.md` and `assets/CASE PROFILE.docx`.

- **High Priority Next Steps → Status column added.** Table grew from 5 columns to 6: Step / Why High Priority / Owner / Routing / Target Date / **Status** (Open / In-Progress / Done). Done rows stay in the table; the table is now self-contained as the audit trail for completed actions. The previous "move completed steps to a Case Brain Completed log" instruction is gone — it referenced an artifact that was never specced in `dw-case-brain`. The simpler in-table audit trail is the system of record. Column widths rebalanced to fit Status without forcing the Step column to wrap.
- **Sourcing notes added for the new Defendant fields** (introduced in v5.5). Place of Birth and Race/Sex → booking record or NCIC/RAP sheet. Physical Description → booking record or incident report narrative (height, weight, build, distinguishing marks, tattoos, scars). Immigration Status → client interview, jail intake screening sheet, or any ICE detainer or A-file reference in discovery. Added a routing breadcrumb: non-citizen clients route plea analysis to **dw-plea-negotiation-analyzer** with the immigration impact noted. The note paragraph appears in both the procedure file and the .docx between the Defendant fields table and the Complaining Witness / Victim sub-block.
- **Section 6 Key Dates ↔ Timeline Sheet boundary clarified.** Section 6 Key Dates is now explicitly scoped as the attorney's *procedural* calendar (court dates, deadlines, motion filing dates). The comprehensive *evidentiary* timeline (every event, every source, conflict-flagged) lives in `Case Tables.xlsx — Timeline Sheet`, populated in Phase 3 Step 1. Different audiences, different lifecycles. The two are explicitly **not** to be synced. Boundary statement added in both the procedure file and the .docx Key Dates note.

## v5.6 (May 2026)
- **Section 2 (Charges & Exposure) restructured into per-charge table** in `references/case-profile-procedure.md`. Was six fields in single cells, which forced multi-count cases into comma-separated jumbles in one box and hid per-count enhancement analysis. Now organized into two sub-blocks under the existing Section 2 banner:
  - **Charges (per count)** — 6-column table (Count / La. Statute / Max Penalty / Mandatory Min / Elements / Responsive Verdicts) with one row per count, matching the Bill of Information / Indictment numbering. Per-count firearm / drug-free-zone / hate-crime sentence enhancements go in the Max Penalty cell so per-count exposure is calculable on its face. "Mandatory Min" requires explicit "None" rather than blank to distinguish absence from unchecked.
  - **Habitual Offender Exposure** — single full-width narrative cell for the cross-cutting La. R.S. 15:529.1 analysis (predicate convictions, enhancement multiplier per affected count, cleansing-period and Boykin / R.S. 15:530.7 challenges, strategic question). Routes to **dw-habitual-offender-auditor**.
- **`assets/CASE PROFILE.docx` template updated to match.** Section 2's six 2-column label/value rows replaced with the 6-column charges table (5 starter rows, sized for Calibri 11pt bold headers without wrap on "Count") plus the bordered narrative box for habitual analysis. Sub-headers in red bold matching v5.5 firm style. Sections 1, 3, 4, 5, 6 and Part 2A/2B/2C unchanged.
- **No procedure-file impact on the Generation Procedure (XML Edit) section.** The new charges table uses the Step 2B multi-row pattern documented in v5.5; the habitual narrative cell uses the Step 2A label/value pattern (cell content is `<w:p/>` to fill).

## v5.5 (May 2026)
- **Generation Procedure (XML Edit) restructured** in `references/case-profile-procedure.md` to support both editing patterns: Step 2A covers the existing label-find-and-fill pattern for 2-column label/value tables (now including the new Defendant, Complaining Witness / Victim, Court & Case Numbers, and Personnel sub-blocks); Step 2B *(new)* covers the multi-row data tables (Seized Property / Devices, Key Dates, High Priority Next Steps) with anchor-and-walk table location, empty-starter-row fill as the preferred path, and `<w:tr>` clone-and-append for overflow. Refresh-Mode append-only rule documented for Step 2B tables.
- **Section 1 (Case Identification) expanded** in `references/case-profile-procedure.md`. Section 1 is now organized into five named sub-blocks instead of a flat bullet list:
  - **Defendant** — added Place of Birth, Race/Sex, Physical Description, and Immigration Status alongside the existing Name, DOB, SS#, Address, Phone, Email.
  - **Complaining Witness / Victim** *(new)* — Name, DOB, Race/Sex, Address. Populates from the charging instrument and police report; multi-victim cases list each. Minor-victim redaction note included.
  - **Court & Case Numbers** — unchanged content (Docket #, Court, Division, Judge, Date of Offense / Arrest / Hire, Co-Defendant(s)); regrouped under its own header for readability.
  - **Investigative / Prosecution Personnel** *(new)* — 10-row table per the firm's CASE PROFILE.docx layout: Case Detective, Assisting Detective, First Responder, Evidence Collection, SANE Nurse, Victim Advocate, Interpreter, Crime Lab Analyst, Issuing Judge (warrants), Prosecuting ADA. Sourcing notes added for each row.
  - **Seized Property / Devices** *(new)* — 7-column table (Item / Owner / Seized From / Date Seized / Warrant # / Bate / Extraction Status / Notes) for every phone, tablet, computer, USB, vehicle, weapon, document, or currency taken from the client, scene, or co-defendant. Drives early routing to **dw-mobile-forensic-auditor** and **dw-forensic-dump-analyzer**. Suppression trigger added: any item appearing in discovery without a warrant, consent, or arrest-incident inventory entry → flag in red and route to **dw-suppression-motion**.
- **Section 6 (Key Dates & Next Steps) restructured** into two sub-blocks. The section name finally matches its content:
  - **Key Dates** *(new format)* — replaced four flat bullets with a 3-column table (Date / Event Description / Source). Capture both past and upcoming events. Captures expanded list including 72-hour hearing, bond hearings, each discovery production, motion deadlines, pretrial conference, Art. 701 release date, statute-of-limitations expiration (La. C.Cr.P. art. 571–576), and habitual offender bill filing deadlines. Calculated dates state the calculation in the Source cell.
  - **High Priority Next Steps** *(new)* — Cowork-prepopulated, attorney-finalized 5-column table (Step / Why High Priority / Owner / Routing / Target Date) of the highest-priority next actions. Routing column points to specialist skills (suppression, bond reduction, pretrial motion library, investigator tasking, forensic dump analyzer, etc.). Cowork proposes High/Medium/Low ranking; attorney finalizes. Completed steps move to Case Brain "Completed" log rather than being deleted.
- **Section count preserved at six.** All cross-references to "Part 1 Section 2–6" elsewhere in this skill, in `lwop-field-maps.md`, and in SKILL.md remain valid.
- **`assets/CASE PROFILE.docx` template updated to match the procedure spec.** New defendant fields (Place of Birth, Race/Sex, Physical Description, Immigration Status) added; new Complaining Witness / Victim block added; new Investigative / Prosecution Personnel 10-row table added; new Seized Property / Devices 7-column table (Item / Owner / Seized From / Date Seized / Warrant # or Bate / Extraction Status / Notes) with 6 starter empty rows added, plus the suppression-trigger note paragraph in red italic; Section 6 restructured with the 3-column Key Dates table (10 starter rows) and the 5-column High Priority Next Steps table (8 starter rows). Sub-headers rendered in red bold matching the firm's existing "Investigative / Prosecution Personnel" header style. Sections 2–5, Part 2A, Part 2B, and Part 2C are untouched. Multi-column tables include light-gray cell borders so empty data rows are visible during data entry.

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
