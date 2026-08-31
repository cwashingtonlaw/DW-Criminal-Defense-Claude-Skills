# Narrative Templates and Examples

Read at Step 3 (Generate Narratives) and Step 4 (Present for Attorney Review) of `dw-billing-narrative-generator-crim`; the entry template, Brief / Standard / Detailed example narratives, and the example approval UI moved verbatim from SKILL.md.

## Step 3 — Narrative Entry Template

**Template:**
```
[Skill Name / Activity]: [Case Phase]
Time: [X.XX hours]
LEDES Code: [Code] [Sub-Code if applicable]
Narrative: [2-3 sentences describing work performed, documents reviewed, analysis conducted, or deliverables created. Use professional language suitable for opposing counsel discovery.]
```

## Step 3 — Example Narratives (Brief / Standard / Detailed)

**Example Narratives:**

**Brief:**
"Reviewed body camera footage and police reports for Fourth Amendment issues. Prepared written analysis."
(1.5 hours, L110.3)

**Standard:**
"Reviewed body camera footage, dispatch records, and police incident reports. Analyzed for Fourth Amendment violations regarding warrantless search and seizure. Prepared written memorandum summarizing findings for motion preparation."
(1.5 hours, L110.3)
**Detailed:**
"Reviewed body camera footage (47 minutes), dispatch call recordings, incident reports, and witness statements. Analyzed evidence timeline and police conduct for potential Fourth Amendment violations including warrantless search, seizure, and detention issues. Prepared comprehensive memorandum with evidence citations and legal analysis framework for suppression motion preparation."
(1.5 hours, L110.3)

## Step 4 — Example Approval UI

**Example Approval UI:**
```
[Session: 2026-04-06] [Case: State v. Rodriguez, 2025-CV-12345]

| Skill | Hours | Code | Narrative | Action |
|-------|-------|------|-----------|--------|
| dw-suppression-motion-crim | 2.25 | L200.1 | [Standard narrative] | [Approve] [Edit] [Reject] |
| dw-brady-giglio-auditor-crim | 1.5 | L160.3 | [Detailed narrative] | [Approve] [Edit] [Reject] |
| dw-cross-exam-architect-crim | 3.0 | L300.1 | [Brief narrative] | [Approve] [Edit] [Reject] |

TOTAL BILLABLE HOURS: 6.75
[Save as Draft] [Submit to Billing] [Export]
```
