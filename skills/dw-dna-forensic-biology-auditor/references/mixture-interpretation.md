# Mixture Interpretation — Reference

Deep methodology reference for **Module C — Mixture Interpretation Audit**. Load when the case involves any DNA mixture (two or more contributors).

---

## 1. Mixture Categories

### 2-Person Mixtures
The most common and most reliably interpreted mixtures, especially when:
- The mixture has a clear major:minor ratio (e.g., 4:1 or greater).
- Template input is sufficient to detect both contributors at all loci.
- A reference profile (often the victim's) can be assumed/conditioned, allowing the analyst to "deduce" the second contributor.

**Audit focus:** Even 2-person mixtures can fail when the minor is near the stochastic threshold, when the ratio is closer to 1:1 making major/minor designation ambiguous, or when partial drop-out makes the minor's profile incomplete.

### 3-Person Mixtures
Substantially harder. Allele sharing between contributors creates ambiguity at many loci. Drop-out probability increases. SWGDAM 2017 and PCAST 2016 flagged 3-person mixtures as moderate-to-high risk, especially when:
- Template amount is below 250 pg total.
- Contributors are roughly equal in template contribution.
- Degradation is present.

### 4+ Person Mixtures (Complex Mixtures)
**Highest risk** — PCAST 2016 explicitly questioned the foundational validity of complex-mixture interpretation. Even with probabilistic genotyping software, the LR depends heavily on the NOC and prior assumptions. Many labs decline to interpret beyond 3 or 4 contributors, but some report LRs for 5+ person mixtures. **Strong Daubert/Foret challenge available** for these results.

---

## 2. Number of Contributors (NOC) Determination

NOC determination is the single most consequential interpretive decision in a mixture case.

### Methods

| Method | Description | Limitation |
|---|---|---|
| **Maximum allele count (MAC)** | Count the maximum number of alleles at any locus; divide by 2 (rounded up) | Underestimates NOC when contributors share alleles |
| **Total allele count (TAC)** | Sum alleles across loci with a threshold | Sensitive to drop-out at low template |
| **Allele count + peak-height ratio analysis** | Manual integration of all loci with PHR information | Highly analyst-dependent |
| **NOCit / similar software** | Probabilistic NOC estimator | Has documented error rate, especially for NOC ≥ 4 |
| **Default to most parsimonious** | Pick the lowest NOC consistent with observed alleles | Often a lab SOP rule; defense angle if the NOC was minimized to enable PG analysis |

### Uncertainty Quantification
- The analyst's NOC call is a point estimate; the true NOC is uncertain.
- Best practice (and SWGDAM 2017 recommendation): test alternative NOC values and report sensitivity.
- A robust report shows the LR computed at NOC=N and NOC=N+1; if the LR is comparable, the call is robust; if it changes by orders of magnitude, the conclusion is NOC-dependent.

**Audit:** Was NOC sensitivity tested? If not, that omission is a finding. Was the NOC call documented with rationale? Is the lab's SOP-mandated method actually applied?

---

## 3. Major / Minor Contributor Analysis

### Deduced vs. Inferred Profiles

- **Deduced profile** — the analyst subtracts a known reference profile (typically the victim's) from the mixture and reports the remaining profile attributable to the unknown contributor. Allowed under most lab SOPs when the reference is well-established and the minor profile is clear.
- **Inferred profile** — the analyst constructs a profile from the mixture without subtraction, designating likely alleles of the unknown contributor. More speculative; should be flagged in interpretation.

### Major / Minor Ratio
- Clear separation (e.g., major peaks 4× minor peak heights) supports straightforward deconvolution.
- Closer ratios (1:1 to 2:1) make major/minor designation ambiguous; analyst should consider all possible contributor pairings.

**Audit:** Did the lab deduce or infer? Was the reference profile well-established (not itself a partial profile)? Was the major/minor ratio sufficient to support the designation?

---

## 4. SWGDAM 2017 Mixture Interpretation Guidelines

The SWGDAM Interpretation Guidelines for Autosomal STR Typing (2017 update) is the U.S. operative standard for mixture interpretation. Key requirements:

1. **Validation must cover the mixture interpretation method** for the sample types and NOCs encountered in casework.
2. **NOC determination methodology documented** and applied consistently.
3. **Stochastic effects accounted for** — sub-threshold alleles, drop-out, drop-in must be addressed in the interpretation, not ignored.
4. **Major and minor contributors designated only when supported** by peak-height ratio analysis.
5. **Likelihood ratio is the preferred statistical framework** for mixtures with two or more contributors.
6. **Verbal scale (if used) must be documented in the lab's SOP** and applied consistently.
7. **Limits of interpretation** — the lab's SOP should specify when a mixture is **uninterpretable** (typically beyond a NOC or template floor). The analyst must apply that limit.

**Audit:** Was SWGDAM 2017 followed in every respect? Where did the lab's actual practice deviate? Was deviation justified or unjustified?

---

## 5. When the Lab Should Have Declined to Interpret

A mixture should be declared **uninterpretable** (or "inconclusive" / "not suitable for comparison") when:

- NOC exceeds the lab's internal validation range.
- Template amount is below the lab's lower validated input range.
- Degradation produces peak imbalance that cannot be resolved.
- Mixture ratio is so close to 1:1 that contributor designation is ambiguous and PG software does not yield interpretable LRs.
- Substantial drop-out across multiple loci.
- The reference profile required for deduction is itself partial or uncertain.

**Audit:** Was an uninterpretable call warranted but not made? Conversely, was an inconclusive call made and then later replaced with an interpretable call after the lab learned the suspect's identity (a "context bias" concern)? Compare draft to final reports.

---

## 6. Defense Challenges to Mixture Conclusions

### Foundational Daubert / Foret Challenge
- Argue the methodology has not been validated for the specific operating point of the case sample (e.g., 4-person low-template mixture).
- Argue the LR is sensitive to NOC and the NOC call itself is uncertain.
- Cite PCAST 2016 finding of validity gaps in complex-mixture interpretation.

### As-Applied Challenge
- Argue the lab deviated from its own SOP.
- Argue the analyst did not follow SWGDAM 2017.
- Argue alternative NOC, alternative propositions, or alternative reference assumptions produce materially different LRs.

### Cross-Examination Themes
- **Lock in NOC methodology** — what did the lab do to count contributors?
- **Sensitivity test absence** — why was alternative NOC not tested?
- **Operating point** — is this sample within the validated operating range?
- **Drop-out and stochastic effects** — were they accounted for or assumed away?
- **Verbal scale** — does the numerical LR support the words used?
- **Activity-level overreach** — does the lab's conclusion address how the DNA got there?

### Common Lab Failures
- Reporting LR for a complex mixture without acknowledging NOC uncertainty.
- Using a single amplification on a low-template mixture without replicate analysis.
- Treating drop-out as negligible when it is not.
- Applying the lab's standard mixture interpretation SOP to a sample outside its validated scope.
- Reporting a "major contributor" designation when the major:minor ratio does not support it.
- Failing to consider an alternative reference profile (e.g., a non-target relative of the defendant) in the LR denominator.

---

## 7. Audit Checklist — Mixture Interpretation

- [ ] NOC determination methodology documented
- [ ] NOC sensitivity test run (alternative NOC values)
- [ ] Mixture within lab's validated NOC and template range
- [ ] Major/minor ratio analysis documented
- [ ] Deduced vs. inferred profile correctly designated
- [ ] Reference profile used for deduction is complete and well-established
- [ ] Stochastic effects (drop-out, drop-in, sub-threshold) addressed
- [ ] SWGDAM 2017 followed
- [ ] Lab's mixture interpretation SOP followed
- [ ] Uninterpretable threshold considered and either met or applied
- [ ] LR reported with NOC and propositions explicit
- [ ] Verbal scale (if any) matches lab's documented mapping
- [ ] Activity-level claims not made beyond what the analysis supports
- [ ] Draft vs. final report compared for context-bias drift

---

*See also: `str-methodology.md` (thresholds, stutter, PHR), `probabilistic-genotyping.md` (STRmix/TrueAllele deconvolution), `statistical-challenges.md` (LR computation, theta).*
