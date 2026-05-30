---
name: dw-case-disposition-crim
category: disposition
description: >
  Comprehensive case closing workflow for criminal case final dispositions. Records
  disposition outcome in Case Brain, generates final billing narrative, client notification
  draft, appeal eligibility assessment, and expungement eligibility assessment. Produces
  closing checklist and archives file while maintaining strict compliance with Louisiana
  Rules of Professional Conduct. ALWAYS invoke for "close the case," "case closed,"
  "disposition," "case resolved," "final disposition," "archive the case," "case outcome,"
  "wrap up the case," "case is over," "verdict entered," "plea entered," "dismissal,"
  "nolle prosequi," "case closing checklist." Do NOT use for active case management
  (use dw-criminal-defense), session persistence (use dw-case-brain), or mid-case status
  updates (use dw-criminal-defense).
---

# D&W Case Disposition Workflow

**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

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

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

### Source Citation Mandate

Every factual assertion in the closing workflow deliverables — disposition record, final billing narrative, client notification, appeal eligibility memo, expungement eligibility assessment, and closing checklist — must trace back to a specific source document. Case closure is irreversible; unsourced disposition data, sentence terms, or eligibility conclusions can mislead the client about appellate deadlines, expungement timing, and post-disposition obligations.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Minute Entry — Disposition, Docket #2026-CR-0456, dated 03/15/2026)`
- `(Plea Colloquy Transcript, p. 12, lines 5-18)`
- `(Sentencing Order, p. 1, para. 2)`
- `(Bill of Information, Count 1, p. 1)`
- `(Case Brain — Disposition Entry, 2026-04-15)`
- `(Court Docket — Verdict Entry, dated 03/15/2026)`

**Multiple-source rule:** When more than one document confirms a fact about the disposition, sentence, or charge resolution, cite all of them — e.g., `(Minute Entry — Disposition; Sentencing Order, p. 1)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH ATTORNEY/COURT RECORD]` so the attorney knows to confirm or remove it before notifying the client or archiving the file.

**Where sourcing applies:** All factual content — disposition type and date, sentence terms, charges resolved or remaining, appeal triggers, expungement waiting periods. Legal standards, Louisiana RPC obligations, and procedural deadlines follow normal legal citation format.

---

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

Invoke **dw-case-brain** to update the permanent case record with disposition details — disposition core data, charge information, sentencing terms (if applicable), and the full set of appellate / post-conviction deadlines (Art. 914 appeal, Art. 881.1 sentence modification, Art. 930.8 post-conviction DNA, Art. 215 motion to recall and resentence). Attorney reviews and approves all entries before the workflow advances.

**Reference**: Read `references/module-1-case-brain-record.md` for the full disposition data schema, charge-status taxonomy, sentencing field list, and appellate-deadline calculation rules.

---

## STEP 2: FINAL BILLING

Invoke **dw-billing-narrative-generator** to capture all unbilled session work across the case lifecycle, then generate a comprehensive billing summary as an Excel workbook (Summary by LEDES category, line-item Detail, By-Phase breakdown). Attorney signs off on final billing before the workflow proceeds to client notification.

**Output path**: `<case-root>/05 - Billing/[ClientLastName] - Final Billing Summary - [Date].xlsx`

**Reference**: Read `references/module-2-final-billing.md` for the four-step billing process, the workbook sheet specification, and the billing summary template items.

---

## STEP 3: CLIENT NOTIFICATION

Invoke **dw-client-communication-drafter** to draft a case resolution letter tailored to the disposition type. Six letter templates cover the disposition-type matrix:

- **A. Acquittal / Dismissal Letter** — congratulatory, immediate Art. 973 expungement path
- **B. Guilty Plea / Guilty Verdict Letter** — sentence breakdown, prominent appeal deadline (Art. 914), probation conditions, good-time cross-reference
- **C. Diversion Completion Letter** — Art. 893/894 disposition, Art. 971 dismissal, expungement eligibility
- **D. Nolle Prosequi Letter** — Art. 215 explanation, recharge risk, Art. 971/972 expungement framework
- **E. Transfer / Jurisdiction Change Letter** — case-transfer mechanics and file handover
- **F. Abatement Letter** — Art. 215.1 (defendant deceased), estate/restitution survival

Letter delivery follows custody status (jail mail certified format vs. email + certified mail). Attorney reviews and approves before sending.

**Reference**: Read `references/module-3-client-notification-letters.md` for the full six-letter template library, the letter content checklist, and the delivery protocol.

---

## STEP 4: APPEAL ASSESSMENT

**Trigger:** Case disposition is Guilty Plea OR Guilty Verdict.

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

**Trigger:** Disposition is Dismissal, Acquittal, Diversion Completion, or Nolle Prosequi.

Conduct detailed analysis under Louisiana Code of Criminal Procedure Articles 971-986 to determine if and when the client is eligible to petition for expungement. The framework covers Art. 971 (dismissals without prejudice), Art. 972 (dismissals with prejudice), Art. 973 (acquittals — immediate, high priority), Art. 977 (first offender pardons), Art. 978 (misdemeanor convictions, ~5-year wait), and Art. 983 (felony convictions, extended wait). For each charge the workflow records statute, eligibility date, waiting period, and offense code.

If immediately eligible, recommend pursuing **dw-pretrial-motion-library** to draft the expungement motion. If future eligibility, set a Google Calendar reminder. Document everything in an Expungement Eligibility Memo saved to `<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/[ClientLastName] - Expungement Eligibility - [Date].docx`.

**Reference**: Read `references/module-5-expungement-eligibility.md` for the full Art. 971-986 article-by-article framework, the per-charge determination checklist, and the eligibility memo specification.

---

## STEP 6: FILE ARCHIVE & CLOSING CHECKLIST

Generate a comprehensive Case Closing Checklist (.docx) verifying every closing requirement is met before archiving. The checklist spans nine sections: Discovery & Evidence Management, Financial Matters, Client Communication, Case Brain & Records, Appeal & Post-Conviction, Expungement, Administrative Closure, Special Case Types (LWOP — routes to **dw-criminal-defense** Phase 1 Step 3 Refresh; sex offense; habitual offender — routes to **dw-habitual-offender-auditor**; juvenile transfer), File Retention & Archive, and a final attorney sign-off block.

The checklist is the verification gate before archival — attorney initials each section and signs the bottom block.

**Output path**: `<case-root>/[ClientLastName] - Case Closing Checklist - [Date].docx` (uses **docx** skill)

**Reference**: Read `references/module-6-closing-checklist.md` for the full nine-section checklist with every line item, plus the sign-off block format.

---

## STEP 7: ARCHIVE & RETENTION

**This step only proceeds if STEP 0-6 are fully complete and the attorney has signed off on the closing checklist.**

Move the case folder from active to archive location (default: prefix with "CLOSED - "), preserving full subfolder structure. Create an Archive Summary capturing case name/number, disposition type and date, archive date, archive path, and the 5-year retention deadline (Louisiana Rules of Professional Conduct minimum). Apply DEVONthink tags ("CLOSED", disposition type, disposition year, archive year). Set a Google Calendar reminder for the file-destruction-eligible date (archive + 5 years).

**Reference**: Read `references/module-7-archive-and-retention.md` for the full folder-relocation procedure, the Louisiana RPC retention policy, the DEVONthink tagging schema, and the final archive checklist.

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
- **dw-criminal-defense** (Step 6, Phase 1 Step 3): LWOP review sheet completion via `000 - Case Profile.docx` Part 2A (Homicide) or 2B (Sex Offense), if applicable — formerly the dw-lwop-populator skill, merged into the master workflow in v5.3
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

Four worked-through scenarios cover the most common disposition-closure paths: (1) Guilty Plea with Immediate Sentencing, (2) Acquittal at Trial, (3) Guilty Verdict with Delayed Sentencing (sentencing-status gate fires), and (4) Diversion Completion.

**Reference**: Read `references/example-scenarios.md` for the four scenarios, each with the full step-by-step skill execution and expected closure result.

---

## TROUBLESHOOTING & EXCEPTIONS

Five exceptions cover non-standard closure paths: (1) Co-Defendant Cases (close per-client only), (2) Retrial / Mistrial Ordered (do NOT archive — return to **dw-criminal-defense**), (3) Cases Transferred to Different Jurisdiction, (4) Confidential Informant or Sensitive Documents (restricted-access archival), and (5) Client Incarcerated Post-Sentencing (jail-mail format, ongoing contact protocol).

**Reference**: Read `references/troubleshooting-exceptions.md` for the five exception categories with full handling procedures.

---

## QUICK REFERENCES

The following reference files in `references/` carry the detailed module content. Read them as the corresponding step is invoked:

- `references/module-1-case-brain-record.md` — Step 1: Case Brain disposition data schema, charge status taxonomy, sentencing fields, appellate deadlines (Arts. 914 / 881.1 / 930.8 / 215)
- `references/module-2-final-billing.md` — Step 2: dw-billing-narrative-generator handoff, four-step billing process, Excel workbook sheet specification, billing summary template items
- `references/module-3-client-notification-letters.md` — Step 3: six disposition-specific letter templates (Acquittal/Dismissal, Guilty Plea/Verdict, Diversion, Nolle Prosequi, Transfer, Abatement), letter content checklist, delivery protocol
- `references/module-5-expungement-eligibility.md` — Step 5: Louisiana Code Title XXXIV Arts. 971-986 article-by-article framework, per-charge determination checklist, expungement memo specification
- `references/module-6-closing-checklist.md` — Step 6: nine-section attorney closing checklist (Discovery, Financial, Client Communication, Case Brain & Records, Appeal & Post-Conviction, Expungement, Administrative Closure, Special Case Types, File Retention & Archive) with sign-off block
- `references/module-7-archive-and-retention.md` — Step 7: archive folder relocation procedure, Louisiana RPC 5-year retention policy, DEVONthink tagging schema, final archive checklist
- `references/example-scenarios.md` — Four worked closure scenarios (immediate-sentencing plea, trial acquittal, delayed-sentencing verdict, diversion completion)
- `references/troubleshooting-exceptions.md` — Five non-standard closure paths (co-defendant, retrial/mistrial, jurisdiction transfer, sensitive documents, post-sentencing custody)

---

**Skill Version:** 1.0
**Last Updated:** April 2026
**Status:** Production Ready
