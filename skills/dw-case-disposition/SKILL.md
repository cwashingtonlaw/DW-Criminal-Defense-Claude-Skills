---
title: D&W Case Disposition Workflow
description: Comprehensive case closing workflow for criminal case final dispositions
trigger:
  - close the case
  - case closed
  - disposition
  - case resolved
  - final disposition
  - archive the case
  - case outcome
  - wrap up the case
  - case is over
  - verdict entered
  - plea entered
  - dismissal
  - nolle prosequi
  - case closing checklist
---

# D&W Case Disposition Workflow

**Version:** 1.0  
**Last Updated:** April 2026  
**Skill Type:** Procedural Workflow Gate  
**Severity:** High (case closure is irreversible)

## Overview

When a criminal case reaches final disposition—through guilty plea, not guilty verdict, guilty verdict, hung jury/mistrial, dismissal, nolle prosequi, diversion completion, transfer, or abatement—this skill executes a comprehensive closing workflow. The workflow records the outcome in the Case Brain, generates final billing and client notification, assesses appeal and expungement eligibility, produces a closing checklist, and archives the file while maintaining strict compliance with Louisiana Rules of Professional Conduct.

**DO NOT USE FOR:**
- Active case management (use **dw-criminal-defense**)
- Session persistence and case context (use **dw-case-brain**)
- Mid-case status updates or routine motions

## STEP 0: DISPOSITION CONFIRMATION HARD STOP

**This is a mandatory gate. Do not proceed without attorney approval of all items below.**

### Required Confirmations

1. **Case Status Verification**
   - Confirm the case has actually reached final disposition
   - Not in trial preparation, not in pre-trial motions, not in plea negotiation
   - Attorney states explicitly: "Yes, this case is closed"

2. **Disposition Type Selection**
   The attorney must specify ONE of the following:
   - Guilty Plea (Art. 651, La. C.Cr.P.)
   - Not Guilty Verdict (acquittal)
   - Guilty Verdict (after trial)
   - Hung Jury / Mistrial
   - Dismissal (with or without prejudice)
   - Nolle Prosequi (prosecutor decline to prosecute, Art. 215)
   - Diversion Completion (Art. 893/894, La. C.Cr.P.)
   - Transfer to Another Court (jurisdiction change)
   - Abatement (death of defendant, Art. 215.1)

3. **Disposition Date Confirmation**
   - Attorney provides the date the disposition was entered (verdict date, plea date, dismissal order date)
   - Format: MM/DD/YYYY

4. **Sentencing Status Gate**
   - IF disposition is Guilty Plea or Guilty Verdict AND sentencing has NOT yet occurred:
     - **DO NOT FULLY CLOSE THE CASE**
     - Mark case as: "DISPOSITION ENTERED — AWAITING SENTENCING"
     - Schedule a follow-up task in Google Calendar to re-invoke this skill after sentencing
     - Save intermediate state to Case Brain
     - STOP here and return to attorney
   - IF sentencing has been imposed:
     - Confirm sentence details (see Step 1)
     - Proceed to Step 1

### Hard Stop Checklist

- [ ] Attorney confirms case has reached final disposition
- [ ] Disposition type explicitly selected from the list above
- [ ] Disposition date provided (MM/DD/YYYY)
- [ ] If guilty plea/verdict: Sentencing status confirmed (imposed or pending)
- [ ] If sentencing pending: Case marked as "Awaiting Sentencing" and follow-up scheduled

**If any item is unchecked, STOP and request missing information from attorney.**

---

## STEP 1: RECORD OUTCOME IN CASE BRAIN

Invoke **dw-case-brain** to update the permanent case record with disposition details.

### Information to Record

**Disposition Core Data:**
- Disposition Type (from Step 0)
- Disposition Date (MM/DD/YYYY)
- Judge/Magistrate Name
- Court (parish, division)

**Charge Information:**
- Final Charges (may differ from original charges if amended, dismissed, or reduced)
- Original Charges vs. Final Charges (if changed)
- Charge Status: Convicted, Acquitted, Dismissed, Nolle Prosequi'd, Diverted

**Sentencing (if applicable):**
- Prison Sentence: Years/Months/Days
- Hard Labor: Yes/No
- Suspended Sentence: Amount
- Probation/Parole: Duration and conditions
- Restitution: Amount and payee
- Fines: Amount
- Court Costs/Fees: Amount
- Sex Offender Registration Required: Yes/No (Art. 15:542, La. R.S.)
- LWOP (Life Without Parole): Yes/No
- Truth-in-Sentencing Application: Yes/No

**Key Appellate Deadlines (calculate and record):**
- **Appeal Motion Deadline:** 30 days from sentence (misdemeanor: 2 days, Art. 914)
- **Sentence Modification Deadline:** 30 days from sentence (Art. 881.1)
- **Probation Review Dates:** As applicable
- **Post-Conviction Remedy Deadlines:** Art. 930.8 (post-conviction DNA), Art. 215 (motion to recall and resentence)

**Case Brain Completion:**
- Attorney reviews all entries in Case Brain
- Confirms accuracy of disposition type, dates, and sentence details
- Approves entry to Case Brain

---

## STEP 2: FINAL BILLING

Invoke **dw-billing-narrative-generator** to capture all unbilled session work and generate a comprehensive billing summary.

### Billing Process

1. **Run dw-billing-narrative-generator**
   - Pass: All case numbers, client name, disposition date
   - Generates: Complete billing narrative for all work across entire case lifecycle
   - Captures: Any unbilled sessions, memos, phone calls, travel, research

2. **Generate Final Billing Summary**
   - Create Excel workbook with following sheets:
     - **Summary Sheet:** Total hours by LEDES category (e.g., Initial Consultation, Pretrial Motions, Trial, Sentencing)
     - **Detail Sheet:** Line-item breakdown by date, hours, description, LEDES code, amount
     - **By Phase:** Investigation, Pretrial, Trial/Plea, Sentencing, Appellate (if any)
   - Calculate total fees, costs reimbursed, outstanding balance
   - Apply any final adjustments or fee reductions per attorney direction

3. **Save Final Billing Summary**
   - **Path:** `<case-root>/05 - Billing/[ClientLastName] - Final Billing Summary - [Date].xlsx`
   - Include: Client name, case number, disposition type, disposition date, invoice date range

4. **Flag for Attorney Review**
   - Highlight any outstanding invoices or unbilled time
   - Present summary to attorney for final approval before case is archived
   - Attorney signs off on final billing before proceeding to Step 3

### Billing Summary Template Items

- Total hours (all categories)
- Total fees (per agreed rate)
- Total costs reimbursed
- Outstanding balance
- Retainer applied / refund due
- Court-appointed case rate (if applicable)
- Payment schedule or lump sum due date

---

## STEP 3: CLIENT NOTIFICATION

Invoke **dw-client-communication-drafter** to draft a case resolution letter tailored to the disposition type.

### Letter Type Selection

**A. Acquittal / Dismissal Letter**
- Opening: Congratulatory message (case successfully resolved in client's favor)
- Explanation: What acquittal/dismissal means legally
- Consequences: No conviction, no probation, no restitution obligations
- **Expungement Path:** Advise on Art. 971-986 eligibility (immediate for acquittals, per Art. 973)
- Criminal Record: Explain record now eligible for expungement
- Next Steps: Offer to pursue expungement motion (reference **dw-pretrial-motion-library**)
- Final Invoice: Attach billing summary, payment terms

**B. Guilty Plea / Guilty Verdict Letter**
- Opening: Acknowledge outcome and explain next steps
- Sentence Explanation: Plain-language breakdown of sentence imposed
  - Prison time, suspended time, probation/parole duration and conditions
  - Restitution, fines, court costs due and payment schedule
  - Sex offender registration (if applicable)
  - Reporting requirements, work restrictions, travel restrictions
- Appeal Rights: Prominently display:
  - **"APPEAL DEADLINE: [Calculated Date] (30 days from sentence under La. C.Cr.P. Art. 914)"**
  - Brief explanation of appeal process
  - Client's right to appeal (with counsel or pro se)
  - Cost implications
  - Ask: "Do you wish to pursue an appeal?"
- Probation/Parole Conditions: List all terms imposed
- Good-Time Credits (if incarcerated): Cross-reference **dw-sentencing-mitigation-specialist** for custody calculations
- Final Invoice: Billing summary and payment information
- Contact Information: How to reach firm for future needs

**C. Diversion Completion Letter**
- Opening: Congratulate on successful diversion completion (Art. 893/894)
- Diversion Details: Explain disposition — case dismissed upon completion
- Remaining Conditions: Any ongoing obligations (counseling, drug testing, etc.)
- Record Status: Explain that case is now dismissable (Art. 971)
- Expungement Eligibility: Advise on eligibility to expunge entire record
- Future Employment: No conviction to disclose
- Final Invoice: Billing summary

**D. Nolle Prosequi Letter**
- Explanation: State dismissed case at prosecutor's request (Art. 215)
- Implications: No conviction, but prosecutor retains right to refile
- Statute of Limitations: Explain recharge deadline (if any)
- Expungement: Eligible immediately under Art. 971 if no prejudice, or Art. 972 if with prejudice
- Contact: How to reach firm if case is refiled

**E. Transfer / Jurisdiction Change Letter**
- Explanation: Case transferred to another court (state, federal, juvenile)
- Next Steps: Introduce new counsel if applicable; explain transition
- Files: Confirm all discovery and exhibits transferred with case
- Contact: Provide firm contact if questions arise

**F. Abatement Letter (Defendant Deceased)**
- Explanation: Case abated upon death of defendant (Art. 215.1)
- Administrative Notes: No further obligations; case closed
- Estate/Restitution: Explain whether obligations survive (per La. law)
- Contact: Identify point of contact if estate inquiries arise

### Letter Content Checklist

- [ ] Disposition type clearly explained in plain language
- [ ] All key dates and deadlines prominently displayed
- [ ] Sentence/obligations summarized with payment information
- [ ] Appeal deadline calculated and prominently shown (if applicable)
- [ ] Expungement eligibility assessed and explained
- [ ] Final billing summary attached or referenced
- [ ] Probation/parole conditions listed (if applicable)
- [ ] Sex offender registration requirements noted (if applicable)
- [ ] Firm contact information and file retention policy included
- [ ] Attorney signature and date on letter

### Letter Delivery

- For clients in custody: Send via jail mail (certified format per facility)
- For clients out of custody: Send via email (if on file) + certified mail
- Attorney reviews and approves letter before sending
- Confirm delivery and obtain attorney sign-off before archiving case

---

## STEP 4: APPEAL ASSESSMENT

**Trigger:** Case disposition is Guilty Plea OR Guilty Verdict

### Appeal Viability Check

1. **Display Appeal Deadline Prominently**
   ```
   APPEAL DEADLINE: [Calculate: Date + 30 days from sentence]
   (La. C.Cr.P. Art. 914 — Motion for appeal must be filed within 30 days of sentence)
   (Misdemeanor appeals: 2 days from date sentence)
   ```

2. **Prompt Attorney Decision**
   ```
   "Do you want to run dw-appellate-error-monitor for an appeal viability assessment?"
   ```

3. **If Attorney Selects YES (Pursuing Appeal)**
   - Invoke **dw-appellate-error-monitor**
   - Pass: Complete trial transcript, trial errors preserved, sentencing transcript
   - Review error log for preserved trial errors
   - Assess viability of appeal based on error preservation
   - **CRITICAL:** Do NOT archive case while appeal is being pursued
   - Mark case status: "APPEAL PENDING — DO NOT ARCHIVE"
   - Save intermediate state to Case Brain
   - Schedule follow-up per appellate timeline
   - Proceed to Step 5A (appeal path)

4. **If Attorney Selects NO (No Appeal)**
   - Record decision in Case Brain: "No appeal pursued"
   - Proceed to Step 5B (expungement eligibility check)

### Step 5A: Appeal Workflow (if applicable)

- Ensure trial transcript is complete and ordered
- Preserve record for appellate review
- Brief attorney on appellate deadlines and filing requirements
- Do NOT proceed to file archival yet
- Notify attorney when appeal is final (appellate court decision rendered)
- Then return to Step 5B for post-appeal actions

---

## STEP 5: EXPUNGEMENT ELIGIBILITY CHECK

**Trigger:** Disposition is Dismissal, Acquittal, Diversion Completion, or Nolle Prosequi

### Expungement Eligibility Assessment

Conduct detailed analysis under Louisiana Code of Criminal Procedure Articles 971-986. Determine if and when client is eligible to petition for expungement.

**Art. 971 — Dismissals Without Prejudice**
- Eligible: Immediately upon dismissal
- Process: File motion to expunge in original court
- Effect: Arrest record, court records, and agency records destroyed

**Art. 972 — Dismissals With Prejudice**
- Eligible for felonies: Varies by case (may require time passage)
- Eligible for misdemeanors: Immediately
- Process: Motion in district court (if original was parish court)

**Art. 973 — Acquittals**
- Eligible: Immediately upon acquittal
- Effect: Entire arrest and prosecution record expunged
- Priority: Strong case for expungement; should be pursued promptly

**Art. 977 — First Offender Pardons**
- If case meets first-offender criteria, may be eligible for pardon
- Requires application to Governor's office
- Effect: Record restoration

**Art. 978 — Misdemeanor Convictions**
- Certain misdemeanors eligible after time period (e.g., drugs, theft)
- Waiting period: Typically 5 years from sentence
- Check offense code against eligibility schedule

**Art. 983 — Felony Convictions**
- Limited felonies eligible after extended waiting period (e.g., 10-15 years)
- Check offense code against eligibility schedule
- High standard; typically for non-violent offenses

### Expungement Eligibility Determination

For each applicable charge:
- [ ] Statute article that grants eligibility
- [ ] Eligibility date (immediate or date eligible)
- [ ] Waiting period (if any)
- [ ] Offense code and description
- [ ] Eligible under which article(s)

### Expungement Recommendation

- If eligible immediately: Recommend pursuing **dw-pretrial-motion-library** to draft expungement motion
- If future eligibility: Create calendar reminder via Google Calendar (1 week before eligibility date)
- Notify client of eligibility and next steps in disposition letter (Step 3)
- Provide estimated attorney fees for expungement motion

### Expungement Eligibility Memo

- Create memo documenting all analysis
- Save to: `<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/[ClientLastName] - Expungement Eligibility - [Date].docx`
- Include:
  - Charge(s) and disposition
  - Applicable statute articles
  - Eligibility date and calculation
  - Recommended next steps
  - Client contact plan

---

## STEP 6: FILE ARCHIVE & CLOSING CHECKLIST

Generate a comprehensive Case Closing Checklist to verify all closing requirements are met before archiving.

### Case Closing Checklist Document

Create a .docx checklist with the following items. Attorney verifies each item and initials/dates.

**Discovery & Evidence Management**
- [ ] All discovery materials returned to prosecutor or destroyed per agreement
- [ ] All evidence/exhibits returned to client or court
- [ ] Client property (cash, vehicle keys, personal items) returned to client
- [ ] Copy of all exhibits retained in case file
- [ ] Discovery ledger finalized (reference **dw-discovery-compliance-monitor**)

**Financial Matters**
- [ ] Final billing generated and reviewed by attorney
- [ ] All invoices sent to client
- [ ] Outstanding balance collected or written off (per attorney decision)
- [ ] Trust account reconciled (if applicable)
- [ ] Cost advances reconciled
- [ ] Court-appointed case: Billing submitted to district defender / appropriate authority

**Client Communication**
- [ ] Case resolution letter sent to client
- [ ] Client advised of appeal rights and deadlines (if applicable)
- [ ] Client advised of expungement eligibility (if applicable)
- [ ] Final invoice provided with payment terms
- [ ] Delivery of notification letter confirmed (email receipt / certified mail tracking)
- [ ] Client contact information updated

**Case Brain & Records**
- [ ] Case Brain updated with final disposition type, date, judge
- [ ] Final charges and sentence recorded in Case Brain
- [ ] Appeal deadline calculated and recorded in Case Brain
- [ ] Sentence modification deadline calculated and recorded
- [ ] Expungement eligibility assessed and recorded in Case Brain
- [ ] All case documents properly organized in folder structure

**Appeal & Post-Conviction**
- [ ] If guilty verdict/plea: Appeal viability assessed or waived
- [ ] If appeal pursued: Case marked "APPEAL PENDING" and NOT archived
- [ ] If no appeal: Decision documented in Case Brain
- [ ] Appellate error log preserved (reference **dw-appellate-error-monitor**)

**Expungement**
- [ ] Expungement eligibility memo completed and filed
- [ ] Client contacted re: expungement path (if eligible)
- [ ] Calendar reminder set for future expungement eligibility (if applicable)
- [ ] Expungement motion drafted or referral provided (if immediate eligibility)

**Administrative Closure**
- [ ] Conflict check database updated (case marked closed)
- [ ] Case management system updated with disposition
- [ ] Calendar cleared of all case-related deadlines (except appeal/future expungement dates)
- [ ] Co-counsel / public defender coordination closed
- [ ] Court coordinator notified of case closure
- [ ] Billing/accounting department notified of case closure

**Special Case Types (if applicable)**
- [ ] LWOP case: LWOP review sheet completed (reference **dw-lwop-populator**)
- [ ] Sex offense case: Registration requirements documented and explained to client
- [ ] Habitual offender case: Habitual offender audit completed (reference **dw-habitual-offender-auditor**)
- [ ] Juvenile case (transferred): Transition documentation completed

**File Retention & Archive**
- [ ] All case documents filed in proper case folders (01 - Intake, 02 - Pretrial, etc.)
- [ ] Sensitive documents (mental health records, etc.) flagged or secured
- [ ] Client file retention notice provided (5-year minimum per La. Rules Prof. Conduct)
- [ ] Archive location confirmed (attorney approval of folder relocation)
- [ ] Archive date recorded
- [ ] DEVONthink tagged with "CLOSED," disposition type, disposition date (if available)

**Checklist Sign-Off**
- Attorney Name (print): ___________________________
- Attorney Signature: ____________________________
- Date: __________________________
- All items completed and verified: YES / NO (circle one)

### Save Case Closing Checklist

- **Path:** `<case-root>/[ClientLastName] - Case Closing Checklist - [Date].docx`
- Use **docx** skill to generate document
- Attorney reviews all items before case is archived
- Attorney initials each section
- Checklist serves as final verification gate before archival

---

## STEP 7: ARCHIVE & RETENTION

**This step only proceeds if STEP 0-6 are fully complete and attorney has signed off on closing checklist.**

### Archive Folder Structure

1. **Specify Archive Location**
   - Default option: Move case folder to archive parent folder with "CLOSED - " prefix
   - Example: Client folder "Smith, John - Case #2024-CR-12345" becomes "CLOSED - Smith, John - Case #2024-CR-12345"
   - Alternative: Attorney may specify custom archive location
   - Confirm with attorney before executing move

2. **Folder Relocation**
   - Move entire case folder from active location to archive location
   - Preserve all subfolder structure (01 - Intake, 02 - Pretrial, etc.)
   - Verify all files moved successfully
   - Remove original folder from active location

3. **Archive Documentation**
   - Create archive summary with:
     - Case name, number, client name
     - Disposition type and date
     - Archive date
     - Archive location path
     - Retention deadline (archive date + 5 years)
   - Save summary to: `<case-root>/[ClientLastName] - Archive Summary - [Date].txt`

### File Retention Policy

**Louisiana Rules of Professional Conduct:**
- Minimum retention: 5 years after case closure (from disposition date)
- Longer retention: If client requests or if conflict/malpractice risk exists
- Destruction: After 5-year minimum, attorney may destroy files unless statute of limitations or ethical duty requires longer retention

**Retention Tracking:**
- Record archive date in Case Brain: "ARCHIVED: [Date]"
- Record destruction deadline in Google Calendar: "[ClientLastName] - File Destruction Eligible: [Archive Date + 5 Years]"
- Attorney responsible for review before destruction

### DEVONthink Tagging (if applicable)

If case files are stored in DEVONthink, apply the following tags:
- "CLOSED" (main status tag)
- "[Disposition Type]" (e.g., "GUILTY_PLEA", "ACQUITTAL", "DISMISSAL")
- "[Disposition Date - YYYY]" (e.g., "2026-04", for chronological sorting)
- "[Archive Date - YYYY]" (e.g., "ARCHIVED_2026")

### Final Archive Checklist

- [ ] Archive location confirmed with attorney
- [ ] Case folder moved to archive location
- [ ] All subfolders and files verified in new location
- [ ] Original active folder removed
- [ ] Archive summary created and saved
- [ ] Retention deadline calculated and recorded
- [ ] Destruction deadline set in Google Calendar (5 years from archive)
- [ ] DEVONthink tags applied (if applicable)
- [ ] Case management system marked as "ARCHIVED"
- [ ] Attorney acknowledges archive completion

**Archive Complete:** Case is now closed and filed per Louisiana Rules of Professional Conduct.

---

## INTEGRATION WITH D&W SKILL ECOSYSTEM

### Reads From:
- **dw-case-brain:** Full case history, preliminary disposition status
- **dw-case-dashboard:** Case critical dates, final status
- **dw-appellate-error-monitor:** Error preservation log (for appeal assessment in Step 4)

### Invokes:
- **dw-billing-narrative-generator** (Step 2): Captures all unbilled work across case lifecycle
- **dw-client-communication-drafter** (Step 3): Drafts disposition-specific client letters
- **dw-appellate-error-monitor** (Step 4): Optional appeal viability assessment
- **dw-sentencing-mitigation-specialist** (Step 3): Custody client good-time calculations
- **dw-pretrial-motion-library** (Step 5): Optional expungement motion draft
- **dw-lwop-populator** (Step 6): LWOP review sheet completion (if applicable)
- **dw-habitual-offender-auditor** (Step 6): Habitual offender audit (if applicable)
- **docx** skill: Case closing checklist generation
- **xlsx** skill: Final billing summary workbook

### Writes To:
- **Case Brain:** Final disposition type, dates, sentence, appeal/expungement deadlines
- **Case Folder:** Closing checklist, billing summary, expungement memo, archive summary
- **DEVONthink:** Archive tags (if available)
- **Google Calendar:** Appeal deadline, expungement eligibility reminder, file destruction deadline

### Uses:
- **docx skill** for closing checklist
- **xlsx skill** for final billing summary
- **Google Calendar API** for deadline tracking
- **DEVONthink MCP** for archive tagging (if available)

---

## CORE RULES

**These rules are non-negotiable and must be followed in every case closure:**

1. **NEVER close a case while sentencing is pending.**
   - If disposition entered but sentencing not yet imposed, mark as "DISPOSITION ENTERED — AWAITING SENTENCING"
   - Schedule follow-up to re-invoke this skill after sentencing
   - Do not proceed to archival until sentencing is complete

2. **NEVER archive a case while an appeal is being pursued.**
   - If attorney selects appeal in Step 4, case is marked "APPEAL PENDING"
   - Case remains in active status until appellate decision is final
   - Return to Step 5B (expungement check) only after appeal is concluded

3. **ALWAYS calculate and prominently display the appeal deadline.**
   - Art. 914: 30 days from sentence (2 days for misdemeanor)
   - Display in multiple locations: Step 4 prompt, client letter, Case Brain
   - Create Google Calendar reminder for appeal deadline
   - Attorney must explicitly approve no-appeal decision before proceeding

4. **ALWAYS check expungement eligibility for dismissals, acquittals, and diversion completions.**
   - Use Art. 971-986 framework in Step 5
   - Notify client of eligibility in disposition letter
   - Create calendar reminder if eligibility is future date
   - Recommend expungement motion if immediately eligible

5. **Attorney must approve all closing documents before case is archived.**
   - Client notification letter reviewed and signed by attorney
   - Final billing summary reviewed by attorney
   - Case closing checklist signed by attorney with all items verified
   - No archival proceeds without explicit attorney sign-off on checklist

6. **Retain files for minimum 5 years after case closure per Louisiana Rules of Professional Conduct.**
   - Record retention deadline in calendar upon archival
   - Calculate destruction deadline as archive date + 5 years
   - Do not destroy files before consulting with attorney regarding statute of limitations, conflict risk, or client request for extended retention

7. **Flag court-appointed cases for district defender billing submission.**
   - Identify if case was court-appointed (La. public defender or appointed private counsel)
   - Verify final billing submitted to district defender / appointing authority
   - Include copies of billing in case file before archival
   - Include court-appointment details in archive summary

---

## EXECUTION SUMMARY

This skill executes a 7-step case disposition workflow:

1. **DISPOSITION CONFIRMATION** — Mandatory gate confirming case has reached final disposition
2. **CASE BRAIN UPDATE** — Record all disposition details, deadlines, sentence
3. **FINAL BILLING** — Capture unbilled work and generate comprehensive billing summary
4. **CLIENT NOTIFICATION** — Draft disposition-specific letter with rights/obligations/next steps
5. **APPEAL ASSESSMENT** — Evaluate appeal viability and set appeal deadline
6. **EXPUNGEMENT CHECK** — Determine expungement eligibility and timeline
7. **FILE ARCHIVE** — Generate closing checklist, move to archive, set retention deadline

**Success Metric:** Case is fully closed, all obligations to client met, file archived and tagged per Louisiana Rules of Professional Conduct, and all downstream systems (Case Brain, DEVONthink, Google Calendar) updated.

---

## EXAMPLE SCENARIOS

### Scenario 1: Guilty Plea with Immediate Sentencing

1. Attorney triggers skill: "Close the case"
2. Confirms disposition: "Guilty Plea, sentenced today"
3. Skill records: Disposition date, sentence details (5 years hard labor, 10 years suspended, 5 years probation)
4. Skill calculates: Appeal deadline = 30 days from today
5. Runs billing generator: Captures all unbilled work
6. Drafts client letter: Explains sentence, appeal rights, probation conditions, final invoice
7. Prompts for appeal: "Pursue appellate review?"
8. If attorney says "No appeal": Proceeds to expungement check (none applicable for guilty plea)
9. Generates closing checklist, archives case

**Result:** Case closed, client notified, appeal deadline tracked in calendar, file archived with 5-year retention note.

### Scenario 2: Acquittal at Trial

1. Attorney triggers skill: "Case is closed — acquittal"
2. Confirms: Verdict date, charges acquitted on
3. Skill records: All charges acquitted, no sentence, no probation
4. Generates client letter: Congratulatory, explains acquittal, advises immediate expungement eligibility (Art. 973)
5. Expungement check: Client eligible immediately under Art. 973
6. Recommends: Pursue expungement motion via **dw-pretrial-motion-library**
7. Creates calendar reminder: Follow-up for expungement motion in 1 week
8. Generates closing checklist, archives case

**Result:** Client notified of favorable outcome, expungement path clearly explained, calendar reminder set for follow-up.

### Scenario 3: Guilty Verdict with Delayed Sentencing

1. Attorney triggers skill: "Verdict entered"
2. Confirms: Guilty verdict, but sentencing is scheduled for 4 weeks
3. Skill halts full closure: Marks as "DISPOSITION ENTERED — AWAITING SENTENCING"
4. Saves intermediate state to Case Brain
5. Creates Google Calendar reminder: "Return to dw-case-disposition workflow after sentencing"
6. Returns to attorney: "Case marked for closure after sentencing"

**After sentencing:** Attorney re-invokes skill with sentencing details, and full closure workflow (Steps 1-7) executes.

### Scenario 4: Diversion Completion

1. Attorney triggers skill: "Client completed diversion program"
2. Confirms: Diversion completion date, all conditions met
3. Skill records: Case dismissed upon diversion completion (Art. 893/894)
4. Generates client letter: Explains successful diversion, record dismissal, immediate expungement eligibility
5. Expungement check: Eligible immediately
6. Recommends expungement motion and sets calendar reminder
7. Generates closing checklist, archives case

**Result:** Client informed of successful completion and clear expungement path.

---

## TROUBLESHOOTING & EXCEPTIONS

### Exception 1: Co-Defendant Cases

If case involves multiple co-defendants:
- Close case only for the specific client represented by this firm
- Note in Case Brain if other co-defendants have pending cases
- Preserve any discovery or evidence for potential cross-case use
- Archive separately by client name to avoid confusion

### Exception 2: Retrial or Mistrial Ordered

If new trial is ordered after verdict:
- Do NOT archive case
- Mark in Case Brain: "MISTRIAL — RETRIAL SCHEDULED"
- Return to **dw-criminal-defense** master workflow
- Re-invoke **dw-case-disposition** only after final verdict/disposition

### Exception 3: Cases Transferred to Different Jurisdiction

If case transferred (federal, state, county):
- Mark disposition as "Transfer to [Jurisdiction]"
- Provide notice to new counsel if applicable
- Archive with note: "Case transferred — files maintained per original jurisdiction requirements"
- Retain files per both jurisdictions' rules of professional conduct (use longer requirement)

### Exception 4: Confidential Informant or Sensitive Documents

If case contains confidential informant information or sealed discovery:
- Flag files as "SENSITIVE — RESTRICTED ACCESS"
- Archive in secure location with access restrictions
- Do not tag in shared systems (DEVONthink, shared drives)
- Maintain separate secure log of sensitive files
- Consult with attorney re: destruction timeline (may exceed 5 years)

### Exception 5: Client Incarcerated Post-Sentencing

For clients entering custody:
- Ensure jail mail notification format complies with facility rules
- Include in letter: Sentence calculation, good-time credit projection (via **dw-sentencing-mitigation-specialist**)
- Provide contact information for firm (appeals, record correction, etc.)
- Note in Case Brain if client will need appellate or post-conviction assistance
- Archive case but maintain active contact protocol for incarcerated client needs

---

**Skill Version:** 1.0  
**Last Updated:** April 2026  
**Status:** Production Ready
