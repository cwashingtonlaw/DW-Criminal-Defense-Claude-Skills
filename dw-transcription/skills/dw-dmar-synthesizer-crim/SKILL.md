---
name: dw-dmar-synthesizer-crim
category: transcription
description: >
  Cross-case DMAR synthesizer for Daniels & Washington. Ingests multiple Defense Media Analysis
  Reports and produces a consolidated inconsistency matrix, cross-case witness comparison, and
  unified defense intelligence brief. ALWAYS invoke for "compare DMARs," "cross-case analysis,"
  "co-defendant comparison," "consolidate DMARs," "inconsistency matrix," "witness comparison
  across cases," "synthesize the DMARs," "cross-reference co-defendant evidence," "multi-case
  DMAR," "compare witness statements across cases," or when working with co-defendants, joined
  cases, or multiple cases involving overlapping witnesses or events. Also triggers when the
  attorney has run transcript pipelines on multiple client folders and wants to see where the
  evidence conflicts. Do NOT use for single-case DMAR generation — use dw-transcript-router-crim
  for that.

---

# DW DMAR Synthesizer — Cross-Case Defense Media Analysis

**Role**: Criminal defense analyst synthesizing evidence across multiple cases
**Jurisdiction**: Louisiana / 5th Circuit (toggle if another jurisdiction applies)
**Privilege**: Attorney Work Product / Privileged Communication

### Source Citation Mandate

Every factual assertion in the Consolidated DMAR, inconsistency matrix, and cross-case witness comparison must trace back to a specific source document across the input DMARs and underlying case files. Cross-case analysis is only credible when the attorney can verify each inconsistency against the original evidence — vague references to "the other case" are not actionable.

**Citation format:** Cite the case, document title, page number, and paragraph or timestamp. Examples:
- `(Case A — DMAR, Witness: Officer Smith, Timestamp 00:15:32)`
- `(Case B — DMAR, Witness: Officer Smith, Timestamp 00:08:14)`
- `(Case A — Arrest Report, p. 3, para. 2)`
- `(Case B — Witness Statement of Jane Doe, p. 2, para. 4)`
- `(Case A — Jail Call Recording, 03/15/2026, Timestamp 04:22)`
- `(Case B — Discovery Production, Bates #00145-00148)`

**Multiple-source rule:** Cross-case inconsistencies inherently involve multiple sources — always cite the conflicting documents from each case side by side.

**Unsourced assertions:** If a cross-case finding cannot be tied to specific documents in the input DMARs or case files, mark it `[UNSOURCED — VERIFY WITH CASE FILES]`. Never present an unsourced inconsistency as established without flagging it.

**Where sourcing applies:** Every entry in the inconsistency matrix, every witness comparison, every timeline conflict, and every Brady finding. Legal analysis and case law citations follow normal citation format.

---

## Why This Skill Exists

Each transcript pipeline (Calcasieu and Rev) produces a Defense Media Analysis Report (DMAR) for a single client's evidence. That's powerful for one case — but criminal defense often involves situations where the real gold is in the *gaps between* cases:
- **Co-defendants** whose recorded statements contradict each other about who did what
- **The same officer** telling different stories across separate interrogations
- **The same witness** giving a statement in Case A that's irreconcilable with their testimony in Case B
- **Timeline conflicts** where the state's narrative for one defendant physically can't coexist with the narrative for another
- **Brady material** hiding in a co-defendant's discovery that was never disclosed to your client

A single-case DMAR can't catch any of this. The synthesizer reads multiple DMARs side by side and systematically finds every place the evidence fights with itself — then packages those findings into a consolidated report the attorney can use at trial, in plea negotiations, or in a severance motion.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded, referenced, or pointed to any DMARs, do not analyze anything yet.**

Your only response must be:

> *"Before I begin — are you uploading any additional DMARs or case files? I need all the DMARs you want compared before I start the cross-case synthesis. Confirm: 'That's all the DMARs.'"*

Proceed **only** after explicit confirmation.

---

## STEP 1 — DMAR INGESTION & INDEXING

### Step 1.1 — Locate and read all DMARs
DMARs are `.docx` files following the naming convention `DMAR — [LastName, FirstName] — [Date].docx`. They may be:
- In the currently selected folder (multiple client subfolders)
- Uploaded directly by the attorney
- In separate case folders the attorney navigates to

Read each DMAR using the `docx` skill's reading capabilities (pandoc or XML unpacking). Extract structured data from every section.

### Step 1.2 — Build the Case Registry

For each DMAR, extract and index:

Registry fields: Client, Docket #, Parish, Platform, Analysis Date, Media Files, Speakers Identified, and CR / RR / ME / IT / KE finding counts. Read `references/dmar-ingestion-and-indexing.md` now for the exact CASE REGISTRY ENTRY block.
### Step 1.3 — Identify Shared Entities

This is the critical indexing step. Across all ingested DMARs, build a master entity list:

**Shared Speakers/Witnesses**: People who appear in more than one DMAR. Match on name (accounting for spelling variations, nicknames, title differences like "Det. Jones" vs. "Detective Jones" vs. "Mark Jones"). Flag every match for the attorney to confirm.

**Shared Locations**: Addresses, intersections, businesses, or landmarks referenced in multiple DMARs.

**Shared Events**: Events described in multiple DMARs (the same incident, arrest, search, or encounter referenced from different perspectives).

**Shared Evidence Items**: Weapons, vehicles, drugs, phones, or other physical evidence mentioned across DMARs.

Present the **Cross-Case Entity Crosswalk** table (Entity | Type | Appears In | Role in Each) to the attorney and ask them to confirm each match and flag false matches; use the exact prompt in `references/dmar-ingestion-and-indexing.md`.

Wait for attorney confirmation before proceeding.

---

## STEP 2 — CROSS-CASE INCONSISTENCY ANALYSIS

For every shared entity confirmed in Step 1.3, systematically compare what each DMAR says. This is the core analytical engine.

### Module S1 — Witness Statement Cross-Case Comparison

For each person who appears as a speaker in multiple DMARs:

1. **Extract all statements** this person made across all DMARs (pull from Section 2 transcript summaries, Section 3 CR findings, and Section 6 speaker analysis)
2. **Compare factual claims** about the same event or topic
3. **Flag inconsistencies** using this format:

Record each as a **CROSS-CASE WITNESS INCONSISTENCY [XW-###]** block, typed DIRECT CONTRADICTION / MATERIAL OMISSION / DETAIL SHIFT / SEQUENCE CONFLICT with severity, defense significance, cross-exam seed, and affected clients. Read `references/cross-case-finding-schemas.md` now for the exact block and the four inconsistency-type definitions.

### Module S2 — Officer Consistency Audit

Officers who appear across multiple cases deserve special scrutiny because their credibility is foundational to the state's case in each matter.

For each officer in multiple DMARs:

1. **Compare their account** of the same underlying incident across cases
2. **Compare interrogation techniques** — if the same officer interrogated multiple defendants, compare the Reid Technique and coercion findings (IT-### findings) across DMARs
3. **Compare Miranda administration** — did the officer give Miranda consistently, or did the warnings differ in completeness or timing across cases?
4. **Compare report-vs-recording patterns** — do the same types of discrepancies (RR-### findings) appear in this officer's work across cases?

Record each as a **CROSS-CASE OFFICER AUDIT [XO-###]** block (category NARRATIVE INCONSISTENCY / TECHNIQUE PATTERN / MIRANDA PATTERN / REPORT PATTERN) per `references/cross-case-finding-schemas.md`.
### Module S3 — Timeline Reconciliation

Merge the Master Timelines (Section 5) from all ingested DMARs into a single unified super-timeline.

This is where physically impossible state narratives become visible. If the state says Defendant A was at Location X at 9:15 PM committing Crime 1, and separately says Defendant B was with Defendant A at Location Y at 9:15 PM committing Crime 2, the merged timeline exposes that.

1. **Normalize all timestamps** across DMARs (resolve timezone, date format, and clock differences)
2. **Interleave all events** from all DMARs into one chronological sequence
3. **Flag conflicts** where the state's theory for one defendant contradicts the state's theory for another:

Record each as a **CROSS-CASE TIMELINE CONFLICT [XT-###]** block per `references/cross-case-finding-schemas.md`.

### Module S4 — Brady/Giglio Cross-Pollination

Review each DMAR's Section 7.4 (Potential Brady/Giglio Issues) and Section 3 (Cross-Reference findings) for evidence that should have been disclosed to another defendant but may not have been.
The classic scenario: Co-defendant B's DMAR contains a witness statement exculpating Co-defendant A — but the state may not have disclosed that statement in A's discovery. Or: Co-defendant B made a deal (Giglio material) that hasn't shown up in Co-defendant A's discovery.

Record each as a **CROSS-CASE BRADY/GIGLIO ALERT [XB-###]** block (Brady Category A / B / C; disclosure status UNKNOWN pending attorney verification) per `references/cross-case-finding-schemas.md`.

### Module S4A — Report-vs-Recording Cross-Case Comparison (Barone 6-Category)

When source DMARs contain Report-vs-Recording Matrices (Section 4A, per `dw-data-contracts-crim` Contract 1 Section 10), compare the matrices across cases:
- **Same officer, different reports**: Does the officer's pattern of omissions, additions, or procedural deviations repeat across cases? Consistent patterns strengthen impeachment.
- **Same event, different officers**: Do different officers' reports diverge from the same recording differently? Divergent accounts of the same event are powerful cross-examination material.
- **Institutional patterns**: Do officers from the same agency exhibit similar report-vs-recording patterns? May support a systemic challenge or policy-compliance argument.

Output as XR-### findings with: officer name, cases compared, pattern identified, severity, and cross-examination recommendation.

### Module S5 — Severance Analysis Intelligence

If co-defendants are joined for trial, the synthesis may reveal grounds for severance under La. C.Cr.P. Art. 704. Flag situations where:

- One defendant's statement implicates another (Bruton v. United States problem)
- The defense theories are mutually antagonistic (each defendant blames the other)
- Evidence admissible against one defendant would unfairly prejudice another
- The timeline conflicts make it impossible for the jury to coherently evaluate both cases simultaneously

Record each as a **SEVERANCE INDICATOR [XS-###]** block (BRUTON / ANTAGONISTIC DEFENSES / SPILLOVER PREJUDICE / IRRECONCILABLE TIMELINES) per `references/cross-case-finding-schemas.md`.

---

## STEP 3 — ATTORNEY CONFIRMATION

Before generating the final report, present a summary of findings:

Present the **Cross-Case Synthesis Preview** — DMARs analyzed, clients, XW / XO / XT / XB / XS counts (with critical counts), top 3 strongest findings, and the confirm-or-dig-deeper prompt. Read `references/synthesis-report-structure.md` now for the exact preview block.

---

## STEP 4 — GENERATE THE SYNTHESIS REPORT (.docx)

Use the `docx` skill to produce the output document.
### Report Structure

Header, then Sections 1–8 (Case Registry & Entity Crosswalk; Inconsistency Matrix; Witness Comparison (XW); Officer Audit (XO); Unified Super-Timeline (XT); Brady/Giglio Cross-Pollination (XB); Severance Analysis (XS); Defense Intelligence Brief) and Appendices A–C (Finding ID Reference; Source DMAR Inventory with SHA-256; Methodology with Act 250 / ABA Opinion 512 and co-counsel sharing warning).

Read `references/synthesis-report-structure.md` now for the complete report skeleton.

### File Naming

`DMAR Synthesis — [ClientA LastName] + [ClientB LastName] — [Date].docx`

For three or more clients:
`DMAR Synthesis — [ClientA] + [ClientB] + [N] others — [Date].docx`

### Save Location

Save to the primary client's case folder (the client whose case the attorney is currently working). If unclear, ask.

---

## STEP 5 — UPDATE CASE BRAIN

Write to `dw-case-brain-crim` for each client whose DMAR was included:

> Cross-case DMAR synthesis completed: [Client A] + [Client B] [+ others].
> [X] cross-case witness inconsistencies, [Y] officer audit findings,
> [Z] timeline conflicts, [W] Brady/Giglio alerts, [V] severance indicators.
> Strongest finding: [one-line summary of top finding].
> Report saved to: [file path].

---

## GUARDRAILS

1. **Privilege warning**: This report compares evidence across multiple clients. If those clients have different attorneys, sharing this report may implicate joint defense agreements or waive privilege. The report's Appendix C includes a warning, but also flag this verbally to the attorney at Step 3 if the DMARs involve clients with separate counsel.

2. **Don't fabricate connections**: Only flag inconsistencies where the DMAR text actually supports the finding. If two witnesses say slightly different things but the difference is trivially explained by perspective (one was farther away, one arrived later), note the difference but rate it MINOR, not CRITICAL. The attorney will assess whether to pursue it.

3. **Preserve source attribution**: Every finding in the synthesis report must trace back to a specific DMAR section, finding ID, source file, and timestamp. The attorney needs to be able to pull the original transcript and verify.

4. **Don't merge findings mechanically**: Two CR-001 findings from different DMARs are not the same finding just because they share an ID number. Finding IDs are local to each DMAR. The synthesis assigns new XW/XO/XT/XB/XS IDs.

5. **Speaker name matching requires confirmation**: Never assume "Marcus Jones" in DMAR-A is the same person as "M. Jones" in DMAR-B without attorney confirmation (Step 1.3). False matches are worse than missed matches.

6. **Scope boundary**: This skill synthesizes existing DMARs. It does not re-analyze raw transcripts or media files. If the attorney needs a DMAR generated first, route to `dw-transcript-router-crim`.

---

## QUICK REFERENCE — LEGAL AUTHORITIES

Controlling authorities for Bruton, severance (Zafiro; La. C.Cr.P. Art. 704), Brady / Kyles / Giglio / Bagley, joint defense privilege (Schwimmer), and Louisiana joinder (La. C.Cr.P. Art. 700–706). Read `references/legal-authorities.md` now for the principle-to-citation table.

---

## INTEGRATION WITH OTHER DW SKILLS

- **Upstream**: `dw-transcript-pipeline-calcasieu-crim` and `dw-transcript-pipeline-rev-crim` (via `dw-transcript-router-crim`) produce the individual DMARs this skill consumes
- **Downstream**: Synthesis findings feed into:
  - `dw-cross-exam-architect-crim` — XW and XO findings become cross-exam chapter seeds
  - `dw-brady-giglio-auditor-crim` — XB alerts trigger fresh Brady audits on individual cases
  - `dw-suppression-motion-crim` — XO Miranda pattern findings support suppression arguments
  - `dw-pretrial-motion-library-crim` — XS severance indicators support severance motions
  - `dw-discovery-compliance-monitor-crim` — XB alerts update discovery ledgers
  - `dw-plea-negotiation-analyzer-crim` — Cross-case inconsistencies strengthen negotiation leverage

---

## Quick References

- **dmar-ingestion-and-indexing.md** — Steps 1.2–1.3; Case Registry entry schema and entity crosswalk prompt
- **cross-case-finding-schemas.md** — Step 2, Modules S1–S5; XW / XO / XT / XB / XS finding-block formats and inconsistency-type definitions
- **synthesis-report-structure.md** — Step 4; full Cross-Case DMAR Synthesis Report skeleton and appendices
- **legal-authorities.md** — Quick Reference; principle-to-citation table (Bruton, Zafiro, Art. 704, Brady, Kyles, Giglio, Bagley, Schwimmer, Art. 700–706)
