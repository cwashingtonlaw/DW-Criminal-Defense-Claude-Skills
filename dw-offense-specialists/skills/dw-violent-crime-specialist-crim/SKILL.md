---
name: dw-violent-crime-specialist-crim
category: offense-specialists
description: >
  Violent-crime defense framework for Louisiana state prosecutions. ALWAYS invoke for "homicide,"
  "murder," "first/second degree murder," "manslaughter," "negligent homicide," "heat of
  passion," "sudden passion," "self-defense," "stand your ground," "justifiable homicide,"
  "defense of others," "felony murder," "aggravated/second degree battery," "battery on a police
  officer," "aggravated assault," "aggravated/second degree kidnapping," "aggravated burglary,"
  "home invasion," "armed/first degree/simple robbery," "firearm enhancement," R.S. 14:30,
  14:30.1, 14:31, 14:32, 14:34, 14:34.1, 14:34.5, 14:37, 14:44, 14:44.1, 14:60, 14:62.8, 14:64,
  14:64.1, 14:64.3, 14:65, "Miller hearing," "juvenile LWOP," "responsive verdict," "Article
  814," or "death-eligible." Do NOT use for sex offenses (dw-sex-offense-specialist-crim), drug
  offenses (dw-drug-offense-specialist-crim), DWI (dw-dwi-specialist-crim), or standalone gun
  charges (dw-firearms-specialist-crim); DO use when a violent crime is the lead charge with a
  firearm.
---

# D&W Violent Crime Specialist

## STEP 0 — FILE INTAKE HARD STOP: CONFIRM VIOLENT-CRIME CASE

Before drafting anything, confirm the elements of a violent-crime case are present and that the case has not been mis-routed. Stop and request clarification if any of the below cannot be answered from the discovery file.

**Case-type verification:**
- Charged statute(s) — exact La. R.S. citations (homicide, battery, kidnapping, burglary, robbery, or stacked combinations).
- Lead charge classification:
  - Capital first degree murder (La. R.S. 14:30) — death-eligibility issue triggered.
  - Non-capital first degree murder (LWOP-eligible).
  - Second degree murder (La. R.S. 14:30.1) — mandatory LWOP.
  - Manslaughter (La. R.S. 14:31) — top count, not responsive.
  - Negligent homicide (La. R.S. 14:32).
  - Aggravated / second degree battery (La. R.S. 14:34, 14:34.1).
  - Battery on a peace officer (La. R.S. 14:34.5).
  - Aggravated assault (La. R.S. 14:37) — including firearm-aggravated subsections.
  - Aggravated / second degree kidnapping (La. R.S. 14:44, 14:44.1).
  - Aggravated burglary (La. R.S. 14:60).
  - Home invasion (La. R.S. 14:62.8).
  - Armed robbery (La. R.S. 14:64) — flag La. R.S. 14:64.3 firearm enhancement automatically.
  - First degree robbery (La. R.S. 14:64.1).
  - Simple robbery (La. R.S. 14:65).
- Defendant age at the time of the offense (juvenile *Miller / Montgomery* trigger).
- Whether a firearm was the instrumentality (drives 14:64.3 analysis and any stacked firearms count).
- Prior felony record (drives habitual-offender exposure under La. R.S. 15:529.1).
- Whether the State is signaling capital intent (death-eligibility decision under La. C.Cr.P. Art. 905.4).
- Co-defendant posture (severance theory, principals doctrine under La. R.S. 14:24).
- Any plausible self-defense, defense-of-others, or heat-of-passion theory in the discovery.

**If any element is unclear, STOP and request clarification before proceeding.** Do not generate downstream work product on an unverified case posture.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all internal deliverable headers.
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `{{CASE_ROOT}}`).

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product unless they become attached exhibits to a filed pleading; apply work-product marking by default. Output paths follow the Cowork Analysis formula:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

If any required Case Brain variable (`{{DEFENDANT_NAME}}`, `{{DOCKET}}`, `{{PARISH}}`, `{{COURT}}`, `{{JUDGE_NAME}}`, `{{ADA_NAME}}`) is missing, prompt the attorney before drafting.

---

**Date of offense governs every statute cite.** Before quoting any element, penalty range, enhancement, or parole-eligibility figure, confirm the date of offense per count and select the statute version in force on that date using `dw-shared-protocols-crim/references/sentencing-statute-versions.md` (15:529.1 / 15:571.3 / 15:574.4 and the offense statute itself). Never fabricate a prior-version value; flag `[VERIFY — Westlaw]` where that file does.

## STEP 1 — INFORMATION GATHERING PROTOCOL

Use `dw-case-brain-crim` to pull the structured case context. The minimum dataset for this skill is:

The minimum dataset covers defendant/victim demographics, charged statutes and responsive-verdict architecture, death-eligibility posture, discovery index, prior record, co-defendant status, scene and motion status, and existing theory drafts. Read `references/information-gathering-checklist.md` now for the itemized list with routing and pull every item.

If the case file is incomplete on any axis above, log the gap, do NOT speculate, and proceed with what is anchored in discovery — flagging unsupported items for follow-up.

---

## SOURCE CITATION MANDATE

Every factual claim made about the case in any deliverable produced by this skill must cite the exact discovery item that supports it. The format is the same as in `dw-drug-offense-specialist-crim` and other charge specialists:

> [Bates No. or filename, page/timestamp, brief description]

Examples:
- "Defendant told the responding officer he was 'protecting himself' (BWC_Officer_Smith_2024-03-12.mp4 at 03:42)."
- "Victim's blood alcohol was 0.21 (Autopsy_Report_VictimName.pdf at p. 8)."
- "Defendant had no felony record as of the date of offense (NCIC_Report_2024-04-01.pdf at p. 1)."

If a fact cannot be sourced to a discovery item, mark it `[UNSOURCED — VERIFY]` and flag for follow-up. Do NOT produce any final deliverable that contains unsourced factual claims. Hearsay sourced to a particular discovery document is acceptable IF the source is identified — the attorney can then judge admissibility separately.

For legal authority, follow `dw-shared-protocols-crim/references/louisiana-citation-style.md` (Louisiana citation format). Where this skill lists `[VERIFY CITATION]` against a case name or pinpoint, the citation must be confirmed against current Westlaw or the Louisiana Reports before the deliverable is finalized.

---

## MODULE A — STATUTORY FRAMEWORK (CHARGE-BY-CHARGE)

Read `references/elements-by-statute.md` now for the element breakdown A.1-A.16 of every statute this skill covers (La. R.S. 14:30 through 14:65), each with its conviction-defining hinge and defense angles, plus the statute-to-module index in § 2.

---

## MODULE B — ELEMENT-BY-ELEMENT DEFENSE THEORY MAP

Attack categories: identity, mental state, causation, element-specific definitions, justification / mitigation, defective charging instrument. Read `references/defense-theory-map.md` now for the three defense positions per element, each attack category with its routing, and the four items to document for every contested element.

---

## MODULE C — SPECIFIC INTENT vs. GENERAL INTENT DOCTRINE (CRITICAL)

La. R.S. 14:10 separates specific intent (14:10(1)) from general intent (14:10(2)); the line controls voluntary intoxication (La. R.S. 14:15(2)), diminished capacity, and heat-of-passion mitigation. Read `references/intent-doctrine-by-charge.md` now for the definitions, the charge-by-charge intent map, why the line matters, and the five-step workflow — then build the intent-attack column on the Module B matrix.

---

## MODULE D — SELF-DEFENSE / DEFENSE OF OTHERS

Read `references/self-defense-jury-charges.md` in full before generating any self-defense work product. Framework: La. R.S. 14:18-14:22; no duty to retreat (14:20(C)-(D), charged verbatim); castle / vehicle / business presumption (14:20(B)); the State must DISPROVE self-defense BRD; hybrid reasonableness; aggressor doctrine and withdrawal. Pair with the Module G responsive verdict. The Module D operational guidance (doctrinal points, when to deploy, pretrial motion package) is appended at the end of that file; route to `dw-pretrial-motion-library-crim` and `dw-jury-instructions-builder-crim`.

---

## MODULE E — JUSTIFICATION FRAMEWORK (NECESSITY, DEFENSE OF PROPERTY)

Defense of property (La. R.S. 14:19 non-deadly force only; 14:20 does not extend deadly force to property alone) and necessity / compulsion (La. R.S. 14:18(6), five elements). Read `references/justification-necessity-defense-of-property.md` now for the doctrinal lines, elements, and routing.

---

## MODULE F — FELONY-MURDER DOCTRINE (La. R.S. 14:30(A)(1) and 14:30.1(A)(2))

A homicide during the perpetration of an enumerated felony is murder regardless of intent as to the killing. Attack the underlying felony, the "in the perpetration" nexus (*State v. Anthony*; *State v. Kalathakis*), principal liability (La. R.S. 14:24), and consider severance; heat-of-passion conversion is generally unavailable. Read `references/felony-murder-doctrine.md` now for the rule, enumerated-felony lists, defense angles, and manslaughter calculus.

---

## MODULE G — HEAT OF PASSION / SUDDEN PASSION (Manslaughter as Responsive Verdict)

Read `references/manslaughter-conversion-analysis.md` in full and `references/responsive-verdict-tables.md` § 1–2 before generating any homicide work product.

Sudden passion / heat of blood reduces murder to manslaughter (La. R.S. 14:31(A)(1); *State v. Tompkins*); manslaughter stays on the Art. 814 responsive-verdict form; conversion drops mandatory LWOP to a 40-year max with parole eligibility — the single most consequential strategic outcome in Louisiana criminal practice. The operating rule and checklist highlights are appended at the end of `references/manslaughter-conversion-analysis.md` — read them now and complete the full § 8 checklist for every homicide.

---

## MODULE H — SENTENCING EXPOSURE: DEATH-ELIGIBILITY, MANDATORY LWOP, JUVENILE LWOP, FIREARM ENHANCEMENT

Read `references/sentencing-exposure-matrix.md` for the full table. This module operationalizes the sentencing decisions that drive plea-versus-trial modeling.

Model H.1 death-eligibility (La. C.Cr.P. Arts. 905.2.1, 905.4), H.2 mandatory LWOP, H.3 juvenile LWOP (*Miller* / *Montgomery*; La. C.Cr.P. Art. 878.1), H.4 the La. R.S. 14:64.3 firearm enhancement, and H.5 habitual-offender exposure. The H.1-H.5 guidance is appended at the end of `references/sentencing-exposure-matrix.md` — read it now; route mitigation to `dw-sentencing-mitigation-specialist-crim` and plea modeling to `dw-plea-negotiation-analyzer-crim`.

---

## MODULE I — HABITUAL OFFENDER EXPOSURE ANALYSIS

For every defendant with a prior felony record, build the habitual-exposure spreadsheet, run the seven-step workflow (certified predicates, Boykin, cleansing period under La. R.S. 15:529.1(C), 14:2(B) violent list, scenario modeling), and apply the defense priorities including the *State v. Dorthey* record. Read the Module I section appended at the end of `references/sentencing-exposure-matrix.md` now; route the audit to `dw-habitual-offender-auditor-crim`.

---

## MODULE J — SPECIALIST-RECOMMENDED MOTIONS AND DISCOVERY

Every violent-crime case should generate the following motion package, calibrated to the facts. Route to `dw-pretrial-motion-library-crim` for templates.

Read `references/motions-and-discovery-package.md` now for the full pretrial motion list (severance, suppression, Prieur opposition, autopsy-photograph limine, production motions, Brady/Giglio, bill of particulars, bond), the discovery demands, and the trial-day motions, each with its skill routing.

---

## STEP 3 — OUTPUT FORMAT

All deliverables produced by this skill are internal work product unless the attorney directs otherwise. Apply work-product marking per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`. Output paths anchor on the Cowork Analysis formula:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

### Primary deliverable: Violent-Crime Case Analysis Report (.docx)

Filename: `Violent_Crime_Case_Analysis_{{DEFENDANT_LAST}}_{{DOCKET}}_{{YYYY-MM-DD}}.docx`

Contents: header, twelve numbered sections (case summary; Modules A-J in order, including the sentencing matrix and habitual spreadsheet; recommended next steps and expert needs), and a source-citation appendix. Secondary deliverables (self-defense, manslaughter-conversion, responsive-verdict, sentencing-exposure, habitual-predicate, felony-murder, capital-posture, and juvenile *Miller* memos) are generated as needed. Read `references/output-deliverable-specs.md` now for section contents and secondary-deliverable filenames.

---

## CROSS-SKILL INTEGRATION

This skill feeds the motion library, jury-instructions builder, mitigation specialist, habitual-offender auditor, and cross-exam architect; pairs with the firearms specialist and witness-threat matrix; reads from case brain, discovery tracking, and the evidence auditors; routes to suppression, bond, plea, trial, appellate, and post-conviction skills. Read `references/cross-skill-integration-map.md` now for the full routing map.

---

## GUARDRAILS — NEVER DEVIATE

1. **Do not invent statutes or case law.** Every La. R.S. citation in this skill maps to a real statute. Real cases used: *Miller v. Alabama*, 567 U.S. 460 (2012); *Montgomery v. Louisiana*, 577 U.S. 190 (2016); *Roper v. Simmons*, 543 U.S. 551 (2005); *Graham v. Florida*, 560 U.S. 48 (2010); *Kennedy v. Louisiana*, 554 U.S. 407 (2008); *Strickland v. Washington*, 466 U.S. 668 (1984); *State v. Tompkins*, 403 So.2d 644 (La. 1981) (sudden-passion line); *State v. Anthony*, 427 So.2d 1155 (La. 1983) and *State v. Kalathakis*, 563 So.2d 228 (La. 1990) (felony-murder termination); *State v. Smith*, 327 So.2d 355 (La. 1976) and *State v. Manieri*, 378 So.2d 931 (La. 1979) (inflammatory-photograph limits); *State v. Lee*, 331 So.2d 455 (La. 1976) (victim-character admissibility under La. C.E. Art. 404(A)(2)(a)). For any other Louisiana case, mark `[VERIFY CITATION]` and confirm pinpoint before any deliverable is finalized.
2. **Source Citation Mandate.** Every factual claim about the case ties to a specific discovery item with file name and page/timestamp. Unsourced claims are marked `[UNSOURCED — VERIFY]` and never appear in a final deliverable.
3. **No-duty-to-retreat language must be charged verbatim.** La. R.S. 14:20(C) and (D) — preserve the issue on the record at every charge conference.
4. **Manslaughter responsive verdict must survive on the verdict form** unless the evidence absolutely cannot support sudden-passion / heat-of-blood. Resist State motions to strip it under La. C.Cr.P. Art. 814(C).
5. **Heat-of-passion burden rests on the State.** Once raised by the evidence (from any source, including the State's own witnesses), the State must DISPROVE BRD. Never allow a charge that places a persuasion burden on the defendant.
6. **Felony-murder cases require an attack on the underlying felony.** Heat-of-passion conversion does not work on a true 14:30.1(A)(2) prosecution. Build the felony-attack column in Module B.
7. **Always check for federal adoption.** Where a violent crime has a firearms component, route in parallel to `dw-firearms-specialist-crim` to assess § 924(c) and § 922(g) exposure. Do not assume the case stays in state court.
8. **Always run the habitual-offender predicate audit.** Habitual exposure can transform every line in the sentencing matrix. Build the spreadsheet in Module I early; route to `dw-habitual-offender-auditor-crim`.
9. **Juvenile defendants trigger *Miller / Montgomery* mandatory procedure.** Never plead a juvenile to LWOP without an Art. 878.1 hearing; never accept a sentence that does not preserve parole eligibility absent a permanent-incorrigibility finding.
10. **Capital-posture cases are capital.** If the State signals death-eligibility under La. C.Cr.P. Art. 905.4, immediately escalate to capital-qualified counsel under LIDB standards and begin mitigation investigation in parallel with guilt-phase work.
11. **Do not produce final deliverables without verifying current statutory text.** The Louisiana legislature has revised the homicide, kidnapping, robbery, and habitual-offender statutes repeatedly. Treat the numbers in `references/sentencing-exposure-matrix.md` as starting points and verify against current law.

---

## QUICK REFERENCE — STATUTE-TO-MODULE INDEX

The statute-to-module index is in `references/elements-by-statute.md` § 2 — consult it to locate the analysis for any charged count.

---

## QUICK REFERENCE — STATUTE-AND-CASE CITATIONS USED

Every statute and case this skill relies on — with verification status and the caveat on the unattributed "mere words" and sudden-passion-burden doctrines — is listed in `references/citations-used.md`. Read it before finalizing any deliverable; verify current statutory text against Westlaw.

---

## CHECKLIST FOR CASE COMPLETION

Read `references/case-completion-checklist.md` now and confirm every item before closing the analysis.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **case-completion-checklist.md** — Checklist for Case Completion; step- and module-level close-out items
- **citations-used.md** — Quick Reference: statutes and cases used, with verification status and caveats
- **cross-skill-integration-map.md** — Cross-Skill Integration; what this skill feeds, pairs with, reads from, routes to
- **defense-theory-map.md** — Module B; categories of attack and per-element documentation requirements
- **elements-by-statute.md** — Module A; elements A.1-A.16 for every covered statute; § 2 statute-to-module index
- **felony-murder-doctrine.md** — Module F; operational rule, enumerated felonies, defense angles, manslaughter calculus
- **information-gathering-checklist.md** — Step 1; minimum case-context dataset from `dw-case-brain-crim`, with routing
- **intent-doctrine-by-charge.md** — Module C; La. R.S. 14:10 definitions, charge-by-charge intent map, workflow
- **justification-necessity-defense-of-property.md** — Module E; defense-of-property line and necessity elements
- **manslaughter-conversion-analysis.md** — Module G; heat-of-passion conversion playbook (La. R.S. 14:31(A)(1)) as responsive verdict to murder; Module G operating rule appended
- **motions-and-discovery-package.md** — Module J; pretrial motions, discovery demands, trial-day motions with routing
- **output-deliverable-specs.md** — Step 3 Output Format; report section contents and secondary-deliverable filenames
- **responsive-verdict-tables.md** — Module G; responsive verdicts under La. C.Cr.P. Art. 814 for homicide, battery, kidnapping, robbery, burglary
- **self-defense-jury-charges.md** — Module D; self-defense / defense-of-others jury charges, no-duty-to-retreat under La. R.S. 14:20(C); Module D operational guidance appended
- **sentencing-exposure-matrix.md** — Modules H and I; mandatory minimums, maximums, parole eligibility, 14:64.3 enhancement, 15:529.1 multipliers; Module H and Module I guidance appended
