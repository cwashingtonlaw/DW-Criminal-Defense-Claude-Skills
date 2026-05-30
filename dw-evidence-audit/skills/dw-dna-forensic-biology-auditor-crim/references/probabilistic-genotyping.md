# Probabilistic Genotyping — Reference

Deep methodology reference for **Module B — Probabilistic Genotyping Audit**. Load when the case involves STRmix, TrueAllele, EuroForMix, LRmix Studio, DNA-VIEW, FST, or any other probabilistic interpretation software.

---

## 1. STRmix vs. TrueAllele — The Two Dominant Systems

### STRmix

- **Developer:** Institute of Environmental Science and Research (ESR, New Zealand); distributed by NicheVision.
- **Methodology:** Continuous probabilistic genotyping. Uses a Markov chain Monte Carlo (MCMC) simulation to generate weighted genotype combinations for each contributor in a mixture, accounting for peak heights, stutter, drop-out, and drop-in.
- **Input:** EPG peak heights (continuous data — not just allele calls).
- **Output:** A likelihood ratio (LR) comparing two hypotheses, weighted genotype combinations per contributor.
- **Validation literature:** Developer validations published by ESR; numerous lab-internal validations; SWGDAM-compliant.
- **Adoption:** Widely deployed in U.S. crime labs, including FBI, NYPD, many state labs.

### TrueAllele

- **Developer:** Cybergenetics (Mark Perlin); distributed by Cybergenetics.
- **Methodology:** Continuous probabilistic genotyping. Uses a different MCMC framework with somewhat different assumptions and a longer compute cycle. Cybergenetics maintains tighter control over its system than ESR does over STRmix.
- **Input:** EPG peak heights (continuous data).
- **Output:** LR per contributor versus alternative.
- **Adoption:** Used by some labs (e.g., NYC OCME historically; New Mexico DPS; private contracts); less commonly deployed than STRmix.
- **Source-code access:** Cybergenetics has aggressively contested source-code disclosure in litigation (see Section 4 below).

### Continuous vs. Semi-Continuous

- **Continuous** — uses full quantitative peak-height information (STRmix, TrueAllele, EuroForMix).
- **Semi-continuous** (also called "qualitative") — uses only allele presence/absence and drop-out/drop-in probabilities (LRmix Studio, LR mix); does not use peak heights. Generally produces more conservative LRs than continuous systems but loses information.

### Other Systems
- **EuroForMix** — open-source continuous PG (Norway); free; less commonly used in U.S. courts.
- **LRmix Studio** — open-source semi-continuous; used internationally; less common in U.S.
- **DNA·VIEW Mixture Solution** — older semi-continuous tool (Charles Brenner); legacy use.
- **FST (Forensic Statistical Tool)** — proprietary OCME tool used in NYC; discontinued; key in *NY v. Hillary* litigation.

---

## 2. Validation Literature & Gaps

### Developer Validation vs. Internal Validation
- Developer validation establishes the software performs as designed across a range of conditions. Internal validation establishes that **this lab, with this analyst training, on this instrumentation, with this kit, can deploy the software within a defined operating range.**
- A lab cannot rely on developer validation alone — internal validation is mandatory under SWGDAM and ANAB.

### Known Validation Gaps Defense Should Probe
- **High contributor counts** — most labs validate to 3 or 4 contributors. A 5-person mixture interpreted by STRmix or TrueAllele may be outside the lab's internal validation range.
- **Very low template inputs** — internal validations often use 50 pg minimum; samples below that operating range produce unreliable LRs.
- **Highly degraded samples** — degradation creates differential peak heights across loci that PG software may misinterpret as contributor structure.
- **Highly imbalanced mixtures** — e.g., 1:1000 ratio; the minor contributor may be near or below the noise floor.
- **Substrate / sample type** — touch DNA from porous surfaces was rarely included in early validations.
- **Inhibition** — co-extracted inhibitors that suppress some loci more than others can be misinterpreted as contributor structure.

### Black-Box Study Problem
PCAST 2016 highlighted that probabilistic genotyping systems should be evaluated through **black-box studies** — large-scale empirical tests where the system is challenged with samples of known composition and the error rate measured against the truth. STRmix and TrueAllele have published some such studies, but PCAST and subsequent commentary have noted that these studies often used favorable sample sets (high template, low contributor count, well-balanced) that do not represent the operating regime in casework. The defense should demand:
- The specific empirical foundation for the system's reliability **at the operating point of the case sample** (NOC, template amount, degradation level, mixture ratio).
- The error rate associated with that operating point.

---

## 3. Deconvolution Assumptions

### Number of Contributors (NOC)
- The analyst (or in some workflows, the software) selects the NOC before running the PG analysis. NOC is a **prior** that materially affects the LR — running the same mixture as 3-person vs. 4-person can yield order-of-magnitude differences.
- NOC determination is methodologically contested. Methods range from "manual review of allele count and balance" to software-based NOC estimators (e.g., NOCit). All have error rates, especially at higher contributor counts.

**Audit:** What NOC was called? What methodology was used to call it? Did the analyst run the PG analysis at alternative NOC values to test sensitivity? Did the SOP authorize the call?

### Prior Probability of Contributor Presence
- The LR's numerator hypothesis ("the suspect is a contributor") is conditional on the suspect being in the mixture. In many cases this is a non-controversial proposition, but in others — particularly touch-DNA cases with potential secondary transfer — the assumption itself is contestable.
- Bayesian framework: the LR updates a prior probability. A high LR with a low prior yields a low posterior. Juries are not typically instructed on this.

### Propositions Tested — Sub-Source vs. Sub-Sub-Source vs. Activity-Level
- **Sub-source proposition** — "the defendant is/is not a contributor to this DNA mixture." Standard PG output.
- **Sub-sub-source proposition** — refines to specific contributor designation (e.g., "the defendant is the major contributor" vs. "a minor contributor").
- **Activity-level proposition** — "the defendant deposited this DNA by [touching the weapon] vs. [secondary transfer]." Activity-level inference is methodologically much harder and rarely supported by PG software output alone. STRmix and TrueAllele do not generate activity-level LRs without additional input (transfer/persistence studies). Activity-level claims by the prosecution should be flagged as exceeding the methodology.

**Audit:** What propositions did the lab actually evaluate? Does the prosecution's claim at trial match the propositions, or does it overreach into activity-level inference unsupported by the analysis?

---

## 4. Source-Code Access Litigation

Defense access to the source code of probabilistic genotyping software has been litigated extensively since approximately 2015.

### Key Cases
- ***People v. Chubbs***, No. B258569 (Cal. Ct. App. 2015) — early TrueAllele source-code dispute; Cybergenetics resisted production; case resolved on other grounds.
- ***New York v. Hillary*** — STRmix source code was disclosed under protective order in this murder case; defense experts identified coding errors that affected LRs in casework. The Hillary disclosure produced the well-known "MiniFiler bug" that ESR subsequently disclosed.
- **Pennsylvania, New Jersey, Michigan source-code litigation** — ongoing line of cases on PG source access.
- **STRmix MiniFiler bug** — ESR self-disclosed a coding error that affected LRs for some MiniFiler-kit mixture analyses; produced under court order in casework. Provides direct precedent that source-code review reveals errors.

### Daubert / Brady / Confrontation Arguments for Disclosure
- **Daubert reliability prong** — the methodology cannot be "tested" by the defense if the source code is unavailable. Without inspection, the defense cannot evaluate whether the published validation reflects the actual implemented algorithm.
- **Brady v. Maryland** — coding errors are exculpatory if they affect the LR in the defendant's case. The State has a duty to disclose; if the State does not have the code, the State must use its discovery process to obtain it from the developer.
- **Confrontation Clause (Crawford / Melendez-Diaz / Bullcoming)** — the software's output is a testimonial statement; defendant has a right to confront the methodology, which requires the ability to inspect.
- **Protective order is the standard remedy** — most courts that have ordered disclosure have done so under a protective order limiting use to defense experts.

### Defense Practice
- File motion to compel source code with offer of protective order.
- Identify a defense expert who can perform source-code review (limited pool — see `defense-dna-experts.md`).
- Even where source-code disclosure is denied, the motion preserves the issue for appeal and may pressure the State to concede on related issues (raw data, validation studies).

---

## 5. Likelihood Ratio Output — How to Read It and What It Doesn't Say

### What the LR Is
The LR is a ratio:

> LR = Pr(evidence | H1) / Pr(evidence | H2)

Where H1 = "suspect is a contributor" and H2 = "suspect is not a contributor; instead, an unrelated person from the population is." An LR of 1 billion means the evidence is 1 billion times more likely under H1 than under H2.

### What the LR Does NOT Say
- **The LR is not the probability of guilt.** Translating an LR to "the probability the defendant is the source" requires multiplying by a prior — which the LR does not provide.
- **The LR depends on the propositions specified.** Change H2 (e.g., "a sibling" instead of "an unrelated person") and the LR changes — often dramatically.
- **The LR is conditional on NOC.** Different NOC, different LR.
- **The LR does not address activity-level claims.** "How did the DNA get there" is not what the LR answers.
- **Prosecutor's fallacy** — treating the LR as the probability of innocence. Routinely committed in argument and even in expert testimony.

### Verbal Scale Translation
Many labs translate the numerical LR into a verbal label:

| LR Range | Verbal Scale (typical) |
|---|---|
| 1 – 10 | Weak / Limited support |
| 10 – 100 | Moderate support |
| 100 – 1,000 | Strong support |
| 1,000 – 1,000,000 | Very strong support |
| > 1,000,000 | Extremely strong support |

**Defense challenge:** Verbal scales are linguistic translations of mathematical values. They are not part of the underlying calculation. The exact mapping varies across labs and across publications (SWGDAM 2018 guidance vs. ENFSI vs. lab-specific). "Extremely strong support" for a particular numerical range in one lab may map to "Very strong support" in another. Argue that the verbal label exceeds what the numerical value supports, or that the verbal scale itself is misleading and the jury should be presented the LR directly.

---

## 6. Notable Defense Wins on Probabilistic Genotyping

- ***NY v. Hillary*** — STRmix source-code disclosure under protective order; subsequent disclosure of MiniFiler bug.
- ***Texas v. Sims*** — DPS Lab withdrew probabilistic genotyping results after internal review found systemic interpretation issues; cases statewide reviewed and re-tested.
- ***Texas DPS contamination crisis (2016–2019)*** — multiple cases reopened after lab admitted protocol deviations.
- ***Australia v. R v. Tuite*** — STRmix LR challenged at trial; appellate review.
- **State-court rulings excluding probabilistic genotyping** in specific cases on Daubert grounds where the operating point was outside validation range.

Defense should monitor *NACDL DNA Resource Center* updates and the National Registry of Exonerations for current cases.

---

## 7. Audit Checklist — Probabilistic Genotyping

- [ ] Software identified (system, version, build)
- [ ] Internal validation study for this software version produced
- [ ] Internal validation covers the operating point of the case sample (NOC, template amount, mixture ratio, degradation, sample type)
- [ ] NOC determination methodology documented; NOC sensitivity test run
- [ ] All propositions tested are documented; no activity-level overreach
- [ ] Reference profiles run through the same software; LR computed for each
- [ ] MCMC convergence diagnostics documented (chain length, convergence statistics)
- [ ] Software's known bug list reviewed against the run version
- [ ] Verbal scale (if used) matches the lab's documented mapping
- [ ] Source code access motion considered; protective order proposed
- [ ] Defense expert engaged to review STRmix/TrueAllele run files

---

*See also: `mixture-interpretation.md` (NOC and SWGDAM 2017), `statistical-challenges.md` (LR vs. RMP, theta, verbal scale), `defense-dna-experts.md` (sourcing PG critics).*
