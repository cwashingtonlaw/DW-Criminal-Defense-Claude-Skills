---
name: dw-transcript-router
description: >
  Parish-based transcript pipeline router for Daniels & Washington. Determines which
  transcription platform (JusticeText or Rev) to use based on case parish, then invokes
  the correct pipeline skill. Calcasieu Parish cases route to dw-transcript-pipeline-calcasieu
  (JusticeText). All other parishes route to dw-transcript-pipeline-rev (Rev.com). Triggers:
  "transcribe the evidence," "transcript pipeline," "process audio/video," "transcribe jail
  calls," "transcribe body cam," "transcribe the interview," "process the recordings," or any
  reference to transcription, media processing, or a client folder containing media discovery
  files. Also triggers on: "run the transcript pipeline," "process the [client] folder,"
  "transcribe the [client] evidence," "new evidence recordings," or "upload recordings."
  This skill replaces the former dw-transcript-pipeline as the single entry point for all
  transcription workflows.
---

# DW Transcript Router

Parish-based routing layer for the D&W dual-platform transcription system.

## Routing Logic

| Parish | Platform | Pipeline Skill |
|--------|----------|----------------|
| Calcasieu | JusticeText | `dw-transcript-pipeline-calcasieu` |
| All other parishes | Rev.com | `dw-transcript-pipeline-rev` |
| Any (ad-hoc single files) | case.dev | `casedev:transcription` (connected skill) |

## Step 1 — Determine the Parish

Check these sources in order:

1. **Case Brain**: If a case is loaded via `dw-case-brain`, read the parish from the case state document.
2. **Attorney statement**: If the attorney mentioned the parish in their prompt (e.g., "transcribe the evidence for the Smith case in Orleans Parish").
3. **Folder path**: D&W case folders often include parish identifiers in the shared drive path (e.g., `Shared drives → Calcasieu PDO Files → ...`).
4. **Ask**: If parish cannot be determined from context, ask:

> Which parish is this case in? This determines which transcription platform I'll use:
> - **Calcasieu** → JusticeText
> - **Any other parish** → Rev.com
> - **Quick single-file transcription** → case.dev (no parish routing needed)

## Step 2 — Route to the Correct Pipeline

Once the parish is determined:

- **If Calcasieu**: Read and execute `dw-transcript-pipeline-calcasieu/SKILL.md`
- **If any other parish**: Read and execute `dw-transcript-pipeline-rev/SKILL.md`

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
- `dw-confession-interrogation-auditor`
- `dw-video-evidence-auditor`
- `dw-forensic-dump-analyzer`
- `dw-cross-exam-architect`
- `dw-case-brain` (session persistence)

The attorney never needs to know which platform produced the transcript — downstream skills receive the same structured input regardless of source.

**Note on case.dev transcripts:** The `casedev:transcription` route produces a raw transcript with speaker diarization — it does NOT generate a full DMAR. If the attorney later needs the full DMAR analysis (inconsistency detection, Miranda analysis, interrogation techniques, cross-examination seeds), run the appropriate parish-based pipeline on the same file. The case.dev transcript can serve as input to accelerate that process.

## Adding New Parishes or Platforms

If a new parish contracts with JusticeText, or Rev changes pricing/availability, update only the routing table in Step 1. The pipeline skills themselves do not contain parish logic.

To add a new transcription platform:
1. Create a new `dw-transcript-pipeline-[platform]` skill following the DMAR output contract in `dw-data-contracts/SKILL.md`
2. Add the platform to the routing table above
3. Ensure the new pipeline produces an identical DMAR schema so downstream skills work unchanged


---

## Output Location

All file outputs from this skill save to an absolute path under the active client's case folder, never to the Cowork project default directory, `/home/claude`, `/tmp`, or `~/Downloads`.

**Output path:**

`{CASE_ROOT}/Deliverables/Phase-2-Discovery/dw-transcript-router/{YYYY-MM-DD}_{descriptive-filename}.{ext}`

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

List all files written, including intermediate exports (routing decision log).
