---
name: dw-timeline-builder-crim
category: trial-prep
description: >
  Build and maintain the master case timeline from all evidence sources. ALWAYS invoke for
  "build the timeline," "case timeline," "master timeline," "chronology," "sequence of
  events," "what happened when," "timeline conflicts," "update the timeline," "visual timeline,"
  "interactive timeline," "timeline chart," or "show me the timeline." Aggregates timestamps
  from incident reports, BWC, cell site data, phone records, witness statements, jail calls,
  and all other sources into a single conflict-flagged chronological record. Populates the
  Timeline sheet in Case Tables.xlsx. Generates visual timelines on demand.
---

# Timeline Builder
**Daniels & Washington | Criminal Defense Case Automation | Version 1.0**

Master chronological timeline skill. Aggregates all timestamped evidence from every source into a unified, conflict-flagged timeline with source citations. Serves as the forensic backbone for cross-examination, impeachment, and defense strategy.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any discovery documents, witness statements, BWC footage, CAD logs, cell records, jail call transcripts, or other timeline source materials, do not analyze anything yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional discovery documents, incident reports, BWC footage, dash cam, 911/CAD logs, cell records, CSLI data, jail call transcripts, witness statements, surveillance footage, forensic reports, or other timeline source materials? I'll start the timeline build only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-build discovery of an additional source — a CSLI report, a previously unproduced BWC clip, or a witness statement — would require complete re-extraction, re-conflict-flagging, and re-validation across the existing timeline.

---

### Source Citation Mandate

Every event in the master timeline must trace back to a specific source document. The timeline is the forensic backbone for cross-examination, impeachment, suppression hearings, and trial narrative; an unsourced event undermines impeachment leverage and introduces error into every downstream filing.

**Citation format:** Cite the document title, page/section, and timestamp or paragraph. Examples:
- `(911 CAD Log — LCPD Case #2026-00456, p. 1, "Call Received")`
- `(Officer Smith BWC, Timestamp 00:05:32)`
- `(Incident Report — LCPD Case #2026-00456, p. 3, para. 2)`
- `(Cell Records — Verizon, Subscriber 504-555-0100, Row #145)`
- `(CSLI Report — Sprint, Tower #ABC123, Ping 14:23:00 UTC)`
- `(Jail Call Transcript — Call ID #2026-7890, Timestamp 00:14:32)`
- `(Surveillance Footage — Convenience Store, 2026-03-15, Timestamp 14:31:00)`

**Multiple-source rule:** When more than one source confirms an event timestamp, cite all of them — e.g., `(911 CAD Log, p. 1; Officer Smith BWC, Timestamp 00:00:08)`.

**Conflict flagging:** When sources disagree on timing, log every source with its timestamp and flag the conflict in the Timeline sheet. Do not silently pick one; the conflict itself may be impeachment material.

**Unsourced assertions:** If an event cannot be tied to a specific source, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows the event is provisional and not yet ready for cross-examination use.

**Where sourcing applies:** Every row of the Timeline sheet — timestamp, event description, conflict notes. Confidence-tier assignments and timezone-conversion methodology follow the Tier 1/2/3 rubric documented below.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## Workflow

### 1. Load Case Context
- Invoke dw-case-brain to load current case folder and prior timeline state
- Confirm case folder path and locate Case Tables.xlsx at root
- Check if Timeline sheet already exists; if so, load existing events for incremental updates

### 2. Source Inventory
Scan case folder for all timestamped evidence:

- **Incident Reports** — text narratives with narrative timestamps, call-in times, arrival times
- **Supplemental Reports** — follow-up investigation timelines
- **Body Worn Camera (BWC)** — start/stop times, key event timestamps from footage
- **Dash Camera Footage** — timestamps of key frames
- **911/Dispatch Records** — CAD logs with precise call times, dispatch times, unit arrival times
- **Cell Site Location Information (CSLI)** — ping timestamps, tower connections
- **Phone Records** — call start/end times, text message timestamps
- **Jail Call Recordings & Transcripts** — recording start times, call duration
- **Witness Statements** — temporal references ("at about 2 PM," "five minutes later")
- **Surveillance/CCTV Footage** — timestamp metadata, key event frames
- **Forensic Examination Reports** — autopsy timestamps, lab receipt times, processing times
- **Social Media Posts** — post timestamps, metadata
- **Financial Transactions** — transaction timestamps
- **GPS/Location Data** — timestamps from tracking devices
- **DMAR Reports** — from dw-transcript-router pipeline output
- **Audit Reports** — from other D&W specialist skills

### 2A. Establish Case Timezone
Before extracting events, establish the case's primary timezone from the incident location:

- **Louisiana cases** — Default timezone is **America/Chicago** (Central Time: CT/CST/CDT)
- **Determine from incident address** — Use location to confirm the correct timezone
- **Normalize all timestamps** — Convert every timestamp to the case timezone for accurate comparison
- **Cross-timezone annotation** — When evidence originates in a different timezone (cell carrier UTC, social media Pacific, etc.), annotate with both original and converted times:
  - Example: "Original: 2024-03-15 18:30:00 UTC → Converted: 2024-03-15 13:30:00 CT (Case Timezone)"
- **DST boundary flag** — If the incident spans a Daylight Saving Time transition, flag affected timestamps:
  - Louisiana DST transition dates (spring forward March; fall back November)
  - Note which timestamps fall in the ambiguous hour
- **Document timezone metadata** — In the Timeline sheet, add a "Timezone/Notes" column capturing the original timezone and conversion method

### 3. Event Extraction
For each source, extract all timestamped events into a structured table:

| Timestamp (Case TZ) | Event | Source | Confidence | Certainty | Notes |
|---|---|---|---|---|---|
| 2024-03-15 14:23:00 CT | 911 call placed | 911 CAD log | Tier 1 | CONFIRMED | Dispatch log timestamp |
| 2024-03-15 14:25:30 CT | First unit dispatched | 911 CAD log | Tier 1 | CONFIRMED | CAD automated entry |
| 2024-03-15 14:32:15 CT | Witness reports subject fled scene | Incident report | Tier 3 | PROBABLE | Officer narrative, 9 min after call |

**Confidence Levels:**
- **High**: Device-generated or institutional logs with machine timestamps
- **Medium**: Institutional records with human-verified timestamps
- **Low**: Witness estimates or narrative approximations

**Certainty Ratings (Barone Discovery Workflow):**
Certainty tracks how confident the defense can be that an event actually occurred as described. This is distinct from Confidence (which tracks timestamp precision). An event can have a precise timestamp (High Confidence) but uncertain occurrence (e.g., an officer's narrative with a CAD timestamp).

- **CONFIRMED**: Multiple independent sources corroborate, or device-generated record with no contradicting evidence. Defense can rely on this event in motions and at trial.
- **PROBABLE**: Single reliable source (Tier 1-2) with no contradiction, or multiple Tier 3-4 sources in agreement. Defense can use but should note single-source limitation.
- **DISPUTED**: Sources disagree on whether or timing of event. Flag for attorney review — may be impeachment material.
- **UNCONFIRMED**: Single Tier 3-4 source only, or based on inference rather than direct observation. Do not rely on without corroboration.
- **ALLEGED**: Assertion by a party with an interest in the outcome (victim, informant, co-defendant). Requires independent verification before defense reliance.

### 4. Conflict Detection & Source Reliability Hierarchy

Identify discrepancies between events at the same timestamp. Flag with color codes:
- **GREEN** — No conflict, single source, or consensus across multiple Tier 1 sources
- **YELLOW** — Minor discrepancy (< 5 min) between sources OR consensus across mixed tiers
- **RED** — Major discrepancy (> 5 min) OR Tier 1 source contradicts Tier 3+ source (impeachment opportunity)

**Source Reliability Hierarchy — Use for conflict assessment:**

**Tier 1 (Highest Reliability) — Device-Generated Timestamps:**
- 911 CAD logs (dispatch call times, unit arrival times)
- Body Worn Camera metadata (start/stop times, key frame timestamps)
- Cell Site Location Information (CSLI) pings (network timestamps)
- GPS/tracking device coordinates (device-generated timestamps)
- Financial transaction logs (bank/merchant system timestamps)
- Digital forensics timestamps (file metadata, system clocks)

**Tier 2 (High Reliability) — Institutional Records:**
- Jail booking system logs (intake times, release times)
- Jail phone system logs (call start/end, duration)
- Lab receipt stamps and processing timelines
- Court minute entries and docket timestamps
- Hospital admission/discharge records
- Coroner/autopsy report timestamps

**Tier 3 (Medium Reliability) — Officer Narratives:**
- Incident reports (written after the fact, subject to recall error)
- Supplemental reports (investigative follow-up, officer recollection)
- Officer testimony about timing
- Detective interview notes

**Tier 4 (Lower Reliability) — Civilian Witness Estimates:**
- Witness statements ("around 2 PM," "about five minutes later")
- Citizen video timestamps (if self-reported, not metadata)
- Social media post times (user-generated, subject to clock drift)

**Conflict Resolution Note:**
This hierarchy does NOT automatically resolve conflicts. Instead, it **informs defense strategy**: When a Tier 1 source (e.g., CSLI ping at 14:32:00) contradicts a Tier 3 source (officer narrative: "subject was on scene at 14:35"), highlight the conflict in RED and note the impeachment opportunity for cross-examination.

### 5. Timeline Outputs
#### 5A. Chronological Master Timeline (Spreadsheet)
Populate the "Timeline" sheet in Case Tables.xlsx with columns:
- Timestamp (Case Timezone)
- Event Description
- Source (with citation)
- Source Tier
- Confidence Level
- Certainty (CONFIRMED / PROBABLE / DISPUTED / UNCONFIRMED / ALLEGED)
- Conflict Status (GREEN/YELLOW/RED)
- Defense Notes / Impeachment Opportunity
- Link to Source Document

#### 5B. Conflict Report
Generate a summary document listing all RED and YELLOW conflicts:
- Event & timestamp
- Conflicting sources and their claims
- Source tier comparison
- Defense implications (e.g., "Officer narrative contradicted by CSLI — potential impeachment")

#### 5C. Defense Strategy Brief
For each RED conflict, propose a cross-examination angle:
- "CSLI shows subject at Tower A at 14:32, but officer states subject was at scene (5 miles away) at 14:30 — timeline impossible, suggests memory error or motive to misstate"

#### 5D. Visual Timeline (Interactive & Static)
Triggered by: "visual timeline," "interactive timeline," "timeline chart," or "show me the timeline"

**Interactive HTML Timeline:**
- Generate HTML page using D3.js or similar visualization library via frontend-design skill
- **Features:**
  - Zoomable/scrollable timeline (hourly, minute, second views)
  - Color-coded events: GREEN (no conflict), YELLOW (minor discrepancy), RED (major conflict)
  - Hover tooltips showing event description, source, and confidence level
  - Click-to-expand: Reveals full source citation and conflict details
  - Legend showing Tier 1–4 source icons
  - Responsive design for desktop, tablet, mobile
- **Output:** index.html + associated CSS/JS, deployable locally or via frontend-design skill

**Static Mermaid Timeline:**
For simpler visualization needs (meeting prep, discovery response, etc.):
- Generate timeline.mermaid file with Mermaid syntax
- Color blocks for conflict status
- Embeddable in markdown documents, GitHub, Confluence
- Example format:
```
timeline
  title Case Timeline: State v. Defendant
  section Early Response
    14:23 : 911 Call Placed : CAD Log (Tier 1)
    14:25 : Unit Dispatched : CAD Log (Tier 1)
  section Arrival & Scene
    14:32 : CONFLICT - Officer: Subject on scene vs. CSLI: Tower A (5 mi away)
    14:35 : Officer Narrative: Subject fled
```

#### 5E. Incremental Updates (Living Document)
When new evidence arrives (supplemental reports, late-discovered audio, etc.):
1. Load existing Timeline sheet from Case Tables.xlsx
2. Extract timestamps from new source
3. Merge into chronological order
4. Re-run conflict detection
5. Update color codes in Timeline sheet
6. Generate conflict summary showing NEW discrepancies
7. Regenerate visual timeline if requested

---

## Integration
**Reads From:**
- Case Tables.xlsx (Timeline sheet if it exists)
- All case folder PDFs, reports, transcripts, and media
- dw-case-brain (current case context)

**Writes To:**
- Case Tables.xlsx → Timeline sheet (chronological events, conflict status)
- Conflict Report PDF (discovery response, motion support)
- Defense Strategy Brief (trial prep, cross-exam outline)
- index.html + assets (interactive timeline visualization)
- timeline.mermaid (static visual for markdown/documents)

**Feeds Into:**
- dw-cross-exam-architect (for impeachment planning)
- dw-pretrial-motion-library (for suppression/Giglio motions)
- dw-trial-notebook-builder (for trial chronology exhibits)
- dw-discovery-compliance-monitor (for discovery response)

---

## Core Rules

### Source Citation
Every timestamp must be traced to its original source with full citation:
- Document name, page number, line number, exhibit
- For CAD logs: log entry ID, dispatcher name if available
- For BWC: file name, start time, key frame timecode
- For witness statements: witness name, date of statement, specific quote if narrative reference

### Timestamp Precision
Record timestamps at their native precision:
- CAD logs: HH:MM:SS (seconds)
- BWC metadata: HH:MM:SS (seconds)
- Witness narrative: "around 2 PM" (approximate, flag as Tier 4)
- Do NOT add false precision (e.g., don't claim a witness said "2:15:30 PM")

### Timezone & Time Format
- **Establish case timezone at Step 2A** — Default to America/Chicago (CT) for Louisiana
- All timestamps normalized to case timezone before comparison
- Cross-timezone evidence annotated with both original and converted times
- Flag DST boundaries if incident spans transition dates
- Format: YYYY-MM-DD HH:MM:SS TZ (e.g., 2024-03-15 14:23:00 CT)
- Include Timezone/Notes column in Timeline sheet documenting conversions

### Conflict Resolution Strategy
Use the Source Reliability Hierarchy (Tier 1–4) to assess conflicts:
- Tier 1 vs. Tier 3+ discrepancy = RED flag, likely impeachment opportunity
- Tier 2 vs. Tier 3 discrepancy = YELLOW, minor timing issues
- Multiple Tier 1 sources in consensus = GREEN, high confidence
- Never "resolve" a conflict by deleting one side; instead, preserve both and flag the discrepancy for attorney review

### Defense Tool Orientation
The timeline is built to serve defense strategy:
- Highlight contradictions between prosecution sources (device data vs. officer narrative)
- Identify timing impossibilities (alibi verification, impossible distances)
- Flag witness perception errors and officer recall gaps
- Support cross-examination impeachment
- Preserve all versions of events for discovery and trial use

---

## File Size Target
Keep this skill document under 25KB to maintain searchability and performance.

---

**Last Updated:** Version 1.0 | Timezone handling (Step 2A), Source Reliability Hierarchy (Step 4), Visual Timeline expansion (Step 5D)
