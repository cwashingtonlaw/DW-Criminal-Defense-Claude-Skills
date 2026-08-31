# WAL Sequencing Analysis — Methodology, Patterns, and Examiner Audit Questions

Read this file at STEP 3 (WAL Sequencing Analysis) — it holds the frame-by-frame sequencing methodology, the What to Look For pattern table, and the audit questions for the examiner's report.

### Sequencing Methodology

**Frame-by-frame analysis:**
Each WAL frame contains:
- **Page number:** Which database page this frame modifies
- **Commit marker:** Whether this frame is the last in a transaction (salt values change at each checkpoint cycle)
- **Salt values:** A pair of 32-bit integers that change with each checkpoint — frames sharing the same salt values belong to the same checkpoint cycle

**Building the timeline:**
1. **Identify checkpoint boundaries** using salt value transitions — each new salt pair marks a new checkpoint cycle
2. **Within each cycle, frames are sequential** — frame N happened before frame N+1
3. **Decode each frame's payload** using the database schema (read from page 1 of the main .db file) to determine what table and record the frame modifies
4. **Map decoded records to human-readable activity:** "At frame 847 (cycle 3), a row was inserted into the `message` table with text 'I'll be there at 9' sent to contact_id 42 at timestamp 1678234567"

### What to Look For

| Pattern | Significance |
|---------|-------------|
| **Messages in WAL not in main .db** | Messages were sent/received after the last checkpoint — the most recent communications, potentially never examined if WAL was ignored |
| **Deleted records recoverable from WAL unused space** | User deleted messages, but the WAL preserved the pre-deletion state — the deletion itself may be significant (consciousness of guilt, or alternatively, routine phone maintenance the State is mischaracterizing) |
| **Sequence gaps** | Missing frame numbers or salt-value discontinuities may indicate WAL truncation (manual or by the forensic tool) — demand explanation |
| **Timestamps inconsistent with WAL ordering** | If decoded record timestamps don't match the WAL frame sequence, this could indicate timestamp manipulation, timezone errors, or parsing artifacts |
| **Multiple writes to the same page** | Shows a record was modified multiple times — the WAL preserves each version, enabling reconstruction of edit history |

### Audit Questions for the Examiner's Report

For each critical database identified in the case:

- [ ] Did the examiner acquire the -wal file alongside the main .db file?
- [ ] Did the examiner acquire the -shm file?
- [ ] Did the examiner analyze WAL frames independently, or did they rely on the forensic tool's automatic WAL-merge?
- [ ] If the tool auto-merged the WAL, was the original pre-merge -wal file preserved?
- [ ] Did the examiner document the number of WAL frames, checkpoint cycles, and any sequence anomalies?
- [ ] Did the examiner attempt to recover records from WAL "unused" space (post-checkpoint frames)?
- [ ] Are there communications or activity in the WAL that do not appear in the examiner's parsed report?
