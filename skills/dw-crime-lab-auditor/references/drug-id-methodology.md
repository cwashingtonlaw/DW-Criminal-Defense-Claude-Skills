# Drug Identification Methodology

This reference is loaded by `dw-crime-lab-auditor` Module A. It addresses the chemistry of controlled-substance identification — presumptive screening, confirmatory analysis, instrumental methods, bulk sampling, and the legal standards (Daubert/Foret) for sufficiency of identification.

---

## 1. The Two-Test Rule

The cornerstone of defensible drug ID. At least one **presumptive** test (which narrows the analyte to a chemical class) plus at least one **confirmatory** test (which identifies the specific molecule).

- **Presumptive tests alone are not sufficient** to identify a controlled substance for purposes of proving the substance element of a charge. They generate false positives; they identify the chemical *class* (e.g., "indicates a cocaine alkaloid") but not the specific substance.
- **Confirmatory tests** must satisfy *Daubert*/*Foret* — reliable methodology, validated, peer-reviewed where applicable, with a known error rate.
- The two-test rule is reflected in **SWGDRUG** (Scientific Working Group for the Analysis of Seized Drugs) recommendations and is the de facto standard for accredited labs.

**SWGDRUG Category A/B/C scheme (current version — VERIFY current revision):**
- **Category A (high discrimination):** mass spectrometry (MS), IR spectroscopy (FTIR), nuclear magnetic resonance (NMR), Raman spectroscopy
- **Category B (moderate discrimination):** capillary electrophoresis, gas chromatography (GC), liquid chromatography (LC), microcrystal tests, pharmaceutical identifiers, thin-layer chromatography (TLC)
- **Category C (low discrimination):** color tests, fluorescence, immunoassay, melting point, UV spectroscopy

**Identification requires either:**
- One Category A test plus a second technique from any category, OR
- A combination from Categories B and C totaling the discriminating power specified by SWGDRUG

If the lab report describes only Category C tests (e.g., Marquis color test) for a Schedule II identification, that is a **CRITICAL audit finding**.

---

## 2. Presumptive (Color / Spot) Tests

Color tests rely on chromogenic reactions between the suspected drug and a reagent. They are fast, cheap, and field-deployable — and they have well-documented false-positive rates.

| Test | Target Class | Common False Positives |
|---|---|---|
| **Marquis** (formaldehyde + sulfuric acid) | Opiates, amphetamines, MDMA, MDA | OTC decongestants; some prescription analgesics; nutmeg oils |
| **Mecke** (selenious acid + sulfuric acid) | Opiates | Various alkaloids |
| **Mandelin** (ammonium vanadate + sulfuric acid) | Amphetamines, ketamine | Many alkaloids; some food dyes |
| **Scott (cobalt thiocyanate)** | Cocaine | Diphenhydramine (Benadryl); some cleaning products; lidocaine and other "caine" anesthetics |
| **Duquenois-Levine** | THC / marijuana | CBD; coffee, oregano, sage, patchouli, mate, nutmeg, some hemp products |
| **Ehrlich's reagent** | Indoles (LSD, psilocybin) | Tryptamine-containing plants |
| **Simon's reagent** | Secondary amines (meth) | Various amines |

**Defense audit points:**
- Was the test performed in the field by a non-analyst (officer with field kit), in the lab as part of a workflow, or both?
- Field tests are presumptive only and inadmissible standing alone for the substance element. They support probable cause but not proof beyond reasonable doubt.
- Cross-reactivity is well-documented; demand the analyst concede the cross-reactant list for any color test relied upon.
- The Scott test (cocaine) yields a positive for diphenhydramine (Benadryl) — a fact every State chemist knows but rarely volunteers.

---

## 3. Microcrystalline Tests

A presumptive-to-confirmatory bridge: the analyte is precipitated as a characteristic crystal and examined under a polarizing microscope. The crystal habit (shape) is compared to reference photomicrographs.

- Strengths: minimal sample required; specific crystal habits for some substances (e.g., cocaine + platinic chloride yields characteristic dendritic crystals)
- Weaknesses: requires extensive analyst experience; subjective; reproducibility depends on conditions; no quantitation
- Category B under SWGDRUG — alone, not sufficient for ID

---

## 4. GC/MS — Gas Chromatography / Mass Spectrometry

**The gold standard for drug ID.** GC separates components in a mixture by volatility; MS fragments each component and produces a mass-to-charge spectrum that functions as a chemical fingerprint.

### What a defensible GC/MS analysis should show
- **Chromatogram** — the trace showing peaks for each component, with retention times
- **Mass spectrum** for each peak of interest — molecular ion (M+), characteristic fragment ions, intensity ratios
- **Library match** against a reference spectrum (NIST, SWGDRUG, in-house library) with a match score (typically reported as a percentage or a quality factor)
- **Analyst-confirmed identification** — the analyst manually compares the unknown spectrum to the reference and signs off, not just a library hit

### GC/MS audit points
- [ ] Was a confirmatory GC/MS run performed, or only a screening run?
- [ ] What was the library match score for the reported substance? (Scores below ~80-85% on a 100-point scale should be challenged)
- [ ] Was the analyst's manual confirmation documented, or was the library hit accepted automatically?
- [ ] Were internal standards (typically deuterated analogues — e.g., cocaine-d3 for cocaine) used? Internal standards control for injection volume and retention-time drift.
- [ ] Was the run performed within calibration period? Was a system-suitability check performed at the start of the batch?
- [ ] **Co-elution risk:** were any other peaks present near the analyte's retention time that could indicate a co-eluting interferent?
- [ ] Was the chromatogram **clean** — single sharp peak — or were there shoulders, tailing, or unresolved peaks?
- [ ] Was the **blank** chromatogram clean? Carry-over from a prior high-concentration sample can produce false positives.
- [ ] Were positive and negative control samples run with the batch?

### Common defense challenges to GC/MS work
1. **No analyst review of raw data** — the lab issued a one-line certificate but cannot produce the analyst-annotated chromatogram. Demand it.
2. **Library match below threshold** — match score borderline; demand the spectrum and an independent expert's review.
3. **Co-elution** — a second peak at or near the analyte's retention time, especially in plant material (marijuana) where many terpenes elute close to THC.
4. **Outdated library** — emerging synthetics may not be in the lab's reference library; the analyst may have substituted a "best guess" identification.
5. **Quantitation without calibration curve** — the State reports a weight percentage of the controlled substance, but the lab did not run a calibration curve for that specific instrument and method that day.

---

## 5. FTIR — Fourier-Transform Infrared Spectroscopy

FTIR identifies compounds by the absorption of IR radiation at frequencies characteristic of specific functional groups. It is Category A under SWGDRUG.

**Strengths:**
- Non-destructive (in many sampling configurations)
- Excellent for **bulk powders** and pharmaceutical tablets
- Very rapid

**Limitations:**
- Less specific than MS for differentiating closely related analogues
- **Mixtures are problematic** — overlapping absorption bands can mask the analyte; FTIR of a heavily-cut sample may not yield a confident identification
- Requires a clean reference spectrum library

**Audit points:**
- [ ] Was the spectrum compared to a reference library and analyst-confirmed?
- [ ] If the sample was a mixture, was the analyte spectrum extractable, or did the cut substances dominate?
- [ ] Was an attenuated total reflectance (ATR) sampling accessory used? ATR-FTIR has different sensitivity than transmission FTIR.

---

## 6. Plant Material Identification (Marijuana, Mushrooms)

**Marijuana** identification traditionally combined macroscopic examination (leaf morphology, seed structure), microscopic examination (cystolith hairs, glandular trichomes), and the Duquenois-Levine color test plus TLC. Post-Farm Bill, this is inadequate.

### Post-Farm Bill (2018) THC vs. CBD problem

The Agriculture Improvement Act of 2018 legalized hemp — Cannabis sativa with delta-9-THC concentration **≤ 0.3% on a dry-weight basis**. Marijuana (illegal under federal and most state law) is the same plant with > 0.3% delta-9-THC.

- **Visual / microscopic examination cannot distinguish marijuana from hemp.** The plants are botanically identical.
- **Duquenois-Levine reacts to both.** Color tests cannot distinguish.
- **A quantitative GC or LC method with proper internal standards is required** to determine whether the delta-9-THC concentration exceeds the 0.3% threshold.

**Audit points (post-Farm Bill marijuana cases):**
- [ ] Did the lab perform **quantitative** analysis of delta-9-THC, or only qualitative identification?
- [ ] If only Duquenois-Levine + macroscopic exam, the identification cannot distinguish marijuana from legal hemp — **CRITICAL audit finding**.
- [ ] Was the analyte distinguished from THCA (the acid precursor in raw plant material) and from delta-8-THC (a different isomer with separate legal status in some jurisdictions)?
- [ ] Was the moisture content / dry-weight basis correctly calculated?

### Mushrooms (psilocybin)

- Macroscopic and microscopic mycological examination identifies the species but not the active alkaloid.
- Psilocybin/psilocin identification requires LC-MS/MS or GC/MS extraction and quantitation.
- Be alert for non-controlled species sold as psilocybin mushrooms.

---

## 7. Bulk Sample / Multi-Unit Sampling

The single most under-litigated issue in drug-ID cases. When the seizure consists of multiple discrete units (e.g., 100 pills, 50 baggies, 30 wax envelopes), the State must prove every unit charged is the controlled substance — or use a defensible statistical sampling protocol.

### Three sampling regimes

1. **Test all** — every unit is individually analyzed. Defensible but expensive; rare for large seizures.
2. **Hypergeometric sampling** — statistically determine the minimum number of units to test such that, at a stated confidence level (typically 95%), all (or a defined fraction) of the untested units can be inferred to be the same substance. The DEA and accredited state labs use published hypergeometric tables.
3. **Convenience sampling** (a.k.a. "tested some") — analyst tested a non-representative subset without a statistical protocol. **This is challengeable.**

### The hypergeometric table (representative — confirm the lab's specific table)

| Population (N units) | Minimum sample size (k) for 95% confidence that ≥ 90% of population is the substance |
|---|---|
| 10 | 5 |
| 20 | 9 |
| 50 | 15 |
| 100 | 18 |
| 1,000 | 20 |

(Exact values vary by confidence level, target fraction, and table source. The DEA, NIST, and SWGDRUG publish slightly different tables — demand the lab's specific table and its citation.)

### Audit points for bulk samples

- [ ] How many units were seized?
- [ ] How many were tested?
- [ ] Was the sampling protocol random, hypergeometric, or convenience?
- [ ] If hypergeometric: what table was used and what confidence level was applied?
- [ ] Were the untested units **weighed** (defensible) or merely **counted** (less defensible) for purposes of the total quantity charged?
- [ ] In a **multi-substance** case (e.g., suspected fentanyl mixed in with heroin baggies), was each unit's identification confirmed individually, or was a single confirmation extrapolated?

**Defense argument when sampling is inadequate:** the State has proven that *the tested units* are the controlled substance. It has not proven the rest. Move in limine to restrict the substantive proof to the tested mass / units.

---

## 8. Daubert / Foret Sufficiency

Under La. C.E. Art. 702 and *State v. Foret*, 628 So. 2d 1116 (La. 1993), expert testimony based on a scientific methodology must be:

1. Testable / testable hypothesis
2. Subject to peer review and publication
3. Have a known or potentially known error rate
4. Apply standards governing the technique
5. Be generally accepted within the relevant scientific community

**Presumptive-only identification fails Daubert/Foret** because the methodology is documented to produce false positives at material rates with no analyst-confirmed orthogonal test. A Daubert/Foret motion is the right vehicle.

**Library-match-only identification** without analyst confirmation can fail the "standards governing the technique" prong — SWGDRUG requires analyst-confirmed identification, not automated library hits.

---

## 9. Common Defense Challenges to Drug ID

1. **Color test only — no confirmatory test.** Daubert/Foret motion to exclude or restrict the identification testimony.
2. **Confirmatory test without raw data.** Motion to compel the chromatograms, mass spectra, and analyst worksheets.
3. **Library match without analyst confirmation.** Cross the analyst on the difference between an automated hit and a confirmed identification.
4. **Inadequate sampling in a bulk case.** Motion in limine to restrict weight to tested units.
5. **CBD-vs-THC distinction not made.** Daubert/Foret motion in post-Farm Bill marijuana cases.
6. **Novel synthetic not in the lab's validated scope.** Daubert/Foret motion plus accreditation-scope challenge.
7. **Co-elution in chromatogram.** Cross the analyst on resolution and demand independent expert review.
8. **Calibration / system-suitability not documented.** Motion to compel; cross the analyst on QA.
9. **Outdated SOP version applied.** Foundation objection; cross on method currency.

---

## 10. Discovery Demand Checklist — Drug ID

- [ ] Full lab report (not just the certificate)
- [ ] Analyst worksheets and bench notes
- [ ] All raw instrument data — chromatograms, mass spectra, library hits with match scores
- [ ] Standard operating procedure (SOP) used, with version number
- [ ] Validation study for the method as applied
- [ ] Calibration / system-suitability records for the date of analysis
- [ ] Internal standard and reference material certificates of analysis
- [ ] Sampling protocol and hypergeometric table (bulk cases)
- [ ] Blank and control sample results from the analytical batch
- [ ] Library version (NIST / SWGDRUG / in-house) with date

---

*Last updated: see SKILL.md version. Mark any specific case-law or statute citation `[VERIFY CURRENT]` before filing.*
