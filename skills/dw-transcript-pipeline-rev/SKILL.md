---
name: dw-transcript-pipeline-rev
description: >
  Rev.com-based transcription pipeline for all non-Calcasieu Parish cases at Daniels & Washington.
  Handles the full workflow: folder scan → Rev upload → transcription → TranscriptPad import →
  Defense Media Analysis Report. Adds MirandaAI-equivalent defense analysis features (Miranda rights
  detection, Reid technique identification, leading question flagging, coercion indicators, key
  event detection, interrogation technique analysis) via Claude analysis layer on top of Rev
  transcripts. Produces a standardized Defense Media Analysis Report (.docx) identical in schema
  to dw-transcript-pipeline-calcasieu output. This skill is invoked by dw-transcript-router for
  all non-Calcasieu cases. Direct triggers: "Rev pipeline," "Rev transcription," "upload to Rev,"
  or when dw-transcript-router routes a non-Calcasieu case here.
---

# DW Transcript Pipeline — All Parishes Except Calcasieu (Rev.com)

**Platform**: Rev.com (rev.com)
**Parishes**: All except Calcasieu (routed by dw-transcript-router)
**Output**: Defense Media Analysis Report (.docx) + TranscriptPad case

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

## Pipeline Phases

### Phase 1: Folder Scan

Identical to Calcasieu pipeline Phase 1.

#### Step 1.1 — Get the target folder
Attorney should have client folder selected. Folder name follows `lastname, firstname` convention.

#### Step 1.2 — Scan for media files
Recursively scan all subfolders. Collect files with these extensions (case-insensitive):

- **Video**: `.mp4`, `.mov`, `.avi`, `.wmv`, `.mkv`, `.flv`, `.webm`, `.m4v`, `.mpg`, `.mpeg`, `.3gp`, `.ts`, `.vob`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.m4a`, `.ogg`, `.flac`, `.wma`, `.aiff`, `.aif`, `.opus`, `.amr`

**Skip files whose name ends with `_TRANSCRIBED`.** These were processed in a prior run.

#### Step 1.3 — Detect duplicates
Flag files with same base name across different paths or sizes. Present and ask attorney which to include.

#### Step 1.4 — Present file list and confirm
Show summary table. Confirm before proceeding. Stop if zero unprocessed files.

#### Step 1.5 — Classify evidence types
Before upload, classify each file for downstream analysis:

| Classification | Examples | Analysis Modules Triggered |
|----------------|----------|---------------------------|
| `INTERROGATION` | Custodial interviews, detective questioning | E (MirandaAI), F (Interrogation) |
| `BODY_CAM` | BWC footage, officer-worn cameras | G (Key Events), H (Use of Force) |
| `DASH_CAM` | In-car camera footage | G (Key Events) |
| `JAIL_CALL` | Inmate phone recordings | I (Jail Call) |
| `911_CALL` | Emergency dispatch recordings | G (Key Events) |
| `WITNESS_INTERVIEW` | Non-custodial witness statements | E (partial), D (Speaker) |
| `SURVEILLANCE` | CCTV, security camera footage | C (Timeline) |
| `OTHER` | Miscellaneous audio/video | C (Timeline), D (Speaker) |

Classification is based on filename patterns, subfolder names, and attorney input. Ask if uncertain.

---

### Phase 2: Rev.com Upload & Transcription

#### Step 2.1 — Determine transcription tier

Ask the attorney:

> I've scanned [N] media files. Which Rev transcription tier should I use?
>
> - **AI Transcription** ($0.25/min) — 96%+ accuracy, results in ~5 minutes. Good for initial review.
> - **Human Transcription** ($1.99/min) — 99%+ accuracy, 12-hour turnaround. Better for court-critical recordings.
> - **Ready to Certify** — 99.6% accuracy, court-formatted with jurisdiction cover page. Use for transcripts you'll file.
> - **Mixed** — AI for bulk, Human for the [N] most critical files. (Recommended for most cases.)

If attorney chooses "Mixed," ask which files should get human transcription.

#### Step 2.2 — Navigate to Rev.com
Navigate to `https://www.rev.com`. Confirm attorney is logged in. If not, ask them to log in.

#### Step 2.3 — Upload media files (ATTORNEY ACTION)

> Please upload the [N] media files to Rev:
>
> 1. Go to **rev.com** → **Order Transcription** (or "New Order" if on dashboard)
> 2. Select **[AI Transcription / Human Transcription / Ready to Certify]** as discussed
> 3. Click **Upload Files** and select from:
>    - **Google Drive**: Navigate to **Shared drives → [PARISH] PDO Files → [client folder] → 01 - Trial Notebook → 05 - Evidence**
>    - **Local/NAS**: Browse to the evidence folder
> 4. Upload these files:
>
> [List files from Phase 1, grouped by subfolder]
>
> **For Human/Ready to Certify orders**: Select **Verbatim** transcription style and enable **Timestamps** (every 2 minutes or speaker change).
>
> Let me know when upload is complete and you have the order confirmation.

Wait for attorney confirmation.

#### Step 2.4 — Monitor transcription status

- **AI transcription**: Check back in 5–15 minutes
- **Human transcription**: Check back in 2–12 hours depending on rush tier
- **Ready to Certify**: Check back in 1–3 business days

Ask attorney to share the Rev order/project URL so Claude can check status via Chrome.

#### Step 2.5 — Download transcripts

Once transcription is complete:
1. Download all transcripts in **DOCX** and **TXT** format (both needed)
2. For AI transcripts, also download **JSON** if available (contains word-level timestamps and confidence scores)
3. Place transcripts alongside source media in the evidence folder
4. Verify download sizes (flag any under 1KB)

---

### Phase 2.5: Transcript Review & Speaker Labeling

Rev's speaker diarization uses "Speaker 1," "Speaker 2" labels by default. The attorney must relabel:

> Transcription is complete for all [N] files. Before I run analysis, please review the transcripts:
>
> 1. **Open each transcript** in Rev's editor (click the transcript in your Rev dashboard)
> 2. **Label speakers** — Click on "Speaker 1" labels and assign real names
> 3. **Fix errors** — Correct any transcription mistakes, especially names, addresses, dates
> 4. **Re-download** the corrected transcripts (DOCX + TXT)
>
> For Human/Ready to Certify transcripts, the speakers may already be labeled if you provided a speaker list with the order.

Wait for confirmation and updated transcript files.

---

### Phase 3: TranscriptPad Import

Identical to Calcasieu pipeline Phase 4:
1. Find or create TranscriptPad case
2. Back up `.tracase` package
3. Stage transcripts in Inbox
4. Import via Add menu
5. Copy media into case and link in database (SQLite)
6. Fix timestamps (Python + SQLite — adjust regex for Rev's timestamp format)
7. Sync both case locations
8. Rename originals with `_TRANSCRIBED` suffix

**Rev Timestamp Format Note**: Rev TXT exports use `[HH:MM:SS]` or `(HH:MM:SS)` format depending on settings. The timestamp fix script regex should handle both Rev and JusticeText formats:
```
\[?(\d{1,2}:\d{2}(?::\d{2})?)\]?\s+(.+?):\s*\n(.*?)(?=\n\[?\d{1,2}:\d{2}|\Z)
```

---

### Phase 4: Defense Media Analysis Report (MirandaAI-Equivalent Features)

This phase adds MirandaAI-equivalent criminal defense analysis capabilities to Rev transcripts using Claude's analytical layer. **Claude reads all downloaded TXT transcripts and performs the analysis modules below.**

The output is a standardized **Defense Media Analysis Report (DMAR)** — identical in structure to the DMAR produced by `dw-transcript-pipeline-calcasieu`.

---

#### Module A — Multi-File Cross-Reference Analysis

For each transcript, extract and compare:
1. **Named entities**: Officers, witnesses, locations, vehicles, weapons, drugs, amounts
2. **Temporal references**: Dates, times, durations, sequences
3. **Factual claims**: What each speaker says happened, in what order

Cross-reference across all transcripts to identify:
- **Contradictions**: Where accounts conflict about the same event
- **Corroborations**: Where multiple sources confirm the same fact
- **Gaps**: Events referenced but not covered by any recording
- **Sequence conflicts**: Where chronological order differs between accounts

Output format (DMAR Section 3):
```
CROSS-REFERENCE FINDING [CR-001]
Files: [File 1 name] @ [timestamp] vs. [File 2 name] @ [timestamp]
Type: CONTRADICTION / CORROBORATION / GAP / SEQUENCE CONFLICT
Speaker 1: [Name] — "[quoted claim]"
Speaker 2: [Name] — "[quoted claim]"
Defense Significance: [How this helps the defense]
Cross-Exam Seed: [One-line question this finding supports]
```

---

#### Module B — Document-vs-Media Comparison

If police reports, incident reports, or other written documents exist in the client folder:
1. Read written reports (PDF/DOCX via file reading skills)
2. Compare factual claims against transcript content
3. Flag every discrepancy

Output format (DMAR Section 4):
```
REPORT-VS-RECORDING DISCREPANCY [RR-001]
Document: [Report name, page, paragraph]
Recording: [File name] @ [timestamp]
Report says: "[quoted from report]"
Recording shows: "[quoted from transcript]"
Severity: CRITICAL / SIGNIFICANT / MINOR
Defense Use: [Impeachment, suppression, Brady, etc.]
```

---

#### Module C — Chronological Master Timeline

Build unified timeline from ALL transcripts and documents:
1. Extract every timestamped event
2. Normalize to single clock
3. Interleave into one chronological sequence
4. Flag gaps and overlapping contradictions

Output format (DMAR Section 5):
```
TIME | SOURCE | EVENT | NOTES
[HH:MM:SS] | [File name] @ [media timestamp] | [What happened] | [Flags]
```

---

#### Module D — Speaker Behavior Analysis

For each identified speaker:
1. **Speech patterns**: Hesitation, corrections, evasions
2. **Emotional shifts**: Changes described by context
3. **Consistency**: Does account stay consistent across recordings?
4. **Power dynamics**: Who controls conversation? Interruptions, redirections

Output as narrative paragraphs in DMAR Section 6.

---

#### Module E — Miranda Rights & Constitutional Events Detection
*REPLICATES MirandaAI's core Miranda detection capability*

**This module runs on ALL transcripts but produces detailed output only for files classified as `INTERROGATION` or `WITNESS_INTERVIEW`.**

Scan every transcript for the following constitutional event categories:

##### E.1 — Miranda Rights Analysis

Search for any variation of Miranda warnings. Flag:

| Finding | What to Look For | Severity |
|---------|-----------------|----------|
| `MIRANDA-COMPLETE` | All four warnings given clearly | INFO |
| `MIRANDA-PARTIAL` | Some warnings given, others omitted | CRITICAL |
| `MIRANDA-ABSENT` | No Miranda warnings in custodial interrogation | CRITICAL |
| `MIRANDA-TIMING` | Warnings given AFTER substantive questioning began | CRITICAL |
| `MIRANDA-WAIVER-ORAL` | Verbal waiver without written form | SIGNIFICANT |
| `MIRANDA-WAIVER-EQUIVOCAL` | Ambiguous waiver ("I guess," "sure, whatever") | CRITICAL |
| `MIRANDA-INVOCATION` | Suspect invokes right to silence or counsel | CRITICAL |
| `MIRANDA-INVOCATION-IGNORED` | Questioning continues after invocation | CRITICAL |
| `MIRANDA-RE-INITIATION` | Police re-approach after invocation | SIGNIFICANT |

The four Miranda components to check:
1. Right to remain silent
2. Anything said can be used against you
3. Right to an attorney
4. If you cannot afford an attorney, one will be appointed

For each finding, record:
```
MIRANDA EVENT [ME-001]
File: [name] @ [timestamp]
Type: [from table above]
Speaker: [who gave/received warnings]
Verbatim: "[exact words from transcript]"
Analysis: [What's missing, ambiguous, or problematic]
Legal Significance: [Which Miranda prong is affected]
Suppress?: [Yes/No/Maybe — with brief reasoning]
```

##### E.2 — Right to Counsel Invocations

Specifically scan for any statement that could constitute an invocation of the right to counsel, including ambiguous statements. MirandaAI's key insight is that invocations are often subtle:

**Clear invocations**: "I want a lawyer," "I need to talk to my attorney," "Get me a lawyer"
**Ambiguous invocations** (Edwards v. Arizona analysis required):
- "Maybe I should talk to a lawyer"
- "Do I need a lawyer?"
- "Can I call my attorney?"
- "I think I want a lawyer"
- "My mama told me to get a lawyer"
- "How do I get a public defender?"

Flag ALL of these. For ambiguous invocations, note that under Edwards v. Arizona and Louisiana jurisprudence, police should have stopped questioning and clarified.

##### E.3 — Custody Determination Markers

Flag statements and circumstances indicating whether the suspect was "in custody" for Miranda purposes:
- Told they are free to leave (or not told)
- Door locked/unlocked
- Handcuffs on/off
- Transport in police vehicle
- Location (police station, home, street, vehicle)
- Duration of encounter
- Number of officers present
- Tone of questioning (accusatory vs. investigative)

---

#### Module F — Interrogation Technique Analysis
*REPLICATES MirandaAI's Reid Technique and coercion detection*

**Runs only on files classified as `INTERROGATION`.**

Scan for the following interrogation techniques and flag each instance:

##### F.1 — Reid Technique Components

| Technique | What to Look For | Flag Level |
|-----------|-----------------|------------|
| **Positive Confrontation** | "We know you did this," "The evidence shows..." | SIGNIFICANT |
| **Theme Development** | Minimizing moral blame, offering justifications | SIGNIFICANT |
| **Handling Denials** | Cutting off denials, not allowing suspect to speak | CRITICAL |
| **Overcoming Objections** | Dismissing suspect's reasons for innocence | SIGNIFICANT |
| **Retention of Attention** | Physical proximity, eye contact demands, touching | SIGNIFICANT |
| **Handling Passive Mood** | Crying, withdrawal — detective intensifies | SIGNIFICANT |
| **Alternative Question** | Offering two choices, both incriminating | CRITICAL |
| **Oral Confession Development** | Leading suspect to provide details | SIGNIFICANT |
| **Written Confession** | Moving to written/recorded statement | INFO |

##### F.2 — Coercion Indicators

| Indicator | What to Look For | Flag Level |
|-----------|-----------------|------------|
| **False Evidence Ploy** | "Your fingerprints were found," "Your DNA matched" (if potentially false) | CRITICAL |
| **Implicit Promises** | "Things will go better if you cooperate," "Help yourself out" | CRITICAL |
| **Explicit Promises** | "I'll talk to the DA," "You'll go home tonight" | CRITICAL |
| **Threats** | "You'll never see your kids," "You're looking at life" | CRITICAL |
| **Minimization** | "It was an accident," "Anyone would have done the same" | SIGNIFICANT |
| **Maximization** | "This is the worst thing I've ever seen," "You're going down for murder" | SIGNIFICANT |
| **Sleep/Food/Bathroom Deprivation** | Long duration without breaks, requests denied | CRITICAL |
| **Isolation Pressure** | "Nobody can help you but yourself," "Your co-defendant is talking" | SIGNIFICANT |
| **Deception About Law** | Misrepresenting charges, penalties, or legal rights | CRITICAL |
| **Fatigue Exploitation** | Increased pressure during late hours or after long wait | SIGNIFICANT |

##### F.3 — False Confession Risk Factors

Flag the presence of any recognized false confession risk factors:
- Juvenile suspect (under 18)
- Intellectual disability indicators (comprehension problems, acquiescence)
- Mental illness indicators (delusions, confusion, disorientation)
- Substance intoxication/withdrawal
- Interrogation duration exceeding 2 hours (flag), 4 hours (critical), 6+ hours (extreme)
- Suspect provides details that were fed by detective (contamination)
- Statement contains implausible or impossible claims
- Suspect changes story to match detective's theory

For each finding:
```
INTERROGATION TECHNIQUE [IT-001]
File: [name] @ [timestamp range]
Category: REID TECHNIQUE / COERCION / FALSE CONFESSION RISK
Specific Technique: [from tables above]
Flag Level: CRITICAL / SIGNIFICANT / INFO
Detective: [name if known]
Verbatim Exchange:
  DETECTIVE @ [timestamp]: "[what detective said]"
  SUSPECT @ [timestamp]: "[suspect's response]"
Analysis: [Why this is significant]
Legal Framework: [Relevant case law — e.g., State v. Blank, Edwards, etc.]
Suppress?: [Yes/No/Maybe]
Cross-Exam Seed: [One-line impeachment question for this detective]
```

---

#### Module G — Key Event Detection
*REPLICATES MirandaAI's automatic key event flagging*

**Runs on all file types.** Automatically detect and timestamp these event categories:

| Event Type | Detection Patterns |
|------------|-------------------|
| **Traffic Stop** | "License and registration," "Do you know why I pulled you over," engine/siren sounds described |
| **Arrest** | "You're under arrest," "Turn around," "Hands behind your back," handcuff sounds |
| **Search** | "Mind if I search," "Consent to search," "Step out of the vehicle," "What's in your pocket" |
| **Use of Force** | "Stop resisting," "Get on the ground," "Taser," physical altercation, screaming |
| **Pursuit** | Running, "Stop," "He's running," heavy breathing |
| **Sobriety Test** | "Walk heel to toe," "Follow my finger," "Breathalyzer," "Blow into this" |
| **Weapon Discovery** | "Gun," "knife," "weapon found," "What is this" |
| **Drug Discovery** | "What's this substance," "Is this yours," field test references |
| **Medical Event** | "Are you hurt," "Call an ambulance," "He's bleeding," medical complaint |
| **Witness Contact** | "Did you see what happened," "Can you tell me," witness statements |
| **911 Content** | Caller description, reported crime, location, suspect description |

For each detected event:
```
KEY EVENT [KE-001]
File: [name] @ [timestamp]
Type: [from table above]
Description: [What happened in 1–2 sentences]
Speakers Involved: [list]
Defense Relevance: [Why this matters — e.g., "No consent given before search"]
```

---

#### Module H — Use of Force Analysis
*Runs only on `BODY_CAM` and `DASH_CAM` files where force events are detected*

If Module G detects use of force events:
1. Map the complete force sequence (what led up to it, the force itself, aftermath)
2. Identify what the officer says vs. what the transcript/audio reveals
3. Flag gaps in recording (camera turned off, muted, obstructed) during force events
4. Note whether force warnings were given before force was used
5. Note suspect's verbal compliance or non-compliance

---

#### Module I — Jail Call Analysis
*Runs only on `JAIL_CALL` files*

Jail calls require special handling:
1. **Identify parties**: Who is the inmate speaking with?
2. **Flag privileged communications**: If the call appears to be with an attorney, flag immediately — this should NOT have been recorded/disclosed
3. **State-of-mind evidence**: Statements showing remorse, lack of knowledge, alibi references
4. **Admissions vs. context**: Distinguish actual admissions from contextual statements
5. **Third-party suspect references**: Any mention of other people involved
6. **Coercion/threats**: Is anyone pressuring the inmate to say specific things?

---

### Phase 5: Generate the DMAR (.docx)

Use the `docx` skill to produce the Defense Media Analysis Report. **This format is identical to the DMAR produced by dw-transcript-pipeline-calcasieu.**

#### DMAR Structure

```
DEFENSE MEDIA ANALYSIS REPORT
[Client Name] | [Docket #] | [Parish]
Transcription Platform: Rev.com ([AI/Human/Ready to Certify])
Analysis Date: [Date]
Prepared by: Claude AI — Attorney Work Product / Privileged

SECTION 1: EVIDENCE INVENTORY
  1.1 Media Files Processed (table: filename, type, duration, source folder, classification)
  1.2 Written Documents Reviewed (table: filename, type, pages, source)
  1.3 Processing Summary (total files, total duration, transcription platform, tier)

SECTION 2: TRANSCRIPT SUMMARIES
  For each transcript:
    2.X.1 File: [name] | Duration: [time] | Speakers: [list] | Classification: [type]
    2.X.2 Synopsis (3–5 sentence summary)
    2.X.3 Key Moments (timestamp + event + defense relevance)
    2.X.4 Miranda/Rights Events (all ME-### findings from Module E)
    2.X.5 Interrogation Technique Flags (all IT-### findings from Module F)
    2.X.6 Key Events Detected (all KE-### findings from Module G)

SECTION 3: CROSS-REFERENCE ANALYSIS
  All CR-### findings from Module A

SECTION 4: REPORT-VS-RECORDING DISCREPANCIES
  All RR-### findings from Module B

SECTION 5: MASTER TIMELINE
  Unified chronological timeline from Module C

SECTION 6: SPEAKER BEHAVIOR ANALYSIS
  Narrative from Module D + Use of Force analysis from Module H + Jail Call analysis from Module I

SECTION 7: DEFENSE INTELLIGENCE SUMMARY
  7.1 Strongest Defense Findings (ranked by impact)
  7.2 Recommended Skill Invocations:
      - "Run dw-confession-interrogation-auditor on [file]" (if interrogation flags found)
      - "Run dw-video-evidence-auditor on [file]" (if BWC/video gaps found)
      - "Run dw-suppression-motion for [issue]" (if Miranda/search violations found)
      - "Build cross-exam for [officer] using DMAR findings"
  7.3 Outstanding Questions
  7.4 Potential Brady/Giglio Issues

APPENDIX A: FILE HASH LOG
  SHA-256 hash of each source media file

APPENDIX B: ANALYSIS METHODOLOGY
  Claude AI analysis on Rev.com transcripts.
  Attorney verification required before any filing or client communication.
  Louisiana Act 250 / ABA Opinion 512 compliance note.
```

Save to client's evidence folder as:
`DMAR — [LastName, FirstName] — [Date].docx`

#### Update Case Brain

Write to `dw-case-brain`:
> Transcription pipeline ([Parish]/Rev) completed for [client name]: [N] media files processed.
> DMAR generated with [X] cross-reference findings, [Y] report discrepancies, [Z] Miranda events,
> [W] interrogation technique flags, [V] key events. Recommended follow-up: [list skill invocations].

---

## Rev-Native Features (Use Directly, Don't Replicate)

These Rev features should be used natively within the Rev platform:

- **Multi-File Insights** (beta): If attorney has Rev Pro/Unlimited, they can use this within Rev for additional cross-file analysis. Claude's Module A provides equivalent capability.
- **SmartDepo**: Use for deposition transcription and summary. Not part of the evidence pipeline.
- **Custom Vocabulary**: Before uploading to Rev, ask attorney for case-specific terms (officer names, street names, medical terms) to add to Rev's custom vocabulary for better accuracy.
- **Verbatim Mode**: Always enable for legal transcriptions — captures "um," "uh," false starts, and overlapping speech that are critical for interrogation analysis.

---

## Quick Reference

| Step | Platform | Method | Who |
|------|----------|--------|-----|
| Scan folder | Local | Filesystem | **Claude** |
| Classify evidence | Local | Claude analysis | **Claude** |
| Upload media | Rev.com | Browser upload | **Attorney** |
| Monitor transcription | Rev.com | Claude in Chrome | **Claude** |
| Review + label speakers | Rev.com | Rev editor | **Attorney** |
| Download transcripts | Rev.com | Claude in Chrome | **Claude** |
| Import to TranscriptPad | TranscriptPad | AppleScript + SQLite | **Claude** |
| Defense Media Analysis | Local | Claude analysis on TXT files | **Claude** |
| Generate DMAR | Local | docx skill | **Claude** |
| Update Case Brain | DEVONthink | dw-case-brain | **Claude** |
| Verify rendering | TranscriptPad | Manual click-through | **Attorney** |

---

## Error Handling

Inherits general error handling from original pipeline, plus:

- **Rev AI accuracy issues**: If AI transcript has obvious errors (garbled sections, [inaudible] markers > 5% of content), recommend attorney re-order those files as Human transcription
- **Empty transcripts**: Flag and exclude from DMAR analysis
- **Missing speaker labels**: Warn that DMAR analysis (especially Modules E and F) will be degraded without proper speaker identification
- **No written reports**: Module B produces empty section — normal for early discovery
- **Extremely long recordings (4+ hours)**: Chunk DMAR analysis by hour, then synthesize
- **Mixed transcription tiers**: Track which files used AI vs. Human in DMAR Section 1.3 so attorney knows confidence level for each
- **Rev order delays**: Human transcription can take 12+ hours. If attorney is time-pressed, recommend AI transcription for immediate DMAR analysis with Human re-order for court-filing versions later
- **JSON unavailable**: If Rev JSON download isn't available (Human transcription orders), word-level timestamps won't be available — DMAR analysis proceeds using TXT timestamps only


---

## Output Location

All file outputs from this skill save to an absolute path under the active client's case folder, never to the Cowork project default directory, `/home/claude`, `/tmp`, or `~/Downloads`.

**Output path:**

`{CASE_ROOT}/Deliverables/Phase-2-Discovery/dw-transcript-pipeline-rev/{YYYY-MM-DD}_{descriptive-filename}.{ext}`

**Resolving `{CASE_ROOT}`:**

1. Read from the active `dw-case-brain` session (preferred)
2. Use an absolute path if present in the attorney's prompt
3. If neither is available, ask the attorney for the absolute case folder path before writing

**Before writing:**

- Create the full subfolder chain with `Filesystem:create_directory` if it doesn't exist
- Confirm the path with the attorney if `{CASE_ROOT}` was resolved from the prompt (not from Case Brain)

**After writing, report the path:**

> ✅ Saved
> `{full absolute path}`
> Size: [size] | Type: [.docx / .pdf / .md / etc.]

List all files written, including intermediate exports (DMAR + transcripts + CSV exports).
