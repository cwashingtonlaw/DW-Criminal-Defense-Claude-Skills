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

## Step 1 — Determine the Parish

Check these sources in order:

1. **Case Brain**: If a case is loaded via `dw-case-brain`, read the parish from the case state document.
2. **Attorney statement**: If the attorney mentioned the parish in their prompt (e.g., "transcribe the evidence for the Smith case in Orleans Parish").
3. **Folder path**: D&W case folders often include parish identifiers in the shared drive path (e.g., `Shared drives → Calcasieu PDO Files → ...`).
4. **Ask**: If parish cannot be determined from context, ask:

> Which parish is this case in? This determines which transcription platform I'll use:
> - **Calcasieu** → JusticeText
> - **Any other parish** → Rev.com

## Step 2 — Route to the Correct Pipeline

Once the parish is determined:

- **If Calcasieu**: Read and execute `dw-transcript-pipeline-calcasieu/SKILL.md`
- **If any other parish**: Read and execute `dw-transcript-pipeline-rev/SKILL.md`

Pass all context forward: client name, docket number, folder path, any specific evidence the attorney mentioned, and the parish name.

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

## Adding New Parishes

If a new parish contracts with JusticeText or Rev changes, update only the routing table in Step 1. The pipeline skills themselves do not contain parish logic.
