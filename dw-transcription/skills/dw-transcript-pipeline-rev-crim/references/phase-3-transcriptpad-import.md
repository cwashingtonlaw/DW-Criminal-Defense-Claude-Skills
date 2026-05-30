# Phase 3 — TranscriptPad Import

Identical to Calcasieu pipeline Phase 4:

1. Find or create TranscriptPad case
2. Back up `.tracase` package
3. Stage transcripts in Inbox
4. Import via Add menu
5. Copy media into case and link in database (SQLite)
6. Fix timestamps (Python + SQLite — adjust regex for Rev's timestamp format)
7. Sync both case locations
8. Rename originals with `_TRANSCRIBED` suffix

## Rev Timestamp Format Note

Rev TXT exports use `[HH:MM:SS]` or `(HH:MM:SS)` format depending on settings. The timestamp fix script regex should handle both Rev and JusticeText formats:

```
\[?(\d{1,2}:\d{2}(?::\d{2})?)\]?\s+(.+?):\s*\n(.*?)(?=\n\[?\d{1,2}:\d{2}|\Z)
```
