---
name: dw-violent-crime-specialist-crim
category: offense-specialists
description: >
  Violent-crime defense framework for Louisiana state prosecutions. ALWAYS invoke for "homicide,"
  "murder," "first degree murder," "second degree murder," "manslaughter," "negligent homicide,"
  "heat of passion," "sudden passion," "self-defense," "stand your ground," "no duty to retreat,"
  "justifiable homicide," "defense of others," "felony murder," "aggravated battery," "second degree
  battery," "battery on a police officer," "aggravated assault," "aggravated kidnapping," "second
  degree kidnapping," "aggravated burglary," "home invasion," "armed robbery," "first degree robbery,"
  "simple robbery," "firearm enhancement on robbery," "R.S. 14:30," "R.S. 14:30.1," "R.S. 14:31,"
  "R.S. 14:32," "R.S. 14:34," "R.S. 14:34.1," "R.S. 14:34.5," "R.S. 14:37," "R.S. 14:44,"
  "R.S. 14:44.1," "R.S. 14:60," "R.S. 14:62.8," "R.S. 14:64," "R.S. 14:64.1," "R.S. 14:64.3,"
  "R.S. 14:65," "Miller hearing," "Montgomery v. Louisiana," "juvenile LWOP," "responsive verdict,"
  "Article 814," or "death-eligible." Do NOT use for sex offenses (use dw-sex-offense-specialist-crim),
  drug offenses (use dw-drug-offense-specialist-crim), DWI (use dw-dwi-specialist-crim), or standalone gun
  charges (use dw-firearms-specialist-crim) — but DO use this skill when a violent crime is the lead
  charge and a firearm is the instrumentality.
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

## STEP 1 — INFORMATION GATHERING PROTOCOL

Use `dw-case-brain-crim` to pull the structured case context. The minimum dataset for this skill is:

- Defendant demographics (age at offense, age at indictment, mental health history).
- Victim identity, age, relationship to defendant, prior history.
- Charged statutes and any responsive-verdict architecture already preserved.
- Death-eligibility posture (has the State filed notice under La. C.Cr.P. Art. 905.2.1?).
- Discovery production index — autopsy report, 911 audio, body-worn camera, scene photos, ballistics, lab work, witness statements, jail calls, social media.
- Prior felony record (with conviction documents available for predicate audit).
- Co-defendant status and any cooperator agreements (route to `dw-brady-giglio-auditor-crim`).
- Crime-scene reconstruction status (route to `dw-crime-scene-auditor-crim`).
- Pretrial motion status (Prieur, severance, motions in limine — route to `dw-pretrial-motion-library-crim`).
- Existing defense theory drafts (route from `dw-case-brain-crim` and any prior memos).

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

The State's prima facie burden differs by charge. Build the element grid for every count in the indictment. Use the matrix in `references/sentencing-exposure-matrix.md` for the exposure side; use this module for the elements side.

### A.1 — La. R.S. 14:30 (First Degree Murder)

Specific intent to kill or inflict great bodily harm AND one or more enumerated aggravating circumstances under La. R.S. 14:30(A) (e.g., killing during the perpetration or attempted perpetration of an enumerated felony — armed robbery, aggravated kidnapping, aggravated burglary, aggravated rape, etc.; killing of a peace officer engaged in lawful duties; killing more than one person; killing of a victim under 12 or over 65; offered or received remuneration). Capital procedures attach if the State invokes them per La. C.Cr.P. Art. 905.4.

### A.2 — La. R.S. 14:30.1 (Second Degree Murder)

Two distinct prongs:
- 14:30.1(A)(1) — specific intent to kill or to inflict great bodily harm.
- 14:30.1(A)(2) — felony-murder: a homicide committed during the perpetration or attempted perpetration of an enumerated felony, regardless of intent. The list includes armed robbery, aggravated kidnapping, aggravated burglary, aggravated arson, drive-by shooting, certain drug offenses, and others. See Module F.

Mandatory life without benefit of parole, probation, or suspension of sentence.

### A.3 — La. R.S. 14:31 (Manslaughter)

Two distinct prongs:
- 14:31(A)(1) — sudden passion / heat of blood. See Module G; see `references/manslaughter-conversion-analysis.md`.
- 14:31(A)(2) — homicide committed without intent to cause death or great bodily harm during enumerated felonies/misdemeanors not on the second-degree-murder list, OR while resisting lawful arrest.

### A.4 — La. R.S. 14:32 (Negligent Homicide)

Killing of a human being by criminal negligence. La. R.S. 14:12 defines criminal negligence as a gross deviation from the standard of care.

### A.5 — La. R.S. 14:34 (Aggravated Battery)

Battery (intentional use of force or violence on another person, La. R.S. 14:33) committed with a dangerous weapon. The "dangerous weapon" element under La. R.S. 14:2(3) includes any instrumentality that, in the manner used, is calculated or likely to produce death or great bodily harm. Defense angles: was the object actually a "dangerous weapon" in the manner used? Was the contact actually a battery (intentional vs. reckless)?

### A.6 — La. R.S. 14:34.1 (Second Degree Battery)

Battery committed without consent of the victim when the offender intentionally inflicts serious bodily injury. La. R.S. 14:34.1(B) defines "serious bodily injury" — substantial risk of death, extreme physical pain, protracted disfigurement, etc. The intent element here is critical: the State must prove the defendant intended to inflict serious bodily injury, not merely that serious bodily injury resulted.

### A.7 — La. R.S. 14:34.5 (Battery on a Peace Officer)

Battery committed without the consent of the victim when the offender has reasonable grounds to believe the victim is a peace officer acting in the performance of his duty. The "reasonable grounds" element opens identification and uniform-recognition challenges. Verify the current subsection-specific minimums and parole restrictions in `references/sentencing-exposure-matrix.md`.

### A.8 — La. R.S. 14:37 (Aggravated Assault)

Assault (intentional placing of another in reasonable apprehension of receiving a battery, La. R.S. 14:36) committed with a dangerous weapon. La. R.S. 14:37.4 (firearm-aggravated assault) is a separate felony. Verify which subsection applies.

### A.9 — La. R.S. 14:44 (Aggravated Kidnapping)

The forcible seizing and carrying of any person from one place to another (or the enticing or persuading of any person to go from one place to another, or the imprisoning or forcible secreting of any person) with the intent to force the victim, or some other person, to give up anything of apparent present or prospective value, or to grant any advantage or immunity, in order to secure a release of the person under the offender's actual or apparent control. The "ransom or thing of value" element is the conviction-defining hinge.

### A.10 — La. R.S. 14:44.1 (Second Degree Kidnapping)

The forcible seizing and carrying or enticing or imprisoning of a person under enumerated aggravating circumstances (the victim is used as a shield or hostage; the victim is used to facilitate the commission of a felony or flight; armed with a dangerous weapon; the victim is wounded or injured; the victim is sexually abused). Lower exposure than 14:44 but still substantial — see matrix.

### A.11 — La. R.S. 14:60 (Aggravated Burglary)

Unauthorized entering of any inhabited dwelling, or of any structure, water craft, or movable where a person is present, with the intent to commit a felony or any theft therein, AND any one of three aggravators: (1) the offender is armed with a dangerous weapon; (2) after entering, the offender arms himself with a dangerous weapon; (3) the offender commits a battery upon any person while in the structure or in entering or leaving.

### A.12 — La. R.S. 14:62.8 (Home Invasion)

Unauthorized entering of any inhabited dwelling, or of any structure belonging to another and used in whole or in part as a home or place of abode by a person, where a person is present, with the intent to use force or violence upon the person of another or to vandalize, deface, or damage the property of another. Aggravators (presence of children under 12, elderly persons, dangerous weapon) raise the exposure.

### A.13 — La. R.S. 14:64 (Armed Robbery)

The taking of anything of value belonging to another, from the person of another or that is in the immediate control of another, by use of force or intimidation, while armed with a dangerous weapon. All three elements are litigation-rich: was something "of value" actually taken or attempted? Was force or intimidation used (not just trickery)? Was the offender armed with a dangerous weapon (live or simulated)? See A.15 for the 14:64.3 firearm enhancement.

### A.14 — La. R.S. 14:64.1 (First Degree Robbery)

The taking of anything of value belonging to another, from the person of another or in the immediate control of another, by use of force or intimidation, when the offender leads the victim to reasonably believe he is armed with a dangerous weapon. The "reasonable belief" standard (vs. the actual-armed standard of 14:64) is the principal off-ramp from armed robbery. Toy guns, simulated weapons, and concealed-hand pretenses convict on 14:64.1, not 14:64.

### A.15 — La. R.S. 14:64.3 (Firearm Enhancement on Armed Robbery)

If the dangerous weapon used in an armed robbery was a firearm, the court SHALL impose an additional 5 years at hard labor without benefit, to be served consecutively to the underlying 14:64 sentence. Defense angles: (i) attack the firearm characterization (was it operable? was it actually a firearm vs. a replica?); (ii) push for the 14:64.1 responsive verdict, which moots 14:64.3 entirely; (iii) verify that the State actually charged 14:64.3 in the indictment — the enhancement must be charged and proved, not added at sentencing.

### A.16 — La. R.S. 14:65 (Simple Robbery)

Taking of anything of value from the person or immediate control of another, by use of force or intimidation, but NOT armed with a dangerous weapon. The misdemeanor-of-felonies in this tier — 7-year max, parole-eligible.

---

## MODULE B — ELEMENT-BY-ELEMENT DEFENSE THEORY MAP

For each charged count, build a column-by-column attack matrix. The defense position on each element is one of: (1) State cannot prove this element BRD; (2) defense will concede this element; (3) the element is contested and will be a jury question.

Standard categories of attack:

- **Identity.** Was the defendant the offender? Eyewitness ID under *State v. Hunt* / *Manson v. Brathwaite* reliability factors — route to `dw-eyewitness-identification-auditor-crim`. Surveillance video clarity. DNA / fingerprint chain. Co-defendant blame-shifting and *Bruton* problems.
- **Mental state.** Specific vs. general intent (Module C). Voluntary intoxication (specific-intent offenses only — La. R.S. 14:15). Mental defect short of insanity (diminished capacity — narrow doctrine in Louisiana; route to mitigation if not exoneration).
- **Causation.** Did the defendant's act cause the harm? Independent intervening causes — medical malpractice in homicide cases, third-party intervening violence, victim's own conduct.
- **Element-specific definitions.** "Dangerous weapon" (14:2(3)) — was the object calculated or likely to produce death or GBH in the manner used? "Serious bodily injury" (14:34.1(B)) — does the actual injury meet the statutory threshold? "Reasonable belief" (14:64.1) vs. actual armed (14:64).
- **Justification / mitigation.** Self-defense (Module D). Defense of others (Module D). Necessity / defense of property (Module E). Heat of passion (Module G).
- **Defective charging instrument.** Bill of information ambiguities, multiplicity, duplicity — route to `dw-pretrial-motion-library-crim`.

For every contested element, document:
- The State's likely proof (witness, exhibit, circumstantial inference).
- The defense counter-proof (cross-exam, contrary witness, exhibit).
- The cite to the discovery item supporting both sides.
- The closing-argument framing.

---

## MODULE C — SPECIFIC INTENT vs. GENERAL INTENT DOCTRINE (CRITICAL)

Louisiana's intent doctrine is the keystone of every homicide and most violent-crime defenses. La. R.S. 14:10 distinguishes:

- **Specific criminal intent (La. R.S. 14:10(1))** — the state of mind that exists when the circumstances indicate that the offender actively desired the prescribed criminal consequences to follow his act.
- **General criminal intent (La. R.S. 14:10(2))** — the state of mind that exists when the offender, in the ordinary course of human experience, must have adverted to the prescribed criminal consequences as reasonably certain to result from his act or failure to act.

### Charge-by-charge intent map

- **First degree murder (14:30)** — specific intent to kill OR inflict GBH (as to (A)(1) variant). Felony-murder variants do not require specific intent as to the killing — but they require the specific intent (or general intent, depending on the felony) of the underlying offense.
- **Second degree murder (14:30.1(A)(1))** — specific intent to kill OR inflict GBH.
- **Second degree murder (14:30.1(A)(2))** — felony-murder. No specific intent to kill required; the intent of the underlying enumerated felony is imputed.
- **Manslaughter (14:31(A)(1))** — what would otherwise be murder but for sudden passion / heat of blood. Specific-intent floor, with mitigation.
- **Negligent homicide (14:32)** — criminal negligence (14:12); no intent to kill required.
- **Aggravated battery (14:34)** — general intent to use force; the "dangerous weapon" element does not require specific intent as to the weapon's character.
- **Second degree battery (14:34.1)** — specific intent to inflict serious bodily injury.
- **Aggravated assault (14:37)** — general intent to place another in reasonable apprehension.
- **Aggravated kidnapping (14:44)** — specific intent (the "in order to secure release" element imports specific intent to extract value or advantage).
- **Aggravated burglary (14:60)** — specific intent to commit a felony or theft inside (the entry intent).
- **Home invasion (14:62.8)** — specific intent to use force or violence or to vandalize.
- **Armed robbery (14:64)** — specific intent to take from the person.
- **Simple robbery (14:65)** — same.

### Why the line matters

- **Voluntary intoxication is a defense to specific-intent offenses only (La. R.S. 14:15(2))**. If the defendant was so intoxicated as to preclude formation of specific intent, the offense reduces (e.g., murder to manslaughter or negligent homicide; aggravated burglary to unauthorized entry; armed robbery to theft).
- **Diminished capacity (mental defect short of insanity)** can negate specific intent in Louisiana, though the doctrine is narrow and admissibility of expert testimony is contested. La. C.E. Art. 704 prohibits an expert in a criminal case from expressing an opinion on the guilt or innocence of the accused, which constrains how directly an expert can opine on intent.
- **Heat of passion (Module G)** is, in effect, a specific-intent mitigation rule — it admits the specific intent but argues the surrounding mental state reduces the grade of the offense.

### Practical workflow

1. Identify the intent element of every count.
2. Identify the discovery support for and against the State's intent proof (statements, prior conduct, planning evidence, weapon possession patterns).
3. Identify any admissibility-of-mental-state evidence (expert reports, intoxication evidence, prior-acts evidence about the victim that bears on the defendant's perception).
4. Build the intent-attack column on the matrix in Module B.
5. Cross-reference Module G when the case involves any provocation — heat of passion is the standard intent-mitigation play for homicides.

---

## MODULE D — SELF-DEFENSE / DEFENSE OF OTHERS

Read `references/self-defense-jury-charges.md` in full before generating any self-defense work product. The summary below is operational guidance only.

### Statutory framework

- La. R.S. 14:18 — justification (umbrella).
- La. R.S. 14:19 — non-deadly force.
- La. R.S. 14:20 — justifiable homicide (deadly force).
- La. R.S. 14:21 — aggressor doctrine.
- La. R.S. 14:22 — defense of others.

### Critical doctrinal points

- **No duty to retreat (La. R.S. 14:20(C))**. A person not engaged in unlawful activity, in a place where he has a right to be, may stand his ground and meet force with force. La. R.S. 14:20(D) bars the trier of fact from considering the possibility of retreat as a factor in reasonableness. This must be charged verbatim — see `references/self-defense-jury-charges.md`.
- **Castle / vehicle / business presumption (La. R.S. 14:20(B))**. The law presumes the homicide actor had a reasonable belief deadly force was necessary when the victim was an unlawful intruder.
- **Burden architecture.** Once self-defense is at issue (low production threshold; State's evidence often raises it), the State must DISPROVE self-defense BRD. The defendant does NOT carry a persuasion burden. See `references/self-defense-jury-charges.md` § 5.
- **Reasonableness is hybrid.** Subjective belief of the defendant AND objective reasonableness from a person in the defendant's circumstances. Prior victim-on-defendant violence known to the defendant is admissible.
- **Aggressor doctrine and withdrawal (La. R.S. 14:21).** Mere words cannot make a person the aggressor. Withdrawal must be communicated or knowable to the adversary.

### When to deploy

Self-defense is the standard primary theory in:
- Domestic violence killings where the defendant is the long-term abuse victim.
- Bar / public-place altercations where the victim displayed a weapon or threw the first blow.
- Home / vehicle / business intrusion cases (castle presumption applies).
- Cases where the victim had a prior history of violence known to the defendant.

Self-defense should be paired with the heat-of-passion responsive verdict (Module G) so that even if the jury rejects justification, the defense lands on manslaughter rather than murder.

### Pretrial motion package

- Motion in limine to admit prior victim acts of violence known to the defendant (reasonableness).
- Motion in limine to admit prior threats (charged or uncharged) by the victim against the defendant.
- Prieur (404B) opposition — the State will try to introduce defendant's prior bad acts to negate self-defense; resist on relevance and prejudice grounds.
- Motion to compel discovery of all 911 calls, BWC, CAD reports, prior DV reports, and victim's criminal history.

Route to `dw-pretrial-motion-library-crim` for templates; route to `dw-jury-instructions-builder-crim` for the charge package.

---

## MODULE E — JUSTIFICATION FRAMEWORK (NECESSITY, DEFENSE OF PROPERTY)

### Defense of property

La. R.S. 14:19 permits non-deadly force in defense of property in a person's lawful possession. La. R.S. 14:20 does NOT extend deadly force to defense of property alone — deadly force requires a threat to life or great bodily harm, or unlawful entry under the castle provisions. The line is critical: a defendant who used deadly force against a fleeing burglar with no threat to person cannot rely on defense of property. The case may still survive on heat-of-passion mitigation (Module G) or, in the right facts, on the (A)(2) prevention-of-forcible-felony branch of La. R.S. 14:20.

### Necessity

Louisiana recognizes a narrow common-law necessity doctrine and a statutory analogue under La. R.S. 14:18(6) (compulsion / coercion by threat of immediate death or great bodily harm). Genuine necessity defenses in violent-crime cases are rare; the more common application is in escape, weapons, and traffic cases. Where a violent-crime case truly fits, the elements are:
- Imminent harm.
- No reasonable legal alternative.
- Direct causal link between the conduct and the avoidance of harm.
- The harm avoided was greater than the harm caused.
- The defendant did not bring on the situation.

If a necessity theory is being raised, document the elements with discovery citations and route to `dw-pretrial-motion-library-crim` for any motion in limine to admit the supporting evidence.

---

## MODULE F — FELONY-MURDER DOCTRINE (La. R.S. 14:30(A)(1) and 14:30.1(A)(2))

### Operational rule

A homicide committed during the perpetration or attempted perpetration of an enumerated felony is murder, regardless of the killer's specific intent as to the killing. The State proves the underlying felony and proves the killing occurred "in the perpetration"; the homicide intent piece is imputed.

### Enumerated felonies

The list is statute-specific:
- **First degree murder (14:30(A)(1))** lists armed robbery, aggravated kidnapping, aggravated burglary, aggravated rape, aggravated arson, aggravated escape, drive-by shooting, and others. Confirm against current statutory text.
- **Second degree murder (14:30.1(A)(2))** lists a slightly different (and historically narrower or broader, depending on amendment cycle) set. Confirm against current statutory text.

### Defense angles

- **Was the underlying felony actually perpetrated or attempted?** If the State cannot prove the felony, the felony-murder theory collapses. (E.g., if the State charges 14:30.1(A)(2) on an armed-robbery predicate but the jury would acquit on the armed-robbery count, the homicide drops to 14:30.1(A)(1) — which now must be proved on specific intent — or further to manslaughter / negligent homicide.)
- **Was the killing "in the perpetration" or an independent intervening event?** The temporal and causal nexus between the felony and the homicide is contested. *State v. Anthony*, 427 So.2d 1155 (La. 1983) (flight after a completed burglary not part of res gestae) and *State v. Kalathakis*, 563 So.2d 228 (La. 1990) frame when the felony has terminated (e.g., when the perpetrator has reached a place of temporary safety).
- **Was the defendant a principal under La. R.S. 14:24?** If the homicide was committed by a co-defendant during the felony, the defendant is liable as a principal — but only for offenses for which he had the requisite intent. The Louisiana Supreme Court has wrestled with the *Pinkerton*-style imputation; the current rule requires that the homicide be a foreseeable consequence of the felony as the defendant participated in it.
- **Was the felony "inherently dangerous"?** Louisiana applies the enumerated-felony rule, not the inherently-dangerous-felony rule of common-law jurisdictions, but the foreseeability question still bites at the principals stage.
- **Sever the homicide count from the felony count?** Sometimes useful where the felony evidence is weak and the State is relying on cumulation; route to `dw-pretrial-motion-library-crim` for a severance motion.

### Manslaughter conversion in felony-murder cases

Heat-of-passion conversion is generally NOT available to a true felony-murder count, because the defendant's emotional state is not what the State must prove. The defense must instead attack the felony or attack the "in the perpetration" link. La. R.S. 14:31(A)(2) felony-manslaughter remains available where the underlying felony is not on the second-degree-murder list. See `references/manslaughter-conversion-analysis.md` § 7.

---

## MODULE G — HEAT OF PASSION / SUDDEN PASSION (Manslaughter as Responsive Verdict)

Read `references/manslaughter-conversion-analysis.md` in full and `references/responsive-verdict-tables.md` § 1–2 before generating any homicide work product.

The two-paragraph operating rule:

A homicide that would otherwise be murder under La. R.S. 14:30 or 14:30.1(A)(1) reduces to manslaughter when committed in sudden passion or heat of blood immediately caused by provocation sufficient to deprive an average person of self-control and cool reflection. Sudden passion and heat of blood are not elements of manslaughter; they are mitigatory factors that the defendant must establish by a preponderance to be entitled to a manslaughter verdict. *State v. Tompkins*, 403 So.2d 644 (La. 1981). Cooling-off is a jury question.

Manslaughter is on the responsive-verdict form for first or second degree murder by operation of La. C.Cr.P. Art. 814 (see `references/responsive-verdict-tables.md` § 1–2). The defense should resist any State motion to strike manslaughter from the verdict form and should propose manslaughter-conversion language for the charge.

A manslaughter conversion drops a mandatory LWOP (or death-eligible) sentence to a 40-year max with parole and probation eligibility — the single most consequential strategic outcome in Louisiana criminal practice.

### Conversion checklist

For every homicide case, complete the checklist in `references/manslaughter-conversion-analysis.md` § 8. Highlights:
- Provocative-act timeline with discovery citations.
- Defendant's emotional state at first contact.
- Cooling-off analysis.
- Self-defense overlap (the same provocation often supports both theories).
- Charge-conference proposal.
- Two-track closing.

---

## MODULE H — SENTENCING EXPOSURE: DEATH-ELIGIBILITY, MANDATORY LWOP, JUVENILE LWOP, FIREARM ENHANCEMENT

Read `references/sentencing-exposure-matrix.md` for the full table. This module operationalizes the sentencing decisions that drive plea-versus-trial modeling.

### H.1 — Death-eligibility (La. R.S. 14:30)

If the State has filed (or signaled) a notice of intent to seek the death penalty under La. C.Cr.P. Art. 905.2.1, the case enters capital posture:
- Voir dire is *Witherspoon / Witt*-qualified.
- Mitigation investigation begins immediately — route to `dw-sentencing-mitigation-specialist-crim`.
- Independent capital-qualified counsel rules apply (Louisiana Indigent Defender Board capital standards).
- Aggravating-circumstance theory must be matched element-by-element against La. C.Cr.P. Art. 905.4.
- Plea negotiations must include LWOP-vs.-death modeling.

### H.2 — Mandatory LWOP (La. R.S. 14:30.1; 14:44; non-capital 14:30)

LWOP cases compress all of the trial-defense effort into the verdict-form architecture. There is no sentencing mitigation that softens the LWOP outcome — the only way out is acquittal, manslaughter conversion, or charge reduction by plea. Route to `dw-plea-negotiation-analyzer-crim` for plea modeling.

### H.3 — Juvenile LWOP (*Miller v. Alabama* / *Montgomery v. Louisiana*)

For any defendant under 18 at the time of the offense:
- *Miller v. Alabama*, 567 U.S. 460 (2012) — mandatory LWOP for juvenile homicide offenders is unconstitutional. Individualized hearing required.
- *Montgomery v. Louisiana*, 577 U.S. 190 (2016) — *Miller* is retroactive on collateral review. Confirms a substantive Eighth Amendment rule.
- La. C.Cr.P. Art. 878.1 — Louisiana's *Miller* hearing procedure. Without an Art. 878.1 finding of permanent incorrigibility, the juvenile must be parole-eligible (typically after 25 years of service per La. R.S. 15:574.4).
- *Roper v. Simmons*, 543 U.S. 551 (2005) — bars death penalty for juvenile offenders.
- *Graham v. Florida*, 560 U.S. 48 (2010) — bars LWOP for non-homicide juvenile offenders (relevant to 14:44 aggravated kidnapping if applied to a juvenile).

Mitigation investigation for the Art. 878.1 hearing requires neuropsychological evaluation, school records, family-history mitigation, brain-development science. Route to `dw-sentencing-mitigation-specialist-crim`.

### H.4 — Firearm enhancement on armed robbery (La. R.S. 14:64.3)

5 years consecutive, without benefit, on top of the 10-99 year armed-robbery sentence. Triggers when the dangerous weapon was a firearm. Defense angles:
- Push for 14:64.1 first-degree-robbery responsive verdict (eliminates 14:64.3 entirely).
- Challenge the "firearm" characterization (replica? inoperable? simulated?).
- Verify the State actually charged 14:64.3 — the enhancement must be charged and proved.

### H.5 — Habitual offender (La. R.S. 15:529.1)

See Module I and `references/sentencing-exposure-matrix.md` § 5. Build the predicate audit early — habitual exposure can transform a 7-year simple-robbery floor into a life-without-benefit ceiling.

---

## MODULE I — HABITUAL OFFENDER EXPOSURE ANALYSIS

For every defendant with a prior felony record, build the habitual-exposure spreadsheet:

| # | Predicate offense | Statute | Date of conviction | Date sentence completed | On 14:2(B) violent list? | Within cleansing period? | Boykin colloquy verified? | Predicate quality |
|---|---|---|---|---|---|---|---|---|

Workflow:
1. Pull all certified conviction documents (route to `dw-habitual-offender-auditor-crim` for the audit).
2. Verify each predicate is actually a felony of conviction (not deferred adjudication; not expunged; not vacated).
3. Verify each predicate's Boykin colloquy was constitutional (right to counsel, right to jury trial, right against self-incrimination — defendant must have been advised and waived knowingly and voluntarily).
4. Verify cleansing period (La. R.S. 15:529.1(C)) — confirm current length, which has changed across recent sessions.
5. Determine which (if any) predicates are on the violent-felony list (La. R.S. 14:2(B)) — drives the cascade to mandatory life under third- or fourth-felony enhancement.
6. Model the post-enhancement exposure for each scenario (no bill, second-felony bill, third-felony bill with violent predicate, etc.).
7. Feed the model into `dw-plea-negotiation-analyzer-crim` for plea-versus-trial decision.

Defense priorities:
- **Attack each predicate's validity** (Boykin, expungement, identity).
- **Negotiate a no-bill** as part of plea structure where possible.
- **Object to the enhancement charge** if the prosecution missed a procedural step (timely filing of the bill, proper service, hearing requirements under La. R.S. 15:529.1(D)).
- **Document the constitutional minimum** — under *State v. Dorthey*, an enhancement that is constitutionally excessive (grossly disproportionate) can be reduced. Build the *Dorthey* record at sentencing.

---

## MODULE J — SPECIALIST-RECOMMENDED MOTIONS AND DISCOVERY

Every violent-crime case should generate the following motion package, calibrated to the facts. Route to `dw-pretrial-motion-library-crim` for templates.

### Pretrial motions (filed)

- **Motion for severance (La. C.Cr.P. Art. 704; multi-count) and Art. 704 (multi-defendant).** Particularly where one count's evidence (e.g., a felony-murder predicate) would be substantially more prejudicial than probative as to a separate count or co-defendant.
- **Motion to suppress identification.** *Manson v. Brathwaite* / *State v. Hunt* reliability factors. Route to `dw-eyewitness-identification-auditor-crim`.
- **Motion to suppress statements / Jackson-Denno hearing.** *Miranda*, voluntariness, custody analysis. Route to `dw-confession-interrogation-auditor-crim`.
- **Motion to suppress physical evidence.** Search-and-seizure challenges. Route to `dw-suppression-motion-crim`.
- **Prieur motion (404B) — opposition.** State will try to introduce prior bad acts to prove identity, motive, or to negate self-defense. Resist on relevance and prejudice. Route to `dw-404b-opposition-crim`.
- **Motion in limine on injury / autopsy photographs.** Inflammatory-photograph limits — *State v. Smith*, 327 So.2d 355 (La. 1976); *State v. Manieri*, 378 So.2d 931 (La. 1979) (probative value vs. prejudicial effect; require necessity findings). Push for cropped or sketch alternatives.
- **Motion for production of ballistics records and chain of custody.** Crime-lab personnel files; equipment calibration; comparison microscopy bench notes.
- **Motion for production of full autopsy file.** Toxicology, gross dissection notes, photographs, ME's prior testimony — pull cause-of-death attack.
- **Motion for 911 audio and CAD records.** Excited utterances, dispatcher comments, complainant identity. Often supports heat-of-passion or self-defense.
- **Motion for full body-worn camera production.** Pre- and post-event footage; defendant's emotional state at first contact (heat of passion).
- **Brady / Giglio demand.** All impeachment material on State witnesses, including informant deals, prior false statements. Route to `dw-brady-giglio-auditor-crim`.
- **Motion for bill of particulars.** Specify the underlying felony for any felony-murder count, identify the dangerous weapon, identify the alleged battery for 14:60(B)(3), etc.
- **Motion for bond reduction / release on conditions.** Route to `dw-bond-and-release-motion-crim`.

### Discovery demands (informal and formal)

- All scene photographs and video.
- Full medical records of victim (treatment, prior injuries, mental health if reasonableness-relevant).
- Prior CAD / police reports involving victim and defendant (DV history, prior threats).
- Cell phone forensic dumps (defendant's, victim's if available). Route to `dw-mobile-forensic-auditor-crim` and `dw-forensic-dump-analyzer-crim`.
- Jail call recordings — review for any defendant statements bearing on intent or self-defense, and for State-witness contamination. Route to `dw-jail-call-analyzer-crim`.
- Social media records (subpoena where appropriate). Route to `dw-social-media-auditor-crim`.
- Co-defendant statements and any cooperation agreements.
- Witness criminal histories.
- Officer disciplinary records (where relevant).

### Trial-day motions

- Motion to strike improper responsive-verdict removal at the charge conference.
- Motion in limine on closing-argument language (no improper "retreat" framing; no improper victim-character framing).
- Motion for judgment of acquittal at the close of the State's case (La. C.Cr.P. Art. 821).

---

## STEP 3 — OUTPUT FORMAT

All deliverables produced by this skill are internal work product unless the attorney directs otherwise. Apply work-product marking per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`. Output paths anchor on the Cowork Analysis formula:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

### Primary deliverable: Violent-Crime Case Analysis Report (.docx)

Filename: `Violent_Crime_Case_Analysis_{{DEFENDANT_LAST}}_{{DOCKET}}_{{YYYY-MM-DD}}.docx`

Contents:
1. Header — work-product marking, defendant, docket, parish/court, date, attorney.
2. Section 1 — Case summary. Charges, facts, posture, jurisdictional notes (state-only here; if federal exposure exists, route also to `dw-firearms-specialist-crim`).
3. Section 2 — Charge-by-charge statutory framework (Module A) with element grid.
4. Section 3 — Element-by-element defense theory map (Module B).
5. Section 4 — Specific vs. general intent analysis (Module C).
6. Section 5 — Self-defense / defense-of-others assessment (Module D), including no-duty-to-retreat language and pattern-charge proposals.
7. Section 6 — Justification / necessity / defense of property (Module E), if applicable.
8. Section 7 — Felony-murder analysis (Module F), if applicable.
9. Section 8 — Heat-of-passion / manslaughter conversion (Module G), with provocation timeline and conversion checklist.
10. Section 9 — Sentencing exposure matrix (Module H) per `references/sentencing-exposure-matrix.md`. Include juvenile *Miller* posture, capital posture, 14:64.3, mandatory LWOP, and habitual scenarios.
11. Section 10 — Habitual-offender exposure spreadsheet (Module I).
12. Section 11 — Motion and discovery checklist (Module J), with routing assignments to other D&W skills.
13. Section 12 — Recommended next steps (in priority order) and expert needs (medical examiner cross-prep, ballistics expert, mental-state expert, mitigation specialist).
14. Source-citation appendix — every factual claim mapped to its discovery citation.

### Secondary deliverables (generated as needed)

- **Self-Defense Analysis Memo** — if self-defense or defense-of-others is in play. Filename: `Self_Defense_Analysis_{{DEFENDANT_LAST}}_{{YYYY-MM-DD}}.docx`. Tracks `references/self-defense-jury-charges.md`.
- **Manslaughter Conversion Memo** — for any homicide case. Filename: `Manslaughter_Conversion_{{DEFENDANT_LAST}}_{{YYYY-MM-DD}}.docx`. Tracks `references/manslaughter-conversion-analysis.md`.
- **Responsive-Verdict Strategy Memo** — verdict-form architecture with proposed charges. Tracks `references/responsive-verdict-tables.md`.
- **Sentencing Exposure Memo** — detailed exposure modeling for plea negotiations. Tracks `references/sentencing-exposure-matrix.md`.
- **Habitual-Offender Predicate Audit** — generated jointly with `dw-habitual-offender-auditor-crim`.
- **Felony-Murder Defense Memo** — if any 14:30(A)(1) or 14:30.1(A)(2) felony-murder count is charged.
- **Capital Posture Memo** — if the State has signaled or filed capital intent.
- **Juvenile *Miller* / Art. 878.1 Memo** — if the defendant was under 18 at the offense.

---

## CROSS-SKILL INTEGRATION

### This skill FEEDS:

- `dw-pretrial-motion-library-crim` — the motion-and-discovery checklist (Module J) seeds template selection.
- `dw-jury-instructions-builder-crim` — verdict-form architecture, pattern-charge proposals, no-duty-to-retreat language, manslaughter-conversion charges.
- `dw-sentencing-mitigation-specialist-crim` — death-eligibility mitigation, *Miller* mitigation, Art. 893 analysis where available, *Dorthey* excessive-sentence record.
- `dw-habitual-offender-auditor-crim` — predicate audit, no-bill negotiation strategy.
- `dw-cross-exam-architect-crim` — element-by-element cross-exam outlines for State witnesses, medical examiner, ballistics expert.

### This skill PAIRS WITH:

- `dw-firearms-specialist-crim` — when a firearm is the instrumentality of the violent crime (most armed-robbery and many homicide cases). The 14:64.3 enhancement is litigated jointly.
- `dw-witness-threat-matrix-crim` — domestic-violence and gang-related cases where witness intimidation, recantation, and family pressure shape the trial posture.

### This skill READS FROM:

- `dw-case-brain-crim` — structured case context.
- `dw-discovery-orchestrator-crim` and `dw-discovery-compliance-monitor-crim` — discovery tracking and deficiency detection.
- `dw-eyewitness-identification-auditor-crim` — ID reliability evaluation.
- `dw-confession-interrogation-auditor-crim` — *Miranda* / voluntariness audit.
- `dw-crime-scene-auditor-crim` — scene reconstruction.
- `dw-mobile-forensic-auditor-crim` and `dw-forensic-dump-analyzer-crim` — phone evidence.
- `dw-jail-call-analyzer-crim` — recorded calls.
- `dw-brady-giglio-auditor-crim` — impeachment file.
- `dw-404b-opposition-crim` — Prieur opposition work.

### This skill ROUTES TO (after case analysis):

- `dw-suppression-motion-crim` — for any 4A challenge.
- `dw-bond-and-release-motion-crim` — for bond reduction.
- `dw-plea-negotiation-analyzer-crim` — for plea-vs.-trial modeling using the sentencing matrix.
- `dw-trial-notebook-builder-crim` — for trial-day assembly.
- `dw-trial-day-assistant-crim` — for in-trial decision support.
- `dw-appellate-error-monitor-crim` — for record preservation tracking.
- `dw-post-conviction-relief-crim` — if conviction returns and PCR claims (IAC under *Strickland v. Washington*, 466 U.S. 668 (1984); *Miller / Montgomery* retroactivity) are in play.

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

| Statute | Offense | Primary Module | Notes |
|---|---|---|---|
| 14:30 | First degree murder | A.1, F, H.1 | Capital posture; felony-murder predicates |
| 14:30.1 | Second degree murder | A.2, C, F, G, H.2 | LWOP; juvenile *Miller* |
| 14:31 | Manslaughter | A.3, C, G | Heat of passion; felony manslaughter |
| 14:32 | Negligent homicide | A.4 | Floor on homicide ladder |
| 14:34 | Aggravated battery | A.5, B | "Dangerous weapon" element |
| 14:34.1 | Second degree battery | A.6, C | Specific intent; "serious bodily injury" |
| 14:34.5 | Battery on police officer | A.7 | Verify subsection minimums |
| 14:37 | Aggravated assault | A.8 | 14:37.4 firearm felony version |
| 14:44 | Aggravated kidnapping | A.9, H.2 | LWOP; "ransom" element |
| 14:44.1 | Second degree kidnapping | A.10 | Without-benefit floor |
| 14:60 | Aggravated burglary | A.11, B | Three aggravator prongs |
| 14:62.8 | Home invasion | A.12 | Verify Art. 814 listing |
| 14:64 | Armed robbery | A.13, H.4 | 14:64.3 enhancement |
| 14:64.1 | First degree robbery | A.14 | "Reasonable belief" std. |
| 14:64.3 | Firearm enhancement | A.15, H.4 | +5 yrs consecutive, no benefit |
| 14:65 | Simple robbery | A.16 | 7-yr max; parole eligible |

---

## QUICK REFERENCE — STATUTE-AND-CASE CITATIONS USED

Real Louisiana statutes (verify current text against Westlaw before finalizing):
- La. R.S. 14:10, 14:12, 14:15, 14:18, 14:19, 14:20, 14:21, 14:22, 14:24
- La. R.S. 14:30, 14:30.1, 14:31, 14:32
- La. R.S. 14:33, 14:34, 14:34.1, 14:34.5
- La. R.S. 14:36, 14:37, 14:37.4
- La. R.S. 14:44, 14:44.1, 14:45, 14:46
- La. R.S. 14:60, 14:62, 14:62.3, 14:62.8, 14:63
- La. R.S. 14:64, 14:64.1, 14:64.3, 14:65
- La. R.S. 14:2(B) (violent-felony list); La. R.S. 14:2(3) (dangerous weapon)
- La. R.S. 15:529.1 (habitual offender); La. R.S. 15:574.4 (parole eligibility)
- La. C.Cr.P. Arts. 801, 807, 814, 815, 821, 878.1, 893, 905.2.1, 905.4

Real federal/U.S. Supreme Court cases:
- *Miller v. Alabama*, 567 U.S. 460 (2012)
- *Montgomery v. Louisiana*, 577 U.S. 190 (2016)
- *Roper v. Simmons*, 543 U.S. 551 (2005)
- *Graham v. Florida*, 560 U.S. 48 (2010)
- *Kennedy v. Louisiana*, 554 U.S. 407 (2008)
- *Strickland v. Washington*, 466 U.S. 668 (1984)

Louisiana state cases used (verified — pinpoints confirmed against publicly available case databases; attorney should still Westlaw-check for currency before filing):
- *State v. Tompkins*, 403 So.2d 644 (La. 1981) — sudden-passion / heat-of-blood mitigation framework
- *State v. Anthony*, 427 So.2d 1155 (La. 1983); *State v. Kalathakis*, 563 So.2d 228 (La. 1990) — felony-murder "in the perpetration" termination
- *State v. Smith*, 327 So.2d 355 (La. 1976); *State v. Manieri*, 378 So.2d 931 (La. 1979) — inflammatory-photograph limits
- *State v. Lee*, 331 So.2d 455 (La. 1976) — victim-character admissibility (La. C.E. Art. 404(A)(2)(a))

The "mere words insufficient to constitute aggression" doctrine and the sudden-passion burden allocation are discussed without specific case attribution where the publicly available record did not yield a clean canonical citation; attorney should add the controlling Louisiana case before filing any deliverable that relies on those doctrines.

---

## CHECKLIST FOR CASE COMPLETION

- [ ] Step 0 case-type verification confirmed against discovery.
- [ ] Step 0.5 shared protocols loaded.
- [ ] Step 1 information gathering complete (gaps logged, not speculated).
- [ ] Module A element grid built for every count.
- [ ] Module B defense theory map built and discovery-cited.
- [ ] Module C intent analysis run for every count.
- [ ] Module D self-defense analysis with no-duty-to-retreat preserved.
- [ ] Module E justification framework run if applicable.
- [ ] Module F felony-murder analysis run if applicable.
- [ ] Module G heat-of-passion conversion checklist complete (homicides only).
- [ ] Module H sentencing exposure modeled (capital, LWOP, juvenile *Miller*, 14:64.3).
- [ ] Module I habitual-offender predicate audit started; routed to `dw-habitual-offender-auditor-crim`.
- [ ] Module J motion and discovery package routed to `dw-pretrial-motion-library-crim`.
- [ ] Primary deliverable generated and saved to Cowork Analysis path.
- [ ] Cross-skill routing complete (firearms-specialist, mitigation-specialist, jury-instructions-builder, cross-exam-architect, plea-negotiation-analyzer as applicable).
- [ ] Source-citation appendix populated; no `[UNSOURCED]` items remain in final deliverable.
- [ ] All `[VERIFY CITATION]` flags resolved or carried forward with attorney sign-off.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **manslaughter-conversion-analysis.md** — Heat-of-passion manslaughter conversion playbook (La. R.S. 14:31(A)(1)) as responsive verdict to first/second-degree murder; statutory mechanics, doctrinal lines, and trial strategy
- **responsive-verdict-tables.md** — Responsive verdicts under La. C.Cr.P. Art. 814 for homicide, battery, kidnapping, robbery, and burglary offenses; verdict-form planning
- **self-defense-jury-charges.md** — Louisiana self-defense and defense-of-others jury charges with the controlling no-duty-to-retreat point under La. R.S. 14:20(C); pattern instruction language
- **sentencing-exposure-matrix.md** — Sentencing exposure matrix: mandatory minimums, statutory maximums, parole/probation eligibility, La. R.S. 14:64.3 firearm enhancement, and La. R.S. 15:529.1 habitual-offender multiplier
