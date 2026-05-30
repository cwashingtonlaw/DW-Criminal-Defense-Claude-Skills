---
name: dw-evidence-placeholder-crim
category: ops
description: >
  Generate placeholder PDFs for media evidence folders. ALWAYS invoke for "evidence
  placeholders," "placeholder PDFs," "catalog the media folders," or "evidence folder
  inventory." Produces one-page summary PDF per folder with file count, type classification,
  and storage path.
---

# Digital Evidence Placeholder Generator

## What This Skill Does

Criminal defense discovery often includes dozens of folders containing raw media — crime scene
photos, surveillance video, body-worn camera footage, recorded interviews, 911 audio, lab photos,
and more. These folders can't be Bates-stamped or processed like documents, so each one needs a
**Digital Evidence Placeholder** — a single-page PDF that sits in the evidence sequence and tells
anyone reviewing the file what's in that folder, how many files it contains, and where to find them.

This skill automates that process. Point it at an evidence directory and it will:

1. Identify every subfolder that contains media or other non-document files
2. Scan each folder for file counts, file types, and total size
3. Classify the contents by media type (Audio, Photo/Image, Video, Other Data)
4. Generate a one-page PDF for each folder matching the firm's standard template
5. Name each PDF identically to its source folder

## When to Use

- After receiving discovery that includes media folders alongside document PDFs
- When building or updating the evidence file and you need placeholders for the media items
- When the evidence sequence has gaps where media folders sit

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## Workflow

### Step 1: Identify the Evidence Directory

Ask the user which directory to scan, or infer it from context (e.g., the currently mounted
workspace folder, or a path they mention). The evidence directory is typically the main case
evidence folder — something like `05 - Evidence` or similar.

### Step 2: Confirm Scope

List the folders found and ask the user which ones need placeholders. Common categories include:

- **Photo folders** — Crime scene photos, search photos, lab photos, victim photos
- **Video folders** — Crime scene videos, surveillance footage, body cam / in-car cam
- **Interview folders** — Recorded interviews (often .MTS files with .docx transcripts)
- **Audio folders** — 911 recordings, dispatch recordings
- **Surveillance folders** — Various formats (.dav, .sec, .264, .avi, .mp4) often with proprietary players
- **Mixed media folders** — Folders with PDFs, videos, and other file types combined

Default to processing all folders unless the user says otherwise. Exclude folders that already
have a corresponding PDF placeholder in the evidence directory to avoid duplicates (unless the
user wants to regenerate them).

### Step 3: Generate the Placeholders

Generate placeholder PDFs using inline Python with `reportlab`. Do **not** reference an external script — the generation logic runs directly in the Cowork sandbox.

```python
# Inline placeholder generator — run in Cowork bash sandbox
# Requires: pip install reportlab --break-system-packages

import os, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

MEDIA_TYPES = {
    "Audio": {".wav", ".mp3", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".wpl"},
    "Photo/Image": {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif", ".raw", ".cr2", ".nef", ".heic"},
    "Video": {".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".mts", ".vob", ".mpg", ".mpeg", ".m4v", ".3gp", ".dav", ".264", ".sec", ".thm", ".bup", ".ifo"},
    "Other Data": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".exe", ".dll", ".db", ".seclist"},
}

def classify_folder(folder_path):
    files = [f for f in Path(folder_path).rglob("*") if f.is_file()]
    types_found = set()
    ext_counts = {}
    for f in files:
        ext = f.suffix.lower()
        ext_counts[ext] = ext_counts.get(ext, 0) + 1
        for cat, exts in MEDIA_TYPES.items():
            if ext in exts:
                types_found.add(cat)
                break
        else:
            types_found.add("Other Data")
    return len(files), types_found, ext_counts

def generate_placeholder(folder_path, output_dir):
    name = Path(folder_path).name
    count, types, ext_counts = classify_folder(folder_path)
    out_path = Path(output_dir) / f"{name}.pdf"
    c = canvas.Canvas(str(out_path), pagesize=letter)
    w, h = letter
    y = h - inch
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w / 2, y, "DIGITAL EVIDENCE PLACEHOLDER")
    y -= 40
    c.setFont("Helvetica-Bold", 11)
    c.drawString(inch, y, f"EVIDENCE ID/NAME: {name}")
    y -= 25
    c.drawString(inch, y, f"NUMBER OF FILES IN FOLDER: {count}")
    y -= 25
    c.drawString(inch, y, "MEDIA TYPE:")
    y -= 20
    c.setFont("Helvetica", 11)
    for cat in ["Audio", "Photo/Image", "Video", "Other Data"]:
        mark = "X" if cat in types else " "
        c.drawString(inch + 20, y, f"[{mark}] {cat}")
        y -= 18
    y -= 15
    c.setFont("Helvetica-Bold", 11)
    c.drawString(inch, y, "DESCRIPTION:")
    y -= 20
    c.setFont("Helvetica", 10)
    fmt_str = ", ".join(f"{v} {k.upper().lstrip('.')} files" for k, v in sorted(ext_counts.items(), key=lambda x: -x[1]))
    c.drawString(inch, y, f"Contains {count} files. File formats: {fmt_str}")
    y -= 30
    c.setFont("Helvetica-Bold", 11)
    c.drawString(inch, y, "STORAGE PATH / LOCATION:")
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(inch, y, str(folder_path))
    c.save()
    return out_path

# Usage: set evidence_dir and optional folder list, then run
# evidence_dir = "<path-to-05-Evidence>"
# folders = None  # or ["folder1", "folder2"] for specific folders
# for d in (folders or [f.name for f in Path(evidence_dir).iterdir() if f.is_dir()]):
#     generate_placeholder(Path(evidence_dir) / d, evidence_dir)
```

To run: set `evidence_dir` to the case's `05 - Evidence` path, optionally specify folder names, and execute in the Cowork bash sandbox. Each output PDF is saved directly into the evidence directory with the same name as its folder plus `.pdf`.

### Step 4: Report Results

After the script runs, summarize what was created:
- Total number of placeholder PDFs generated
- Any folders that were skipped and why (e.g., empty folders, folders that already had placeholders)
- A quick breakdown by media type if useful

## Media Type Classification

The script classifies files by extension into four categories. A folder can have multiple types
checked if it contains mixed content.

| Category | Extensions |
|----------|-----------|
| Audio | .wav, .mp3, .aac, .flac, .ogg, .wma, .m4a, .wpl |
| Photo/Image | .jpg, .jpeg, .png, .bmp, .tiff, .gif, .raw, .cr2, .nef, .heic |
| Video | .mp4, .avi, .mov, .mkv, .wmv, .flv, .mts, .vob, .mpg, .mpeg, .m4v, .3gp, .dav, .264, .sec, .thm, .bup, .ifo |
| Other Data | .pdf, .docx, .doc, .txt, .xlsx, .csv, .exe, .dll, .db, .seclist, and files with no extension |

## Description Generation

The script generates contextual descriptions based on the folder name and contents:

- **Photo folders** → "Contains X photographic image files"
- **Crime scene videos** → "Contains X crime scene video recordings and associated thumbnail files"
- **Surveillance folders** → "Contains surveillance video footage"
- **Interview folders** → "Contains recorded interview files" (+ "including transcription document(s)" if .docx files present)
- **Body cam / in-car folders** → "Contains body-worn camera and/or in-car camera video recordings" (+ transcript note if applicable)
- **911 / dispatch recordings** → "Contains audio recordings" (+ transcript note if applicable)

Each description also includes a file format breakdown (e.g., "File formats: 91 JPG files, 3 MP4 files").

## Template Layout

The generated PDF matches the firm's standard one-page format:

```
DIGITAL EVIDENCE PLACEHOLDER

EVIDENCE ID/NAME: [folder name]
NUMBER OF FILES IN Folder: [ count ]
MEDIA TYPE:
  [ ] Audio    [ ] Photo/Image    [ ] Video    [ ] Other Data

DESCRIPTION:
Brief Description of Folder Contents:
[auto-generated description]

STORAGE PATH / LOCATION:
Refer to the detailed directory path below for retrieval:
[relative path from case root]
```

Checked boxes show an "X" inside the box. The layout uses Helvetica fonts on US Letter paper
with 1-inch margins.

## Notes

- The script counts files inside immediate subdirectories too (one level deep), since some
  evidence folders contain nested directories (e.g., surveillance folders with camera-specific subfolders).
- `.db` files (macOS Thumbs.db etc.) are counted in the file total and classified as Photo/Image
  since they typically accompany photo folders, but this doesn't affect the description text.
- Proprietary player executables (.exe) that ship with surveillance footage are counted and
  classified as Other Data.
- The storage path uses the relative path from the evidence root (e.g., `05 - Evidence/054 - Item # 30 - Crime Scene Photos`).
