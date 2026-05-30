# Statistical Challenges — Reference

Deep methodology reference for **Module D — Statistical Challenges**. Load whenever the State reports any DNA statistic (RMP, CPI, LR, kinship index).

---

## 1. Random Match Probability (RMP) vs. Likelihood Ratio (LR)

### RMP
The probability that a randomly selected, unrelated individual from a reference population would have the same DNA profile as the evidence sample. Computed by multiplying allele frequencies across loci (with theta and zygosity corrections).

- **Use case:** Single-source profiles and clear major-contributor profiles from mixtures.
- **Report format:** "The probability of selecting an unrelated individual at random with this profile is 1 in 1 quintillion."
- **Limitation:** Does not address mixtures with shared alleles or partial profiles cleanly. Inappropriate as the primary statistic for complex mixtures.

### Combined Probability of Inclusion (CPI / CPE)
The probability that a randomly selected individual would be **included** in (not excluded from) the mixture as a potential contributor.

- **Use case:** Older approach for mixtures; has been criticized by SWGDAM and ISFG as inferior to LR for mixtures because it discards information.
- **Audit angle:** A lab using CPI rather than LR for a complex mixture is using a less informative statistic; results may be less probative (or, depending on the case theory, less prejudicial) than an LR would produce.

### Likelihood Ratio (LR)
The ratio of the probability of the evidence under two competing hypotheses (e.g., H1: defendant is a contributor; H2: defendant is not, an unrelated person is).

- **Use case:** Preferred for mixtures under SWGDAM 2017 and ISFG.
- **Limitation:** Highly conditional on the propositions specified, NOC, prior assumptions, and software parameters.
- **Misinterpretation risk:** Prosecutor's fallacy — treating the LR as P(innocence) inverts the statistic. Defender's fallacy is the converse error.

**Audit:** Which statistic did the lab use? Was it appropriate for the evidence type? Did the analyst or prosecutor commit the prosecutor's fallacy in characterization (oral testimony, closing argument)?

---

## 2. Database Substructure and Allele Frequency Assumptions

### Population Databases
Allele frequencies are derived from population reference databases. Common U.S. databases include:
- NIST 1036 Caucasian / African American / Hispanic
- FBI population databases (caucasian, African American, southeastern Hispanic, southwestern Hispanic, Native American)
- Manufacturer-supplied databases (PowerPlex, GlobalFiler)

The choice of database materially affects the RMP and LR for any defendant. Best practice is to compute statistics in **all relevant populations** and report the most conservative value.

**Audit:**
- Which database(s) were used?
- Was the most conservative reported, or was a single (potentially less conservative) population selected?
- Is the population database appropriate for the defendant's actual ancestry, particularly for Native American defendants where regional substructure can be substantial?

### Sample Size of the Database
Smaller reference databases produce less stable allele-frequency estimates, particularly for rare alleles. Database sample sizes of 200+ are typical; some legacy databases are smaller. Rare alleles may receive minimum-frequency corrections (typically 5/(2N) where N is the database size).

---

## 3. Theta Correction (FST)

### What Theta Is
Theta (also written F<sub>ST</sub>) is a correction factor accounting for population substructure — the fact that real populations are not panmictic, and individuals from the same subpopulation share more alleles by descent than truly random individuals.

### Typical Values
- Standard theta values applied in forensic statistics: **0.01 to 0.03**.
- NRC II (1996) recommended 0.01 for most populations and 0.03 for small isolated subpopulations.
- FBI guidance: typically 0.01 for general use; 0.03 may be applied for Native American populations or small endogamous communities.

### Effect on the Statistic
- Higher theta → more conservative (smaller) statistic. RMP increases (less rare); LR decreases (less probative).
- Theta = 0 → ignores substructure entirely; produces aggressive statistics inappropriate for substructured populations.

**Audit:**
- What theta was used?
- Was the value appropriate for the defendant's population?
- Was theta = 0.01 used for a defendant from a substructured population where 0.03 was warranted?

---

## 4. FBI vs. SWGDAM Standards

### FBI Quality Assurance Standards (QAS)
The FBI promulgates QAS for DNA labs that participate in CODIS. QAS requires:
- Validation studies
- Proficiency testing (semiannually)
- Casework review
- Statistical reporting standards
- Audit cycles

### SWGDAM
SWGDAM publishes interpretation and validation guidelines that are consensus standards rather than regulatory requirements. SWGDAM 2017 (Interpretation Guidelines for Autosomal STR Typing) is the operative interpretation standard.

### NRC I (1992) and NRC II (1996)
National Research Council reports on forensic DNA. NRC II remains influential on statistical framework (theta, population databases). Some labs still apply NRC II-derived formulas.

**Audit:** Are the lab's statistical methods consistent with current QAS, SWGDAM, and ISFG recommendations? Or is the lab still applying legacy NRC I/II calculations that have been superseded?

---

## 5. Convergence of LR Values

When the same mixture is run through multiple PG systems (STRmix vs. TrueAllele vs. EuroForMix), the LRs are not always close. The lab community has reported cases where two systems give LRs differing by orders of magnitude on the same sample.

### Why This Matters
- Convergence across systems is a measure of methodological robustness.
- Lack of convergence indicates that the LR is sensitive to modeling assumptions specific to one system.
- Many courts and commentators have requested cross-validation studies; few labs perform them in casework.

**Audit:** Was the mixture run on more than one system? If yes, what was the cross-system LR comparison? If no, has the lab considered or rejected cross-validation?

---

## 6. Statistical Overstatement — How Weak Evidence Is Inflated

Several mechanisms inflate the apparent strength of weak DNA evidence:

### Reporting Practices That Inflate Strength
- **Selecting the most favorable population** — choosing the database that produces the largest LR rather than the most conservative.
- **Using theta = 0 or 0.01 when 0.03 was appropriate** — produces aggressive statistics.
- **Reporting the highest-stratum verbal label** when the LR is near the lower end of the range.
- **Aggregating across loci** without acknowledging dependence — if multiple loci share information, multiplying frequencies overstates.
- **Ignoring drop-out probability** — pretending the analyst saw the full profile when partial drop-out reduces evidentiary value.
- **Reporting "match" instead of LR** — the language "match" implies certainty that the LR does not justify.

### Activity-Level Overstatement
- Reporting an LR for sub-source ("DNA from this person") but then characterizing the evidence at activity level ("the defendant touched the gun"). The LR does not support the activity-level inference.

### Cross-Examination Themes
- Establish the propositions H1 and H2 explicitly.
- Establish what the LR does and does not say.
- Establish that "match" is not a synonym for "the only person who could have left this DNA."
- Establish theta and population database selection sensitivity.

---

## 7. Verbal Scale for LR

| LR | Verbal Label (SWGDAM 2018 example) |
|---|---|
| 1 – 10 | Limited support |
| 10 – 100 | Moderate support |
| 100 – 1,000 | Moderately strong support |
| 1,000 – 10,000 | Strong support |
| 10,000 – 1,000,000 | Very strong support |
| > 1,000,000 | Extremely strong support |

### Where Verbal Scales Mislead
- Different labs use different mappings — comparing across labs is misleading.
- Verbal scales suggest a continuous calibration that the underlying math does not justify.
- "Extremely strong support" sounds like certainty but is a label for a numerical range.
- Juries may not understand that "very strong support for H1 vs. H2" is conditional on the specified hypotheses.

### Defense Approach
- Motion in limine to exclude verbal scale and require the analyst to report the numerical LR with explicit propositions.
- Cross-examination establishing the verbal scale is a translation, not a measurement.

---

## 8. Population Genetics Pitfalls

### Defendant's Ancestry
- Mixed ancestry defendants may not fit cleanly into any single reference population.
- Native American defendants — substantial substructure within and across tribes; standard databases may not be representative.
- Recent-immigrant defendants — the U.S. reference databases may not represent the relevant population.

### Relatives
- The standard LR denominator assumes an "unrelated alternate contributor." If the defendant has a close relative who could be the source, the LR should be computed with the relative as the alternate hypothesis — typically reducing the LR by orders of magnitude (especially for siblings).

**Audit:** Was the possibility of a close relative as the alternate hypothesis considered? Was an LR computed for the relative case?

---

## 9. Audit Checklist — Statistical Challenges

- [ ] Statistical framework identified (RMP / CPI / LR)
- [ ] Framework appropriate for the evidence type
- [ ] Population databases identified
- [ ] Most conservative statistic reported (or justification for selection)
- [ ] Theta value documented and appropriate for defendant's population
- [ ] Minimum allele frequency correction applied for rare alleles
- [ ] Independence assumptions (loci-level) addressed
- [ ] Relative-as-alternative hypothesis considered if applicable
- [ ] Verbal scale (if used) matches lab's documented mapping
- [ ] Cross-system comparison (STRmix vs. TrueAllele) considered if available
- [ ] No prosecutor's-fallacy language in lab report or oral testimony
- [ ] Activity-level claims not made beyond sub-source LR
- [ ] Statistical computation documented step-by-step (auditable)

---

*See also: `probabilistic-genotyping.md` (LR computation by software), `mixture-interpretation.md` (LR for mixtures), `louisiana-dna-case-law.md` (legal standards).*
