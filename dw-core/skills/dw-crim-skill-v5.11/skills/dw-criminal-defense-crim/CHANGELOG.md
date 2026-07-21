# dw-criminal-defense-crim — Changelog

## v5.11 (July 2026) — Prosecution Theory, Art. 814 auto-verdicts, JusticeWorks ingest

Refocuses the Case Profile as a defense document built against a sourced statement of the State's case, and hardens the Charges section so responsive verdicts are emitted from statute rather than reconstructed from memory. Drafted from lessons learned on *State v. Harrison* (14780-25). Affects `references/case-profile-procedure.md`, `SKILL.md` (Step 3 spine and checks), and adds one reference file. `assets/CASE PROFILE.docx` template still needs the new § 1 prose block and the two new Seized Property columns added on first generation — see the migration note below.

- **NEW Part 1 Section 1 — Prosecution's Theory of the Case.** A 1–3 page, discovery-cited defense-authored synopsis of the State's case (charge & forum, the State's narrative, theory of guilt, key proof, apparent weak points). Every factual assertion carries a `[DOC ###]`/Bates cite; no unsupported inference; attribution not adoption; adverse and favorable facts both named. Rebuilt only on explicit instruction or a materially new production; never overwrites attorney edits. **All prior Part 1 sections shift +1** — Case Identification is now § 2 … Key Dates & Next Steps is now § 11.

- **REVISED § 4 Charges & Exposure — Responsive Verdicts auto-generated.** The Responsive Verdicts cell is now emitted verbatim from the new `references/art814-responsive-verdict-map.md`, matched to the billed offense **by offense name** and reproduced in statutory order (with the ¶ C evidence-sufficiency, ¶ D value-ceiling, and ¶ B(2) CDS-weight footnotes). Fixes an earlier bad seed that wrongly listed **negligent homicide** as responsive to **first degree murder** — art. 814(A)(1) does not include it; negligent homicide is responsive to second degree murder (A)(3) and manslaughter (A)(5). Verified against the firm's source statute PDF for offenses (A)(1)–(23), including all homicide anchors.

- **NEW reference file — `references/art814-responsive-verdict-map.md`.** All 71 art. 814(A) enumerated offenses with verbatim verdict sets and an R.S. crosswalk (convenience only). Carries the KeyCite red flag for 2026 Act 103 (H.B. 92) as a `[VERIFY]` before trial reliance.

- **REVISED § 2 Seized Property / Devices table (7 → 9 columns).** Adds **Evidence ID / PR#** (the agency's own property/voucher identifier, cited verbatim; `NONE ON RECEIPT` routes to `dw-chain-of-custody-auditor-crim`) and **Owner Basis** (warrant-tied owner attribution with source doc; inference marked `[VERIFY]`).

- **NEW input source — JusticeWorks / DefenderData "Case File Detail" export.** Structured ingest mapped to §§ 2, 5, 6, 9 (Case ID, Bail/Bond, Arraignment, Court Appearance Log, Plea Log, contacts). Authoritative for administrative fields; conflicts reconciled and flagged in red, not silently overwritten. Event notes scanned for conflict-of-interest and theory flags → surfaced to § 11.

- **RESTATED § 6 Court Appearance Log and § 9 Plea Discussions Log** as fixed-schema, dated, append-only tables — seeded from the DefenderData export, thereafter append-only (history is never edited; a superseding entry is a new dated row).

- **NEW closing block — VERIFY / [ATTORNEY] Roll-Up.** After population, every `[VERIFY]` tag and blank `[ATTORNEY]` field is collected into a two-part punch-list with an `OPEN ITEMS: N to verify · M awaiting attorney` count; highest-stakes items cross-listed to § 11 High Priority Next Steps. Replaces the ad hoc completion-notes free text.

- **NEW generation step 2C — position-based section auto-renumbering pass.** Renumbers Part 1 section banners sequentially by document order regardless of banner cell count (1-, 2-, or 6-cell merged headers), resetting at each Part boundary. Idempotent; runs in both Initial Generation and Refresh Mode. Prevents the duplicate/gapped-number failures that follow section insertion or reorder.

- **Template updated.** The `assets/CASE PROFILE.docx` template now carries the v5.11 structure natively: the new § 1 Prosecution's Theory of the Case block (dark banner, red "not an admission" note, five bolded sub-heads), all Part 1 banners renumbered 2–11 (Part 2A/2B/2C banners untouched), and the Seized Property / Devices table rebuilt at 9 columns (Evidence ID / PR# after Item, Owner Basis after Owner). No first-generation column/section surgery is required. Build hygiene: write to a fresh temp filename, validate, then delete-and-replace the live file (and close it in Word first) to avoid the stale-cache revert.

## v5.9 (May 2026) — Barone Discovery Workflow Audit

Integrates the 9-step Barone Discovery Workflow into Phase 2 and revises Report 4 to support competing-theory analysis. Four new skills come online; five existing skills receive cross-cutting enhancements; one new shared protocol governs evidence verification.

- **NEW Phase 2 Step 1E** — Barone pre-analysis. Runs `dw-neutral-inventory-crim` (Report 0: theory-neutral discovery catalog with 6 modules) and `dw-theory-deconstructor-crim` (Report 2a: facts/inferences/assumptions decomposition with Gap Analysis Matrix and Alternative Inference Table). Both produce outputs in `Cowork Analysis/` before the 8 reports run.

- **REVISED Report 4 — "Core Defense Narrative" → "Competing Defense Theories"** — Single narrative replaced with multiple viable theories. Each theory now carries: theory name, summary, supporting evidence (with Bate stamps), weaknesses, prosecution counter-arguments, viability (STRONG/MODERATE/WEAK), and compatible Report 5 defenses. Followed by a Comparative Matrix. Rationale: premature commitment to one defense narrative creates confirmation bias; presenting alternatives lets the attorney choose with eyes open.

- **NEW Report 4a — Theory Selection Memo** — Attorney-driven, attorney sign-off required. Documents: selected theory, selection rationale, top 5-10 supporting evidence items, top 3-5 vulnerabilities, critical assumptions, pivot triggers, abandoned theories with reasoning. Gates downstream Barone skills.

- **NEW Phase 2 Step 2A — Post-Report-4 routing** — After attorney signs off on Report 4a, dispatches the selected theory to:
  - `dw-adversarial-stress-test-crim` — prosecutor red-team simulation (7 modules covering vulnerability scan, cross-examination simulation, closing preview, rebuttal evidence, defense counter-response matrix, jury perception risk, priority preparation checklist)
  - `dw-theory-to-workplan-crim` — 7-stream action plan (investigation / discovery / experts / motion practice / witness prep / exhibits / narrative)

- **Phase 3 Step 1 — Timeline Sheet enhanced** with Certainty column (CONFIRMED / PROBABLE / DISPUTED / UNCONFIRMED / ALLEGED). Distinct from Confidence (timestamp precision) — Certainty tracks event reliability. Drives defense reliance decisions for motions and cross-examination.

- **Phase 3 Step 9 — Opening/Closing prep** updated to consume the attorney-selected theory from Report 4a (replacing prior reference to "Core Defense Narrative").

- **NEW shared protocol** — `dw-shared-protocols-crim/references/verification-protocol.md`. Adds `[VERIFIED]` / `[UNVERIFIED]` flags to every catalog entry and fact extraction. Supplements (does not replace) the Source Citation Mandate. Required summary statistic at end of every deliverable using the protocol.

- **DMAR Section 10 — Report-vs-Recording Matrix (6-category)** added across `dw-video-evidence-auditor-crim`, `dw-transcript-pipeline-calcasieu-crim`, `dw-transcript-pipeline-rev-crim`, and `dw-dmar-synthesizer-crim`. Categories: Narrative Match / Omissions / Additions / Timing Discrepancies / Quote Accuracy / Procedural Compliance.

- **Discovery Compliance Ledger — 7-Bucket classification** added to `dw-discovery-compliance-monitor-crim`. Barone buckets: Law Enforcement / Physical-Forensic / Digital-Electronic / Witness / Expert / Prosecution File / Brady-Giglio. Enables completeness analysis by category.

- **Data contracts v1.2** — DMAR Section 10, Timeline Certainty column, Discovery Bucket column added to Contracts 1, 4, and 6.

- **Skill index v1.2** — Quick Lookup expanded with 4 new skill rows; dedicated "Barone Discovery Workflow" section documenting the 9-step pipeline.

- **Operations Guide v1.3** — Comprehensive Markdown manual at `docs/DW_Skills_Operations_Guide_v1.3.md` supersedes v1.2.docx.

- **Cowork Project Instructions v2.0** — `docs/DW_Criminal_Defense_Cowork Project_Instructions_1.md` rewritten to reflect current skill suite and Barone workflow.

## v5.8 (May 2026)

Comprehensive update to `assets/CASE PROFILE.docx` and `references/case-profile-procedure.md` to absorb the firm's legacy Criminal Defense Cover Sheet into Part 1 of the Case Profile. After v5.8 the standalone Cover Sheet is obsolete; the Case Profile is the single intake document. Part 2A/2B/2C unchanged.

- **Part 1 expanded from six sections to ten.** New sections added: § 2 Probation/Parole Status, § 5 Court Appearance Log, § 8 Plea Discussions Log, § 9 Family/Friends Contact List. Existing § 2 Charges & Exposure → § 3; existing § 3 Arraignment & Bail → § 4 (renamed Arraignment & Bail History and expanded); existing § 4 Case-Specific Defenses → § 6; existing § 5 Client Background → § 7; existing § 6 Key Dates & Next Steps → § 10. Section banner colors follow the canonical per-section-number scheme already established by Parts 2A/2B/2C; § 10 introduces a new brown banner (`5D4037`) since the canonical scheme previously stopped at § 9.

- **§ 1 Case Identification expanded** with two new top-of-section visual blocks and two new Court & Case Numbers fields:
  - **Case Classification** — four-checkbox row (☐ MISDEMEANOR ☐ FELONY ☐ STATE ☐ FEDERAL) at the very top of § 1. Quick visual triage cue. Multi-check allowed for state+federal dual exposure (e.g., 922(g) stacked on R.S. 14:95.1).
  - **Next Court Date** — single highlighted row (yellow label, soft-red value) immediately under Case Classification. This is the *current* next court date — the attorney's at-a-glance answer to "when is this case back in court?" The full forward-looking calendar still lives in § 10 Key Dates; Next Court Date is a pointer to whichever § 10 row is closest to today. **This is the one § 1 field Cowork actively refreshes on every Refresh Mode run.**
  - **Bill / Indictment Date** — new row in Court & Case Numbers. Distinct from Date of Arrest (which can precede the bill by weeks or months). Material for prescription analysis under La. C.Cr.P. arts. 571–576.
  - **Docket # (Companion / Related)** — new row in Court & Case Numbers. Captures severed counts, parallel magistrate-court dockets, related civil proceedings (protective orders, custody actions), or co-defendant dockets.

- **§ 2 Probation/Parole Status (NEW)** — twelve-field 2-column table. Populate only if the client is on probation, parole, drug court, diversion, or any form of court supervision at the time of the new arrest. A probation/parole hold can override bond reduction and is often the gating issue for pretrial release; failure to capture this on intake is the most common cause of an unwinnable bond hearing. Fields: On Probation/Parole? (Y/N) | Type | Officer | Officer Phone/Email | Supervising Court/Parish | Underlying Conviction/Docket # | Supervision Start Date | Supervision Expiration | Sentence Eligibility/Time Remaining | Detainer/Hold Active? (Y/N — flag in red if Y) | Special Conditions | Notes/Revocation Exposure `[ATTORNEY]`. Routing: active detainer → **dw-bond-and-release-motion-crim**; revocation-likely-regardless-of-disposition → **dw-plea-negotiation-analyzer-crim** for global-resolution math.

- **§ 4 Arraignment & Bail History expanded** in three ways:
  - **Arraignment History is now a multi-row table** (Date / Charges Read / Prosecutor / Judge / Plea Entered / Notes), supporting re-arraignment after amended bills, superseding indictments, and habitual offender bill arraignments. Was single-arraignment K/V; multi-event cases previously had no clean place to record subsequent arraignments.
  - **Cash Bond Amount** — new row in the Bail/Bond block, distinct from Bond Amount — Total. Material when source-of-funds disputes arise under R.S. 15:85.1 or when refundability of bond is at issue.
  - **Bail Notes** — new free-text row capturing the history of bond hearings, modifications, and source-of-funds disputes. Cowork populates the chronology; attorney annotates strategy.

- **§ 5 Court Appearance Log (NEW)** — six-column multi-row table (Date / Appearance Type / ADA / Judge / Bail Status / Notes-Rulings). Backward-looking chronological record of every court appearance after the initial arraignment — status conferences, motion hearings, pre-trial conferences, calendar calls. Explicitly distinct from § 10 Key Dates (forward-looking) and § 4 Arraignment History (arraignments only). Sourcing: court minute entries, attorney post-court notes (Plaud recordings, Apple Notes session bookends), staff intake from clerk's office. Refresh Mode: append-only with Next Court Date in § 1 updated from the most recent continuance ruling.

- **§ 7 Client Background — two rows added.** **Substance Abuse History** separated from Medical/Mental Health because it drives different doctrine (R.S. 13:5304 drug court eligibility, federal safety-valve under 18 U.S.C. § 3553(f), and multiple mitigation pathways). **Other Relevant Info** added as a catch-all for TBI history, foster care background, victimization history, language proficiency, learning disabilities, custodial obligations, and anything else that informs case theory or mitigation but doesn't fit a named bucket.

- **§ 8 Plea Discussions Log (NEW)** — six-column multi-row table (Date / Plea Offer-Counter / Source / Conveyed to Client (Y/N + Date) / Client Response / Notes). Captures every plea offer, every counter-offer, and every conveyance to the client. This log is the firm's contemporaneous Rule 1.4 compliance record. Distinct from **dw-plea-negotiation-analyzer-crim**: the analyzer captures the trial-exposure math for any specific offer; the log captures the existence, conveyance, and response across every offer's lifecycle. Refresh Mode allows one in-place exception: the "Conveyed to Client" cell may be updated when conveyance happens after the row is first created.

- **§ 9 Family/Friends Contact List (NEW)** — six-column multi-row table (Person / Relation / Phone-Email-Address / Role / Vetted? / Notes). The client's support network: sentencing mitigation, character witnesses, bond co-signers, jail visit coordination. Vetting routes through **dw-defense-investigator-tasking-crim**. Attorney work product — never share externally without the named person's consent.

- **Refresh Mode rules updated** to handle the four new append-only multi-row tables (§ 4 Arraignment History, § 5 Court Appearance Log, § 8 Plea Discussions Log, § 9 Family/Friends Contact List) alongside the existing § 1 Seized Property, § 10 Key Dates, § 10 High Priority Next Steps. Two narrow in-place exceptions documented: § 8 Conveyed-to-Client cell, § 10 High Priority Next Steps Status cell. § 1 Next Court Date is the one § 1 field actively refreshed on every Refresh Mode run.

- **Section banner color scheme codified.** Each Part 1 section number now has its canonical color matching the established Part 2A/2B/2C scheme: §1 blue-grey `607D8B` | §2 indigo `5C6BC0` | §3 blue `1976D2` | §4 red `C62828` | §5 deep orange `E64A19` | §6 orange `F57C00` | §7 green `388E3C` | §8 purple `7B1FA2` | §9 teal `00796B` | §10 brown `5D4037` (new, since canonical scheme stopped at §9).

- **Generation Procedure (XML Edit) — Step 2B table count grew from three to seven multi-row tables.** Step 2A is unchanged in pattern but applies to two new K/V tables (§ 2 Probation/Parole, § 4 Bail/Bond). A new "single-row visual block" pattern documented for § 1 Case Classification (checkbox row) and § 1 Next Court Date (highlighted K/V row).

- **Quality Check updated** with line items for the new sections — Case Classification marked, Next Court Date populated, Probation/Parole Status populated or marked N, Cash Bond and Bail Notes captured, Court Appearance Log seeded, Substance Abuse and Other Relevant Info rows present, Plea Discussions Log and Family/Friends Contact List seeded, Next Court Date reconciled with the closest § 10 Key Dates row, and probation/parole hold flags surfaced in completion notes.

- **`references/quick-reference.md` routing table — `dw-defense-investigator-tasking-crim` entry added.** Pre-existing gap: the skill was referenced by `case-profile-procedure.md` and several specialist skills but had never made it into the routing table. v5.8 newly references it in § 9 Family/Friends Contact List vetting (and § 10 High Priority Next Steps for that vetting work), which surfaced the latent gap. Row inserted in the cross-cutting evidence/investigation cluster between Chain of custody and Other crimes evidence.

- **No changes to Part 2A, 2B, or 2C.** No changes to `lwop-field-maps.md` or `lwop-extraction-patterns.md`. SKILL.md updated for version bump (5.7 → 5.8) and two Part 1 references: the Phase 1 Step 3 "six sections" line and the Step 3 Quality Gate's "sections 1–6" line, both updated to the ten-section structure with a Refresh Mode Next Court Date note. `defense-shield-procedure.md` updated for one cross-reference: Case-Specific Defenses moved from § 4 to § 6 in the renumbering.


## v5.7 (May 2026)

Closes the v5.5 follow-up backlog — three coordinated changes to `references/case-profile-procedure.md` and `assets/CASE PROFILE.docx`.

- **High Priority Next Steps → Status column added.** Table grew from 5 columns to 6: Step / Why High Priority / Owner / Routing / Target Date / **Status** (Open / In-Progress / Done). Done rows stay in the table; the table is now self-contained as the audit trail for completed actions. The previous "move completed steps to a Case Brain Completed log" instruction is gone — it referenced an artifact that was never specced in `dw-case-brain-crim`. The simpler in-table audit trail is the system of record. Column widths rebalanced to fit Status without forcing the Step column to wrap.
- **Sourcing notes added for the new Defendant fields** (introduced in v5.5). Place of Birth and Race/Sex → booking record or NCIC/RAP sheet. Physical Description → booking record or incident report narrative (height, weight, build, distinguishing marks, tattoos, scars). Immigration Status → client interview, jail intake screening sheet, or any ICE detainer or A-file reference in discovery. Added a routing breadcrumb: non-citizen clients route plea analysis to **dw-plea-negotiation-analyzer-crim** with the immigration impact noted. The note paragraph appears in both the procedure file and the .docx between the Defendant fields table and the Complaining Witness / Victim sub-block.
- **Section 6 Key Dates ↔ Timeline Sheet boundary clarified.** Section 6 Key Dates is now explicitly scoped as the attorney's *procedural* calendar (court dates, deadlines, motion filing dates). The comprehensive *evidentiary* timeline (every event, every source, conflict-flagged) lives in `Case Tables.xlsx — Timeline Sheet`, populated in Phase 3 Step 1. Different audiences, different lifecycles. The two are explicitly **not** to be synced. Boundary statement added in both the procedure file and the .docx Key Dates note.

## v5.6 (May 2026)
- **Section 2 (Charges & Exposure) restructured into per-charge table** in `references/case-profile-procedure.md`. Was six fields in single cells, which forced multi-count cases into comma-separated jumbles in one box and hid per-count enhancement analysis. Now organized into two sub-blocks under the existing Section 2 banner:
  - **Charges (per count)** — 6-column table (Count / La. Statute / Max Penalty / Mandatory Min / Elements / Responsive Verdicts) with one row per count, matching the Bill of Information / Indictment numbering. Per-count firearm / drug-free-zone / hate-crime sentence enhancements go in the Max Penalty cell so per-count exposure is calculable on its face. "Mandatory Min" requires explicit "None" rather than blank to distinguish absence from unchecked.
  - **Habitual Offender Exposure** — single full-width narrative cell for the cross-cutting La. R.S. 15:529.1 analysis (predicate convictions, enhancement multiplier per affected count, cleansing-period and Boykin / R.S. 15:530.7 challenges, strategic question). Routes to **dw-habitual-offender-auditor-crim**.
- **`assets/CASE PROFILE.docx` template updated to match.** Section 2's six 2-column label/value rows replaced with the 6-column charges table (5 starter rows, sized for Calibri 11pt bold headers without wrap on "Count") plus the bordered narrative box for habitual analysis. Sub-headers in red bold matching v5.5 firm style. Sections 1, 3, 4, 5, 6 and Part 2A/2B/2C unchanged.
- **No procedure-file impact on the Generation Procedure (XML Edit) section.** The new charges table uses the Step 2B multi-row pattern documented in v5.5; the habitual narrative cell uses the Step 2A label/value pattern (cell content is `<w:p/>` to fill).

## v5.5 (May 2026)
- **Generation Procedure (XML Edit) restructured** in `references/case-profile-procedure.md` to support both editing patterns: Step 2A covers the existing label-find-and-fill pattern for 2-column label/value tables (now including the new Defendant, Complaining Witness / Victim, Court & Case Numbers, and Personnel sub-blocks); Step 2B *(new)* covers the multi-row data tables (Seized Property / Devices, Key Dates, High Priority Next Steps) with anchor-and-walk table location, empty-starter-row fill as the preferred path, and `<w:tr>` clone-and-append for overflow. Refresh-Mode append-only rule documented for Step 2B tables.
- **Section 1 (Case Identification) expanded** in `references/case-profile-procedure.md`. Section 1 is now organized into five named sub-blocks instead of a flat bullet list:
  - **Defendant** — added Place of Birth, Race/Sex, Physical Description, and Immigration Status alongside the existing Name, DOB, SS#, Address, Phone, Email.
  - **Complaining Witness / Victim** *(new)* — Name, DOB, Race/Sex, Address. Populates from the charging instrument and police report; multi-victim cases list each. Minor-victim redaction note included.
  - **Court & Case Numbers** — unchanged content (Docket #, Court, Division, Judge, Date of Offense / Arrest / Hire, Co-Defendant(s)); regrouped under its own header for readability.
  - **Investigative / Prosecution Personnel** *(new)* — 10-row table per the firm's CASE PROFILE.docx layout: Case Detective, Assisting Detective, First Responder, Evidence Collection, SANE Nurse, Victim Advocate, Interpreter, Crime Lab Analyst, Issuing Judge (warrants), Prosecuting ADA. Sourcing notes added for each row.
  - **Seized Property / Devices** *(new)* — 7-column table (Item / Owner / Seized From / Date Seized / Warrant # / Bate / Extraction Status / Notes) for every phone, tablet, computer, USB, vehicle, weapon, document, or currency taken from the client, scene, or co-defendant. Drives early routing to **dw-mobile-forensic-auditor-crim** and **dw-forensic-dump-analyzer-crim**. Suppression trigger added: any item appearing in discovery without a warrant, consent, or arrest-incident inventory entry → flag in red and route to **dw-suppression-motion-crim**.
- **Section 6 (Key Dates & Next Steps) restructured** into two sub-blocks. The section name finally matches its content:
  - **Key Dates** *(new format)* — replaced four flat bullets with a 3-column table (Date / Event Description / Source). Capture both past and upcoming events. Captures expanded list including 72-hour hearing, bond hearings, each discovery production, motion deadlines, pretrial conference, Art. 701 release date, statute-of-limitations expiration (La. C.Cr.P. art. 571–576), and habitual offender bill filing deadlines. Calculated dates state the calculation in the Source cell.
  - **High Priority Next Steps** *(new)* — Cowork-prepopulated, attorney-finalized 5-column table (Step / Why High Priority / Owner / Routing / Target Date) of the highest-priority next actions. Routing column points to specialist skills (suppression, bond reduction, pretrial motion library, investigator tasking, forensic dump analyzer, etc.). Cowork proposes High/Medium/Low ranking; attorney finalizes. Completed steps move to Case Brain "Completed" log rather than being deleted.
- **Section count preserved at six.** All cross-references to "Part 1 Section 2–6" elsewhere in this skill, in `lwop-field-maps.md`, and in SKILL.md remain valid.
- **`assets/CASE PROFILE.docx` template updated to match the procedure spec.** New defendant fields (Place of Birth, Race/Sex, Physical Description, Immigration Status) added; new Complaining Witness / Victim block added; new Investigative / Prosecution Personnel 10-row table added; new Seized Property / Devices 7-column table (Item / Owner / Seized From / Date Seized / Warrant # or Bate / Extraction Status / Notes) with 6 starter empty rows added, plus the suppression-trigger note paragraph in red italic; Section 6 restructured with the 3-column Key Dates table (10 starter rows) and the 5-column High Priority Next Steps table (8 starter rows). Sub-headers rendered in red bold matching the firm's existing "Investigative / Prosecution Personnel" header style. Sections 2–5, Part 2A, Part 2B, and Part 2C are untouched. Multi-column tables include light-gray cell borders so empty data rows are visible during data entry.

## v5.4 (May 2026)
- **Major refactor:** SKILL.md reduced from 844 lines to a slim workflow spine following the `dw-forensic-dump-analyzer-crim` structural model.
- **NEW reference files:**
  - `references/case-tables-write-protocol.md` — extracted from SKILL.md
  - `references/case-profile-procedure.md` — extracted Phase 1 Step 3 detailed procedure (operating modes, Part 1/2A/2B/2C field detail, LWOP population workflow, Refresh Mode merge rules, XML edit procedure)
  - `references/defense-shield-procedure.md` — extracted Phase 3 Step 3 detailed procedure
  - `references/quick-reference.md` — Cowork action types, Case Tables sheet reference, phase quick map, specialist skill routing table
- **Linked previously orphaned references:** `color-coding.md` and `folder-structure-and-naming.md` are now properly pointed to from SKILL.md.
- **DELETED orphaned references:** `case-tables-sheet-reference.md` (outdated duplicate of Quick Reference) and `textexpander-snippets.md` (content lives in `dw-shared-protocols-crim`).
- **DELETED `scripts/master-trial-advocate-playbook.md`:** stale (referenced 9 reports; current count is 8 since v5.2) and never integrated into the workflow.
- **DELETED `assets/legacy/`:** archived Calcasieu PDO standalone LWOP forms (`LWOP Homicide Review Sheet - FOR TYPING.docx`, `LWOP Sex Offense Review Sheet - FOR TYPING.docx`) removed. The merge into Part 2A/2B of `000 - Case Profile.docx` is recorded in the v5.3 changelog entry below; originals are preserved in firm template archives and GitHub history.
- **Fixed stale skill reference:** Phase 1 Step 2e now correctly routes to `dw-transcript-router-crim` (parish-based pipeline selection). The original referenced a non-existent `casedev:transcription` skill.
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
