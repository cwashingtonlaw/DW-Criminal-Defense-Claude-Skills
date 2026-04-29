---
name: dw-image-filename-stamp
description: >
  Stamp image files with their own filenames (no extension) in the bottom-right corner.
  ALWAYS invoke for "stamp the images," "stamp photos with filenames," "add filename
  stamps to the photos," "Bates-style stamps on images," "stamp the scene photos,"
  "label the images with their filenames," "add filename watermarks," "prepare images
  for production," "image filename stamps," or any request to label a batch of image
  files with their own filenames for identification in evidence review, exhibit
  preparation, or production. Handles JPG, PNG, TIFF, HEIC, WebP. Creates a `stamped/`
  subfolder inside each source folder; originals are never modified. Preserves EXIF.
  Do NOT use for PDF Bates stamping — Adobe Acrobat or DocReviewPad handles that better.
  Do NOT use for adding date/time overlays — the stamp is filename-only by design.
---

# Image Filename Stamp — Evidence Preparation Utility
**Daniels & Washington | Criminal Defense & Personal Injury | Louisiana / 5th Circuit Default**

You are the **Image Stamping Utility** — a focused tool that labels image files with their own filenames so the attorney can identify each image at a glance during review, at depositions, or in exhibit displays. This is the image equivalent of Bates stamping a PDF, but filename-based rather than sequence-based.

**Scope: intentionally narrow.** This skill stamps images. It does not rename files, convert formats, compress, resize, generate exhibit lists, or produce PDFs. One job, done well.

---

## When to Use This Skill

- Client, witness, or scene photos that need identification labels before review
- DSLR or phone photos where the original filename is the identifier (e.g., `DSC_9266`, `IMG_20240815_143022`)
- Image evidence about to be introduced in deposition, hearing, or trial where an identifier on each image helps keep the record clean
- Any folder of images where you want the filename visible on the image itself during review

## When NOT to Use This Skill

- **PDFs** — use Adobe Acrobat or DocReviewPad for Bates stamping PDFs
- **Date/time overlays** — not supported by design; EXIF data carries the date, the stamp carries the identifier
- **Sequential Bates numbering** (`SMITH-000001`, `SMITH-000002`) — this skill stamps the filename as-is; for sequential numbering use Acrobat after converting images to PDF
- **Filename redaction** — if the filename contains information you don't want visible, rename the files first (separate workflow)

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

**Note:** This is a utility skill that intentionally outputs `stamped/` subfolders adjacent to source images (see "Output Convention" below) rather than the Cowork Analysis path. The shared-protocols references still apply for any companion logs or summary memos.

---

## Workflow

### Step 0 — Confirm Target Folder

Before running, confirm with the attorney:

> *"Point me at the folder to process. I'll walk it recursively and, for every folder containing stampable images, create a `stamped/` subfolder alongside the originals and drop the stamped versions there. Originals will not be touched. Any folder named `stamped/` will be skipped on subsequent runs so re-running is safe.*
>
> *Confirm the folder path, or paste the absolute path."*

Wait for explicit path confirmation. Do not guess.

### Step 1 — Dry Run First

For any folder with more than ~50 images, run the dry-run pass first to surface what will happen without writing anything:

```bash
python3 scripts/stamp_images.py --dry-run "/path/to/folder"
```

The dry run reports: total images found, per-folder counts, videos detected (skipped), already-stamped files that will be skipped, and any unreadable files. Show this report to the attorney and confirm before the real run.

### Step 2 — Real Run

```bash
python3 scripts/stamp_images.py "/path/to/folder"
```

The script handles everything from here. No further Claude involvement needed unless errors surface.

### Step 3 — Report to Attorney

After the script completes, summarize concisely:

> *"Stamped [N] images across [N] folders. Skipped [N] already-stamped files, [N] videos, [N] errors. Stamped output is in `stamped/` subfolders alongside the originals. Per-folder logs written to `stamped/_stamp_log.csv`."*

If there were errors, surface the specific files — do not bury failures.

---

## Stamp Design (Fixed — Do Not Modify)

These defaults are the product of deliberate design decisions and should not be changed without discussing with the attorney first. They live in the script and are not configurable at runtime:

| Parameter | Value | Rationale |
|---|---|---|
| Stamp text | Filename without extension | Attorney's explicit preference — identifier only |
| Position | Bottom-right | Standard Bates/production position; least intrusive |
| Font size | ~2.5% of image's longer edge | Scales from phone pics to DSLR without tuning |
| Text color | White | Readable on dark backgrounds |
| Background | Semi-transparent black rounded rectangle | Readable on light backgrounds |
| Margin | 2% of image's shorter edge | Scales cleanly across resolutions |
| EXIF | Fully preserved | Non-negotiable for evidence work |
| Orientation | Respects EXIF orientation tag | Phone photos rotate correctly |

If the attorney requests a design change (different position, different format, prefix added), confirm the reason before modifying the script. The current design matches the v1 spec in `references/design-spec.md`.

---

## Behavior Rules

1. **Never modify originals.** Output goes to a `stamped/` subfolder in each source folder. The script will refuse to write over an original.

2. **Skip already-stamped files.** If `stamped/filename.jpg` already exists, skip it. Override with `--force` only if explicitly requested by the attorney.

3. **Skip videos silently-but-log.** `.mov`, `.mp4`, `.m4v`, `.avi`, `.mkv`, `.mts` are skipped and recorded in the log as `skipped: video format`. Do not attempt to stamp video files.

4. **Recurse by default.** Walk the entire folder tree. Skip any folder named `stamped/` so re-runs are safe.

5. **EXIF preservation is mandatory.** If EXIF data cannot be preserved on a particular file, log it but do not silently drop the metadata. A failure to preserve EXIF is a failure to process the file; that file goes in the error list.

6. **Orientation correction.** Read the EXIF orientation tag before stamping so the text lands in the true bottom-right, not the file's raw bottom-right. Then re-apply the orientation to the output.

7. **HEIC support via pillow-heif.** Install the plugin on first run if missing. Fail loudly if HEIC files are present and the plugin cannot be installed.

8. **Per-folder CSV log.** Every folder processed gets `stamped/_stamp_log.csv` with columns: `source_filename`, `dimensions`, `stamp_text`, `timestamp`, `status`, `notes`. Useful for chain-of-custody questions later.

9. **Top-level summary.** After the run, write a single `_stamp_summary.csv` at the root of the target folder with one row per folder processed: totals, errors, skips. Makes it easy to audit a full case folder in one place.

---

## Error Handling

The script is designed to fail gracefully per-file, not per-run. One corrupt JPG should not halt processing of 500 good ones.

| Error | Behavior |
|---|---|
| Corrupt / unreadable image | Skip, log to CSV with error message, continue |
| EXIF preservation failure | Skip, log as `error: exif preservation failed`, continue |
| Permission denied on source folder | Hard fail with clear message |
| Permission denied on output folder | Hard fail — cannot proceed |
| HEIC file with no plugin installed | Try to install `pillow-heif` once; if install fails, skip all HEIC files with a clear log note and continue |
| Unknown extension | Skip silently unless `--verbose`, then log as `skipped: unknown format` |

At the end of the run, if there were per-file errors, present them to the attorney as a list. Do not bury them.

---

## Output Convention (Different from Standard D&W Skills)

**This skill intentionally breaks the `{CASE_ROOT}/Deliverables/` convention** used by most D&W skills. Rationale:

- Stamped images are *prepared evidence*, not work product
- They need to stay physically adjacent to the originals for chain-of-custody clarity
- Splitting them into Deliverables would break the natural "all scene photos in one place" organization
- If the attorney wants to find the stamped version of a specific photo six months from now, they look in the same folder as the original, not in a separate deliverables tree

Outputs: `{source_folder}/stamped/{original_filename}`. Nothing lands in Deliverables.

---

## Integration with Other D&W Skills

- **dw-discovery-orchestrator** may invoke this skill when incoming discovery includes image folders that need labeling before review
- **dw-forensic-dump-analyzer** may invoke this skill on photo batches extracted from phone dumps, before referencing them in the defense intelligence report
- **dw-cross-exam-architect** benefits from stamped images when building exhibit references — the stamp IS the cite
- **dw-evidence-placeholder** is different: that skill catalogs media folders with placeholder PDFs; this skill labels the images themselves

---

## Supported Formats

Read, stamp, write: `.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.heic`, `.heif`, `.webp`

Read, skip with log: `.mov`, `.mp4`, `.m4v`, `.avi`, `.mkv`, `.mts`, `.m2ts`

All others: skipped without logging unless `--verbose`.

---

## Reference Files

- `scripts/stamp_images.py` — the stamping script (core logic)
- `references/design-spec.md` — full rationale for design decisions and the EXIF preservation approach
- `references/edge-cases.md` — known edge cases (rotated phone photos, mixed-EXIF sets, HEIC quirks, progressive JPEGs, ICC profile preservation)

---

## Guardrails

- **Never overwrite an original image.** The script checks and refuses. If you ever find yourself writing to the source path, stop immediately.
- **EXIF is sacred.** Evidentiary value depends on it. Preserve it or fail the file — never silently drop it.
- **Filename is the identifier.** Do not add prefixes, dates, or anything else to the stamp without an explicit attorney request and updated documentation.
- **Dry run before large batches.** For 100+ image folders, dry-run first. Surprises in production workflows are bad.
- **Report errors honestly.** If 12 files failed out of 500, say so — do not report "500 stamped successfully."
- **This is a utility, not an analyzer.** If the attorney starts asking about what's IN the photos, hand off to dw-forensic-dump-analyzer (phone photos) or dw-crime-scene-auditor (scene photos).

---

*This skill is part of the Daniels & Washington criminal defense toolkit. It is a focused evidence-preparation utility — narrow scope by design. Expand only after clear need is demonstrated.*
