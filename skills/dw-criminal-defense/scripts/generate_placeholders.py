#!/usr/bin/env python3
"""
Digital Evidence Placeholder Generator
Daniels & Washington Criminal Defense

Scans evidence folders containing media files and generates a one-page
placeholder PDF for each folder, matching the firm's standard template.

Usage:
    python generate_placeholders.py --evidence-dir /path/to/evidence
    python generate_placeholders.py --evidence-dir /path/to/evidence --folders "folder1" "folder2"
"""

import argparse
import os
import sys

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


# ── File extension classification ───────────────────────────────────────

AUDIO_EXTS = {'.wav', '.mp3', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.wpl'}
PHOTO_EXTS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif', '.raw',
              '.cr2', '.nef', '.heic', '.db'}
VIDEO_EXTS = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.mts', '.vob',
              '.mpg', '.mpeg', '.m4v', '.3gp', '.dav', '.264', '.sec', '.thm',
              '.bup', '.ifo'}
OTHER_EXTS = {'.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv', '.exe',
              '.dll', '.seclist'}


def classify_extension(ext):
    """Return the media category for a file extension."""
    ext = ext.lower()
    if ext in AUDIO_EXTS:
        return 'audio'
    elif ext in PHOTO_EXTS:
        return 'photo'
    elif ext in VIDEO_EXTS:
        return 'video'
    elif ext in OTHER_EXTS or ext == '':
        return 'other'
    else:
        return 'other'


# ── Folder scanning ────────────────────────────────────────────────────

def scan_folder(folder_path, folder_name):
    """
    Scan a folder (and one level of subdirectories) and return:
        (file_count, has_audio, has_photo, has_video, has_other, description)
    """
    files = []
    for item in os.listdir(folder_path):
        full = os.path.join(folder_path, item)
        if os.path.isfile(full):
            files.append(item)
        elif os.path.isdir(full):
            # Include files one level deep inside subdirectories
            try:
                for sub_item in os.listdir(full):
                    if os.path.isfile(os.path.join(full, sub_item)):
                        files.append(sub_item)
            except PermissionError:
                pass

    file_count = len(files)

    has_audio = False
    has_photo = False
    has_video = False
    has_other = False

    ext_counts = {}
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        category = classify_extension(ext)

        if category == 'audio':
            has_audio = True
        elif category == 'photo':
            has_photo = True
        elif category == 'video':
            has_video = True
        else:
            has_other = True

        label = ext.upper().strip('.') if ext else '(no ext)'
        ext_counts[label] = ext_counts.get(label, 0) + 1

    # ── Build contextual description ────────────────────────────────
    desc_parts = []
    name_lower = folder_name.lower()
    has_transcripts = any(f.lower().endswith('.docx') for f in files)

    if 'crime scene video' in name_lower:
        desc_parts.append(
            f"Contains {file_count} crime scene video recordings and "
            "associated thumbnail files")
    elif 'crime scene photo' in name_lower:
        desc_parts.append(f"Contains {file_count} crime scene photographs")
    elif ('photo' in name_lower or 'pictures' in name_lower
          or 'lab photos' in name_lower):
        desc_parts.append(f"Contains {file_count} photographic image files")
    elif 'surveillance' in name_lower:
        desc_parts.append("Contains surveillance video footage")
    elif 'interview' in name_lower:
        desc_parts.append("Contains recorded interview files")
        if has_transcripts:
            desc_parts.append("including transcription document(s)")
    elif ('body' in name_lower
          and ('cam' in name_lower or 'car' in name_lower
               or 'in-car' in name_lower)):
        desc_parts.append(
            "Contains body-worn camera and/or in-car camera video recordings")
        if has_transcripts:
            desc_parts.append("with associated transcription document(s)")
    elif '911' in name_lower or 'dispatch' in name_lower:
        desc_parts.append("Contains audio recordings")
        if has_transcripts:
            desc_parts.append("with associated transcription document(s)")
    elif 'victim' in name_lower:
        desc_parts.append("Contains photographs of victims")
    elif 'search' in name_lower and 'photo' in name_lower:
        desc_parts.append("Contains photographs from search execution")
    elif 'avail media' in name_lower or 'arrest' in name_lower:
        desc_parts.append("Contains mixed media files related to arrest")
    else:
        desc_parts.append(f"Contains {file_count} digital evidence files")

    # File format breakdown
    sorted_exts = sorted(ext_counts.items(), key=lambda x: -x[1])
    format_strs = [
        f"{count} {ext} file{'s' if count > 1 else ''}"
        for ext, count in sorted_exts
    ]
    if format_strs:
        desc_parts.append("File formats: " + ", ".join(format_strs))

    description = ". ".join(desc_parts) + "."

    return file_count, has_audio, has_photo, has_video, has_other, description


# ── PDF generation ─────────────────────────────────────────────────────

def create_placeholder_pdf(output_path, evidence_name, file_count,
                           has_audio, has_photo, has_video, has_other,
                           description, storage_path):
    """Create a single Digital Evidence Placeholder PDF."""
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    left = 1.0 * inch
    right = width - 1.0 * inch
    usable_width = right - left

    # ── Title ──
    c.setFont("Helvetica-Bold", 18)
    title = "DIGITAL EVIDENCE PLACEHOLDER"
    title_width = c.stringWidth(title, "Helvetica-Bold", 18)
    c.drawString((width - title_width) / 2, height - 1.0 * inch, title)

    # Horizontal rule
    y = height - 1.25 * inch
    c.setLineWidth(1)
    c.line(left, y, right, y)

    # ── EVIDENCE ID/NAME ──
    y -= 0.35 * inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left, y, "EVIDENCE ID/NAME:")
    name_x = left + c.stringWidth("EVIDENCE ID/NAME:  ", "Helvetica-Bold", 11)
    available = right - name_x

    # Auto-shrink font to fit long names
    for size in (10, 9, 8, 7):
        if c.stringWidth(evidence_name, "Helvetica", size) <= available:
            break
    c.setFont("Helvetica", size)
    c.drawString(name_x, y, evidence_name)
    c.setLineWidth(0.5)
    c.line(name_x, y - 0.05 * inch, right, y - 0.05 * inch)

    # ── NUMBER OF FILES ──
    y -= 0.40 * inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left, y, "NUMBER OF FILES IN Folder:")
    c.setFont("Helvetica", 11)
    bracket_x = left + c.stringWidth(
        "NUMBER OF FILES IN Folder:  ", "Helvetica-Bold", 11)
    c.drawString(bracket_x, y, f"[ {file_count} ]")

    # ── MEDIA TYPE ──
    y -= 0.40 * inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left, y, "MEDIA TYPE:")

    y -= 0.30 * inch
    c.setFont("Helvetica", 11)
    checkbox_size = 10
    gap = 1.6 * inch
    cx = left

    for label, checked in [("Audio", has_audio), ("Photo/Image", has_photo),
                           ("Video", has_video), ("Other Data", has_other)]:
        c.rect(cx, y - 2, checkbox_size, checkbox_size)
        if checked:
            c.setFont("Helvetica-Bold", 10)
            c.drawString(cx + 1.5, y - 0.5, "X")
            c.setFont("Helvetica", 11)
        c.drawString(cx + checkbox_size + 4, y, label)
        cx += gap

    # ── DESCRIPTION ──
    y -= 0.50 * inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left, y, "DESCRIPTION:")

    y -= 0.22 * inch
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(left, y, "Brief Description of Folder Contents:")

    y -= 0.30 * inch
    c.setFont("Helvetica", 10)

    # Word-wrap description
    lines = _word_wrap(c, description, "Helvetica", 10, usable_width)
    for line in lines:
        c.drawString(left, y, line)
        y -= 0.20 * inch

    # Blank underlines to fill remaining description space
    for _ in range(max(0, 3 - len(lines))):
        c.setLineWidth(0.5)
        c.line(left, y + 0.05 * inch, right, y + 0.05 * inch)
        y -= 0.20 * inch

    # ── STORAGE PATH / LOCATION ──
    y -= 0.30 * inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left, y, "STORAGE PATH / LOCATION:")

    y -= 0.22 * inch
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(left, y, "Refer to the detailed directory path below for retrieval:")

    y -= 0.30 * inch
    c.setFont("Courier", 9)

    # Word-wrap path on "/" boundaries
    path_lines = _path_wrap(c, storage_path, "Courier", 9, usable_width)
    for line in path_lines:
        c.drawString(left, y, line)
        y -= 0.20 * inch

    for _ in range(max(0, 3 - len(path_lines))):
        c.setLineWidth(0.5)
        c.line(left, y + 0.05 * inch, right, y + 0.05 * inch)
        y -= 0.20 * inch

    c.save()


def _word_wrap(c, text, font, size, max_width):
    """Break text into lines that fit within max_width."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = current + (" " if current else "") + word
        if c.stringWidth(test, font, size) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _path_wrap(c, path, font, size, max_width):
    """Break a file path into lines, splitting on '/' boundaries."""
    segments = path.split("/")
    lines = []
    current = ""
    for seg in segments:
        test = current + ("/" if current else "") + seg
        if c.stringWidth(test, font, size) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = seg
    if current:
        lines.append(current)
    return lines


# ── Main ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate Digital Evidence Placeholder PDFs")
    parser.add_argument(
        '--evidence-dir', required=True,
        help='Path to the evidence directory containing media folders')
    parser.add_argument(
        '--folders', nargs='*', default=None,
        help='Specific folder names to process (default: all subfolders)')
    args = parser.parse_args()

    evidence_dir = args.evidence_dir
    if not os.path.isdir(evidence_dir):
        print(f"Error: '{evidence_dir}' is not a valid directory.")
        sys.exit(1)

    # Determine the evidence directory name for storage paths
    evidence_dir_name = os.path.basename(os.path.normpath(evidence_dir))

    # Get folder list
    all_dirs = sorted([
        d for d in os.listdir(evidence_dir)
        if os.path.isdir(os.path.join(evidence_dir, d))
    ])

    if args.folders:
        # Filter to only requested folders
        requested = set(args.folders)
        folders = [d for d in all_dirs if d in requested]
        missing = requested - set(folders)
        if missing:
            print(f"Warning: folders not found: {missing}")
    else:
        folders = all_dirs

    # Exclude the Evidence_Placeholder folder itself
    folders = [f for f in folders if f != "Evidence_Placeholder"]

    print(f"Processing {len(folders)} folders in: {evidence_dir}\n")

    success = 0
    skipped = 0

    for folder_name in folders:
        folder_path = os.path.join(evidence_dir, folder_name)

        try:
            result = scan_folder(folder_path, folder_name)
            file_count, has_audio, has_photo, has_video, has_other, desc = result

            if file_count == 0:
                print(f"[SKIP] {folder_name} (empty folder)")
                skipped += 1
                continue

            storage_path = f"{evidence_dir_name}/{folder_name}"
            output_path = os.path.join(evidence_dir, f"{folder_name}.pdf")

            create_placeholder_pdf(
                output_path=output_path,
                evidence_name=folder_name,
                file_count=file_count,
                has_audio=has_audio,
                has_photo=has_photo,
                has_video=has_video,
                has_other=has_other,
                description=desc,
                storage_path=storage_path,
            )

            media = []
            if has_audio: media.append("Audio")
            if has_photo: media.append("Photo")
            if has_video: media.append("Video")
            if has_other: media.append("Other")

            print(f"[OK] {folder_name}.pdf  "
                  f"({file_count} files | {', '.join(media)})")
            success += 1

        except Exception as e:
            print(f"[ERROR] {folder_name}: {e}")

    print(f"\nDone: {success} created, {skipped} skipped.")


if __name__ == "__main__":
    main()
