# Design Spec — dw-image-filename-stamp

This document captures *why* the skill makes the design choices it does. If you're considering changing a default, read this first — most defaults are load-bearing.

## Why the stamp is filename-only (no extension, no prefix, no date)

The attorney's v1 spec was explicit: stamp the filename only. Rationale:

- **No extension**: `DSC_9266` reads cleaner than `DSC_9266.JPG`. The extension tells you nothing useful at a glance — file manager icons already do that job. Where it *does* matter (`DSC_9266.RAW` vs `DSC_9266.JPG`), the stamp isn't the right place to carry that info; file listings are.
- **No prefix**: the original filename is the identifier. If prefixes are needed for production (e.g., `SMITH-001-`), rename the files first as a separate step. Baking prefix logic into the stamper creates two sources of truth (filename vs. stamp) and invites drift.
- **No date**: EXIF carries the date. Duplicating it on the stamp creates confusion if the EXIF and the stamp ever disagree (e.g., after editing). The stamp answers "which file is this"; EXIF answers "when was this taken." Don't mix the jobs.

## Why bottom-right

Mirrors Acrobat Bates-stamp convention. Least intrusive on most photographic compositions — subjects are usually centered or upper-third framed, so bottom-right is typically empty sky, ground, or background. Right-aligned text is also how English readers expect identifiers (page numbers, signatures).

## Why semi-transparent black rectangle behind white text

Photographic images have unpredictable backgrounds. White text on bright sky disappears; black text on a dark floor disappears; a solid white box looks amateurish and obscures content. A semi-transparent black rounded rectangle with white text:

- Readable on every background from blown-out sky to pitch-dark shadow
- Shows a hint of the underlying image (not fully opaque), so it reads as a label rather than a hole in the photo
- Rounded corners keep it visually soft
- Professional appearance appropriate for exhibit use

Alpha of 160/255 was chosen after testing — high enough to guarantee text contrast, low enough to feel like a label rather than a paste-on sticker.

## Why 2.5% font ratio and 2% margin ratio

Tested against phone pics (1200×1600) and DSLR (4000×3000). At 2.5%:

- Phone pic: ~40px text — large enough to read when the photo is viewed at normal screen size
- DSLR: ~100px text — proportional, doesn't dominate

Fixed pixel sizes break on mixed-resolution sets. A stamp that looks right on a phone pic is invisible on a DSLR file and vice versa.

## Why we preserve EXIF at all costs

In evidence work, EXIF data carries:

- **Date/time taken** — often dispositive for timeline defense or impeachment of a witness's recollection
- **GPS coordinates** — location evidence (alibi, scene reconstruction, stitching with cell-site data)
- **Camera make/model** — authentication (was this really the witness's phone?)
- **Lens focal length, aperture, ISO** — can speak to whether a claimed sighting was physically possible
- **Device serial number (sometimes)** — chain of custody

Stripping EXIF from a photograph used in discovery could constitute spoliation of evidence. The script's approach: preserve EXIF or refuse to process the file. There is no middle ground.

## Why we re-orient via EXIF before stamping

Phone photos commonly have an EXIF orientation tag saying "the raw pixels are sideways, rotate them 90° when displaying." If you stamp the raw pixels and then re-save the EXIF, the stamp lands in the wrong corner once a viewer applies the rotation.

Fix: `ImageOps.exif_transpose()` bakes the rotation into the pixels before stamping, the stamp goes in the true bottom-right, and we save the image with EXIF intact (minus the orientation tag, which is now irrelevant because the pixels are already correctly oriented).

## Why the output convention breaks the D&W `Deliverables/` pattern

Most D&W skills output to `{CASE_ROOT}/Deliverables/{Phase}/{SkillName}/...`. This skill intentionally does not.

Reason: stamped images are **prepared evidence**, not work product. They need to stay physically adjacent to the originals so that:

1. The chain-of-custody story stays simple ("here are the originals, here are the stamped production copies, same folder")
2. When the attorney reviews scene photos six months later, the stamped versions are where the photos are — no separate tree to hunt through
3. Case folders can be archived, shared, or uploaded as single units without Deliverables having orphan references to evidence

If a future version needs to also write a production log or manifest into `Deliverables/`, that can coexist — the stamped images stay with the originals; the log goes to Deliverables.

## What this skill intentionally does NOT do

- **Sequential Bates numbering** (SMITH-000001, etc.) — use Acrobat on PDFs
- **Image compression or resizing** — evidence should not be altered
- **Format conversion** — JPEG in, JPEG out (exception: HEIC→JPG for portability, documented)
- **Redaction** — separate concern, separate skill (not built)
- **Metadata stripping** — opposite of our goal
- **Image analysis or OCR** — that's `dw-forensic-dump-analyzer` or `dw-crime-scene-auditor`

Narrow scope, done well, is the design goal.
