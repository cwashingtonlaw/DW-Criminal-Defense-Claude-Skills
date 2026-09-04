# Contract 3: Cross-Examination Outlines — Full Schema

Read from the SKILL.md **Contract 3: Cross-Examination Outlines** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producer:** `dw-cross-exam-architect-crim`
**Consumers:** `dw-trial-notebook-builder-crim`, `dw-case-brain-crim`

### One Deliverable per Witness

| # | Deliverable | Format | Filename Pattern |
|---|------------|--------|-----------------|
| 1 | Cross-Examination Outline | .docx | `Cross-Examination — [Witness Name].docx` |

**No Source Catalog and no Combined Sources PDF.** The skill stopped producing them; the Source Register inside the outline is its only index. Outlines built before that change may still have `Source Catalog — [Witness Name].pdf` and `Combined Sources — [Witness Name].pdf` beside them — consumers should read those where they exist and never expect them for a new build.

### Cross-Examination Outline Required Structure

Assembled in this order: cover page · Source Register · chapters · Discovery Gap Report · Preservation Log.

**Source Register** — page 2, three columns, header shaded blue `D6E4F0`:

| Column | Description | Required |
|--------|-------------|----------|
| Source Number | Permanent `(N)`, never reassigned | Yes |
| Evidence Item | Document title as it actually appears; carries the date where one distinguishes versions | Yes |
| Reference/Bates | Bates range, page span, timestamp range, evidence item number, or filing citation | Yes |

**Chapters** — one per page, two-column table plus a blank notes box:

| Field | Description | Required |
|-------|-------------|----------|
| Chapter Title | Topic area for this line of questioning, tied to the case theme | Yes |
| Witness | Full name and role of the witness | Yes |
| Goals | What this chapter aims to establish (2–4); Impact/Fragility for law enforcement | Yes |
| Source/Exhibit | Bulleted, each beginning with its `(N)` register number. Header shaded blue `D6E4F0` | Yes |
| Questions | Numbered, restarting at 1 in each chapter. Header shaded red `F4CCCC` | Yes |
| Notes — Witness Responses | Blank bordered box, ~5 lines, spanning both columns, label shaded yellow `FFF2CC`. Delivered empty for the attorney to write in | Yes |

No third column, and no expected answers, branch logic, impeachment bullets, evidentiary flags, preservation bullets or strategy notes on any chapter page. Branch logic and flags are reported to the attorney at build time; ground-to-state and proffer-substance are pre-filled columns in the Preservation Log.

**Formatting:** Times New Roman 12 pt, 1" margins, landscape chapter pages, page numbers bottom right (`Page N of M`), work product marking in the header.

### Output Location
`01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/` or `Defense Witnesses/`
