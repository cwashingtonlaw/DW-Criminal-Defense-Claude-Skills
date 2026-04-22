# TranscriptPad Database Reference

Technical reference for the TranscriptPad `.tracase` SQLite Core Data database. Documented from analysis of working cases (Perry, Joseph and Taraba, Andrew), March 2026.

## Package Structure

A `.tracase` file is a macOS directory bundle:

```
CaseName.tracase/
├── ImportedFiles/              ← UUID-named file copies (no extensions)
│   ├── AABBCCDD-1122-3344-...
│   └── ...
├── StoreContent/
│   └── persistentStore         ← SQLite database (Core Data)
└── importedFiles.json          ← UUID → original path mapping
```

## Database Location

```
<CaseName>.tracase/StoreContent/persistentStore
```

Standard SQLite3 database. Always close TranscriptPad before making direct modifications.
## Entity Types (Z_PRIMARYKEY Table)

| Z_ENT | Z_NAME | Description |
|-------|--------|-------------|
| 1 | TRACase | The case itself |
| 2 | TRACaseFile | Physical files imported into the case |
| 3 | TRADocument | Media documents (audio/video) |
| 4 | TRAFolder | Folder organization |
| 5 | TRAIssueCode | Issue coding categories |
| 6 | TRAPageBookmark | Page bookmarks |
| 7 | TRATranscript | Transcript metadata |
| 8 | TRATranscriptFlag | Transcript flags/markers |
| 9 | TRATranscriptLine | Individual transcript lines (the bulk of data) |
| 10 | TRAVideoClip | Video clips |
| 11 | TRAVideoClipSegment | Video clip segments |

The `Z_MAX` column in Z_PRIMARYKEY tracks the highest Z_PK assigned for each entity. **Always update Z_MAX after inserting new records.**

## Key Tables

### ZTRACASEFILE (Entity 2)

Physical files imported into the case. Each imported file (transcript .txt, media .mp4/.wav/.mp3) gets one entry.

| Column | Type | Description |
|--------|------|-------------|
| Z_PK | INTEGER | Primary key |
| Z_ENT | INTEGER | Always 2 |
| Z_OPT | INTEGER | Optimistic lock counter |
| ZPARENTCASE | INTEGER | FK → ZTRACASE.Z_PK (usually 1) |
| ZSIZE | INTEGER | File size in bytes |
| ZTRANSCRIPT | INTEGER | FK → ZTRATRANSCRIPT.Z_PK (for .txt files only) |
| ZFILENAME | VARCHAR | Original filename |
| ZORIGINALFILEPATH | VARCHAR | Original absolute path on disk |
| ZUUID | VARCHAR | UUID matching the filename in ImportedFiles/ |
### ZTRATRANSCRIPT (Entity 7)

Transcript metadata. One entry per imported transcript file.

| Column | Type | Description |
|--------|------|-------------|
| Z_PK | INTEGER | Primary key |
| Z_ENT | INTEGER | Always 7 |
| Z_OPT | INTEGER | Optimistic lock counter |
| ZFILE | INTEGER | FK → ZTRACASEFILE.Z_PK |
| ZPARENTCASE | INTEGER | FK → ZTRACASE.Z_PK |
| ZTITLE | VARCHAR | Transcript display name |

### ZTRATRANSCRIPTLINE (Entity 9)

Individual lines of transcript text. This is where timestamps and content live.

| Column | Type | Description |
|--------|------|-------------|
| Z_PK | INTEGER | Primary key |
| Z_ENT | INTEGER | Always 9 |
| Z_OPT | INTEGER | Always 1 |
| ZHIGHLIGHTCOLOR | INTEGER | Highlight color (0 = none) |
| ZISCONTINUATION | INTEGER | Boolean: continuation of previous line |
| ZISFOOTER | INTEGER | Boolean: footer line |
| ZISHEADER | INTEGER | Boolean: header line |
| ZISMARKED | INTEGER | Boolean: marked/flagged |
| ZISQUESTION | INTEGER | Boolean: question line |
| ZISREDACTED | INTEGER | Boolean: redacted |
| **ZLENGTH** | INTEGER | Character count of ZTEXT |
| **ZPHYSICALLINENUMBER** | INTEGER | Sequential line number (1-based) |
| **ZTIMECODEMS** | INTEGER | **Timestamp in milliseconds** — the KEY field |
| **ZTRANSCRIPTLINENUMBER** | INTEGER | Line number on page (1-based) |
| **ZTRANSCRIPTPAGENUMBER** | INTEGER | Page number (always 1 for audio/video) |
| ZUNDERSCORECOLOR | INTEGER | Underscore/underline color (0 = none) |
| ZFLAG | INTEGER | Flag reference (NULL if none) |
| ZFLAGIBEGIN | INTEGER | Flag begin position |
| ZFLAGIEND | INTEGER | Flag end position |
| **ZPARENTTRANSCRIPT** | INTEGER | FK → ZTRATRANSCRIPT.Z_PK |
| **ZTEXT** | VARCHAR | Line text content |
| ZUNREDACTEDTEXT | VARCHAR | Original text before redaction (NULL if not redacted) |
#### Timestamp Rendering

TranscriptPad renders timestamps from two sources:

1. **Left-margin blue column**: Derived from `ZTIMECODEMS`. Shows minutes (and hours if applicable) in the format `MM:` or `HH:MM:`. For example, `ZTIMECODEMS = 126000` (2 minutes, 6 seconds) renders as `02:` in the left column.

2. **Text body prefix**: The `ZTEXT` field should start with `:SS` (seconds portion). For example: `  :06 - Speaker Name - Content text here`.

Combined, the user sees: `02:` in the margin + `:06 - Speaker Name - Content` in the text = `02:06` as the full timestamp.

#### Text Format Convention

For audio/video transcripts with timestamps:
```
  :SS - Speaker Name - Content text
```
- Two leading spaces
- Colon + two-digit seconds
- Space-dash-space separator
- Speaker name
- Space-dash-space separator
- Content text

### ZTRADOCUMENT (Entity 3)

Media document entries (audio/video files).

| Column | Type | Description |
|--------|------|-------------|
| Z_PK | INTEGER | Primary key |
| Z_ENT | INTEGER | Always 3 |
| Z_OPT | INTEGER | Optimistic lock counter |
| ZSIZE | INTEGER | File size in bytes |
| ZSORTORDEROBJECT | INTEGER | Sort position |
| **ZFILE** | INTEGER | FK → ZTRACASEFILE.Z_PK |
| **ZPARENTCASE** | INTEGER | FK → ZTRACASE.Z_PK (usually 1) |
| ZPARENTFOLDER | INTEGER | FK → ZTRAFOLDER.Z_PK (NULL if root) |
| ZLASTOPENEDDATE | TIMESTAMP | Last opened date |
| **ZFILETYPE** | VARCHAR | Always `'video'` for media (even audio files) |
| ZLEGACYFILENAMEFROMMIGRATION | VARCHAR | Legacy field |
| **ZTITLE** | VARCHAR | Display title |

**Important**: Set `ZFILETYPE = 'video'` for ALL media files, including audio-only files (.mp3, .wav). This enables the media player in the TranscriptPad UI.
### Z_3VIDEOTRANSCRIPTS (Join Table)

Links documents (media) to transcripts. This is the critical relationship that enables transcript-to-media sync/playback.

| Column | Type | Description |
|--------|------|-------------|
| **Z_3VIDEOS** | INTEGER | FK → ZTRADOCUMENT.Z_PK |
| **Z_7VIDEOTRANSCRIPTS** | INTEGER | FK → ZTRATRANSCRIPT.Z_PK |
| **Z_FOK_3VIDEOS** | INTEGER | Always `2048` (observed constant) |

### importedFiles.json

JSON file at the root of the `.tracase` package. Maps UUIDs (used as filenames in `ImportedFiles/`) to original file paths:

```json
{
  "A1B2C3D4-E5F6-7890-ABCD-EF1234567890": "/original/path/to/transcript.txt",
  "F9E8D7C6-B5A4-3210-FEDC-BA0987654321": "/original/path/to/video.mp4"
}
```

## Relationships Diagram

```
ZTRACASE (1)
  └─── ZTRACASEFILE (2) ──┬── .txt files ──→ ZTRATRANSCRIPT (7)
       (ZPARENTCASE)      │   (ZTRANSCRIPT)      │
                          │                       └──→ ZTRATRANSCRIPTLINE (9)
                          │                            (ZPARENTTRANSCRIPT)
                          │
                          └── media files ──→ ZTRADOCUMENT (3)
                              (no direct FK)    (ZFILE → ZTRACASEFILE.Z_PK)
                                                  │
                                                  └──→ Z_3VIDEOTRANSCRIPTS
                                                       (Z_3VIDEOS → ZTRADOCUMENT.Z_PK,
                                                        Z_7VIDEOTRANSCRIPTS → ZTRATRANSCRIPT.Z_PK)
```
## Common Operations

### Insert a new transcript line

```sql
INSERT INTO ZTRATRANSCRIPTLINE (
    Z_PK, Z_ENT, Z_OPT,
    ZHIGHLIGHTCOLOR, ZISCONTINUATION, ZISFOOTER, ZISHEADER,
    ZISMARKED, ZISQUESTION, ZISREDACTED,
    ZLENGTH, ZPHYSICALLINENUMBER, ZTIMECODEMS,
    ZTRANSCRIPTLINENUMBER, ZTRANSCRIPTPAGENUMBER,
    ZUNDERSCORECOLOR, ZFLAG, ZFLAGIBEGIN, ZFLAGIEND,
    ZPARENTTRANSCRIPT, ZTEXT, ZUNREDACTEDTEXT
) VALUES (
    <next_pk>, 9, 1,
    0, 0, 0, 0,
    0, 0, 0,
    <char_count>, <line_num>, <timestamp_ms>,
    <line_on_page>, 1,
    0, NULL, NULL, NULL,
    <transcript_pk>, '<formatted_text>', NULL
);
```

### Link a media document to a transcript

```sql
-- 1. Insert case file
INSERT INTO ZTRACASEFILE (Z_PK, Z_ENT, Z_OPT, ZPARENTCASE, ZSIZE, ZFILENAME, ZORIGINALFILEPATH, ZUUID)
VALUES (<next_pk>, 2, 1, 1, <size>, '<filename>', '<path>', '<uuid>');

-- 2. Insert document
INSERT INTO ZTRADOCUMENT (Z_PK, Z_ENT, Z_OPT, ZSIZE, ZSORTORDEROBJECT, ZFILE, ZPARENTCASE, ZFILETYPE, ZTITLE)
VALUES (<next_pk>, 3, 1, <size>, <sort>, <casefile_pk>, 1, 'video', '<title>');

-- 3. Link to transcript
INSERT INTO Z_3VIDEOTRANSCRIPTS (Z_3VIDEOS, Z_7VIDEOTRANSCRIPTS, Z_FOK_3VIDEOS)
VALUES (<document_pk>, <transcript_pk>, 2048);
-- 4. Update primary key counters
UPDATE Z_PRIMARYKEY SET Z_MAX = <new_max> WHERE Z_ENT = 2;
UPDATE Z_PRIMARYKEY SET Z_MAX = <new_max> WHERE Z_ENT = 3;
```

### Query timestamp status

```sql
-- Check if timestamps are properly set (non-zero ZTIMECODEMS)
SELECT ZPARENTTRANSCRIPT, COUNT(*) as lines,
       MIN(ZTIMECODEMS) as min_ms, MAX(ZTIMECODEMS) as max_ms,
       SUM(CASE WHEN ZTIMECODEMS = 0 THEN 1 ELSE 0 END) as zero_count
FROM ZTRATRANSCRIPTLINE
GROUP BY ZPARENTTRANSCRIPT;
```

## TranscriptPad App Paths

| Path | Purpose |
|------|---------|
| `~/Library/Mobile Documents/com~apple~CloudDocs/LIT SUITE/TranscriptPad/` | iCloud case storage |
| `~/Library/Containers/com.litsoftware.transcriptpad/Data/Library/Application Support/com.litsoftware.transcriptpad/Inbox/` | File import inbox |
| Evidence folder within client directory | Portable case copy |