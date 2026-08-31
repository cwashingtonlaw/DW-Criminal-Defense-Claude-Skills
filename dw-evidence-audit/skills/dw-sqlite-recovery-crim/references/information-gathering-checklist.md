# Information Gathering Checklist

Read this file at STEP 1 (Information Gathering Protocol) — it holds the full Essential / Strategic checklist (items 1-10) to collect before auditing.

### Essential (must have before auditing)
1. **Forensic Report(s):** The examiner's report — Cellebrite, MSAB XRY, Magnet AXIOM, or equivalent
2. **Raw Database Files (if available):** .db or .sqlite files with their companion -wal and -shm files
3. **Device Identifier:** Make, model, OS version (determines SQLite version and WAL behavior)
4. **Extraction Type Used:** Logical, Advanced Logical, FFS, or Physical — this determines whether WAL files were even captured
5. **Charges:** All counts with statutory citations — severity determines how aggressively to challenge incomplete recovery
6. **What the State Claims the Database Evidence Proves:** The prosecution's theory regarding the digital records

### Strategic (request if not provided)
7. **Which databases matter to the case?** SMS/MMS (sms.db), iMessage (chat.db), WhatsApp (ChatStorage.sqlite / msgstore.db), call logs, location data, browser history, etc.
8. **Defense theory of missing data:** Are there messages/records the defense believes should exist but don't appear in the examiner's report?
9. **Examiner credentials:** Name, agency, certifications, SQLite-specific training
10. **Whether raw database + WAL files were produced in discovery** — or only parsed/exported reports

**Present missing info as a ranked checklist before auditing.** If essentials 1, 4, and 5 are missing, do not audit — ask first.
