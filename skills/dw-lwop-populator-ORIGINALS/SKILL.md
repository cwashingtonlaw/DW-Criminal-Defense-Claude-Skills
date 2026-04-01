---
name: dw-lwop-populator
description: >
  Auto-populate LWOP review sheets for the District Defender. ALWAYS invoke for "LWOP
  sheet," "LWOP review," "District Defender review," or "life without parole worksheet."
  Reads discovery PDFs and fills the correct template (Homicide or Sex Offense) as .docx.
---

# LWOP Review Sheet Populator — Daniels & Washington

This skill reads discovery materials from a Calcasieu Parish criminal defense case folder and produces a populated LWOP Review Sheet as a Word document (.docx). The Calcasieu Parish Public Defender's Office requires these sheets for every case carrying Life Without Parole exposure, submitted to the District Defender.

There are two templates — **Homicide** and **Sex Offense** — and the skill selects the correct one based on the charges.

---

## The Cardinal Rule: Zero Field Omission

Every field listed in `references/field-maps.md` must appear in the output document. No exceptions. The form can be redesigned for readability — color-coded sections, improved typography, better table layout — but the information captured must be **complete and identical** to what the original PDO template asks for. If a field has no data, leave its value cell blank. Never delete, merge away, or skip a field.

Before saving the final document, run the field-completeness checklist in Step 6.

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

Read the docx skill (at the path listed in your available skills) for the full unpack/edit/repack procedure.

Use the **unpack → edit XML → repack** approach to fill in the template:

```bash
# 1. Copy the correct template from this skill's assets/ folder
cp "assets/LWOP Homicide Review Sheet - FOR TYPING.docx" working/template.docx

# 2. Unpack
python <docx-skill-path>/scripts/office/unpack.py working/template.docx working/unpacked/

# 3. Edit the XML cells in working/unpacked/word/document.xml
#    (Use the Edit tool to find label cells and fill adjacent data cells)

# 4. Repack
python <docx-skill-path>/scripts/office/pack.py working/unpacked/ output.docx --original working/template.docx

# 5. Validate
python <docx-skill-path>/scripts/office/validate.py output.docx
```

**How the templates are structured:**
The templates are organized into 8 color-coded sections, each its own table:
1. **Key Dates & Deadlines** (blue-gray) — quick-reference summary
2. **Case Information** (blue) — defendant, charges, victims, witnesses, co-defendant details
3. **Defendant Statement** (red) — statement substance
4. **Suppression Analysis** (deep orange) — Miranda sub-fields + suppression determination (consolidated from old Discovery + Defendant Statement sections)
5. **Motions** (orange) — all pretrial motions including bond reduction sub-fields
6. **Investigation** (green) — investigator assignment and results
7. **Evidence Inventory** (purple) — what evidence exists, with counts for videos/photos/statements/reports
8. **Records & Authorizations** (teal) — HIPPA dates, school records, IEP

Each table uses `<w:tbl>` with rows (`<w:tr>`) and cells (`<w:tc>`). Each field label is in one cell, and the adjacent cell is where data goes. To populate a field:

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

**UI Enhancements (encouraged):**
You may improve the visual design of the document to make it more readable and professional — for example:
- Color-coded section headers (e.g., blue for Case Info, red for Motions, green for Discovery)
- Alternating row shading in tables
- Better typography and cell padding
- Visual separation between major sections

The only constraint is that every field from the template must remain present and fillable. The information is sacred; the layout is not.

### Step 6: Field-Completeness Checklist (Mandatory)

Before saving the final document, verify every field is present by walking through the appropriate checklist from `references/field-maps.md`. The checklists are organized by template type (Homicide or Sex Offense) and list every single cell that must exist in the output.

For each field on the checklist:
1. Confirm the field label exists in the output document
2. Confirm the data cell is present (populated with extracted data, or blank if no data — but the cell itself exists)
3. If a field is missing, stop and add it before proceeding

Log any fields left blank and the reason (missing discovery, attorney-only field, etc.) for the completion notes.

### Step 7: Produce Completion Notes

After generating the document, provide a brief summary:

1. **Fields populated** — which fields were filled and from which source documents
2. **Fields left blank** — which fields could not be populated and why (reference the exact field name from the checklist)
3. **Conflicts found** — contradictions between sources the attorney should review
4. **Missing discovery** — documents referenced in police reports but absent from folder
5. **Suppression flags** — Miranda/search/seizure issues identified during extraction

### Step 8: Save and Present

Save the output to the case folder:
`LWOP [Homicide/Sex Offense] Review Sheet - ([Client Last Name]).docx`

Example: `LWOP Homicide Review Sheet - (Cole).docx`

---

## What Claude Populates vs. What the Attorney Completes

The review sheet is a collaboration. Claude fills in factual data from discovery. The attorney makes judgment calls.

**Claude populates:**
- Key Dates & Deadlines summary (offense, arrest, indictment, arraignment, discovery, court dates)
- All identifying information (name, docket, dates, co-defendants, victims)
- Co-defendant details (separately charged?, plea status, cooperating?)
- Charges and aggravating factors (from charging instruments and reports)
- Witness lists with counts and statement summaries
- Police report summaries
- Defendant statement details
- Suppression Analysis section — all 7 Miranda sub-fields (advised?, invoked?, voluntary?, Reid?, confession?, credible?, against interest?) plus suppression determination and basis
- Evidence Inventory with counts (police reports, videos, photos, witness statements)
- Lab reports by type (DNA, tox, ballistics) and by party column (Deceased/Accuser, Client, Co-Defendant, Witness)
- Bond Reduction sub-fields (Date filed, Original amount, Bond after reduction hearing)
- Motions already filed (dates and types)
- Investigation section (from investigator request forms)
- Records & Authorizations — HIPPA dates (Signed, Requested, Received) each separately, School Records and IEP dates each separately

**Attorney completes (leave blank or mark "Preliminary — attorney review required"):**
- Theory of the Case (both Initial and Trial) — unless attorney already noted this
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

When invoked as part of Phase 0 of the `dw-criminal-defense` workflow:
- Save to `Pretrial Notebook → 03 - Case Analysis & Notes` as `001 - LWOP Worksheet.docx`

When invoked standalone:
- Save to the root of the client's case folder with the naming convention above

## Updating an Existing Sheet

When new discovery arrives and the attorney wants the sheet updated:
1. Read the existing populated LWOP sheet
2. Read the new discovery documents
3. Merge new information — add to witness lists, update discovery checklist, flag new issues
4. Do not overwrite attorney-entered content (trial theory, defense strategy, attorney notes)
5. Note in completion summary what was added or changed
