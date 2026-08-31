# Daubert/Foret Hearing Day Package

This reference contains the operational deliverables a defense attorney needs to actually try a Daubert/Foret hearing — distinct from the doctrinal framework in `daubert-foret-framework.md` (which supports the motion-drafting stage) and from trial cross-examination materials in `cross-exam-seeds.md`.

**Use this file when:** the motion to exclude has been filed, a hearing has been set, and the attorney needs the concrete documents and outlines to litigate the hearing itself.

**Pair with:** `la-daubert-hearing-procedure.md` for Louisiana-specific procedural rules (burden, standard of proof, timing, ruling format).

---

## 1. Hearing Witness Order

The defense controls witness order on its own motion. Plan the sequence to build cumulatively toward the exclusion ruling.

### Default defense-driven sequence

| Order | Witness | Purpose | Time Budget |
|-------|---------|---------|-------------|
| 1 | The challenged expert (called adversely) | Establish qualification deficiencies, methodology weaknesses, and concessions on factor 1–5 limitations | 60–120 min |
| 2 | Defense rebuttal expert (if retained) | Establish that methodology fails Daubert factors; introduce contrary scientific literature; explain why the expert's specific application is unreliable | 30–60 min |
| 3 | Custodian / records witness (if needed) | Authenticate prior testimony transcripts, lab proficiency records, accreditation documents for impeachment | 5–15 min |

### When to reverse order

If the State has the burden of admissibility (which it does — see `la-daubert-hearing-procedure.md`), the State calls its expert first on direct. Defense then cross-examines, and the cross *is* the centerpiece of the hearing. In that posture, the witness order is:

1. State's expert on direct (State controls)
2. Defense cross of State's expert (this is where the hearing is won or lost)
3. Defense rebuttal expert (defense's case-in-chief on the motion)
4. State rebuttal (if any)
5. Argument

### Decision points before the hearing

- **Is a defense rebuttal expert required?** If methodology is the central challenge, yes. If only qualifications are challenged, the cross of the State's expert may be sufficient.
- **Will the State's expert appear in person or by remote testimony?** Object to remote testimony if cross-examination effectiveness will be impaired.
- **Is sequestration ordered?** Move for sequestration of all witnesses (La. C.E. Art. 615) so the State's expert cannot tailor testimony to defense rebuttal expert.

---

## 2. Hearing Exhibit List

The hearing exhibit list is narrower and more technical than a trial exhibit list. Foundation requirements are relaxed at a Daubert hearing because the hearing itself is to determine admissibility — but the attorney should still anticipate State objections.

### Standard defense exhibit categories

| Exhibit Type | Examples | Foundation Source |
|-------------|----------|-------------------|
| **Expert's CV** | Current CV, prior CV versions if available | Self-authenticating; admit through expert on cross |
| **Expert's report** | Report served in this case, supplemental reports | Already in record via discovery |
| **Prior testimony transcripts** | Sworn testimony from other cases | Custodian or stipulation; offered for impeachment under La. C.E. Art. 613 |
| **Lab records** | Bench notes, chain of custody, proficiency tests, accreditation certificates | Subpoena duces tecum to lab; or stipulate authenticity |
| **Authoritative scientific literature** | NAS Report 2009, PCAST Report 2016, peer-reviewed studies, OSAC standards, DOJ ULTR guidelines | La. C.E. Art. 803(18) learned treatise; expert recognition required for full use |
| **Standards documents** | SWGDAM, AFTE, OSAC, ASB, ISO/IEC 17025 standards applicable to the discipline | Authenticate through expert or judicial notice |
| **Prior court rulings on this expert** | Daubert exclusion orders, limiting orders, disciplinary findings | Self-authenticating certified copies |
| **Demonstrative aids** | Charts of factor analysis, methodology diagrams | Mark for identification; offer if helpful to court |

### Foundation hierarchy (in case the State objects)

1. **Stipulation** — try to stipulate authenticity of all documentary exhibits before the hearing
2. **Self-authentication** — La. C.E. Art. 902 covers public records, certified copies, learned treatises
3. **Expert recognition** — for treatises, the State's expert (on cross) recognizes the work as authoritative under Art. 803(18)
4. **Custodian** — last resort; subpoena lab/agency records custodian

### Pre-hearing exhibit motion

File a "Notice of Intent to Use Learned Treatises" identifying every published source defense intends to cross-examine the State's expert with. This forces the State to either stipulate, object pre-hearing, or waive.

---

## 3. Cross-Examination Outline (Hearing-Specific)

Hearing cross is **not the same as trial cross**. At trial, defense attacks credibility for the jury. At a Daubert hearing, defense extracts the concessions the judge needs to rule for exclusion.

### Architecture

The hearing cross should march through Daubert/Foret factors in order, locking in factor-by-factor concessions. Unlike trial cross, length is appropriate — judges expect detail.

| Phase | Goal | Approximate Duration |
|-------|------|---------------------|
| **A. Qualification deconstruction** | Establish gaps between the expert's actual training and the opinions offered (Art. 702 qualification) | 15–30 min |
| **B. Factor 1 — Testability** | Lock in admissions about whether method has been tested under conditions like this case | 10–20 min |
| **C. Factor 2 — Peer review** | Establish what published peer-reviewed support exists, and what critical literature exists (NAS, PCAST) | 10–20 min |
| **D. Factor 3 — Error rate** | Force expert to acknowledge known error rate or admit none has been established | 10–20 min |
| **E. Factor 4 — Standards compliance** | Walk through governing standards and identify any deviation in this case | 10–25 min |
| **F. Factor 5 — General acceptance** | Distinguish practitioner acceptance from independent scientific acceptance; establish authoritative critiques | 5–15 min |
| **G. Analytical gap (Joiner)** | Walk through the data-to-conclusion logic chain and expose any leap | 10–20 min |
| **H. Litigation-driven opinion** | If applicable, establish that opinion was developed for this case rather than from independent research | 5–10 min |
| **I. DOJ Uniform Language compliance** | If absolute terms appear in report or testimony, lock that in | 5 min |
| **J. Bias and fee** | Brief — unless central to the motion, save bias for trial cross | 5–10 min |

### Question-form rules at hearing

- **Closed leading questions are still preferred**, but the judge will tolerate occasional open questions if they elicit a damaging concession
- **Use "you would agree" framing** — attorneys commonly call this the "Daubert frame": *"You would agree, doctor, that [factor concession]?"*
- **Treatise-anchored questions** — *"Are you familiar with the 2016 PCAST Report on Forensic Science?"* → *"You agree it found firearm/toolmark identification has not been validated as foundationally valid?"* (anchor every methodology challenge to a recognized authority)
- **Avoid argument** — judges punish argumentative cross at hearings; the goal is record-building, not jury persuasion

### Reserve cross-exam topics

Do **not** burn these at the hearing — save for trial cross before the jury:
- Personal credibility attacks
- Demeanor-based impeachment
- Sympathetic-to-defendant testimony elicited from State's expert
- Discipline-specific cross-examination chapters from `cross-exam-seeds.md` (these are trial materials)

---

## 4. Opposition Brief Response Template

The State will file an opposition brief defending the expert. Defense should file a reply (where local rules permit) addressing State arguments point-by-point.

```
DEFENDANT'S REPLY IN SUPPORT OF DAUBERT/FORET MOTION TO EXCLUDE

I.   INTRODUCTION
     [1 paragraph framing what the State conceded and what remains contested]

II.  THE STATE CONCEDES OR FAILS TO ADDRESS [X] ISSUES
     [List each motion argument the opposition did not engage. Argue
      these are conceded for purposes of the hearing.]

III. RESPONSE TO STATE'S ARGUMENTS
     A. [State Argument 1]
        [State's position]
        [Defense response with authority]
     B. [State Argument 2]
        [State's position]
        [Defense response with authority]
     [...]

IV.  THE STATE'S CASE LAW IS DISTINGUISHABLE / NON-CONTROLLING
     [Address each case the State cites; distinguish on facts,
      jurisdiction, or post-decision developments.]

V.   THE STATE'S RELIANCE ON PRACTITIONER ACCEPTANCE FAILS
     [Recurring State move: cite acceptance "in the field" without
      addressing independent scientific bodies. Distinguish.]

VI.  CONCLUSION
     [Restate requested relief: EXCLUDE / LIMIT / DAUBERT HEARING]
```

### Common State arguments and defense responses

| State Argument | Defense Response |
|----------------|------------------|
| "The methodology has been admitted in [N] prior cases." | Prior admission ≠ reliability; courts now apply *Daubert* with greater rigor; cite NAS/PCAST post-dating those rulings. |
| "The expert has testified as an expert before." | Prior qualification ≠ qualification here; methodology and case-specific application are still subject to Art. 702. |
| "The defense's challenges go to weight, not admissibility." | This is a gatekeeping motion; Art. 702(3) and (4) require **reliable methodology** and **reliable application**, both threshold admissibility questions. |
| "The expert is well-credentialed." | Credentials do not validate methodology; *Joiner* analytical gap can defeat even a well-credentialed expert. |
| "PCAST is not binding." | PCAST is not binding precedent but is authoritative scientific literature directly relevant to Factor 2 and Factor 5. |
| "Defense is asking the court to retry the science." | No — defense is asking the court to apply Art. 702's reliability gate as written. |

---

## 5. Oral Argument Outline

Oral argument at the hearing should be tight — assume 10–20 minutes. The judge has read the briefs.

```
ORAL ARGUMENT OUTLINE — DAUBERT/FORET HEARING

I.   ROADMAP (30 seconds)
     "Your Honor, defense will argue three things:
        (1) [primary ground]
        (2) [secondary ground]
        (3) [Joiner / analytical gap, if applicable]
      We respectfully request the Court [EXCLUDE / LIMIT] the testimony of [expert]."

II.  THE GATEKEEPING DUTY (1 minute)
     - Art. 702 imposes affirmative gatekeeping
     - Foret adopts Daubert framework
     - Burden is on the proponent (the State); cite la-daubert-hearing-procedure.md

III. PRIMARY GROUND (3-5 minutes)
     - Lead with the strongest factor failure
     - Cite the testimony elicited on cross today
     - Cite the authoritative literature in evidence

IV.  SECONDARY GROUND (2-4 minutes)
     - Second-strongest factor failure
     - Pattern: testimony elicited + literature

V.   ANALYTICAL GAP (2 minutes — if applicable)
     - Walk the data-to-conclusion chain
     - Identify the leap

VI.  RESPONSE TO ANTICIPATED STATE ARGUMENT (1-2 minutes)
     - Acknowledge State's strongest counter
     - Distinguish

VII. RELIEF REQUESTED (30 seconds)
     - "Exclude under Art. 702" or
     - "Limit testimony to [scope]" or
     - "Defer ruling pending [supplemental briefing / testing]"
```

### Argument craft notes

- **Quote the witness verbatim where possible.** Use the just-elicited cross to anchor the legal argument.
- **Read the bench.** If the judge interrupts with questions, that's the issue the judge cares about — engage it.
- **Preserve the record.** If the court rules from the bench, request specific findings on each Daubert factor for appellate review (see `la-daubert-hearing-procedure.md`).

---

## 6. Proposed Findings of Fact and Conclusions of Law

Some Louisiana judges request or accept proposed FOF/COL after the hearing — particularly in complex methodology challenges. Submit even if not requested when the issue is appellate-significant.

```
PROPOSED FINDINGS OF FACT AND CONCLUSIONS OF LAW
ON DEFENDANT'S MOTION TO EXCLUDE EXPERT TESTIMONY

FINDINGS OF FACT

1. [Expert]'s qualifications are [summary based on hearing record].
2. [Expert]'s methodology in this case consisted of [summary].
3. The methodology has [/has not] been empirically tested. [Cite hearing testimony.]
4. The methodology has [/has not] been subjected to peer review. [Cite testimony / literature.]
5. The known error rate for this methodology is [X% / unknown / contested]. [Cite testimony / NAS / PCAST.]
6. Published standards governing this methodology are [list]. The expert [followed / did not follow] them in this case. [Cite testimony.]
7. The methodology is [/is not] generally accepted in the relevant scientific community. [Distinguish practitioner from independent scientific community.]
8. There is [/is not] an analytical gap between the data and the expert's conclusion. [Cite testimony.]
[Continue for each disputed fact.]

CONCLUSIONS OF LAW

1. La. C.E. Art. 702 governs the admissibility of expert testimony.
2. The Court serves as gatekeeper. State v. Foret, 628 So.2d 1116 (La. 1993).
3. The proponent of the testimony bears the burden of establishing admissibility by a preponderance of the evidence.
4. Applying the Daubert/Foret factors:
   a. Testability: [conclusion]
   b. Peer review: [conclusion]
   c. Error rate: [conclusion]
   d. Standards: [conclusion]
   e. General acceptance: [conclusion]
5. [Optional: analytical gap; litigation-driven opinion; Kumho discretion.]
6. Therefore, the testimony [is excluded / is limited to (scope) / is admitted].
```

### Why submit FOF/COL even if not requested

- **Preserves appellate record.** A Daubert ruling without specific findings is harder to review on abuse-of-discretion appeal but easier to defend if the trial court adopts defense-friendly findings verbatim.
- **Frames the ruling.** If the court adopts substantial portions, the appellate record reflects defense's framing rather than the State's.
- **Forces opposing party to respond.** If the State submits competing FOF/COL, the differences highlight what is actually disputed.

---

## 7. Post-Hearing Brief (If Court Defers Ruling)

If the court takes the matter under advisement, file a post-hearing brief within the court's stated deadline (typically 7–14 days). The post-hearing brief differs from the original motion brief because it now incorporates the hearing record.

### Required elements

1. **Summary of hearing testimony** — what each witness said, with transcript page citations once available
2. **Findings the court should make** — narrative version of the proposed FOF/COL
3. **Application of Daubert factors to the developed record** — replace pre-hearing speculation with hearing-elicited testimony
4. **Authority update** — any case law decided between motion filing and hearing
5. **Renewed request for relief** — exclude, limit, or further evidentiary hearing

---

## 8. Hearing-Day Logistics Checklist

| Item | Status |
|------|--------|
| Subpoenas issued and served | [ ] |
| Sequestration motion ready | [ ] |
| Exhibits pre-marked and copied (judge, clerk, witness, opposing counsel, defense) | [ ] |
| Notice of intent to use learned treatises filed | [ ] |
| Cross-examination outline printed (do not read verbatim — use as scaffold) | [ ] |
| Authoritative literature tabbed and indexed | [ ] |
| Court reporter ordered (transcript will be needed for trial / appeal) | [ ] |
| Deposition transcripts of expert tabbed for impeachment | [ ] |
| Defense rebuttal expert prepped and present | [ ] |
| Proposed FOF/COL drafted in advance, ready to submit | [ ] |
| Ruling-form motion ready (limiting order draft, exclusion order draft) | [ ] |
| Post-hearing brief deadline calendared | [ ] |
| Trial date confirmed (Daubert ruling timing matters for trial preparation) | [ ] |

---

## Output Routing

Hearing Day Package deliverables follow the standard output path formula. Save to:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Daubert Hearing Day Package - [Expert Last Name].docx
```

Substantial sub-deliverables (cross-exam outline, proposed FOF/COL, reply brief) may be saved as separate files in the same folder with filename suffixes:

- `Daubert Hearing - Cross Outline - [Expert].docx`
- `Daubert Hearing - Proposed FOF-COL - [Expert].docx`
- `Daubert Hearing - Reply Brief - [Expert].docx`
- `Daubert Hearing - Exhibit List - [Expert].docx`

All deliverables receive attorney work-product marking per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`.

## Module I Overview (carried over from SKILL.md) — Burden, Six Deliverables, Hearing vs. Trial Cross, Appellate Record, Logistics

### Burden and Standard at the Hearing

The proponent of the testimony bears the burden of establishing admissibility by a preponderance of the evidence. In a criminal case where the State seeks to introduce expert testimony, the State carries this burden. *See Daubert*, 509 U.S. at 592 n.10; La. C.E. Art. 104(A); *Bourjaily v. United States*, 483 U.S. 171, 175-76 (1987).

The defense's role at the hearing is therefore not to "prove unreliability" but to test whether the State has carried its burden. Frame every cross-examination question and every argument with that framing.

### Six Hearing Day Deliverables

The Hearing Day Package consists of six discrete deliverables, each generated from the prior module outputs:

| # | Deliverable | Source Modules | Filename |
|---|------------|----------------|----------|
| 1 | **Witness order plan** with sequencing, time budgets, and sequestration strategy | A + F | `Daubert Hearing - Witness Order - [Expert].docx` |
| 2 | **Hearing exhibit list** with foundation hierarchy and Notice of Intent to Use Learned Treatises | E + G | `Daubert Hearing - Exhibit List - [Expert].docx` |
| 3 | **Hearing-specific cross-examination outline** structured factor-by-factor (distinct from trial cross seeds in Module G) | B + C + D + G | `Daubert Hearing - Cross Outline - [Expert].docx` |
| 4 | **Reply brief** responding to State's opposition point-by-point | B + C | `Daubert Hearing - Reply Brief - [Expert].docx` |
| 5 | **Oral argument outline** (10-20 minute roadmap) with verbatim cross quotes inserted post-hearing | All applicable modules | `Daubert Hearing - Oral Argument - [Expert].docx` |
| 6 | **Proposed Findings of Fact and Conclusions of Law** factor-by-factor | All applicable modules | `Daubert Hearing - Proposed FOF-COL - [Expert].docx` |

Optional seventh deliverable: **post-hearing brief** if the court takes the matter under advisement.

### Hearing Cross vs. Trial Cross — Critical Distinction

Hearing cross is **not** the same as trial cross. The audiences, goals, question forms, and topical scope all differ:

| Dimension | Hearing Cross (Module I) | Trial Cross (Module G) |
|-----------|-------------------------|-----------------------|
| **Audience** | Judge as gatekeeper | Jury as factfinder |
| **Goal** | Extract factor-by-factor concessions to defeat admissibility | Establish credibility-undermining concessions for closing argument |
| **Length** | Detailed; judges expect thorough factor analysis | Tight; juror attention is finite |
| **Question form** | Closed leading + occasional treatise-anchored open questions | Closed leading only |
| **Topical scope** | Daubert factors 1-5 + analytical gap + DOJ Uniform Language | Discipline-specific seeds, methodology errors, bias |
| **Demeanor / personality** | Reserved; do not burn at hearing | Available for impeachment at trial |

**Rule:** Reserve discipline-specific cross-examination chapters from `cross-exam-seeds.md` for trial. Do not preview those at the hearing — once previewed, the State will prepare the expert to neutralize them at trial.

### Building the Appellate Record at the Hearing

Although La. C.E. Art. 104(A) relaxes evidentiary rules at preliminary admissibility hearings, the appellate court reviews the ruling on the record made. Therefore:

1. **Authenticate exhibits anyway** when feasible (stipulation, self-authentication under Art. 902, or expert recognition under Art. 803(18))
2. **Make every objection on the record** even when the court is likely to overrule
3. **Request specific findings on each Daubert factor** before the court rules — a general "motion denied" is harder to appeal than a ruling that engages each factor
4. **Order the hearing transcript** promptly after the hearing
5. **Submit Proposed FOF/COL** even if the court has not requested them — adoption shapes the appellate record

For the standards of review on direct appeal, supervisory writ, and federal habeas, see `references/la-daubert-hearing-procedure.md`.

### Hearing Day Logistics Checklist

Run through the logistics checklist in `references/hearing-day-package.md` (Section 8) at least 48 hours before the hearing. Common items: subpoenas, sequestration motion, pre-marked exhibits, court reporter, defense rebuttal expert prep, ruling-form drafts (limiting order and exclusion order skeletons), post-hearing brief deadline calendaring, trial date confirmation.
