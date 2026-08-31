# SQLite Architecture Primer — Pages, WAL, -shm, and Rollback Journals

Read this file at STEP 2 (SQLite Architecture Primer) — it holds the plain-language explanation of how SQLite stores data, why the WAL is the goldmine, the -shm file, and rollback journals, for framing findings to attorneys, judges, and jurors.

### How SQLite Stores Data

SQLite organizes data into **pages** (typically 4096 bytes). A database file is a sequence of these pages. When a record is "deleted" by an application, SQLite doesn't zero out the data — it marks the page space as available for reuse and adds it to the **freelist**. The actual bytes remain on disk until a new record overwrites them.

This is the first recovery opportunity: **freelist page carving** — scanning pages marked as "free" for remnants of deleted records.

### The Write-Ahead Log (WAL) — The Goldmine

Starting with SQLite 3.7.0 (2010), most mobile apps use WAL mode for performance. Here's how it works and why it matters for defense:

**Normal operation flow:**
1. App writes a new or modified record → SQLite appends it to the **-wal file** (not the main .db file)
2. The -wal file accumulates transactions as sequential "frames"
3. Periodically, SQLite performs a **checkpoint** — copying committed frames from the -wal file back into the main .db file
4. After a successful checkpoint, those frames become "unused" WAL space

**Why this creates a forensic goldmine:**

The -wal file preserves a **sequential transaction history**. Each frame has a header containing a salt value and frame number that establishes chronological order. Even after a checkpoint, the -wal file is not truncated by default — it's reused by overwriting from the beginning. This means:

- **Pre-checkpoint frames** contain data not yet written to the main database — the most recent activity
- **Post-checkpoint "unused" frames** contain remnants of previous transactions that were checkpointed — older activity that may have been subsequently deleted from the main database
- **The WAL records the order of operations**, allowing reconstruction of a timeline of user activity

### The -shm (Shared Memory) File

The -shm file is a shared-memory index that maps WAL frames to database pages. It tells SQLite which frames in the WAL are active. Forensically, the -shm file helps determine which WAL frames were "live" at the time of extraction versus which were remnants from prior checkpoints.

### Rollback Journals (-journal files)

Some older apps or specific configurations use rollback journal mode instead of WAL. In this mode, before modifying a page, SQLite copies the original page to a -journal file. If the transaction is rolled back, the journal restores the original data. Forensically, -journal files may contain original (pre-modification) versions of records — useful when the prosecution relies on the current state of a database but the defense needs to show what was there before.
