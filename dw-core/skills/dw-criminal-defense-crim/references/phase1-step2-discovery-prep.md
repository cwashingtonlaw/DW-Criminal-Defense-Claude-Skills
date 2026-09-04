# Phase 1 Step 2 — Prepare Discovery for Review (Detailed)

Read from SKILL.md **Phase 1 Step 2** — the full 2a–2f procedure (download log, Bate-stamping, evidence-folder duplication, document separation, transcription routing, placeholder generation) and the Step 2 Check.

*Converts raw discovery into organized, Bate-stamped, searchable files. Folder sorting runs in parallel with OCR — do not wait for OCR to begin sorting.*

**2a — Download & Organize Discovery**
- Sort all downloaded files into `01 - Pleadings` and `02 - Discovery` subfolders in the Pretrial Notebook.
- Move audio/video files to `05 - Evidence` in the Trial Notebook only — no duplicates.
- Generate a **Download Log**: date received, production set name, file count, total pages (estimated).
- Flag image-only PDFs (need OCR) vs. text-searchable PDFs.
- **Staff action (parallel):** Run OCR on all flagged image-only PDFs using Adobe Acrobat Professional, PDF Expert, or ScanSnap.

**2b — Bate-Stamp Documents**
**Maintain:** `Bate Stamp Master Log.xlsx` as the single source of truth.

Log columns: Production Set | Date Received | Start Number | End Number | Staff Member | Date Stamped

Rules:
- Sequential numbering in order received. Never restart mid-case. Continuous across all production dates.
- Before any new stamping: check log for current highest number, output the next available.
- After stamping: update log immediately — no batch updates.
- Flag any numbering gap — alert staff before proceeding.
- Flag any overlap (duplicate numbers) — halt until resolved.

**2c — Duplicate Discovery to Evidence Folder**
- Copy all Bate-stamped, OCR'd documents to `05 - Evidence` in the Trial Notebook.
- Run file count and size comparison between source and destination.
- Flag any file that failed to copy or shows a size mismatch.
- Do not proceed to 2d until copy is 100% verified.

**2d — Separate Discovery into Individual Documents**
- Review the State's index to identify document divisions and names.
- Split the combined PDF into individual files at the State's document boundaries.
- Apply naming convention: `[3-digit prefix] - [Document Name]` with sequential numbering starting at `001` (e.g., `001 - Bill of Information`, `002 - Incident Report`). Assign the next consecutive number to each document — never skip numbers.
- Create subfolders for multi-file audio/video using the same sequential number (e.g., `008 - Body Camera Footage/`).
- Output a **Separation Checklist**: expected document count (from State index) vs. actual file count.
- Flag any document in the State's index with no corresponding file — log in Report 7 queue.

**2e — Transcribe Interviews & Digital Media**
Route to **dw-transcript-router-crim** for parish-based pipeline selection (JusticeText for Calcasieu, Rev for all other parishes). The router handles upload, transcription, TranscriptPad import, and Defense Media Analysis Report generation.
- When transcripts return: name each transcript PDF identically to its audio/video file, save in the same folder.
- Add transcript as a separate row in the Evidence Table, with its own Evidence Number and its own page count (the media row keeps the `A/V — HH:MM:SS` runtime).
- Confirm every audio/video file has a corresponding transcript before proceeding.

**2f — Digital Evidence Handling — Generate Placeholders**
Media folders (photos, videos, audio, surveillance, body cam footage) cannot be Bate-stamped like documents. Each media folder needs a **Digital Evidence Placeholder** — a one-page PDF that sits in the evidence sequence and describes the folder's contents. Optionally route complex media analysis to **dw-evidence-placeholder-crim** skill for full inventory generation.

**Run the bundled generator script:**
```bash
python3 <skill-directory>/scripts/generate_placeholders.py \
  --evidence-dir "<path-to-05-Evidence>" \
  [--folders "folder1" "folder2" ...]  # optional: specific folders only
```

If `--folders` is omitted, the script processes all subfolders automatically. The script scans each subfolder for file counts, types, and size; classifies contents by media type (Audio, Photo/Image, Video, Other Data); generates a one-page PDF placeholder matching the firm's template layout (defined in `assets/Evidence_Placeholder_Template.md`); and names each PDF identically to its source folder.

**Workflow:**
- Identify every subfolder in `05 - Evidence` that contains media files
- Confirm scope with user — default to processing all folders unless told otherwise
- Skip folders that already have a corresponding placeholder PDF (use `--force` to regenerate)
- After running, report: total placeholders created, any folders skipped, breakdown by media type

**✓ Step 2 Check:**
- [ ] File count in Evidence Folder matches downloaded discovery
- [ ] Bate Stamp Log shows no gaps or overlaps
- [ ] All image-only PDFs have been OCR'd and confirmed text-searchable
- [ ] No documents in the State's index are absent from the Evidence Folder
- [ ] Separation Checklist: expected count = actual count
- [ ] Every audio/video file has a corresponding transcript entry
- [ ] Digital Evidence Placeholder PDF exists for every media folder in `05 - Evidence`
