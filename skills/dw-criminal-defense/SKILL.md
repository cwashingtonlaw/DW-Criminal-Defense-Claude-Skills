---
name: dw-criminal-defense
description: >
  Master 3-phase criminal defense workflow. ALWAYS invoke for "case intake," "new case,"
  "run Phase 1/2/3," initial case setup, "fill out the LWOP sheet," "LWOP review,"
  "District Defender review," "life without parole worksheet," or "refresh the Case Profile."
  Do NOT use for loading existing case state — use dw-case-brain. Do NOT use for case
  status checks — use dw-case-dashboard. Do NOT use for the client-facing first meeting
  / intake interview — use dw-client-intake-interview (this skill handles the case file
  side; the intake interview skill handles the live client meeting and feeds into Phase 1).
---

# Daniels & Washington — Criminal Defense Cowork Skill
**Version 5.4 | Internal Use Only**

This skill governs all Claude Cowork operations for criminal defense case management at Daniels & Washington. Follow this skill for every task involving a client case file. The 3-phase workflow below is the single source of truth.

**v5.4 changes:**
- Phase 2 Step 1 expanded with new sub-step **1D — Charge-Type Specialist Routing** dispatching to `dw-drug-offense-specialist`, `dw-dwi-specialist`, `dw-sex-offense-specialist`, `dw-firearms-specialist`, and the new `dw-violent-crime-specialist`.
- Phase 2 Step 1C now routes jail-call evidence to the new `dw-jail-call-analyzer`.
- Phase 3 Step 10 (Appellate Readiness) now hands off to the new `dw-appellate-brief-builder` after `dw-appellate-error-monitor` produces the ranked-issue list, with collateral relief routed separately to `dw-post-conviction-relief`.
- Phase 3 added new **Step 11 — Trial Day Support** routing to the new `dw-trial-day-assistant`; previous Step 11 (Assemble Trial Notebook) renumbered to Step 12.
- Description updated to disambiguate from `dw-client-intake-interview` (client-facing first meeting) — this skill remains the case-file orchestrator.
- `dw-expert-witness-evaluator` Module I (Daubert/Foret Hearing Day Package) now noted in 1C routing for hearing-day operational deliverables.

**v5.3 change:** The former `dw-lwop-populator` skill has been merged into Phase 1 Step 3. LWOP review sheets are no longer a separate deliverable — they live as Part 2A (Homicide) or Part 2B (Sex Offense) of the unified `000 - Case Profile.docx`. The populator's field schema and extraction rules are now in `references/lwop-field-maps.md` and `references/lwop-extraction-patterns.md`. Refresh Mode (Phase 1 Step 3 sub-mode) handles late-discovery updates that previously triggered standalone populator runs.

---

## Bundled Resources

This skill includes bundled files organized into three directories. Load them as needed — they are not all required at once.

```
dw-criminal-defense/
├── SKILL.md                              ← You are here
├── references/
│   ├── case-analysis-prompts.md          ← Phase 2: all 8 report prompt templates
│   ├── output-path-convention.md         ← Where to save deliverables (CASE_ROOT resolution, phase folders, naming)
│   ├── lwop-field-maps.md                ← v5.3: complete field schema for Part 2A (Homicide) and Part 2B (Sex Offense) of 000 - Case Profile.docx
│   └── lwop-extraction-patterns.md       ← v5.3: how to extract each field from discovery (filename patterns, content markers, sourcing rules)
├── assets/
│   ├── CASE PROFILE.docx                 ← Master Case Profile template (Part 1 + case-type Parts 2A/2B/2C)
│   ├── Case Tables.xlsx                  ← Master spreadsheet template (copy to new case roots)
│   ├── Evidence_Placeholder_Template.md  ← Layout spec for digital evidence placeholder PDFs
│   └── legacy/
│       ├── LWOP Homicide Review Sheet - FOR TYPING.docx    ← Reference only — original Calcasieu PDO standalone form
│       └── LWOP Sex Offense Review Sheet - FOR TYPING.docx ← Reference only — original Calcasieu PDO standalone form
└── scripts/
    └── generate_placeholders.py          ← Generates one-page placeholder PDFs for media evidence folders
```

**When to load each resource:**
- **Phase 1 Step 1 (new case):** Read `references/output-path-convention.md` to resolve `CASE_ROOT`. Copy `assets/Case Tables.xlsx` to the case root if not already present.
- **Phase 1 Step 2f:** Run `scripts/generate_placeholders.py` against the evidence directory.
- **Phase 1 Step 3 (Case Profile, any LWOP case):** Read both `references/lwop-field-maps.md` and `references/lwop-extraction-patterns.md` before populating Part 2A or 2B. Copy `assets/CASE PROFILE.docx` into the case folder as `000 - Case Profile.docx`.
- **Phase 1 Step 3 Refresh Mode:** Same two reference files plus the existing `000 - Case Profile.docx` already on the case file.
- **Phase 2 Step 2:** Read `references/case-analysis-prompts.md` for the exact prompt templates for all 8 reports.
- **Any file-write step:** Consult `references/output-path-convention.md` for the canonical save path.

---

## Core Rules (Always Apply)

- **Never create new spreadsheets.** All tabular data goes into the sheets that already exist in `Case Tables.xlsx` at the root of the case folder.
- **Never create new folders** unless a standard subfolder is confirmed missing.
- **Naming convention:** All documents use `[3-digit prefix] - [Document Name].docx` format with **sequential numbering starting at 001** (e.g., `001 - Bill of Information`, `002 - Incident Report`, `003 - Arrest Warrant`). Number documents consecutively with no gaps — do not skip numbers or leave room between entries.
- **Cowork drafts; attorney approves.** Claude prepopulates templates and drafts documents. Attorneys make final decisions and send all external communications.
- **Quality Gates must be confirmed** before advancing to the next phase. Do not proceed if any gate item is unresolved.
- **Louisiana law applies** unless otherwise indicated. Use Louisiana statutes for all charge research, discovery obligations, and citations.
- **Attorney-only fields are sacred.** Any field marked `[ATTORNEY]` in red font must be preserved blank for attorney completion. Cowork never fills these. In Refresh Mode, Cowork never overwrites them.

---

## Case Tables Write Protocol

**CRITICAL:** Google Drive sync can silently overwrite changes to Case Tables.xlsx if the file is open in Excel, Google Sheets, or any other application on another device. To prevent data loss, **ALWAYS follow this protocol before writing to any sheet in Case Tables.xlsx** — including Evidence Table, Timeline Sheet, Witness Sheet, Witness List - Alpha, Witness List - Priority, Defense Matrix, Defense Shield, Running List, and any future sheets.

### Pre-Write Warning

Before modifying any sheet in Case Tables.xlsx, alert the attorney with this exact message:

> "I need to update Case Tables.xlsx. **Please close it in Excel, Google Sheets, or any other application before I proceed.** Google Drive sync can overwrite my changes if the file is open elsewhere. Confirm when it's closed."

### Wait for Confirmation

Do not proceed to write until the attorney explicitly confirms the file is closed. Accept confirmations like:
- "closed"
- "go ahead"
- "it's closed"
- "ready"
- Any other affirmative confirmation that the file is no longer open

### Write the Changes

Once confirmed, perform the update to Case Tables.xlsx.

### Post-Write Verification

After writing, instruct the attorney:

> "Update complete. Please open Case Tables.xlsx and confirm you can see [specific sheet name and change description]. If the change isn't visible, let me know and I'll reapply it."

### Retry Protocol — If Changes Disappear

If the attorney reports the change is missing:
1. Ask them to close the file again
2. Re-read the current state of Case Tables.xlsx (it may have been overwritten by sync)
3. Reapply the changes
4. Verify again using the Post-Write Verification message above

### Guardrail

**Never write to Case Tables.xlsx without first warning the attorney to close the file and waiting for confirmation.** Google Drive sync conflicts can silently overwrite changes, causing lost work.

---

## PHASE 1 — Case Intake & Matter Setup

*Triggered the moment a new client engagement is confirmed. This phase covers everything from folder creation through a fully organized, Bate-stamped, searchable case file with a complete Case Profile — the foundation for all analysis in Phase 2.*

### Step 1: Folder Setup

- Read `references/output-path-convention.md` to resolve `CASE_ROOT` (checks Case Brain session → attorney prompt → Cowork project mapping → asks attorney).
- Read `references/folder-structure-and-naming.md` for the full standard folder layout (including Exhibit List, Billing, and Case Closing locations) and the master document/audio/video naming conventions.
- Confirm all standard subfolders exist: `01 - Trial Notebook` (all sub-tabs) and `02 - Pretrial Notebook` (all sub-tabs).
- Locate `Case Tables.xlsx` at the root of the case folder. If this is a new case and no `Case Tables.xlsx` exists, copy the master template from `assets/Case Tables.xlsx` into the case root.
- Do not create new folders unless a standard subfolder is missing.

**✓ Step 1 Check:** Folder structure confirmed, `CASE_ROOT` resolved, `Case Tables.xlsx` located.

### Step 2: Prepare Discovery for Review

*Converts raw discovery into organized, Bate-stamped, searchable files. Folder sorting runs in parallel with OCR — do not wait for OCR to begin sorting.*

**2a — Download & Organize Discovery**
- Sort all downloaded files into `01 - Pleadings` and `02 - Discovery` subfolders in the Pretrial Notebook.
- Move audio/video files to `05 - Evidence` in the Trial Notebook only — no duplicates.
- Generate a **Download Log**: date received, production set name, file count, total pages (estimated).
- Flag image-only PDFs (need OCR) vs. text-searchable PDFs.
- **Staff action (parallel):** Run OCR on all flagged image-only PDFs using Adobe Acrobat Professional, PDF Expert, or ScanSnap.

**2b — Bate-Stamp Documents**
**Maintain:** `Bate Stamp Master Log.xlsx` as the single source of truth.

Log columns: Production Set | Date Received | Start Number | End Number | Staff Member | Date Stamped

Rules:
- Sequential numbering in order received. Never restart mid-case. Continuous across all production dates.
- Before any new stamping: check log for current highest number, output the next available.
- After stamping: update log immediately — no batch updates.
- Flag any numbering gap — alert staff before proceeding.
- Flag any overlap (duplicate numbers) — halt until resolved.

**2c — Duplicate Discovery to Evidence Folder**
- Copy all Bate-stamped, OCR'd documents to `05 - Evidence` in the Trial Notebook.
- Run file count and size comparison between source and destination.
- Flag any file that failed to copy or shows a size mismatch.
- Do not proceed to 2d until copy is 100% verified.

**2d — Separate Discovery into Individual Documents**
- Review the State's index to identify document divisions and names.
- Split the combined PDF into individual files at the State's document boundaries.
- Apply naming convention: `[3-digit prefix] - [Document Name]` with sequential numbering starting at `001` (e.g., `001 - Bill of Information`, `002 - Incident Report`). Assign the next consecutive number to each document — never skip numbers.
- Create subfolders for multi-file audio/video using the same sequential number (e.g., `008 - Body Camera Footage/`).
- Output a **Separation Checklist**: expected document count (from State index) vs. actual file count.
- Flag any document in the State's index with no corresponding file — log in Report 7 queue.

**2e — Transcribe Interviews & Digital Media**
Route to **casedev:transcription** skill for audio/video processing with speaker diarization.
- Staff uploads all audio/video files to casedev vault; skill handles transcription automatically.
- When transcripts return: name each transcript PDF identically to its audio/video file, save in the same folder.
- Add transcript as a separate row in the Evidence Table (Evidence Type: Transcript).
- Confirm every audio/video file has a corresponding transcript before proceeding.

**2f — Digital Evidence Handling — Generate Placeholders**
Media folders (photos, videos, audio, surveillance, body cam footage) cannot be Bate-stamped like documents. Each media folder needs a **Digital Evidence Placeholder** — a one-page PDF that sits in the evidence sequence and describes the folder's contents. Optionally route complex media analysis to **dw-evidence-placeholder** skill for full inventory generation.

**Run the bundled generator script:**
```bash
python3 <skill-directory>/scripts/generate_placeholders.py \
  --evidence-dir "<path-to-05-Evidence>" \
  [--folders "folder1" "folder2" ...]  # optional: specific folders only
```

If `--folders` is omitted, the script processes all subfolders automatically. The script scans each subfolder for file counts, types, and size; classifies contents by media type (Audio, Photo/Image, Video, Other Data); generates a one-page PDF placeholder matching the firm's template layout (defined in `assets/Evidence_Placeholder_Template.md`); and names each PDF identically to its source folder.

**Workflow:**
- Identify every subfolder in `05 - Evidence` that contains media files
- Confirm scope with user — default to processing all folders unless told otherwise
- Skip folders that already have a corresponding placeholder PDF (use `--force` to regenerate)
- After running, report: total placeholders created, any folders skipped, breakdown by media type

**✓ Step 2 Check:**
- [ ] File count in Evidence Folder matches downloaded discovery
- [ ] Bate Stamp Log shows no gaps or overlaps
- [ ] All image-only PDFs have been OCR'd and confirmed text-searchable
- [ ] No documents in the State's index are absent from the Evidence Folder
- [ ] Separation Checklist: expected count = actual count
- [ ] Every audio/video file has a corresponding transcript entry
- [ ] Digital Evidence Placeholder PDF exists for every media folder in `05 - Evidence`

### Step 3: Generate Case Profile

**Output:** `000 - Case Profile.docx` → save to `Pretrial Notebook → 03 - Case Analysis & Notes`
**Source template:** `assets/CASE PROFILE.docx` — copy this template to the output path before populating.
**Reference files (mandatory for any LWOP case):** `references/lwop-field-maps.md` (field schema for Part 2A and 2B) and `references/lwop-extraction-patterns.md` (extraction rules from discovery documents).

This single document replaces the former Initial Case Profile, Criminal Defense Cover, and (where applicable) the standalone LWOP review sheet. It follows the lifecycle of a criminal case — from identification through disposition — so the attorney can use it as a living reference from intake through trial.

The template has two parts:

- **Part 1 — Case Profile** (six sections). Populate for **every** case.
- **Part 2 — Case-Type Specific Review Sheet.** Populate **exactly one** of Part 2A, 2B, or 2C based on the charges:
  - **Part 2A — LWOP Homicide** — for cases with LWOP exposure on a homicide charge (La. R.S. 14:30, 14:30.1). Submit to the District Defender per Calcasieu PDO requirements.
  - **Part 2B — LWOP Sex Offense** — for cases with LWOP exposure on a sex offense charge (La. R.S. 14:42, 14:42.1, 14:43, 14:43.1, 14:81.2). Submit to the District Defender 30 days after appointment and every consecutive 30 days.
  - **Part 2C — Other Felony** — for non-LWOP felony cases. No District Defender submission requirement.

If the case carries both homicide and sex offense LWOP exposure, populate both Part 2A and Part 2B.

#### Operating Modes

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

#### Part 1 — Case Profile (always completed)

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

#### Part 2 — Case-Type Specific Review Sheet

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

#### Attorney-only fields

Every field marked `[ATTORNEY]` (Theory of the Case — Initial, Theory of the Case — Trial, Possible Defense Witnesses, Does Defendant want to testify?, and any Section 4 — Defenses entries that require client communication or strategic judgment) is rendered in **red font** with `[ATTORNEY]` placeholder text. Cowork leaves these blank.

In the XML, apply red font by setting `<w:color w:val="FF0000"/>` inside the `<w:rPr>` run properties for the relevant text runs.

Any content flagged for attorney review (conflicts between sources, preliminary assessments, items needing verification) should also be rendered in red font so the attorney can spot it at a glance.

#### LWOP Population (Part 2A / 2B)

When the case has LWOP exposure (Part 2A or 2B is in scope), populate Part 2A or 2B of `000 - Case Profile.docx` directly from discovery using the field schema in `references/lwop-field-maps.md` and the extraction rules in `references/lwop-extraction-patterns.md`.

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

For each field, follow the source-priority and extraction notes in `references/lwop-field-maps.md`. Critical sourcing rules:

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
Walk every field listed for the active case-type branch in `references/lwop-field-maps.md`. For each field:
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

#### Refresh Mode (Part 2A / 2B update from new discovery)

When `000 - Case Profile.docx` already exists and new discovery has been added since its last modification:

1. **Read the existing `000 - Case Profile.docx` in full.** Identify which case-type branch is populated (Part 2A, 2B, or 2C). If multiple branches are populated (rare — both 2A and 2B for cases with both homicide and sex-offense LWOP exposure), refresh both.
2. **Identify the new discovery.** Either the attorney has named it explicitly, or compare the case folder's file timestamps against the existing Case Profile's last-modified date. List the new items.
3. **Re-extract using `references/lwop-extraction-patterns.md`** against the new discovery only (not the full case file — that would re-do work already in the document).
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

#### Generation procedure (XML edit)

Read the docx skill (at the path listed in your available skills) for the full unpack/edit/repack procedure. Then:

```bash
# Initial Generation Mode
cp "<skill>/assets/CASE PROFILE.docx" "<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/000 - Case Profile.docx"

# 1. Unpack
python <docx-skill-path>/scripts/office/unpack.py "<output-path>" working/unpacked/

# 2. Edit the XML cells in working/unpacked/word/document.xml
#    - For each Part 2A/2B field listed in references/lwop-field-maps.md:
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

**✓ Step 3 Check:**
- [ ] `assets/CASE PROFILE.docx` copied into `Pretrial Notebook → 03 - Case Analysis & Notes` as `000 - Case Profile.docx` (Initial Generation Mode) OR existing file read in full (Refresh Mode)
- [ ] Part 1 sections 1–6 populated from available sources (Initial Generation only)
- [ ] Exactly one of Part 2A, 2B, or 2C selected based on charges; the other two parts left blank or removed
- [ ] If LWOP exposure is present (Part 2A or 2B): every field listed in `references/lwop-field-maps.md` for that branch is present in the output (field-completeness checklist run)
- [ ] All `[ATTORNEY]` fields preserved in red for attorney completion
- [ ] In Refresh Mode: all attorney-entered content preserved untouched; Refresh Log entry appended
- [ ] Completion notes generated (fields populated, fields blank with reasons, conflicts, missing discovery, suppression flags)

### Step 4: Build Case Tables

Populate three sheets in `Case Tables.xlsx`. Do not create new sheets — use the existing ones. Maintain all existing color coding, dropdown lists, and formatting. The Case Profile (Step 3) provides the charge and defense context needed for accurate assessment of all columns.

**Reference:** Read `references/color-coding.md` for the firm's full header and dropdown color specs (hex values for every column, evidence type, witness type, review priority, defense relevance, and timeline tag). Use the `xlsx` skill to apply formatting per those specs.

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See "Case Tables Write Protocol" section above.

**4a — Evidence Table**
Populate the **Evidence Table Sheet** with the full discovery catalog, including analysis columns.

| # | Column | How Populated |
|---|--------|---------------|
| 1 | Doc # | Auto — file name prefix (3-digit) |
| 2 | Evidence Type | Auto — file type + content; Transcript listed separately from A/V |
| 3 | Name | Auto — file name (must match 3-digit convention) |
| 4 | Description | Staff — brief content summary |
| 5 | Bate Stamp | Auto — cross-referenced to Bate Stamp Log |
| 6 | Reviewed (Y/N) | Staff / Attorney — updated after document review |
| 7 | Notes | Staff / Attorney — key observations and flags |
| 8 | Discovery Set | Auto — from Download Log |
| 9 | Date of Delivery | Auto — from Download Log |
| 10 | Review Priority ★ | **Cowork** — AI assessment: HIGH / MED / LOW |
| 11 | Defense Relevance ★ | **Cowork** — AI preliminary, attorney confirms: FAVORABLE / NEUTRAL / FLAG |

**Review Priority rules:**
- HIGH: all audio/video, all interviews, incident reports, lab reports, prior bad acts
- MED: supplemental reports, witness statements, photographs
- LOW: administrative documents, chain of custody logs, return of service

**Defense Relevance rules:**
- FAVORABLE: documents suggesting innocence, inconsistency, or constitutional violation
- FLAG: documents suggesting suppression issues, Brady material, or missing items
- NEUTRAL: all other documents

*Attorney must review all FAVORABLE and FLAG items before Phase 2. Cowork's assessment is preliminary — attorney confirmation required on all AI assessments.*

**4b — Witness Table – Priority** (`Witness List - Priority` sheet)
Extract every witness name encountered during discovery organization and transcription. Sort by witness impact on case outcome. Cross-reference against Case Profile defenses to identify which witnesses are central to the identified defense theories or the prosecution's burden of proof.

Importance ranking: Key Witness > Eyewitnesses > Law Enforcement > Character Witnesses > Others

Columns: Name | Witness Type | Association | Sources (Bate stamps) | Trial Exam Prepared (Y/N)

Bold-mark any witness who appears in multiple documents, gives conflicting statements, or is central to identified defense theories as **KEY WITNESS**.

**4c — Witness Table – Alpha** (`Witness List - Alpha` sheet)
Same data as 4b, sorted alphabetically. Standard reference list for quick lookup.

**✓ Step 4 Check:**
- [ ] Evidence Table row count matches file count in Evidence Folder
- [ ] Review Priority populated for every row in Evidence Table
- [ ] Defense Relevance populated for every row in Evidence Table
- [ ] Witness Table – Priority populated, ranked, and cross-referenced against Case Profile
- [ ] Witness Table – Alpha populated and sorted

### ✓ Phase 1 Quality Gate
Before proceeding to Phase 2, confirm all step checks are complete:
- [ ] Folder structure confirmed — all standard subfolders exist (Step 1)
- [ ] Discovery fully organized, Bate-stamped, OCR'd, transcribed, and placeholders generated (Step 2)
- [ ] `000 - Case Profile.docx` complete with all auto-populated fields (Step 3) — including Part 2A/2B for any LWOP case
- [ ] All Case Tables populated — Evidence Table (all 11 columns), Witness Tables (Priority and Alpha) (Step 4)
- [ ] Case state saved to **dw-case-brain** — Phase 1 complete, ready for Phase 2

---

## PHASE 2 — Case Processing & Analysis

*Runs parallel analysis before attorney review. Auto-action loops triggered by Reports 7 and 8 eliminate rework in Phase 3.*

### Step 1: Rapid Triage & Specialist Routing
Before the 8 Case Analysis Reports are generated, scan all case documents to produce two deliverables: a **Triage Routing Memo** and early **specialist skill dispatches**. The purpose of this step is speed — get routing decisions to specialist skills fast so they can begin working in parallel while the full reports are being written. This step flags and routes; the reports (Step 2) analyze in depth.

**1A — Triage Routing Memo**
Quickly scan all discovery documents and produce a short routing memo that identifies which documents need specialist attention. The memo is a working document for Cowork's internal use — not a deliverable to the attorney. It contains routing decisions, not analysis.

For each flag below, list the specific documents (by name and Bate stamp) and the routing destination. Do not write analysis — just identify and route:
- **Constitutional flags:** documents suggesting 4th, 5th, or 6th Amendment concerns → route to **dw-suppression-motion** *(Report 3 will provide the full analysis)*
- **Brady/Giglio flags:** material potentially favorable to the defense that may not have been disclosed → route to **dw-brady-giglio-auditor** *(Report 7 will provide the full table)*
- **Witness inconsistency flags:** witnesses who appear in multiple documents with conflicting accounts → flag for **Report 8** *(Report 8 will provide the full impeachment plan)*
- **Timeline conflict flags:** events with conflicting dates, times, or sequences across documents → flag for **Report 1** *(Report 1 will build the authoritative timeline)*

**1B — Chain of Custody Audit**
This is substantive analysis, not triage — no report covers this domain. Verify that each piece of physical evidence has an unbroken custody log from collection to present. Flag any gaps, undocumented transfers, or missing logs. Route findings to **dw-chain-of-custody-auditor**.

**1C — Specialist Evidence Routing**
Classify evidence by type and dispatch to the appropriate specialist skill for early analysis. Specialist skills can begin their work in parallel while the 8 reports are being generated in Step 2.

- Eyewitness identification issues → **dw-eyewitness-identification-auditor**
- Confession/interrogation issues → **dw-confession-interrogation-auditor**
- Cell phone forensics → **dw-mobile-forensic-auditor** then **dw-forensic-dump-analyzer**
- Video evidence analysis → **dw-video-evidence-auditor**
- Cell site/location data → **dw-cell-site-geolocation-auditor**
- Social media evidence → **dw-social-media-auditor**
- Child forensic interviews → **dw-child-forensic-interview-auditor**
- Expert witness issues → **dw-expert-witness-evaluator** (Module I for Daubert/Foret hearing day package once a hearing is set)
- Jail call recordings (Securus / GTL/ViaPath / NCIC / IC Solutions) → **dw-jail-call-analyzer** (transcribes via dw-transcript-router; cross-feeds dw-witness-threat-matrix and dw-cross-exam-architect)

**1D — Charge-Type Specialist Routing**
Identify the charge category and dispatch to the corresponding charge-type specialist for element-by-element defense framework, sentencing exposure analysis, and discipline-specific motions/discovery. Specialists run in parallel with the 8 reports.

- Drug offenses (CDS, distribution, possession with intent) → **dw-drug-offense-specialist**
- DWI / OWI / vehicular homicide → **dw-dwi-specialist**
- Sex offenses (incl. SANE-exam audit) → **dw-sex-offense-specialist**
- Firearms offenses (state and federal) → **dw-firearms-specialist**
- Violent crimes (homicide, manslaughter, agg battery, agg assault, armed robbery, kidnapping, home invasion) → **dw-violent-crime-specialist**

Cases involving multiple specialist domains (e.g., armed robbery with felon-in-possession enhancement) should dispatch to all applicable specialists.

Save all Step 1 outputs to: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` subfolder.

### Step 2: Generate the 8 Case Analysis Reports
Read `references/case-analysis-prompts.md` for the exact prompt template for each report. That file contains the common analytical framework ("Dream Team" lens), the source citation standard, and per-report instructions. Name each report exactly as shown below. For each report, identify and route specific issues to specialist skills.

Note: The former "Report 8 — Witness Table" has been removed because witness data is already captured in `Case Tables.xlsx` during Phase 1 Step 4 (Witness List - Priority and Witness List - Alpha sheets). The former Report 9 (Key Witness Impeachment Plan) is now Report 8.

| # | Report Name | Output Location | Priority | Skill Routing |
|---|-------------|-----------------|----------|----------------|
| 1 | Comprehensive Case Timeline | `Case Tables.xlsx — Timeline Sheet` ⚠ | Standard | - |
| 2 | Prosecution's Case Summary | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 3 | Immediate Red Flags | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★** | **dw-suppression-motion** (for warrant/search issues); **dw-expert-witness-evaluator** (for expert issues) |
| 4 | Core Defense Narrative | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 5 | Viable Legal Defenses | `01 - Trial Notebook/09 - Case Analysis/` | Standard | **dw-404b-opposition** (for bad acts); **dw-sentencing-mitigation-specialist** (for sentencing exposure); **dw-habitual-offender-auditor** (for habitual claims) |
| 6 | Memorable Theme | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 7 | Table of Missing Discovery | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★ → Auto-Action** | **dw-brady-giglio-auditor** |
| 8 | Key Witness Impeachment Plan | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★ → Auto-Action** | **dw-cross-exam-architect** |

**Bond/Release Issues:** If Report 3 or 5 identifies bond concerns → route to **dw-bond-and-release-motion**
**Plea Negotiations:** If prosecution indicates negotiation interest → route to **dw-plea-negotiation-analyzer**

### Step 3: Auto-Action — Report 7 → Missing Discovery Demand Letter
*Triggered immediately upon filing Report 7.*

**Output:** `Missing Discovery Demand — [Date].docx` → save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

**Reference:** Read `references/textexpander-snippets.md` for the firm's standard boilerplate (Case Caption, Signature Block, Certificate of Service, Discovery Citations, Cowork Draft Disclaimer). Use these exact text blocks — do not paraphrase the firm's standard language.

- Extract every item listed in Report 7's data table.
- Draft a formal demand letter addressed to the prosecution citing Brady/Giglio obligations.
- List each missing item with description and why it is material to the defense.
- Include Louisiana statutory citations for discovery disclosure requirements.
- **Attorney must approve before letter is sent.**

### Step 4: Auto-Action — Report 8 → Impeachment Worksheets
*Triggered immediately upon filing Report 8.*

Create one Impeachment Worksheet per key witness in `Trial Notebook → 03 - Witnesses`:
- **Prepopulate:** witness name, role, all document references (Bate stamps) from Evidence Table
- **Prepopulate:** all impeachment material from Report 8 for that witness
- **Prepopulate:** all prior statements from transcripts with Bate stamp references
- **Add:** Witness Dossier cover page consolidating everything known about this witness
- **Leave blank (attorney completes):** Line of Attack, Question Sequence, Anticipated Responses

### Step 5: Route Case Analysis to Attorney
Once all 8 reports and auto-action documents are complete:
- Draft attorney email: *"Case Analysis Ready for Review — [Client Name] / [Case Number]"*
- Attach Case Analysis Index listing all 8 reports + Cowork Analysis findings
- Confirm Missing Discovery Demand Letter is ready for attorney approval
- Confirm all Impeachment Worksheets are filed and ready for Phase 3

### Step 6: Auto-Push Attorney Review Checklist to Apple Notes
*Triggered immediately after Step 5. The attorney needs actionable review items in their daily-driver app — not buried in the case folder.*

After completing all 8 reports and auto-actions, Cowork generates an **Attorney Review Checklist** and pushes it to Apple Notes. This ensures the attorney sees the checklist where they actually work, with a clear deadline.

**Checklist content** (auto-generated from Phase 2 outputs):
- Title: `Attorney Review Checklist — [Matter Name] ([YYYY-MM-DD])`
- Deadline: 5 business days from creation date
- One checkbox item per attorney-action deliverable:
  - Missing Discovery Demand Letter (review, sign, send)
  - Report 3 Red Flags (prioritize HIGH items for motion practice)
  - Report 5 Legal Defenses (decide which motions to file)
  - Report 6 Memorable Theme (confirm or select alternative)
  - Impeachment Worksheets (complete Line of Attack, Question Sequence, Anticipated Responses)
  - Expert Witness retention (child psych, SANE, forensic interview)
  - Any outstanding discovery demands from Report 7
- Footer: `Generated by Cowork — Daniels & Washington`

**Push to Apple Notes (via iCloud web):**
1. Use Claude in Chrome to navigate to `https://www.icloud.com/notes`
2. Wait for iCloud Notes to load (user must be logged into iCloud in Chrome)
3. Click the "New Note" button to create a new note
4. Type the same title and checklist content
5. Apple Notes on iCloud supports checklist formatting — use the checklist button in the toolbar

**Fallback behavior (important — Chrome may not always be connected):**
If Claude in Chrome is not available or Apple Notes is unreachable:
1. Save the checklist as `Attorney Review Checklist — [Date].md` at the case root
2. Log the failed push in the Quality Gate
3. Alert the attorney: *"Review checklist saved locally — Chrome automation was unavailable for Apple Notes. Connect Claude in Chrome and re-run Step 6 to push."*

The reason for the fallback is that Claude in Chrome requires the browser extension to be installed and connected, which isn't always the case. The local markdown file ensures the checklist is never lost, even if the push fails.

### ✓ Phase 2 Quality Gate
Before proceeding to Phase 3, confirm:
- [ ] All 8 reports named correctly and saved to correct locations
- [ ] Triage Routing Memo, Chain of Custody Audit, and Specialist Evidence Routing complete — all outputs saved to Cowork Analysis subfolder
- [ ] Missing Discovery Demand Letter drafted and ready for attorney approval
- [ ] Impeachment Worksheet exists for every witness named in Report 8
- [ ] Witness Dossier cover page exists for every key witness
- [ ] Attorney notified via email with Case Analysis Index
- [ ] Attorney Review Checklist pushed to Apple Notes (or fallback .md saved at case root)
- [ ] Case state saved to **dw-case-brain** — Phase 2 complete, ready for Phase 3

---

## PHASE 3 — Trial Notebook & Attorney Preparation

*Converts case analysis into actionable trial preparation. Cowork pre-builds all templates; attorneys complete cross and direct exam preparation using the integrated templates.*

### Step 1: Case Timeline Spreadsheet
Built from **Report 1** (Comprehensive Case Timeline) → `Case Tables.xlsx — Timeline Sheet`

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See "Case Tables Write Protocol" section above.

Columns to populate: Start Date | Start Time | End Date | End Time | Title | Subtitle | Description | Tags (Cowork Flags) | Bate Stamp | Notes

Rules:
- Sort all events in strict chronological order
- Color-code: prosecution events (light red) | defense-favorable (light green) | neutral (white)
- Hyperlink Source Doc column to corresponding file in Evidence Folder where possible
- Flag any timeline event that conflicts with another document in the Cowork Flags column
- Maintain all existing color coding, dropdown lists, and formatting

### Step 2: Update Witness Tables
The Witness Tables (Priority and Alpha) were initially populated in Phase 1 Step 4. Now update them with intelligence from Phase 2's case analysis:

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See "Case Tables Write Protocol" section above.

- Incorporate Report 8 (Key Witness Impeachment Plan) — bold-mark any witness with an Impeachment Plan as **KEY WITNESS** in both tables
- Re-rank Priority table: Key Witness (Report 8) > Eyewitnesses > Law Enforcement > Character Witnesses > Others
- Update the `Trial Exam Prepared (Y/N)` column as preparation progresses

### Step 3: Defense Shield & Defense Matrix

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See "Case Tables Write Protocol" section above.

This step has two parts: first, build the case-specific **Defense Shield** (the universe of potential defenses filtered to this case); then populate the **Defense Matrix** (charges mapped to the defenses you'll actually run).

#### 3A — Build the Case-Specific Defense Shield

The `Case Tables.xlsx` template contains **Defense Shield templates** — comprehensive catalogs of potential defenses organized by case type. These templates exist on the `Legal Defenses (Rape)` and `Legal Defenses (Homicide)` sheets. They are reference libraries, not checklists. Rarely if ever will every defense apply to a given case. Your job is to analyze the case facts and build a case-specific shield containing only the defenses that have traction.

**If a template exists for this case type** (currently: Rape, Homicide):

1. **Read the full template sheet** for this case type. Each row represents a potential defense category with columns for: Defense Category, Specific Defense, Priority/Feasibility, Key Action/Theory, Critical Expert/Witness Needed, Evidence Source/Location, and Litigation Checkpoint.

2. **Evaluate every defense row against the actual case facts.** For each potential defense, ask:
   - Does the discovery contain evidence supporting this defense?
   - Does the Case Profile (Section 4 — Case-Specific Defenses) flag facts relevant to this defense?
   - Do the 8 Case Analysis Reports identify weaknesses in the State's case that this defense exploits?

3. **Populate only the applicable defenses.** For each defense that has factual support in this case:
   - Keep the template's strategic guidance (Key Action/Theory column) as a starting framework
   - **Replace generic placeholders** with case-specific facts, Bate stamp references, witness names, and evidence locations from the actual discovery
   - **Update the Priority/Feasibility** column (High/Med/Low) based on the strength of the case-specific evidence — not the template default
   - **Fill in** the Critical Expert/Witness and Evidence Source columns with the actual witnesses and documents from this case file

4. **Remove defenses that clearly don't apply.** If a defense has zero factual support in the discovery (e.g., "Misidentification" in a case where identity isn't in dispute), delete that row from the case-specific sheet. A lean, focused shield is more useful than an exhaustive one full of inapplicable theories.

5. **Flag borderline defenses for attorney review.** When a defense has some factual support but isn't clearly viable — or when its applicability depends on facts only the attorney or client knows — mark it with a `⚖ ATTORNEY REVIEW` tag in the Priority column. Present these to the attorney with a brief explanation of what makes it borderline, and ask whether to keep or discard.

**If no template exists for this case type** (e.g., drug offenses, DWI, weapons charges, theft/fraud, domestic violence):

Build a new Defense Shield from scratch following the same column structure as the existing templates. The process:

1. **Research the charge elements** under Louisiana statutes. Identify what the State must prove for each count.
2. **Catalog potential defenses** organized by category (Constitutional, Identity, Forensic, Credibility, Mens Rea, Investigation, Procedural, etc.). Use the Rape and Homicide templates as structural models — the defense *categories* often overlap across case types even when the specific defenses differ.
3. **For each defense**, fill in all 7 columns: Defense Category, Specific Defense, Priority/Feasibility, Key Action/Theory of the Case, Critical Expert/Witness Needed, Evidence Source/Location, and Litigation Checkpoint.
4. **Populate only case-applicable defenses** — follow the same filtering logic as above.
5. **Save the new template** as a new sheet in `Case Tables.xlsx` named `Legal Defenses ([Case Type])` so it's available for future cases of the same type.

**Also populate the "Dealing with States Narrative" sheet.** This sheet contains 13 counter-narrative strategies (Ignore It, Make Lemonade, Backchain, Clarify & Polarize, Absurd, Use the Mirror, Moral Core, Own It, Drop It, Context, Undermine, Rules, Exclude It). The template includes both Rape-specific and Homicide-specific application columns. For this case:
- Link each strategy to the defense categories you've identified as applicable
- Write case-specific applications showing how each strategy applies to the actual facts and witnesses
- Not every strategy will be useful — populate only the ones that map to your defense theories

#### 3B — Populate the Defense Matrix

Now that the Defense Shield identifies *which* defenses apply, the Defense Matrix maps them to *specific charges*. Populate the Defense Matrix sheet in `Case Tables.xlsx`. Complete all 7 columns.

- **Charge column:** list each offense charged AND all responsive verdicts on separate rows
- Review `Art 814 Responsive Verdicts` document in `Trial Notebook → 01 - Jury Instructions & Selection`
- For each charge/responsive verdict row, pull the applicable defenses from the Defense Shield you just built
- Cross-reference: every defense in the Shield should map to at least one charge in the Matrix; any defense that doesn't map to a charge may not belong in the Shield
- Route jury instruction research and drafting to **dw-jury-instructions-builder** for comprehensive instruction set
- Route voir dire strategy to **dw-voir-dire-assistant** for juror challenge guidance

#### 3C — Initialize the Running List

The `Running List` sheet tracks defenses as they are discovered or refined throughout the life of the case. It has three columns: Litigation Phase, Defenses Raised/Discovered, and Source. The phases are pre-populated (Discovery, Motions, Witness notes, Exhibits, Demonstratives, Case Vocab, Voir Dire, Open/Close).

At this point, populate the Running List with any defenses already identified during Phases 1 and 2. As the case progresses through motions, witness prep, and trial, update the Running List whenever a new defense theory emerges or an existing one gains/loses support. The Running List feeds back into the Defense Shield — if a new defense surfaces during motions practice, add it to the Shield and Matrix.

### Step 4: Version Control — Amended & Superseded Documents
When the prosecution sends corrected or supplemental productions:

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See "Case Tables Write Protocol" section above.

- Maintain a version control log to keep the Master Evidence Table accurate
- Mark superseded documents clearly in the Evidence Table
- Do not delete prior versions — archive with notation

### Step 5: Case Readiness Memo
The attorney's single entry point into the Trial Notebook — one-page summary of everything the attorney needs to know before diving into the file.

Inputs: all 8 case analysis reports, Cowork parallel analysis, current case status

### Step 6: Discover the Story Worksheet (Case Story Development)
Complete before witness preparation begins. This is the foundation of the defense narrative and informs all witness examination preparation.

### Step 7: Cross Exam Preparation (Per Key Witness)
*Attorney work — Cowork prepopulates templates with available intelligence. Route specialist witness types to appropriate skills. Complete for all Key Witness Impeachment Plan witnesses and Top 10 priority witnesses only.*

**7A — Witness Cross Battle Card:** one-page intelligence summary per witness
- **Eyewitness to crime** → route to **dw-eyewitness-identification-auditor** for ID weakness analysis
- **Law enforcement officer** → route to **dw-cross-exam-architect** for hostile witness strategy
- **Expert witness (prosecution)** → route to **dw-expert-witness-evaluator** for methodology challenges
- **Save location:** `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`

**7B — Mapping the Cross Worksheet:** prepopulate from impeachment materials, Report 8, and all prior statements. Route to **dw-cross-exam-architect** for strategic question mapping.

**7C — Cross Exam Template:** prepopulate structure and available impeachment points; leave question sequencing and line of attack to attorney. Route specialized witness cross (confessions, interrogation tactics, mobile forensics, video authentication) to appropriate specialist skills.

### Step 8: Direct Exam Preparation (Per Defense Witness)
*Attorney work — Cowork prepopulates templates with intelligence from Discover the Story worksheet and Witness Dossiers.*

**8A — Mapping the Direct Worksheet**

**8B — Direct Exam Template**
- **Save location:** `01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`

### Step 9: Opening Statement & Closing Argument Preparation
*Attorney-driven — Cowork populates the framework from case analysis outputs.*

Populate the Mapping the Story templates (Opening and Closing) from: Report 4 (Core Defense Narrative), Report 6 (Memorable Theme), and the Discover the Story worksheet.

### Step 10: Appellate Readiness
*Post-conviction and during trial preparation — monitor for appealable issues.*

Route preservation of trial error, evidentiary challenges, and appellate strategy to **dw-appellate-error-monitor** to ensure all grounds for appeal are documented and preserved for post-conviction review.

After verdict and sentence, when the appellate record is designated and the ranked-issue output from `dw-appellate-error-monitor` is in hand, route brief drafting to **dw-appellate-brief-builder** for the direct-appeal brief (assignments of error, statement of facts with record cites, per-assignment argument structured as standard of review → preservation → law → application → prejudice, and reply brief). For collateral relief (PCR, federal habeas, sentence modification) instead of direct appeal, route to **dw-post-conviction-relief**.

### Step 11: Trial Day Support
*During trial — fast-cycle, in-court support.*

Route real-time trial-day support to **dw-trial-day-assistant** for: daily docket, real-time objection log (which feeds upstream to **dw-appellate-error-monitor**), witness scorecards (which feed **dw-cross-exam-architect** for next-day prep), exhibit tracker, juror observation log including Batson tracking, end-of-day recap with overnight tasks, and mid-trial issue spotter (Brady, surprise testimony, mistrial triggers under La. C.Cr.P. Art. 770/771). The trial-day assistant produces short, scannable outputs designed for use during breaks and at counsel table — final polish rolls into the trial notebook via Step 12.

### Step 12: Assemble Trial Notebook
*Final assembly — triggered when all Phase 3 deliverables are complete.*

Route to **dw-trial-notebook-builder** to assemble all Phase 2 and Phase 3 deliverables into the final Trial Notebook. The trial notebook builder scans the case folder for all upstream deliverables, organizes them into the Trial Notebook folder structure, generates a master index, and produces a Trial Readiness Gap Report identifying any missing items.

---

## Quick Reference

### Cowork Action Types
- ⚡ **COWORK ACTION** — Claude executes this step
- ⚠ **STAFF ACTION** — Human staff executes; Claude may assist or verify
- ⚖ **ATTORNEY ACTION** — Attorney-only; Claude prepopulates supporting materials only
- ✓ **QUALITY GATE** — Must be confirmed before advancing to next phase
- 📋 **TEMPLATE GUIDE** — Reference for populating a specific document

### Standard Folder Structure Reference
```
[Case Root]/
├── Case Tables.xlsx                    ← Master data file — never replace
├── 01 - Trial Notebook/
│   ├── 01 - Jury Instructions & Selection/
│   ├── 03 - Witnesses/                 ← Impeachment Worksheets filed here
│   ├── 05 - Evidence/                  ← Bate-stamped, OCR'd docs + A/V
│   └── 09 - Case Analysis/             ← Reports 2-8
└── 02 - Pretrial Notebook/
    ├── 01 - Pleadings/
    ├── 02 - Discovery/
    ├── 03 - Case Analysis & Notes/
    │   ├── 000 - Case Profile.docx     ← Single deliverable: Part 1 + Part 2A/2B/2C
    │   └── Cowork Analysis/            ← Parallel analysis outputs
    └── 06 - Law & Research/            ← Missing Discovery Demand Letters
```

### Case Tables.xlsx — Sheet Reference
The master template in `assets/Case Tables.xlsx` contains all sheets below with pre-formatted headers, column structures, dropdowns, and color coding. Copy it to new case roots; never create sheets from scratch.

| Sheet Name | Contents | Phase Populated |
|------------|----------|-----------------|
| Evidence Table | Master discovery index (11 columns) | Phase 1 Step 4 |
| Timeline Sheet | Chronological case events (10 columns) | Phase 2 Report 1 / Phase 3 Step 1 |
| Witness List - Alpha | Alphabetical witness list (6 columns) | Phase 1 Step 4 → Phase 3 Step 2 |
| Witness List - Priority | Priority-ranked witness list (6 columns) | Phase 1 Step 4 → Phase 3 Step 2 |
| Defense Matrix | Charges, responsive verdicts, defenses (7 columns) | Phase 3 Step 3B |
| Legal Defenses (Rape) | **Defense Shield template** — sex offense defense catalog (7 columns) | Phase 3 Step 3A (sex offense cases only) |
| Legal Defenses (Homicide) | **Defense Shield template** — homicide defense catalog (7 columns) | Phase 3 Step 3A (homicide cases only) |
| Legal Defenses ([Case Type]) | **Defense Shield template** — created for new case types as needed (7 columns) | Phase 3 Step 3A (when no template exists) |
| Dealing with States Narrative | Counter-narrative strategies — Rape & Homicide applications (6 columns) | Phase 3 Step 3A |
| Running List | Defenses discovered/refined during each litigation phase (3 columns) | Phase 3 Step 3C → ongoing through trial |

### Document Naming Convention
- All documents: `[3-digit prefix] - [Document Name].docx`
- Audio/video folders: `[3-digit prefix] - [Name]/`
- Transcripts: named identically to their corresponding A/V file
- Missing Discovery Demand Letters: `Missing Discovery Demand — [Date].docx`
- Impeachment Worksheets: one per key witness, filed in `Trial Notebook → 03 - Witnesses`

---

## Changelog

### v5.3 (April 2026)
- **MERGED:** `dw-lwop-populator` is now part of this skill. The standalone populator skill has been retired.
- **NEW reference files:** `references/lwop-field-maps.md` and `references/lwop-extraction-patterns.md` (both moved from the populator's `references/` folder).
- **NEW assets/legacy/ folder:** archives the two original Calcasieu PDO standalone templates (`LWOP Homicide Review Sheet - FOR TYPING.docx`, `LWOP Sex Offense Review Sheet - FOR TYPING.docx`) for reference. They are no longer used as the output substrate.
- **Phase 1 Step 3 expanded:** absorbs the populator's full workflow — extraction priority order, source-priority rules, formatting conventions, attorney-only field handling, field-completeness checklist, completion notes.
- **NEW: Refresh Mode** added as a sub-mode of Phase 1 Step 3. Handles late-discovery updates that previously triggered standalone populator runs. Strict merge rules preserve all attorney-entered content; Refresh Log entry appended to the document on each refresh.
- **Trigger phrases added** to skill description: "fill out the LWOP sheet," "LWOP review," "District Defender review," "life without parole worksheet," "refresh the Case Profile."
- **Documentation patch** for Part 1 Section 5 (Prior Criminal History): explicit format guidance for LWOP cases (`MM-DD-YYYY — Offense Name (Disposition)`) vs. non-LWOP narrative form.
- **HIPAA spelling normalized** throughout (legacy templates retained "HIPPA" typo; v5.3 references and unified template use "HIPAA").

### v5.2 (April 2026)
- Consolidated former Initial Case Profile, Criminal Defense Cover, and standalone LWOP review sheet into single `000 - Case Profile.docx` with Part 1 + Part 2A/2B/2C.
- Report 8 (Witness Table) removed — witness data is captured in Case Tables.xlsx during Phase 1 Step 4.
- Former Report 9 renumbered to Report 8.
- Bundled resources: 8 report prompt templates, output path convention, Case Tables.xlsx master template, Evidence Placeholder template, generate_placeholders.py script.

---

*This skill reflects Daniels & Washington Cowork Workflow Version 5.3 (April 2026). Update this file whenever the master workflow document is revised.*
