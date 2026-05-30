# Edge Cases — dw-image-filename-stamp-crim

Known edge cases and how the script handles them. Read before modifying the script.

## Phone photos with EXIF orientation

**The problem.** iPhones and most Android phones capture the sensor data in a fixed orientation and add an EXIF orientation tag (values 1–8) telling viewers how to rotate it for display. If you open the raw pixels, the image may appear sideways or upside down.

**The fix.** `PIL.ImageOps.exif_transpose()` reads the orientation tag, rotates the pixels to match, and clears the tag. We do this *before* stamping so the stamp lands in the true bottom-right. The saved file has correctly oriented pixels and no orientation tag (because it no longer needs one).

**Verification.** Take an iPhone portrait photo, run it through the stamper, open the result in Preview. The stamp should be in the bottom-right regardless of how the phone was held when the photo was taken.

## HEIC/HEIF files (modern iPhones)

**The problem.** iPhones from iOS 11+ default to HEIC, not JPEG. Pillow can't read HEIC out of the box.

**The fix.** The script attempts to install `pillow-heif` on first run (trying three install strategies in order: plain, `--user`, `--break-system-packages`). Once installed, HEIC files read normally.

**Output format note.** HEIC files are saved as `.jpg` in the stamped output, not `.heic`. Rationale: HEIC support in legal-tech tools (TranscriptPad, TrialPad, Westlaw) is inconsistent as of 2026. JPEG is universally supported. If HEIC output is ever needed, `pillow-heif` supports writing HEIC — but the default is portability.

**Fallback.** If `pillow-heif` cannot be installed (corporate restrictions, offline machine), HEIC files are skipped and logged. The script does not crash.

## Progressive JPEGs

**The problem.** Some JPEGs are encoded progressively (loads in passes, low-res first). Pillow handles reading fine but the default save isn't progressive.

**Current behavior.** We save with `quality=95, subsampling=0` which produces high-quality baseline JPEGs. Progressive encoding is not preserved. This is a deliberate tradeoff — progressive output is slightly less compatible with older tools, and baseline JPEGs are the safer default for legal production.

**If a client specifically needs progressive output**, add `progressive=True` to the save kwargs for JPEGs. Not currently exposed as a flag.

## Images with ICC color profiles

**The problem.** Professional photography often embeds ICC color profiles (sRGB, Adobe RGB, DCI-P3). Dropping the profile on save causes color shifts when the image is later viewed in a color-managed application.

**The fix.** The script reads `im.info.get("icc_profile")` and passes it through to the save call. ICC profile preservation is automatic for JPEG, PNG, TIFF, and WebP outputs.

## Rotated pages / images with EXIF orientation values 5-8

**The problem.** EXIF orientation tag values 5–8 indicate the image is stored rotated AND mirrored (used rarely, mostly by old scanners). Some image tools handle these correctly; some don't.

**The fix.** `ImageOps.exif_transpose()` handles all 8 orientation values correctly — including mirrored variants.

## TIFF with alpha channel vs without

**The problem.** TIFFs can be RGB, RGBA, CMYK, grayscale, or palette-indexed. Saving an RGBA TIFF as RGB would drop the alpha channel (data loss); saving an RGB TIFF as RGBA creates a meaningless alpha channel.

**The fix.** The script tracks the original mode. If the original was not RGBA, the output converts back to the original's equivalent before saving. If the original was RGBA, alpha is preserved.

**Note.** TIFF compression defaults to LZW (lossless, well-supported). If you need a different compression, edit the `save_kwargs` in `stamp_image`.

## Files inside `stamped/` subfolders on re-run

**The problem.** If the user runs the script, then runs it again, the output tree now has `stamped/` subfolders containing images. Without guards, the script would recursively stamp its own outputs.

**The fix.** `iter_image_folders()` skips any folder whose path contains `stamped/` as a component. This means `Evidence/Scene/stamped/`, `Evidence/Scene/stamped/nested/`, and any other stamped descendant is excluded.

**Implication.** If a user legitimately has a folder named "stamped" (e.g., a client named Stamped), the script will skip it. This is an acceptable tradeoff — the word is specific enough to avoid collisions in practice, and the alternative (marker files, metadata tags) is more complex and more fragile.

## Re-running after partial processing (some files stamped, some not)

**The problem.** A run crashes halfway through. Some files in a folder have stamped versions, some don't.

**The fix.** The script checks for the existence of the destination file *per image*, not per folder. On re-run, already-stamped files are skipped and the missing ones are processed. No `--force` needed.

## Filenames with special characters

**The problem.** Filenames like `DSC (1).JPG`, `IMG_2024 - copy.jpg`, or filenames with Unicode (`Αρχείο.jpg`) could cause font rendering issues or path escaping bugs.

**Current behavior.** `pathlib.Path` handles special characters in filenames correctly at the OS level. Font rendering of non-Latin Unicode depends on the system font selected by `_load_font()`; DejaVu Sans (Linux fallback) and Helvetica (macOS default) both support wide Unicode ranges.

**Known limit.** If the filename contains characters outside the loaded font's glyph set, those characters will render as boxes (`.notdef`). Not a blocker for typical DSLR/phone filenames.

## Permissions / read-only source folders

**The problem.** If the source folder is read-only (e.g., mounted from a read-only volume), the script cannot create the `stamped/` subfolder there.

**Current behavior.** The script fails loudly with a clear permission error. It does not fall back to an alternate output location — failing loudly is safer than silently writing evidence copies somewhere unexpected.

**Workaround for read-only sources.** Copy the folder tree to a writable location first, then run the stamper there.

## Very large images (50 MP+)

**The problem.** A 50-megapixel image is ~150MB in memory when loaded as RGBA. Processing 500 of them uses serious RAM.

**Current behavior.** Pillow loads one image at a time; after each save, the image is garbage-collected. Peak memory is one image's worth, not the whole batch.

**If you're hitting memory limits** (unlikely on a Mac with 128GB of unified memory), the fix would be to process in smaller chunks by folder. Not currently needed.

## Password-protected or DRM-encrypted images

Not a thing in practice. JPEG, PNG, TIFF, HEIC, WebP — none support user-level encryption. If you hit this, it's not an image file; it's something wearing an image extension.

## "The stamp is too small / too big"

This is a design decision question, not an edge case — see `design-spec.md`. If genuinely needed, the `STAMP_FONT_RATIO` constant at the top of the script is the single knob. Don't expose it as a CLI flag without updating the SKILL.md to document it.
