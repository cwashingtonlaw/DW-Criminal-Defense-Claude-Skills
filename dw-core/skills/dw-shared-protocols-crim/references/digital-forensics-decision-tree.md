# Digital Forensics Audit Decision Tree

Three D&W evidence-audit skills form a sequential digital forensics stack. This reference guides routing and ordering.

---

## The Three Skills

| Skill | Purpose | Input | Output |
|---|---|---|---|
| `dw-mobile-forensic-auditor-crim` | Validates extraction **methodology** — tool settings, legal authorization, chain of custody, OS security bypass | Cellebrite/UFED/GrayKey extraction report | Methodology audit; suppression motion seeds |
| `dw-forensic-dump-analyzer-crim` | Mines phone dump **content** for defense intelligence — messages, calls, photos, location, financial, health data | Phone dump files (UFDR, spreadsheets, exports) | Defense Intelligence Report; timeline; alibi/impeachment evidence |
| `dw-sqlite-recovery-crim` | Recovers **deleted data** from SQLite databases and WAL files | Raw `.sqlite`, `.db`, `-wal`, `-shm` files from extraction | Recovered records; WAL transaction timeline; phantom-artifact audit |

---

## Mandatory Ordering

```
Step 1: dw-mobile-forensic-auditor-crim    (methodology audit)
          │
          ├── If extraction FAILS audit → dw-suppression-motion-crim
          │
          └── If extraction PASSES audit ↓
                │
Step 2: dw-forensic-dump-analyzer-crim     (content mining)
          │
          ├── If raw SQLite/WAL files present ↓
          │
Step 3: dw-sqlite-recovery-crim            (deleted data recovery)
```

**This ordering is not optional.** Two critical reasons:

1. **Legal foundation first.** If the extraction methodology is deficient (warrantless, overbroad, improperly executed), the entire phone dump may be suppressible. Mining content before auditing methodology wastes attorney time on evidence that may never be admissible.

2. **WAL auto-merge destruction.** Forensic tools (Cellebrite, MSAB XRY) auto-merge WAL files on import, destroying the original transaction history. If the extraction tool already auto-merged, the WAL data is gone — but if raw database files exist alongside the extraction, they must be analyzed by `dw-sqlite-recovery-crim` BEFORE any tool or process that might trigger a checkpoint merge.

---

## When to Invoke Each Skill

| You have... | Invoke |
|---|---|
| A Cellebrite/UFED/GrayKey/Magnet extraction **report** (PDF or HTML showing extraction settings, device info, tool version) | `dw-mobile-forensic-auditor-crim` |
| Phone dump **content** files (call logs, message exports, photo galleries, app data) | `dw-forensic-dump-analyzer-crim` (after methodology audit) |
| Raw `.sqlite`, `.db`, `-wal`, or `-shm` database files | `dw-sqlite-recovery-crim` (after content mining identifies gaps) |
| Both an extraction report AND content files | Run all three in sequence |
| Only content files (no extraction report available) | `dw-forensic-dump-analyzer-crim` directly — but flag that methodology was not auditable |

---

## WAL Destruction Warning

| Forensic Tool | WAL Behavior | Defense Risk |
|---|---|---|
| **Cellebrite UFED/PA** | Auto-merges WAL on import | Destroys original WAL transaction history; no option to preserve pre-merge state |
| **MSAB XRY** | Auto-merges; known merge errors | Documented phantom artifacts from incorrect WAL merge; may produce false records |
| **Magnet AXIOM** | Auto-merges by default; preservation optional | Better than Cellebrite/XRY, but verify examiner enabled preservation |
| **Oxygen Forensic Detective** | Configurable | Verify configuration used |

If the extraction report shows Cellebrite or XRY was used, WAL recovery may be limited to freelist-page carving. Flag this in the audit.

---

## Handoffs Between Skills

**Mobile Forensic Auditor → Dump Analyzer:** If methodology passes, offer to route to `dw-forensic-dump-analyzer-crim` with audit findings attached (locked containers, partial extractions, scope limitations become context for content analysis).

**Dump Analyzer → SQLite Recovery:** If the UFDR contains raw SQLite databases, hand off to `dw-sqlite-recovery-crim` for WAL analysis before proceeding — WAL data may not survive repeated file access.

**SQLite Recovery → Cross-Exam Architect:** All three skills can generate cross-examination seeds. Consolidate findings and route to `dw-cross-exam-architect-crim` for the examiner's cross outline.

**Any skill → Brady/Giglio Auditor:** If selective extraction or undisclosed data surfaces, route to `dw-brady-giglio-auditor-crim`.

**Any skill → Suppression Motion:** If 4th/5th Amendment violations surface, route to `dw-suppression-motion-crim`.
