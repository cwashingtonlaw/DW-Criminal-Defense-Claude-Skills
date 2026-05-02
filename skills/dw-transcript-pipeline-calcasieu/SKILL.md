---
name: dw-transcript-pipeline-calcasieu
description: >
  JusticeText-based transcription pipeline for Calcasieu Parish cases at Daniels & Washington.
  ALWAYS invoke for "JusticeText pipeline," "Calcasieu transcription," "upload to JusticeText,"
  "transcribe Calcasieu media," "Calcasieu DMAR," or when dw-transcript-router routes a Calcasieu
  case here. Handles the full workflow: folder scan → JusticeText upload → transcription →
  TranscriptPad import → Defense Media Analysis Report. Adds Rev-equivalent AI analysis features
  (multi-file cross-referencing, inconsistency detection, chronological timeline construction,
  document-vs-media comparison) via Claude analysis layer on top of JusticeText transcripts.
  Produces a standardized Defense Media Analysis Report (.docx) identical in schema to
  dw-transcript-pipeline-rev output. This skill is invoked by dw-transcript-router for Calcasieu
  Parish cases.
---

# DW Transcript Pipeline — Calcasieu Parish (JusticeText)

**Platform**: JusticeText (platform.justicetext.com)
**Parish**: Calcasieu only (routed by dw-transcript-router)
**Output**: Defense Media Analysis Report (.docx) + TranscriptPad case

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any audio or video files for transcription (interrogations, jail calls, interviews, body-worn camera, dashcam, 911 calls, civilian video), do not begin upload to JusticeText yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional media for this batch? I'll start the JusticeText upload only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. Mid-batch additions cause partial uploads, broken case-tab ordering on JusticeText, and DMAR sequencing issues when the late files come back out of order.

---

### Source Citation Mandate

Every factual assertion in the Defense Media Analysis Report (DMAR) must trace back to a specific source recording and timestamp. The DMAR is the foundation for cross-examination, motions, and trial strategy — every inconsistency, key statement, Miranda event, and timeline entry must be verifiable by replaying the exact moment in the recording.

**Citation format:** Cite the recording filename, timestamp, and speaker. Examples:
- `(Interview_Client_03152026.mp4, Timestamp 00:15:32 — Det. Smith)`
- `(BWC_OfficerJohnson_03152026.mp4, Timestamp 00:02:14 — Officer Johnson)`
- `(JailCall_03162026_1430.mp3, Timestamp 04:22 — Client to "Mom")`
- `(911_Call_03152026.wav, Timestamp 00:01:45 — Caller)`
- `(CCTV_MainSt_03152026.mp4, Timestamp 22:10:45)`

**Multiple-source rule:** When different recordings capture the same event, cite all of them. Cross-referenced timestamps across recordings are powerful evidence of timeline accuracy or contradiction.

**Unsourced assertions:** If a DMAR finding cannot be tied to a specific recording and timestamp, mark it `[UNSOURCED — VERIFY WITH RECORDING]`. Never present an unsourced finding as established without flagging it.

**Where sourcing applies:** All factual content in the DMAR — key statements, inconsistencies, Miranda events, timeline entries, and cross-reference findings. Analytical conclusions about defense strategy implications do not require timestamp citations but should reference the underlying findings.

---

## Bundled Resources

This skill includes the following reference documentation and automation tools:

### References

1. **justicetext-architecture.md** (`references/`)
   - JusticeText API endpoints and authentication mechanisms
   - AWS Cognito configuration and S3 bucket mappings
   - File upload flow documentation
   - Future automation paths for API-based uploads

2. **transcriptpad-database.md** (`references/`)
   - TranscriptPad `.tracase` SQLite Core Data schema
   - Entity types, table relationships, and primary key management
   - Timestamp rendering mechanics (ZTIMECODEMS field behavior)
   - Common database operations and SQL examples

### Scripts

3. **transcriptpad-timestamp-fix.py** (`scripts/`)
   - Parses JusticeText .txt transcript exports with [MM:SS] or [HH:MM:SS] timestamps
   - Converts to milliseconds for TranscriptPad ZTIMECODEMS field
   - Reformats text as `:SS - Speaker - Content` matching TranscriptPad conventions
   - Updates both evidence folder and iCloud `.tracase` database locations
   - Usage: Configure EVIDENCE_PATH, CASE_PATHS, and TRANSCRIPT_FILES mapping, then run the script

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## Pipeline Phases

### Phase 1: Folder Scan

Identical to the original dw-transcript-pipeline Phase 1. Scan the client folder for media files.

#### Step 1.1 — Get the target folder
The attorney should have the client folder selected in Cowork. Folder name follows `lastname, firstname` convention.

#### Step 1.2 — Scan for media files
Recursively scan all subfolders. Collect files with these extensions (case-insensitive):

- **Video**: `.mp4`, `.mov`, `.avi`, `.wmv`, `.mkv`, `.flv`, `.webm`, `.m4v`, `.mpg`, `.mpeg`, `.3gp`, `.ts`, `.vob`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.m4a`, `.ogg`, `.flac`, `.wma`, `.aiff`, `.aif`, `.opus`, `.amr`

**Skip files whose name ends with `_TRANSCRIBED`.** These were processed in a prior run.

#### Step 1.3 — Detect duplicates
Flag files with the same base name across different paths or sizes. Present duplicates and ask attorney which to include.

#### Step 1.4 — Present file list and confirm
Show summary table: client folder, total files, each file (name, subfolder, size, type), skipped files, excluded duplicates. Confirm before proceeding. Stop if zero unprocessed files.

---

### Phase 2: JusticeText Upload & Transcription

#### Step 2.1 — Navigate to JusticeText
Navigate to `https://platform.justicetext.com`. Confirm attorney is logged in.

#### Step 2.2 — Find or create workspace
Look for workspace matching `lastname, firstname`. Create if not found.

#### Step 2.3 — Upload media files (ATTORNEY ACTION)
Ask which shared drive the files are on. For Calcasieu:

> I've opened the **[client name]** workspace in JusticeText. Please upload the [N] media files:
>
> 1. Click the purple **"Upload files"** button (top right)
> 2. Click **"Media, PDF"**
> 3. In the upload dialog, click **"Google Drive"**
> 4. Navigate to: **Shared drives → Calcasieu PDO Files → [client folder] → 01 - Trial Notebook → 05 - Evidence**
> 5. Select the files listed below
>
> [List files from Phase 1, grouped by subfolder]

Wait for attorney confirmation.

#### Step 2.4 — Verify upload and transcription status
Scan workspace file list. Confirm each file appears and check status (Uploading → Transcribing → Ready).

#### Step 2.5 — Monitor progress
If transcription is running, inform attorney of expected timeline (15–45 min per hour of audio).

---

### Phase 2.5: Transcript Review & Speaker Labeling (ATTORNEY ACTION)

> Transcription is complete for all [N] files. Before I download, please review in JusticeText:
>
> 1. **Label speakers** — Assign real names (e.g., "Det. Jones," "Defendant")
> 2. **Fix errors** — Correct names, addresses, dates
> 3. **Add annotations** — Flag important moments
>
> Let me know when done.

Wait for confirmation.

---

### Phase 3: Download Transcripts

Download PDF and TXT transcripts from JusticeText for each file. Place alongside source media in the evidence folder. Verify download sizes (flag any under 1KB as potentially empty).

---

### Phase 4: TranscriptPad Import

Follow the original pipeline's Phase 4 workflow:
1. Find or create TranscriptPad case
2. Back up `.tracase` package
3. Stage transcripts in Inbox
4. Import via Add menu (AppleScript or manual fallback)
5. Copy media into case and link in database (SQLite)
6. Fix timestamps (Python + SQLite)
7. Sync both case locations
8. Rename originals with `_TRANSCRIBED` suffix

---

### Phase 5: Defense Media Analysis Report (Rev-Equivalent Features)

This phase adds Rev-equivalent AI analysis capabilities to JusticeText transcripts using Claude's analytical layer. The output is a standardized **Defense Media Analysis Report (DMAR)** as a `.docx` file.

**Claude reads all downloaded TXT transcripts from Phase 3 and performs the following analysis modules.**

#### Module A — Multi-File Cross-Reference Analysis
*Replicates Rev's Multi-File Insights capability*

For each transcript, extract and compare:
1. **Named entities**: Officers, witnesses, locations, vehicles, weapons, drugs, amounts
2. **Temporal references**: Dates, times, durations, sequences ("before," "after," "then")
3. **Factual claims**: What each speaker says happened, in what order

Cross-reference across all transcripts to identify:
- **Contradictions**: Where Speaker A in File 1 says X but Speaker B in File 2 says Y about the same event
- **Corroborations**: Where multiple sources confirm the same fact
- **Gaps**: Events referenced but not covered by any recording
- **Sequence conflicts**: Where the chronological order of events differs between accounts

Output format (in DMAR Section 3):
```
CROSS-REFERENCE FINDING [CR-001]
Files: [File 1 name] @ [timestamp] vs. [File 2 name] @ [timestamp]
Type: CONTRADICTION / CORROBORATION / GAP / SEQUENCE CONFLICT
Speaker 1: [Name] — "[quoted claim]"
Speaker 2: [Name] — "[quoted claim]"
Defense Significance: [How this helps the defense theory]
Cross-Exam Seed: [One-line question this finding supports]
```

#### Module B — Document-vs-Media Comparison
*Replicates Rev's ability to compare PDFs/documents against transcripts*

If police reports, incident reports, or other written documents exist in the client folder:
1. Read the written reports (PDF/DOCX via file reading skills)
2. Compare factual claims in written reports against transcript content
3. Flag every discrepancy between what an officer wrote and what the recording shows

Output format (in DMAR Section 4):
```
REPORT-VS-RECORDING DISCREPANCY [RR-001]
Document: [Report name, page, paragraph]
Recording: [File name] @ [timestamp]
Report says: "[quoted from report]"
Recording shows: "[quoted from transcript]"
Severity: CRITICAL / SIGNIFICANT / MINOR
Defense Use: [Impeachment, suppression, Brady, etc.]
```

#### Module C — Chronological Master Timeline
*Replicates Rev's timeline construction capability*

Build a unified timeline from ALL transcripts and documents:
1. Extract every timestamped event from every source
2. Normalize to a single clock (resolve timezone/format differences)
3. Interleave events from all sources into one chronological sequence
4. Flag timeline gaps (periods with no coverage from any source)
5. Flag overlapping contradictions (two sources describing different events at the same time)

Output format (in DMAR Section 5):
```
TIME | SOURCE | EVENT | NOTES
[HH:MM:SS] | [File name] @ [media timestamp] | [What happened] | [Any flags]
```

#### Module D — Speaker Behavior Analysis
*Replicates Rev's sentiment/behavioral analysis*

For each identified speaker across all transcripts:
1. **Speech patterns**: Hesitation markers, corrections, evasions
2. **Emotional shifts**: Changes in tone described by context (raised voice, crying, silence)
3. **Consistency**: Does this speaker's account stay consistent across multiple recordings?
4. **Power dynamics**: Who controls the conversation? Interruptions, redirections, topic changes

Output as narrative paragraphs in DMAR Section 6, organized by speaker.

---

### Phase 6: Generate the DMAR (.docx)

Use the `docx` skill to produce the Defense Media Analysis Report. **This format is identical to the DMAR produced by dw-transcript-pipeline-rev.**

#### DMAR Structure

```
DEFENSE MEDIA ANALYSIS REPORT
[Client Name] | [Docket #] | [Parish: Calcasieu]
Transcription Platform: JusticeText
Analysis Date: [Date]
Prepared by: Claude AI — Attorney Work Product / Privileged

SECTION 1: EVIDENCE INVENTORY
  1.1 Media Files Processed (table: filename, type, duration, source folder)
  1.2 Written Documents Reviewed (table: filename, type, pages, source)
  1.3 Processing Summary (total files, total duration, transcription platform)

SECTION 2: TRANSCRIPT SUMMARIES
  For each transcript:
    2.X.1 File: [name] | Duration: [time] | Speakers: [list]
    2.X.2 Synopsis (3–5 sentence summary)
    2.X.3 Key Moments (timestamp + event + defense relevance)
    2.X.4 Miranda/Rights Events (if applicable — timestamp + what was said)
    2.X.5 Interrogation Technique Flags (if applicable — see Module E below)

SECTION 3: CROSS-REFERENCE ANALYSIS
  All CR-### findings from Module A

SECTION 4: REPORT-VS-RECORDING DISCREPANCIES
  All RR-### findings from Module B
  (Empty section with "No written reports available for comparison" if none exist)

SECTION 5: MASTER TIMELINE
  Unified chronological timeline from Module C

SECTION 6: SPEAKER BEHAVIOR ANALYSIS
  Narrative analysis from Module D, organized by speaker

SECTION 7: DEFENSE INTELLIGENCE SUMMARY
  7.1 Strongest Defense Findings (ranked by impact)
  7.2 Recommended Skill Invocations:
      - "Run dw-confession-interrogation-auditor on [file]" (if interrogation detected)
      - "Run dw-video-evidence-auditor on [file]" (if BWC/video gaps found)
      - "Build cross-exam for [officer] using DMAR findings" (for each officer)
  7.3 Outstanding Questions (what the recordings don't answer)
  7.4 Potential Brady/Giglio Issues (if any detected)

APPENDIX A: FILE HASH LOG
  SHA-256 hash of each source media file for chain of custody

APPENDIX B: ANALYSIS METHODOLOGY
  Statement that analysis was performed by Claude AI on [platform] transcripts.
  Attorney verification required before any filing or client communication.
  Louisiana Act 250 / ABA Opinion 512 compliance note.
```

Save to the client's evidence folder as:
`DMAR — [LastName, FirstName] — [Date].docx`

#### Update Case Brain

Write to `dw-case-brain`:
> Transcription pipeline (Calcasieu/JusticeText) completed for [client name]: [N] media files
> processed. DMAR generated with [X] cross-reference findings, [Y] report discrepancies,
> [Z] defense-significant moments. Recommended follow-up: [list recommended skill invocations].

---

## JusticeText-Native Features (Use Directly, Don't Replicate)

These JusticeText features should be used natively — Claude does NOT need to replicate them:

- **MirandaAI**: JusticeText's built-in AI for Miranda detection, Reid technique analysis, leading question identification. The attorney should use MirandaAI within the JusticeText platform directly.
- **Key Event Detection**: JusticeText auto-flags arrests, traffic stops, sobriety tests.
- **Presentation Mode**: Synchronized video + transcript display for trial. Use within JusticeText.

The DMAR **supplements** these native features with cross-file analysis that JusticeText cannot perform (it analyzes files individually, not across the full evidence set).

---

## Quick Reference

| Step | Platform | Method | Who |
|------|----------|--------|-----|
| Scan folder | Local | Filesystem | **Claude** |
| Upload media | JusticeText | Google Drive picker | **Attorney** |
| Monitor transcription | JusticeText | Claude in Chrome | **Claude** |
| Review + label speakers | JusticeText | Manual | **Attorney** |
| Download transcripts | JusticeText | Claude in Chrome | **Claude** |
| Import to TranscriptPad | TranscriptPad | AppleScript + SQLite | **Claude** |
| Defense Media Analysis | Local | Claude analysis on TXT files | **Claude** |
| Generate DMAR | Local | docx skill | **Claude** |
| Update Case Brain | DEVONthink | dw-case-brain | **Claude** |
| Verify rendering | TranscriptPad | Manual click-through | **Attorney** |

---

## Error Handling

Inherits all error handling from the original dw-transcript-pipeline, plus:

- **Empty transcripts**: If a TXT file contains only headers and no transcript content, flag to attorney and exclude from DMAR analysis
- **Missing speaker labels**: If speakers are still "Speaker 1", "Speaker 2" in the TXT, warn attorney that DMAR speaker analysis will be generic — recommend going back to JusticeText to label speakers first
- **No written reports**: Module B (document comparison) produces an empty section with a note; this is normal for early-stage discovery
- **Extremely long recordings (4+ hours)**: Process DMAR analysis in chunks — summarize each hour, then synthesize cross-file analysis across chunks


Follow shared protocols for output paths (see Step 0.5).
