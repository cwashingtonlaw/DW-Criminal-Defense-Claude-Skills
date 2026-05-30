#!/usr/bin/env python3
"""
dw-image-filename-stamp — stamp images with their own filenames.

Usage:
    python3 stamp_images.py /path/to/folder              # real run
    python3 stamp_images.py --dry-run /path/to/folder    # preview only, no writes
    python3 stamp_images.py --force /path/to/folder      # re-stamp even if output exists
    python3 stamp_images.py --verbose /path/to/folder    # log skipped unknown formats too

Writes stamped copies to a `stamped/` subfolder inside each folder that contains
images. Never modifies originals. Preserves EXIF. Respects orientation.

Designed for the Daniels & Washington case workflow. Originals are evidence.
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable

# ----------------------------- Configuration ------------------------------- #

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".heic", ".heif", ".webp"}
VIDEO_EXTS = {".mov", ".mp4", ".m4v", ".avi", ".mkv", ".mts", ".m2ts", ".wmv", ".flv"}
STAMPED_DIRNAME = "stamped"

# Stamp design — fixed per SKILL.md. Change only with attorney approval.
STAMP_FONT_RATIO = 0.025          # font size = 2.5% of longer edge
STAMP_MARGIN_RATIO = 0.02         # margin = 2% of shorter edge
STAMP_PADDING_RATIO = 0.4         # inner padding = 40% of font size
STAMP_CORNER_RATIO = 0.3          # rounded corner radius = 30% of font size
STAMP_BG_ALPHA = 160              # out of 255 — semi-transparent black
STAMP_TEXT_COLOR = (255, 255, 255, 255)
STAMP_BG_COLOR = (0, 0, 0, STAMP_BG_ALPHA)


# ------------------------------ Dependencies ------------------------------- #

def ensure_pillow() -> None:
    """Pillow is required. Install if missing. Tries multiple strategies."""
    try:
        import PIL  # noqa: F401
        return
    except ImportError:
        pass

    install_strategies = [
        [sys.executable, "-m", "pip", "install", "--quiet", "Pillow"],
        [sys.executable, "-m", "pip", "install", "--quiet", "--user", "Pillow"],
        [sys.executable, "-m", "pip", "install", "--quiet",
         "--break-system-packages", "Pillow"],
    ]
    for cmd in install_strategies:
        try:
            print(f"[setup] Installing Pillow: {' '.join(cmd[-2:])}", file=sys.stderr)
            subprocess.check_call(cmd, stderr=subprocess.DEVNULL)
            import PIL  # noqa: F401
            return
        except Exception:
            continue

    print("ERROR: Pillow is required but could not be installed. "
          "Install manually with: pip install Pillow", file=sys.stderr)
    sys.exit(3)


def try_enable_heic() -> bool:
    """Try to enable HEIC/HEIF reading. Returns True on success.

    Tries in order: (1) already-installed, (2) pip install, (3) pip install --user,
    (4) pip install --break-system-packages. Never raises — returns False if all fail.
    """
    try:
        import pillow_heif  # type: ignore
        pillow_heif.register_heif_opener()
        return True
    except ImportError:
        pass

    install_strategies = [
        [sys.executable, "-m", "pip", "install", "--quiet", "pillow-heif"],
        [sys.executable, "-m", "pip", "install", "--quiet", "--user", "pillow-heif"],
        [sys.executable, "-m", "pip", "install", "--quiet",
         "--break-system-packages", "pillow-heif"],
    ]
    for cmd in install_strategies:
        try:
            print(f"[setup] Attempting: {' '.join(cmd[-3:])}", file=sys.stderr)
            subprocess.check_call(cmd, stderr=subprocess.DEVNULL)
            import pillow_heif  # type: ignore
            pillow_heif.register_heif_opener()
            print("[setup] HEIC support enabled.", file=sys.stderr)
            return True
        except Exception:
            continue

    print("[setup] pillow-heif unavailable; HEIC/HEIF files will be skipped with a log note.",
          file=sys.stderr)
    return False


# ------------------------------- Data model -------------------------------- #

@dataclass
class FileResult:
    source: Path
    status: str              # "stamped" | "skipped" | "error"
    notes: str = ""
    dimensions: str = ""
    stamp_text: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


@dataclass
class FolderResult:
    folder: Path
    results: list[FileResult] = field(default_factory=list)

    @property
    def counts(self) -> dict[str, int]:
        c = {"stamped": 0, "skipped": 0, "error": 0}
        for r in self.results:
            c[r.status] = c.get(r.status, 0) + 1
        return c


# ------------------------------- Stamping ---------------------------------- #

def _load_font(size: int):
    """Load a font, with fallbacks."""
    from PIL import ImageFont
    # Try common system fonts
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size=size)
            except Exception:
                continue
    return ImageFont.load_default()


def stamp_image(src: Path, dst: Path) -> FileResult:
    """Stamp one image. Returns a FileResult describing what happened."""
    from PIL import Image, ImageDraw, ImageOps

    stamp_text = src.stem  # filename without extension — per attorney spec

    try:
        with Image.open(src) as im:
            # Capture EXIF bytes before any transformation
            exif_bytes = im.info.get("exif", b"")
            icc = im.info.get("icc_profile")

            # Respect EXIF orientation — rotate so the "true" bottom-right is visible
            im = ImageOps.exif_transpose(im)

            # Convert to RGBA for compositing with semi-transparent overlay
            original_mode = im.mode
            if im.mode != "RGBA":
                im_rgba = im.convert("RGBA")
            else:
                im_rgba = im

            w, h = im_rgba.size
            longer = max(w, h)
            font_size = max(int(longer * STAMP_FONT_RATIO), 12)
            font = _load_font(font_size)

            # Measure text properly using a real draw context
            measure_draw = ImageDraw.Draw(im_rgba)
            bbox = measure_draw.textbbox((0, 0), stamp_text, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]

            shorter = min(w, h)
            padding = int(font_size * STAMP_PADDING_RATIO)
            margin = int(shorter * STAMP_MARGIN_RATIO)
            corner = max(int(font_size * STAMP_CORNER_RATIO), 2)

            box_w = text_w + 2 * padding
            box_h = text_h + 2 * padding
            x1 = w - margin - box_w
            y1 = h - margin - box_h
            x2 = w - margin
            y2 = h - margin

            # Composite overlay for semi-transparent background
            overlay = Image.new("RGBA", im_rgba.size, (0, 0, 0, 0))
            odraw = ImageDraw.Draw(overlay)
            odraw.rounded_rectangle((x1, y1, x2, y2), radius=corner, fill=STAMP_BG_COLOR)
            odraw.text(
                (x1 + padding - bbox[0], y1 + padding - bbox[1]),
                stamp_text,
                fill=STAMP_TEXT_COLOR,
                font=font,
            )
            stamped = Image.alpha_composite(im_rgba, overlay)

            # Convert back to output mode. JPEGs can't handle RGBA.
            out_ext = dst.suffix.lower()
            if out_ext in (".jpg", ".jpeg"):
                stamped = stamped.convert("RGB")
                save_kwargs = {"quality": 95, "subsampling": 0}
            elif out_ext in (".heic", ".heif"):
                # Save HEIC as JPEG to keep things portable; update the destination suffix.
                stamped = stamped.convert("RGB")
                dst = dst.with_suffix(".jpg")
                save_kwargs = {"quality": 95, "subsampling": 0}
            elif out_ext == ".png":
                save_kwargs = {"optimize": True}
            elif out_ext in (".tif", ".tiff"):
                if stamped.mode == "RGBA" and original_mode not in ("RGBA", "LA"):
                    stamped = stamped.convert("RGB")
                save_kwargs = {"compression": "tiff_lzw"}
            elif out_ext == ".webp":
                save_kwargs = {"quality": 95, "method": 6}
            else:
                save_kwargs = {}

            # Preserve EXIF and ICC profile where supported
            if exif_bytes:
                save_kwargs["exif"] = exif_bytes
            if icc:
                save_kwargs["icc_profile"] = icc

            # Ensure destination directory exists
            dst.parent.mkdir(parents=True, exist_ok=True)

            # Safety check — never overwrite the source path
            if dst.resolve() == src.resolve():
                return FileResult(
                    source=src, status="error",
                    notes="refused: destination equals source",
                )

            stamped.save(dst, **save_kwargs)

            return FileResult(
                source=src,
                status="stamped",
                dimensions=f"{w}x{h}",
                stamp_text=stamp_text,
                notes=f"-> {dst.name}",
            )

    except Exception as exc:
        return FileResult(source=src, status="error", notes=f"error: {exc}")


# ------------------------------- Walking ----------------------------------- #

def iter_image_folders(root: Path) -> Iterable[Path]:
    """Yield every folder under root that contains at least one image file,
    excluding any folder named `stamped/` (and their descendants)."""
    for folder in [root] + [p for p in root.rglob("*") if p.is_dir()]:
        # Skip stamped/ and anything inside it
        if STAMPED_DIRNAME in folder.parts:
            continue
        try:
            contents = list(folder.iterdir())
        except PermissionError:
            continue
        has_image = any(
            p.is_file() and p.suffix.lower() in IMAGE_EXTS
            for p in contents
        )
        if has_image:
            yield folder


def process_folder(
    folder: Path,
    heic_ok: bool,
    dry_run: bool,
    force: bool,
    verbose: bool,
) -> FolderResult:
    """Process every image file in a single folder (not recursive — one level)."""
    result = FolderResult(folder=folder)
    stamped_dir = folder / STAMPED_DIRNAME

    for child in sorted(folder.iterdir()):
        if not child.is_file():
            continue
        ext = child.suffix.lower()

        if ext in VIDEO_EXTS:
            result.results.append(FileResult(
                source=child, status="skipped", notes="skipped: video format",
            ))
            continue

        if ext not in IMAGE_EXTS:
            if verbose:
                result.results.append(FileResult(
                    source=child, status="skipped", notes="skipped: unknown format",
                ))
            continue

        if ext in (".heic", ".heif") and not heic_ok:
            result.results.append(FileResult(
                source=child, status="skipped", notes="skipped: HEIC plugin unavailable",
            ))
            continue

        dst = stamped_dir / child.name
        # Pre-skip check for the HEIC -> JPG rename case
        if ext in (".heic", ".heif"):
            dst_alt = stamped_dir / (child.stem + ".jpg")
            if not force and (dst.exists() or dst_alt.exists()):
                result.results.append(FileResult(
                    source=child, status="skipped", notes="skipped: already stamped",
                ))
                continue
        else:
            if not force and dst.exists():
                result.results.append(FileResult(
                    source=child, status="skipped", notes="skipped: already stamped",
                ))
                continue

        if dry_run:
            result.results.append(FileResult(
                source=child, status="stamped", notes="[dry-run] would stamp",
                stamp_text=child.stem,
            ))
            continue

        result.results.append(stamp_image(child, dst))

    return result


# ------------------------------- Logging ----------------------------------- #

def write_folder_log(folder_result: FolderResult, dry_run: bool) -> None:
    """Write per-folder CSV log into the stamped/ subfolder."""
    if dry_run:
        return
    stamped_dir = folder_result.folder / STAMPED_DIRNAME
    if not stamped_dir.exists():
        return  # nothing to log about
    log_path = stamped_dir / "_stamp_log.csv"
    write_header = not log_path.exists()
    with log_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow([
                "source_filename", "dimensions", "stamp_text",
                "timestamp", "status", "notes",
            ])
        for r in folder_result.results:
            writer.writerow([
                r.source.name, r.dimensions, r.stamp_text,
                r.timestamp, r.status, r.notes,
            ])


def write_summary(root: Path, all_results: list[FolderResult], dry_run: bool) -> Path | None:
    """Write top-level summary CSV at the root."""
    if dry_run:
        return None
    summary_path = root / "_stamp_summary.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "folder", "total_files", "stamped", "skipped", "errors", "timestamp",
        ])
        for fr in all_results:
            c = fr.counts
            writer.writerow([
                str(fr.folder.relative_to(root)) or ".",
                len(fr.results),
                c.get("stamped", 0),
                c.get("skipped", 0),
                c.get("error", 0),
                datetime.now().isoformat(timespec="seconds"),
            ])
    return summary_path


def print_report(all_results: list[FolderResult], dry_run: bool) -> None:
    total_stamped = sum(fr.counts.get("stamped", 0) for fr in all_results)
    total_skipped = sum(fr.counts.get("skipped", 0) for fr in all_results)
    total_errors = sum(fr.counts.get("error", 0) for fr in all_results)

    prefix = "[DRY RUN] " if dry_run else ""
    print()
    print(f"{prefix}Folders processed: {len(all_results)}")
    print(f"{prefix}Images stamped:    {total_stamped}")
    print(f"{prefix}Skipped:           {total_skipped}")
    print(f"{prefix}Errors:            {total_errors}")

    if total_errors:
        print()
        print("Errors:")
        for fr in all_results:
            for r in fr.results:
                if r.status == "error":
                    print(f"  {r.source}: {r.notes}")


# -------------------------------- Main ------------------------------------- #

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Stamp images with their own filenames (D&W image stamp utility)."
    )
    parser.add_argument("folder", help="Root folder to process (recursive).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Report what would happen without writing anything.")
    parser.add_argument("--force", action="store_true",
                        help="Re-stamp files even if output already exists.")
    parser.add_argument("--verbose", action="store_true",
                        help="Log skipped unknown formats too.")
    args = parser.parse_args()

    root = Path(args.folder).expanduser().resolve()
    if not root.exists():
        print(f"ERROR: folder does not exist: {root}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"ERROR: not a folder: {root}", file=sys.stderr)
        return 2

    ensure_pillow()
    heic_ok = try_enable_heic()

    folders = list(iter_image_folders(root))
    if not folders:
        print(f"No image-containing folders found under {root}")
        return 0

    print(f"Processing {len(folders)} folder(s) under {root}...")
    all_results: list[FolderResult] = []
    for folder in folders:
        fr = process_folder(folder, heic_ok, args.dry_run, args.force, args.verbose)
        all_results.append(fr)
        write_folder_log(fr, args.dry_run)

    summary = write_summary(root, all_results, args.dry_run)
    print_report(all_results, args.dry_run)
    if summary:
        print(f"\nSummary written to: {summary}")

    # Exit code: 1 if any errors occurred, else 0
    total_errors = sum(fr.counts.get("error", 0) for fr in all_results)
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
