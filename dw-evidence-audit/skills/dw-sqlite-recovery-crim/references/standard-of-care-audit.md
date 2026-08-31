# Standard of Care Audit — NIST SP 800-86, SWGDE, ASTM E2763, Challenge Layers, and Cross-Examination Framework

Read this file at STEP 5 (Standard of Care Audit) — it holds the three governing standards, the three-layer standard-of-care challenge, and the escalating cross-examination framework.

### NIST SP 800-86: Guide to Integrating Forensic Techniques into Incident Response

NIST Special Publication 800-86 establishes the standard framework for digital forensic examinations. Key requirements relevant to SQLite/WAL analysis:

- **Section 3.1 (Data Collection):** "All relevant data should be collected, even data that is not immediately relevant to the current investigation." WAL files, -shm files, and rollback journals are integral components of the SQLite database — collecting the .db file without its companions is an incomplete acquisition.
- **Section 3.2 (Examination):** The examination phase must "make the evidence visible" including "reducing the volume of data... while retaining the integrity of the data." This requires parsing WAL frames and recovering deleted records — not merely running an automated tool and accepting its parsed output.
- **Section 3.3 (Analysis):** Analysis requires the examiner to "draw conclusions based on the evidence found." An examiner who did not analyze WAL unused space, freelist pages, or unallocated database space cannot draw reliable conclusions about the absence of evidence.

### SWGDE (Scientific Working Group on Digital Evidence) Best Practices

SWGDE's "Best Practices for Mobile Phone Forensics" and "Best Practices for Computer Forensics" establish peer-reviewed standards:

- Examiners must document **all files acquired**, including journal and temporary files
- Examiners must use **validated tools** for the specific data type — auto-merging WAL files without independent verification violates validation requirements
- Examiners must distinguish between **"data not found" and "data not searched for"** — a conclusion of "no deleted messages" based on a tool that didn't search WAL unused space is professionally misleading

### ASTM E2763: Standard Practice for Computer Forensics

- Requires documentation of **all analysis steps** — if WAL analysis was not performed, this must be noted (and typically isn't)
- Requires that the examiner's conclusions be **supportable by the methodology used** — conclusions about deleted data that rely on tools incapable of WAL unused space recovery are unsupportable

### Building the Standard-of-Care Challenge

When the examiner's report omits WAL analysis, construct the challenge in three layers:

**Layer 1 — The Standard Exists:**
> "NIST SP 800-86 requires that forensic examinations recover 'all relevant data,' including data in temporary and journal files. SWGDE best practices require examiners to document all acquired files and to distinguish between 'data not found' and 'data not searched for.' These are the accepted professional standards in digital forensics."

**Layer 2 — The Standard Was Not Met:**
> "The examiner's report does not document analysis of the [database name]-wal file, the freelist pages of the [database name] database, or unallocated space within database pages. [If applicable: The forensic tool used (Cellebrite UFED / MSAB XRY) auto-merges WAL files during import, destroying the original WAL transaction history without preserving it.] The examiner either did not perform WAL analysis or used a tool that made WAL analysis impossible — either outcome falls below the standard of care."

**Layer 3 — The Failure Matters:**
> "The -wal file for [database] contained [X frames / Y KB of unused space] that could contain deleted records directly relevant to the charges. The examiner's conclusion that [specific conclusion, e.g., 'no deleted messages were found'] cannot be sustained because the methodology used was structurally incapable of searching the locations where deleted messages are most likely to persist. The absence of evidence in the examiner's report is an artifact of incomplete methodology, not an absence of evidence on the device."

### Cross-Examination Framework (Standard of Care)

These questions establish the examiner's failure to meet professional standards, escalating from foundational to damaging:

**Establishing expertise and awareness:**
1. "You're familiar with NIST Special Publication 800-86 — the Guide to Integrating Forensic Techniques into Incident Response?"
2. "That publication is considered a foundational standard in digital forensics, correct?"
3. "NIST 800-86 requires that forensic examinations recover all relevant data, including data in temporary and journal files?"

**Establishing what WAL files are:**
4. "You're aware that SQLite databases — which store text messages, call logs, and app data on mobile devices — use Write-Ahead Log files?"
5. "And you understand that when a user deletes a text message, the deleted data often persists in the WAL file?"
6. "The WAL file is, in effect, a transaction history — it records changes to the database in chronological order?"

**Establishing the gap:**
7. "In your examination of [device], did you independently analyze the WAL file for [database name]?"
8. "Did your forensic tool automatically merge the WAL file into the main database during import?" [If yes: "And that merge process overwrites the original WAL transaction history, correct?"]
9. "Did you preserve the original, unmerged WAL file before your tool processed it?"
10. "Your report concludes that [specific conclusion about deleted data]. That conclusion is based on the data your tool presented to you after it processed the database, correct?"
11. "But you did not independently verify whether the WAL file — the location where deleted data is most likely to persist — contained additional records?"

**The conclusion:**
12. "So your conclusion about [deleted data / absence of messages] is based on a methodology that did not examine the primary location where deleted data is stored?"
13. "Would you agree that, under NIST 800-86, a conclusion about the absence of data requires that the examiner actually search the locations where that data could exist?"
