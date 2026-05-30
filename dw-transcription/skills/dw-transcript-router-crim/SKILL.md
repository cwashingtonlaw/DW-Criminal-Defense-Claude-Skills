---
name: dw-transcript-router-crim
category: transcription
description: >
  Parish-based transcript pipeline router for Daniels & Washington. ALWAYS invoke for
  "transcribe the evidence," "transcript pipeline," "process audio/video," "transcribe jail
  calls," "transcribe body cam," "transcribe the interview," "process the recordings,"
  "run the transcript pipeline," "process the [client] folder," "transcribe the [client]
  evidence," "new evidence recordings," "upload recordings," or any reference to transcription,
  media processing, or a client folder containing media discovery files. Determines which
  transcription platform (JusticeText or Rev) to use based on case parish, then invokes
  the correct pipeline skill. Calcasieu Parish cases route to dw-transcript-pipeline-calcasieu-crim
  (JusticeText). All other parishes route to dw-transcript-pipeline-rev-crim (Rev.com). This skill
  replaces the former dw-transcript-pipeline as the single entry point for all transcription
  workflows.
---

# DW Transcript Router

Parish-based routing layer for the D&W dual-platform transcription system.

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any audio or video files (interrogations, jail calls, interviews, body-worn camera, dashcam, 911 calls, civilian video, or any media requiring transcription), do not begin routing yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional audio or video files for transcription? I'll start routing only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. Routing the wrong batch to the wrong pipeline (Calcasieu/JusticeText vs. Rev.com) creates re-work and billing complications.

---

### Source Citation Mandate

Every factual claim in routing memos, parish determinations, or pipeline-selection rationale must trace back to a specific source — typically the case file's parish-of-prosecution designation in `Case Brain` or the case-tables spreadsheet. Routing decisions feed billing (different platforms have different cost structures) and downstream analysis (transcript format and DMAR schema differ by pipeline), so the basis for routing must be auditable.

**Citation format:** Cite the source of the parish determination. Examples:
- `(Case Brain — Parish: Calcasieu, last updated 2026-04-15)`
- `(Case Tables.xlsx, Case Profile sheet, Parish field)`
- `(Bill of Information, Docket #2026-CR-0456, 14th JDC)`
- `(Attorney instruction — Parish: Caddo, 2026-04-15)`

**Unsourced assertions:** If parish is unclear, do not route — ask the attorney rather than guessing. Mark any uncertain routing `[UNSOURCED — CONFIRM PARISH]` until the attorney confirms.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## Routing Logic

| Parish | Platform | Pipeline Skill |
|--------|----------|----------------|
| Calcasieu | JusticeText | `dw-transcript-pipeline-calcasieu-crim` |
| All other parishes | Rev.com | `dw-transcript-pipeline-rev-crim` |
| Any (ad-hoc single files) | case.dev | `casedev:transcription` (connected skill) |

## Step 1 — Determine the Parish

Check these sources in order:

1. **Case Brain**: If a case is loaded via `dw-case-brain-crim`, read the parish from the case state document.
2. **Attorney statement**: If the attorney mentioned the parish in their prompt (e.g., "transcribe the evidence for the Smith case in Orleans Parish").
3. **Folder path**: D&W case folders often include parish identifiers in the shared drive path (e.g., `Shared drives → Calcasieu PDO Files → ...`).
4. **Ask**: If parish cannot be determined from context, ask:

> Which parish is this case in? This determines which transcription platform I'll use:
> - **Calcasieu** → JusticeText
> - **Any other parish** → Rev.com
> - **Quick single-file transcription** → case.dev (no parish routing needed)

## Step 2 — Route to the Correct Pipeline

Once the parish is determined:

- **If Calcasieu**: Read and execute `dw-transcript-pipeline-calcasieu-crim/SKILL.md`
- **If any other parish**: Read and execute `dw-transcript-pipeline-rev-crim/SKILL.md`

Pass all context forward: client name, docket number, folder path, any specific evidence the attorney mentioned, and the parish name.

- **If the attorney requests ad-hoc / single-file transcription** (e.g., "just transcribe this one recording," "quick transcript of this file"): Route to `casedev:transcription` skill. This uses case.dev's transcription API with speaker diarization. It does NOT produce a full DMAR — it returns a raw transcript. Use this for quick turnaround on individual files when the full pipeline workflow isn't needed.

**When to suggest case.dev over the full pipeline:**
- Single file (not a batch of discovery media)
- Attorney wants a quick transcript, not a full Defense Media Analysis Report
- File is already isolated (not part of a larger evidence folder scan)
- Attorney explicitly asks for "quick" or "fast" transcription

## Step 3 — Confirm Routing

Before starting the pipeline, confirm with the attorney:

> This is a **[Parish]** case, so I'll use **[JusticeText/Rev]** for transcription. Both pipelines
> produce identical Defense Media Analysis reports for your downstream skills. Ready to proceed?

## Output Guarantee

Both pipeline skills produce an identical **Defense Media Analysis Report** (DMAR) as a `.docx` file. This report uses a standardized schema consumed by:
- `dw-confession-interrogation-auditor-crim`
- `dw-video-evidence-auditor-crim`
- `dw-forensic-dump-analyzer-crim`
- `dw-cross-exam-architect-crim`
- `dw-case-brain-crim` (session persistence)

The attorney never needs to know which platform produced the transcript — downstream skills receive the same structured input regardless of source.

**Note on case.dev transcripts:** The `casedev:transcription` route produces a raw transcript with speaker diarization — it does NOT generate a full DMAR. If the attorney later needs the full DMAR analysis (inconsistency detection, Miranda analysis, interrogation techniques, cross-examination seeds), run the appropriate parish-based pipeline on the same file. The case.dev transcript can serve as input to accelerate that process.

## Adding New Parishes or Platforms

If a new parish contracts with JusticeText, or Rev changes pricing/availability, update only the routing table in Step 1. The pipeline skills themselves do not contain parish logic.

To add a new transcription platform:
1. Create a new `dw-transcript-pipeline-[platform]` skill following the DMAR output contract in `dw-data-contracts-crim/SKILL.md`
2. Add the platform to the routing table above
3. Ensure the new pipeline produces an identical DMAR schema so downstream skills work unchanged


Follow shared protocols for output paths (see Step 0.5).
