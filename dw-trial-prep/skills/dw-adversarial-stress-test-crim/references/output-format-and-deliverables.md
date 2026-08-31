# Output Format — Deliverables and Case Brain Update

Read at **Step 3** — filenames and section-by-section contents of the primary report, the Top 5 executive summary, and the Case Brain update.

---

### Primary deliverable: Adversarial Stress Test Report (.docx)

Filename: `Adversarial_Stress_Test_{{DEFENDANT_LAST}}_{{DOCKET}}_{{YYYY-MM-DD}}.docx`

Contents:
1. Header -- work-product marking, defendant, docket, parish/court, date, attorney.
2. Executive Summary -- one-page "Top 5 Vulnerabilities" with risk ratings, evidence citations, and recommended actions. Designed for quick attorney review before diving into the full report.
3. Section 1 -- Theory Under Test (from Report 4a: selected theory, supporting evidence, theme).
4. Section 2 -- Theory Vulnerability Scan (Module A: top 10 weaknesses ranked by severity).
5. Section 3 -- Prosecution Cross-Examination Simulation (Module B: per-witness cross questions).
6. Section 4 -- Prosecution Closing Argument Preview (Module C: full draft closing).
7. Section 5 -- Rebuttal Evidence Identification (Module D: rebuttal evidence inventory).
8. Section 6 -- Defense Counter-Response Matrix (Module E: attack-by-attack response plan).
9. Section 7 -- Jury Perception Risk Assessment (Module F: risk ratings with rationale).
10. Section 8 -- Priority Preparation Checklist (Module G: ranked action items with skill routing).
11. Source-citation appendix -- every factual claim mapped to its discovery citation.

### Secondary deliverable: Top 5 Vulnerabilities Executive Summary (.docx)

Filename: `Stress_Test_Top_5_{{DEFENDANT_LAST}}_{{DOCKET}}_{{YYYY-MM-DD}}.docx`

A standalone one-page document for quick attorney review. Contains:
- The 5 highest-risk vulnerabilities from the full report.
- For each: the attack, the evidence the prosecution would use, the defense counter-response, the jury risk rating, and the single most important preparation action.
- A footer noting: *"Full Adversarial Stress Test Report available -- see [filename]."*

### Case Brain update

After generating the report, update `dw-case-brain-crim` with:
- Stress test completion date.
- Top 5 vulnerability summary (for quick-reference on case reload).
- Cross-skill routing tasks generated.
- Flag: `STRESS_TEST_CURRENT` = `true` (set to `false` when new evidence arrives or theory shifts -- see Re-Run Protocol below).
