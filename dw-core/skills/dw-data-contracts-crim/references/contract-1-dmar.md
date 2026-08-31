# Contract 1: Defense Media Analysis Report (DMAR) — Full Schema

Read from the SKILL.md **Contract 1: Defense Media Analysis Report (DMAR)** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producers:** `dw-transcript-pipeline-calcasieu-crim`, `dw-transcript-pipeline-rev-crim`
**Consumers:** `dw-confession-interrogation-auditor-crim`, `dw-video-evidence-auditor-crim`, `dw-forensic-dump-analyzer-crim`, `dw-cross-exam-architect-crim`, `dw-dmar-synthesizer-crim`, `dw-case-brain-crim`

### Filename Pattern
`Defense Media Analysis Report — [Client Last Name] [Date].docx`

### Required Sections (in order)
1. **Header Block** — Must include the following fields, in this order:
   - `Schema Version: <semver>` (current: `1.0`) — bumped when this contract changes the DMAR shape; downstream consumers should refuse to parse a higher major version they don't recognize
   - `Date Generated: <ISO-8601>` (e.g., `2026-05-02T14:32:00Z`) — when this DMAR was produced
   - `Pipeline: <skill-name>` (e.g., `dw-transcript-pipeline-rev-crim`) — which producer skill emitted this DMAR
   - `Client Name`
   - `Docket Number`
   - `Parish`
2. **Media Inventory** — Table of all media files processed with: filename, duration, file type, speaker count, transcription status
3. **Transcript Summaries** — Per-file summary with: key statements (with timestamps), speakers identified, topics covered
4. **Inconsistency Matrix** — Cross-file contradictions: who said what, where it conflicts, timestamp references for both
5. **Miranda & Rights Analysis** — Whether rights were administered, timing, waiver status, any issues (applies to interrogation recordings only — mark N/A for other media types)
6. **Interrogation Technique Detection** — Reid technique markers, leading questions, coercion indicators, minimization/maximization (applies to interrogation recordings only — mark N/A for other media types)
7. **Key Event Timeline** — Chronological timeline of significant events across all media files with timestamps and source file references
8. **Defense Intelligence Brief** — Actionable findings organized by: favorable to defense, unfavorable to defense, requires further investigation
9. **Cross-Examination Seeds** — Specific contradictions, omissions, or procedural issues that can be used in cross-examination, with source references
10. **Report-vs-Recording Matrix (Barone 6-Category)** — Systematic comparison of what official reports say versus what recordings actually show. One matrix per officer/report-recording pair. Required categories:

| Category | What to Compare | Defense Significance |
|----------|----------------|---------------------|
| **1. Narrative Match** | What the report says happened vs. what the recording shows happened | Outright contradictions = impeachment gold |
| **2. Omissions** | What the report omits that the recording shows | What officers chose NOT to document may reveal bias or cover-up |
| **3. Additions** | What the report adds that the recording doesn't show | Fabricated or embellished facts undermine credibility |
| **4. Timing Discrepancies** | Chronological differences between report timestamps and recording timestamps | Inaccurate timelines may conceal constitutional violations (e.g., Miranda delay) |
| **5. Quote Accuracy** | What was said (recording) vs. what was reported as said (report) | Paraphrased or altered quotes may change meaning — especially confessions |
| **6. Procedural Compliance** | Procedures described in report vs. procedures shown in recording | Officers may claim procedures were followed that recordings show were not (search protocols, Miranda, use of force) |

Each matrix entry must include: Report citation (document, page, paragraph), Recording citation (file, timestamp range), Discrepancy description, and Severity (CRITICAL / SIGNIFICANT / MINOR).

### Required Fields per Transcript Entry
- Source filename (must match filename in evidence folder)
- Duration (HH:MM:SS)
- Speaker labels (consistent across all entries)
- Transcript text with timestamps at minimum 30-second intervals
- Confidence flags for uncertain transcription segments

### Output Location
`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`
