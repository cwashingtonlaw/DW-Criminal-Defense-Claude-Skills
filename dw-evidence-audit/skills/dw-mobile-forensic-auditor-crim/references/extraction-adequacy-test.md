# Extraction Adequacy Test

Read at STEP 2 (Methodology Triage) of `dw-mobile-forensic-auditor-crim/SKILL.md` — the adequacy decision matrix applied after classifying the extraction level.

### Adequacy Test
Apply this decision matrix:

**If the case involves serious charges (homicide, sexual offense, LWOP-eligible, distribution/trafficking) AND a Logical or Advanced Logical extraction was used:**
> ⚠ **METHODOLOGY FLAG — CRITICAL:** Law enforcement chose a superficial extraction method (Level [X]) in a [charge severity] case. A Full File System or Physical extraction was available and would have captured deleted messages, app databases, SQLite WAL journals, and unallocated space artifacts that the chosen method cannot access. This methodological choice forfeited the ability to recover deleted evidence — evidence that could exculpate or further contextualize the State's narrative. Flag for: (1) cross-examination of examiner, (2) Missing Discovery Demand, (3) potential motion to compel re-extraction or independent examination.

**If a Logical extraction was used but the examiner's report draws conclusions about "no deleted data" or "no additional relevant data":**
> ⚠ **METHODOLOGY FLAG — MISLEADING CONCLUSION:** The examiner asserts [specific claim] but used a Logical extraction that is structurally incapable of accessing deleted records, SQLite WAL files, or unallocated space. This conclusion exceeds the scope of the methodology employed. The absence of evidence in a Logical dump is not evidence of absence.

**If a Full File System or Physical extraction was used, confirm:**
- Was the extraction verified with hash values (MD5 + SHA-256)?
- Was the write-blocker documented?
- Was the extraction performed on the original device or a clone?
- Were extraction logs preserved showing parameters and any errors?
