# Phase 1 Step 3 — Case Profile Procedure (Detailed)

This file contains the full procedural detail for Phase 1 Step 3 (Generate Case Profile). The SKILL.md spine summarizes Step 3 and points here; this file is the operating manual.

For the LWOP-specific field schema and extraction rules, see:
- `lwop-field-maps.md` — complete field schema for Part 2A (Homicide) and Part 2B (Sex Offense)
- `lwop-extraction-patterns.md` — how to extract each field from discovery (filename patterns, content markers, sourcing rules)

---

## Overview

**Output:** `000 - Case Profile.docx` → save to `Pretrial Notebook → 03 - Case Analysis & Notes`
**Source template:** `assets/CASE PROFILE.docx` — copy this template to the output path before populating.

This single document replaces the former Initial Case Profile, Criminal Defense Cover, and (where applicable) the standalone LWOP review sheet. It follows the lifecycle of a criminal case — from identification through disposition — so the attorney can use it as a living reference from intake through trial.

The template has two parts:

- **Part 1 — Case Profile** (six sections). Populate for **every** case.
- **Part 2 — Case-Type Specific Review Sheet.** Populate **exactly one** of Part 2A, 2B, or 2C based on the charges:
  - **Part 2A — LWOP Homicide** — for cases with LWOP exposure on a homicide charge (La. R.S. 14:30, 14:30.1). Submit to the District Defender per Calcasieu PDO requirements.
  - **Part 2B — LWOP Sex Offense** — for cases with LWOP exposure on a sex offense charge (La. R.S. 14:42, 14:42.1, 14:43, 14:43.1, 14:81.2). Submit to the District Defender 30 days after appointment and every consecutive 30 days.
  - **Part 2C — Other Felony** — for non-LWOP felony cases. No District Defender submission requirement.

If the case carries both homicide and sex offense LWOP exposure, populate both Part 2A and Part 2B.

---

## Operating Modes

Step 3 has two operating modes. Pick the right one before starting.

**Initial Generation Mode** — runs as part of Phase 1 intake when no `000 - Case Profile.docx` exists yet on the case file. Populates the entire document end-to-end.

**Refresh Mode** — runs when `000 - Case Profile.docx` already exists and new discovery has arrived. Updates Part 2A/2B fields from the new discovery only. **Never** overwrites attorney-entered content. **Never** re-touches Part 1 Sections 1–6 unless the attorney explicitly says "rebuild the Case Profile."

Triggers for Refresh Mode:
- "Update the LWOP review"
- "Refresh the Case Profile"
- "New discovery came in — update Part 2A"
- "Re-pull the LWOP fields"
- The case folder already contains `000 - Case Profile.docx` AND new discovery has been added since its last modification

Initial Generation Mode is the default. If unclear which mode applies, ask the attorney.

---

## Part 1 — Case Profile (always completed)

**Section 1 — Case Identification**
- Client Name | DOB | SS# | Address | Phone | Email
- Docket # | Court | Division | Judge
- Date of Offense | Date of Arrest | Date of Hire
- Co-Defendant(s) (if any)
- **Cowork populates** from court filings and intake documents where available. **Staff/Attorney completes** remaining client demographic fields.

**Section 2 — Charges & Exposure**
- All charges with Louisiana statutory citations
- Maximum penalty for each count
- Elements the prosecution must prove for each count
- Any mandatory minimums flagged
- Habitual offender exposure (if applicable)
- Responsive verdicts for each charge (reference `Art 814 Responsive Verdicts`)

**Section 3 — Arraignment & Bail**
- Arraignment: Date | Charges Read | Prosecutor | Judge
- Plea entered
- Bail status: ROR / REMAND / BAIL SET — record bond amounts
- Conditions of release
- **Populate from court filings when available; leave blank fields for attorney completion.**

**Section 4 — Case-Specific Defenses**
Review all available case file materials — arrest reports, police narratives, witness statements, evidence logs, bodycam summaries, transcripts, and any other intake documents. Identify defenses grounded in what the case file actually contains. This is not a list of generic defenses.

For each potential defense, include:
- The defense theory
- The specific evidence or document supporting it (with Bate stamp reference)
- Constitutional issues flagged (unlawful stop, Miranda violations, warrant defects)
- Factual weaknesses in the State's case (inconsistent accounts, evidence gaps, timeline conflicts)
- Affirmative defenses supported by the facts
- Recommendation for attorney investigation

**Section 5 — Client Background** *(Attorney completes after client interview)*
- Prior Criminal History
  - **Format guidance for LWOP cases (Part 2A or 2B applies):** Use structured list `MM-DD-YYYY — Offense Name (Disposition)`, one prior per line. The District Defender expects rap-sheet-style summaries on submitted forms. Pull from the client's NCIC printout / RAP sheet. Include dispositions where available.
  - **Format guidance for non-LWOP cases:** Narrative form is acceptable.
- Family / Home Life
- Educational History
- Employment History
- Medical / Mental Health
- Military Service (if applicable)

**Section 6 — Key Dates & Next Steps**
- Next Court Date (from Google Calendar)
- Bill/Indictment Date
- Discovery deadlines
- Motion filing deadlines

---

## Part 2 — Case-Type Specific Review Sheet

Populate exactly one of Part 2A, 2B, or 2C. None of these fields duplicate Part 1 — they capture only the case-development detail required for that case type.

**Common to 2A / 2B / 2C** (every case-type branch contains these nine sections):
1. **Key Dates (LWOP/case-specific):** Age at Time of Offense | Discovery Filed (date) | Discovery Received (date) | Trial Date
2. **Co-Defendant Details:** Separately Charged? | Plea Status | Cooperating with State?
3. **Case Specifics** — *differs per case type, see below*
4. **Defendant Statement:** substance + voluntariness flags
5. **Suppression Analysis:** Miranda advised/invoked, Voluntary, Reid technique, Confession, Statements credible, Against client's interest, Suppression motion Y/N + Why + basis
6. **Motions:** Discovery, Bill of Particulars, Suppression(s), In Limine, Reveal the Deal, Bond Reduction (filed?, date filed, original amount, post-hearing amount), Speedy Trial, Other Motions, Reports Checklist, Prescription, Defendant testify? [ATTORNEY]
7. **Investigation:** Investigator Assigned | Request Form Completed On | Requested by Attorney | Results
8. **Evidence Inventory** — *differs per case type, see below*
9. **Records & Authorizations:** HIPAA Y/N, Date Signed, Date Requested, Date Received, School Records, IEP, Date Records Requested, Date IEP Requested

**Part 2A — LWOP Homicide-specific fields (Sections 3 and 8 only):**
- Section 3: Alleged Victim(s) (* by name of any deceased) | Aggravating Factors (La. C.Cr.P. art. 905.4) | Theory of the Case — Initial [ATTORNEY] | Theory of the Case — Trial [ATTORNEY] | Witnesses (numbered list) | Witness Statements (numbered list) | Police Report Summary | Possible Defense Witnesses [ATTORNEY]
- Section 8: standard evidence inventory PLUS **Autopsy — Performed by**, **Autopsy — Date first read by attorney**, and lab column **Deceased** (alongside Client / Co-Defendant / Witness)
- Footer: "Submission: To be submitted to the District Defender."

**Part 2B — LWOP Sex Offense-specific fields (Sections 3 and 8 only):**
- Section 3: Alleged Victim(s) (include ages & DOBs) | Aggravating Factors (focus on age of victim, relationship to defendant, use of force, threats, position of trust/authority) | Theory — Initial [ATTORNEY] | Theory — Trial [ATTORNEY] | Witnesses | Witness Statements | Police Report Summary | Possible Defense Witnesses [ATTORNEY]
- Section 8: standard evidence inventory PLUS **SANE Exam — Performed by**, **SANE Exam — Date first read by attorney**, **CAC Video — Is it viewable?**, **CAC Video — Date first viewed by attorney**, and lab column **Accuser** (alongside Client / Co-Defendant / Witness)
- Footer: "Submission: To be submitted to the District Defender 30 days after appointment and again every consecutive 30 days."

**Part 2C — Other Felony-specific fields (Sections 3 and 8 only):**
- Section 3: Alleged Victim(s) / Complainant(s) (if applicable) | Charging Instrument Attached (Indictment or Bill of Information — Y/N) | Theory — Initial [ATTORNEY] | Theory — Trial [ATTORNEY] | Witnesses | Witness Statements | Police Report Summary | Possible Defense Witnesses [ATTORNEY]
- Section 8: standard evidence inventory PLUS **Physical Evidence Inventory** (weapons, drugs, paraphernalia, clothing, etc.), **Lab type** (DNA, toxicology, ballistics, drug analysis, digital forensics), and lab column **Victim/Complainant** (alongside Client / Co-Defendant / Witness). No autopsy, SANE, or CAC fields.
- No District Defender submission footer.

---

## Attorney-only fields

Every field marked `[ATTORNEY]` (Theory of the Case — Initial, Theory of the Case — Trial, Possible Defense Witnesses, Does Defendant want to testify?, and any Section 4 — Defenses entries that require client communication or strategic judgment) is rendered in **red font** with `[ATTORNEY]` placeholder text. Cowork leaves these blank.

In the XML, apply red font by setting `<w:color w:val="FF0000"/>` inside the `<w:rPr>` run properties for the relevant text runs.

Any content flagged for attorney review (conflicts between sources, preliminary assessments, items needing verification) should also be rendered in red font so the attorney can spot it at a glance.

---

## LWOP Population (Part 2A / 2B)

When the case has LWOP exposure (Part 2A or 2B is in scope), populate Part 2A or 2B of `000 - Case Profile.docx` directly from discovery using the field schema in `lwop-field-maps.md` and the extraction rules in `lwop-extraction-patterns.md`.

**Extraction priority order (read documents in this sequence):**

1. Charging Instrument (Indictment / Bill of Information) — establishes charges, docket, defendant name, victim names
2. Police / Incident Report — core facts, witnesses, timeline, officer names
3. Defendant Statement — Miranda status, confession/denial, voluntariness
4. Witness Statements — corroboration or inconsistency with police report
5. Autopsy Report (Homicide) / SANE Report (Sex Offense) — forensic evidence
6. Lab Reports — toxicology, DNA, ballistics
7. CAC Interview (Sex Offense) — victim's account
8. Criminal History (RAP sheet) — prior convictions for Part 1 Section 5
9. Medical Records — HIPAA-related records
10. Investigator Reports — defense investigation results
11. Filed Motions — motions section data
12. Bond Documents — bond reduction data

For each field, follow the source-priority and extraction notes in `lwop-field-maps.md`. Critical sourcing rules:

| Field | Source | Notes |
|---|---|---|
| Indictment Date | Date printed on the Grand Jury Indictment / Bill of Information | The filing date on the instrument itself, not the offense date |
| Age at Time of Offense | Calculated from client DOB (booking/RAP) vs. offense date | If DOB unavailable, note approximate age from documents |
| Indictment Attached | Always mark **Yes** | If we have the case folder and are filling Part 2A/2B, the indictment is presumed present |
| Prior Convictions | Client's RAP sheet / NCIC printout | Format MM-DD-YYYY — Offense Name (Disposition); pull into Part 1 Section 5 |

**Formatting conventions:**
- **Witnesses:** Numbered list. Each entry: number, bolded name, then relationship in parentheses (e.g., "1. **Det. John Smith** (lead detective)"; "2. **Maria Garcia** (eyewitness, neighbor)").
- **Witness Statements:** Numbered list. Each entry: number, bolded witness name, who took the statement, date/time, summary with direct quotes bolded. Note inconsistencies between witnesses.
- **Charges:** Include the Louisiana statute number (e.g., "14:42 First Degree Rape").
- **Aggravating Factors:** Include specific alleged acts, not just legal categories.
- **Police Report Summary:** Specific times, locations, officer actions, dispatch/arrival times.
- Direct quotes are **bolded**.

**Field-completeness checklist (mandatory before saving):**
Walk every field listed for the active case-type branch in `lwop-field-maps.md`. For each field:
1. Confirm the field label exists in the output document
2. Confirm the data cell is present (populated or blank — but the cell exists)
3. If a field is missing, stop and add it before proceeding

Log any fields left blank and the reason (missing discovery, attorney-only field, etc.) in the completion notes.

**Completion notes (after generating the document):**
Provide a brief summary including:
1. Fields populated — which fields were filled and from which source documents
2. Fields left blank — which fields could not be populated and why
3. Conflicts found — contradictions between sources the attorney should review (rendered in red in the document)
4. Missing discovery — documents referenced in police reports but absent from the folder
5. Suppression flags — Miranda/search/seizure issues identified during extraction

---

## Refresh Mode (Part 2A / 2B update from new discovery)

When `000 - Case Profile.docx` already exists and new discovery has been added since its last modification:

1. **Read the existing `000 - Case Profile.docx` in full.** Identify which case-type branch is populated (Part 2A, 2B, or 2C). If multiple branches are populated (rare — both 2A and 2B for cases with both homicide and sex-offense LWOP exposure), refresh both.
2. **Identify the new discovery.** Either the attorney has named it explicitly, or compare the case folder's file timestamps against the existing Case Profile's last-modified date. List the new items.
3. **Re-extract using `lwop-extraction-patterns.md`** against the new discovery only (not the full case file — that would re-do work already in the document).
4. **Apply updates field-by-field** using these merge rules:

| Existing cell state | Action |
|---|---|
| Blank | Populate from new discovery |
| Cowork-extracted black-text content | Update if newer source contradicts; preserve if newer source is silent |
| Black-text content matching attorney handwriting / additions | **Do not touch** unless attorney explicitly says "re-pull everything" |
| Red `[ATTORNEY]` placeholder | **Never touch** |
| Red attorney-flagged content | **Never touch** |

5. **Append a Refresh Log entry** at the bottom of Part 2A or 2B (under Section 9 — Records & Authorizations):
```
REFRESH LOG — [YYYY-MM-DD]
New discovery processed: [list Bates ranges or file names]
Fields updated: [list field names]
Attorney-only fields preserved: [list field names left untouched]
Conflicts flagged for attorney review (red text added in fields): [list field names]
```
6. **Run the field-completeness checklist** as in Initial Generation Mode.
7. **Save** as `000 - Case Profile.docx` (same filename — overwrite the existing file).

**Save the output for both modes** to:
`Pretrial Notebook → 03 - Case Analysis & Notes/000 - Case Profile.docx`

---

## Generation Procedure (XML Edit)

Read the docx skill (at the path listed in your available skills) for the full unpack/edit/repack procedure. Then:

```bash
# Initial Generation Mode
cp "<skill>/assets/CASE PROFILE.docx" "<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/000 - Case Profile.docx"

# 1. Unpack
python <docx-skill-path>/scripts/office/unpack.py "<output-path>" working/unpacked/

# 2. Edit the XML cells in working/unpacked/word/document.xml
#    - For each Part 2A/2B field listed in lwop-field-maps.md:
#      - Find the cell containing the label text
#      - Locate the adjacent/next cell in the same row
#      - Replace empty <w:t/> with extracted data
#      - Preserve all <w:rPr> and <w:pPr> formatting
#    - Use multiple <w:p> paragraphs within a cell for multi-line content
#    - Apply red font (<w:color w:val="FF0000"/>) to attorney-only fields and flagged content
#    - For Part 2 case-type selection: keep the active branch; remove or leave blank the inactive branches per attorney instruction

# 3. Repack
python <docx-skill-path>/scripts/office/pack.py working/unpacked/ "<output-path>" --original "<skill>/assets/CASE PROFILE.docx"

# 4. Validate
python <docx-skill-path>/scripts/office/validate.py "<output-path>"
```

For Refresh Mode, replace step 1 with reading the existing file, and apply the merge rules from the Refresh Mode subsection above when editing cell contents in step 2.

---

## Step 3 Quality Check

- [ ] `assets/CASE PROFILE.docx` copied into `Pretrial Notebook → 03 - Case Analysis & Notes` as `000 - Case Profile.docx` (Initial Generation Mode) OR existing file read in full (Refresh Mode)
- [ ] Part 1 sections 1–6 populated from available sources (Initial Generation only)
- [ ] Exactly one of Part 2A, 2B, or 2C selected based on charges; the other two parts left blank or removed
- [ ] If LWOP exposure is present (Part 2A or 2B): every field listed in `lwop-field-maps.md` for that branch is present in the output (field-completeness checklist run)
- [ ] All `[ATTORNEY]` fields preserved in red for attorney completion
- [ ] In Refresh Mode: all attorney-entered content preserved untouched; Refresh Log entry appended
- [ ] Completion notes generated (fields populated, fields blank with reasons, conflicts, missing discovery, suppression flags)
