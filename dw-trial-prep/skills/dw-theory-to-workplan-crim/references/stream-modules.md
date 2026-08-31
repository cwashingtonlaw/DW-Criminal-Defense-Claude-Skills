# The 7 Streams — Module A through Module G Task Categories

Read at Step 2 (Modules A–G) — the full task-category checklists for each of the seven workplan streams, with per-stream routing.

### MODULE A -- STREAM 1: Investigation Tasks

What facts need to be verified, investigated, or developed to support or test the selected theory?

**Task categories:**

1. **Witness interviews** -- Which witnesses need to be located and interviewed? What questions flow from the defense theory? Which witnesses have not yet been contacted?
   - Alibi witnesses (verify alibi timeline)
   - Occurrence witnesses (develop defense-favorable version)
   - Character witnesses (if character evidence is part of the theory)
   - Victim background witnesses (prior aggression, reputation for violence -- relevant to self-defense theories)

2. **Physical location visits** -- What scenes need to be visited, photographed, measured, or reconstructed?
   - Crime scene (lighting, sightlines, distances, access points)
   - Alibi locations (verify plausibility)
   - Surveillance camera canvass (identify cameras that may have captured relevant footage)

3. **Record subpoenas** -- What records need to be subpoenaed to support or test the theory?
   - Medical records (victim or defendant)
   - Employment records
   - Phone records (call logs, cell site data)
   - Social media account records
   - Prior police reports involving the victim
   - 911 audio and CAD records
   - Surveillance footage from businesses

4. **Fact verification** -- What factual claims in the theory need independent verification?
   - Timeline verification against physical evidence
   - Witness statement consistency checks
   - Physical plausibility of the defense version

**Routing:** Generate tasks and route to `dw-defense-investigator-tasking-crim` for investigator assignment and tracking.

---

### MODULE B -- STREAM 2: Discovery Actions

What additional discovery is needed to support or test this theory? What discovery deficiencies must be resolved?

**Task categories:**

1. **Outstanding discovery demands** -- Pull from `dw-discovery-compliance-monitor-crim` ledger. What has been demanded but not produced?
   - Flag items that are CRITICAL to the selected theory
   - Draft motion to compel for items outstanding beyond 30 days

2. **New discovery demands driven by the theory** -- What has not yet been demanded but is now needed because of the theory selection?
   - Brady/Giglio demands specific to this theory (e.g., if self-defense theory, demand victim's criminal history, prior DV reports, prior threats)
   - Expert-related discovery (lab bench notes, calibration records, analyst training records)
   - Witness-related discovery (witness criminal histories, prior statements, cooperation agreements)

3. **Motions to compel** -- For any outstanding critical items, draft or route motion to compel.

4. **Discovery preservation** -- Identify evidence at risk of destruction or loss and issue preservation demands.

**Routing:** Route discovery ledger tasks to `dw-discovery-compliance-monitor-crim`. Route Brady/Giglio demands to `dw-brady-giglio-auditor-crim`. Route motions to compel to `dw-pretrial-motion-library-crim`.

---

### MODULE C -- STREAM 3: Expert Witness Needs

What expert testimony is needed to support this theory? What prosecution experts need to be challenged?

**Task categories:**

1. **Defense expert retention** -- What experts does the defense need to retain?
   - Identify the discipline (forensic pathologist, ballistics, DNA, mental health, accident reconstruction, cell site, etc.)
   - Define the scope of engagement (consulting only vs. testifying)
   - Budget estimate and funding source (if public defender, indigent defense fund application under La. C.Cr.P. Art. 725)
   - Timeline for retention, report completion, and deposition/testimony

2. **Prosecution expert challenges** -- What prosecution experts need Daubert/Foret challenges?
   - Identify each prosecution expert and their discipline
   - Route to `dw-expert-witness-evaluator-crim` for full evaluation
   - Timeline for filing Daubert/Foret motion and hearing

3. **Expert opinion development** -- What specific opinions need to be developed?
   - Define the question the expert must answer
   - Identify the materials the expert needs to review
   - Set deadline for expert report

4. **Expert coordination** -- Schedule expert review of materials, coordinate with investigator for scene visits if needed, arrange for expert to review opposing expert's report.

**Routing:** Route expert evaluations to `dw-expert-witness-evaluator-crim`. Route indigent expert funding motions to `dw-pretrial-motion-library-crim`.

---

### MODULE D -- STREAM 4: Motion Practice

What pretrial motions support this theory? What motions must be filed to exclude harmful evidence or preserve favorable evidence?

**Task categories:**

1. **Suppression motions** -- Based on constitutional issues identified in the case analysis:
   - 4th Amendment (search and seizure) -- route to `dw-suppression-motion-crim`
   - 5th Amendment (statements / Miranda) -- route to `dw-suppression-motion-crim`
   - 14th Amendment (identification) -- route to `dw-suppression-motion-crim`
   - Fruit of the poisonous tree cascades

2. **404(b) opposition** -- If the State has filed or signaled a Prieur notice:
   - Route to `dw-404b-opposition-crim` for opposition drafting
   - If the defense wants to introduce 404(b) evidence about the victim (e.g., prior violence in a self-defense case), draft the supporting motion

3. **Motions in limine** -- Theory-specific evidentiary motions:
   - Exclude prejudicial photographs (inflammatory autopsy photos, crime scene photos)
   - Exclude hearsay or improper opinion testimony
   - Limit expert testimony scope
   - Exclude prior bad acts of the defendant

4. **Severance motions** -- Sever counts or co-defendants if joinder prejudices the selected theory.

5. **Other pretrial motions** -- Bill of particulars, bond reduction, continuance, venue change, recusal -- any motion that advances the theory or removes obstacles.

**Routing:** Route all motions to `dw-pretrial-motion-library-crim` for template selection and drafting. Route suppression motions to `dw-suppression-motion-crim`. Route 404(b) work to `dw-404b-opposition-crim`.

---

### MODULE E -- STREAM 5: Witness Preparation

Which witnesses need to be prepared? What testimony supports the theory? What cross-examination themes align with the theory?

**Task categories:**

1. **Cross-examination outlines for prosecution witnesses** -- For each prosecution witness:
   - How does their testimony interact with the defense theory?
   - What concessions can be extracted that support the theory?
   - What impeachment material exists?
   - Route to `dw-cross-exam-architect-crim` for full outline development

2. **Direct-examination outlines for defense witnesses** -- For each defense witness:
   - What testimony supports the theory?
   - What foundation must be laid?
   - What exhibits will be introduced through this witness?
   - Route to `dw-direct-exam-architect-crim` for full outline development

3. **Witness preparation sessions** -- Schedule and plan preparation for:
   - Defendant (if testifying -- strategic decision for attorney)
   - Character witnesses
   - Expert witnesses (coordinate testimony with expert report)
   - Alibi witnesses

4. **Witness sequencing** -- Determine the order of defense witnesses to build the theory narrative. Cross-reference with `dw-trial-narrative-builder-crim` for narrative arc.

**Routing:** Route cross-examination work to `dw-cross-exam-architect-crim`. Route direct-examination work to `dw-direct-exam-architect-crim`.

---

### MODULE F -- STREAM 6: Exhibit & Evidence Strategy

What exhibits support the theory? What demonstratives need to be created? What evidence authentication issues must be resolved?

**Task categories:**

1. **Exhibit identification** -- From the Evidence Table in Case Tables.xlsx, identify every exhibit that supports the defense theory:
   - Documentary exhibits (records, reports, photographs)
   - Physical exhibits (weapons, clothing, objects)
   - Digital exhibits (cell phone records, social media, surveillance video)
   - Demonstrative exhibits (diagrams, maps, timelines, charts)

2. **Exhibit preparation** -- For each identified exhibit:
   - Authentication method (stipulation, witness testimony, self-authentication)
   - Predicate witness (who lays the foundation?)
   - Enlargements or display format for trial
   - Pre-marking and exhibit list preparation

3. **Demonstrative creation** -- What demonstratives need to be built?
   - Crime scene diagram with defense-favorable annotations
   - Timeline chart showing defense version
   - Comparison charts (e.g., witness statement inconsistencies)
   - Maps (alibi route, cell site coverage areas)

4. **Evidence authentication challenges** -- What prosecution exhibits can be challenged on authentication, chain of custody, or admissibility grounds?
   - Cross-reference with `dw-chain-of-custody-auditor-crim` findings
   - Identify hearsay, best evidence, or foundation deficiencies

**Routing:** Route exhibit management to `dw-exhibit-manager-crim`. Route trial notebook assembly to `dw-trial-notebook-builder-crim`.

---

### MODULE G -- STREAM 7: Narrative & Theme Development

How does the theory translate into the courtroom story? What is the memorable theme? How does every piece of the trial reinforce that theme?

**Task categories:**

1. **Case theme development** -- Distill the defense theory into a one-sentence theme that:
   - Is memorable and repeatable
   - Frames the entire case from the defense perspective
   - Can be introduced in voir dire, reinforced in opening, proved through evidence, and argued in closing

2. **Opening statement outline** -- Build the opening around the theme:
   - Hook / primacy opener tied to the theme
   - Defense narrative in story form
   - Roadmap of the evidence the jury will hear
   - Route to `dw-trial-narrative-builder-crim` for full development

3. **Closing argument framework** -- Build the closing around the theme:
   - Element-by-element burden walk using the Defense Matrix
   - Witness credibility summary using cross-examination findings
   - Verdict form walk-through
   - Route to `dw-trial-narrative-builder-crim` for full development

4. **Jury instruction requests** -- What special jury instructions does the theory require?
   - Self-defense charges (La. R.S. 14:20 -- no duty to retreat, castle doctrine)
   - Heat-of-passion / manslaughter responsive verdict
   - Specific intent negation (intoxication, mental defect)
   - Lesser included offenses / responsive verdicts
   - Route to `dw-jury-instructions-builder-crim` for charge package

5. **Voir dire themes** -- What juror attitudes and experiences are relevant to this theory?
   - Route to `dw-voir-dire-assistant-crim` for voir dire question development

**Routing:** Route narrative work to `dw-trial-narrative-builder-crim`. Route jury instruction work to `dw-jury-instructions-builder-crim`. Route voir dire work to `dw-voir-dire-assistant-crim`.
