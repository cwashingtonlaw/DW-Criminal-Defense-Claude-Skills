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

- **Part 1 — Case Profile** (ten sections). Populate for **every** case.
- **Part 2 — Case-Type Specific Review Sheet.** Populate **exactly one** of Part 2A, 2B, or 2C based on the charges:
  - **Part 2A — LWOP Homicide** — for cases with LWOP exposure on a homicide charge (La. R.S. 14:30, 14:30.1). Submit to the District Defender per Calcasieu PDO requirements.
  - **Part 2B — LWOP Sex Offense** — for cases with LWOP exposure on a sex offense charge (La. R.S. 14:42, 14:42.1, 14:43, 14:43.1, 14:81.2). Submit to the District Defender 30 days after appointment and every consecutive 30 days.
  - **Part 2C — Other Felony** — for non-LWOP felony cases. No District Defender submission requirement.

If the case carries both homicide and sex offense LWOP exposure, populate both Part 2A and Part 2B.

---

## Operating Modes

Step 3 has two operating modes. Pick the right one before starting.

**Initial Generation Mode** — runs as part of Phase 1 intake when no `000 - Case Profile.docx` exists yet on the case file. Populates the entire document end-to-end.

**Refresh Mode** — runs when `000 - Case Profile.docx` already exists and new discovery, new court appearances, new plea offers, or other new artifacts have arrived. Updates fields from the new artifacts only. **Never** overwrites attorney-entered content. **Never** re-touches Part 1 sections 1–10 wholesale unless the attorney explicitly says "rebuild the Case Profile." Refresh Mode appends rows to multi-row tables (Court Appearance Log, Plea Discussions Log, Arraignment History, Family/Friends Contact List, Key Dates, High Priority Next Steps) when genuinely new data arrives, and updates the **Next Court Date** highlighted cell at the top of § 1 from the courtroom calendar.

Triggers for Refresh Mode:
- "Update the LWOP review"
- "Refresh the Case Profile"
- "New discovery came in — update Part 2A"
- "Re-pull the LWOP fields"
- "New court date — update the cover"
- "Log the plea offer"
- "Log today's court appearance"
- The case folder already contains `000 - Case Profile.docx` AND new discovery / minute entries / plea correspondence / appearance entries have been added since its last modification

Initial Generation Mode is the default. If unclear which mode applies, ask the attorney.

---

## Part 1 — Case Profile (always completed)

Part 1 contains ten sections. Sections marked **[NEW v5.8]** were added to capture fields that previously lived only on the firm's legacy Criminal Defense Cover Sheet; they are now native to the Case Profile and obviate the need for any separate cover artifact.

**Section 1 — Case Identification**

***Case Classification*** **[NEW v5.8]**
A four-checkbox row at the very top of § 1: ☐ MISDEMEANOR ☐ FELONY ☐ STATE ☐ FEDERAL. Quick visual triage cue for the attorney and for staff routing.

**Sourcing:** Bill of Information / Indictment header (state vs. federal forum); statute classification (felony vs. misdemeanor under La. R.S. 14:2 / Title 14 / Title 40); for dual state-federal exposure (e.g., 922(g) stacked on R.S. 14:95.1), mark both STATE and FEDERAL and add a Section 1 note flagging the dual prosecution.

***Next Court Date*** **[NEW v5.8]**
A single highlighted row (yellow label, soft-red value cell) immediately below Case Classification. This is the *current* next court date — the attorney's at-a-glance answer to "when is this case back in court?" Refresh Mode updates this cell every time a new appearance is set or rescheduled. The full forward-looking procedural calendar still lives in § 10 Key Dates; the Next Court Date row is a pointer to whichever § 10 row is closest to today.

**Sourcing:** Court minute entries, scheduling orders, JusticeWorks portal, Google Calendar entry for the case, or attorney/staff verbal update. Format as `MM-DD-YYYY @ HH:MM — [Appearance Type] — [Courtroom/Division]`.

***Defendant***
- Name | DOB | Place of Birth | Race/Sex | Physical Description
- SS# | Immigration Status
- Address | Phone | Email

**Sourcing for the Defendant fields:** Place of Birth and Race/Sex → booking record or NCIC / RAP sheet. Physical Description → booking record or incident report narrative (height, weight, build, distinguishing marks, tattoos, scars). Immigration Status → client interview, jail intake screening sheet, or any ICE detainer or A-file reference in discovery. If the client is a non-citizen, flag the case for collateral-consequences review and route plea analysis to **dw-plea-negotiation-analyzer-crim** with the immigration impact noted.

***Complaining Witness / Victim*** *(if applicable; if multiple complainants/victims, list each)*
- Name | DOB | Race/Sex | Address

***Court & Case Numbers***
- Docket # | Docket # (Companion / Related) **[NEW v5.8]** | Bill / Indictment Date **[NEW v5.8]**
- Court | Division | Judge
- Date of Offense | Date of Arrest | Date of Hire
- Co-Defendant(s) (if any)

**Sourcing for Bill/Indictment Date:** date stamp on the Bill of Information or grand jury Indictment as filed. Distinct from Date of Arrest (which can precede the bill by weeks or months). Companion / Related docket numbers capture severed counts, parallel magistrate-court dockets, related civil proceedings (protective orders, custody actions), or co-defendant dockets — anything the attorney needs to cross-reference for conflict, discovery, or scheduling.

***Investigative / Prosecution Personnel***
- Case Detective
- Assisting Detective
- First Responder
- Evidence Collection
- SANE Nurse
- Victim Advocate
- Interpreter
- Crime Lab Analyst
- Issuing Judge (warrants)
- Prosecuting ADA

**Sourcing for the Personnel block:** Case Detective / Assisting Detective → police report header. First Responder → first-on-scene officer in the incident report or CAD log. Evidence Collection → crime scene log or evidence custodian sheet. SANE Nurse → SANE exam report (sex offense cases). Victim Advocate → DA's office victim services correspondence. Interpreter → recorded interview transcripts or court minutes. Crime Lab Analyst → lab report signature block. Issuing Judge → search and arrest warrant signature lines. Prosecuting ADA → bill of information or indictment.

***Seized Property / Devices***

Table of every phone, tablet, computer, hard drive, USB device, vehicle, weapon, document, currency, or other item taken from the client, the scene, or any co-defendant at arrest or by warrant. Capture as a table:

| Item | Owner | Seized From | Date Seized | Warrant # / Bate | Extraction Status | Notes |
|---|---|---|---|---|---|---|

- **Item:** type + make/model + identifier (e.g., "iPhone 14 Pro, IMEI 35xxxxxx," "Samsung Galaxy S22, IMEI 35xxxxxx," ".380 ACP pistol, S/N xxxxx," "2018 Honda Civic, VIN xxxxxxxx").
- **Owner:** Client | Co-Defendant | Witness | Unknown.
- **Seized From:** location and circumstances (e.g., "from client's person at arrest," "from vehicle, consent search," "from residence per warrant").
- **Date Seized:** MM-DD-YYYY.
- **Warrant # / Bate:** warrant docket number if seized by warrant; Bate stamp of the seizure inventory, property receipt, or consent form.
- **Extraction Status:** for digital devices — Not Extracted | In Progress | Complete + Bate of extraction report. Drives routing to **dw-mobile-forensic-auditor-crim** (methodology audit) and **dw-forensic-dump-analyzer-crim** (content review).
- **Notes:** chain-of-custody anomalies, passcode/password status, devices listed in police narrative but not in the property receipt, attorney flags.

**Suppression trigger:** any device or item that appears in discovery without a corresponding warrant, consent record, or arrest-incident inventory entry → flag in red and route to **dw-suppression-motion-crim**.

**Cowork populates** Case Classification (best inference from charges; attorney confirms), Defendant identifying fields, Complaining Witness / Victim identifying fields, Court & Case Numbers (including Bill/Indictment Date and any Companion Docket #), the Investigative / Prosecution Personnel block, and the Seized Property / Devices table from charging instruments, police reports, search and arrest warrants, property receipts and evidence inventories, lab reports, SANE reports, and court filings where available. **Staff/Attorney completes** remaining demographic fields after client and family interviews. Next Court Date is updated by Cowork on every Refresh from court minutes / scheduling orders. If the complaining witness is a minor, redact identifying details in any externally distributed copy.

---

**Section 2 — Probation/Parole Status** **[NEW v5.8]**

Populate **only** if the client is currently on probation, parole, drug court, diversion, or any form of court supervision (state or federal) at the time of the new arrest. A probation/parole hold can override bond reduction and is often the gating issue for pretrial release; failure to capture this on intake is the single most common cause of an unwinnable bond hearing.

Twelve fields in a 2-column label/value table:
- On Probation or Parole? (Y/N)
- Type (Probation / Parole / Drug Court / Diversion / Other)
- Parole / Probation Officer
- Officer Phone / Email
- Supervising Court / Parish
- Underlying Conviction / Docket #
- Supervision Start Date
- Supervision Expiration Date
- Sentence Eligibility / Time Remaining
- Detainer / Hold Active? (Y/N — flag in red if Y)
- Special Conditions (drug testing, GPS, no-contact, curfew)
- Notes / Revocation Exposure `[ATTORNEY]`

**Sourcing:** Client interview, NCIC / RAP sheet, prior PSI, parole certificate or supervision agreement, P/P officer direct contact, or jail intake screening (which often surfaces an active detainer). Federal supervision data lives on the federal PACER docket; state supervision data is usually accessible through the DOC inmate locator or by direct call to the supervising officer.

**Routing:** Active detainer → **dw-bond-and-release-motion-crim** with the revocation-versus-new-charge sequencing strategy noted. Pending revocation hearing → flag in § 10 High Priority Next Steps. If the new charges are likely to trigger revocation regardless of disposition, route plea analysis to **dw-plea-negotiation-analyzer-crim** so the global-resolution math is correct.

If the client is **not** on supervision, mark the first row "N" and leave the rest blank. Do not delete the section.

---

**Section 3 — Charges & Exposure**

***Charges (per count)***

Six-column table — one row per count:

| Count | La. Statute | Max Penalty | Mandatory Min | Elements | Responsive Verdicts |
|---|---|---|---|---|---|

- **Count:** sequential numbering matching the Bill of Information / Indictment (1, 2, 3, …).
- **La. Statute:** full citation with subsection and grade as written (e.g., "14:30.1", "14:42(A)(4)", "40:967(B)(4)(b)").
- **Max Penalty:** statutory maximum exposure (e.g., "Life w/o parole", "0–30 yrs at hard labor", "0–10 yrs"). Note any firearm / drug-free-zone / hate-crime sentence enhancements applicable to this count in the same cell so per-count exposure is calculable on its face.
- **Mandatory Min:** mandatory minimum, if any (e.g., "Life w/o benefits", "10 yrs at hard labor w/o parole, probation, or suspension"). State "None" explicitly when there is no minimum — blank reads as unchecked.
- **Elements:** numbered list of statutory elements the State must prove (one element per line within the cell). Pull from the statute text, the pattern jury instruction, or the charging instrument.
- **Responsive Verdicts:** enumerated verdicts per La. C.Cr.P. art. 814 where the charge is listed there; otherwise note "Art. 815 (lesser & necessarily included)" and identify the included offenses the defense intends to argue. Cross-reference the firm's `Art 814 Responsive Verdicts` document.

***Habitual Offender Exposure*** *(populate only when a habitual bill is filed, threatened, or anticipated; otherwise leave blank)*

Cross-cutting analysis under La. R.S. 15:529.1. Capture in a single narrative cell:
- Predicate convictions (date / parish / docket / disposition / cleansing-period status)
- Enhancement multiplier per affected count (2nd / 3rd / 4th felony) or sentence floor
- Cleansing-period challenges (whether the look-back has run on any predicate)
- Boykin / R.S. 15:530.7 challenges to predicate validity
- Strategic question: motion to quash the habitual bill, negotiate a non-habitual cap, or accept

Route to **dw-habitual-offender-auditor-crim** for the full audit.

---

**Section 4 — Arraignment & Bail History**

***Arraignment History*** **[EXPANDED v5.8]** *(one row per arraignment or re-arraignment)*

Six-column multi-row table — captures every arraignment proceeding. The initial arraignment is row 1; any re-arraignment after an amended bill, a superseding indictment, or a habitual offender bill arraignment is a new row.

| Date | Charges Read | Prosecutor | Judge | Plea Entered | Notes |
|---|---|---|---|---|---|

***Bail / Bond***

Seven-field label/value table — the State of the Bail. Distinct from § 5 Court Appearance Log, which captures every appearance; this block captures only the bail/bond posture and its modifications.

- Bail Status (ROR / REMAND / BAIL SET / EXAM ORDERED)
- Bond Amount — Total
- Bond Type (Commercial Surety / Cash / Property / Personal Recognizance)
- Cash Bond Amount (if posted) **[NEW v5.8]** — the actual cash posted, distinct from total bond. Material when source-of-funds disputes arise (R.S. 15:85.1) or when refundability of bond is at issue.
- Bail Set / Hearing Date
- Conditions of Release (GPS, no-contact, drug testing, curfew, travel restrictions)
- Bail Notes (history of bond hearings, modifications, source-of-funds disputes) **[NEW v5.8]**

**Sourcing:** Bond order, court minute entries, surety affidavit, bond receipt, conditions-of-release form. The "Bail Notes" cell is the free-text history of every bail modification — Cowork populates the chronology; attorney annotates strategy.

**Populate from court filings when available; leave blank fields for attorney completion.**

---

**Section 5 — Court Appearance Log** **[NEW v5.8]**

Backward-looking chronological record of every court appearance after the initial arraignment — status conferences, motion hearings, pre-trial conferences, calendar calls. **Distinct from § 10 Key Dates**, which is forward-looking statutory deadlines and upcoming procedural milestones. This section answers "what's happened so far"; § 10 answers "what's coming."

Six-column multi-row table:

| Date | Appearance Type | ADA | Judge | Bail Status | Notes / Rulings |
|---|---|---|---|---|---|

- **Date:** MM-DD-YYYY.
- **Appearance Type:** Status / Motion Hearing / Pretrial Conference / Calendar Call / Continuance / Rule to Show Cause / Other.
- **ADA:** name of prosecutor who appeared (often differs from the Prosecuting ADA of record).
- **Judge:** name of judge who took the bench (often a duty judge differing from the assigned judge).
- **Bail Status:** ROR / REMAND / Bond Continued at $X / Bond Modified to $X. Captures any change to bail at that appearance.
- **Notes / Rulings:** rulings made, continuances granted (and to what date), motions ore tenus, what was discussed off-the-record at sidebar, any preservation-of-error issues — route preservation issues to **dw-appellate-error-monitor-crim**.

**Sourcing:** court minute entries, attorney post-court notes (Plaud recordings, Apple Notes session bookends in Case Brain), staff intake from clerk's office.

**Refresh Mode:** append-only — never modify existing rows. New appearances become new rows in chronological order. Update Next Court Date in § 1 from the most recent appearance's continuance ruling.

---

**Section 6 — Case-Specific Defenses** *(Repeat for each defense)*

Review all available case file materials — arrest reports, police narratives, witness statements, evidence logs, bodycam summaries, transcripts, and any other intake documents. Identify defenses grounded in what the case file actually contains. This is not a list of generic defenses.

For each potential defense, include:
- The defense theory
- The specific evidence or document supporting it (with Bate stamp reference)
- Constitutional issues flagged (unlawful stop, Miranda violations, warrant defects)
- Factual weaknesses in the State's case (inconsistent accounts, evidence gaps, timeline conflicts)
- Affirmative defenses supported by the facts
- Recommendation for attorney investigation

---

**Section 7 — Client Background** *(Attorney completes after client interview)*
- Prior Criminal History
  - **Format guidance for LWOP cases (Part 2A or 2B applies):** Use structured list `MM-DD-YYYY — Offense Name (Disposition)`, one prior per line. The District Defender expects rap-sheet-style summaries on submitted forms. Pull from the client's NCIC printout / RAP sheet. Include dispositions where available.
  - **Format guidance for non-LWOP cases:** Narrative form is acceptable.
- Family / Home Life
- Educational History
- Employment History
- Medical / Mental Health
- Substance Abuse History **[NEW v5.8]** — separated from Medical/Mental Health because it drives different doctrine (R.S. 13:5304 drug court eligibility, federal safety-valve under 18 U.S.C. § 3553(f), and several mitigation pathways). Capture history of use, history of treatment (inpatient/outpatient/Medication-Assisted Treatment), current sobriety status, any substance-related prior convictions.
- Military Service (if applicable)
- Other Relevant Info **[NEW v5.8]** — anything that informs case theory or mitigation that doesn't fit the named buckets above. Examples: TBI history, foster care background, victimization history, immigration status nuance (separate from § 1 Defendant field), language proficiency, learning disabilities, financial dependents, custodial obligations.

---

**Section 8 — Plea Discussions Log** **[NEW v5.8]**

Every plea offer extended by the State, every counter-offer made by the defense, and every conveyance to the client. Rule 1.4 of the Louisiana Rules of Professional Conduct requires that material decisions — including plea offers — be communicated to the client; this log is the firm's contemporaneous record of compliance. For formal trial-exposure analysis of any specific offer, route to **dw-plea-negotiation-analyzer-crim** (this log captures the existence and conveyance; the analyzer captures the math).

Six-column multi-row table:

| Date | Plea Offer / Counter | Source (ADA / Court / Email) | Conveyed to Client (Y/N + Date) | Client Response | Notes |
|---|---|---|---|---|---|

- **Date:** date the offer was made or received.
- **Plea Offer / Counter:** terms in concrete form (e.g., "Plead to Ct. 1 as charged, dismiss Cts. 2-3, joint recommendation 15 yrs DOC w/ first 5 w/o benefits"). Counter-offers in the same row when made same-day; otherwise new row.
- **Source:** named ADA + medium (email / in-chambers / on the record / phone call) + court date if on-record. Email source → save to case folder and cite the Bates or filename.
- **Conveyed to Client (Y/N + Date):** Rule 1.4 trigger. If conveyed in person at jail, note jail visit date; if by mail, note send date; if by phone, note call date. If conveyance is pending, note "Pending — set for [date]."
- **Client Response:** Accept / Reject / Counter / Take Time to Consider. Echo back specific language where consequential ("client says 'absolutely not' to any sex offender registration").
- **Notes:** strategic context (was this offered before or after the suppression ruling? before or after the State got the lab report?).

**Sourcing:** ADA emails, court minute entries reflecting in-court offers, attorney post-court notes, Plaud recordings of client jail visits, dw-case-brain-crim session entries.

**Refresh Mode:** append-only — never modify existing rows. Conveyance updates may add a new row if a conveyance occurred after the row was first created and the original row left "Conveyed = No"; otherwise the original row's Conveyance cell is updated in place (the only field allowed to be modified in Refresh Mode for this table) and a note added in the Notes cell.

---

**Section 9 — Family / Friends Contact List** **[NEW v5.8]**

The client's support network — the universe of non-client people who matter for the case. Used for sentencing mitigation, character witnesses, bond co-signers, jail visit coordination, family-status updates, and humanizing the client at trial. A potential character witness must be vetted before being committed to; a bond co-signer must be qualified before being offered to the State. This list is the working roster; vetting and qualifying happen separately.

Six-column multi-row table:

| Person | Relation | Phone / Email / Address | Role (Mitigation / Character / Bond / Support) | Vetted? | Notes |
|---|---|---|---|---|---|

- **Person:** full legal name. Nicknames go in Notes.
- **Relation:** Mother / Father / Spouse / Partner / Sibling / Aunt-Uncle / Cousin / Grandparent / Child / Coworker / Pastor / Coach / Mentor / Employer / Friend / Other.
- **Phone / Email / Address:** at least one durable contact method. Mark "Best to reach" in Notes if ambiguous.
- **Role:** primary intended role (Mitigation = sentencing letter / PSI interview / hearing testimony; Character = trial character witness; Bond = potential co-signer / property pledge; Support = jail visits, fund transfers, family liaison). Multi-role people get the highest-stakes role here and the rest in Notes.
- **Vetted?** Y / N / Pending. Vetting for Character witness means CCAP / background check + interview; for Bond means property ownership + credit verification; for Mitigation means readiness interview with attorney or investigator. **dw-defense-investigator-tasking-crim** routes the vetting work.
- **Notes:** known criminal history (disqualifies for Bond), prior cooperation with law enforcement on the client's case (disqualifies for Character), strained relationship (use carefully for Mitigation), language preferences, work-schedule constraints on jail visits.

**Sourcing:** client interview (Section 7 prompts cover most of this — Cowork pre-populates from any names the client has volunteered in earlier sessions or in jail-call transcripts), jail intake visitor list, social-media public connections (LinkedIn / Facebook public profile — never DM-based outreach), Plaud recordings.

**Privacy note:** This list is attorney work product. Never share externally without the named person's consent. Redact when producing the Case Profile to anyone outside the firm.

**Refresh Mode:** append-only. New names become new rows. Vetting status updates in place.

---

**Section 10 — Key Dates & Next Steps**

***Key Dates***

The attorney's at-a-glance procedural calendar — court dates, statutory deadlines, motion filing deadlines, and other procedural milestones. Capture as a three-column table:

| Date | Event Description | Source |
|---|---|---|

**Boundary with `Case Tables.xlsx — Timeline Sheet`:** § 10 Key Dates holds *procedural* milestones — the courtroom calendar the attorney works off of. The Timeline Sheet, populated in Phase 3 Step 1 from the 8 case analysis reports, holds the comprehensive *evidentiary* timeline (every event, every source, conflict-flagged). Different audiences, different lifecycles. Do not sync the two; keep them deliberately separate.

**Boundary with § 5 Court Appearance Log:** § 5 is backward-looking (every appearance that has happened, with its rulings); § 10 Key Dates is forward-looking (every deadline and appearance that's coming, plus the past procedural milestones that anchor the case's calendar — date of arrest, bill filing, arraignment).

**Boundary with § 1 Next Court Date:** The Next Court Date row in § 1 is a single highlighted cell pointing at whichever § 10 Key Dates row is closest to today. § 10 is the system of record; § 1 is the visual cue.

Populate with both past and upcoming procedural events. Past events stay in the table — do not delete them; together they show the case's procedural posture at a glance.

Events to capture (representative, not exhaustive):
- Date of Offense
- Date of Arrest / 72-hour hearing
- Bond hearing(s)
- Bill of Information / Indictment filed
- Arraignment
- Discovery received (one row per production set)
- Discovery deadline (per court order or La. C.Cr.P. art. 728/729 statutory)
- Motion filing deadlines
- Motion hearings (one row per hearing)
- Pretrial conference
- Trial date (and any continuances — keep prior trial dates as separate rows)
- Speedy trial demand date / La. C.Cr.P. art. 701 release date
- Statute of limitations expiration (La. C.Cr.P. art. 571–576 as applicable)
- Habitual offender bill filing deadline (if applicable)

Source examples for the third column: Bill of Information, court minute entry [date], scheduling order, Google Calendar, discovery transmittal letter, motion order, statutory calculation.

Sort chronologically. Where a date is calculated rather than documented (e.g., Art. 701 release date), state the calculation in the Source cell.

***High Priority Next Steps***

Cowork-prepopulated, attorney-finalized list of the highest-priority case actions that should happen next. Generate from available Phase 1 and Phase 2 outputs and from the current case posture. Each row of the table:

| Step | Why High Priority | Owner | Routing | Target Date | Status |
|---|---|---|---|---|---|

- **Step:** what to do, in plain action language.
- **Why High Priority:** the deadline, statutory clock, evidentiary risk, or strategic value driving urgency (e.g., "Art. 701 clock runs in 28 days," "scene canvass before businesses overwrite surveillance," "preserve suppression argument for warrantless phone search," "client in custody — bond reduction").
- **Owner:** Attorney | Investigator | Cowork | Staff.
- **Routing:** specialist skill or workflow when applicable (e.g., **dw-suppression-motion-crim**, **dw-bond-and-release-motion-crim**, **dw-pretrial-motion-library-crim**, **dw-defense-investigator-tasking-crim**, **dw-mobile-forensic-auditor-crim**).
- **Target Date:** when the step needs to be done.
- **Status:** Open | In-Progress | Done. New rows default to Open. Update as work progresses. Done rows stay in the table — they are the audit trail of completed actions, not deletions. The table is the system of record; nothing leaves it.

Common high-priority steps Cowork should consider:
- File written discovery demand and Brady/Giglio request → **dw-pretrial-motion-library-crim**
- File motion to suppress (any item flagged in § 1 Seized Property without warrant/consent, or any Phase 2 Report 3 red flag) → **dw-suppression-motion-crim**
- File bond reduction (if client in custody) → **dw-bond-and-release-motion-crim**
- File Art. 701 motion for release on lack of indictment / lack of trial → **dw-pretrial-motion-library-crim**
- File bill of particulars and motion to quash issues → **dw-pretrial-motion-library-crim**
- Send investigator on early scene visit, business canvass, witness locate → **dw-defense-investigator-tasking-crim**
- Vet § 9 contact-list names for Bond / Character / Mitigation roles → **dw-defense-investigator-tasking-crim**
- Retain experts (SANE, child psych, mobile forensics, ballistics) — name the expert(s) needed and the issue
- Complete full client interview to populate § 7 Background and § 9 Family/Friends list
- Order missing records (school, IEP, medical, mental health, military, employment)
- Subpoena third-party records (phone subscriber records, surveillance footage, GPS/CSLI, EMS run reports)
- Forensic extraction review on any device with Extraction Status = Complete → **dw-forensic-dump-analyzer-crim**
- If § 2 Probation/Parole shows active supervision: confirm detainer status and sequence revocation hearing strategy → **dw-bond-and-release-motion-crim** + **dw-plea-negotiation-analyzer-crim**

Rank each step **High / Medium / Low** by the combination of deadline urgency and strategic impact. Cowork proposes the ranking; **attorney finalizes**. The combination of Status + Target Date gives the attorney a single-glance view of what's open, what's in flight, what's overdue, and what's been completed — without rows ever leaving the table.

---

## Part 2 — Case-Type Specific Review Sheet

Populate exactly one of Part 2A, 2B, or 2C. None of these fields duplicate Part 1 — they capture only the case-development detail required for that case type.

**Common to 2A / 2B / 2C** (every case-type branch contains these nine sections):
1. **Key Dates (LWOP/case-specific):** Age at Time of Offense | Discovery Filed (date) | Discovery Received (date) | Trial Date
2. **Co-Defendant Details:** Separately Charged? | Plea Status | Cooperating with State?
3. **Case Specifics** — *differs per case type, see lwop-field-maps.md*
4. **Defendant Statement:** substance + voluntariness flags
5. **Suppression Analysis:** Miranda advised/invoked, Voluntary, Reid technique, Confession, Statements credible, Against client's interest, Suppression motion Y/N + Why + basis
6. **Motions:** Discovery, Bill of Particulars, Suppression(s), In Limine, Reveal the Deal, Bond Reduction (filed?, date filed, original amount, post-hearing amount), Speedy Trial, Other Motions, Reports Checklist, Prescription, Defendant testify? [ATTORNEY]
7. **Investigation:** Investigator Assigned | Request Form Completed On | Requested by Attorney | Results
8. **Evidence Inventory** — *differs per case type, see lwop-field-maps.md*
9. **Records & Authorizations:** HIPAA Y/N, Date Signed, Date Requested, Date Received, School Records, IEP, Date Records Requested, Date IEP Requested

(See `lwop-field-maps.md` for full Part 2A / 2B field schemas and `lwop-extraction-patterns.md` for sourcing rules per field. Part 2 was untouched by the v5.8 changes.)

---

## Refresh Mode — Detailed Merge Rules

Refresh Mode runs when new evidence or events arrive after the Case Profile is already built. The merge logic differs by table type.

**For label/value tables (most of Part 1 § 1, § 2, § 4 Bail/Bond, § 7 Client Background, and all of Part 2):**

1. Find the existing field by its label.
2. Apply updates field-by-field using these merge rules:

| Existing cell state | Action |
|---|---|
| Blank | Populate from new source |
| Cowork-extracted black-text content | Update if newer source contradicts; preserve if newer source is silent |
| Black-text content matching attorney handwriting / additions | **Do not touch** unless attorney explicitly says "re-pull everything" |
| Red `[ATTORNEY]` placeholder | **Never touch** |
| Red attorney-flagged content | **Never touch** |

3. Update the **Next Court Date** highlighted cell in § 1 from the most recent court minute or scheduling order — this is the **one** § 1 field Cowork actively refreshes on every run.

**For multi-row data tables (§ 1 Seized Property, § 4 Arraignment History, § 5 Court Appearance Log, § 8 Plea Discussions Log, § 9 Family/Friends Contact List, § 10 Key Dates, § 10 High Priority Next Steps):**

Append-only. Existing rows are never modified or deleted. New data becomes new rows. Two narrow exceptions:
- § 8 Plea Discussions Log "Conveyed to Client" cell may be updated in place when conveyance happens after the row was first created.
- § 10 High Priority Next Steps "Status" cell updates in place from Open → In-Progress → Done as work progresses.

**Append a Refresh Log entry** at the bottom of the document (under Part 2 Section 9 — Records & Authorizations, or at the end of Part 1 § 10 if Part 2 is not yet populated):
```
REFRESH LOG — [YYYY-MM-DD]
New sources processed: [list Bates ranges, minute-entry dates, email senders, file names]
Fields updated: [list field names — usually Next Court Date and any label/value updates]
Rows appended: [Court Appearance Log: N rows | Plea Discussions Log: N rows | etc.]
Attorney-only fields preserved: [list field names left untouched]
Conflicts flagged for attorney review (red text added in fields): [list field names]
```

Then run the field-completeness checklist as in Initial Generation Mode and save as `000 - Case Profile.docx` (same filename — overwrite the existing file).

**Save the output for both modes** to:
`Pretrial Notebook → 03 - Case Analysis & Notes/000 - Case Profile.docx`

---

## Generation Procedure (XML Edit)

Read the docx skill (at the path listed in your available skills) for the full unpack/edit/repack procedure. Then follow Steps 1–5 below. The XML to edit is always `working/unpacked/word/document.xml`.

### Step 1 — Copy and unpack

```bash
# Initial Generation Mode
cp "<skill>/assets/CASE PROFILE.docx" "<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/000 - Case Profile.docx"

# Refresh Mode: skip the cp and read the existing file in place
python <docx-skill-path>/scripts/office/unpack.py "<output-path>" working/unpacked/
```

### Step 2A — Label/Value Tables (existing pattern)

For every field that lives in a 2-column label/value table — **Defendant**, **Complaining Witness / Victim**, **Court & Case Numbers**, **Investigative / Prosecution Personnel**, all of § 2 Probation/Parole Status, § 4 Bail/Bond, § 6 Defenses, § 7 Client Background, and all of Part 2A/2B/2C's section fields — use the label-find-and-fill pattern:

1. Find the cell containing the label text (e.g., `<w:t>Place of Birth</w:t>`)
2. Locate the adjacent right-side cell in the same `<w:tr>` (the empty data cell, which contains a single `<w:p/>`)
3. Replace that cell's `<w:p/>` with a paragraph containing the value:

```xml
<w:p>
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
      <w:sz w:val="22"/>
    </w:rPr>
    <w:t xml:space="preserve">VALUE</w:t>
  </w:r>
</w:p>
```

For multi-line content, repeat the `<w:p>...</w:p>` block once per line within the same cell. Preserve all `<w:tcPr>` (width, shading) and the cell's outer `<w:tc>...</w:tc>` boundary unchanged.

### Step 2B — Multi-Row Data Tables (added in v5.5, expanded in v5.8)

Seven Part 1 tables have a header row followed by empty starter rows; each starter row holds one record:

| Table | Sub-header anchor text | Columns | Starter rows |
|---|---|---|---|
| Seized Property / Devices | `Seized Property / Devices` | 7 — Item, Owner, Seized From, Date Seized, Warrant # / Bate, Extraction Status, Notes | 6 |
| Arraignment History **[NEW v5.8]** | `Arraignment History (one row per arraignment or re-arraignment)` | 6 — Date, Charges Read, Prosecutor, Judge, Plea Entered, Notes | 4 |
| Court Appearance Log **[NEW v5.8]** | (table directly under `Section 5 — Court Appearance Log` banner) | 6 — Date, Appearance Type, ADA, Judge, Bail Status, Notes / Rulings | 8 |
| Plea Discussions Log **[NEW v5.8]** | (table directly under `Section 8 — Plea Discussions Log` banner) | 6 — Date, Plea Offer / Counter, Source, Conveyed to Client (Y/N + Date), Client Response, Notes | 6 |
| Family / Friends Contact List **[NEW v5.8]** | (table directly under `Section 9 — Family / Friends Contact List` banner) | 6 — Person, Relation, Phone / Email / Address, Role, Vetted?, Notes | 10 |
| Key Dates | `Key Dates` | 3 — Date, Event Description, Source | 10 |
| High Priority Next Steps | `High Priority Next Steps` | 6 — Step, Why High Priority, Owner, Routing, Target Date, Status | 8 |

There is also one **single-row visual block** in § 1 that follows neither the label/value nor the multi-row pattern:

| Block | Anchor text | Cells | Notes |
|---|---|---|---|
| Case Classification | `Case Classification` | 4 (checkbox row) | Edit by checking ☒ next to the correct cell(s); leave the others as ☐. Multi-check allowed for State+Federal dual exposure. |
| Next Court Date | `Next Court Date` / `NEXT COURT DATE` | 2 (yellow label, soft-red value) | Single-row K/V. The value cell is the only field actively refreshed on every Refresh Mode run. |

**Locate the target table:**

1. Find the sub-header paragraph by its exact text (e.g., `<w:t>Seized Property / Devices</w:t>`), or the section header banner for tables that sit directly under their section header (Court Appearance Log, Plea Discussions Log, Family/Friends Contact List).
2. Walk forward to the next `<w:tbl>` opening. That is the target table.
3. The first `<w:tr>` is the bold-centered header row — **never modify it**.
4. The remaining `<w:tr>` blocks are empty starter rows. Each cell's content is just `<w:p/>`; the surrounding `<w:tcPr>` carries width, borders, and white shading.

**Fill an empty starter row** (preferred path while data ≤ starter count):

For each starter row you fill, replace each of its cells' `<w:p/>` with the paragraph block from Step 2A, using that cell's column value. Do not touch `<w:tcPr>` — column widths, borders, and shading must remain intact. Move column-by-column left to right; leave a cell as `<w:p/>` if the value is unknown.

**Append additional rows** (overflow path when data exceeds starter count):

1. Locate the last `<w:tr>` in the table (the final empty starter).
2. Duplicate that entire `<w:tr>...</w:tr>` block, including every `<w:tc>` child with its `<w:tcPr>`.
3. Insert the duplicate immediately before the table's `</w:tbl>` closing tag.
4. Fill the duplicated cells using the empty-row fill pattern above.
5. Repeat for each additional record.

This preserves column widths and the cell-border block automatically, since you are cloning known-good XML.

**Refresh Mode rule for these tables:** append-only. Never modify or remove existing rows except in the two narrow cases documented above (§ 8 "Conveyed to Client" cell, § 10 High Priority "Status" cell).

### Step 3 — Apply red font for attorney-only and flagged content

For every field marked `[ATTORNEY]` and any Cowork-flagged conflict text, add red color to the run properties:

```xml
<w:rPr>
  <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
  <w:color w:val="FF0000"/>
  <w:sz w:val="22"/>
</w:rPr>
```

For sub-block sub-headers and instruction notes already in the template (rendered in `C62828` red), preserve them as-is — they are part of the template, not content.

### Step 4 — Part 2 branch selection

Keep the active Part 2A / 2B / 2C branch; remove or leave blank the inactive branches per attorney instruction.

### Step 5 — Repack and validate

```bash
python <docx-skill-path>/scripts/office/pack.py working/unpacked/ "<output-path>" --original "<skill>/assets/CASE PROFILE.docx"
python <docx-skill-path>/scripts/office/validate.py "<output-path>"
```

For Refresh Mode, the merge rules from the Refresh Mode subsection above apply to Step 2A cell content. Step 2B uses the append-only rule stated above.

---

## Step 3 Quality Check

- [ ] `assets/CASE PROFILE.docx` copied into `Pretrial Notebook → 03 - Case Analysis & Notes` as `000 - Case Profile.docx` (Initial Generation Mode) OR existing file read in full (Refresh Mode)
- [ ] § 1 Case Classification checkbox marked (Misd / Felony / State / Federal)
- [ ] § 1 Next Court Date populated (or marked "TBD — awaiting scheduling order")
- [ ] § 1 Court & Case Numbers includes Bill/Indictment Date and any Companion / Related dockets
- [ ] § 2 Probation/Parole Status populated (or first-row "N" if client not on supervision)
- [ ] Part 1 § 1–§ 10 populated from available sources (Initial Generation only)
- [ ] § 4 Arraignment History row 1 captures initial arraignment; § 4 Bail/Bond block includes Cash Bond and Bail Notes
- [ ] § 5 Court Appearance Log seeded with any post-arraignment appearances already in the file
- [ ] § 7 Client Background includes Substance Abuse History and Other Relevant Info rows (blank is acceptable; the rows must exist)
- [ ] § 8 Plea Discussions Log seeded if any plea offers have already been made
- [ ] § 9 Family/Friends Contact List seeded with any names volunteered in client interviews to date
- [ ] § 10 Key Dates and § 10 High Priority Next Steps populated; Next Court Date in § 1 reconciled with the closest § 10 row
- [ ] Exactly one of Part 2A, 2B, or 2C selected based on charges; the other two parts left blank or removed
- [ ] If LWOP exposure is present (Part 2A or 2B): every field listed in `lwop-field-maps.md` for that branch is present in the output (field-completeness checklist run)
- [ ] All `[ATTORNEY]` fields preserved in red for attorney completion
- [ ] In Refresh Mode: all attorney-entered content preserved untouched; Refresh Log entry appended
- [ ] Completion notes generated (fields populated, fields blank with reasons, conflicts, missing discovery, suppression flags, probation/parole hold flags)
