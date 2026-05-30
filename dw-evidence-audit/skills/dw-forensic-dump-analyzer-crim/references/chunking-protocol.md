# Chunking Protocol — Large Forensic Dump Handling

This protocol governs how the Forensic Dump Analyzer processes data that exceeds a single context window. Cell phone dumps routinely contain tens of thousands of records across multiple data categories. Attempting to ingest everything at once will crash the analysis.

**Core principle:** Break the dump into manageable chunks, analyze each chunk through all eight defense lenses (prioritized by charge type), track cumulative findings in a Session State Block, surface high-value findings immediately, and consolidate at the end.

---

## When to Chunk

**Chunk when ANY of these are true:**
- Total data exceeds ~50,000 rows or ~2MB of text content
- More than 5 data categories present
- Any single file exceeds ~15,000 rows
- Cellebrite HTML reports exceed ~100 pages
- Attorney provides a full extraction folder

**Single-pass when ALL true:** Under ~15,000 rows, ≤ 3 categories, attorney pre-filtered, clean CSV/Excel format.

When in doubt, chunk. Crashing mid-analysis wastes more time than unnecessary chunking.

---

## Tiered Chunking Strategy

### Charge-Adaptive Tier Ordering

**The charge type overrides the default tier order** using the Chunking Tier Override column from SKILL.md:

| Charge Type | Override |
|-------------|----------|
| Homicide / Manslaughter | Location → Tier 1 |
| Sexual Offense | Victim communications → Tier 1 |
| Drug Offenses | Call logs → Tier 1 |
| Robbery / Burglary | Location → Tier 1 |
| Assault / DV | Victim communications → Tier 1 |
| Weapons Offenses | Photos/EXIF → Tier 2 |
| LWOP-Eligible | No override — full tiers at maximum rigor |

When an override applies, swap the overridden category into Tier 1 and shift displaced categories down one.

### Default Tier Priority Order

| Tier | Data Category | Why First |
|------|--------------|-----------|
| 1 | SMS/MMS/iMessage during critical window | Alibi, admissions, victim contact |
| 2 | Chat apps during critical window | Same as T1, often missed by LE |
| 3 | Call logs during critical window | Timeline anchoring, frequency |
| 4 | Location data during critical window | Alibi proof or State contradiction |
| 5 | SMS/Chat apps — expanded date range | Relationship context, third-party |
| 6 | Call logs — expanded date range | Frequency baselines |
| 7 | Browser history & search queries | State of mind, guilt rebuttal |
| 8 | Photos/Videos with EXIF | Location/timestamp corroboration |
| 9 | App data (financial, health, notes) | Supplementary intelligence |
| 10 | System logs, settings, installed apps | Technical context |

### Within Each Tier — Date Windowing

If a single tier is still too large:
1. **Critical window:** Offense date/time ± 48 hours
2. **Extended window:** 2 weeks before and after
3. **Full range:** All remaining data

### Chunk Size Target

~5,000–10,000 rows of structured data per chunk. For Cellebrite HTML, one report section per chunk.

---

## Pre-Processing: Data Reduction Before Chunking

Run `scripts/preprocessing.py` or apply these steps manually:

### 0. Duplicate & Artifact Detection (Run First)
Use `deduplicate_records()` from the preprocessing script. Cellebrite frequently exports the same record into multiple tables. Deduplicate before chunking to avoid inflating counts and burning tokens.

### 1. Convert Verbose Formats to Lean CSVs
Use `cellebrite_html_to_csv()` from the preprocessing script. Cellebrite HTML is often 10x the token count of equivalent CSV.

### 2. Strip Metadata Noise
Remove columns with no defense value: internal database IDs, hash values (unless chain of custody is at issue), parsing tool metadata, duplicate timestamp formats.

### 3. Date-Filter Before Loading
Use `filter_critical_window()` from the preprocessing script. If the attorney specifies a critical window, filter ALL files to that window before loading.

### 4. Deduplicate
Use `deduplicate_records()`. Deduplicate on content + timestamp + participants before analysis.

---

## Session State Block

### Full Display (session start, resume, and session end only)

```
╔══════════════════════════════════════════════════════════╗
║              SESSION STATE BLOCK                         ║
║         [Case Name / Docket No.]                         ║
╠══════════════════════════════════════════════════════════╣
║ PHONE:         [Owner / Make / Model / Phone Number]     ║
║ CHARGES:       [All counts]                              ║
║ DEFENSE THEORY: [Summary]                                ║
║ STATE'S CLAIM:  [What State says phone proves]           ║
║ CRITICAL WINDOW: [Date/time range]                       ║
║ KEY PEOPLE:     [Names / numbers]                        ║
║ KEY LOCATIONS:  [Addresses / areas]                      ║
║ EXTRACTION AUTH: [Examiner / Tool / Hash status]         ║
╠══════════════════════════════════════════════════════════╣
║ CHUNKS COMPLETED:                                        ║
║   [✓/—] Tier 1–10 with status and record counts         ║
╠══════════════════════════════════════════════════════════╣
║ CUMULATIVE FINDINGS:                                     ║
║   Defense-Favorable: N (S strong / M moderate)           ║
║   Adverse: N | Handoffs: [skills] | Leads: N pending     ║
╠══════════════════════════════════════════════════════════╣
║ NEXT CHUNK: [Tier/category and date range]               ║
╚══════════════════════════════════════════════════════════╝
```

### Compact Display (between chunks — after first display)

After the initial full display, use a single-line status between chunks to save tokens:

```
[SSB: 3/10 chunks | 12 findings (8 fav, 4 adverse) | 2 leads pending | Next: T4 Location critical window]
```

Only redisplay the full block on: session start, session resume from Continuation Block, and session end (final consolidation).

---

## Chunk Findings Ledger

After each chunk, produce a compressed summary:

```
CHUNK FINDINGS — [Tier X: Category] | [N] records | [date range]
──────────────────────────────────────────────────────────
DEFENSE-FAVORABLE:
  [F1] [description] | [source: file, rows] | STRONG ← EXPANDED BELOW
  [F2] [description] | [source] | MODERATE
  [F3] [description] | [source] | CONTEXTUAL

ADVERSE:
  [A1] [description] | [source] | CONCERNING

MISINTERPRETATION FLAGS:
  [M1] [pattern] | [correct interpretation]

CROSS-CHUNK LEADS: [L1] [contact/pattern for later tiers]
HANDOFFS: → [skill]: [what]
──────────────────────────────────────────────────────────
```

### Progressive Surfacing of High-Value Findings

When a finding is rated **STRONG**, expand it immediately in the chunk output — do not compress to one line:

```
═══ STRONG FINDING — IMMEDIATE ATTENTION ═══
FINDING: [Full description]
DATA: [Specific records with source file, row/line, timestamp]
DEFENSE VALUE: [Why this matters — plain language]
SUGGESTED USE: [Cross-exam, motion, argument — specific and actionable]
AUTH: [Complete / Exception noted]
BASELINE CONTEXT: [If baseline built — how this compares to normal]
═══════════════════════════════════════════
```

This lets the attorney act on critical findings before the full analysis is complete. Reserve one-line compression for MODERATE and CONTEXTUAL findings only.

---

## Early Termination Gate

After each chunk, assess whether continuing adds meaningful value:

### Assessment Criteria

| Condition | Recommendation |
|-----------|---------------|
| Strong alibi established (location + communications confirm client elsewhere) | Offer to stop: *"Strong alibi from T1-T2. Continue remaining tiers or generate report?"* |
| 3+ STRONG findings identified across different lenses | Offer to stop or accelerate: *"Solid foundation established. Continue at full depth, scan-only remaining tiers, or generate report?"* |
| All data so far is adverse — nothing helps | Be honest and offer options: *"No defense-favorable findings in T1-T4. Continue (later tiers may yield something), or stop and recommend next steps?"* |
| Attorney is in a time crunch | Always ask between chunks: *"Ready for next chunk, or generate report with current findings?"* |

### Early Termination Options

1. **Stop and report:** Generate report with findings to date. Note which tiers were analyzed and which were skipped.
2. **Scan remaining tiers:** Continue through remaining tiers at scan-only depth — flag obvious findings, skip deep analysis. Faster but less thorough.
3. **Continue full analysis:** Proceed through all tiers at full depth.

The attorney decides. Never silently skip tiers — always present the choice.

---

## Chunk Execution Workflow

For each chunk:

1. **Display status** — compact SSB line (full block only at session boundaries)
2. **Load chunk data** — files/rows for this tier and date window
3. **Apply defense lenses** — prioritized per charge type (full depth for primary, scan for secondary)
4. **Check Cross-Chunk Leads** — search this chunk for leads from prior chunks
5. **Produce Chunk Findings Ledger** — compressed for MODERATE/CONTEXTUAL, expanded for STRONG
6. **Update SSB** — compact line with new counts
7. **Assess early termination** — offer the attorney the choice if criteria met
8. **Present next steps** — what comes next, or if analysis is complete

**Between chunks:**
> *"T[X] complete — [N] defense / [N] adverse. [Early termination offer if applicable, or:] Next: T[Y] [Category]. Continue?"*

---

## Continuation Protocol — Resuming Across Sessions

When a session must end before completion:

```
╔══════════════════════════════════════════════════════════╗
║              CONTINUATION BLOCK                          ║
║         Save this — paste it to resume analysis          ║
╠══════════════════════════════════════════════════════════╣
║ TO RESUME: Paste this block + next data file(s). Say:    ║
║ "Continue forensic dump analysis — [Case Name]"          ║
╠══════════════════════════════════════════════════════════╣
║ [FULL SESSION STATE BLOCK]                               ║
║ [ALL CHUNK FINDINGS LEDGERS FROM THIS SESSION]           ║
╚══════════════════════════════════════════════════════════╝
```

**On resume:** Parse SSB + ledgers, read this protocol, resume at next tier, do NOT re-analyze completed chunks.

---

## Final Consolidation

When all tiers are complete (or attorney elects early termination):

1. **Merge all Chunk Findings Ledgers** into a unified findings database
2. **Resolve Cross-Chunk Leads** — confirm or dismiss each
3. **Re-rank findings** — some gain/lose significance with full data context
4. **Identify cross-category patterns** — connections visible only in consolidation
5. **Generate report** — Full Report or Quick Brief based on scope (see SKILL.md Step 6)
6. **Final SSB update** — full block with "ANALYSIS COMPLETE" status

Note which tiers were analyzed, which were scanned, and which were skipped (if early termination).

---

## Quick Reference — Estimated Chunk Sizes

| Data Category | Typical Volume | Chunks Needed |
|--------------|---------------|---------------|
| SMS/MMS (1 year) | 5K–50K records | 1–5 |
| Chat apps (all) | 10K–200K records | 2–20 |
| Call logs (1 year) | 1K–10K records | 1 |
| Location data (1 year) | 5K–100K records | 1–10 |
| Browser history | 500–5K records | 1 |
| Photos/EXIF | 100–10K records | 1–2 |
| App data | Varies | 1–5 |
