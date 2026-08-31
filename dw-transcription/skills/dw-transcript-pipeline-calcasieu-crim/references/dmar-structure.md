# Defense Media Analysis Report (DMAR) — Structure

Read at Phase 6 (Generate the DMAR) of `dw-transcript-pipeline-calcasieu-crim`; the full DMAR skeleton (header fields per `dw-data-contracts-crim` Contract 1, Sections 1–7 including 4A Barone matrix, Appendices A–B) moved verbatim from SKILL.md.

#### DMAR Structure

```
DEFENSE MEDIA ANALYSIS REPORT
Schema Version: 1.0                          ← per dw-data-contracts-crim Contract 1
Date Generated: [ISO-8601 timestamp]         ← per dw-data-contracts-crim Contract 1
Pipeline: dw-transcript-pipeline-calcasieu-crim   ← per dw-data-contracts-crim Contract 1
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

SECTION 4A: REPORT-VS-RECORDING MATRIX (BARONE 6-CATEGORY)
  Per-officer comparison matrix per dw-data-contracts-crim Contract 1 Section 10:
    4A.1 Narrative Match — report account vs. recording events
    4A.2 Omissions — what the report leaves out
    4A.3 Additions — what the report adds without recording support
    4A.4 Timing Discrepancies — report timestamps vs. recording timestamps
    4A.5 Quote Accuracy — reported quotes vs. actual statements
    4A.6 Procedural Compliance — procedures described vs. procedures shown
  Each entry: Report citation | Recording citation | Discrepancy | Severity
  (Empty section with "No officer reports available for matrix comparison" if none exist)

SECTION 5: MASTER TIMELINE
  Unified chronological timeline from Module C

SECTION 6: SPEAKER BEHAVIOR ANALYSIS
  Narrative analysis from Module D, organized by speaker

SECTION 7: DEFENSE INTELLIGENCE SUMMARY
  7.1 Strongest Defense Findings (ranked by impact)
  7.2 Recommended Skill Invocations:
      - "Run dw-confession-interrogation-auditor-crim on [file]" (if interrogation detected)
      - "Run dw-video-evidence-auditor-crim on [file]" (if BWC/video gaps found)
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
