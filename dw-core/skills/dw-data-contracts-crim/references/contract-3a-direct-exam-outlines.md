# Contract 3A: Direct-Examination Outlines — Full Schema

Read from the SKILL.md **Contract 3A: Direct-Examination Outlines** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producer:** `dw-direct-exam-architect-crim`
**Consumers:** `dw-trial-notebook-builder-crim`, `dw-case-brain-crim`

### One Deliverable per Defense Witness

| # | Deliverable | Format | Filename Pattern |
|---|------------|--------|-----------------|
| 1 | Direct-Examination Outline | .docx | `Direct-Examination — [Witness Name].docx` |

Plus an indexing summary copy at `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Direct-Exam Summary - [Witness Name] - [YYYY-MM-DD].docx`.

**No Source Catalog and no Combined Sources PDF.** The skill stopped producing them; the Source Register inside the outline is its only index. Outlines built before that change may still have `Source Catalog — [Witness Name] Direct.pdf` and `Combined Sources — [Witness Name] Direct.pdf` beside them — consumers should read those where they exist and never expect them for a new build.

### Direct-Examination Outline Required Structure

**Identical to Contract 3 (cross-examination).** Assembled in order: cover page · Source Register · chapters · Discovery & Notice Gap Report · Preservation Log · Rehearsal & Prep Schedule.

**Source Register** — page 2, three columns, header shaded blue `D6E4F0`:

| Column | Description | Required |
|--------|-------------|----------|
| Source Number | Permanent `(N)`, never reassigned | Yes |
| Evidence Item | Document title as it actually appears; carries the date where one distinguishes versions | Yes |
| Reference/Bates | Bates range, page span, timestamp range, or self-authentication citation | Yes |

"Personal knowledge" is not a register entry — it appears in the SOURCE/EXHIBIT cell as `Personal knowledge — foundation at Q[#]`.

**Chapters** — one per page, two-column table plus a blank notes box:

| Field | Description | Required |
|-------|-------------|----------|
| Chapter Title | Topic area for this line of questioning, tied to the case theme | Yes |
| Witness | Full name and role of the witness | Yes |
| Goals | What this chapter aims to establish for the defense theory (2–4) | Yes |
| Source/Exhibit | Bulleted, each beginning with its `(N)` register number, or a personal-knowledge foundation reference. Header shaded blue `D6E4F0` | Yes |
| Questions | Open-ended, non-leading (who/what/when/where/how/why/describe/explain), numbered, restarting at 1 in each chapter. Header shaded red `F4CCCC` | Yes |
| Notes — Witness Responses | Blank bordered box, ~5 lines, spanning both columns, label shaded yellow `FFF2CC`. Delivered empty for the attorney to write in | Yes |

No third column. Foundation requirements are built into the question order rather than noted beside it. Anticipated answers, anticipated cross-attack vectors, redirect plans, demeanor cues, rehearsal items and evidentiary flags are **reported to the attorney at STEP 5, never printed on a chapter page**; ground-to-state and proffer-substance are pre-filled columns in the Preservation Log. The one inline annotation permitted is a `[LEADING OK — basis]` tag in the QUESTIONS cell.

**Formatting:** Times New Roman 12 pt, 1" margins, landscape chapter pages, page numbers bottom right (`Page N of M`), work product marking in the header — the same spec as Contract 3.

### Output Location

`01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`
