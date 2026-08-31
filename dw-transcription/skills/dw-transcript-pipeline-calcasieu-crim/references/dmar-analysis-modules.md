# DMAR Analysis Modules A–D — Procedures and Output Formats

Read at Phase 5 (Defense Media Analysis Report) of `dw-transcript-pipeline-calcasieu-crim` before running Modules A–D; the per-module extraction steps and the CR-### / RR-### / timeline / speaker output formats moved verbatim from SKILL.md.

## Module A — Multi-File Cross-Reference Analysis

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

## Module B — Document-vs-Media Comparison

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

## Module C — Chronological Master Timeline

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

## Module D — Speaker Behavior Analysis

For each identified speaker across all transcripts:
1. **Speech patterns**: Hesitation markers, corrections, evasions
2. **Emotional shifts**: Changes in tone described by context (raised voice, crying, silence)
3. **Consistency**: Does this speaker's account stay consistent across multiple recordings?
4. **Power dynamics**: Who controls the conversation? Interruptions, redirections, topic changes

Output as narrative paragraphs in DMAR Section 6, organized by speaker.
