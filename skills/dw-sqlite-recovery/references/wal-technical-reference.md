# SQLite WAL Technical Reference — Defense Forensics Deep Dive

**For use by `dw-sqlite-recovery`. Internal reference. Treat as expert preparation material.**

This reference is the technical backstop for the audit and cross-examination work the skill produces. It collects what every defense digital-forensics witness should be able to testify to, what every defense lawyer should be able to walk a State's expert through on cross, and what tool-by-tool failures look like in the field. Everything here is grounded in the **SQLite Database File Format** (https://www.sqlite.org/fileformat.html) and the **Write-Ahead Logging** documentation (https://www.sqlite.org/wal.html). Cite-check against current SQLite documentation before testifying — the engine evolves and SQLite's own docs are the controlling authority.

---

## 1. Why WAL Files Matter for Defense

When a SQLite database is opened in WAL journal mode (default on modern iOS, Android, and macOS messaging apps), changes are NOT written into the main `.db` file at the moment they occur. Instead, they are written into a companion file with the same name plus the suffix `-wal` (e.g., `sms.db-wal`). Periodically, the engine "checkpoints" — copies committed data from the WAL into the main database and resets the WAL.

The defense consequence: **the most recent activity on the device — including data the user thought was deleted — is often present only in the WAL file, not the `.db`.** A forensic examiner who extracts only the `.db` and ignores the `-wal` and `-shm` companion files is presenting a sanitized, sometimes hours- or days-stale view of the device.

Common defense-relevant data that lives in WAL files:

- "Deleted" iMessages, SMS, and group chat messages
- Recently deleted contacts, call log entries, calendar events
- Browser history entries the user cleared
- WhatsApp and Signal messages purged from the user-facing app
- Photo metadata (location, timestamps) for photos removed from camera roll
- Health, fitness, and location data points removed from app history

If the State's case turns on what the device shows or doesn't show, the WAL is often the only place where the rebuttal evidence lives.

---

## 2. WAL Binary Format

A WAL file is a header followed by zero or more frames. Every byte position below is fixed by the SQLite specification.

### 2.1 WAL Header (32 bytes, big-endian)

| Offset | Size | Field | Defense Significance |
|---|---|---|---|
| 0 | 4 | Magic number (0x377f0682 or 0x377f0683) | Confirms the file is a SQLite WAL. Wrong magic = the file has been truncated, corrupted, or replaced. |
| 4 | 4 | File format version (currently 3007000) | Mismatch with the database file = examiner used a tool that doesn't understand the WAL version. |
| 8 | 4 | Page size in bytes (must match the main DB) | Mismatch = corrupted pairing. |
| 12 | 4 | Checkpoint sequence number | Increments every checkpoint. A high number paired with a small WAL = many checkpoints; a low number with a huge WAL = recent heavy activity uncheckpointed. |
| 16 | 4 | Salt-1 | Used in frame header checksums. Reset on every checkpoint. |
| 20 | 4 | Salt-2 | Same as Salt-1; also reset on checkpoint. |
| 24 | 4 | Checksum-1 | Cumulative checksum protecting WAL integrity. |
| 28 | 4 | Checksum-2 | Cumulative checksum protecting WAL integrity. |

If Salt-1/Salt-2 do not match the values in the corresponding `-shm` (shared memory) file, the WAL has been opened by a different process than expected — possibly the forensic tool itself if not handled correctly.

### 2.2 WAL Frame (24-byte header + page-size payload)

After the header, the WAL is an array of frames. Each frame is:

| Offset | Size | Field | Defense Significance |
|---|---|---|---|
| 0 | 4 | Page number in the database | Tells you which DB page the frame replaces. |
| 4 | 4 | "Commit flag" — DB size in pages after this frame, or 0 | Non-zero = this frame was the last in a committed transaction. Zero = mid-transaction frame. **A frame with a zero commit flag may contain data that was rolled back — but that data still exists in the WAL until checkpoint.** |
| 8 | 4 | Salt-1 (must match WAL header) | Validates frame as belonging to current WAL generation. |
| 12 | 4 | Salt-2 (must match WAL header) | Same. |
| 16 | 4 | Checksum-1 | Cumulative; protects all bytes through this frame. |
| 20 | 4 | Checksum-2 | Same. |
| 24 | page_size | Page payload (raw database page) | The actual data — a copy of the database page as it would look after this frame is checkpointed. |

The frame payload is a complete database page, byte-for-byte. To reconstruct historical state, you walk the WAL frame-by-frame, replaying each page substitution in order — the equivalent of replaying a journal.

### 2.3 The `-shm` (Shared Memory) File

The `-shm` file is a small file (32 KB on most systems) used by SQLite to coordinate WAL access between processes. It contains:

- An index of frame numbers per database page
- Reader/writer locks
- The "wal-index" — a hash table mapping page numbers to the most recent frame containing that page

For defense purposes, the `-shm` is generally not directly evidentiary, **but its presence or absence at acquisition time tells you something**:

- `-shm` present at acquisition + tool didn't acquire it = the examiner left state on the device that should have been collected.
- `-shm` rebuilt by the forensic tool = the examiner *opened* the database, which is a write operation that mutates state. This is a **chain of custody issue**.

---

## 3. Checkpoint Mechanics

A checkpoint is the operation that copies committed WAL frames back into the main `.db` file. There are several checkpoint modes:

| Mode | Behavior | Defense Significance |
|---|---|---|
| `PASSIVE` | Default. Copies as much as possible without blocking readers/writers. May leave frames behind. | After a passive checkpoint, the WAL is *truncated to zero only if no readers are still using earlier frames*. Otherwise, the WAL retains older frames. |
| `FULL` | Waits for all writers to finish, then checkpoints everything. | Forces all WAL data into the main DB. |
| `RESTART` | Like FULL, plus blocks new writers until all readers finish. | Used during shutdown. |
| `TRUNCATE` | Like RESTART, plus resets the WAL file to zero bytes. | This is the only mode that *deletes* WAL data. |

**Implications for defense:**
- A "checkpointed" device does NOT mean the WAL is empty. Most checkpoints are PASSIVE and leave data behind.
- iOS and Android typically run PASSIVE checkpoints under low-memory pressure; FULL/RESTART/TRUNCATE only at app shutdown or device shutdown.
- A WAL file growing well beyond 1000 pages typically indicates the device has not had a clean shutdown recently — meaning forensic acquisition captured an in-flight state, which is a feature, not a bug.

### Auto-checkpoint threshold

By default, SQLite triggers an auto-checkpoint when the WAL reaches 1000 pages. Most apps leave this default. But:

- iOS limits aggressive WAL growth to manage device storage.
- Apps can override the threshold via PRAGMA wal_autocheckpoint.

If a State's expert claims "the WAL is too small to contain anything significant," counter with: 1000 pages × 4 KB page size = up to 4 MB of recent data, including potentially thousands of message records.

---

## 4. Freelist Chain Navigation

When SQLite deletes a record, the page it lived on is added to the database's "freelist." Pages on the freelist are eligible for reuse but are NOT zeroed out — the deleted data remains until the page is overwritten. This is true in both the main `.db` and in WAL frames.

### Freelist structure

| Component | Where | Significance |
|---|---|---|
| Database header pointer | Bytes 32–35 of page 1 | Page number of the first trunk page in the freelist. |
| Trunk page | Variable | A linked list node. Header: pointer to next trunk + count of leaf pages. Body: page numbers of the leaves. |
| Leaf page | Variable | A page that has been "freed" but still contains its old contents. |

To recover deleted records:

1. Read the database header to get the freelist trunk pointer.
2. Walk the trunk chain; for each trunk, enumerate its leaves.
3. Read each leaf as a raw page; parse the cell pointer array and cell payload area.
4. Even though the cell pointer array marks the cells as deleted, the cell payload bytes are usually intact until overwritten.
5. Repeat for every WAL frame whose page number matches a freed page — those frames hold the page's *historical* states, often containing records that were live at one point.

This is **carving with structure** — much higher fidelity than blind raw-disk carving because we know exactly where to look and what the data should look like.

---

## 5. Record Reconstruction

Even on freed or partially overwritten pages, individual records can often be reconstructed because of SQLite's record format:

### Record format

| Field | Size | Description |
|---|---|---|
| Record header length | 1–9 bytes (varint) | Total length of the header. |
| Type codes | Variable | One varint per column: 0=NULL, 1=8-bit int, 2=16-bit int, ..., 9=constant 1, 10–11=reserved, 12+even=BLOB, 13+odd=TEXT. The high bits of TEXT/BLOB type codes encode length. |
| Column values | Variable | Concatenated, in column order. |

### Reconstruction strategy

1. Scan the page for plausible record header lengths (small varints near the bottom of the cell payload area).
2. For each candidate, parse the header and compute the total record size.
3. Validate by checking that text columns contain valid UTF-8 and that integer columns are in plausible ranges (e.g., timestamps should be reasonable Unix or Mac absolute times).
4. Cross-reference the rowid (primary key) against any overlapping records in the live database to detect deletions.

**Defense-favorable framing:** When a State's expert testifies that a deleted message "cannot be recovered" without examining freelist leaves and WAL frames, that statement is technically false. The cross-examination question becomes: *"Did you examine the freelist? Did you parse the WAL frames? If not, how do you know what was on this device?"*

---

## 6. Forensic Tool Deficiency Documentation

Defense audits should specifically test whether the State's forensic tool handled WAL/SHM correctly. The most common failures by tool:

### Cellebrite (UFED Physical Analyzer / 4PC)

- **Default behavior:** Reads the `.db` and treats `-wal` as auxiliary. Some versions checkpoint the WAL silently *before* reading the database, destroying evidence.
- **Defense check:** Inspect the extraction log for any line containing "checkpoint" or "wal_autocheckpoint" against the target database. If present, the tool wrote to the device. If the tool's manifest shows the `-wal` file with size 0, ask whether the original was zero or whether the tool truncated.
- **Cross-exam question:** *"Did your tool perform a checkpoint operation on this database before reading it? Yes or no — and if you don't know, explain why your report doesn't say."*

### GrayKey (Magnet Forensics)

- **Default behavior:** Generally captures `-wal` and `-shm` alongside `.db` for extracted apps, but "logical" extractions may miss WAL data depending on agent permissions.
- **Defense check:** Compare file listing in the GrayKey output package — confirm that for every relevant database, all three files (`.db`, `-wal`, `-shm`) are present and timestamps are consistent.
- **Cross-exam question:** *"For the sms.db database, your extraction includes the `.db` file at [size] bytes. Does it include the `-wal` companion file? What size? What timestamps?"*

### Oxygen Forensic Detective

- **Default behavior:** Captures companion files, but the parser sometimes only reads the `.db` and silently skips the WAL during analysis.
- **Defense check:** Check the analysis report for an explicit "WAL frames analyzed: N" entry. If absent, the tool may have ignored the WAL even though it was extracted.
- **Cross-exam question:** *"Your report shows [X] messages from sms.db. How many WAL frames did your tool analyze? Were they parsed for additional records?"*

### Magnet AXIOM

- **Default behavior:** Modern versions parse WAL frames for known SQLite databases. But "Quick Image" or "Triage" modes often skip WAL analysis.
- **Defense check:** Identify the AXIOM module used. If "Triage" or any quick mode, the WAL was likely skipped.

### Open-source / Linux-based tools (Plaso, sqlite3 CLI, sqlitedict)

- These tools generally do NOT analyze WAL/SHM unless explicitly directed.
- A `.dump` of a SQLite database via the `sqlite3` CLI checkpoints the WAL and produces output reflecting the checkpointed state — destroying the historical view in WAL frames.

### General principle

The defense argument is rarely "the State's tool can't read WAL files" — it is "the State's expert *did not* read them, *or* the tool checkpointed before reading." Both are evidence-destruction concerns under La. C.E. Art. 702 reliability and 5th Circuit Daubert factors.

---

## 7. Defense Expert Examination Checklist

When the firm retains a defense digital forensics expert to re-examine a State's extraction or to examine a device under court order, this is the checklist of items the expert should address — and the lawyer should confirm in writing before deposition or trial.

### Acquisition phase
- [ ] Did the State's tool or our re-extraction acquire `-wal` and `-shm` files alongside every `.db` file?
- [ ] Was the device imaged in a write-blocked manner, or did the extraction process write to the device (e.g., by opening WAL databases)?
- [ ] Are file modification timestamps for `.db`, `-wal`, and `-shm` consistent with each other?
- [ ] Are SHA-256 hashes of all three files documented at acquisition?

### Initial integrity check
- [ ] Validate WAL header magic number.
- [ ] Confirm WAL header page size matches the `.db` page size.
- [ ] Validate frame checksums sequentially through the WAL.
- [ ] Identify any corrupted or unparseable frames and document.

### Frame-by-frame analysis
- [ ] Enumerate every frame in the WAL.
- [ ] For each frame: page number, commit flag, frame index, hash of payload.
- [ ] Identify frames that replace the same page number — older states of the same record.
- [ ] Replay the WAL in order to reconstruct the database state at any committed transaction boundary.

### Freelist analysis
- [ ] Walk the freelist trunk chain in the main `.db`.
- [ ] Carve each leaf page for record headers.
- [ ] Cross-reference recovered rowids against live records to identify deletions.
- [ ] For each WAL frame matching a freelist leaf page: extract older record states.

### Record reconstruction
- [ ] Parse recovered records using the table's `CREATE TABLE` schema (read from `sqlite_master`).
- [ ] Validate column types against schema; flag mismatches.
- [ ] Translate Unix timestamps, Mac absolute times, and any application-specific encodings.
- [ ] Generate a deletion timeline: each deleted record with last-known timestamp and inferred deletion timestamp.

### Reporting
- [ ] Document all findings with frame numbers, page numbers, and rowids.
- [ ] State explicitly: "The State's expert did NOT examine the WAL/freelist for this database. The following records were recoverable from those structures."
- [ ] If no recoverable data: state explicitly that the absence of recoverable data is itself a finding (and may be exculpatory if the State's narrative depends on the existence of deleted-but-present data).

### Daubert / La. C.E. Art. 702 framing
- [ ] Confirm methodology aligns with NIST SP 800-86 (Guide to Integrating Forensic Techniques) and SWGDE digital evidence standards.
- [ ] Identify peer-reviewed publications supporting the WAL/freelist analysis methodology (e.g., the SQLite documentation itself, plus publications from the DFIR community).
- [ ] Identify the error rate of the methodology — for WAL replay and freelist carving, this is essentially "lossless when correctly applied" because we are reading the actual binary structures, not making inferences.
- [ ] Confirm general acceptance in the digital forensics community.

---

## 8. Common Cross-Examination Trap Questions

A well-prepared State's expert may try to deflect with these answers. Cross-examination prep should anticipate:

| State's expert says | Defense response |
|---|---|
| "WAL files are temporary; they get deleted." | Only on TRUNCATE checkpoint, which only happens at clean shutdown. Devices captured live retain WAL data. |
| "There was no WAL file when I examined this database." | Did you check whether your tool checkpointed it on open? Show me the chain of custody for the `-wal` file at acquisition time. |
| "WAL analysis isn't standard practice." | SQLite's own documentation describes WAL as the default journal mode. Failing to analyze it is failing to read the file format the data is stored in. |
| "I didn't have time to do a full WAL analysis." | A WAL replay on a 4 MB file takes seconds with the right tooling. What tooling did you use? |
| "The WAL contained no recoverable data." | Did you walk the freelist? Did you carve cell payloads on freed pages? What was your analysis methodology, step by step? |
| "My tool automatically does this." | What tool? What version? Show me the analysis log entry that says "WAL frames parsed: N." |

---

## 9. Authority and Standards

- **SQLite Database File Format:** https://www.sqlite.org/fileformat.html — controlling reference. SQLite's own format documentation is the authority every expert and judge can verify.
- **SQLite Write-Ahead Logging:** https://www.sqlite.org/wal.html — covers WAL behavior, checkpoint modes, autocheckpoint thresholds.
- **NIST SP 800-86, Guide to Integrating Forensic Techniques into Incident Response** — establishes minimum methodology standards including the requirement to preserve volatile and journal data.
- **SWGDE Best Practices for Computer Forensics** — peer-reviewed methodology standards.
- **DFRWS papers on SQLite forensics** — search the proceedings of the Digital Forensics Research Workshop for "SQLite WAL" — multiple peer-reviewed papers since 2014 establish carving methodology.
- **La. C.E. Art. 702 / *State v. Foret*, 628 So. 2d 1116 (La. 1993)** — Louisiana's expert reliability framework.
- **Daubert v. Merrell Dow Pharmaceuticals, 509 U.S. 579 (1993)** — federal reliability framework, persuasive in Louisiana.

---

## 10. Defense Motions Toolbox (Cross-Reference)

WAL/SHM analysis findings drive these motions, generally produced by other D&W skills:

- **Motion to Compel Production** — raw `.db`, `-wal`, `-shm` files, extraction logs, tool validation records. Produced via `dw-pretrial-motion-library`.
- **Motion for Independent Examination** — defense expert re-extraction with WAL-aware tooling. Produced via `dw-pretrial-motion-library`.
- **Daubert / Foret Challenge** — challenging the State's expert under La. C.E. Art. 702 when the methodology omits WAL analysis. Produced via `dw-expert-witness-evaluator`.
- **Cross-examination outlines** — produced via `dw-cross-exam-architect` from the seeds in Step 7 of the parent skill.

---

*Last reviewed: 2026-04-29. Maintained by D&W. The SQLite project occasionally evolves the WAL format and checkpoint behavior — when in doubt, consult the live SQLite documentation rather than this snapshot. This reference is internal preparation material; it is not a substitute for retaining a qualified defense digital forensics expert in any case where SQLite/WAL evidence is contested.*
