# Contract 5: Case Brain Registration Entry — Full Schema

Read from the SKILL.md **Contract 5: Case Brain Registration Entry** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producer:** Any skill that generates a deliverable
**Consumer:** `dw-case-brain-crim` (writes to Obsidian), `dw-trial-notebook-builder-crim` (reads), `dw-case-dashboard-crim` (reads)

### COMPANION SKILL OUTPUTS Entry Format

Each entry in the Case Brain's COMPANION SKILL OUTPUTS section must follow this format:

```
- **[Date]** | `[skill-name]` | [Output filename] | [folder path relative to case root]
```

Example:
```
- **2026-04-01** | `dw-mobile-forensic-auditor-crim` | Mobile Forensic Extraction Audit — Cole 2026-04-01.docx | 01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

### OPEN ISSUES Entry Format (when audit identifies attorney action items)

```
- [ ] [Brief description of issue] — from `[skill-name]` ([date])
```
