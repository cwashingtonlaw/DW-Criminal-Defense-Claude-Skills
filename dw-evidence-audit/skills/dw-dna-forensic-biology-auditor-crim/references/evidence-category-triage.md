# DNA Evidence Category Triage

Read at STEP 2 of `dw-dna-forensic-biology-auditor-crim/SKILL.md` — the Evidence Category Matrix and Conspicuous Absence flag template moved verbatim from SKILL.md.

### Evidence Category Matrix

| Category | What It Is | Typical Issue | Audit Module(s) |
|---|---|---|---|
| **Single-source STR** | Clean profile from one contributor matched to a reference | Often the strongest DNA evidence — focus on contamination, chain of custody, activity-level inference | A, E |
| **2-person mixture** | DNA from two contributors interpreted to assign major/minor | Sub-threshold alleles, stochastic effects, contributor inference; LR computation | A, C, D |
| **3+ person complex mixture** | DNA from three or more contributors, often degraded | Interpretive limits — PCAST 2016 flagged complex mixtures as the highest-risk category; NOC uncertainty; black-box deconvolution | A, B, C, D |
| **Low-template / LCN DNA** | Sub-100 picogram inputs, increased PCR cycles or post-amp enhancement | Stochastic drop-out, drop-in, allele imbalance, replicate inconsistency — many labs and courts have rejected LCN | A, C, E |
| **Touch / transfer DNA** | DNA from skin cells deposited by contact | Secondary/tertiary transfer, persistence, shedder variability — activity-level propositions overreach | A, C, E |
| **Y-STR** | Y-chromosome-only profile (male lineage) | Haplotype frequency (not unique to individual), shared with paternal relatives, statistical limits | A, D |
| **Mitochondrial DNA (mtDNA)** | Maternal-line marker for degraded/hair-shaft samples | Heteroplasmy, haplogroup commonality, contamination from maternal relatives | A, D, E |
| **Kinship analysis** | Familial relationship calculations | Prior-probability assumptions, pedigree assumptions, software validation | B, D |
| **CODIS database hit** | A profile uploaded to CODIS produced a candidate match | Hit is investigative lead, not evidence — confirmation re-test required; database-search statistics differ from RMP | A, D, F |
| **Investigative Genetic Genealogy (IGG)** | SNP profile run against direct-to-consumer (GEDmatch, FamilyTreeDNA) databases to identify suspects via family trees | 4th Amendment scope, particularity, third-party doctrine; private-lab SNP methodology pre-*Daubert*/*Foret*; Brady on methodology | F |

### Conspicuous Absence Flags

When the charge type strongly implies DNA evidence should exist but does not appear in discovery, flag:

> **CONSPICUOUS ABSENCE — [Category]:** In a [charge type] case where the state alleges [touching / penetration / weapon use / etc.], [evidence type] would be standard investigative evidence. No [evidence type] appears in the discovery provided. This absence should be explored: was it obtained and not disclosed (*Brady* concern)? Was it not obtained (investigative deficiency — possibly favorable)? Was it obtained with unfavorable results to the prosecution (*Brady/Youngblood*)? Flag for Missing Discovery Demand + cross-examination of lead investigator.
