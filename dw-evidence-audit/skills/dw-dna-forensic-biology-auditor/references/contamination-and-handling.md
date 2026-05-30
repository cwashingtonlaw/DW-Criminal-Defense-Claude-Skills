# Contamination & Handling — Reference

Deep methodology reference for **Module E — Contamination & Handling**. Load whenever DNA evidence is at issue (essentially every case).

---

## 1. Collection-Stage Contamination

### Crime-Scene Contamination Vectors
- **Investigator DNA** — officers and crime-scene technicians shed DNA at scenes. Without proper PPE (mask, gloves changed between items, hairnet), investigator DNA can deposit on evidence.
- **Victim DNA on items belonging to or touched by the suspect** — handling sequence matters; victim DNA may legitimately be present from earlier innocent contact.
- **Secondary transfer at the scene** — touching item A and then item B can transfer DNA between items. Investigators must change gloves between items.
- **Substrate DNA** — environmental DNA already on surfaces (skin cells from prior occupants, casual contact). A "background DNA" reference of the scene itself is rarely collected but should be.

### Collection Method Audit
- [ ] What collection method was used (swab — wet/dry technique; tape lift; cutting)?
- [ ] Were gloves changed between items?
- [ ] Was PPE consistent with reduce-contamination protocols?
- [ ] Was the scene processed in an order that minimized cross-contamination (suspect-related items first, then victim items — or vice versa as appropriate)?
- [ ] Were elimination samples collected from all officers and technicians who handled evidence?

### Victim Contact / Sexual Assault Specifics
- Sexual-assault evidence collection follows a defined kit protocol (e.g., the Louisiana Sexual Assault Kit). Deviations from the kit protocol are audit findings.
- Time between offense and collection — DNA evidence degrades with time, washing, urination, defecation. The collection timing must be documented and considered in interpretation.

---

## 2. Transport Contamination

- **Container integrity** — paper bags (preferred for DNA evidence; allows drying) vs. plastic (encourages bacterial growth, degradation).
- **Temperature** — DNA degrades at elevated temperature; samples left in vehicle trunks in Louisiana summer heat can degrade substantially.
- **Time** — every hour between collection and freezing/refrigeration matters for some sample types.
- **Sealing** — evidence tape with date, initials, and case number. Breaks in the tape without documentation = chain break.

**Audit:** Were collection-to-storage times documented? Were items stored at appropriate temperatures during transport? Were sealing protocols followed?

---

## 3. Lab Workflow Contamination

### Required Controls

| Control | Purpose | When Run |
|---|---|---|
| **Reagent blank** | Detects contamination in extraction reagents | Every extraction batch |
| **Amplification negative (PCR negative)** | Detects contamination in amplification reagents | Every amplification batch |
| **Positive control (e.g., 9947A)** | Confirms amplification worked | Every amplification batch |
| **Validation blank** | Establishes the lab environment is contamination-free | Periodically per SOP |

### What a Failed or Off-Spec Control Means
- A reagent blank showing peaks indicates contamination somewhere upstream. The lab's SOP must specify the response (re-extract, re-amplify, declare batch invalid).
- An amplification negative showing peaks indicates contamination in the amplification process.
- A positive control failure means the amplification did not work properly; all samples in the batch are suspect.

**Audit:** Were all required controls run? Did any control show off-spec results? How did the lab respond? Was the response documented and consistent with the SOP?

### Cross-Contamination Between Samples
- Same-batch processing of evidence samples and reference samples is a contamination risk. Best practice is separating evidence and reference workflows.
- Carryover from prior samples in the same instrument (CE injection) — typically detected by reagent blanks but possible.
- High-template samples in the same batch as low-template samples can produce contamination if pipetting hygiene is poor.

**Audit:** Were defendant reference samples and evidence samples processed in separate batches? If not, is there evidence of carryover?

### Lab Environment
- Pre-PCR (extraction) and post-PCR (amplification, CE) areas should be physically separated to prevent amplicon carryover contaminating fresh samples.
- Air-flow direction, equipment dedication, and personnel movement protocols all matter.
- Periodic environmental swabs of bench, equipment, and air handling should be documented.

---

## 4. Reference Sample Contamination

### Sources
- **Analyst DNA** — analyst's own DNA detected in the evidence sample. Many U.S. labs maintain an "elimination database" of all current and former analyst, technician, and contractor profiles. The elimination database should be searched against any unknown profile in case work.
- **Technician / collection officer DNA** — same issue.
- **Victim DNA on suspect evidence** — particularly in sexual assault and assault cases, the victim's DNA legitimately appears on the suspect's clothing or weapons from contact during the offense. The interpretive challenge is distinguishing offense-related contact from prior innocent contact.

### Audit
- Is the lab's elimination database current and complete?
- Was the elimination database searched against any unknown profile in this case?
- Are the analyst, technicians, and officers in the database?

### Pre-Existing Profile Contamination
- Reference samples may have been collected from the defendant at booking; if booking-station equipment was contaminated, the "reference" profile may itself be a mixture.

---

## 5. Chain of Custody — Lab-Side

### From Intake Through Disposal
The lab-side chain of custody covers:
- **Intake** — receipt from law enforcement, logging, initial barcoding
- **Storage** — secure refrigeration/freezer; access logs
- **Internal transfers** — extraction → quantification → amplification → CE → analyst review
- **Sub-sampling** — taking a portion for testing; what was preserved for re-testing
- **Re-tests / re-runs** — if any
- **Disposal / return** — to law enforcement or destruction

### Audit
- [ ] Intake date and condition documented
- [ ] Storage conditions documented (freezer temperature logs)
- [ ] Access logs identify every person who handled the item
- [ ] Every internal transfer logged with date, time, and recipient
- [ ] Sufficient sample preserved for defense re-test (La. R.S. 15:622 considerations)
- [ ] Re-test documentation if applicable
- [ ] Final disposition documented

### Common Break Points
- Time gap in the log without explanation.
- Initials of an unidentified person.
- Storage logs missing for the relevant period.
- Item moved to a new location without log entry.
- Sub-sampling without documentation of the consumed quantity.

---

## 6. Touch / Transfer DNA — Specific Contamination Concerns

Touch DNA is especially vulnerable to contamination concerns:

### Secondary and Tertiary Transfer
- Person A shakes hands with Person B; Person B then touches a weapon; Person A's DNA may be on the weapon despite Person A having never touched the weapon.
- Tertiary transfer (A → B → C → object) has been demonstrated in laboratory studies, though typically at lower levels.
- The lab cannot tell the difference between primary deposit and secondary/tertiary transfer from the EPG alone.

### Persistence and Shedder Variability
- Some individuals shed DNA prolifically ("good shedders"); others shed little. The amount of DNA recovered does not establish the duration or recency of contact.
- DNA can persist on surfaces for weeks to months under certain conditions; absence of DNA does not prove non-contact, and presence does not prove recent contact.

### Activity-Level Inference Limits
- Sub-source LR ("this DNA is from the defendant") does not establish how the DNA got there.
- Activity-level propositions require transfer/persistence studies that the lab usually has not conducted; PG software does not produce activity-level LRs.
- The defense should object to activity-level testimony unsupported by activity-level analysis.

### Cross-Examination Themes for Touch DNA
- Establish that touch-DNA presence does not establish duration of contact.
- Establish that secondary transfer is possible and documented.
- Establish that the defendant could have deposited DNA on the item innocently before the offense.
- Establish that "shedder status" varies and the data does not address it.

---

## 7. Audit Checklist — Contamination & Handling

- [ ] Crime-scene collection PPE and glove-change protocol documented
- [ ] Scene processing order documented; cross-contamination risk addressed
- [ ] Elimination samples from officers and technicians available
- [ ] Background DNA at scene considered
- [ ] Transport temperature and timing documented
- [ ] Container appropriate (paper for DNA evidence)
- [ ] Sealing intact through chain
- [ ] All required lab controls run (reagent blanks, PCR negatives, positive controls)
- [ ] All controls passed; any off-spec results documented with response
- [ ] Evidence and reference samples processed in separate batches (or, if same batch, justification)
- [ ] Pre-PCR / post-PCR areas physically separated
- [ ] Periodic lab environment swabs documented
- [ ] Elimination database current and searched against unknown profiles
- [ ] Chain of custody log complete, no unexplained gaps
- [ ] Storage temperature logs available for the relevant period
- [ ] Sufficient sample preserved for defense re-test
- [ ] Touch-DNA specific concerns (transfer, persistence, shedder variability) addressed
- [ ] No activity-level inference unsupported by activity-level analysis

---

*See also: `str-methodology.md` (analytical controls), `mixture-interpretation.md` (interpretive impact of contamination), `louisiana-dna-case-law.md` (Brady/Foret).*
