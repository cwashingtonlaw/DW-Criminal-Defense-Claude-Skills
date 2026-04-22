---
name: dw-billing-narrative-generator
description: >
  Generate billing time entry narratives from session work. ALWAYS invoke for "billing entries," "time entries," "log my time," "what did we bill today," "generate narratives," "billing summary," or at session close when the attorney asks to capture time. Produces LEDES-compatible narratives.
---

# D&W Billing Narrative Generator — Session-to-Billings Pipeline

**Version 2.0 | Internal Use Only**

Converts a session's work output into discoverable-safe, attorney-reviewed billing narratives. Reads session activity (skills invoked, documents created/reviewed, analysis performed, case brain updates) and maps each work product to standard UTBMS/LEDES litigation codes. Deduplicates redundant work, generates professional billing language safe for discovery. Attorney adjusts times and approves before submission.

---

## Workflow

### STEP 1 — Session Work Inventory

Review the completed session and catalog all work performed:
- Skills invoked (with timestamps if available)
- Documents created, reviewed, or modified
- Analysis performed (research, evidence review, strategic assessment)
- Case Brain updates or cross-case connections noted
- Meetings or consultations conducted
- Time estimates for each work product

**Gather:**
- Skill execution log
- Document modification timestamps
- Analysis scope and deliverables
- Any attorney notes on time spent
### STEP 1A — Deduplication Logic

Check for duplicate work items before mapping to billing codes:

**Deduplication Rules:**
- If the same D&W skill was invoked multiple times on the same evidence or case issue (e.g., dw-suppression-motion run twice for edits to the same motion), consolidate into a single billing entry
- Combine time estimates: sum the hours from each invocation
- Preserve the most comprehensive description from the work product
- Flag for attorney review: "Combined 2 sessions on [topic] = [total hours]"
- If same LEDES code + same subject matter appears twice, merge into one entry with combined time

**Example:**
- Session 1: dw-suppression-motion (1.5 hrs) — Fourth Amendment illegal search
- Session 2: dw-suppression-motion (0.75 hrs) — Fourth Amendment illegal search (edits)
- Deduplicated: dw-suppression-motion (2.25 hrs) — Fourth Amendment illegal search (drafting and revisions)
### STEP 2 — Map to Billing Categories

Use the D&W Skill-to-LEDES Code Mapping table below to assign each work item to its primary billing code. Add sub-codes from the Criminal Defense Sub-Codes reference section for additional granularity.

#### D&W Skill-to-LEDES Code Mapping

| D&W Skill | Primary LEDES Code | Activity Type |
|-----------|-------------------|---------------|
| dw-case-brain | L100 | Case Management |
| dw-case-dashboard | L100 | Case Management |
| dw-criminal-defense (Phase 1) | L100 | Case Management |
| dw-discovery-orchestrator | L160 | Discovery |
| dw-discovery-compliance-monitor | L160 | Discovery |
| dw-suppression-motion | L200 | Motions |
| dw-404b-opposition | L200 | Motions |
| dw-pretrial-motion-library | L200 | Motions |
| dw-bond-and-release-motion | L200 | Motions |
| dw-cross-exam-architect | L300 | Trial Preparation |
| dw-trial-notebook-builder | L300 | Trial Preparation |
| dw-jury-instructions-builder | L300 | Trial Preparation |
| dw-voir-dire-assistant | L300 | Trial Preparation |
| dw-jury-focus-group | L300 | Trial Preparation || dw-witness-statement-analyzer | L110 | Investigation |
| dw-timeline-builder | L110 | Investigation |
| dw-video-evidence-auditor | L110 | Investigation |
| dw-forensic-dump-analyzer | L110 | Investigation |
| dw-mobile-forensic-auditor | L110 | Investigation |
| dw-crime-scene-auditor | L110 | Investigation |
| dw-chain-of-custody-auditor | L110 | Investigation |
| dw-cell-site-geolocation-auditor | L110 | Investigation |
| dw-eyewitness-identification-auditor | L110 | Investigation |
| dw-social-media-auditor | L110 | Investigation |
| dw-confession-interrogation-auditor | L110 | Investigation |
| dw-child-forensic-interview-auditor | L110 | Investigation |
| dw-brady-giglio-auditor | L160 | Discovery |
| dw-expert-witness-evaluator | L130 | Experts |
| dw-sex-offense-specialist | L120 | Legal Research |
| dw-plea-negotiation-analyzer | L150 | Negotiations |
| dw-sentencing-mitigation-specialist | L500 | Sentencing |
| dw-habitual-offender-auditor | L500 | Sentencing |
| dw-post-conviction-relief | L500 | Sentencing |
| dw-appellate-error-monitor | L400 | Appeals |
| dw-client-communication-drafter | L100 | Case Management |
| dw-defense-investigator-tasking | L110 | Investigation |
| dw-transcript-router | L140 | Transcripts |
| dw-lwop-populator | L500 | Sentencing |
#### Criminal Defense Sub-Codes Reference

Use these sub-codes for additional granularity and to distinguish specific activity types within main LEDES categories:

| Sub-Code | Description | Primary LEDES |
|----------|-------------|---------------|
| L110.1 | Witness Interview (Defense) | L110 |
| L110.2 | Scene Investigation | L110 |
| L110.3 | Digital/Electronic Evidence Review | L110 |
| L110.4 | Forensic Evidence Analysis | L110 |
| L120.1 | Legal Research — Statutory | L120 |
| L120.2 | Legal Research — Case Law | L120 |
| L120.3 | Strategy Conference (Internal) | L120 |
| L160.1 | Discovery Receipt & Indexing | L160 |
| L160.2 | Discovery Compliance Audit | L160 |
| L160.3 | Brady/Giglio Review | L160 |
| L200.1 | Motion Drafting | L200 |
| L200.2 | Motion Research | L200 |
| L200.3 | Motion Hearing Preparation | L200 |
| L300.1 | Cross-Examination Preparation | L300 |
| L300.2 | Jury Selection Preparation | L300 |
| L300.3 | Trial Exhibit Preparation | L300 |
| L500.1 | Sentencing Memorandum | L500 |
| L500.2 | Post-Conviction Review | L500 |
### STEP 3 — Generate Narratives

For each deduplicated work item, draft a discovery-safe billing narrative using this template:

**Template:**
```
[Skill Name / Activity]: [Case Phase]
Time: [X.XX hours]
LEDES Code: [Code] [Sub-Code if applicable]
Narrative: [2-3 sentences describing work performed, documents reviewed, analysis conducted, or deliverables created. Use professional language suitable for opposing counsel discovery.]
```

**Safety Rules:**
- Never include strategy assessments, case theory debates, or attorney mental impressions
- Describe work product facts only: "Reviewed X documents for Y purposes"
- Do not name witnesses except where necessary (use "witness interview" instead of "Spoke with John Smith about...")
- Avoid speculation about evidence value or defense theories
- Focus on scope and methodology, not conclusions
- Generate multiple narrative options (Brief, Standard, Detailed) for attorney selection

**Example Narratives:**

**Brief:**
"Reviewed body camera footage and police reports for Fourth Amendment issues. Prepared written analysis."
(1.5 hours, L110.3)

**Standard:**
"Reviewed body camera footage, dispatch records, and police incident reports. Analyzed for Fourth Amendment violations regarding warrantless search and seizure. Prepared written memorandum summarizing findings for motion preparation."
(1.5 hours, L110.3)
**Detailed:**
"Reviewed body camera footage (47 minutes), dispatch call recordings, incident reports, and witness statements. Analyzed evidence timeline and police conduct for potential Fourth Amendment violations including warrantless search, seizure, and detention issues. Prepared comprehensive memorandum with evidence citations and legal analysis framework for suppression motion preparation."
(1.5 hours, L110.3)

---

### STEP 4 — Present for Attorney Review

Generate a time entry summary sheet with:
- **Session Date:** [Date]
- **Case:** [Case name and matter ID]
- **Total Hours:** [Sum]
- **Summary Table:** Skill invoked | Hours | LEDES Code | Narrative | [Approve/Edit/Reject buttons]

Display all three narrative options (Brief/Standard/Detailed) and allow attorney to:
1. **Adjust time:** Click to edit hours (shows time calculation rules)
2. **Choose narrative:** Select Brief, Standard, or Detailed version
3. **Modify narrative:** Free-form edit before approval
4. **Approve:** Confirms entry for billing submission
5. **Reject:** Removes entry from this billing cycle
6. **Flag for review:** Attorney adds internal notes

**Example Approval UI:**
```
[Session: 2026-04-06] [Case: State v. Rodriguez, 2025-CV-12345]

| Skill | Hours | Code | Narrative | Action |
|-------|-------|------|-----------|--------|
| dw-suppression-motion | 2.25 | L200.1 | [Standard narrative] | [Approve] [Edit] [Reject] |
| dw-brady-giglio-auditor | 1.5 | L160.3 | [Detailed narrative] | [Approve] [Edit] [Reject] |
| dw-cross-exam-architect | 3.0 | L300.1 | [Brief narrative] | [Approve] [Edit] [Reject] |

TOTAL BILLABLE HOURS: 6.75
[Save as Draft] [Submit to Billing] [Export]
```
### STEP 5 — Output Options

Attorney selects output format after approval. System automatically creates save paths and folder structure.

#### Save Paths

**Default (XLSX):**
- Path: `<case-root>/05 - Billing/[ClientLastName] - Time Entries - [YYYY-MM-DD].xlsx`
- Creates folder if needed: `<case-root>/05 - Billing/`
- Format: Multi-tab workbook with entries, narrative legend, LEDES code reference
- Includes: Session date, skill, hours, LEDES code, narrative, attorney approval signature line

**Alternative (CSV):**
- Path: `<case-root>/05 - Billing/[ClientLastName] - Time Entries - [YYYY-MM-DD].csv`
- Format: Comma-separated values for import into billing software
- Fields: Date, Skill, Hours, LEDES Code, Sub-Code, Narrative, Attorney Initials

**Archival (PDF Summary):**
- Path: `<case-root>/05 - Billing/[ClientLastName] - Time Entries - [YYYY-MM-DD].pdf`
- Format: Print-ready summary with QR code linking to original XLSX
- Includes: All entries, total hours, attorney approval statement

#### Folder Creation Rules
- If `<case-root>/05 - Billing/` does not exist, create automatically
- Preserve existing entries if folder exists (append new date-stamped files)
- Maintain consistent naming: `[ClientLastName] - Time Entries - [YYYY-MM-DD]`
- Use client last name from case brain database; prompt attorney to confirm if ambiguous
#### Output Actions

```
[XLSX Export] — Downloads workbook
[CSV Export] — Downloads CSV for billing software import
[PDF Summary] — Generates print-ready summary
[Email to Billing] — Sends XLSX to billing@dw-criminal.local
[Archive] — Saves to case file automatically; note date in case log
```

---

## Integration

### Triggering the Skill

This skill is **automatically invoked** in these scenarios:

1. **Explicit request:** User asks "Generate billing entries," "Log my time," "Create narratives," "What did we bill today?"
2. **Session close:** At end of session, if attorney asks "Can you capture this for billing?"
3. **Scheduled:** Nightly summary if multiple skills were invoked in a single session
4. **Case brain sync:** When dw-case-brain is updated with session work products, flag for billing review

### Data Sources

- **dw-case-brain:** Current case phases, parties, evidence status
- **Session transcript:** Skills invoked, timestamps, user notes
- **Document system:** Files created/modified during session (timestamps, names)
- **Attorney notes:** Any explicit time estimates or narrative guidance provided in-session

### Output Integration

- **XLSX files:** Compatible with practice management software (Clio, Lexis Advance, etc.)
- **CSV files:** Direct import to billing databases
- **PDF summaries:** Print for attorney records or client file
- **Email option:** Routes to billing team with case ID in subject line
---

## Core Rules

### Billing Ethics & Compliance

1. **Accuracy:** Never inflate or deflate time estimates. Use conservative estimates based on documented work.
2. **Segregation:** Bill only for work actually performed; do not bundle unrelated tasks.
3. **Discovery safety:** All narratives must be suitable for opposing counsel review. No strategy, theory, or mental impressions.
4. **Attorney approval:** No entry is submitted until attorney has reviewed and approved.
5. **Client communication:** Time entries may be shared with client; avoid internal-only language.

### Narrative Standards

- **Length:** 1-3 sentences per entry; avoid overly detailed descriptions
- **Active voice:** "Reviewed X documents" not "Documents were reviewed"
- **Specificity:** "Fourth Amendment search analysis" not "legal work"
- **Scope clarity:** Quantify where possible ("50-page document," "14 witness interviews")
- **Neutral tone:** Describe work performed, not conclusions reached

### Deduplication Guardrails

- Only consolidate if SAME skill + SAME subject matter within same session or immediately adjacent sessions
- Always preserve combined time (sum all component hours)
- Flag any consolidation >4 hours for attorney review
- If uncertain, default to separate entries; attorney can manually consolidate

### LEDES Code Accuracy

- Use primary code from D&W Skill-to-LEDES mapping table
- Add sub-code only if it meaningfully distinguishes activity type
- Do not force-fit work into wrong categories for billing purposes
- When skill spans multiple categories, create separate entries for each category
### Time Estimate Logic

- **Skill execution time:** Base estimate from skill output timestamp minus invocation time
- **Analysis work:** 0.5 hour minimum per skill execution; more if complex evidence
- **Document creation:** 0.25 hours per document (brief memos); up to 1+ hours per comprehensive memorandum
- **Reviews/revisions:** 0.25 hours per revision round (consolidated in deduplication step)
- **Attorney input:** If attorney provides explicit time in session notes, use that figure
- **Conservative approach:** Round down when uncertain; flag outliers (>3 hours per entry) for review

### Confidentiality & Access

- Time entries contain case information; treat as privileged work product
- Do not share unsaved drafts with external parties
- XLSX/CSV files should be password-protected before email transmission
- Archive completed entries in secure case file location only
- Retain drafts for 30 days after approval; delete if rejected

---

## Example Workflow

**Scenario:** Attorney completes a session involving suppression motion drafting, discovery review, and Brady analysis.

1. **STEP 1 — Session Work Inventory**
   - dw-suppression-motion invoked at 2:15 PM, completed 4:00 PM (1.75 hours)
   - dw-brady-giglio-auditor invoked at 4:05 PM, completed 5:15 PM (1.25 hours)
   - dw-discovery-compliance-monitor invoked at 1:30 PM, completed 2:10 PM (0.67 hours)
   - No duplicates identified

2. **STEP 1A — Deduplication Check**
   - Each skill invoked once with distinct subject matter
   - No consolidation needed
   - Proceed to mapping
3. **STEP 2 — Map to Billing Categories**
   - dw-suppression-motion → L200.1 (Motion Drafting)
   - dw-brady-giglio-auditor → L160.3 (Brady/Giglio Review)
   - dw-discovery-compliance-monitor → L160.2 (Discovery Compliance Audit)

4. **STEP 3 — Generate Narratives** (Standard option shown)

   **Entry 1:**
   - Skill: dw-suppression-motion
   - Time: 1.75 hours
   - LEDES Code: L200.1
   - Narrative: "Drafted Fourth Amendment suppression motion challenging warrantless vehicle search. Reviewed case law on vehicle exception to warrant requirement. Incorporated factual analysis from police reports and witness statements."

   **Entry 2:**
   - Skill: dw-brady-giglio-auditor
   - Time: 1.25 hours
   - LEDES Code: L160.3
   - Narrative: "Conducted Brady/Giglio audit of prosecution discovery materials. Reviewed police reports and witness statements for material exculpatory information and witness credibility issues. Prepared summary for case file."

   **Entry 3:**
   - Skill: dw-discovery-compliance-monitor
   - Time: 0.67 hours
   - LEDES Code: L160.2
   - Narrative: "Updated discovery compliance ledger with received police reports and digital evidence. Cross-referenced with case inventory to ensure all materials logged and tracked."
5. **STEP 4 — Present for Attorney Review**

   Summary displayed:
   ```
   Session: 2026-04-06 | Case: State v. Williams, 2025-CR-08847
   Total Hours (before approval): 3.67

   | Skill | Hours | Code | Narrative | Action |
   |-------|-------|------|-----------|--------|
   | dw-suppression-motion | 1.75 | L200.1 | [Narrative] | [Approve] |
   | dw-brady-giglio-auditor | 1.25 | L160.3 | [Narrative] | [Approve] |
   | dw-discovery-compliance-monitor | 0.67 | L160.2 | [Narrative] | [Approve] |
   ```

   Attorney reviews, approves all three entries without modification.

6. **STEP 5 — Output Options**

   System generates:
   - XLSX: `/case-root/05 - Billing/Williams - Time Entries - 2026-04-06.xlsx`
   - CSV: `/case-root/05 - Billing/Williams - Time Entries - 2026-04-06.csv`
   - PDF: `/case-root/05 - Billing/Williams - Time Entries - 2026-04-06.pdf`

   Attorney selects XLSX export for import into Clio practice management system.

---

**Version History:**
- v2.0 (2026-04-06): Added deduplication logic, D&W skill mapping, sub-codes, explicit save paths
- v1.0 (2025-12-XX): Initial release with basic narrative generation