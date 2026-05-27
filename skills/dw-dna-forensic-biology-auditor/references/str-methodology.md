# STR Methodology — Reference

Deep methodology reference for **Module A — STR Methodology Audit**. Load when the case involves any STR-based DNA evidence (essentially all autosomal DNA cases).

---

## 1. Validation Framework

### Governing Standards

- **SWGDAM Guidelines** (Scientific Working Group on DNA Analysis Methods) — the U.S. operative standards body for forensic DNA. Current relevant documents include the SWGDAM Validation Guidelines for DNA Analysis Methods, the Interpretation Guidelines for Autosomal STR Typing (updated 2017), and Y-STR / mtDNA guidelines.
- **ISFG (International Society for Forensic Genetics) DNA Commission Recommendations** — international standards on mixture interpretation, biostatistics, low-template work, and probabilistic genotyping. Frequently cited by defense and treated as persuasive.
- **NIST (National Institute of Standards and Technology)** — publishes Standard Reference Materials, validation studies, and the foundational scientific literature on STR analysis (e.g., Butler, *Forensic DNA Typing*).
- **PCAST 2016** — President's Council of Advisors on Science and Technology, *Report on Forensic Science in Criminal Courts*. Flagged complex DNA mixtures as a high-risk forensic discipline; identified validity gaps; recommended foundational and as-applied validation studies for any analytical method offered in court.
- **ANAB / ASCLD-LAB Accreditation Standards** — ISO/IEC 17025-based accreditation; defines lab quality requirements, internal validation expectations, proficiency testing cadence.

### The Validation Question — Has THIS Lab Validated THIS Kit for THIS Sample Type?

Validation is not a one-time event. Every lab must conduct **internal validation** of every kit and method before use, even if the developer has run a separate developer validation. Internal validation specifies the lab's analytical threshold, stochastic threshold, mixture interpretation policy, and statistical reporting framework.

Audit questions:
- Is the internal validation study for the kit used in this case (e.g., PowerPlex Fusion 6C, GlobalFiler, Identifiler Plus, Yfiler Plus, PowerPlex Y23) on file and produced in discovery?
- Was the sample type at issue (touch DNA from a porous surface, sexual-assault swab, bone, hair shaft) within the scope of the validation? Internal validation studies that used only optimal-condition samples may not cover degraded, low-template, or substrate-bound DNA.
- When was the most recent validation revalidation? Has the kit version, instrument, or interpretation software changed since the validation?

---

## 2. Analytical Threshold vs. Stochastic Threshold

This distinction is the technical core of STR audit work — most analysts will be cross-examined on it.

### Analytical Threshold (AT)

The minimum peak height (in RFU — relative fluorescence units) above which a peak is **called** as a true allele rather than baseline noise. Typical AT values range from 50 to 200 RFU depending on the kit, instrument, and lab. The AT must be set per the lab's internal validation; borrowing the developer's recommended AT without internal validation is a documentation failure.

**Audit:** What AT did the lab use? Was it set per validation? Are peaks just above the AT being reported as conclusive when their reliability is in question?

### Stochastic Threshold (ST)

The peak height above which the analyst can be confident that **both alleles of a heterozygous pair would be detected** if present. Below the ST, stochastic effects (random sampling during PCR amplification) can cause one allele to drop out, making a true heterozygote appear as a homozygote. Typical ST values range from 150 to 400 RFU.

**Why this matters for defense:** A profile with peaks below the ST cannot be reliably treated as a complete profile. If the State's analyst calls a "match" using data below the ST without acknowledging the stochastic limitations, the conclusion overstates the evidence. SWGDAM requires that stochastic effects be addressed in mixture interpretation.

**Audit:** Were any reported alleles below the lab's stochastic threshold? Did the analyst document why those alleles were nonetheless treated as conclusive? Did the lab's SOP authorize the call?

---

## 3. Stutter, Drop-In, Drop-Out, Peak-Height Ratio

### Stutter

PCR artifact — a peak typically one repeat unit shorter (n−4) than the true allele, caused by polymerase strand-slippage during amplification. Forward stutter (n+4) and double stutter (n−8) also occur but less commonly. Stutter ratios are kit-, locus-, and allele-specific. If a peak is at a stutter position relative to a larger peak, the analyst must determine whether it is stutter or a true minor-contributor allele.

**Audit:** Were stutter ratios documented per the kit's validation? Were any sub-threshold peaks at stutter positions called as minor-contributor alleles without justification?

### Allele Drop-Out

A true allele is present in the DNA template but fails to amplify above the analytical threshold. Most common in low-template DNA, degraded DNA, and minor contributors in mixtures.

### Allele Drop-In

A spurious allele appears in the profile from contamination — typically a single peak just above the AT. Distinguishing drop-in from a true minor-contributor allele is one of the hardest interpretive problems and a major source of mixture overinterpretation.

### Peak-Height Ratio (PHR) / Heterozygote Balance

For a heterozygous locus, the two alleles' peak heights should be approximately balanced. The PHR is the smaller peak divided by the larger peak. The lab's validation should define an expected minimum PHR (often 0.6 or 0.7 for high-template DNA). PHR below the threshold suggests stochastic effects, degradation, or the presence of a second contributor.

**Audit:** Were any heterozygous calls made with PHR below the lab's threshold without documentation? Were imbalanced peak pairs treated as single-contributor profiles when they may indicate a mixture?

---

## 4. Capillary Electrophoresis (CE) — How Data Goes From Sample to EPG

1. **Collection & Extraction** — biological sample collected (swab, fabric, etc.); DNA extracted using a chemistry such as DNA IQ, EZ1, Maxwell, or organic extraction.
2. **Quantification** — typically by qPCR (Quantifiler Trio, Plexor HY) measuring autosomal and male-specific DNA. Establishes the input DNA template amount and male:female ratio.
3. **Amplification (PCR)** — multiplex STR kit (PowerPlex Fusion, GlobalFiler, Identifiler Plus, Yfiler Plus, etc.) amplifies 20+ STR loci with fluorescent primers. Typical cycle count: 28–30 cycles for standard, increased for low-template.
4. **Capillary Electrophoresis** — amplified product injected into a CE instrument (ABI 3500, 3500xL, 3130xl). DNA fragments separated by size; fluorescent labels detected by laser.
5. **Data Collection & GeneMapper ID-X (or comparable) Analysis** — raw data converted to peaks, called against a size standard and allelic ladder. Outputs the electropherogram (EPG).
6. **Manual Review** — qualified analyst reviews each EPG, calls each peak, designates contributors, and applies the lab's interpretation SOP.

**Audit points at each step:**
- Quantification — was male:female ratio consistent with the case theory? Was the input quantity within the kit's validated range?
- Amplification — was cycle count standard? Any post-amp enhancement (e.g., increased injection time)? Replicate amplifications run?
- CE instrument — calibration current? Run conditions per SOP?
- GeneMapper review — manual edits documented? Edit history preserved?

---

## 5. EPG Interpretation — Reading the Electropherogram

The EPG is a series of colored peaks (one color per dye channel, corresponding to a set of STR loci) plotted against fragment size. Defense audit of an EPG looks for:

| Feature | What It Is | Audit Concern |
|---|---|---|
| **Peak height (RFU)** | Signal strength at each allele position | Compare to AT and ST; check for sub-threshold peaks called as alleles |
| **Off-ladder allele** | A peak not at a position defined in the allelic ladder | May indicate a rare microvariant, a sequence variant, or an artifact; should be documented and resolved |
| **Pull-up** | Bleed-through of a peak in one dye channel into the spectrum of another dye channel | Should be flagged and not called as a true allele in the other channel |
| **Dye blob** | Free-dye artifact appearing as a broad peak | Should be excluded from interpretation |
| **Spike** | Single-channel sharp peak, often from a current spike or air bubble | Should be excluded |
| **−A / +A artifacts** | Incomplete adenylation by polymerase | Affects peak shape and may complicate calls |
| **Stutter peaks** | n−4 (back stutter), n+4 (forward stutter), n−8 (double stutter) | Distinguish from true minor-contributor alleles |
| **Plus-shift** | Stutter or off-ladder migration anomaly | Documented and explained |
| **Disequilibrium** | Imbalanced peak heights at a heterozygous locus | May indicate stochastic effects or mixture |

**Audit demand:** Request the raw `.fsa` or `.hid` files, not just the printed EPG image. The raw files preserve the underlying data; printed images may have been cropped or rescaled. The analyst's GeneMapper edit history (deleted peaks, manually added peaks, threshold overrides) is typically available within the project file and is Brady material.

---

## 6. Common Methodology Challenges

### Improper Threshold Application
- AT/ST not validated for the kit or sample type used.
- AT/ST applied inconsistently between samples in the same batch.
- Sub-threshold peaks reported as conclusive alleles without explicit justification.

### Inadequate Replicate Analysis
- Low-template samples should be amplified in replicate (typically 2–3 amplifications) to identify which alleles are reproducible and which are stochastic artifacts. Single-amplification low-template work is widely criticized.

### Failure to Document Interpretive Choices
- Manual peak edits not logged.
- NOC (number of contributors) call not documented with rationale.
- Allele designations changed between draft and final report without explanation.

### Software-Only Allele Calls
- Some labs allow GeneMapper or similar software to call alleles without independent analyst confirmation. Best practice is independent dual analyst review.

### Kit-Specific Issues
- **PowerPlex Fusion 6C** — 24-locus multiplex with 6 dye channels; high information content but stutter behavior varies by locus.
- **GlobalFiler** — 24-locus including DYS391; analyst must understand DYS391 behavior in female samples.
- **Identifiler Plus** — older 16-locus kit still used in legacy cases; lower information content.
- **Yfiler Plus** — 27 Y-STR loci; rapidly mutating loci (RM Y-STRs) introduce complexity.

### Validation Scope Mismatches
- The internal validation used clean, full-template, single-source samples. The case sample is a degraded touch-DNA swab from a complex substrate. The lab applied the same thresholds — but validation does not cover the operating regime.

### Off-Ladder Alleles
- Microvariants and sequence variants — designated as e.g., "9.3" — must be confirmed by an allelic ladder match or independent confirmation. Off-ladder alleles in mixtures dramatically complicate interpretation.

---

## 7. Audit Checklist — STR Methodology

- [ ] Lab's internal validation for the kit used produced in discovery
- [ ] Internal validation covers the sample type (touch, degraded, low-template, mixture, substrate-bound) at issue
- [ ] Analytical threshold set per validation
- [ ] Stochastic threshold set per validation
- [ ] No reported alleles below the stochastic threshold without explicit justification
- [ ] Peak-height ratios within the lab's threshold for all heterozygous calls
- [ ] Stutter, pull-up, dye blob, spike, and adenylation artifacts documented and excluded
- [ ] Off-ladder alleles confirmed by ladder or independent run
- [ ] Replicate amplifications run for low-template samples
- [ ] GeneMapper edit history preserved and produced
- [ ] Raw `.fsa` / `.hid` files preserved and produced (not just printed EPGs)
- [ ] Dual analyst review documented
- [ ] Reference samples from defendant, victim, known elimination samples processed in separate batches
- [ ] Reagent blanks, amplification negatives, and positive controls run with the case batch and within specification

---

*See also: `mixture-interpretation.md` (NOC, deconvolution), `probabilistic-genotyping.md` (STRmix/TrueAllele specific), `contamination-and-handling.md` (controls and chain).*
