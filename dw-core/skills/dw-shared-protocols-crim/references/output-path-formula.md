# Output Path Formula

Standardized output path convention for all D&W file-writing skills. Anchored on `CASE_ROOT` (exposed as a YAML variable in `dw-case-brain-crim` v3.3+).

## Core principle

Every file-writing skill MUST anchor its output on `CASE_ROOT`. Never write to absolute paths, user home, Desktop, or arbitrary locations. The case folder is the source of truth for everything related to a matter.

## CASE_ROOT resolution

`CASE_ROOT` is resolved by `dw-case-brain-crim` based on the case parish/jurisdiction:

| Source | Path pattern |
|---|---|
| Calcasieu PDO | `/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/CALCASIEU PDO Files/[Client Folder]` |
| NOLA Conflict | `/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/NOLA Conflict Cases/[Client Folder]` |
| D&W private (paid retainer) | `/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/D&W Law Firm (CJW)/[Client Folder]` |

Consuming skills must read `CASE_ROOT` from the active Case Brain, never hardcode a path.

## Standard subfolder structure under CASE_ROOT (firm legacy convention)

```
{{CASE_ROOT}}/
├── 01 - Trial Notebook/
│   ├── 01 - Jury Instructions & Selection/    # Voir dire, jury charges, verdict forms
│   ├── 03 - Witnesses/                        # Impeachment worksheets, cross outlines
│   │   ├── Prosecution Witnesses/
│   │   └── Defense Witnesses/
│   ├── 05 - Evidence/                         # Bate-stamped, OCR'd docs + A/V
│   └── 09 - Case Analysis/                    # Internal work product
│       └── Cowork Analysis/                   # Auditor outputs, Reports 2-7/9, internal analyses
└── 02 - Pretrial Notebook/
    ├── 01 - Pleadings/                        # All filed motions, memos, oppositions
    ├── 02 - Discovery/                        # Raw discovery as received
    ├── 03 - Case Analysis & Notes/            # Case Profile, LWOP, warrant audits, expert reports
    └── 06 - Law & Research/                   # Caselaw, demand letters, post-conviction
```

Additional firm folders that may exist at the case root (not used by motion skills directly):
- `05 - Billing/` — billing narratives and time entries
- Optional Phase 0 documents live in `02 - Pretrial Notebook/03 - Case Analysis & Notes/` with the `000 -`, `001 -`, `002 -` numeric prefix scheme.

## Output path formula by skill type

### Filed pleadings (motions, oppositions, memos)

```
{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/[YYYY-MM-DD] - [MotionType] - [ShortDescriptor].docx
```

Examples:
- `02 - Pretrial Notebook/01 - Pleadings/2026-04-28 - Motion to Suppress - Stop and Search.docx`
- `02 - Pretrial Notebook/01 - Pleadings/2026-04-28 - Motion to Suppress - Stop and Search - Proposed Order.docx`
- `02 - Pretrial Notebook/01 - Pleadings/2026-04-28 - Motion to Suppress - Stop and Search - Notice of Hearing.docx`
- `02 - Pretrial Notebook/01 - Pleadings/2026-04-28 - Opposition 404B - Prior Battery.docx`

### Auditor reports (warrant audits, expert challenges, case-specific audits with a charging-document nexus)

```
{{CASE_ROOT}}/02 - Pretrial Notebook/03 - Case Analysis & Notes/[NNN] - [Audit Type] - [Client Last Name].docx
```

Examples:
- `02 - Pretrial Notebook/03 - Case Analysis & Notes/050 - Search Warrant Audit - Cole.docx`
- `02 - Pretrial Notebook/03 - Case Analysis & Notes/051 - Habitual Offender Audit - Cole.docx`

### Internal analysis / Cowork audit deliverables (cross-cutting analysis, witness threat matrices, investigator tasking, Brady audits, forensic audits)

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/[Descriptor] - [Date].docx
```

Examples:
- `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Brady-Giglio Audit - Officer Smith - 2026-04-28.docx`
- `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Witness Threat Matrix - 2026-04-28.docx`
- `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Pre-Trial Motion Action Plan - Cole - 2026-04-28.docx`

### Sentencing materials

All sentencing-phase materials go to `{{CASE_ROOT}}/01 - Trial Notebook/08 - Verdict_Sentencing/`. This includes mitigation memoranda, PSI objections, sentencing letters, and any other sentencing work product. Filed sentencing pleadings (e.g., formal sentencing memoranda submitted to the court) also go to `02 - Pretrial Notebook/01 - Pleadings/`.

### Case Brain

```
{{CASE_ROOT}}/02 - Pretrial Notebook/03 - Case Analysis & Notes/000 - Case Profile.docx
```

(Note: Case Brains live in the Obsidian "Dream Team Law" vault; the `000 - Case Profile.docx` is the case-folder snapshot.)

### Trial notebook

The completed trial notebook is assembled in place using the existing `01 - Trial Notebook/` structure — `dw-trial-notebook-builder-crim` indexes the curated tabs rather than creating a new one.

### Discovery deliverables

```
{{CASE_ROOT}}/02 - Pretrial Notebook/02 - Discovery/[YYYY-MM-DD] - [Production Label]/
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/[YYYY-MM-DD] - Discovery Triage.docx
```

A/V files copied to `01 - Trial Notebook/05 - Evidence/` (no duplicates).

## Filename conventions

- **Date prefix:** ISO 8601 (`YYYY-MM-DD`) for chronological sorting on filed pleadings and dated audit/internal deliverables
- **3-digit numeric prefix:** Used inside `02 - Pretrial Notebook/03 - Case Analysis & Notes/` and `01 - Trial Notebook/05 - Evidence/` per firm convention (e.g., `000 - Case Profile.docx`, `010 - Incident Report.pdf`)
- **Separator:** Use ` - ` (space-hyphen-space) rather than underscores; this matches the firm's existing folder/file scheme
- **Type tag:** Plain English, title case (e.g., `Motion to Suppress`, `Opposition 404B`, `Memorandum in Support`)
- **Suffix tags:** ` - Filed`, ` - Draft`, ` - Proposed Order`, ` - Notice of Hearing`, ` - Internal`
- **Extension:** `.docx` for editable documents, `.pdf` for finals/exhibits/catalogs

## Versioning

When iterating on a draft, use suffix ` - v2`, ` - v3`, etc., or move prior versions to an `_archive/` subfolder. Do not overwrite a filed version. The filed version is preserved with a ` - Filed` suffix and timestamp.

## What NOT to do

- Do not write to `~/Desktop/`, `~/Downloads/`, or `/tmp/`
- Do not invent subfolder names not in the standard structure above
- Do not write to a path outside `CASE_ROOT` for case-specific work
- Do not hardcode `CASE_ROOT` — always read from the active Case Brain
- Do not skip the date prefix on filed pleadings — chronological order matters for case file integrity
- Do not use the deprecated PascalCase scheme (`04_Motions/`, `03_Auditor_Reports/`, etc.) — that scheme never matched the firm's actual folders

---

**v1.1 — Aligned with firm's legacy folder convention. Previous PascalCase scheme (`04_Motions/Pretrial/`, `03_Auditor_Reports/`, `05_Internal_Analysis/`, etc.) deprecated.**
