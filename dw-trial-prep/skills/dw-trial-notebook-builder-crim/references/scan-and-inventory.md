# Scan & Inventory Tables (Step 1)

Read at Step 1 — the 9-tab Trial Notebook folder-scan table (1A), Pretrial Notebook scan (1B), Case Tables audit (1C), Case Brain cross-reference (1D), and Inventory Table format (1E), verbatim.

---

### 1A — Trial Notebook Folder Scan

The D&W Trial Notebook uses this 9-tab structure:

| Tab | Folder Path | What to Look For |
|-----|-------------|------------------|
| Tab 1 | `01 - Trial Notebook/01 - Jury Instructions & Selection/` | Proposed jury charges, verdict forms, responsive verdict analysis, Art 814 documents, voir dire materials, juror questionnaires, strike lists, Batson tracking |
| Tab 2 | `01 - Trial Notebook/02 - Opening & Closing/` | Opening Statement (.docx from `dw-trial-narrative-builder-crim`), Closing Argument (.docx from `dw-trial-narrative-builder-crim`), Theme Tracker (.xlsx from `dw-trial-narrative-builder-crim`), Rebuttal Anticipation Memo (.docx from `dw-trial-narrative-builder-crim`), Mapping the Story worksheets, memorable theme documents |
| Tab 3 | `01 - Trial Notebook/03 - Witnesses/` | Cross-exam outlines from `dw-cross-exam-architect-crim` (.docx, source catalogs .pdf, combined source documents .pdf), Direct-exam outlines from `dw-direct-exam-architect-crim` (.docx, source catalogs .pdf, combined source documents .pdf), impeachment worksheets, witness battle cards, witness dossiers. Check both `Prosecution Witnesses/` and `Defense Witnesses/` subfolders |
| Tab 4 | `01 - Trial Notebook/04 - Exhibit List/` | Master exhibit list, exhibit authentication tracker, stipulated exhibits list |
| Tab 5 | `01 - Trial Notebook/05 - Evidence/` | Bate-stamped documents, digital evidence placeholders, transcripts, media files |
| Tab 6 | `01 - Trial Notebook/06 - Motions in Limine/` | Filed motions in limine, 404(b) oppositions, Prieur notice responses |
| Tab 7 | `01 - Trial Notebook/07 - Legal Research/` | Legal memoranda, statutory compilations, case law printouts |
| Tab 8 | `01 - Trial Notebook/08 - Jury Selection Notes/` | Voir dire question outlines, juror analysis cards, panel composition tracking |
| Tab 9 | `01 - Trial Notebook/09 - Case Analysis/` | All 9 case analysis reports, Cowork parallel analysis outputs, missing discovery demands |
| Tab 9 (Cowork) | `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` | Opening Statement outline, Closing Argument outline, Theme Tracker, Rebuttal Anticipation Memo (from `dw-trial-narrative-builder-crim`); DNA / Forensic Biology Audit Report (from `dw-dna-forensic-biology-auditor-crim`); Crime Lab Audit Report (from `dw-crime-lab-auditor-crim`); plus all other auditor findings and Cowork parallel analyses |

**Note:** Some case folders may have slight naming variations. Adapt to the folder structure
you find, but flag any non-standard organization in the gap report.

### 1B — Pretrial Notebook Scan

Also scan the Pretrial Notebook for trial-relevant items:

| Folder | What to Look For |
|--------|------------------|
| `02 - Pretrial Notebook/01 - Pleadings/` | Pretrial motions, bond motions, discovery motions, arraignment filings |
| `02 - Pretrial Notebook/02 - Discovery/` | Raw discovery productions, State's index, discovery compliance ledger |
| `02 - Pretrial Notebook/03 - Case Analysis & Notes/` | Initial Case Profile, LWOP Worksheet, Criminal Defense Cover, attorney notes |

### 1C — Case Tables Audit

Open `Case Tables.xlsx` at the case root and verify these sheets exist and are populated:

| Sheet | Phase | Status Check |
|-------|-------|-------------|
| Evidence Table | Phase 1 | Row count > 0; check for empty Review Priority or Defense Relevance columns |
| Timeline Sheet | Phase 2/3 | Row count > 0; check chronological ordering |
| Witness List | Phase 1 → 3 | Row count > 0; Priority (1–5) populated |


### 1D — Cross-Reference with Case Brain

Compare the scan results against the Case Brain's `COMPANION SKILL OUTPUTS` section:
- Flag any deliverable listed in the Case Brain but not found in the folder (moved? deleted?)
- Flag any deliverable found in the folder but not recorded in the Case Brain (update needed)

### 1E — Build the Inventory Table

Compile a complete inventory as a structured table:

| # | Deliverable | Expected Location | Status | File Name | Notes |
|---|------------|-------------------|--------|-----------|-------|
| 1 | Jury Instructions Package | Tab 1 | FOUND / MISSING / PARTIAL | [filename] | [any issues] |
| 2 | Verdict Form | Tab 8 | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

Use the full deliverable checklist in `references/deliverable-map.md` to ensure nothing
is missed.
