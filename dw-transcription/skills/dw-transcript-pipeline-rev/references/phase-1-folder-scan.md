# Phase 1 — Folder Scan & Evidence Classification

This phase is identical to the Calcasieu pipeline Phase 1, with the addition of evidence-type classification (Step 1.5) used by the Rev pipeline to drive downstream analysis modules.

## Step 1.1 — Get the target folder
Attorney should have client folder selected. Folder name follows `lastname, firstname` convention.

## Step 1.2 — Scan for media files
Recursively scan all subfolders. Collect files with these extensions (case-insensitive):

- **Video**: `.mp4`, `.mov`, `.avi`, `.wmv`, `.mkv`, `.flv`, `.webm`, `.m4v`, `.mpg`, `.mpeg`, `.3gp`, `.ts`, `.vob`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.m4a`, `.ogg`, `.flac`, `.wma`, `.aiff`, `.aif`, `.opus`, `.amr`

**Skip files whose name ends with `_TRANSCRIBED`.** These were processed in a prior run.

## Step 1.3 — Detect duplicates
Flag files with same base name across different paths or sizes. Present and ask attorney which to include.

## Step 1.4 — Present file list and confirm
Show summary table. Confirm before proceeding. Stop if zero unprocessed files.

## Step 1.5 — Classify evidence types

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
