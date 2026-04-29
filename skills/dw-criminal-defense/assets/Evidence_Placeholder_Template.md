# Evidence Placeholder Template — Layout Specification

**For use by `dw-criminal-defense` and `scripts/generate_placeholders.py`. Internal reference.**

This document specifies the layout of the one-page Digital Evidence Placeholder PDFs that `scripts/generate_placeholders.py` writes for each media-evidence subfolder under a case's `Pretrial Notebook → 02 - Discovery` tree. The script is the source of truth for the actual output; this file is the human-readable layout spec used to (a) explain to attorneys what the placeholder pages look like, (b) guide anyone modifying the script, and (c) document the firm convention so the layout stays consistent across cases.

---

## Purpose

When discovery includes large volumes of native-format media (BWC video folders, jail call directories, phone-dump exports, surveillance archives), the firm does not move or duplicate those files into the trial notebook. Instead, the script generates a one-page **placeholder PDF** for each media folder. The PDF lives in the trial notebook at the appropriate exhibit location; the original media stays in the discovery directory. The placeholder is named identically to its source folder so the connection is unambiguous.

The placeholder serves three functions:

1. **Stand-in exhibit** — included in the trial notebook so the attorney has a paginated index entry for the media without bloating the binder with raw files.
2. **Folder summary** — captures file count and media-type composition at a glance.
3. **Pointer to the original** — records the absolute path so the attorney (or co-counsel) can locate the source files quickly during prep or trial.

---

## Page Format

- **Page size:** US Letter (8.5" × 11"), portrait
- **Margins:** 1.0" left and right; content begins 1.0" from top
- **Single page only** — long descriptions and paths word-wrap onto subsequent lines but never spill onto a second page

---

## Content Blocks (top to bottom)

### 1. Title

| Property | Value |
|---|---|
| Text | `DIGITAL EVIDENCE PLACEHOLDER` |
| Font | Helvetica-Bold, 18 pt |
| Position | Centered, 1.0" from top |
| Followed by | 1 pt horizontal rule across the usable width |

### 2. Evidence ID / Name

| Property | Value |
|---|---|
| Label | `EVIDENCE ID/NAME:` (Helvetica-Bold, 11 pt) |
| Value | The folder name (Helvetica, auto-shrinking 10 → 7 pt to fit one line) |
| Underline | 0.5 pt rule beneath the value, full usable width |

### 3. Number of Files

| Property | Value |
|---|---|
| Label | `NUMBER OF FILES IN Folder:` (Helvetica-Bold, 11 pt) |
| Value | `[ N ]` (Helvetica, 11 pt) |

### 4. Media Type

| Property | Value |
|---|---|
| Label | `MEDIA TYPE:` (Helvetica-Bold, 11 pt) |
| Checkboxes (left to right) | `Audio`, `Photo/Image`, `Video`, `Other Data` |
| Checkbox size | 10 pt squares with `X` mark when present |
| Spacing | 1.6" between checkbox positions |
| Determination | Set by `classify_extension()` in the script — categories: audio, photo, video, other |

### 5. Description

| Property | Value |
|---|---|
| Label | `DESCRIPTION:` (Helvetica-Bold, 11 pt) |
| Caption | `Brief Description of Folder Contents:` (Helvetica-Oblique, 10 pt) |
| Body | Auto word-wrapped (Helvetica, 10 pt) — up to ~3 lines of useful description |
| Empty space | Filled with 0.5 pt blank underlines if the description occupies fewer than 3 lines |

The description text is provided by the attorney or generated when the script runs. The script's default is empty; attorneys should supply context (e.g., "BWC footage from Officer Smith covering arrival at scene through suspect transport").

### 6. Storage Path / Location

| Property | Value |
|---|---|
| Label | `STORAGE PATH / LOCATION:` (Helvetica-Bold, 11 pt) |
| Caption | `Refer to the detailed directory path below for retrieval:` (Helvetica-Oblique, 10 pt) |
| Body | The absolute path to the source folder (Courier, 9 pt) |
| Wrapping | Word-wrap on `/` boundaries — keeps individual path components legible |
| Empty space | Filled with 0.5 pt blank underlines if the path occupies fewer than 3 lines |

The path is the absolute filesystem location of the source media folder, typically anchored under `CASE_ROOT/02 - Pretrial Notebook/02 - Discovery/`. Use Google Drive desktop paths for production cases; do not use volatile temporary paths.

---

## File Classification (driven by extension)

The script categorizes media files by extension. The categories drive the MEDIA TYPE checkboxes. Attorneys reviewing this template should be aware of the lists so they can sanity-check classifications.

### Audio
`.wav`, `.mp3`, `.aac`, `.flac`, `.ogg`, `.wma`, `.m4a`, `.wpl`

### Photo / Image
`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`, `.raw`, `.cr2`, `.nef`, `.heic`, `.db`

(`.db` is included because Cellebrite-style extractions sometimes drop SQLite previews into image folders.)

### Video
`.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`, `.flv`, `.mts`, `.vob`, `.mpg`, `.mpeg`, `.m4v`, `.3gp`, `.dav`, `.264`, `.sec`, `.thm`, `.bup`, `.ifo`

(`.dav`, `.sec`, `.bup`, `.ifo` cover surveillance DVR formats. `.thm` is a thumbnail companion.)

### Other Data
`.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.csv`, `.exe`, `.dll`, `.seclist`, plus any extension not in the lists above.

---

## Output File Naming

For source folder `…/02 - Discovery/Body Cam Footage – Officer Smith/`, the output PDF is:

```
…/[trial-notebook destination]/Body Cam Footage – Officer Smith.pdf
```

The placeholder is named identically to the source folder (with `.pdf` appended). This rule is the single most important convention for the placeholder system — it lets a reader map any placeholder back to its source folder by name alone, with no separate manifest required.

---

## Script Invocation Reference

```bash
# Process every subfolder of an evidence directory
python3 scripts/generate_placeholders.py --evidence-dir "/path/to/02 - Discovery/Media"

# Process only specific subfolders
python3 scripts/generate_placeholders.py \
    --evidence-dir "/path/to/02 - Discovery/Media" \
    --folders "Body Cam Footage – Officer Smith" "Jail Calls"
```

Subfolders named `Evidence_Placeholder` are skipped automatically (these are the script's own output destinations from prior runs).

---

## When This Template Changes

If the firm decides to add a new field, change a label, or alter the visual layout:

1. Update `scripts/generate_placeholders.py` to produce the new output.
2. Update this file to match.
3. **Do not** keep the script and this spec out of sync — both should describe the same layout.
4. Existing placeholder PDFs from prior runs do not need to be regenerated; the layout change applies forward only.

---

*Last reviewed: 2026-04-29. Maintained by D&W. The script is the implementation; this file is the spec for humans.*
