# Error Handling & Rev-Native Features

## Rev-Native Features (Use Directly, Don't Replicate)

These Rev features should be used natively within the Rev platform:

- **Multi-File Insights** (beta): If attorney has Rev Pro/Unlimited, they can use this within Rev for additional cross-file analysis. Claude's Module A provides equivalent capability.
- **SmartDepo**: Use for deposition transcription and summary. Not part of the evidence pipeline.
- **Custom Vocabulary**: Before uploading to Rev, ask attorney for case-specific terms (officer names, street names, medical terms) to add to Rev's custom vocabulary for better accuracy.
- **Verbatim Mode**: Always enable for legal transcriptions — captures "um," "uh," false starts, and overlapping speech that are critical for interrogation analysis.

---

## Error Handling

Inherits general error handling from original pipeline, plus:

- **Rev AI accuracy issues**: If AI transcript has obvious errors (garbled sections, [inaudible] markers > 5% of content), recommend attorney re-order those files as Human transcription
- **Empty transcripts**: Flag and exclude from DMAR analysis
- **Missing speaker labels**: Warn that DMAR analysis (especially Modules E and F) will be degraded without proper speaker identification
- **No written reports**: Module B produces empty section — normal for early discovery
- **Extremely long recordings (4+ hours)**: Chunk DMAR analysis by hour, then synthesize
- **Mixed transcription tiers**: Track which files used AI vs. Human in DMAR Section 1.3 so attorney knows confidence level for each
- **Rev order delays**: Human transcription can take 12+ hours. If attorney is time-pressed, recommend AI transcription for immediate DMAR analysis with Human re-order for court-filing versions later
- **JSON unavailable**: If Rev JSON download isn't available (Human transcription orders), word-level timestamps won't be available — DMAR analysis proceeds using TXT timestamps only
