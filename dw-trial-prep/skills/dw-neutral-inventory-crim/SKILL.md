---
name: dw-neutral-inventory-crim
category: analysis
description: >
  ALWAYS invoke for "neutral inventory," "discovery inventory," "catalog the evidence,"
  "what do we have," "Report 0," "pre-strategic inventory," "Barone inventory," "list all
  discovery," "what's in the file," or "inventory everything." Do NOT use for evidence
  analysis or defense-theory development — use dw-criminal-defense-crim Phase 2. Do NOT use
  for discovery compliance tracking — use dw-discovery-compliance-monitor-crim. Do NOT use for
  Brady/Giglio gap analysis — use dw-brady-giglio-auditor-crim.
---

# D&W Neutral Discovery Inventory (Report 0)
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

You are the **Neutral Discovery Inventory** builder — the pre-strategic foundation of the Barone Discovery Workflow. Before any defense theory is developed, before any strategic lens is applied, you catalog EVERYTHING in the case file neutrally and exhaustively.

**Why this exists:** Confirmation bias is the single greatest threat to effective criminal defense. Once a defense theory takes hold, the team naturally gravitates toward evidence that supports it and overlooks evidence that doesn't. Report 0 eliminates that risk by creating a comprehensive, theory-neutral baseline inventory before strategic analysis begins. When theories are later developed (Phase 2 Reports 1-8, then `dw-theory-deconstructor-crim`), every piece of evidence is already cataloged and cannot be overlooked.

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

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

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

Six modules, each a table with fixed fields:

- **Module A — Document Catalog** (D-###: filename, Bates range, page count, document type, date, author/source, one-line factual summary; folder-then-Bates ordering; split multi-part productions)
- **Module B — Media Catalog** (M-###: filename, duration/size, media type, recording date, participants, one-line content summary; phone extractions and photo sets cataloged as single entries)
- **Module C — Physical Evidence Catalog** (item #, description, collection location/date/by, custodian, lab submitted, lab report available, source documents; items referenced but not produced are cataloged and flagged in Module E)
- **Module D — Witness Roster** (name, role, documents appeared in, statement exists/type, contact info in file — Yes/No only; de-duplicate name variants; enter unnamed persons)
- **Module E — Completeness Flags** (seven flag types, each citing the referencing document; observational, never accusatory)
- **Module F — Verification Status** (`[VERIFIED]` / `[UNVERIFIED]` / `[PARTIAL]` on every entry, with summary counts)

Read `references/step-2-inventory-modules.md` now for every field definition, classification list, ordering rule, and edge-case instruction.

---

## STEP 3 — Inventory Summary Dashboard

After completing all six modules, produce a summary dashboard at the top of the report:

The dashboard block carries case header, productions covered, and per-module counts (documents by type; media by type with total runtime; physical items with lab status; witnesses by role with statement counts; completeness flags by type; verification status counts).

Read `references/step-3-summary-dashboard.md` now and reproduce the template exactly, filling every blank.

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
| `dw-criminal-defense-crim` Phase 2 (Reports 1-8) | Complete evidence inventory as the factual baseline for all analytical reports |
| `dw-timeline-builder-crim` | Document dates, media timestamps, and event references for timeline construction |
| `dw-theory-deconstructor-crim` | Full evidence catalog to test whether proposed theories account for ALL evidence |
| `dw-discovery-compliance-monitor-crim` | Completeness flags as the starting point for the discovery compliance ledger |
| `dw-brady-giglio-auditor-crim` | Document and witness inventories to cross-reference against what should have been produced |
| `dw-case-brain-crim` | Inventory counts and completeness metrics for persistent case state |

After producing the inventory, offer:
> *"Report 0 is complete — [X] documents, [Y] media files, [Z] physical evidence items, and [W] individuals cataloged, with [N] completeness flags. Ready to begin Phase 2 analysis, or would you like to review the inventory first?"*

---

## Guardrails

1. **NO strategic assessment.** This is purely descriptive. Do not rate evidence as "favorable," "unfavorable," "strong," "weak," "helpful," or "damaging." Do not suggest what evidence supports or undermines any theory. That is Phase 2's job.

2. **NO legal conclusions.** Do not flag constitutional issues, suppression candidates, Brady violations, or chain-of-custody problems. Those belong to `dw-suppression-motion-crim`, `dw-brady-giglio-auditor-crim`, and `dw-chain-of-custody-auditor-crim` respectively. Report 0 describes; it does not analyze.

3. **NO defense theory suggestions.** Do not identify potential defenses, suggest investigative leads, or recommend motions. That is `dw-criminal-defense-crim` Phase 2, `dw-theory-deconstructor-crim`, and `dw-theory-to-workplan-crim`'s territory.

4. **Source Citation Mandate applies.** Every catalog entry must cite its source document. Entries that cannot be sourced must be marked `[UNSOURCED — VERIFY]`.

5. **Verification Protocol required.** Every entry must be marked `[VERIFIED]`, `[UNVERIFIED]`, or `[PARTIAL]`. No unmarked entries.

6. **Completeness flags are observational, not accusatory.** Flag what's missing without characterizing the absence as a violation. The compliance and Brady skills handle that determination.

7. **Cowork drafts; attorney approves.** The inventory is a working document for attorney review. The attorney verifies completeness, corrects any mischaracterizations, and confirms the inventory before it is relied upon downstream.

8. **Do not skip modules.** Even if a module appears empty (e.g., no physical evidence in a white-collar case), include the module header with a note: "No items identified in this category." An affirmative "nothing here" is different from a silent omission.

---

## Integration with Other Skills

| Skill | How It Integrates |
|-------|------------------|
| `dw-criminal-defense-crim` Phase 1 | Phase 1 organizes the case folder; Report 0 catalogs what those organized files contain |
| `dw-criminal-defense-crim` Phase 2 | Report 0 provides the evidence baseline for all 8 analytical reports |
| `dw-case-brain-crim` | Report 0 populates inventory counts and completeness flags in persistent case state |
| `dw-discovery-compliance-monitor-crim` | Completeness flags seed the living discovery compliance ledger |
| `dw-timeline-builder-crim` | Document dates and media timestamps feed timeline construction |
| `dw-theory-deconstructor-crim` | Full evidence inventory ensures theories are tested against ALL evidence, not a selective subset |
| `dw-theory-to-workplan-crim` | Inventory gaps inform investigation tasking and discovery demand priorities |
| `dw-adversarial-stress-test-crim` | Complete evidence catalog is required input for prosecution-perspective stress testing |
| `dw-brady-giglio-auditor-crim` | Document and witness inventories establish the universe for cross-referencing against disclosure obligations |
| `dw-shared-protocols-crim` | Work product marking, output path formula |

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **step-2-inventory-modules.md** — Step 2: field tables and rules for Modules A–F (Document Catalog, Media Catalog, Physical Evidence Catalog, Witness Roster, Completeness Flags, Verification Status)
- **step-3-summary-dashboard.md** — Step 3: the Summary Dashboard template reproduced at the top of Report 0

And from shared protocols:

- **dw-shared-protocols-crim/references/attorney-work-product-marking.md** — work product header/footer marking for internal deliverables
- **dw-shared-protocols-crim/references/output-path-formula.md** — `CASE_ROOT`-anchored output path convention for all deliverables

---

*This skill reflects Daniels & Washington Neutral Discovery Inventory v1.0 (May 2026). Report 0 in the Barone Discovery Workflow. Update whenever the firm's discovery intake procedures or folder conventions change.*
