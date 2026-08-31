# Contract 3C: DNA / Forensic Biology Audit Report — Full Schema

Read from the SKILL.md **Contract 3C: DNA / Forensic Biology Audit Report** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producer:** `dw-dna-forensic-biology-auditor-crim`
**Consumers:** `dw-cross-exam-architect-crim`, `dw-trial-notebook-builder-crim`, `dw-expert-witness-evaluator-crim`, `dw-brady-giglio-auditor-crim`, `dw-case-brain-crim`

### Filename Pattern

`DNA Forensic Biology Audit — [Client Last Name] [Date].docx`

### Required Sections

Inherits the Contract 2 (Auditor Skill Reports) structure (Executive Summary, Evidence Examined, Methodology, Findings, Defense Implications, Key Findings for Cross-Examination, Recommendations, Case Brain Registration), with these DNA-specific additions:

1. **Evidence Inventory** — Per-item table: item number, source (swab/cutting/reference), collection date, collector, lab item number
2. **Testing Methodology Audit** — Extraction method, quantification platform, amplification kit (Identifiler/Fusion/GlobalFiler), capillary electrophoresis instrument, allele-calling thresholds
3. **Mixture Interpretation** — Number of contributors, deconvolution method, probabilistic genotyping software (STRmix / TrueAllele / EuroForMix), version, validation status, parameter set used
4. **Statistical Calculations** — Likelihood ratio or RMP, propositions tested, reference population database used, sub-population correction (theta)
5. **CODIS / Database Hit Audit** — If applicable: hit confirmation, moderate/high stringency, candidate match procedure
6. **Standards Compliance Check** — SWGDAM, ISO/IEC 17025, lab accreditation body (ANAB / A2LA), validation studies
7. **Chain of Custody Cross-Reference** — Cross-reference to `dw-chain-of-custody-auditor-crim` findings for the same items
8. **Analyst Credentials & Discipline History** — Cross-reference to `dw-expert-witness-evaluator-crim`
9. **Cross-Examination Seeds** — Mixture interpretation challenges, stochastic threshold issues, drop-in / drop-out assumptions, contamination indicators

### Output Location

`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`
