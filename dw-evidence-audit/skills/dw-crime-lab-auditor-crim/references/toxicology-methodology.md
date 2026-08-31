# Toxicology Methodology

This reference is loaded by `dw-crime-lab-auditor-crim` Module B. It addresses the chemistry of forensic toxicology — immunoassay screening, instrumental confirmation, blood-alcohol analysis, drug-tox interpretation, and the metabolite-vs-impairment problem.

**Scope boundary:** DWI roadside conduct, SFST protocol, breath-instrument operator audit, and rising-BAC arithmetic belong to `dw-dwi-specialist-crim`. This reference covers the **lab-side** chemistry of blood and urine analysis.

---

## 1. The Screening / Confirmation Hierarchy

Forensic toxicology is a two-tier process:

1. **Screening** — fast, broad-spectrum, sensitive but not specific. Designed to flag any sample that may contain a drug or drug class.
2. **Confirmation** — slow, narrow, highly specific. Required before any positive screen can be reported as a definitive identification.

**Every positive screen must be confirmed by an orthogonal technique** at a defined cutoff. A screen-only positive is not a defensible identification.

---

## 2. Immunoassay Screening (ELISA, EMIT, CEDIA)

Immunoassays use antibodies that bind to a target analyte (or drug class). Bound vs. unbound antibody ratios are detected by enzyme-substrate color change (EMIT), fluorescence polarization, or other detection.

### Common immunoassay platforms
- **ELISA** (Enzyme-Linked Immunosorbent Assay) — common in postmortem and DWI workflows
- **EMIT** (Enzyme-Multiplied Immunoassay Technique) — common in workplace and clinical workflows
- **CEDIA** (Cloned Enzyme Donor Immunoassay) — used in some clinical and forensic labs

### Cutoffs

Each assay has a defined **cutoff** — a concentration threshold above which the screen reports "positive." Cutoffs are designed to balance false negatives against false positives. Common cutoffs (representative; **verify with the specific lab's SOP**):

| Drug class | Typical screening cutoff (urine) |
|---|---|
| Amphetamines | 500 ng/mL |
| Cocaine metabolite (benzoylecgonine) | 150 ng/mL |
| Opiates | 2,000 ng/mL (DHHS) or 300 ng/mL (lower clinical cutoff) |
| Cannabinoids (carboxy-THC) | 50 ng/mL |
| Benzodiazepines | 200-300 ng/mL |
| Methadone | 300 ng/mL |
| PCP | 25 ng/mL |

(Blood cutoffs are typically lower. Confirm with the specific lab.)

### Cross-Reactivity — Where False Positives Come From

Immunoassay antibodies bind related compounds, not just the target. Cross-reactivity is documented in the manufacturer's package insert and is **discoverable**.

Representative cross-reactants:
- **Amphetamine screens:** pseudoephedrine, phenylephrine, selegiline (metabolizes to amphetamine), bupropion, ranitidine (older formulations), trazodone, labetalol
- **Opiate screens:** poppy seeds, quinolone antibiotics, rifampin, dextromethorphan (at high doses)
- **Benzodiazepine screens:** sertraline, oxaprozin
- **THC screens:** efavirenz, hemp-derived CBD products (especially full-spectrum)
- **PCP screens:** dextromethorphan, diphenhydramine, venlafaxine, tramadol

**Audit points for immunoassay screening:**
- [ ] What is the assay's cutoff for the reported analyte?
- [ ] What cross-reactants does the manufacturer document?
- [ ] Was the screening cutoff applied correctly? (A cutoff is not "any signal above zero" — it is a specific concentration threshold)
- [ ] Was a confirmation performed for every positive screen reported in the case?
- [ ] Was the patient/subject on any medication that cross-reacts with the screen? Demand the medication list.

---

## 3. Confirmatory Testing — GC/MS and LC-MS/MS

Confirmation requires an **orthogonal** technique — one based on different chemical principles from the screen. Immunoassay confirmation by another immunoassay is **not** confirmation.

### GC/MS for tox

- Excellent for volatile and semi-volatile analytes
- Requires derivatization for polar analytes (silylation, acylation)
- Provides retention time + mass spectrum — chemical fingerprint

### LC-MS/MS for tox

- Better for polar, thermally-labile, and high-mass analytes (most modern drugs, including fentanyl analogues, novel opioids, synthetic cannabinoids)
- Triple-quadrupole MS/MS allows multiple-reaction-monitoring (MRM) for specificity
- The current state-of-the-art for forensic toxicology confirmation

### Required elements of a defensible confirmation

- **Deuterated internal standards** (e.g., cocaine-d3, morphine-d3, fentanyl-d5) added to every sample at a known concentration
- **Calibration curve** — at least 5 points spanning the expected concentration range, run with the batch
- **Quality control samples** at low, mid, and high concentrations
- **Defined cutoff for confirmation** (typically equal to or below the screening cutoff)
- **Retention time within ±5% of standard** and **ion ratios within ±20% of standard** for positive identification
- **Analyst review** of chromatogram, MS spectrum, and ion ratios

### Audit points for confirmation

- [ ] Was the confirmation technique orthogonal to the screen?
- [ ] What was the confirmation cutoff and how does it relate to the screen cutoff?
- [ ] Were deuterated internal standards used?
- [ ] Were ion ratios within the lab's acceptance criteria?
- [ ] Was the analyst-confirmed report distinguished from an automated report?
- [ ] Were positive controls run with the batch and did they pass?

---

## 4. Calibration — The Numeric Backbone

Quantitation (reporting a concentration in ng/mL or g/dL) requires a calibration curve constructed from reference standards.

- **Linearity** — typically R² ≥ 0.99 across the calibration range
- **Range** — the validated range of concentrations. Results above the upper limit must be diluted and re-run; results below the lower limit (LOQ — limit of quantitation) cannot be quantified
- **Internal standards** — deuterated analogues of the analyte; controls for injection-volume variability and matrix effects
- **Recovery / matrix-effect studies** — part of validation; verifies that the analyte is recovered from biological matrix (blood, urine) at acceptable efficiency
- **Carryover study** — verifies that a high-concentration sample does not bleed into the next injection

### Audit points

- [ ] Was a calibration curve run on the date of analysis?
- [ ] What was the R² of the curve?
- [ ] Was the reported concentration within the linear range?
- [ ] If the result was above the upper range, was the sample diluted and re-run?
- [ ] Were internal standards used and at what concentration?

---

## 5. Sample Retention / Preservation — La. R.S. 32:663

Louisiana law (La. R.S. 32:663 and analogous provisions — **VERIFY CURRENT**) entitles a defendant in a DWI/DUI prosecution involving chemical testing to have a portion of the sample preserved for independent testing by a defense laboratory.

**Audit points:**
- [ ] Did the lab preserve an aliquot of the blood or urine sample?
- [ ] Was the aliquot offered for or made available to the defense?
- [ ] What were the storage conditions for the preserved sample? Were they sufficient to maintain integrity for the time elapsed?
- [ ] If the sample was consumed in testing without preservation, does this trigger *Trombetta/Youngblood* (*California v. Trombetta*, 467 U.S. 479 (1984); *Arizona v. Youngblood*, 488 U.S. 51 (1988))?
- [ ] If preservation occurred but the defense was not notified of the right to independent testing, is there a procedural-due-process challenge?

---

## 6. Blood Alcohol Specifically

### Headspace GC

The accepted technique for forensic blood-alcohol quantitation. The sample is sealed in a vial, equilibrated at a controlled temperature, and the vapor (headspace) above the liquid is sampled and injected onto a GC column. Ethanol elutes at a characteristic retention time and is quantified against an internal standard (typically n-propanol).

### Critical elements

- **Internal standard** — n-propanol added to every sample, calibrator, and control
- **Dual-column or GC/MS confirmation** — best-practice labs run two columns of different polarity, or confirm with GC/MS, to rule out co-eluting volatiles (e.g., acetone, isopropanol, methanol)
- **Calibration** — multi-point curve with calibrators at known ethanol concentrations
- **Controls** — low, mid, and high QC samples each batch; certified reference material
- **Reporting** — the reported value should be in g/100 mL (g%) or g/dL, and the report should specify **whole blood** vs. **serum**

### Whole blood vs. serum / plasma — the conversion problem

Hospital clinical labs typically report **serum** or **plasma** ethanol. Forensic labs report **whole blood** ethanol. Serum/plasma reads approximately **1.14× higher** than whole blood for the same person at the same time (water content of serum is higher).

- A hospital serum BAC of 0.114 g/dL converts to approximately 0.10 g/dL whole blood.
- If the State introduces a hospital serum result without converting to whole-blood basis, this is a **CRITICAL audit finding** — the report has been compared against the wrong legal threshold.
- The conversion factor itself is approximate (range 1.10-1.18 reported in the literature); a defense expert can argue for the lower end.

### Anticoagulant / preservative

Forensic blood draws use **sodium fluoride + potassium oxalate** tubes (gray-top). Sodium fluoride inhibits glycolysis (which can otherwise produce ethanol post-collection from blood glucose); potassium oxalate is an anticoagulant.

- A blood sample drawn into the wrong tube (e.g., a clinical EDTA tube without fluoride) can ferment in storage, producing ethanol in the sample after collection — a false positive or inflated reading.
- Audit the tube type, the volume drawn, and the time-to-analysis.

### Storage and stability

- Refrigerated (4 °C) blood samples in gray-top tubes are stable for ethanol analysis for **weeks to months**
- Improperly stored samples (room temperature; without preservative; partially filled tubes) can show significant changes (typically loss, but in contaminated samples, gain)
- Audit the chain-of-custody for temperature gaps and storage duration

### DWI / DWI Drug-Tox handoff

When the case involves DWI and the lab analysis is part of that workflow, the **lab portion** is audited here; the **roadside conduct, SFST, instrument-operator audit, and rising-BAC defense** belong to `dw-dwi-specialist-crim`. Coordinate by passing lab-side findings into that skill's workflow.

---

## 7. THC — Active vs. Metabolite, Presence vs. Impairment

The single most important fact in driving-under-the-influence-of-marijuana cases:

- **Delta-9-THC** (the psychoactive component) has a short blood half-life (1-4 hours for occasional users; longer for chronic users). Detectable for hours, not days.
- **11-OH-THC** (an active metabolite) has somewhat longer detectability but still relatively short.
- **11-nor-9-carboxy-THC ("carboxy-THC")** is an inactive metabolite. Detectable in blood for days to weeks (chronic users) and in urine for weeks.

**The legal implication:** a positive carboxy-THC result proves **past use** of THC. It does **not** prove **impairment at the time of the alleged offense**. Many states (and the federal scientific consensus) recognize this distinction; some "per se" statutes nonetheless criminalize any detectable metabolite.

**Audit points:**
- [ ] Did the lab quantify delta-9-THC specifically, or only carboxy-THC?
- [ ] Was the analyte in blood (more probative of recent use) or urine (less probative of impairment at a specific time)?
- [ ] What concentration was reported, and what is the literature on impairment thresholds for that concentration?
- [ ] Did the State's witness conflate "positive for THC metabolites" with "impaired by marijuana"?

---

## 8. Postmortem Redistribution

In postmortem toxicology (overdose cases, deaths in custody, vehicular homicide), drug concentrations measured in heart blood or femoral blood can differ substantially from antemortem concentrations due to **postmortem redistribution (PMR)**.

- Drugs with high tissue binding (tricyclic antidepressants, some opioids, methadone) can redistribute from tissue into vascular compartments after death
- Heart blood is more affected by PMR than femoral (peripheral) blood
- Time between death and sample collection matters

**Audit points (postmortem cases):**
- [ ] Was the blood drawn from a peripheral site (femoral preferred) or from the heart?
- [ ] What was the time interval from death to collection?
- [ ] Did the toxicologist acknowledge PMR in interpreting the result?
- [ ] Was a tissue sample (liver, vitreous humor) also analyzed for comparison?

---

## 9. Common Defense Challenges to Toxicology

1. **Immunoassay-only positive — no confirmation.** Daubert/Foret motion or motion in limine to exclude.
2. **Confirmation by an immunoassay (not orthogonal).** Same.
3. **Cross-reactivity from prescribed medication.** Demand the medication list; cross the analyst on package-insert cross-reactants.
4. **Hospital serum BAC introduced as "blood alcohol" without conversion.** Motion in limine; cross on serum-vs-whole-blood.
5. **Carboxy-THC introduced to prove impairment.** Motion in limine; expert testimony on metabolite half-life.
6. **Sample not preserved; defense denied independent testing.** *Trombetta/Youngblood* motion; La. R.S. 32:663 motion.
7. **Wrong-tube blood draw (clinical tube without fluoride).** Foundation challenge; cross on fermentation risk.
8. **Postmortem redistribution not addressed.** Cross the toxicologist; defense toxicology expert.
9. **Calibration curve not run on the date of analysis.** Motion to compel; cross on quantitation validity.
10. **Below limit of quantitation (LOQ).** The reported value is not defensible as a precise concentration.

---

## 10. Discovery Demand Checklist — Toxicology

- [ ] Full lab report (not just the certificate)
- [ ] Screening assay manufacturer and package insert (cross-reactivity table)
- [ ] Screening cutoff applied
- [ ] Confirmatory technique chromatograms and spectra, with analyst worksheets
- [ ] Calibration curve and R² for the date of analysis
- [ ] Internal standard concentration and lot number
- [ ] QC sample results for the batch
- [ ] Storage / chain-of-custody for the sample from collection to analysis
- [ ] Tube type and preservative documentation (blood-alcohol cases)
- [ ] Whole-blood vs. serum specification (BAC cases)
- [ ] Preserved-aliquot location and availability (independent testing)
- [ ] Postmortem-redistribution worksheet (postmortem cases)
- [ ] Medication list / hospital records of the subject (cross-reactivity defense)

---

*Last updated: see SKILL.md version. Mark any specific case-law, statute, or numeric cutoff `[VERIFY CURRENT]` before filing.*

---

## Module B Short Version (moved from SKILL.md)

Short version: every positive drug screen by immunoassay (ELISA, EMIT) must be confirmed by an orthogonal technique — typically GC/MS or LC-MS/MS — at a defined cutoff with deuterated internal standards. Blood-alcohol quantitation by headspace GC requires calibration curve, dual-column or GC-MS confirmation, and explicit whole-blood-vs-serum reporting (serum reads ~1.14× higher than whole blood). Defendant has a statutory right to a preserved sample for independent testing (La. R.S. 32:663 and related provisions — VERIFY CURRENT). For THC, the presence of carboxy-THC metabolite proves only past use, not impairment at the time of driving. Postmortem redistribution is a major confounder for postmortem tox.
