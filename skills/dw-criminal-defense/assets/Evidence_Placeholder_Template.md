# Digital Evidence Placeholder Template

This template defines the layout for the one-page Digital Evidence Placeholder PDF generated for each media folder in `05 - Evidence`. The `scripts/generate_placeholders.py` script uses this layout.

## Placeholder Layout

```
────────────────────────────────────────────────────
DIGITAL EVIDENCE PLACEHOLDER

EVIDENCE ID/NAME: [folder name from evidence directory]

NUMBER OF FILES IN FOLDER: [auto-counted]

MEDIA TYPE:
☐ Audio     ☐ Photo/Image     ☐ Video     ☐ Other Data
(checked based on file extension classification)

DESCRIPTION:
[Auto-generated: "This folder contains X files: Y audio,
Z video, W images, N other. File formats: .mp4, .jpg, ..."
Includes file format breakdown by count.]

STORAGE PATH / LOCATION:
[Full absolute path to the source folder for retrieval]
────────────────────────────────────────────────────
```

## Media Type Classification

| Category    | Extensions                                                                                  |
|-------------|---------------------------------------------------------------------------------------------|
| Audio       | .wav, .mp3, .aac, .flac, .ogg, .wma, .m4a, .wpl                                           |
| Photo/Image | .jpg, .jpeg, .png, .bmp, .tiff, .gif, .raw, .cr2, .nef, .heic                              |
| Video       | .mp4, .avi, .mov, .mkv, .wmv, .flv, .mts, .vob, .mpg, .mpeg, .m4v, .3gp, .dav, .264, .sec, .thm, .bup, .ifo |
| Other Data  | .pdf, .docx, .doc, .txt, .xlsx, .csv, .exe, .dll, .db, .seclist                            |
