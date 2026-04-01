# LWOP Review Sheet Field Maps

This document defines every field in both review sheet templates and how to extract data for each field from discovery materials. Use this as your extraction guide.

## Shared Fields (Both Homicide and Sex Offense)

These fields appear in both templates with identical meaning:

### Header Section

| Field | Source Priority | Extraction Notes |
|-------|----------------|------------------|
| STATE v. | Indictment/Bill of Information → Police Report header → Case folder name | Full legal name as it appears on the charging instrument |
| DOCKET NO | Indictment/Bill → Court filings | Format: XXXXX-XX (Calcasieu Parish) |
| DATE OF OFFENSE | Indictment → Police Report → Incident Report | Include time if available. Use range for ongoing offenses. |
| AGE AT TIME OF OFFENSE | Calculate from DOB (intake/booking) and offense date | If DOB unavailable, note approximate age from reports |
| CO-DEFENDANT(S) | Indictment → Police Report | List all. Note if separately charged. |
| CHARGES | Indictment/Bill of Information | Include Louisiana statute number (e.g., "14:42 First Degree Rape"). List each count separately. |
| AGGRAVATING FACTOR(S) | Indictment → Police Report → Witness Statements | For homicide: factors under La. C.Cr.P. art. 905.4. For sex: age of victim, relationship, use of force, threats. |
| INDICTMENT ATTACHED | Check case folder for indictment PDF | Mark: Yes, Not Received, or Amended |
| THEORY OF THE CASE (Initial) | Attorney notes / Criminal Defense Cover | If no attorney notes exist, leave blank — this is attorney work |
| THEORY OF THE CASE (Trial) | Attorney notes | Always leave blank — attorney completes at trial prep |
| PRIOR CONVICTIONS | Rap sheet / Criminal history / NCIC | List date and offense for each. Include dispositions if available. |
| WITNESS(ES) | Police Report witness list → All statements → Interview transcripts | List every named witness with role (e.g., "eyewitness," "responding officer," "forensic analyst") |
| WITNESS STATEMENT(S) | Discovery — all witness statements | Summarize each statement: who said what, when, to whom. Note inconsistencies between statements. |
| POLICE REPORT | Discovery — incident/supplemental reports | Summarize key facts. Note responding officers, dispatch time, arrival time. |
| DEFENSE(S) | Attorney notes / Criminal Defense Cover / Initial Case Profile | If no attorney notes exist, note potential defenses visible from discovery but mark as "Preliminary — attorney review required" |
| POSSIBLE DEFENSE WITNESS(ES) | Attorney notes / Case analysis | List anyone who could support defense theory. Include alibi witnesses, character witnesses, experts. |
| STATEMENT(S) BY DEFENDANT | Client statements in discovery | Include: name/rank of person taking statement, Miranda status, summary of substance. Flag voluntariness issues. |
| SHOULD A MOTION TO SUPPRESS BE FILED? / WHY? | Analysis of client statement + search/seizure facts | Flag if: Miranda issues, warrantless search, coerced confession, illegal stop. |

### Motions Section

| Field | Source | Notes |
|-------|--------|-------|
| DISCOVERY; date filed | Case folder — filed motions | Date the discovery motion was filed |
| BILL OF PARTICULARS; date filed | Filed motions | Date filed |
| SUPPRESSION(s) | Analysis of constitutional issues | Describe basis for each suppression motion |
| IN LIMINE | Case analysis | Motions to exclude evidence |
| REVEAL THE DEAL | Discovery — informant/cooperator info | Any deals between State and witnesses |
| BOND REDUCTION | Filed motions / Bond docs | Date filed, original amount, amount after hearing |
| SPEEDY TRIAL | Case timeline | Note any speedy trial issues |
| Other Motions | All filed motions in case folder | List with dates filed |
| PRESCRIPTION | Statute of limitations analysis | Note prescription period and whether it's an issue |
| Does Defendant want to testify? | Attorney notes | Leave blank — attorney decision |

### Investigation Section

| Field | Source | Notes |
|-------|--------|-------|
| INVESTIGATOR ASSIGNED | Investigator request form | Name of assigned investigator |
| INVESTIGATOR REQUEST FORM COMPLETED ON | Investigator request form | Date form was completed |
| INVESTIGATION REQUESTED BY ATTORNEY | Investigator request form | Attorney name |
| RESULTS OF INVESTIGATION | Investigator reports | Summarize findings |

### Discovery Section

| Field | Source | Notes |
|-------|--------|-------|
| DATE FILED | Discovery motion | Date discovery was filed |
| DATE RECEIVED | Download log / Discovery cover letter | Date discovery was received from State |
| Police Reports | Discovery inventory | Note if any are missing |
| Video(s) | Discovery inventory | Note if viewable, date first viewed |
| Photo(s) | Discovery inventory | Note if clear, date first viewed |
| Lab(s) | Lab reports in discovery | Note which labs for which parties |
| Other Forensic(s) | Discovery inventory | DNA, ballistics, digital forensics, etc. |
| Witness Statement(s) | Discovery | Date first reviewed by attorney |
| Client Statement(s) | Discovery | Miranda advised? Invoked? Voluntary? Reid technique? Confession? Credible? Against interest? |
| Co-Defendant(s)' Statement(s) | Discovery | Summarize |
| HIPAA | Medical records releases | Date signed, requested, received |
| School Record(s) | School records / IEP | Date requested, IEP status |

## Homicide-Specific Fields

These fields appear ONLY in the Homicide Review Sheet:

| Field | Source | Notes |
|-------|--------|-------|
| ALLEGED VICTIM(S) — asterisk deceased | Police Report / Autopsy / Death Certificate | Place * by name of deceased victims |
| Autopsy | Autopsy report in discovery | Performed by [ME name], date first read by attorney |

## Sex Offense-Specific Fields

These fields appear ONLY in the Sex Offense Review Sheet:

| Field | Source | Notes |
|-------|--------|-------|
| ALLEGED VICTIM(S) — ages & birth dates | Police Report / CAC interview / Indictment | Include ages and DOBs for all alleged victims |
| SANE Exam | SANE/PERK records in discovery | Performed by [examiner], date first read |
| CAC Video | Children's Advocacy Center interview video | Is it viewable? Date first viewed |
| Labs — "Accuser" column | Lab reports | Instead of "Deceased" (homicide), sex offense uses "Accuser" |

## Determining Case Type

Use this decision tree to determine which template to use:

1. **Check the charges:**
   - Murder (14:30, 14:30.1), Manslaughter (14:31), Negligent Homicide (14:32) → **HOMICIDE**
   - Rape (14:42, 14:42.1, 14:43, 14:43.1), Sexual Battery (14:43.1), Molestation (14:81.2), Indecent Behavior (14:81) → **SEX OFFENSE**

2. **Check the case folder name:** Look for keywords "Murder," "Homicide," "Rape," "Sex"

3. **Check discovery contents:** Presence of autopsy report → likely homicide. Presence of SANE/CAC → likely sex offense.

4. **If both charges exist:** Generate BOTH sheets. This can happen with felony murder involving sexual assault.

5. **If unclear:** Ask the attorney which template to use.
