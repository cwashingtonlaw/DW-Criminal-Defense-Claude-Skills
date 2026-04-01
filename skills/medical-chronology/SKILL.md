---
name: medical-chronology
description: >
  Use this skill whenever a user uploads medical records (PDFs) and wants them
  summarized into a structured Medical Chronology. Triggers include: "summarize
  medical records", "fill out the medical chronology", "create a med chron",
  "medical summary for personal injury", or any upload of medical PDFs with a
  request to organize or summarize them. Outputs a filled-in Word (.docx) document
  matching the Medical Chronology template AND a plain-text markdown summary.
---

# Medical Chronology Skill

## Purpose

Transform raw medical record PDFs into a fully populated Medical Chronology Word
document plus a plain-text summary. The output faithfully replicates the standard
Medical Chronology template used for personal injury cases at Daniels & Washington.

---

## Dependencies

Read these skill files before writing any code or generating any output:

- `/mnt/skills/public/docx/SKILL.md` — for generating the Word document
- `/mnt/skills/public/pdf/SKILL.md` — for extracting text from PDFs

---

## Inputs

- One or more medical record PDFs uploaded by the user
- Optional (if not found in the records): client name, date of birth, date of incident

---

## Step-by-Step Workflow

### Step 1 — Check for Bate-Stamps

Before extracting any content, inspect each PDF page for existing Bate-stamp numbers
(typically a sequential number in the corner of each page, e.g., "000001", "P-001",
"Bates 0001").

- **If Bate-stamps are present**: Record the exact stamp for each page so it can be
  cited in output tables.
- **If Bate-stamps are absent**: Assign sequential stamps yourself, starting at
  `000001`, incrementing by 1 per page across all uploaded PDFs (treat a multi-PDF
  upload as one continuous document, stamped in the order the PDFs were provided).
  **Notify the user immediately** with a message like:

  > ⚠️ No Bate-stamps were detected in the uploaded records. I have assigned
  > sequential Bate-stamps (000001–XXXXXX) for citation purposes. Please review
  > and adjust if needed.

---

### Step 2 — Extract Raw Data from PDFs

Read all pages of all uploaded PDFs. Extract the following categories, recording
the Bate-stamp for every piece of information:

#### Patient Identifiers

- Full name
- Date of birth
- Date of incident/accident (DOI)

#### Current Accident Information (post-DOI)

**Injuries & Symptoms**

- Every complaint, symptom, or injury reported
- Date first reported + Bate-stamp

**Diagnostic & Imaging Reports**

- MRI, X-ray, CT, EMG, nerve conduction, ultrasound, bone scan, etc.
- Date of service, test name, significant findings, Bate-stamp

**Medical/Surgical Procedures**

- Date of service, procedure name (brief description), related diagnosis/complaints,
  Bate-stamp

**Medications Prescribed**

- Date prescribed, medication name, purpose/indication, Bate-stamp

**Impact on Life/Employment**

- Work status (working, off work, light duty, restricted, etc.)
- Impact on activities of daily living (ADLs) and quality of life
- Any documented disability rating or work restrictions
- Patient's condition as of the most recent records
- Future treatment recommended (if documented)

#### Past Medical History (prior to DOI)

**Prior Incidents/Injuries/Conditions**

- Date, type of incident/condition, related symptoms/treatment, last reported date
  prior to DOI, any noted aggravation of prior condition by current accident, Bate-stamp

**Prior Diagnostic & Imaging Reports**

- Date of service, test, significant findings, Bate-stamp

**Prior Medical/Surgical Procedures**

- Date of service, procedure (brief description), related diagnosis, Bate-stamp

**Prior Medications**

- Date prescribed, medication name, purpose, Bate-stamp

**Family/Social History** (if documented)

#### Subsequent Accidents/Injuries (after DOI, separate incident)

- Date of incident, type of incident (brief description), complaints/symptoms,
  aggravation of current case injuries, Bate-stamp

#### Provider List

- For each provider/facility: date range of treatment, facility name + specialty,
  number of visits, Bate-stamp range

---

### Step 3 — Flag Reviewer's Comments

While extracting data, actively identify and flag the following issues. Each flag
becomes a **Reviewer's Comment** in the output (red italic text in Word, prefixed
with `* Reviewer's Comment:`).

| Issue Type | What to Flag |
|---|---|
| **Contradicting information** | Conflicting dates, diagnoses, or findings across providers or records |
| **Illegible handwritten notes** | Pages or sections that cannot be read — note as "Illegible Notes" in the visit heading; leave content as `_____` |
| **Illegible/missing dates** | Render as `00/00/0000` |
| **Missing records** | Gaps in the timeline suggesting missing visits; records referenced but not present; providers mentioned but no records included |
| **Misinterpretations** | Notes where a prior transcription appears to misrepresent clinical findings |
| **Clarifications needed** | Ambiguous terminology, unclear causation attributions, inconsistent injury descriptions |

Collect all flags with their Bate-stamps for population into the Missing Medical
Records table and as inline Reviewer's Comments in the Detailed Chronology.

---

### Step 4 — Write the Brief Summary / Flow of Events

Draft a concise narrative (150–400 words) that:

- Describes the incident and how the patient initially presented
- Outlines major medical events in chronological order (key diagnoses, surgeries,
  significant test results, treatment milestones)
- Notes the patient's current status as of the last available record
- Highlights any significant prior history relevant to the case
- Is written in plain, professional language suitable for attorney review

This narrative goes at the top of the output document, immediately after the
header block.

---

### Step 5 — Populate the Word Document

Read `/mnt/skills/public/docx/SKILL.md` first, then generate the Word document
using python-docx. Follow the template section order exactly:

#### 5a — Header Block (top of document)

Four-cell table:

| CLIENT NAME | [value] | DATE OF BIRTH | [value] |
|---|---|---|---|
| DATE OF INCIDENT | [value] | SUMMARY UPDATE | [today's date] |

#### 5b — Brief Summary / Flow of Events

Narrative paragraph immediately below the header table.

#### 5c — Current Accident Information Tables

**Injuries & Symptoms**

| DATE FIRST REPORTED | COMPLAINTS / SYMPTOMS / INJURIES | BATE-STAMP |
|---|---|---|

**Diagnostic & Imaging Reports**

| DATE OF SERVICE | DIAGNOSTIC OR IMAGING REPORT (Test Performed) | SIGNIFICANT FINDINGS | BATE-STAMP |
|---|---|---|---|

**Medical/Surgical Procedures**

| DATE OF SERVICE | MEDICAL/SURGICAL PROCEDURE (Brief Description) | RELATED DIAGNOSIS (Complaints/Symptoms/Injuries) | BATE-STAMP |
|---|---|---|---|

**Medications Prescribed**

| DATE PRESCRIBED | MEDICATION | PURPOSE OF MEDICATION | BATE-STAMP |
|---|---|---|---|

**Impact on Life/Employment**
Narrative paragraph or bulleted list below the medications table.

#### 5d — Past Medical History Tables

**Prior Incidents/Injuries/Conditions**

| DATE | TYPE OF INCIDENT / INJURY / CONDITION | RELATED SYMPTOMS / TREATMENT | LAST REPORTED (Prior to DOI) | AGGRAVATION OF PRIOR CONDITION | BATE-STAMP |
|---|---|---|---|---|---|

**Prior Diagnostic & Imaging Reports**

| DATE OF SERVICE | DIAGNOSTIC OR IMAGING REPORT (Test Performed) | SIGNIFICANT FINDINGS | BATE-STAMP |
|---|---|---|---|

**Prior Medical/Surgical Procedures**

| DATE OF SERVICE | MEDICAL/SURGICAL PROCEDURE (Brief Description) | RELATED DIAGNOSIS (Complaints/Symptoms/Injuries) | BATE-STAMP |
|---|---|---|---|

**Prior Medications Prescribed**

| DATE PRESCRIBED | MEDICATION | PURPOSE OF MEDICATION | BATE-STAMP |
|---|---|---|---|

#### 5e — Summary of Subsequent Accidents and Injuries

| DATE OF INCIDENT | TYPE OF INCIDENT (Brief Description) | COMPLAINTS/INJURY/SYMPTOMS | AGGRAVATION OF INJURY (Current Case) | BATE-STAMP |
|---|---|---|---|---|

#### 5f — Missing Medical Records

| DATE | PROVIDER | MISSING RECORD | REASON RECORD NEEDED | BATE-STAMP |
|---|---|---|---|---|

#### 5g — Provider List

| DATE RANGE | FACILITY/PROVIDER + Specialty | NUMBER OF VISITS | BATE-STAMP |
|---|---|---|---|

#### 5h — Detailed Chronology

Four-column table: DATE | PROVIDER | OCCURRENCE/TREATMENT | BATE-STAMP

Each encounter occupies one row. The OCCURRENCE/TREATMENT cell contains labeled
sub-fields in this order:

```
Chief Complaint:     [text]
Physical Exam:       [text]
Findings/Impression: [text]
Medications:         [text]
Therapies:           [text]
Procedures:          [text]
Plan:                [text]
```

Leave a sub-field blank (do not omit the label) if the visit has no documented
content for that field.

#### 5i — Reviewer's Comments Summary

A dedicated section at the end of the document titled **"Reviewer's Comments Summary"**
listing all flagged issues with their Bate-stamp references.

---

#### Formatting Rules for Reviewer's Comments in Word

- Font color: red (RGB 255, 0, 0)
- Style: italic
- Prefix: `* Reviewer's Comment:`
- Placement: inline within the relevant table cell or chronology row where the issue
  was found, AND listed again in the Reviewer's Comments Summary section at the end

#### Illegible Content Rules

- Illegible dates → `00/00/0000`
- Illegible notes → `_____` with `(Illegible Notes)` appended to the row/visit heading

---

### Step 6 — Generate the Plain-Text Summary

Produce a Markdown (.md) file containing:

- Client name, DOB, DOI at the top
- Brief Summary narrative (same text as in the Word doc)
- Each section rendered as a Markdown table matching the column headers defined
  in Step 5
- A Reviewer's Comments section listing all flags with Bate-stamp references
- Provider list

This file is for quick reference and easy pasting into case management systems
such as Clio.

---

### Step 7 — Deliver Outputs

Copy both files to `/mnt/user-data/outputs/` and present them:

1. `[ClientLastName]_Medical_Chronology.docx`
2. `[ClientLastName]_Medical_Chronology_Summary.md`

Then provide a brief verbal report covering:

- Number of providers identified
- Date range of records reviewed
- Total number of Reviewer's Comments flagged (with a one-line breakdown by type)
- Whether Bate-stamps were self-assigned (and the range applied)
- Any notable gaps or high-priority issues the attorney should be aware of

---

## Quality Rules

- **Never alter clinical meaning** — capture information "as it is" in the records
- **Chronological order** — all tables and the Detailed Chronology must be sorted
  by date ascending
- **Bate-stamp every row** — no table row should be left without a Bate-stamp
  reference unless the information is derived (e.g., the Brief Summary)
- **Do not infer diagnoses** — only document what is explicitly stated in the records
- **Flag, don't omit** — if something is unclear, flag it as a Reviewer's Comment
  rather than leaving it out or guessing
- **Separate pre- and post-DOI records** — correctly categorize all information as
  current accident vs. prior history based on the date of incident
- **Zoom-in vs. zoom-out** — if the attorney specifies a detail level (all details /
  relevant details only), apply it consistently throughout the Detailed Chronology

---

## Example Trigger Phrases

- "Here are the medical records for John Smith. Can you create a medical chronology?"
- "Please summarize these PDFs into the medical chronology template."
- "Fill out the med chron for this PI case."
- "Organize these medical records — DOI was 3/15/2024."
- "Create a med chron from these records and flag anything that looks off."
