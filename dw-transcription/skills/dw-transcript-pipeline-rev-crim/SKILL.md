---
name: dw-transcript-pipeline-rev-crim
category: transcription
description: >
  Rev.com-based transcription pipeline for all non-Calcasieu Parish cases at Daniels & Washington.
  ALWAYS invoke for "Rev pipeline," "Rev transcription," "upload to Rev," "transcribe non-Calcasieu
  media," "Rev DMAR," or when dw-transcript-router-crim routes a non-Calcasieu case here. Handles the
  full workflow: folder scan → Rev upload → transcription → TranscriptPad import → Defense Media
  Analysis Report. Adds MirandaAI-equivalent defense analysis features (Miranda rights detection,
  Reid technique identification, leading question flagging, coercion indicators, key event
  detection, interrogation technique analysis) via Claude analysis layer on top of Rev transcripts.
  Produces a standardized Defense Media Analysis Report (.docx) identical in schema to
  dw-transcript-pipeline-calcasieu-crim output. This skill is invoked by dw-transcript-router-crim for all
  non-Calcasieu cases.
---

# DW Transcript Pipeline — All Parishes Except Calcasieu (Rev.com)

**Platform**: Rev.com (rev.com)
**Parishes**: All except Calcasieu (routed by dw-transcript-router-crim)
**Output**: Defense Media Analysis Report (.docx) + TranscriptPad case

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any audio or video files for transcription (interrogations, jail calls, interviews, body-worn camera, dashcam, 911 calls, civilian video), do not begin upload to Rev yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional media for this batch? I'll start the Rev upload only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. Mid-batch additions cause partial uploads, duplicate billing on Rev, and broken DMAR ordering when the late files come back out of sequence.

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

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## Pipeline Phases — Overview

| Phase | Purpose | Reference |
|-------|---------|-----------|
| 1 | Folder scan, duplicate detection, evidence-type classification | `references/phase-1-folder-scan.md` |
| 2 | Rev.com tier selection, upload, monitoring, download | `references/phase-2-rev-upload.md` |
| 2.5 | Transcript review and speaker labeling (attorney action) | `references/phase-2-rev-upload.md` |
| 3 | TranscriptPad import (.tracase database) | `references/phase-3-transcriptpad-import.md` |
| 4 | Defense Media Analysis (Modules A–I) | This file (module list) + per-module references |
| 5 | Generate the DMAR (.docx) and update Case Brain | `references/dmar-structure.md` |

---

### Phase 1: Folder Scan

Identical to the Calcasieu pipeline Phase 1, with an additional evidence-classification step that drives downstream analysis modules.

Read `references/phase-1-folder-scan.md` for the full procedure: file extensions to scan, the `_TRANSCRIBED` skip rule, duplicate handling, and the classification table mapping each evidence type (`INTERROGATION`, `BODY_CAM`, `DASH_CAM`, `JAIL_CALL`, `911_CALL`, `WITNESS_INTERVIEW`, `SURVEILLANCE`, `OTHER`) to the analysis modules it triggers.

---

### Phase 2: Rev.com Upload & Transcription

Read `references/phase-2-rev-upload.md` for the full procedure. Summary:

- **Step 2.1** — Ask the attorney to choose a transcription tier: AI ($0.25/min), Human ($1.99/min), Ready to Certify, or Mixed (recommended).
- **Step 2.2** — Navigate to `https://www.rev.com` and confirm login.
- **Step 2.3** — Attorney uploads media via Google Drive picker or local browse. Verbatim mode + timestamps required for Human/Ready to Certify orders.
- **Step 2.4** — Monitor transcription status (5–15 min for AI, 2–12 hr for Human, 1–3 days for Ready to Certify).
- **Step 2.5** — Download transcripts (DOCX + TXT, plus JSON when available). Verify file sizes (flag <1KB).

### Phase 2.5: Transcript Review & Speaker Labeling

Rev's diarization defaults to "Speaker 1," "Speaker 2." Attorney must relabel speakers and correct names/addresses/dates in Rev's editor before re-downloading. See `references/phase-2-rev-upload.md` for the attorney-action script.

---

### Phase 3: TranscriptPad Import

Identical to the Calcasieu pipeline Phase 4, with a Rev-specific timestamp regex. Read `references/phase-3-transcriptpad-import.md` for:

- The 8-step import sequence (find/create case, back up `.tracase`, stage in Inbox, import via Add menu, copy media + link in SQLite, fix timestamps, sync both case locations, rename originals with `_TRANSCRIBED`).
- The combined Rev/JusticeText timestamp regex used by `transcriptpad-timestamp-fix.py`.

---

### Phase 4: Defense Media Analysis Report (MirandaAI-Equivalent Features)

This phase adds MirandaAI-equivalent criminal defense analysis capabilities to Rev transcripts using Claude's analytical layer. **Claude reads all downloaded TXT transcripts and runs the analysis modules below.**

The output is a standardized **Defense Media Analysis Report (DMAR)** — identical in structure to the DMAR produced by `dw-transcript-pipeline-calcasieu-crim`.

#### Module Map

| Module | Purpose | Runs On | Reference |
|--------|---------|---------|-----------|
| A — Multi-File Cross-Reference | Find contradictions, corroborations, gaps, sequence conflicts across files | All transcripts | `references/modules-cross-ref-timeline-speaker.md` |
| B — Document-vs-Media Comparison | Compare written reports against transcript content | All transcripts (when reports exist) | `references/modules-cross-ref-timeline-speaker.md` |
| C — Chronological Master Timeline | Unified timeline across all sources | All transcripts | `references/modules-cross-ref-timeline-speaker.md` |
| D — Speaker Behavior Analysis | Speech patterns, emotional shifts, consistency, power dynamics | All transcripts | `references/modules-cross-ref-timeline-speaker.md` |
| E — Miranda & Constitutional Events | Miranda warnings, invocations, custody markers (3 sub-modules) | All; detailed for `INTERROGATION` and `WITNESS_INTERVIEW` | `references/module-e-miranda-detection.md` |
| F — Interrogation Technique Analysis | Reid technique, coercion indicators, false-confession risk (3 sub-modules) | `INTERROGATION` only | `references/module-f-interrogation-techniques.md` |
| G — Key Event Detection | Auto-detect traffic stops, arrests, searches, force, sobriety tests, etc. | All file types | `references/module-g-key-event-detection.md` |
| H — Use of Force Analysis | Force-sequence mapping, recording-gap detection | `BODY_CAM`, `DASH_CAM` (when force detected) | `references/modules-cross-ref-timeline-speaker.md` |
| I — Jail Call Analysis | Privilege flagging, state-of-mind, admissions vs. context | `JAIL_CALL` only | `references/modules-cross-ref-timeline-speaker.md` |

Read each referenced file for the per-module detection patterns, severity tables, output schemas, and verbatim-quote formats.

---

### Phase 4A: Report-vs-Recording Matrix (Barone 6-Category)

For every officer whose written report can be compared against a transcribed recording, generate a **Report-vs-Recording Matrix** per `dw-data-contracts-crim` Contract 1 Section 10. The six comparison categories are: (1) Narrative Match, (2) Omissions, (3) Additions, (4) Timing Discrepancies, (5) Quote Accuracy, (6) Procedural Compliance. Each discrepancy entry includes report citation, recording citation, discrepancy description, and severity (CRITICAL / SIGNIFICANT / MINOR). This matrix appears as DMAR Section 4A.

---

### Phase 5: Generate the DMAR (.docx)

Use the `docx` skill to produce the Defense Media Analysis Report. **The format is identical to the DMAR produced by `dw-transcript-pipeline-calcasieu-crim`.**

Read `references/dmar-structure.md` for the full Header Block + Section 1–7 + Section 4A (Barone Report-vs-Recording Matrix) + Appendix A/B template, the filename pattern (`DMAR — [LastName, FirstName] — [Date].docx`), and the Case Brain update entry.

**Header Block fields required by `dw-data-contracts-crim` Contract 1:**

- `Schema Version: 1.0`
- `Date Generated: <ISO-8601 timestamp>`
- `Pipeline: dw-transcript-pipeline-rev-crim`

These three fields must appear in the Header Block exactly as shown — downstream consumers (`dw-confession-interrogation-auditor-crim`, `dw-video-evidence-auditor-crim`, `dw-cross-exam-architect-crim`, `dw-dmar-synthesizer-crim`, `dw-case-brain-crim`) parse them and may refuse a higher major version they don't recognize.

---

## Rev-Native Features & Error Handling

Read `references/error-handling-and-rev-features.md` for:

- **Rev-Native Features (Use Directly, Don't Replicate)** — Multi-File Insights, SmartDepo, Custom Vocabulary, Verbatim Mode.
- **Error Handling** — AI accuracy degradation, empty transcripts, missing speaker labels, no written reports, long recordings, mixed tiers, order delays, JSON unavailability.

---

## Quick Reference — Who Does What

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
| Update Case Brain | DEVONthink | dw-case-brain-crim | **Claude** |
| Verify rendering | TranscriptPad | Manual click-through | **Attorney** |

Follow shared protocols for output paths (see Step 0.5).

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **phase-1-folder-scan.md** — Folder-scan procedure, supported media extensions, duplicate detection, and the evidence-type classification table that drives downstream module selection
- **phase-2-rev-upload.md** — Rev.com tier selection, attorney upload script, transcription monitoring windows, download checklist, and the Phase 2.5 speaker-labeling protocol
- **phase-3-transcriptpad-import.md** — TranscriptPad `.tracase` import sequence and the combined Rev/JusticeText timestamp regex
- **module-e-miranda-detection.md** — Module E (Miranda Rights & Constitutional Events): the nine MIRANDA-* finding types, the four-component check, ambiguous-invocation list (Edwards v. Arizona), and custody-determination markers
- **module-f-interrogation-techniques.md** — Module F (Interrogation Technique Analysis): Reid Technique components, coercion indicators, false-confession risk factors, and the IT-### output schema
- **module-g-key-event-detection.md** — Module G (Key Event Detection): the eleven auto-detected event types with detection-pattern table and the KE-### output schema
- **modules-cross-ref-timeline-speaker.md** — Modules A, B, C, D, H, and I: cross-reference findings, document-vs-media comparison, master timeline, speaker behavior, use-of-force analysis, and jail-call analysis
- **dmar-structure.md** — Full Defense Media Analysis Report template (Header Block per `dw-data-contracts-crim` Contract 1, Sections 1–7, Appendices A/B), filename pattern, and Case Brain update entry
- **error-handling-and-rev-features.md** — Rev-native features to use directly (Multi-File Insights, SmartDepo, Custom Vocabulary, Verbatim Mode) and Rev-specific error-handling rules
