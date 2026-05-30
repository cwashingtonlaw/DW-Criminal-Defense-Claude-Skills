# DMAR Structure (Phase 5 Output)

Use the `docx` skill to produce the Defense Media Analysis Report. **This format is identical to the DMAR produced by `dw-transcript-pipeline-calcasieu-crim`.**

The Header Block fields (`Schema Version`, `Date Generated`, `Pipeline`) are required by `dw-data-contracts-crim` Contract 1 — emit them exactly as shown.

## DMAR Structure

```
DEFENSE MEDIA ANALYSIS REPORT
Schema Version: 1.0                       ← per dw-data-contracts-crim Contract 1
Date Generated: [ISO-8601 timestamp]      ← per dw-data-contracts-crim Contract 1
Pipeline: dw-transcript-pipeline-rev-crim      ← per dw-data-contracts-crim Contract 1
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
      - "Run dw-confession-interrogation-auditor-crim on [file]" (if interrogation flags found)
      - "Run dw-video-evidence-auditor-crim on [file]" (if BWC/video gaps found)
      - "Run dw-suppression-motion-crim for [issue]" (if Miranda/search violations found)
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

## Update Case Brain

Write to `dw-case-brain-crim`:
> Transcription pipeline ([Parish]/Rev) completed for [client name]: [N] media files processed.
> DMAR generated with [X] cross-reference findings, [Y] report discrepancies, [Z] Miranda events,
> [W] interrogation technique flags, [V] key events. Recommended follow-up: [list skill invocations].
