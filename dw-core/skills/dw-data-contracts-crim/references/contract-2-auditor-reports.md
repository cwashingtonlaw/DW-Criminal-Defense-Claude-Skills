# Contract 2: Auditor Skill Reports — Full Schema

Read from the SKILL.md **Contract 2: Auditor Skill Reports** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producers:** All `dw-*-auditor` skills (mobile-forensic, video-evidence, crime-scene, chain-of-custody, cell-site-geolocation, social-media, eyewitness-identification, confession-interrogation, child-forensic-interview, expert-witness-evaluator, dna-forensic-biology, crime-lab)
**Consumers:** `dw-cross-exam-architect-crim`, `dw-trial-notebook-builder-crim`, `dw-case-dashboard-crim`, `dw-case-brain-crim`

### Filename Pattern
`[Audit Type] Report — [Client Last Name] [Date].docx`

Examples:
- `Mobile Forensic Extraction Audit — Cole 2026-04-01.docx`
- `Video Evidence Audit — Tezeno 2026-03-15.docx`
- `Chain of Custody Audit — Nicholas 2026-03-20.docx`
- `DNA Audit Report — Cole 2026-05-10.docx`
- `Crime Lab Audit Report — Cole 2026-05-10.docx`

### Required Sections (all auditor reports must include)
1. **Executive Summary** — 2-3 paragraph overview of findings and significance
2. **Evidence Examined** — List of specific items audited with Bate stamp references
3. **Methodology** — What standards/protocols were applied (SWGDE, NIST, agency policy, etc.)
4. **Findings** — Detailed findings organized by severity: Critical, Significant, Minor, Informational
5. **Defense Implications** — How each finding affects the defense case
6. **Key Findings for Cross-Examination** — Bullet list of specific points that can be used to challenge evidence or impeach witnesses. Each point must include: the finding, the source reference (Bate stamp or document), and a suggested line of questioning.
7. **Recommendations** — Suggested next steps (motions to file, experts to retain, additional investigation)
8. **Case Brain Registration** — Skill name, output filename, date, location (per the Register Output with Case Brain protocol)

### Severity Definitions
- **Critical**: Evidence should be excluded or case outcome materially affected
- **Significant**: Weakens prosecution's case or supports defense theory
- **Minor**: Procedural deficiency that may not affect admissibility but can be raised
- **Informational**: Noted for completeness but unlikely to affect case

### Output Location
`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`
