# UFDR File Format & Extraction Instructions

## Cellebrite UFDR Container Structure

A UFDR file (Cellebrite's native export container) is a renamed ZIP archive containing the following directory structure:

```
[filename].ufdr
├── report.html or report.xml         # Structured data export
├── files/                            # Extracted media files
│   ├── photos/
│   ├── videos/
│   ├── audio/
│   └── documents/
├── metadata/                         # Extraction metadata and device info
└── databases/                        # Raw SQLite databases (file system/physical)
    ├── *.db
    └── *.db-wal                      # Write-Ahead Log files
```

## Extraction & Processing

Run `scripts/preprocessing.py` → `extract_ufdr()` to unpack, or manually:

```bash
unzip -o [filename].ufdr -d [output_directory]
```

After extraction, inventory the contents and proceed with normal format handling:
- HTML tables → CSV conversion
- Media file cataloging
- Database inspection

## Critical WAL File Note

**CRITICAL:** If the UFDR contains raw SQLite databases, hand off to **dw-sqlite-recovery-crim** for WAL analysis before proceeding — WAL data may not survive repeated file access. Write-Ahead Log files (*.db-wal) contain uncommitted transactions that can recover deleted records.