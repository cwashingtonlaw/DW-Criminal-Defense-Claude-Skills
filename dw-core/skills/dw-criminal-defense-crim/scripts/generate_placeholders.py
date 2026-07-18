#!/usr/bin/env python3
"""
Digital Evidence Placeholder Generator — Daniels & Washington

Scans media subfolders in the evidence directory and generates a one-page
PDF placeholder for each folder. Each placeholder summarizes the folder's
contents (file count, media types, formats) so it can sit in the evidence
sequence alongside Bate-stamped documents.

Usage:
    python3 generate_placeholders.py --evidence-dir "<path-to-05-Evidence>" \
        [--folders "folder1" "folder2" ...]

If --folders is omitted, all subfolders are processed.
Folders that already have a corresponding placeholder PDF are skipped
unless --force is passed.
"""

import argparse
import os
import sys
from collections import Counter
from pathlib import Path

# --- Media type classification ---
MEDIA_TYPES = {
    "Audio": {".wav", ".mp3", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".wpl"},
    "Photo/Image": {
        ".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif", ".raw",
        ".cr2", ".nef", ".heic",
    },
    "Video": {
        ".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".mts", ".vob",
        ".mpg", ".mpeg", ".m4v", ".3gp", ".dav", ".264", ".sec", ".thm",
        ".bup", ".ifo",
    },
    "Other Data": {
        ".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".exe",
        ".dll", ".db", ".seclist",
    },
}


def classify_file(ext: str) -> str:
    """Return the media category for a file extension."""
    ext = ext.lower()
    for category, extensions in MEDIA_TYPES.items():
        if ext in extensions:
            return category
    return "Other Data"


def scan_folder(folder_path: Path) -> dict:
    """Scan a folder and return a summary of its contents."""
    files = [f for f in folder_path.iterdir() if f.is_file()]
    total = len(files)

    ext_counts = Counter(f.suffix.lower() for f in files)
    category_counts = Counter()
    for ext, count in ext_counts.items():
        cat = classify_file(ext)
        category_counts[cat] += count

    total_size = sum(f.stat().st_size for f in files)

    return {
        "total_files": total,
        "ext_counts": dict(ext_counts),
        "category_counts": dict(category_counts),
        "total_size_bytes": total_size,
        "categories_present": sorted(category_counts.keys()),
    }


def format_size(size_bytes: int) -> str:
    """Human-readable file size."""
    for unit in ("B", "KB", "MB", "GB"):
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def generate_placeholder_pdf(folder_path: Path, summary: dict, output_path: Path):
    """Generate a one-page placeholder PDF for the given folder."""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.units import inch
        from reportlab.pdfgen import canvas
    except ImportError:
        print("ERROR: reportlab not installed. Install with: pip install reportlab")
        print("Falling back to text-based placeholder.")
        generate_placeholder_txt(folder_path, summary, output_path.with_suffix(".txt"))
        return False

    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter

    y = height - 1 * inch

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, y, "DIGITAL EVIDENCE PLACEHOLDER")
    y -= 0.5 * inch

    c.setLineWidth(1.5)
    c.line(0.75 * inch, y, width - 0.75 * inch, y)
    y -= 0.4 * inch

    # Evidence ID/Name
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75 * inch, y, "EVIDENCE ID / NAME:")
    c.setFont("Helvetica", 11)
    c.drawString(2.75 * inch, y, folder_path.name)
    y -= 0.35 * inch

    # File count
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75 * inch, y, "NUMBER OF FILES IN FOLDER:")
    c.setFont("Helvetica", 11)
    c.drawString(3.5 * inch, y, str(summary["total_files"]))
    y -= 0.35 * inch

    # Total size
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75 * inch, y, "TOTAL SIZE:")
    c.setFont("Helvetica", 11)
    c.drawString(2.75 * inch, y, format_size(summary["total_size_bytes"]))
    y -= 0.5 * inch

    # Media type checkboxes
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75 * inch, y, "MEDIA TYPE:")
    y -= 0.3 * inch

    categories = ["Audio", "Photo/Image", "Video", "Other Data"]
    x_positions = [0.75, 2.5, 4.25, 6.0]
    c.setFont("Helvetica", 10)
    for cat, x_pos in zip(categories, x_positions):
        checked = cat in summary["categories_present"]
        symbol = "\u2611" if checked else "\u2610"
        # Use ZapfDingbats for checkboxes
        if checked:
            c.setFont("ZapfDingbats", 12)
            c.drawString(x_pos * inch, y, "4")  # checkmark in ZapfDingbats
        else:
            c.setFont("ZapfDingbats", 12)
            c.drawString(x_pos * inch, y, "o")  # empty circle
        c.setFont("Helvetica", 10)
        c.drawString(x_pos * inch + 0.2 * inch, y, cat)
    y -= 0.5 * inch

    # Description
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75 * inch, y, "DESCRIPTION:")
    y -= 0.25 * inch

    c.setFont("Helvetica", 10)
    desc_parts = []
    for cat in categories:
        count = summary["category_counts"].get(cat, 0)
        if count > 0:
            desc_parts.append(f"{count} {cat}")

    desc_line1 = f"This folder contains {summary['total_files']} files: {', '.join(desc_parts)}."
    c.drawString(0.75 * inch, y, desc_line1)
    y -= 0.2 * inch

    # File format breakdown
    ext_str = ", ".join(
        f"{ext} ({count})" for ext, count in sorted(summary["ext_counts"].items())
    )
    if len(ext_str) > 85:
        # Wrap long lines
        words = ext_str.split(", ")
        line = ""
        for word in words:
            if len(line + word) > 85:
                c.drawString(0.75 * inch, y, f"Formats: {line}")
                y -= 0.2 * inch
                line = word + ", "
            else:
                line += word + ", "
        if line:
            c.drawString(0.75 * inch, y, f"  {line.rstrip(', ')}")
            y -= 0.2 * inch
    else:
        c.drawString(0.75 * inch, y, f"Formats: {ext_str}")
        y -= 0.2 * inch

    y -= 0.3 * inch

    # Storage path
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.75 * inch, y, "STORAGE PATH / LOCATION:")
    y -= 0.25 * inch
    c.setFont("Courier", 8)
    path_str = str(folder_path.resolve())
    # Wrap long paths
    max_chars = 90
    while path_str:
        c.drawString(0.75 * inch, y, path_str[:max_chars])
        path_str = path_str[max_chars:]
        y -= 0.18 * inch

    y -= 0.3 * inch
    c.setLineWidth(0.5)
    c.line(0.75 * inch, y, width - 0.75 * inch, y)
    y -= 0.2 * inch
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(
        width / 2, y,
        "Generated by Daniels & Washington Cowork — Digital Evidence Placeholder System"
    )

    c.save()
    return True


def generate_placeholder_txt(folder_path: Path, summary: dict, output_path: Path):
    """Fallback: generate a text-based placeholder when reportlab is unavailable."""
    categories = ["Audio", "Photo/Image", "Video", "Other Data"]

    lines = [
        "=" * 60,
        "DIGITAL EVIDENCE PLACEHOLDER",
        "=" * 60,
        "",
        f"EVIDENCE ID / NAME: {folder_path.name}",
        f"NUMBER OF FILES IN FOLDER: {summary['total_files']}",
        f"TOTAL SIZE: {format_size(summary['total_size_bytes'])}",
        "",
        "MEDIA TYPE:",
    ]

    for cat in categories:
        checked = "[X]" if cat in summary["categories_present"] else "[ ]"
        count = summary["category_counts"].get(cat, 0)
        lines.append(f"  {checked} {cat} ({count} files)")

    lines.append("")
    lines.append("DESCRIPTION:")

    desc_parts = []
    for cat in categories:
        count = summary["category_counts"].get(cat, 0)
        if count > 0:
            desc_parts.append(f"{count} {cat}")
    lines.append(
        f"This folder contains {summary['total_files']} files: {', '.join(desc_parts)}."
    )

    ext_str = ", ".join(
        f"{ext} ({count})" for ext, count in sorted(summary["ext_counts"].items())
    )
    lines.append(f"Formats: {ext_str}")

    lines.append("")
    lines.append("STORAGE PATH / LOCATION:")
    lines.append(str(folder_path.resolve()))
    lines.append("")
    lines.append("-" * 60)
    lines.append(
        "Generated by Daniels & Washington Cowork — Digital Evidence Placeholder System"
    )

    output_path.write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(
        description="Generate Digital Evidence Placeholder PDFs for media folders."
    )
    parser.add_argument(
        "--evidence-dir",
        required=True,
        help="Path to the 05 - Evidence directory",
    )
    parser.add_argument(
        "--folders",
        nargs="*",
        help="Specific folder names to process (default: all subfolders)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate placeholders even if they already exist",
    )
    args = parser.parse_args()

    evidence_dir = Path(args.evidence_dir)
    if not evidence_dir.is_dir():
        print(f"ERROR: Evidence directory not found: {evidence_dir}")
        sys.exit(1)

    # Identify target folders
    if args.folders:
        targets = [evidence_dir / name for name in args.folders]
        missing = [t for t in targets if not t.is_dir()]
        if missing:
            print(f"WARNING: Folders not found: {[str(m) for m in missing]}")
        targets = [t for t in targets if t.is_dir()]
    else:
        targets = sorted([d for d in evidence_dir.iterdir() if d.is_dir()])

    if not targets:
        print("No subfolders found to process.")
        sys.exit(0)

    created = 0
    skipped = 0
    results = {"Audio": 0, "Photo/Image": 0, "Video": 0, "Other Data": 0}

    for folder in targets:
        placeholder_name = f"{folder.name}.pdf"
        placeholder_path = evidence_dir / placeholder_name

        if placeholder_path.exists() and not args.force:
            print(f"  SKIP: {folder.name} (placeholder already exists)")
            skipped += 1
            continue

        summary = scan_folder(folder)
        if summary["total_files"] == 0:
            print(f"  SKIP: {folder.name} (empty folder)")
            skipped += 1
            continue

        success = generate_placeholder_pdf(folder, summary, placeholder_path)
        if success:
            print(f"  CREATED: {placeholder_name} ({summary['total_files']} files)")
            created += 1
        else:
            txt_path = placeholder_path.with_suffix(".txt")
            print(f"  CREATED (txt fallback): {txt_path.name}")
            created += 1

        for cat, count in summary["category_counts"].items():
            if cat in results:
                results[cat] += count

    # Summary report
    print(f"\n{'=' * 50}")
    print(f"Placeholder Generation Complete")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Total folders scanned: {len(targets)}")
    print(f"\nMedia breakdown across all processed folders:")
    for cat, count in results.items():
        if count > 0:
            print(f"  {cat}: {count} files")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
