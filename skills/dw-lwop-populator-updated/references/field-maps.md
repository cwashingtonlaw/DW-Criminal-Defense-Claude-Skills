# LWOP Review Sheet Field Maps

This document defines **every field** in both review sheet templates and how to extract data for each from discovery materials. It also serves as the mandatory completeness checklist referenced in Step 6 of the SKILL.md.

Every field listed below must appear in the final output document. If data is unavailable, leave the value cell blank — but the field itself must exist. Never merge, skip, or omit a field.

---

## Homicide Template — Complete Field Inventory

### Section 1: KEY DATES & DEADLINES (Blue-Gray header)

New summary section for quick reference during District Defender status meetings.

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| H-1 | Offense Date | Indictment → Police Report | Same as DATE OF OFFENSE in Case Info; duplicated here for quick reference |
| H-2 | Arrest Date | Booking/Intake → Police Report | Date of arrest/booking |
| H-3 | Indictment Date | Indictment header | Date the indictment was filed |
| H-4 | Arraignment Date | Court filings / Case docket | Date of arraignment |
| H-5 | Discovery Filed | Discovery motion | Date discovery motion was filed |
| H-6 | Discovery Received | Download log / Cover letter | Date discovery was received from State |
| H-7 | Next Court Date | Court filings / Attorney notes | Upcoming court date |
| H-8 | Trial Date | Court filings / Attorney notes | Scheduled trial date if set |

### Section 2: CASE INFORMATION (Blue header)

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| H-9 | STATE v. | Indictment/Bill → Police Report → Folder name | Full legal name from charging instrument |
| H-10 | DOCKET NO: | Indictment/Bill → Court filings | Format: XXXXX-XX (Calcasieu Parish) |
| H-11 | DATE OF OFFENSE: | Indictment → Police Report | Include time if available. Range for ongoing offenses. |
| H-12 | AGE AT TIME OF OFFENSE: | Calculate from DOB and offense date | If DOB unavailable, note approximate age |
| H-13 | CO-DEFENDANT(S): | Indictment → Police Report | List all names |
| H-14 | Co-Defendant — Separately charged? | Indictment → Court records | Yes/No for each co-defendant |
| H-15 | Co-Defendant — Plea status: | Court records / Discovery | Pending, pled guilty, cooperating, etc. |
| H-16 | Co-Defendant — Cooperating? | Discovery / Attorney notes | Whether co-defendant is cooperating with State |
| H-17 | ALLEGED VICTIM(S) (* = deceased) | Police Report / Autopsy / Death Certificate | **HOMICIDE:** Place asterisk * by name of deceased victims |
| H-18 | CHARGES: | Indictment/Bill of Information | Include LA statute number (e.g., "14:30 First Degree Murder"). Each count separately. |
| H-19 | AGGRAVATING FACTOR(S): | Indictment → Police Report → Witness Statements | La. C.Cr.P. art. 905.4 factors. Include specific alleged acts. |
| H-20 | INDICTMENT ATTACHED: | Case folder check | Checkbox: Yes / Not Received / Amended |
| H-21 | THEORY OF THE CASE — Initial Theory | Attorney notes / Criminal Defense Cover | **Attorney field.** Leave blank if no notes. |
| H-22 | THEORY OF THE CASE — Trial Theory | Attorney notes | **Attorney field.** Always leave blank. |
| H-23 | PRIOR CONVICTIONS: | Rap sheet / NCIC | Format: MM-DD-YYYY -- Offense Name. Include dispositions. |
| H-24 | WITNESS(ES): | Police Report → All statements → Transcripts | Every named witness with role and count |
| H-25 | WITNESS STATEMENT(S): | All witness statements | Detailed summaries. Bold names and quotes. Note inconsistencies. |
| H-26 | POLICE REPORT: | Incident/supplemental reports | Times, locations, officer actions, dispatch/arrival. |
| H-27 | DEFENSE(S): | Attorney notes / Case analysis | Mark "Preliminary — attorney review required" if no notes |
| H-28 | POSSIBLE DEFENSE WITNESS(ES): | Attorney notes / Case analysis | Alibi, character, expert witnesses |

### Section 3: DEFENDANT STATEMENT (Red header)

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| H-29 | STATEMENT(S) BY DEFENDANT | Client statements in discovery | Name/rank of person taking statement, summary of substance. Flag voluntariness issues. |

### Section 4: SUPPRESSION ANALYSIS (Deep Orange header)

Consolidated section — Miranda sub-fields moved here from Discovery, combined with suppression determination.

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| H-30 | Miranda advised? | Client statement / Miranda waiver form | Yes/No |
| H-31 | Miranda invoked? | Client statement | Did client invoke rights? |
| H-32 | Voluntary? | Client statement analysis | Duration, breaks, food/water, threats/promises |
| H-33 | Reid technique? | Client statement | Was Reid or similar interrogation method used? |
| H-34 | Confession? | Client statement | Does the statement contain a confession? |
| H-35 | Statements credible? | Client statement | Are statements internally consistent? |
| H-36 | Against client's interest? | Client statement | Statements against interest? |
| H-37 | SHOULD A MOTION TO SUPPRESS BE FILED? | Analysis | Yes/No determination |
| H-38 | WHY? | Analysis | Basis for suppression |
| H-39 | Suppression basis / details: | Analysis | Full explanation — Miranda, search/seizure, coercion, illegal stop |

### Section 5: MOTIONS (Orange header)

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| H-40 | DISCOVERY; date filed: | Filed motions | Date discovery motion was filed |
| H-41 | BILL OF PARTICULARS; date filed: | Filed motions | Date filed |
| H-42 | SUPPRESSION(s): | Constitutional analysis | Basis for each suppression motion |
| H-43 | IN LIMINE: | Case analysis | Motions to exclude evidence |
| H-44 | REVEAL THE DEAL: | Discovery — informant info | Deals between State and witnesses |
| H-45 | BOND REDUCTION: | Filed motions / Bond docs | Whether filed |
| H-46 | BOND REDUCTION — Date filed: | Filed motions | Date filed |
| H-47 | Original amount: | Bond docs | Original bond amount |
| H-48 | Bond after reduction hearing: | Bond docs / Court minutes | Amount after hearing |
| H-49 | SPEEDY TRIAL: | Case timeline | Speedy trial issues |
| H-50 | List of other Motions: | All filed motions | List with dates filed |
| H-51 | Reports Checklist: | Case folder inventory | Check applicable items |
| H-52 | PRESCRIPTION: | Statute of limitations | Period and whether it's an issue |
| H-53 | Does Defendant want to testify? | — | **Attorney field.** Always leave blank. |

### Section 6: INVESTIGATION (Green header)

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| H-54 | INVESTIGATOR ASSIGNED: | Investigator request form | Name |
| H-55 | INVESTIGATOR REQUEST FORM COMPLETED ON: | Investigator request form | Date |
| H-56 | INVESTIGATION REQUESTED BY ATTORNEY: | Investigator request form | Attorney name |
| H-57 | RESULTS OF INVESTIGATION: | Investigator reports | Summary of findings |

### Section 7: EVIDENCE INVENTORY (Purple header)

Split from old Discovery section. Focuses on what physical/documentary evidence exists.

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| H-58 | DATE FILED: | Discovery motion | Date discovery was filed |
| H-59 | DATE RECEIVED: | Download log / Cover letter | Date received from State |
| H-60 | Police Reports — Count: | Discovery inventory | **NEW.** Number of police reports received |
| H-61 | Police Reports — Are any missing? | Discovery inventory | Note which are missing |
| H-62 | Video(s) — Count: | Discovery inventory | **NEW.** Number of videos |
| H-63 | Video(s) — Are they viewable? | Discovery inventory | Viewing status |
| H-64 | Video(s) — Date first viewed by attorney | Attorney log | Date |
| H-65 | Photo(s) — Count: | Discovery inventory | **NEW.** Number of photos |
| H-66 | Photo(s) — Are they clear? | Discovery inventory | Quality |
| H-67 | Photo(s) — Date first viewed by attorney | Attorney log | Date |
| H-68 | Autopsy — Performed by: | Autopsy report | **HOMICIDE-SPECIFIC.** Medical Examiner name |
| H-69 | Autopsy — Date first read by attorney | Attorney log | Date |
| H-70 | Lab type: | Lab reports | **NEW.** DNA, toxicology, ballistics, digital forensics, etc. |
| H-71 | Lab(s) — Deceased: | Lab reports | **HOMICIDE-SPECIFIC column.** |
| H-72 | Lab(s) — Client: | Lab reports | Whether labs exist for client |
| H-73 | Lab(s) — Co-Defendant: | Lab reports | Whether labs exist for co-defendant |
| H-74 | Lab(s) — Witness: | Lab reports | Whether labs exist for witness |
| H-75 | Other Forensic(s): | Discovery inventory | DNA, ballistics, digital forensics, etc. |
| H-76 | Witness Statements — Count: | Discovery | **NEW.** Number of witness statements |
| H-77 | Witness Statements — Date first reviewed by attorney | Attorney log | Date |
| H-78 | Client Statement(s) | Discovery | Note: Miranda sub-fields now in Suppression Analysis section |
| H-79 | Co-Defendant(s)' Statement(s): | Discovery | Summarize |
| H-80 | Miscellaneous Discovery: | Discovery inventory | Anything not covered above |

### Section 8: RECORDS & AUTHORIZATIONS (Teal header)

Split from old Discovery section. Focuses on records requests and authorizations.

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| H-81 | HIPPA: | Medical records releases | Whether forms exist |
| H-82 | Date HIPPA Signed: | HIPPA form | Date authorization signed |
| H-83 | Date HIPPA Requested: | Records request log | Date records requested |
| H-84 | Date HIPPA Received: | Records receipt log | Date records received |
| H-85 | School Record(s): | School records | Whether present |
| H-86 | IEP: | School records / IEP | IEP status |
| H-87 | Date Records Requested: | Records request log | Date school records requested |
| H-88 | Date IEP Requested: | Records request log | Date IEP requested |

**Homicide template total: 88 checklist items (H-1 through H-88)**

---

## Sex Offense Template — Complete Field Inventory

The Sex Offense template is identical to Homicide except where noted below. All shared fields use the same checklist numbers.

### Section 1: KEY DATES & DEADLINES
Identical to Homicide (H-1 through H-8).

### Section 2: CASE INFORMATION
All fields identical except:

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| S-17 | ALLEGED VICTIM(S) (Include ages & birth dates) | Police Report / CAC / Indictment | **SEX OFFENSE-SPECIFIC.** Ages and DOBs for all alleged victims. |

**Sex Offense AGGRAVATING FACTOR(S) note:** Focus on: age of victim, relationship to defendant, use of force, threats, position of trust/authority.

### Section 3: DEFENDANT STATEMENT
Identical to Homicide (H-29).

### Section 4: SUPPRESSION ANALYSIS
Identical to Homicide (H-30 through H-39).

### Section 5: MOTIONS
Identical to Homicide (H-40 through H-53).

### Section 6: INVESTIGATION
Identical to Homicide (H-54 through H-57).

### Section 7: EVIDENCE INVENTORY
Fields H-58 through H-67 are identical (dates, police reports, videos, photos). Then it diverges:

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| S-68 | SANE Exam — Performed by: | SANE report | **SEX OFFENSE-SPECIFIC.** Replaces Autopsy. Examiner name. |
| S-69 | SANE Exam — Date first read by attorney | Attorney log | Date |
| S-70 | CAC Video — Is it viewable? | CAC interview video | **SEX OFFENSE-SPECIFIC.** Additional field not in Homicide. |
| S-71 | CAC Video — Date first viewed by attorney | Attorney log | Date |
| S-72 | Lab type: | Lab reports | DNA, toxicology, etc. |
| S-73 | Lab(s) — Accuser: | Lab reports | **SEX OFFENSE-SPECIFIC.** Replaces "Deceased" column. |
| S-74 | Lab(s) — Client: | Lab reports | Whether labs exist for client |
| S-75 | Lab(s) — Co-Defendant: | Lab reports | Whether labs exist for co-defendant |
| S-76 | Lab(s) — Witness: | Lab reports | Whether labs exist for witness |

Remaining fields (Other Forensics, Witness Statements, Client Statement, Co-Defendant Statements, Miscellaneous) are identical to Homicide.

### Section 8: RECORDS & AUTHORIZATIONS
Identical to Homicide (H-81 through H-88).

**Sex Offense template total: 92 checklist items** (88 base + 2 CAC Video fields + 2 from SANE replacing Autopsy at same count, but CAC adds net 2)

### Submission note difference
- **Homicide:** "To be submitted to the District Defender"
- **Sex Offense:** "To be submitted to the District Defender 30 days after appointment and again every consecutive 30 days."

---

## Quick Reference: Fields That Differ Between Templates

| Field Area | Homicide | Sex Offense |
|-----------|----------|-------------|
| Title | LWOP HOMICIDE CASE REVIEW SHEET | LWOP SEX CASE REVIEW SHEET |
| Submission note | "To be submitted to the District Defender" | "...30 days after appointment and again every consecutive 30 days." |
| Alleged Victims | "Place an asterisk * by deceased" | "Include ages & birth dates" |
| Evidence — forensic exam | Autopsy / Performed by / Date first read | SANE Exam / Performed by / Date first read |
| Evidence — additional media | (none) | CAC Video / Is it viewable? / Date first viewed |
| Labs — party column | Deceased | Accuser |

---

## Quick Reference: New Fields (v2 Enhancements)

These fields are new additions not present in the original PDO template:

| Field | Section | Purpose |
|-------|---------|---------|
| Arrest Date | Key Dates | Quick reference |
| Indictment Date | Key Dates | Quick reference |
| Arraignment Date | Key Dates | Quick reference |
| Next Court Date | Key Dates | Quick reference |
| Trial Date | Key Dates | Quick reference |
| Co-Defendant — Separately charged? | Case Info | Cooperation tracking |
| Co-Defendant — Plea status | Case Info | Cooperation tracking |
| Co-Defendant — Cooperating? | Case Info | Cooperation tracking |
| Suppression basis / details | Suppression Analysis | Consolidated suppression reasoning |
| Police Reports — Count | Evidence Inventory | Volume tracking |
| Video(s) — Count | Evidence Inventory | Volume tracking |
| Photo(s) — Count | Evidence Inventory | Volume tracking |
| Lab type | Evidence Inventory | Type specificity (DNA, tox, ballistics) |
| Witness Statements — Count | Evidence Inventory | Volume tracking |

---

## Criminal Defense Case Management Sections (Sections 9–17)

These sections are appended after the LWOP Review sections in both templates. They come from the firm's Criminal Defense Cover template and are identical across both Homicide and Sex Offense templates. These pages provide supplemental case management tracking beyond what the District Defender review requires.

### Section 9: TO DO LIST

Two pages of task tracking tables.

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-1 | TO DO | Attorney notes / Case analysis | Task description — leave blank for attorney |
| C-2 | COMMENTS | Attorney notes | Notes on the task — leave blank for attorney |
| C-3 | DEADLINE | Court filings / Calendar | Due date — populate if tied to known court date |

### Section 10: ARRAIGNMENT LOG

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-4 | Date | Court docket / Arraignment records | Date of arraignment |
| C-5 | Charges | Indictment / Bill | Charges read at arraignment |
| C-6 | Prosecutor | Court records | Prosecuting ADA name |
| C-7 | Judge | Court records | Presiding judge |
| C-8 | NOTES | Attorney notes | Plea entered, bail set, continuance, etc. |

### Section 11: BAIL/BOND & PROBATION/PAROLE

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-9 | Release on Recognizance (ROR) | Bond docs / Court minutes | Checkbox — check if ROR granted |
| C-10 | REMAND | Bond docs / Court minutes | Checkbox — check if remanded |
| C-11 | BAIL SET/EXAM ORDERED | Bond docs / Court minutes | Checkbox — check if bail set, with amount |
| C-12 | BAIL NOTES | Bond docs / Attorney notes | Free-text notes on bail conditions, arguments |
| C-13 | BOND $ | Bond docs | Bond amount set by court |
| C-14 | Cash $ | Bond docs | Cash bond amount if applicable |
| C-15 | Parole/Probation Officer | Probation records | Name of supervising officer |
| C-16 | Parole/Probation Expires | Probation records | Expiration date of parole/probation |
| C-17 | Sentence Eligibility | Sentencing records | Sentence eligibility information |

**Note:** The LWOP Review Motions section (H-45 through H-48) tracks bond reduction filings. This section tracks the broader bail/bond status and probation/parole details — they are complementary, not duplicative.

### Section 12: CLIENT INTERVIEW FORMS (×3)

Three blank interview templates. These are attorney-use forms — leave all fields blank unless the attorney has existing notes.

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-18 | Purpose | — | **Attorney field.** Always leave blank. |
| C-19 | Name | — | Client name — may pre-populate from Case Info |
| C-20 | Topic | — | **Attorney field.** Always leave blank. |
| C-21 | Date | — | **Attorney field.** Always leave blank. |
| C-22 | Primary Question/Issue | — | **Attorney field.** Always leave blank. |
| C-23 | Questions/Issues | — | **Attorney field.** Always leave blank. |
| C-24 | Notes | — | **Attorney field.** Always leave blank. |
| C-25 | Summary | — | **Attorney field.** Always leave blank. |

### Section 13: CLIENT BACKGROUND INFO

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-26 | PRIOR CRIMINAL HISTORY | Rap sheet / NCIC / Court records | Narrative summary of criminal history (complements the structured H-23 field) |
| C-27 | FAMILY/HOME LIFE | Mitigation materials / PSI | Family structure, living situation, dependents |
| C-28 | EDUCATIONAL HISTORY | School records / Client intake | Education level, schools attended, IEP/special education |
| C-29 | EMPLOYMENT HISTORY | Client intake / Mitigation | Employment history, current job, skills |
| C-30 | MEDICAL/MENTAL HEALTH/SUBSTANCE ABUSE | Medical records / HIPPA returns | Diagnoses, treatment history, medications, substance use |
| C-31 | OTHER RELEVANT INFO | Various | Military service, community ties, character references |

### Section 14: FAMILY/FRIENDS CONTACT LIST

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-32 | PERSON | Discovery / Client intake | Name of family member or friend |
| C-33 | RELATION | Discovery / Client intake | Relationship to client |
| C-34 | CONTACT INFO | Discovery / Client intake | Phone, address, email |

### Section 15: COURT APPEARANCES LOG

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-35 | Date | Court docket | Date of court appearance |
| C-36 | ADA/Judge | Court docket | Prosecutor and judge present |
| C-37 | Bail Status | Court minutes / Bond docs | Current bail status at that appearance |
| C-38 | Notes | Attorney notes / Court minutes | What happened — motions heard, continuance, etc. |

### Section 16: WITNESS INTERVIEW FORMS (×2)

Two blank interview templates for witness interviews. Same structure as Client Interview forms.

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-39 through C-46 | (Same fields as C-18 through C-25) | — | **Attorney field.** Always leave blank. |

### Section 17: PLEA DISCUSSIONS LOG

| # | Field Label | Source Priority | Extraction Notes |
|---|-------------|----------------|------------------|
| C-47 | PLEA OFFER | Discovery / Plea correspondence | Description of the plea offer |
| C-48 | COMMENTS | Attorney notes | Attorney's analysis, client's response |
| C-49 | DATE | Plea correspondence | Date offer was made or discussed |

**Criminal Defense Case Management total: 49 checklist items (C-1 through C-49)**

---

## Determining Case Type

Use this decision tree:

1. **Check charges:**
   - Murder (14:30, 14:30.1), Manslaughter (14:31), Negligent Homicide (14:32) → **HOMICIDE**
   - Rape (14:42, 14:42.1, 14:43, 14:43.1), Sexual Battery (14:43.1), Molestation (14:81.2), Indecent Behavior (14:81) → **SEX OFFENSE**

2. **Check folder name:** Keywords "Murder," "Homicide," "Rape," "Sex"

3. **Check discovery:** Autopsy report → likely homicide. SANE/CAC → likely sex offense.

4. **Both charges:** Generate BOTH sheets.

5. **Unclear:** Ask the attorney.
