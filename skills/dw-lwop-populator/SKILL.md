---
name: dw-lwop-populator
description: >
  Auto-populate LWOP review sheets for the District Defender. ALWAYS invoke for "LWOP
  sheet," "LWOP review," "District Defender review," or "life without parole worksheet."
  Reads discovery PDFs and fills the correct template (Homicide or Sex Offense) as .docx.
---

# LWOP Review Sheet Populator — Daniels & Washington

This skill reads discovery materials from a Calcasieu Parish criminal defense case folder and produces a populated LWOP Review Sheet as a Word document (.docx). The Calcasieu Parish Public Defender's Office requires these sheets for every case carrying Life Without Parole exposure, submitted to the District Defender.

There are two templates — **Homicide** and **Sex Offense** — and the skill selects the correct one based on the charges. The populated sheet preserves the original formatting, letterhead, and layout of the official PDO template.

### Source Citation Mandate

Every factual entry populated on the LWOP Review Sheet must trace back to a specific source document in the case file. The District Defender reviews these sheets to assess resource allocation and case strategy — inaccurate or unsourced entries undermine that assessment and waste the reviewing attorney's time.

**Citation format:** Cite the document title, page number, and paragraph. Examples:
- `(Arrest Report — LCPD Case #2026-00456, p. 2, para. 3)`
- `(Autopsy Report, p. 4, Cause of Death)`
- `(Witness Statement of Jane Doe, p. 2, para. 4)`
- `(Bill of Information, Count 1)`
- `(Discovery Production, Bates #00145-00148)`
- `(Criminal History Record, NCIC Report, p. 3)`

**Unsourced entries:** If a field cannot be populated from a specific document, mark it `[UNSOURCED — VERIFY]` rather than guessing. The attorney will fill it from client interview or additional discovery.

**Where sourcing applies:** All factual fields on the LWOP sheet — charges, facts of the offense, witness information, criminal history, and case assessment entries.

---

## When This Skill Runs

This skill activates when:
- An attorney says "fill out the LWOP sheet" or "populate the LWOP review" for a client
- A case folder is identified as having LWOP exposure during Phase 0 of the dw-criminal-defense workflow
- The user uploads or points to discovery files and asks for case review sheet population
- The user wants to update an existing LWOP sheet after receiving new discovery

## What You Need Before Starting

1. **A case folder path** — either the client's subfolder (e.g., `Cole, Lindsey/`) or a set of uploaded files
2. **Discovery documents** — at minimum, the charging instrument (indictment/bill) and police report. The more discovery available, the more complete the sheet.
3. **The template files** are bundled in this skill's `assets/` folder:
   - `LWOP Homicide Review Sheet - FOR TYPING.docx`
   - `LWOP Sex Offense Review Sheet - FOR TYPING.docx`

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## Step-by-Step Workflow

### Step 1: Survey the Case Folder

List all files in the case folder. Categorize each file by document type using the patterns in `references/extraction-patterns.md`.

Produce a mental inventory: charging instruments, police reports, defendant statements, witness statements, autopsy/SANE, CAC interviews, lab reports, criminal history, existing LWOP sheets, Criminal Defense Cover, D&W analysis spreadsheets.

### Step 2: Determine the Case Type

Read `references/field-maps.md` — specifically the "Determining Case Type" section.

Check the charges from the charging instrument (or folder name if no charging instrument yet):
- **Homicide charges** (La. R.S. 14:30, 14:30.1, 14:31) → Use the **Homicide** template
- **Sex offense charges** (La. R.S. 14:42, 14:42.1, 14:43, 14:43.1, 14:81.2) → Use the **Sex Offense** template
- **Both** → Generate both sheets
- **Unclear** → Ask the attorney

### Step 3: Extract Data from Discovery

Read each document in priority order (see `references/extraction-patterns.md` — "Extraction Priority Order"). For each document, extract the information mapped to review sheet fields as defined in `references/field-maps.md`.

**For large case folders (20+ files):** Prioritize the charging instrument first (gives you the framework), then police report (narrative backbone), then defendant statement (suppression analysis), then autopsy/SANE (forensic evidence), then remaining materials.

**Reading files:**
- PDFs: use `pandoc` or the PDF skill's text extraction
- .docx: use `pandoc` to convert to markdown
- .xlsx: use Python with openpyxl to read spreadsheet data

### Step 4: Check for Existing Data

Before generating a new sheet, check if an existing LWOP sheet, Criminal Defense Cover, or Defense Shield/Case Tables spreadsheets already exist with data. If an existing LWOP sheet exists, read it and merge — keep any attorney-entered data (especially Theory of the Case, Defenses, attorney notes) and supplement with newly extracted information.

### Step 5: Generate the Populated Document

Use the **unpack → edit XML → repack** approach to fill in the template while preserving the official PDO formatting:

```bash
# 1. Copy the correct template from this skill's assets/ folder
cp "assets/LWOP Homicide Review Sheet - FOR TYPING.docx" working/template.docx

# 2. Unpack
python /mnt/.skills/skills/docx/scripts/office/unpack.py working/template.docx working/unpacked/

# 3. Edit the XML cells in working/unpacked/word/document.xml
#    (Use the Edit tool to find label cells and fill adjacent data cells)

# 4. Repack
python /mnt/.skills/skills/docx/scripts/office/pack.py working/unpacked/ output.docx --original working/template.docx

# 5. Validate
python /mnt/.skills/skills/docx/scripts/office/validate.py output.docx
```

Read the docx skill (`/mnt/.skills/skills/docx/SKILL.md`) for the full unpack/edit/repack procedure if you need a refresher.

**How the templates are structured in XML:**
Both templates use `<w:tbl>` (Word tables) with rows (`<w:tr>`) and cells (`<w:tc>`). Each field label (like "STATE v.") is in one cell, and the adjacent cell is where data goes. To populate a field:

1. Find the cell containing the label text (e.g., `STATE v.`)
2. Locate the adjacent/next cell in the same row
3. Replace the empty `<w:t/>` or `<w:t xml:space="preserve"> </w:t>` with the extracted data
4. Preserve all `<w:rPr>` and `<w:pPr>` formatting from the cell

**For multi-line content** (witness statements, aggravating factors, etc.):
- Use multiple `<w:p>` paragraphs within the cell
- For bullet lists, use separate paragraphs — each starts with a bold name and colon, then details
- Bold key names and direct quotes, matching the formatting conventions in the completed example sheets

**Formatting conventions observed in completed examples (Cole, Dugas, Ruano):**
- Witness names are **bolded**
- Direct quotes from statements are **bolded**
- Each witness gets its own bullet/paragraph with sub-details
- Charges include the Louisiana statute number (e.g., "14:42 First Degree Rape")
- Prior convictions formatted as: `MM-DD-YYYY -- Offense Name`
- Aggravating factors include specific alleged acts, not just legal categories

### Step 6: Produce Completion Notes

After generating the document, provide a brief summary:

1. **Fields populated** — which fields were filled and from which source documents
2. **Fields left blank** — which fields could not be populated and why
3. **Conflicts found** — contradictions between sources the attorney should review
4. **Missing discovery** — documents referenced in police reports but absent from folder
5. **Suppression flags** — Miranda/search/seizure issues identified during extraction

### Step 7: Save and Present

Save the output to the case folder:
`LWOP [Homicide/Sex Offense] Review Sheet - ([Client Last Name]).docx`

Example: `LWOP Homicide Review Sheet - (Cole).docx`

---

## What Claude Populates vs. What the Attorney Completes

The review sheet is a collaboration. Claude fills in factual data from discovery. The attorney makes judgment calls.

**Claude populates:**
- All identifying information (name, docket, dates, co-defendants, victims)
- Charges and aggravating factors (from charging instruments and reports)
- Witness lists and statement summaries
- Police report summaries
- Defendant statement details including Miranda analysis
- Discovery checklist (what's present, what's missing)
- Motions already filed (dates and types)
- Investigation section (from investigator request forms)
- Preliminary suppression analysis (flagging issues for attorney)

**Attorney completes (leave blank or mark "Preliminary — attorney review required"):**
- Theory of the Case (both initial and trial) — unless attorney already noted this
- Final defense strategy
- "Does Defendant want to testify?" — always leave blank
- Any field requiring attorney judgment or client communication

## Detail Level and Voice

Match the depth and tone of the completed examples in the caseload. The voice is factual and objective — report what the documents say without editorializing.

- **Witness statements** get detailed multi-paragraph summaries with direct quotes bolded
- **Aggravating factors** include specific alleged acts described in the discovery
- **Police report summaries** include specific times, locations, officer actions
- **Prior convictions** include date, offense name, and disposition where available

## Working with the dw-criminal-defense Skill

When invoked as part of Phase 0 of the `dw-criminal-defense` workflow or standalone, follow shared protocols for output paths (see Step 0.5).

## Updating an Existing Sheet

When new discovery arrives and the attorney wants the sheet updated:
1. Read the existing populated LWOP sheet
2. Read the new discovery documents
3. Merge new information — add to witness lists, update discovery checklist, flag new issues
4. Do not overwrite attorney-entered content (trial theory, defense strategy, attorney notes)
5. Note in completion summary what was added or changed
