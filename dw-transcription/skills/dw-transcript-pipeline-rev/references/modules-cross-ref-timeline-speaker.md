# Analysis Modules A, B, C, D, H, I

These modules run during Phase 4 (Defense Media Analysis) alongside Modules E, F, and G (which have their own dedicated reference files).

---

## Module A — Multi-File Cross-Reference Analysis

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

## Module B — Document-vs-Media Comparison

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

## Module C — Chronological Master Timeline

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

## Module D — Speaker Behavior Analysis

For each identified speaker:
1. **Speech patterns**: Hesitation, corrections, evasions
2. **Emotional shifts**: Changes described by context
3. **Consistency**: Does account stay consistent across recordings?
4. **Power dynamics**: Who controls conversation? Interruptions, redirections

Output as narrative paragraphs in DMAR Section 6.

---

## Module H — Use of Force Analysis

*Runs only on `BODY_CAM` and `DASH_CAM` files where force events are detected*

If Module G detects use of force events:
1. Map the complete force sequence (what led up to it, the force itself, aftermath)
2. Identify what the officer says vs. what the transcript/audio reveals
3. Flag gaps in recording (camera turned off, muted, obstructed) during force events
4. Note whether force warnings were given before force was used
5. Note suspect's verbal compliance or non-compliance

---

## Module I — Jail Call Analysis

*Runs only on `JAIL_CALL` files*

Jail calls require special handling:
1. **Identify parties**: Who is the inmate speaking with?
2. **Flag privileged communications**: If the call appears to be with an attorney, flag immediately — this should NOT have been recorded/disclosed
3. **State-of-mind evidence**: Statements showing remorse, lack of knowledge, alibi references
4. **Admissions vs. context**: Distinguish actual admissions from contextual statements
5. **Third-party suspect references**: Any mention of other people involved
6. **Coercion/threats**: Is anyone pressuring the inmate to say specific things?
