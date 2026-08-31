# Unused Space Carving — The Three Recovery Zones

Read this file at STEP 4 (Unused Space Carving) — it holds Recovery Zone 1 (WAL unused space), Zone 2 (freelist pages), and Zone 3 (unallocated space within pages) with what to look for and audit questions for each.

### Recovery Zone 1: WAL Unused Space

After a checkpoint, the frames that were copied back to the main .db become "stale" — they're no longer referenced by the -shm index, but their bytes remain in the -wal file until overwritten by new transactions. These stale frames are the **WAL Unused Space**.

**Recovery technique:**
- Parse the -wal file frame-by-frame, ignoring the -shm index (which only tracks "live" frames)
- Identify frames with salt values from previous checkpoint cycles
- Decode these frames against the database schema
- Cross-reference recovered records against the examiner's report — anything recovered here that's missing from the report is a finding

**Tools:**
- **SQLite Forensic Explorer** (Sanderson Forensics) — purpose-built for WAL unused space carving; parses stale frames and presents them alongside live data
- **Epilog** — SQLite journal forensics tool that reconstructs WAL transaction history
- **sqlite3** command-line with custom queries — `PRAGMA wal_checkpoint(PASSIVE)` can reveal checkpoint status; manual hex analysis of the -wal file reveals stale frame boundaries
- **Autopsy / Sleuth Kit** — general-purpose forensic suite with SQLite parsing plugins

### Recovery Zone 2: Freelist Pages

When SQLite deletes a record, the page (or portion of a page) is added to the database's **freelist** — a linked list of pages available for reuse. The data on freelist pages is intact until a new record is written to that page.

**Recovery technique:**
- Read the freelist chain starting from the freelist trunk page (offset 32–35 in the database header)
- Parse each freelist leaf page for record fragments using the table's schema
- Reconstruct partial records — even fragmentary recovery (e.g., a phone number without the associated message, or a timestamp without the full record) can be forensically significant

**Audit point:** If the examiner's report says "no deleted records found" but a freelist analysis was not performed, that conclusion is unsupported. Freelist pages are only accessible through FFS or Physical extractions — if a Logical extraction was used, the examiner never had access to freelists in the first place.

### Recovery Zone 3: Unallocated Space Within Pages

SQLite pages can contain **unallocated regions** — space between the cell pointer array and the cell content area, or space freed by in-place record deletion that didn't trigger page reorganization. These regions may contain fragments of deleted records.

**Recovery technique:**
- For each page in the database, compare the defined cell boundaries against the total page size
- Extract bytes in unallocated regions
- Attempt record reconstruction using the table schema and known SQLite record format (varint-encoded header, followed by column values)

**Tools for all three recovery zones:**
| Tool | WAL Unused | Freelist | Unallocated | Notes |
|------|-----------|----------|-------------|-------|
| SQLite Forensic Explorer | Yes | Yes | Yes | Best-in-class for defense work; visual WAL timeline |
| Cellebrite Physical Analyzer | Partial | Partial | No | Auto-merges WAL (destructive); limited carving |
| Magnet AXIOM | Partial | Yes | Partial | Better carving than Cellebrite; still auto-merges WAL |
| MSAB XRY | Partial | Partial | No | Known WAL merge errors (phantom artifacts) |
| Oxygen Forensic Detective | Yes | Yes | Partial | Decent WAL handling; verify version |
| Belkasoft Evidence Center | Yes | Yes | Yes | Strong SQLite carving; independent verification tool |
