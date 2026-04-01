---
name: dw-transcript-pipeline
description: >
  End-to-end audio/video transcription pipeline for Daniels & Washington. Scans a client
  folder for media files, guides the attorney through JusticeText upload, monitors
  transcription, downloads PDF and TXT transcripts, and imports everything into TranscriptPad
  with media sync and timestamps. Use this skill any time an attorney says: "transcribe the
  evidence," "upload to JusticeText," "transcript pipeline," "process audio/video," "send
  files to JusticeText," "import into TranscriptPad," "sync transcript to video," "transcribe
  jail calls," "transcribe body cam," "transcribe the interview," "process the recordings,"
  or references a client folder containing media discovery files. Also triggers on any mention
  of TranscriptPad import, JusticeText upload, "process the [client] folder," "add more
  recordings to TranscriptPad," or "new evidence recordings."
---

# DW Transcript Pipeline

Transcription pipeline: local folder → JusticeText → TranscriptPad.

## Automation Boundaries

**Claude automates:** folder scan, duplicate detection, JusticeText workspace nav, transcription
status checks, PDF/TXT download, TranscriptPad case creation, transcript import, media linkage
(direct SQLite), and timestamp correction.

**Attorney must do manually (two steps only):**
1. **Upload** — Select and upload media files into JusticeText (file_upload is not available in
   the Claude in Chrome extension; see Known Limitations)
2. **Verify** — Open TranscriptPad and click each transcript to confirm timestamps render in the
   left-margin column (AppleScript cannot render the Catalyst content pane; see Known Limitations)

## Prerequisites

- **Claude in Chrome** MCP tools (JusticeText browser automation)
- **Cowork filesystem access** to the client folder
- **macOS `osascript`** via Desktop Commander or Control your Mac MCP
- **Python 3** on the host Mac
- Attorney is logged into JusticeText at `platform.justicetext.com`
- TranscriptPad is installed with an active LIT SUITE subscription

If any are missing, tell the attorney which tools need to be enabled and stop.

---

## Phase 1: Folder Scan

### Step 1.1 — Get the target folder

The attorney should have the client folder selected in Cowork. The folder name follows the
`lastname, firstname` convention and is used to match or create the JusticeText workspace and
TranscriptPad case. If not selected, use `request_cowork_directory` to ask.

### Step 1.2 — Scan for media files

Recursively scan all subfolders. Collect every file with these extensions (case-insensitive):

- **Video**: `.mp4`, `.mov`, `.avi`, `.wmv`, `.mkv`, `.flv`, `.webm`, `.m4v`, `.mpg`, `.mpeg`,
  `.3gp`, `.ts`, `.vob`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.m4a`, `.ogg`, `.flac`, `.wma`, `.aiff`, `.aif`, `.opus`,
  `.amr`

**Skip files whose name (without extension) already ends with `_TRANSCRIBED`.** These have
already been processed in a previous run — the `_TRANSCRIBED` suffix is the pipeline's natural
checkpoint for Phase 1.

### Step 1.3 — Detect duplicates

Flag files with the same base name across different paths or sizes. Common D&W patterns:
- Numbered-prefix copies (e.g., `025 - CP176-A.mp4` vs `CP176-A.mp4`) — smaller file is usually compressed
- Files duplicated across the evidence root and numbered subfolders

Present duplicates and ask the attorney which to include.

**Large file warning**: Flag files over 500MB — TranscriptPad copies media into the `.tracase` package, doubling storage. Offer a compressed version if available.

### Step 1.4 — Present file list and confirm

Show a summary table: client folder name, total files, each file (name, subfolder, size,
type), skipped `_TRANSCRIBED` files, and excluded duplicates. Confirm before proceeding. Stop
if zero unprocessed files are found.

---

## Phase 2: JusticeText Upload & Transcription

### Step 2.1 — Navigate to JusticeText

Navigate to `https://platform.justicetext.com`. Confirm the attorney is logged in (workspace
list visible). If a login screen appears, ask them to log in and then resume.

### Step 2.2 — Find or create the workspace

Look for a workspace matching `lastname, firstname` in the left sidebar under "Workspaces."

- **Found**: Click it to open
- **Not found**: Click the `add_box` icon next to "Workspaces," name it exactly as the folder is named
- **Multiple partial matches**: Show options and ask which to use

### Step 2.3 — Upload media files (MANUAL — Attorney Action Required)

Before giving upload instructions, ask the attorney which shared drive the files are on. D&W
handles cases across multiple parishes (Calcasieu, Orleans, Jefferson, etc.), each with its own
shared drive. Do not assume a specific drive path — ask first.

> I've opened the **[client name]** workspace in JusticeText. Please upload the [N] media files:
>
> 1. Click the purple **"Upload files"** button (top right)
> 2. Click **"Media, PDF"**
> 3. In the upload dialog, click **"Google Drive"**
> 4. Navigate to: **Shared drives → [PARISH] PDO Files → [client folder] → 01 - Trial Notebook → 05 - Evidence**
> 5. Navigate into each subfolder and select the files listed below
>
> [List files from Phase 1, grouped by subfolder]
>
> If files are on a local drive or NAS, click **"Select files"** under "Upload from your computer" instead.
>
> Let me know when upload is complete.

**Wait for attorney confirmation before proceeding.**

### Step 2.4 — Verify upload and transcription status

After attorney confirms:
1. Scan the workspace file list
2. Confirm each expected file appears
3. Check status for each:
   - **"Uploading" / "Processing"**: Still ingesting — wait and recheck
   - **"Transcribing" / "In progress"**: AI transcription running
   - **"Not reviewed" / "Ready"**: Transcription complete ✓
   - **"Failed" / "Error"**: Flag to attorney

JusticeText typically auto-transcribes on upload. If not, look for a "Transcribe" button and ask.

### Step 2.5 — Monitor progress

If transcription is still running, tell the attorney they can ask to "check transcript status for
[client name]" at any time. Claude will navigate to the workspace and report status.

**Time expectations**: JusticeText transcription typically takes 15–45 minutes per hour of audio,
depending on audio quality and server load. Low-quality recordings (jail calls, body cam with
background noise) tend toward the longer end. For a batch of 10+ files, expect 1–3 hours total.
Let the attorney know so they can plan accordingly.

Status polling is performed manually via Claude in Chrome — just ask to "check transcript status for
[client name]" at any time.

---

## Phase 2.5: Transcript Review & Speaker Labeling (Attorney Action)

Before downloading transcripts, the attorney should review and edit them in JusticeText. This is
the platform's core value — skipping this step means the transcripts imported into TranscriptPad
will have generic speaker labels ("Speaker 1," "Speaker 2") and uncorrected transcription errors.

> Transcription is complete for all [N] files. Before I download, please review the transcripts
> in JusticeText:
>
> 1. **Label speakers** — Click each transcript and assign real names (e.g., "Det. Jones,"
>    "Defendant," "Victim") to replace "Speaker 1," "Speaker 2," etc.
> 2. **Fix errors** — Correct any transcription mistakes, especially names, addresses, and
>    dates that the AI may have misheard
> 3. **Add annotations** — Flag important moments if you'd like them in the PDF export
>
> Once you're satisfied with the transcripts, let me know and I'll download them.

**Wait for attorney confirmation before proceeding to Phase 3.**

---

## Phase 3: Download Transcripts

When the attorney confirms transcripts are reviewed and all files show complete status:

### Step 3.1 — Download PDF and TXT for each file

For each transcribed file:
1. Click the file to open the transcript view
2. Locate the export/download button ("Export," "Download," or download icon)
3. Download **PDF** — include: summary, timestamps, speakers, annotations
4. Return to the transcript view, download **TXT** — include: timestamps, speakers; exclude: summary, annotations

### Step 3.2 — Verify and move transcripts to evidence folder

Locate newly downloaded files in `~/Downloads` (match by filename and recent modification time).

**Verify each downloaded file is not empty or truncated:**
- PDF files should be > 10 KB (an empty/failed PDF export is typically < 5 KB)
- TXT files should be > 1 KB (an empty/failed TXT export is typically < 500 bytes)
- If any file fails this check, re-download it. If it fails again, flag to the attorney.

Rename each to match the original media filename and move to the **same directory** as the source file:

- `<original-filename-without-extension>.pdf`
- `<original-filename-without-extension>.txt`

Example: source at `032 - Item 8 interview/DET-2_Primary_1273_09052024220152.mp4` → save as
`DET-2_Primary_1273_09052024220152.pdf` and `.txt` in that same subfolder.

### Step 3.3 — Confirm downloads

Show the attorney each original file with its corresponding transcript file paths and sizes.

---

## Phase 4: TranscriptPad Import

Uses a **hybrid approach**: AppleScript UI for case creation and transcript import, plus
**direct SQLite manipulation** for media linkage and timestamps (Catalyst limitations make
UI-based media import unreliable). See `references/transcriptpad-database.md` for full schema.

### .tracase Package Structure

```
CaseName.tracase/
├── ImportedFiles/          ← UUID-named copies of all imported media (NO file extension)
├── StoreContent/
│   └── persistentStore     ← SQLite Core Data database
└── importedFiles.json      ← Maps UUIDs to original file paths
```

Maintain copies in two locations:
1. **Evidence folder** — inside the client's evidence directory
2. **iCloud**: `~/Library/Mobile Documents/com~apple~CloudDocs/LIT SUITE/TranscriptPad/`

### Step 4.1 — Find or create TranscriptPad case

**Check for an existing case first.** Search both the evidence folder and iCloud location for
a `.tracase` matching the client name. If one exists:
- Ask the attorney: "A TranscriptPad case for [client name] already exists. Should I add the
  new transcripts and media to it, or create a fresh case?"
- **Add to existing**: Skip case creation, proceed to Step 4.2 with the existing case path.
  Query the existing database to find current max PKs before inserting new records.
- **Create fresh**: Delete the existing `.tracase` from both locations, then create new.

**To create a new case** (AppleScript):

```applescript
tell application "TranscriptPad" to activate
delay 3
tell application "System Events"
    tell process "TranscriptPad"
        click menu item "New" of menu "File" of menu bar 1
        delay 2
        -- Select "Empty Case File" from template chooser
        delay 1
        keystroke "lastname, firstname"
        delay 0.5
        -- "Done" button may ignore element-level click; use coordinate click:
        -- click at {centerX, centerY}  (calculate from position + size)
        key code 36 -- Return fallback
        delay 2
    end tell
end tell
```

### Step 4.2 — Stage transcripts in TranscriptPad Inbox

Copy each `.txt` file to the Inbox directory:

```bash
INBOX="$HOME/Library/Containers/com.litsoftware.transcriptpad/Data/Library/Application Support/com.litsoftware.transcriptpad/Inbox"
mkdir -p "$INBOX"
cp "/path/to/transcript1.txt" "$INBOX/"
# repeat for all .txt files
```

### Step 4.3 — Import via Add menu (AppleScript)

```applescript
tell application "System Events"
    tell process "TranscriptPad"
        -- Use the pop up button with description "Add" (NOT the doc.badge.plus button)
        set addBtn to first pop up button of window 1 whose description is "Add"
        perform action "AXShowMenu" of addBtn  -- regular click may not work
        delay 1
        click menu item 1 of menu 1 of addBtn  -- "New Files (N)"
        delay 2
        -- In the file selection sheet: Select All Files → Import Selected Files → Done
    end tell
end tell
```

After import, each transcript has a `Z_PK` in `ZTRACASEFILE` and a linked entry in `ZTRATRANSCRIPT`.

### Step 4.4 — Back up the case package

**Before any direct database manipulation, back up the entire `.tracase` package.** If a bad
insert or PK conflict corrupts the Core Data database, this backup is the only recovery path.

```bash
CASE_PATH="/path/to/CaseName.tracase"
cp -r "$CASE_PATH" "${CASE_PATH}.backup-$(date +%Y%m%d-%H%M%S)"
```

Also **close TranscriptPad** before modifying the database — Core Data does not tolerate
concurrent writes from external processes.

### Step 4.5 — Determine current primary key values

Before inserting any records, query the current max PKs from the database. Every `INSERT` must
use a PK higher than the current max, and you must update `Z_PRIMARYKEY` after all inserts.

```sql
-- Get current max PKs for each entity type you'll insert into
SELECT Z_ENT, Z_MAX FROM Z_PRIMARYKEY WHERE Z_ENT IN (2, 3, 9);
-- Z_ENT 2 = TRACaseFile
-- Z_ENT 3 = TRADocument
-- Z_ENT 9 = TRATranscriptLine
```

Use these values as your starting point. Increment sequentially for each new record (e.g., if
`Z_MAX` for entity 2 is 14, your first new TRACaseFile gets `Z_PK = 15`, the next gets 16, etc.).

### Step 4.6 — Add media files (Filesystem + SQLite)

**Copy media into ImportedFiles — files are stored WITHOUT their extension:**
```bash
CASE_PATH="/path/to/CaseName.tracase"
UUID=$(uuidgen | tr '[:lower:]' '[:upper:]')
# CRITICAL: the destination filename is the bare UUID with NO extension
cp "/path/to/media_file.mp4" "$CASE_PATH/ImportedFiles/$UUID"
```

TranscriptPad identifies file types from `importedFiles.json` and database metadata, not from
the filename extension. If you accidentally copy as `$UUID.mp4` instead of just `$UUID`, the
media player will not find the file.

**Update importedFiles.json** — read existing JSON, add `"UUID": "/original/path/to/file.mp4"`, write back.

**Insert database records** (using PKs from Step 4.5):

```sql
-- ZTRACASEFILE: register the file
INSERT INTO ZTRACASEFILE (Z_PK, Z_ENT, Z_OPT, ZPARENTCASE, ZSIZE, ZFILENAME, ZORIGINALFILEPATH, ZUUID)
VALUES (<next_pk>, 2, 1, 1, <file_size>, '<filename>', '<original_path>', '<UUID>');

-- ZTRADOCUMENT: create document entry
-- Use 'video' for ALL media types (audio and video) to enable the media player
INSERT INTO ZTRADOCUMENT (Z_PK, Z_ENT, Z_OPT, ZSIZE, ZSORTORDEROBJECT, ZFILE, ZPARENTCASE,
    ZPARENTFOLDER, ZLASTOPENEDDATE, ZFILETYPE, ZTITLE)
VALUES (<next_pk>, 3, 1, <file_size>, <sort_order>, <casefile_pk>, 1, NULL, NULL, 'video', '<title>');

-- Z_3VIDEOTRANSCRIPTS: link document to transcript
INSERT INTO Z_3VIDEOTRANSCRIPTS (Z_3VIDEOS, Z_7VIDEOTRANSCRIPTS, Z_FOK_3VIDEOS)
VALUES (<document_pk>, <transcript_pk>, 2048);  -- Z_FOK_3VIDEOS is always 2048

-- After ALL inserts, update max PK counters
UPDATE Z_PRIMARYKEY SET Z_MAX = <new_max> WHERE Z_ENT = 2;  -- TRACaseFile
UPDATE Z_PRIMARYKEY SET Z_MAX = <new_max> WHERE Z_ENT = 3;  -- TRADocument
```

### Step 4.7 — Fix timestamps (Python + SQLite)

JusticeText `.txt` exports use `[MM:SS] Speaker Name:` format. TranscriptPad needs:
- **ZTIMECODEMS**: timestamp in milliseconds
- **ZTEXT**: `  :SS - Speaker - Content`

Run `references/transcriptpad-timestamp-fix.py`, updating `TRANSCRIPT_FILES` (Z_PK → `.txt` path)
and `CASE_PATHS` before executing:

```bash
python3 /tmp/fix_timestamps.py
```

Verify after:
```sql
SELECT ZPARENTTRANSCRIPT, COUNT(*), MIN(ZTIMECODEMS), MAX(ZTIMECODEMS)
FROM ZTRATRANSCRIPTLINE GROUP BY ZPARENTTRANSCRIPT;
```

### Step 4.8 — Sync both case locations

Copy the completed `.tracase` package to the secondary location (evidence folder or iCloud),
or run the timestamp script against both `CASE_PATHS` simultaneously.

### Step 4.9 — Rename processed media files

Add `_TRANSCRIBED` suffix to each original media file (not to PDF/TXT transcripts):

`interview_jones.mp4` → `interview_jones_TRANSCRIBED.mp4`

### Step 4.10 — Attorney verification (MANUAL)

> Transcripts and media are imported. Please:
> 1. Open TranscriptPad and open the **[client name]** case
> 2. Click each transcript in the sidebar
> 3. Confirm timestamps appear in the blue left-margin column
> 4. Click play to confirm media playback
>
> Expected display: left column shows `02:`, line starts with `:06 - Speaker - text`

### Step 4.11 — Update case brain

If the `dw-case-brain` skill is available, write a session update summarizing the pipeline run:

> Transcription pipeline completed for [client name]: [N] media files processed. Transcripts
> downloaded from JusticeText (PDF + TXT) and placed alongside source media in evidence folder.
> All files imported into TranscriptPad case "[lastname, firstname]" with media linked and
> timestamps synced. Original media files renamed with _TRANSCRIBED suffix. Attorney
> verification pending.

This ensures the next session has full context about what was done without the attorney
needing to re-explain.

---

## Known Limitations

**TranscriptPad Catalyst content pane**: Clicking transcript items via AppleScript accessibility
API never renders the content pane (shows "No File Selected"). This is a macOS Catalyst framework
limitation — human mouse clicks work correctly. All data setup is handled via direct SQLite
manipulation; attorney manually clicks through to verify. AppleScript *can* reliably launch the
app, create cases, trigger the Add popup, and navigate import dialogs — it just cannot render
content or trigger playback.

**JusticeText file upload**: `file_upload` via the Chrome DevTools Protocol is globally disabled
in the current Claude in Chrome extension (affects Google Drive paths, SMB mounts, and local
files identically). Upload must be done manually. See `references/justicetext-architecture.md`
for potential future API upload route.

**JusticeText TXT format**: Exports include a header section followed by transcript blocks.
The timestamp regex handles both `[MM:SS]` and `[HH:MM:SS]` formats. If JusticeText changes
their export format, update the regex in the timestamp fix script:
`\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s+(.+?):\s*\n(.*?)(?=\n\[\d{1,2}:\d{2}|\Z)`

---

## Error Handling

- **Upload issues**: Try one file at a time; check file size limits; use local file picker instead of Google Drive picker
- **Transcription timeout**: Alert attorney if a file hasn't completed after 24 hours
- **"Done" button unresponsive**: Calculate center from position + size, use `click at {centerX, centerY}`
- **AppleScript returns empty**: Add 3–6 second delays after app launch before querying elements
- **Python script path issues**: Cowork VM paths (`/sessions/...`) don't exist on the host Mac — write scripts to `/tmp/` via Desktop Commander, then execute from there
- **File naming conflict**: Ask the attorney whether to overwrite or add a numeric suffix
- **Large batches (20+ files)**: Process in batches of 10; checkpoint after each batch
- **Download location**: If files aren't in `~/Downloads`, ask where Chrome saves downloads
- **iCloud sync conflicts**: Delete existing `.tracase` from iCloud before creating a new case
- **Database corruption**: Restore from the `.tracase.backup-*` created in Step 4.4. If no backup exists, the attorney may need to recreate the case from scratch.
- **Empty/truncated downloads**: Re-download the file. If it fails twice, flag to the attorney — the JusticeText export may have an issue.

### AppleScript Fallback — Manual Steps

If AppleScript automation fails repeatedly for case creation (Step 4.1) or transcript import
(Step 4.3), the attorney can do these two steps manually in about 60 seconds. Everything
else — media files in `ImportedFiles/`, database records, transcript-to-media links,
timestamps — is set up via direct filesystem and SQLite operations that don't depend on
AppleScript. Tell the attorney:

> AppleScript automation is having trouble with TranscriptPad. You can do these two steps
> manually — everything else is already set up:
>
> 1. **Create the case**: Open TranscriptPad → File → New → Empty Case File → name it
>    "[lastname, firstname]"
> 2. **Import transcripts**: Click the **Add** button (the one with a "+" icon, not the
>    report icon) → "New Files" → Select All → Import
>
> Once that's done, let me know and I'll continue with the media linking and timestamps.

### Pipeline Failure Recovery

If the pipeline fails mid-run, report exactly where it stopped and what has already been
completed. For example:

> Pipeline stopped at Phase 4, Step 4.6 (media file insertion). Here's what's done:
> - ✅ Phase 1–3: All [N] transcripts downloaded and placed in evidence folder
> - ✅ Step 4.1–4.3: TranscriptPad case created, transcripts imported
> - ✅ Step 4.4: Backup exists at [path]
> - ❌ Step 4.6: 3 of 8 media files inserted before error
>
> To resume, say "pick up the transcript pipeline from Step 4.6" and I'll continue
> from where I left off.

The `_TRANSCRIBED` suffix on media files also serves as a natural checkpoint — re-running
the pipeline skips already-processed files in Phase 1.

---

## Status Check

If the attorney asks to "check transcript status" or "check on [client] transcriptions":
1. Navigate to the JusticeText workspace via Claude in Chrome
2. Read each file's status column
3. Report complete, in-progress, and failed files
4. For completed files, ask if the attorney wants to proceed with download and TranscriptPad import

---

## Quick Reference

| Step | Platform | Method | Who |
|------|----------|--------|-----|
| Scan folder | Local | Filesystem / Bash | **Claude** |
| Detect duplicates | Local | Filesystem | **Claude** |
| Open JusticeText workspace | JusticeText | Claude in Chrome | **Claude** |
| Upload media files | JusticeText | Google Drive / local file picker | **Attorney** |
| Verify uploads + transcription status | JusticeText | Claude in Chrome | **Claude** |
| Review transcripts + label speakers | JusticeText | Manual review | **Attorney** |
| Download PDF + TXT transcripts | JusticeText | Claude in Chrome | **Claude** |
| Verify downloads (size check) | Local | Filesystem | **Claude** |
| Move transcripts to evidence folder | Local | Filesystem | **Claude** |
| Find or create TranscriptPad case | TranscriptPad | AppleScript UI (or manual fallback) | **Claude** |
| Back up .tracase package | Local | Filesystem | **Claude** |
| Stage transcripts in Inbox | Local | Filesystem | **Claude** |
| Import transcripts via Add menu | TranscriptPad | AppleScript UI (or manual fallback) | **Claude** |
| Copy media into case + link in database | Local | Filesystem + SQLite | **Claude** |
| Fix timestamps | TranscriptPad | Python + SQLite | **Claude** |
| Sync both case locations | Local | Filesystem | **Claude** |
| Rename originals with _TRANSCRIBED | Local | Filesystem | **Claude** |
| Verify rendering + playback | TranscriptPad | Manual click-through | **Attorney** |
| Update case brain | dw-case-brain | Session update | **Claude** |
