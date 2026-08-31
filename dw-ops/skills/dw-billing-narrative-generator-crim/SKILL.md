---
name: dw-billing-narrative-generator-crim
category: ops
description: >
  Generate billing time entry narratives from session work. ALWAYS invoke for "billing entries," "time entries," "log my time," "what did we bill today," "generate narratives," "billing summary," or at session close when the attorney asks to capture time. Produces LEDES-compatible narratives.
---

# D&W Billing Narrative Generator — Session-to-Billings Pipeline

**Version 2.0 | Internal Use Only**

Converts a session's work output into discoverable-safe, attorney-reviewed billing narratives. Reads session activity (skills invoked, documents created/reviewed, analysis performed, case brain updates) and maps each work product to standard UTBMS/LEDES litigation codes. Deduplicates redundant work, generates professional billing language safe for discovery. Attorney adjusts times and approves before submission.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any time entries, billing logs, session activity exports, prior billing narratives, or case activity records, do not analyze anything yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional time entries, billing logs, session activity exports, prior billing narratives, or case activity records? I'll start narrative generation only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-narrative discovery of an additional session log, a missed Case Brain update, or a co-counsel's parallel time entries would require complete re-deduplication and re-mapping to LEDES codes.

---

### Source Citation Mandate

Every factual assertion in the billing narratives must trace back to a specific source — a session log, document timestamp, Case Brain entry, or attorney-supplied note. Billing narratives are discoverable in fee disputes and may be reviewed by judges in fee-shifting motions; unsourced time claims undermine the credibility of the billing record.

**Citation format:** Cite the underlying work product or activity log. Examples:
- `(Session Log — 2026-04-15, dw-suppression-motion-crim invocation)`
- `(Case Brain Update — 2026-04-15, Suppression Motion drafted)`
- `(Document Modified — Motion to Suppress.docx, 2026-04-15 14:32)`
- `(Attorney Note — Phone call with client, 2026-04-15)`

**Multiple-source rule:** When more than one source confirms the work performed, cite all of them — e.g., `(Session Log — 2026-04-15; Document Modified — Motion to Suppress.docx, 2026-04-15)`.

**Unsourced assertions:** If a time entry cannot be tied to a documented activity, mark it `[UNSOURCED — VERIFY WITH ATTORNEY]` so the attorney can confirm or remove it before submission to the billing system.

**Where sourcing applies:** All factual content in narratives — task descriptions, durations, deliverables produced. Narratives must accurately describe work actually performed; do not invent activities to fill time blocks.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

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
- If the same D&W skill was invoked multiple times on the same evidence or case issue (e.g., dw-suppression-motion-crim run twice for edits to the same motion), consolidate into a single billing entry
- Combine time estimates: sum the hours from each invocation
- Preserve the most comprehensive description from the work product
- Flag for attorney review: "Combined 2 sessions on [topic] = [total hours]"
- If same LEDES code + same subject matter appears twice, merge into one entry with combined time

**Example:**
- Session 1: dw-suppression-motion-crim (1.5 hrs) — Fourth Amendment illegal search
- Session 2: dw-suppression-motion-crim (0.75 hrs) — Fourth Amendment illegal search (edits)
- Deduplicated: dw-suppression-motion-crim (2.25 hrs) — Fourth Amendment illegal search (drafting and revisions)
### STEP 2 — Map to Billing Categories

Use the D&W Skill-to-LEDES Code Mapping table in `references/ledes-code-mapping.md` to assign each work item to its primary billing code. Add sub-codes from the Criminal Defense Sub-Codes Reference in the same file for additional granularity.

Primary codes: L100 Case Management, L110 Investigation (all evidence auditors, timeline, investigator tasking), L120 Legal Research, L130 Experts, L140 Transcripts, L150 Negotiations, L160 Discovery (orchestrator, compliance monitor, Brady/Giglio), L200 Motions, L300 Trial Preparation, L400 Appeals, L500 Sentencing. Sub-codes (L110.1–.4, L120.1–.3, L160.1–.3, L200.1–.3, L300.1–.3, L500.1–.2) add granularity within a primary code.

Read `references/ledes-code-mapping.md` now for the full D&W Skill-to-LEDES Code Mapping table and the Criminal Defense Sub-Codes Reference table.

### STEP 3 — Generate Narratives

For each deduplicated work item, draft a discovery-safe billing narrative using this template:

**Template fields:** `[Skill Name / Activity]: [Case Phase]`, `Time`, `LEDES Code [Sub-Code]`, and a 2–3 sentence `Narrative` suitable for opposing-counsel discovery. Read `references/narrative-templates-and-examples.md` now for the exact template block.

**Safety Rules:**
- Never include strategy assessments, case theory debates, or attorney mental impressions
- Describe work product facts only: "Reviewed X documents for Y purposes"
- Do not name witnesses except where necessary (use "witness interview" instead of "Spoke with John Smith about...")
- Avoid speculation about evidence value or defense theories
- Focus on scope and methodology, not conclusions
- Generate multiple narrative options (Brief, Standard, Detailed) for attorney selection

**Example narratives** (Brief / Standard / Detailed versions of the same 1.5-hour L110.3 body-camera review) are in `references/narrative-templates-and-examples.md` — read them now before drafting.

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

See the **Example Approval UI** block (session header, per-skill table with Approve / Edit / Reject actions, total billable hours, Save as Draft / Submit to Billing / Export) in `references/narrative-templates-and-examples.md`.
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
[Email to Billing] — Sends XLSX to billing@danielswashington.com
[Archive] — Saves to case file automatically; note date in case log
```

---

## Integration

### Triggering the Skill

This skill is **automatically invoked** in these scenarios:

1. **Explicit request:** User asks "Generate billing entries," "Log my time," "Create narratives," "What did we bill today?"
2. **Session close:** At end of session, if attorney asks "Can you capture this for billing?"
3. **Scheduled:** Nightly summary if multiple skills were invoked in a single session
4. **Case brain sync:** When dw-case-brain-crim is updated with session work products, flag for billing review

### Data Sources

- **dw-case-brain-crim:** Current case phases, parties, evidence status
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

Worked example — a session with suppression-motion drafting, discovery review, and Brady analysis walked through Steps 1 → 1A → 2 → 3 → 4 → 5 (three entries, 3.67 hours, XLSX export to Clio). Read `references/example-workflow.md` now for the full walkthrough.

---

## Quick References

- **ledes-code-mapping.md** — Step 2; D&W Skill-to-LEDES Code Mapping table and Criminal Defense Sub-Codes Reference
- **narrative-templates-and-examples.md** — Steps 3–4; narrative entry template, Brief / Standard / Detailed example narratives, example approval UI
- **example-workflow.md** — Example Workflow; end-to-end worked session (Steps 1–5)

---

**Version History:**
- v2.0 (2026-04-06): Added deduplication logic, D&W skill mapping, sub-codes, explicit save paths
- v1.0 (2025-12-XX): Initial release with basic narrative generation
