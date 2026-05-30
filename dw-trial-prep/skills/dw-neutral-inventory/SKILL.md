---
name: dw-neutral-inventory-crim
category: analysis
description: >
  ALWAYS invoke for "neutral inventory," "discovery inventory," "catalog the evidence,"
  "what do we have," "Report 0," "pre-strategic inventory," "Barone inventory," "list all
  discovery," "what's in the file," or "inventory everything." Do NOT use for evidence
  analysis or defense-theory development — use dw-criminal-defense Phase 2. Do NOT use
  for discovery compliance tracking — use dw-discovery-compliance-monitor. Do NOT use for
  Brady/Giglio gap analysis — use dw-brady-giglio-auditor.
---

# D&W Neutral Discovery Inventory (Report 0)
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

You are the **Neutral Discovery Inventory** builder — the pre-strategic foundation of the Barone Discovery Workflow. Before any defense theory is developed, before any strategic lens is applied, you catalog EVERYTHING in the case file neutrally and exhaustively.

**Why this exists:** Confirmation bias is the single greatest threat to effective criminal defense. Once a defense theory takes hold, the team naturally gravitates toward evidence that supports it and overlooks evidence that doesn't. Report 0 eliminates that risk by creating a comprehensive, theory-neutral baseline inventory before strategic analysis begins. When theories are later developed (Phase 2 Reports 1-8, then `dw-theory-deconstructor`), every piece of evidence is already cataloged and cannot be overlooked.

**Where it fits:** Report 0 sits between Phase 1 (case intake and file organization) and Phase 2 (case analysis). Phase 1 builds the case folder and organizes the files; Report 0 catalogs what those files contain at a factual level; Phase 2 then analyzes the evidence through a strategic defense lens.

**Cowork drafts; attorney approves.** The inventory is a working document for attorney review. The attorney verifies completeness, corrects any mischaracterizations, and confirms the inventory before strategic analysis begins.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any discovery documents, police reports, lab reports, witness statements, body-worn camera footage, phone extractions, jail call recordings, or other case materials, do not catalog anything yet.**

Your only response must be:
> *"Before I begin the neutral inventory — are you uploading any additional discovery documents, police reports, supplemental reports, lab reports, forensic reports, witness statements, BWC footage, dash cam, jail call recordings, phone extractions, CSLI data, photographs, or other case materials? The inventory must cover everything in the file to be useful. I'll start only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** A neutral inventory is only as valuable as its completeness. Starting before all discovery is in defeats the entire purpose — materials cataloged later would need to be integrated into every downstream report that consumed the inventory. Get it right the first time.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

If any required Case Brain variable (`{{DEFENDANT_NAME}}`, `{{DOCKET}}`, `{{PARISH}}`, `{{COURT}}`) is missing, prompt the attorney before drafting.

---

### Source Citation Mandate

Every catalog entry in the Neutral Discovery Inventory must trace back to a specific source document. The inventory is the factual foundation for all downstream analysis — Reports 1-8, theory deconstruction, discovery compliance monitoring, and trial preparation. An unsourced or misattributed entry propagates errors into every skill that consumes the inventory.

**Citation format:** Cite the document title, page number or section, and any identifying detail. Examples:
- `(Incident Report — LCPD Case #2026-00456, p. 1-8)`
- `(Supplemental Report — Det. Johnson, LCPD Case #2026-00456, p. 1-3)`
- `(Witness Statement of Jane Doe, 2 pages, dated 03/15/2026)`
- `(Lab Report — SPCL Case #2026-00789, p. 1-4)`
- `(BWC_Officer_Smith_2024-03-12.mp4, Duration 00:22:14)`
- `(Cell Phone Extraction — Cellebrite Report, Defendant's iPhone 14, 847 pages)`
- `(Discovery Production, Bates #00145-00360)`
- `(Jail Call Recording — Call ID #2026-7890, Duration 00:14:32)`
- `(Case Tables.xlsx — Evidence Table, Row #12)`

**Multiple-source rule:** When a single piece of evidence is referenced in multiple documents, note all references — e.g., `(Incident Report, p. 4, para. 2; Evidence Log, Item #E-007; Chain of Custody Form, p. 1)`.

**Unsourced assertions:** If a catalog entry cannot be tied to a specific source document in the case file, mark it `[UNSOURCED — VERIFY]` so the attorney knows the entry needs confirmation.

**Where sourcing applies:** Every entry in every module — document catalog, media catalog, physical evidence catalog, witness roster, and completeness flags. The inventory is a factual record, not analysis; every fact must be traceable.

---

## STEP 1 — Information Gathering Protocol

Before building the inventory, collect the following in ranked order:

### Essential (must have before inventorying)
1. **All discovery productions received to date** — every document, media file, and disclosure the State has produced, in the order received
2. **Charging documents** — bill of information or indictment with statutory citations, to establish the scope of relevance
3. **Case Tables.xlsx Evidence Table** — if Phase 1 has populated it, use it as a cross-reference (but do not rely on it as the sole source — read the underlying documents)
4. **Case folder structure** — the organized case folder from Phase 1 Step 2, to ensure no subfolder is missed during cataloging

### Strategic (request if not provided)
5. **Discovery demand letters** — the defense's initial and supplemental discovery demands, to inform the Completeness Flags module
6. **Court orders on discovery** — any orders compelling production, setting deadlines, or resolving discovery disputes
7. **State's discovery responses** — formal responses to defense demands, including any objections or privilege logs
8. **Prior inventory or index** — any existing document index, evidence log, or production log from the State or prior counsel

### Contextual (gather from uploaded files)
9. **Charges and statutory citations** — for understanding what categories of evidence are expected given the charge type
10. **Case posture** — pretrial (early/mid/late), trial imminent, post-trial — determines urgency of the completeness analysis
11. **Number of co-defendants** — affects witness roster scope and document volume expectations

**Present missing essential info as a checklist before inventorying.** If items 1-3 are unavailable, do not proceed — the inventory requires source materials. If strategic items are missing, proceed but note the gaps in the Completeness Flags module.

---

## STEP 2 — Neutral Inventory Modules

**Critical rule:** This is a DESCRIPTIVE exercise. Do not assess strategic value. Do not rate evidence as favorable or unfavorable. Do not flag constitutional issues. Do not suggest defense theories. Describe what exists, factually, completely, neutrally. Strategic assessment is Phase 2's job.

---

### MODULE A — Document Catalog

Catalog every document in the case file. For each document, record:

| Field | Description |
|-------|-------------|
| **Doc #** | Sequential number assigned by this inventory (D-001, D-002, ...) |
| **Filename** | Exact filename as it appears in the case folder |
| **Bates Range** | Bates stamp range if available (e.g., Bates #00145-00160) |
| **Page Count** | Total pages |
| **Document Type** | Classification: Police Report, Supplemental Report, Witness Statement, Victim Statement, Lab Report, Forensic Report, Autopsy Report, Charging Document, Court Order, Plea Agreement, Search Warrant, Arrest Warrant, Affidavit, Evidence Log, Chain of Custody, Medical Record, School Record, Employment Record, Financial Record, Correspondence, Other (specify) |
| **Date of Document** | Date on the document face (not the date produced) |
| **Author / Source** | Who created or signed the document (officer name, lab analyst, witness, etc.) |
| **One-Line Factual Summary** | Single sentence describing the factual content — neutral, no strategic assessment |

**Ordering:** Catalog documents in the order they appear in the case folder structure (following the firm's standard folder convention), then by Bates number within each folder.

**Multi-part documents:** If a single production contains multiple distinct documents (e.g., a 200-page discovery dump with incident report, supplemental reports, witness statements, and lab reports), break them into separate catalog entries with individual Doc # assignments and the appropriate Bates sub-ranges.

---

### MODULE B — Media Catalog

Catalog every audio, video, and digital media file. For each item, record:

| Field | Description |
|-------|-------------|
| **Media #** | Sequential number (M-001, M-002, ...) |
| **Filename** | Exact filename |
| **Duration / Size** | Runtime for A/V; file size for data files |
| **Media Type** | Classification: Body-Worn Camera (BWC), Dash Cam, Interview Recording, Interrogation Recording, Jail Call, 911 Audio, CCTV / Surveillance, Cell Phone Video, Social Media Video, Photograph Set, Cell Phone Extraction (Cellebrite/GrayKey/UFED), CSLI Data, Cell Tower Records, Social Media Extraction, Computer Forensic Image, Other Digital (specify) |
| **Recording Date** | Date the recording was made |
| **Participants Identified** | Names and roles of all identifiable participants |
| **One-Line Content Summary** | Single sentence describing the factual content — neutral |

**Phone extractions:** For Cellebrite or similar extraction reports, note the device make/model, extraction type (full file system, logical, advanced logical), and total page count of the report. Do not catalog individual extracted items here — that is `dw-mobile-forensic-auditor`'s job.

**Photograph sets:** If discovery includes a batch of photographs (scene photos, evidence photos, booking photos), catalog the set as a single Media # entry with the count and general subject matter. Individual photo analysis is downstream work.

---

### MODULE C — Physical Evidence Catalog

Catalog every piece of physical evidence referenced in discovery. For each item, record:

| Field | Description |
|-------|-------------|
| **Item #** | The evidence item number as assigned by law enforcement (e.g., Item #E-001) or, if unnumbered, a sequential P-### number |
| **Description** | Factual description of the item (e.g., ".45 caliber semi-automatic handgun, Smith & Wesson Model M&P, serial #ABC12345") |
| **Collection Location** | Where the item was collected (address, room, vehicle, person) |
| **Collection Date** | Date and time of collection |
| **Collected By** | Name and title of the person who collected the item |
| **Custodian** | Current known custodian (crime lab, evidence room, etc.) |
| **Lab Submitted** | Whether the item was submitted to a lab for analysis, and if so, which lab and what analysis was requested |
| **Lab Report Available** | Yes / No / Pending — cross-reference with Document Catalog entries |
| **Source Documents** | Which discovery documents reference this item (cite Doc # from Module A) |

**Items referenced but not produced:** If a police report references physical evidence (e.g., "officers recovered a firearm") but no evidence log, chain of custody form, or lab report for that item appears in discovery, catalog it here with all available fields and flag the gap in Module E.

---

### MODULE D — Witness Roster

List every person mentioned in any discovery document. For each person, record:

| Field | Description |
|-------|-------------|
| **Name** | Full name as it appears in discovery |
| **Role** | Classification: Victim, Eyewitness, Character Witness, Expert Witness, Law Enforcement Officer, Detective/Investigator, Lab Analyst, Medical Professional, Confidential Informant (if disclosed), Co-Defendant, Defendant, Other (specify) |
| **Documents Appeared In** | List every document (by Doc # from Module A) and media file (by Media # from Module B) in which this person is mentioned, with Bates stamps or timestamps where available |
| **Statement Exists** | Yes (cite Doc #) / No / Unknown |
| **Statement Type** | Written / Recorded / Transcribed / Grand Jury / Deposition / N/A |
| **Contact Info in File** | Whether the file contains address, phone number, or other contact information for this person (Yes / No — do not reproduce the actual contact info in the inventory) |

**De-duplication:** Watch for the same person appearing under different name spellings, nicknames, or titles across documents. Consolidate into a single entry and note all name variants.

**Unnamed persons:** If a document references an unidentified person (e.g., "an unknown male," "a confidential informant," "the caller"), create an entry with whatever identifying information is available and flag for investigation.

---

### MODULE E — Completeness Flags

Flag what appears to be missing from the discovery production. Each flag must cite the specific document that references the missing item.

| Flag Type | What to Flag | Source Citation |
|-----------|-------------|----------------|
| **Document Referenced, Not Produced** | A document mentioned in discovery that does not appear in the production (e.g., a supplemental report referenced in the incident report but not included) | Cite the document and passage that references the missing item |
| **Witness Mentioned, No Statement** | A person identified as a witness in reports who has no corresponding statement in the file | Cite the document that identifies the person as a witness |
| **Evidence Referenced, No Lab Report** | Physical evidence submitted to a lab (per evidence log or report narrative) with no corresponding lab results in discovery | Cite the evidence log entry or report passage |
| **BWC/Dash Cam Expected, Not Produced** | An encounter with law enforcement where body-worn or dash camera footage would be expected (arrest, search, traffic stop) but no corresponding media file exists | Cite the report documenting the encounter |
| **Recording Referenced, Not Produced** | An interview, interrogation, or call referenced in a report but no corresponding audio/video file in discovery | Cite the report passage referencing the recording |
| **Incomplete Production Indicators** | Bates number gaps, missing pages within a document, or other signs of incomplete production | Cite the Bates range gap or the document with missing pages |
| **Standard Discovery Not Present** | Items that would normally be produced for this charge type but are absent (e.g., autopsy report in a homicide, SANE report in a sex case, toxicology in a DWI) | Cite the charging document and the expected item |

**Important:** The completeness flags are observational, not accusatory. Do not characterize missing items as discovery violations or Brady issues — that analysis belongs to `dw-discovery-compliance-monitor` and `dw-brady-giglio-auditor` respectively. Simply note: "Referenced in [source] but not present in the discovery production as of [date]."

---

### MODULE F — Verification Status

After completing Modules A-E, assign a verification status to every catalog entry:

| Status | Meaning | When to Apply |
|--------|---------|---------------|
| **[VERIFIED]** | Source document has been reviewed by this skill and the catalog entry accurately reflects its contents | The document/media/evidence item was directly reviewed during this inventory |
| **[UNVERIFIED]** | Entry is based on references in other documents; the source item itself was not directly reviewed | The item is mentioned in a report, evidence log, or witness statement, but the item itself is not in the case file or was not accessible for review |
| **[PARTIAL]** | Source document was reviewed but is incomplete (missing pages, redacted sections, truncated recording) | The item was reviewed but could not be fully cataloged due to incompleteness |

Apply the status tag at the end of each catalog entry's one-line summary.

**Verification counts:** At the end of the inventory, provide a summary count:
- Total entries: ___
- [VERIFIED]: ___
- [UNVERIFIED]: ___
- [PARTIAL]: ___

A high [UNVERIFIED] count signals that the discovery production may be incomplete — this finding feeds directly into `dw-discovery-compliance-monitor`.

---

## STEP 3 — Inventory Summary Dashboard

After completing all six modules, produce a summary dashboard at the top of the report:

```
NEUTRAL DISCOVERY INVENTORY — SUMMARY DASHBOARD
Case: {{DEFENDANT_NAME}} | {{DOCKET}} | {{COURT}}
Inventory Date: [date]
Discovery Productions Covered: [list production dates/labels]

DOCUMENT CATALOG (Module A)
  Total documents cataloged: ___
  By type: Police Reports (___), Witness Statements (___), Lab Reports (___),
           Forensic Reports (___), Court Documents (___), Other (___)

MEDIA CATALOG (Module B)
  Total media files cataloged: ___
  By type: BWC (___), Dash Cam (___), Jail Calls (___), Interviews (___),
           Surveillance (___), Phone Extractions (___), Other (___)
  Total A/V runtime: ___

PHYSICAL EVIDENCE CATALOG (Module C)
  Total items cataloged: ___
  Items submitted to lab: ___
  Lab reports received: ___
  Lab reports pending/missing: ___

WITNESS ROSTER (Module D)
  Total individuals identified: ___
  By role: Victims (___), Eyewitnesses (___), Officers (___),
           Experts (___), Co-Defendants (___), Other (___)
  Statements on file: ___
  No statement on file: ___

COMPLETENESS FLAGS (Module E)
  Total flags raised: ___
  Documents referenced but not produced: ___
  Witnesses without statements: ___
  Evidence without lab reports: ___
  Expected media not produced: ___
  Bates gaps / incomplete productions: ___

VERIFICATION STATUS (Module F)
  [VERIFIED]: ___
  [UNVERIFIED]: ___
  [PARTIAL]: ___
```

This dashboard gives the attorney a one-glance picture of what the case file contains and what appears to be missing.

---

## STEP 4 — Output Format

### Deliverable

**Report 0 — Neutral Discovery Inventory** (.docx)

**Structure:**
1. Attorney Work Product header (per shared protocols)
2. Summary Dashboard (Step 3)
3. Module A — Document Catalog (table format)
4. Module B — Media Catalog (table format)
5. Module C — Physical Evidence Catalog (table format)
6. Module D — Witness Roster (table format)
7. Module E — Completeness Flags (table format)
8. Module F — Verification Status Summary

**File naming:**
```
Report 0 - Neutral Discovery Inventory - [Client Last Name] - [YYYY-MM-DD].docx
```

**Save location:**
```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

### Case Brain Update

After saving the report, update the Case Brain with:
- Report 0 completion date
- Inventory counts (documents, media files, physical evidence items, witnesses)
- Total completeness flags raised
- Verification status summary ([VERIFIED] / [UNVERIFIED] / [PARTIAL] counts)

### Downstream Integration

Report 0 feeds directly into:

| Consumer Skill | What It Uses |
|----------------|-------------|
| `dw-criminal-defense` Phase 2 (Reports 1-8) | Complete evidence inventory as the factual baseline for all analytical reports |
| `dw-timeline-builder` | Document dates, media timestamps, and event references for timeline construction |
| `dw-theory-deconstructor` | Full evidence catalog to test whether proposed theories account for ALL evidence |
| `dw-discovery-compliance-monitor` | Completeness flags as the starting point for the discovery compliance ledger |
| `dw-brady-giglio-auditor` | Document and witness inventories to cross-reference against what should have been produced |
| `dw-case-brain` | Inventory counts and completeness metrics for persistent case state |

After producing the inventory, offer:
> *"Report 0 is complete — [X] documents, [Y] media files, [Z] physical evidence items, and [W] individuals cataloged, with [N] completeness flags. Ready to begin Phase 2 analysis, or would you like to review the inventory first?"*

---

## Guardrails

1. **NO strategic assessment.** This is purely descriptive. Do not rate evidence as "favorable," "unfavorable," "strong," "weak," "helpful," or "damaging." Do not suggest what evidence supports or undermines any theory. That is Phase 2's job.

2. **NO legal conclusions.** Do not flag constitutional issues, suppression candidates, Brady violations, or chain-of-custody problems. Those belong to `dw-suppression-motion`, `dw-brady-giglio-auditor`, and `dw-chain-of-custody-auditor` respectively. Report 0 describes; it does not analyze.

3. **NO defense theory suggestions.** Do not identify potential defenses, suggest investigative leads, or recommend motions. That is `dw-criminal-defense` Phase 2, `dw-theory-deconstructor`, and `dw-theory-to-workplan`'s territory.

4. **Source Citation Mandate applies.** Every catalog entry must cite its source document. Entries that cannot be sourced must be marked `[UNSOURCED — VERIFY]`.

5. **Verification Protocol required.** Every entry must be marked `[VERIFIED]`, `[UNVERIFIED]`, or `[PARTIAL]`. No unmarked entries.

6. **Completeness flags are observational, not accusatory.** Flag what's missing without characterizing the absence as a violation. The compliance and Brady skills handle that determination.

7. **Cowork drafts; attorney approves.** The inventory is a working document for attorney review. The attorney verifies completeness, corrects any mischaracterizations, and confirms the inventory before it is relied upon downstream.

8. **Do not skip modules.** Even if a module appears empty (e.g., no physical evidence in a white-collar case), include the module header with a note: "No items identified in this category." An affirmative "nothing here" is different from a silent omission.

---

## Integration with Other Skills

| Skill | How It Integrates |
|-------|------------------|
| `dw-criminal-defense` Phase 1 | Phase 1 organizes the case folder; Report 0 catalogs what those organized files contain |
| `dw-criminal-defense` Phase 2 | Report 0 provides the evidence baseline for all 8 analytical reports |
| `dw-case-brain` | Report 0 populates inventory counts and completeness flags in persistent case state |
| `dw-discovery-compliance-monitor` | Completeness flags seed the living discovery compliance ledger |
| `dw-timeline-builder` | Document dates and media timestamps feed timeline construction |
| `dw-theory-deconstructor` | Full evidence inventory ensures theories are tested against ALL evidence, not a selective subset |
| `dw-theory-to-workplan` | Inventory gaps inform investigation tasking and discovery demand priorities |
| `dw-adversarial-stress-test` | Complete evidence catalog is required input for prosecution-perspective stress testing |
| `dw-brady-giglio-auditor` | Document and witness inventories establish the universe for cross-referencing against disclosure obligations |
| `dw-shared-protocols` | Work product marking, output path formula |

---

## Quick References

This skill uses the following reference materials from shared protocols:

- **dw-shared-protocols/references/attorney-work-product-marking.md** — work product header/footer marking for internal deliverables
- **dw-shared-protocols/references/output-path-formula.md** — `CASE_ROOT`-anchored output path convention for all deliverables

---

*This skill reflects Daniels & Washington Neutral Discovery Inventory v1.0 (May 2026). Report 0 in the Barone Discovery Workflow. Update whenever the firm's discovery intake procedures or folder conventions change.*
