# Extraction Patterns for Discovery Documents

This reference describes the common document types found in Calcasieu Parish criminal discovery and how to extract structured data from each.

## Document Recognition

### By Filename Patterns
| Pattern | Document Type |
|---------|--------------|
| `*incident*`, `*report*`, `*supplemental*` | Police/Incident Report |
| `*autopsy*` | Autopsy Report |
| `*SANE*`, `*PERK*`, `*sexual assault*` | SANE Exam Report |
| `*CAC*`, `*advocacy*`, `*forensic interview*` | CAC Interview |
| `*lab*`, `*toxicology*`, `*DNA*` | Lab Report |
| `*statement*`, `*interview*`, `*transcript*` | Witness/Defendant Statement |
| `*indictment*`, `*bill of information*`, `*bill of particulars*` | Charging Instrument |
| `*booking*`, `*arrest*`, `*intake*` | Booking/Intake Document |
| `*criminal history*`, `*rap sheet*`, `*NCIC*` | Criminal History |
| `*motion*` | Filed Motion |
| `*HIPAA*`, `*HIPPA*`, `*medical*`, `*LCMH*` | Medical Records |
| `*school*`, `*IEP*`, `*education*` | School Records |
| `*bond*` | Bond Documents |
| `*investigator*`, `*investigation*` | Investigator Reports/Requests |
| `*offer*`, `*plea*` | Plea Offers |
| `*CRIMINAL DEFENSE COVER*` | D&W Case Cover Sheet |
| `*LWOP*` | Existing LWOP Sheet (may have partial data) |
| `*Defense Shield*`, `*Defense Matrix*`, `*Case Tables*` | D&W Analysis Spreadsheets |

### By Content Markers
When filenames aren't descriptive, scan the first page for:
- "STATE OF LOUISIANA" + "vs." → Charging instrument or court filing
- "CALCASIEU PARISH SHERIFF'S OFFICE" → Police report
- "REPORT OF INVESTIGATION" → Supplemental police report
- "AUTOPSY REPORT" or "OFFICE OF THE CORONER" → Autopsy
- "SEXUAL ASSAULT NURSE EXAMINER" → SANE report
- "CHILDREN'S ADVOCACY CENTER" → CAC interview
- "VOLUNTARY STATEMENT" → Witness/defendant statement
- "MIRANDA" or "RIGHTS" → Defendant statement (check Miranda compliance)
- "NATIONAL CRIME INFORMATION CENTER" → Criminal history

## Extraction Priority Order

When populating the review sheet, read documents in this order. Earlier documents provide the framework; later documents fill in details and flag inconsistencies.

1. **Charging Instrument** (Indictment/Bill) — establishes charges, docket number, defendant name, victim name(s)
2. **Criminal Defense Cover** (if exists) — may have fields already completed by attorney
3. **Existing LWOP Sheet** (if exists) — may have partial data from earlier review
4. **Police/Incident Report** — core facts, witnesses, timeline, officer information
5. **Defendant Statement** — Miranda status, confession/denial, voluntariness
6. **Witness Statements** — corroboration or inconsistency with police report
7. **Autopsy Report** (homicide) / **SANE Report** (sex offense) — forensic evidence
8. **Lab Reports** — toxicology, DNA, ballistics
9. **CAC Interview** (sex offense) — victim's account
10. **Criminal History** — prior convictions
11. **Medical Records** — HIPAA-related records
12. **Investigator Reports** — defense investigation results
13. **Filed Motions** — motions section data
14. **Bond Documents** — bond reduction data
15. **D&W Spreadsheets** (Defense Shield, Case Tables) — may contain additional analysis

## Critical Sourcing Rules

These fields have specific sourcing requirements — always follow these rules:

| Field | Source | How to Find It |
|-------|--------|---------------|
| Indictment Date | Grand Jury Indictment / Bill of Information | The date printed on the charging instrument itself (filing date), not the offense date |
| Age at Time of Offense | Client's DOB vs. offense date | Find DOB in booking/intake docs, rap sheet, or police report; calculate age at offense date |
| Indictment Attached | N/A | Always mark **Yes** |
| Prior Convictions | Client's rap sheet / NCIC printout | Look for criminal history document; format as MM-DD-YYYY -- Offense Name |

## Data Extraction Tips

### Police Reports
- **Officer names** appear in the header or signature block — extract for witness list
- **Dispatch/arrival times** are usually in the first paragraph — critical for timeline
- **Witness names** often appear as "Contact was made with [NAME]" or "Statement taken from [NAME]"
- **Miranda warnings** — search for "Miranda," "rights," "advised" — extract exact language used
- **Weapons/evidence** — search for "seized," "recovered," "collected," "item #"

### Witness Statements
- **Who took the statement** — name and rank, usually in header
- **Date/time** of statement
- **Key admissions or observations** — the meat of the summary
- **Inconsistencies** — compare timestamps, descriptions of events, sequences of actions across different witness statements

### Defendant Statements
These deserve extra scrutiny because they directly impact suppression analysis:
- Was Miranda given? (Look for Miranda waiver form reference)
- Was Miranda invoked at any point? (Look for "I want a lawyer" or similar)
- Was the statement voluntary? (Look for duration, breaks, food/water, threats/promises)
- Was Reid technique or similar interrogation method used?
- Does the statement contain a confession or admissions against interest?
- Are the statements internally consistent?

### Autopsy Reports (Homicide)
- **Medical Examiner name** — for the "Performed by" field
- **Cause of death** — relevant to charges and defenses
- **Manner of death** — homicide, accident, undetermined
- **Toxicology results** — both victim and defendant if available
- **Injury pattern** — relevant to theory of case

### SANE Reports (Sex Offense)
- **Examiner name** — for the "Performed by" field
- **Exam date** — may differ from offense date
- **Findings** — injuries consistent/inconsistent with allegations
- **Evidence collected** — specimens for DNA analysis

### CAC Interviews (Sex Offense)
- **Interviewer name** — for witness list
- **Child's disclosures** — what was said, level of detail
- **Leading questions** — potential impeachment material
- **Consistency with other accounts**

## Handling Missing Information

When a field cannot be populated from available discovery:
- **Leave the field blank** — do not write "N/A" or "Unknown"
- **Add a note at the end of the document** listing all fields that could not be populated and what documents would be needed to complete them
- **Exception:** If there's a partial answer (e.g., you know there are witnesses but not all their names), populate what you can and note what's incomplete

## Handling Conflicting Information

When different documents provide contradictory information for the same field:
- **Use the most authoritative source** (charging instrument > police report > witness statement)
- **Note the conflict** in the relevant field — e.g., "March 17, 2023 (per indictment; police report states March 18)"
- **Flag for attorney review** in your completion notes
