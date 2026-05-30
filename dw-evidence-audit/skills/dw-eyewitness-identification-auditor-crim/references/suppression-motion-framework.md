## MODULE G -- Suppression Motion Framework

### G.1 -- Motion to Suppress Suggestive Identification

When the identification procedure was impermissibly suggestive and the Manson reliability factors do not outweigh the suggestiveness, the remedy is suppression:

**Structure of the Motion:**

```
MOTION TO SUPPRESS OUT-OF-COURT IDENTIFICATION
Daniels & Washington | [Case Name / Docket No.]

I. INTRODUCTION
[Brief statement that the identification was the product of
an impermissibly suggestive procedure that created a
substantial risk of misidentification]

II. STATEMENT OF FACTS
[Detailed factual account of the identification procedure,
drawn from discovery documents with specific citations]

III. THE IDENTIFICATION PROCEDURE WAS
     IMPERMISSIBLY SUGGESTIVE
[Document every suggestive element of the procedure:
 - Administration method (single-blind vs. double-blind)
 - Lineup composition deficiencies
 - Instruction failures
 - Post-identification feedback
 - Contextual suggestiveness
 Cite: Stovall v. Denno; Simmons v. United States;
 Foster v. California; State v. Higgins]

IV. THE IDENTIFICATION IS NOT RELIABLE UNDER
    THE TOTALITY OF CIRCUMSTANCES
[Five-factor Manson/Brathwaite analysis:
 Factor 1: Opportunity to view -- with supporting science
 Factor 2: Degree of attention -- with supporting science
 Factor 3: Accuracy of prior description -- with analysis
 Factor 4: Level of certainty -- with confidence critique
 Factor 5: Time between crime and confrontation
 Cite: Manson v. Brathwaite; Neil v. Biggers;
 State v. Guillory; State v. Higgins]

V. THE IN-COURT IDENTIFICATION MUST ALSO BE
   SUPPRESSED AS FRUIT OF THE SUGGESTIVE PROCEDURE
[If the out-of-court identification is suppressed, the
 in-court identification is admissible only if the State
 can establish an independent basis -- i.e., that the
 in-court identification derives from a source independent
 of the tainted out-of-court procedure.
 Cite: United States v. Wade; Gilbert v. California;
 La. C.Cr.P. Art. 163-164]

VI. CONCLUSION AND PRAYER FOR RELIEF
[Request suppression of both the out-of-court identification
 and any in-court identification that is the fruit of the
 suggestive procedure]
```

### G.2 -- Independent Source Doctrine

If the out-of-court identification is suppressed, the State will attempt to establish that the in-court identification has an "independent source" -- i.e., the witness's ability to identify the defendant in court derives from the witness's observation of the perpetrator during the crime, not from the suggestive identification procedure.

**Independent Source Factors (United States v. Wade, 388 U.S. 218, 241 (1967)):**

| Factor | Assessment Framework |
|--------|---------------------|
| Prior opportunity to observe the alleged criminal act | Same as Manson Factor 1 -- evaluate viewing conditions |
| Existence of any discrepancy between pre-lineup description and defendant's actual appearance | Compare initial description to defendant |
| Any identification prior to lineup of another person | If witness previously identified someone else, independent source is weak |
| Identification by picture of defendant prior to lineup | Prior photo exposure contaminates in-court ID |
| Failure to identify defendant on a prior occasion | Prior failure undercuts independent source |
| Lapse of time between alleged act and lineup identification | Longer interval weakens independent source |

### G.3 -- Sixth Amendment / Right to Counsel Challenge

Under United States v. Wade, 388 U.S. 218 (1967), and Gilbert v. California, 388 U.S. 263 (1967), a defendant has a Sixth Amendment right to the presence of counsel at any post-indictment lineup or identification confrontation.

| Situation | Right to Counsel | Authority |
|-----------|-----------------|-----------|
| Post-indictment live lineup | Yes -- counsel must be present or right waived | United States v. Wade; La. C.Cr.P. Art. 164 |
| Post-indictment photo array | No right to counsel (Ash) | United States v. Ash, 413 U.S. 300 (1973) |
| Pre-indictment lineup | No Sixth Amendment right (Kirby) | Kirby v. Illinois, 406 U.S. 682 (1972) |
| Pre-indictment photo array | No right to counsel | United States v. Ash |
| Showup (pre- or post-indictment) | Due process analysis under Stovall/Manson | Stovall v. Denno |

**If a post-indictment live lineup was conducted without counsel present and without a valid waiver, the identification is subject to per se exclusion under Wade.**

---

## MODULE H -- Cross-Examination Seeds

For each deficiency identified in the audit, generate cross-examination chapter seeds formatted for the **dw-cross-exam-architect-crim** skill.

### H.1 -- Identifying Witness Cross-Examination Seeds

**Viewing Conditions Chapter:**
```
CROSS CHAPTER SEED -- Viewing Conditions
Witness Type: Identifying Witness
Chapter Goal: Establish that viewing conditions were poor
  and inconsistent with reliable facial identification
Key Questions:
  Q1: You testified that you saw the person for approximately
      [duration] -- is that correct?
  Q2: And during that [duration], you were [describe stressful
      circumstance], correct?
  Q3: The lighting at the location was [describe actual
      conditions], wasn't it?
  Q4: You were approximately [distance] feet away from the
      person, correct?
  Q5: You had never seen this person before in your life,
      had you?
Source: [Witness statement / police report with page reference]
Impeachment Note: [If witness's trial testimony about conditions
  contradicts initial statement to police]
Legal Authority: Manson v. Brathwaite, Factor 1; NAS Report (2014)
```

**Confidence Chapter:**
```
CROSS CHAPTER SEED -- Confidence Inflation
Witness Type: Identifying Witness
Chapter Goal: Establish that witness's current confidence
  is inflated from original identification confidence
Key Questions:
  Q1: When you made your identification on [date], you said
      [verbatim confidence statement], correct?
  Q2: [If tentative]: You weren't certain at that time,
      were you?
  Q3: After you made your identification, the officer said
      [quote any feedback], didn't he/she?
  Q4: Today, you're telling this jury you're absolutely
      certain -- but that's not what you said on [date],
      is it?
  Q5: Between [identification date] and today, you've seen
      [defendant] in this courtroom [number] times, correct?
Source: [Photo array documentation; confidence statement]
Impeachment Note: Compare original confidence to trial testimony
Legal Authority: Wells & Bradfield (1998); NAS Report (2014);
  Manson Factor 4
```

**Cross-Racial Identification Chapter (if applicable):**
```
CROSS CHAPTER SEED -- Cross-Racial Identification
Witness Type: Identifying Witness
Chapter Goal: Establish that the identification was cross-racial
  and that the witness has limited experience with the
  other racial group
Key Questions:
  Q1: You are [race/ethnicity], correct?
  Q2: The person you identified is [race/ethnicity], correct?
  Q3: At the time of the crime, how many people of
      [defendant's race/ethnicity] did you interact with
      on a daily basis?
  Q4: You would agree that people are generally better at
      recognizing faces of their own racial group?
Source: [Witness statement; demographic information]
Legal Authority: Meissner & Brigham (2001); NAS Report (2014);
  State v. Guilbeaux (if applicable)
```

### H.2 -- Lineup Administrator Cross-Examination Seeds

**Administration Method Chapter:**
```
CROSS CHAPTER SEED -- Administration Procedure
Witness Type: Lineup Administrator / Detective
Chapter Goal: Establish that the procedure did not follow
  best practices and was susceptible to administrator influence
Key Questions:
  Q1: You administered this photo array to [witness], correct?
  Q2: You knew which photo was the suspect before you showed
      the array to the witness, didn't you?
  Q3: You're aware that the National Academy of Sciences
      recommends double-blind administration, aren't you?
  Q4: Your department does not require double-blind
      administration, does it?
  Q5: You were standing [describe proximity] to the witness
      while she/he viewed the photos, correct?
  Q6: You could see which photo the witness was looking at,
      couldn't you?
Source: [Photo array procedure report; department policy]
Impeachment Note: If department policy requires double-blind
  but was not followed
Legal Authority: NAS Report (2014) at 106; La. C.Cr.P. Art. 163
```

**Filler Selection Chapter:**
```
CROSS CHAPTER SEED -- Filler Selection
Witness Type: Lineup Administrator / Detective
Chapter Goal: Establish that fillers were not properly selected
  and the suspect stood out
Key Questions:
  Q1: How did you select the filler photographs for this array?
  Q2: Did you use the witness's description to select fillers,
      or did you match fillers to the suspect's appearance?
  Q3: [For each distinguishing feature]: The suspect's photo
      is the only one showing [feature], correct?
  Q4: If I showed this array to 100 people who had never seen
      the crime and asked them to guess which person was the
      suspect, how many do you think would pick [defendant]?
Source: [Photo array packet; filler source documentation]
Impeachment Note: [If functional size is less than nominal size]
Legal Authority: Manson v. Brathwaite; State v. Guillory
```

---

## MODULE I -- Expert Witness Need Assessment

### I.1 -- When to Recommend an Eyewitness Expert

An eyewitness identification expert should be recommended in every case where the identification is a critical piece of evidence AND any of the following conditions exist:

| Condition | Reason for Expert | Priority |
|-----------|------------------|----------|
| Cross-racial identification | Jurors underestimate the own-race bias | HIGH |
| Weapon focus present | Jurors do not intuitively understand weapon focus | HIGH |
| High stress during crime | Jurors assume stress enhances memory (it impairs it) | HIGH |
| Long retention interval (weeks/months) | Jurors underestimate memory decay | MODERATE |
| Confirming feedback given | Expert needed to explain confidence inflation mechanism | HIGH |
| Witness confidence increased over time | Expert needed to explain that confidence is not stable | HIGH |
| Multiple identification procedures | Expert needed to explain commitment effect | HIGH |
| Showup identification | Expert needed to explain inherent suggestiveness | MODERATE |
| Poor viewing conditions | Expert may be needed to quantify visual acuity limits | MODERATE |
| Identification is the sole or primary evidence | Stakes require maximum defense effort | HIGH |

### I.2 -- Expert Qualifications to Seek

The ideal defense eyewitness expert should have:

- Ph.D. in cognitive psychology, experimental psychology, or a related field
- Active research program in eyewitness memory and identification
- Peer-reviewed publications in eyewitness identification journals
- Experience testifying as an expert in state and federal courts
- Familiarity with the NAS Report (2014) and current meta-analyses
- No history of testifying exclusively for one side (prosecution or defense)
- Ability to explain complex science in accessible terms for lay jurors

### I.3 -- Key Expert Testimony Topics

| Topic | What the Expert Establishes | Counterintuitive Finding |
|-------|---------------------------|------------------------|
| Confidence-accuracy relationship | Confidence is a poor predictor of accuracy under imperfect conditions | Jurors intuitively believe confident witnesses are accurate |
| Weapon focus effect | Attention to weapon reduces face encoding | Jurors assume witnesses look at faces, not weapons |
| Cross-racial identification | Own-race bias is well-established | Jurors may not recognize the effect or may find it uncomfortable |
| Stress and memory | High stress impairs encoding | Jurors assume adrenaline sharpens memory |
| Memory decay | Memory degrades rapidly after the event | Jurors assume memory is stable over time |
| Post-identification feedback | Feedback inflates confidence retrospectively | Jurors assume confidence is inherent to the witness |
| Unconscious transference | Witness may identify a familiar face from a different context | Jurors assume recognition = accurate identification |
| Forgetting curve | Most forgetting occurs in the first 24-48 hours | Jurors assume gradual, linear decay |
| System variable effects | Police procedures affect identification accuracy | Jurors assume police procedures are neutral |

### I.4 -- Daubert/Foret Admissibility of Eyewitness Expert Testimony

Under Louisiana law, expert testimony on eyewitness identification must satisfy the requirements of La. C.E. Art. 702 and the *Daubert*/*Foret* framework (State v. Foret, 628 So.2d 1116 (La. 1993)):

| Daubert Factor | Application to Eyewitness Expert |
|---------------|--------------------------------|
| **Testability** | Eyewitness memory research is based on controlled experiments with testable hypotheses |
| **Peer review & publication** | Thousands of peer-reviewed publications; multiple meta-analyses |
| **Error rate** | Known error rates for identification under various conditions |
| **Standards** | NAS Report (2014); APA guidelines; established research methodology |
| **General acceptance** | Scientific consensus documented in NAS Report; multiple professional organizations endorse findings |

State v. Higgins, 898 So.2d 1219, 1230 (La. 2005): The Louisiana Supreme Court recognized the scientific basis for challenges to eyewitness identification reliability and applied the Manson/Brathwaite framework with attention to modern research.

United States v. Brownlee, 454 F.3d 131 (3d Cir. 2006): While a Third Circuit case, Brownlee is widely cited for holding that the exclusion of eyewitness expert testimony was an abuse of discretion where the case turned on the identification and the expert would have addressed counterintuitive aspects of eyewitness memory. 5th Circuit practitioners can cite this as persuasive authority.
