---
name: dw-404b-opposition-crim
category: pleadings
description: >
  Oppose other crimes evidence under 404(b). ALWAYS invoke for "404(b)," "Prieur notice,"
  "prior bad acts," "other crimes evidence," "oppose 404(b)," or "kitchen sink notice."
  Produces Opposition + Memorandum in Support. Read
  ../../../dw-core/skills/dw-shared-protocols-crim/references/template-selection-protocol.md before drafting.
---

# Daniels & Washington — 404(B) Other Crimes Evidence Opposition Generator
**Version 1.0 | Internal Use Only**

This skill generates complete, ready-to-edit filings to oppose the State's introduction of other crimes evidence under La. C.E. Art. 404(B). It produces two separate Word documents: a short-form **Opposition to State's 404(B) Notice** (or **Motion in Limine to Exclude**) and a detailed **Memorandum in Support**. It reads the State's Prieur notice and discovery files to extract facts, searches firm databases for templates and prior authority, and applies Louisiana law throughout.

**Cowork drafts; attorney approves.** Every output is a draft for attorney review. The attorney verifies facts, confirms legal arguments, signs, and files.

---

## STEP 0 -- FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any 404(b) notices, Prieur notices, prior conviction records, prior bad acts evidence, witness statements, or case discovery, do not analyze anything yet.**

Your only response must be:
> *"Before I begin -- are you uploading any additional 404(b)/Prieur notices, prior conviction records, prior bad acts evidence, witness statements, police reports, or other case documents? I'll start analysis only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-analysis discovery of an additional prior bad act, a missing exhibit referenced in the State's notice, or a co-defendant's similar 404(b) ruling would require complete re-evaluation of the opposition's relevance, prejudice, and Prieur compliance arguments.

---

### Source Citation Mandate

Every factual assertion in the Opposition and Memorandum in Support must trace back to a specific source document. 404(b) litigation is fact-intensive — the court evaluates whether each prior act qualifies under an enumerated exception based on the documented record. Unsourced claims about what the defendant allegedly did, when, or in what context carry no weight at a Prieur hearing.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(State's 404(B) Notice, p. 2, para. 3)`
- `(Prior Conviction Minute Entry — Docket #2018-CR-0456, p. 1)`
- `(Prior Police Report — LCPD Case #2018-00123, p. 4, para. 5)`
- `(Witness Statement — [Name], 03/15/2026, p. 2)`
- `(Discovery Production, Bates #00145-00148)`

**Multiple-source rule:** When more than one document confirms a fact about a prior act, cite all of them — e.g., `(Prior Police Report, p. 4, para. 5; Booking Record, p. 1)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows to confirm or remove it before filing.

**Where sourcing applies:** All factual content about prior acts, the State's proffered exception, the defense theory, and prejudice analysis. Legal standards and case law follow normal legal citation format.

---

## Filing Types

This skill generates two types of filings depending on the posture:

| Filing Type | When to Use | Triggered By |
|-------------|-------------|--------------|
| **Opposition to State's 404(B) Notice** | The State has filed a Prieur notice seeking to introduce other crimes evidence | State's notice is uploaded or described |
| **Defense Motion in Limine** | The defense wants to preemptively exclude anticipated 404(b) evidence before the State files notice | Attorney identifies evidence the State is likely to use |

When the State has filed a notice, generate an Opposition. When the defense is acting preemptively, generate a Motion in Limine. In both cases, the Memorandum in Support follows the same analytical framework.

---

## The 404(B) Analytical Framework

Understanding this framework is essential — it drives every argument in the filing. Louisiana's 404(B) exclusionary rule rests on a fundamental principle: evidence that a person committed other crimes or bad acts is inadmissible to prove that the person acted in conformity with that character on the charged occasion. The substantial risk of grave prejudice to the defendant is too high. *State v. Prieur*, 277 So.2d 126, 128 (La. 1973).

The State may overcome this bar only by satisfying ALL of the following requirements:

### Requirement 1: Adequate Written Notice (Prieur)
The State must furnish written notice within a reasonable time before trial describing the other acts with the "general particularity required of an indictment or information." *Prieur*, 277 So.2d at 130. The notice must specify which exception(s) the State relies upon. A "kitchen sink" notice listing every possible exception without connecting each item of evidence to a specific exception is inadequate. *State v. Goffner (I)*, 23-179 (La. App. 5 Cir. 04/07/23); *Goffner (II)*, 23-403 (La. App. 5 Cir. 08/17/23); *Goffner (III)*, 23-403 (La. App. 5 Cir. 08/18/23).

### Requirement 2: Pretrial Hearing
A Prieur hearing must be held before the evidence is admitted. The court must make specific, individualized rulings on each item of evidence — not in globo rulings on an entire production. *Goffner (II)*; *Goffner (III)*.

### Requirement 3: Legitimate Purpose (Not Character)
The evidence must be offered for one of the enumerated purposes under La. C.E. Art. 404(B)(1) — motive, opportunity, intent, preparation, plan, knowledge, identity, absence of mistake or accident — or as res gestae / integral act. It cannot be a subterfuge for depicting the defendant's bad character or propensity for criminal behavior. *Rose*, 949 So.2d at 1243-44.

### Requirement 4: Independent Relevance to a Material Fact
The other crimes evidence must tend to prove a material fact genuinely at issue in the case, not merely a fact the State asserts. If the defendant has not placed intent, identity, plan, etc. at issue, the evidence lacks independent relevance. *State v. Martin*, 377 So.2d 259, 263 (La. 1979).

### Requirement 5: State Must Prove Defendant Committed the Other Acts
The State bears the burden of proving the defendant actually committed the other crimes or acts. *State v. Galliano*, 2002-2849 (La. 1/10/03), 839 So.2d 932.

### Requirement 6: Probative Value Must Outweigh Prejudicial Effect
Even if the evidence passes all the above tests, it must still survive the La. C.E. Art. 403 balancing test — its probative value must substantially outweigh the danger of unfair prejudice, confusion of issues, misleading the jury, undue delay, or waste of time.

---

## Workflow

### STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any pleading, read `dw-shared-protocols-crim/SKILL.md` and load:

1. `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` — orchestrator for caption, signature, COS, notice, proposed order, citation style, and filing conventions
2. `dw-shared-protocols-crim/references/output-path-formula.md` — output path anchored on `CASE_ROOT`

Filed pleadings receive NO work product marking. Follow the boilerplate component sequence in order. Output to the appropriate `01 - Trial Notebook/` motion subfolder per the formula.

### Step 1: Template-First Search

Before drafting, search DEVONthink for firm templates and prior 404(b) filings. This is the firm's Template-First Drafting Rule.

**DEVONthink searches to run:**
```
"404" OR "other crimes" in group "404 B - Other Crimes" (database: Law Library-Criminal)
"motion exclude other crimes" OR "oppose 404" OR "Prieur"
"motion in limine" AND "404"
```

Also search the active case folder's `06 - Law & Research` for any case-specific research already completed.

Key documents known to exist in DEVONthink (404 B - Other Crimes folder):
- `motion to Exclude other crimes evidence` — prior motion template
- `brief memo-404 b` — brief memo on 404(B) law
- `044s2 Supplement to Adequate 404b Notice` — Neveaux capital case supplement with Goffner opinions
- `notice requirement` — Prieur notice requirement analysis
- `Notes of Decisions for Art 404` — comprehensive case law digest
- `Louisiana supreme court reigns in 404 b` — analysis of Louisiana Supreme Court restrictions
- `State v. Jones, 285 So.3d 1074` — recent case law

**After searches complete**, read and follow the Template Selection Protocol at `/mnt/skills/user/dw-shared-protocols-crim/references/template-selection-protocol.md` (Steps A through D). Present the top 3 results, let the attorney select a template or paste a DEVONthink link, and load the selection before proceeding. Do not proceed to Step 2 until the attorney has selected a template or chosen to draft from scratch.

If a template is selected, preserve the firm's preferred formatting and legal positions — then update with case-specific facts and authority. If drafting from scratch, use this skill's built-in structure and offer to save the final approved version as a new template.

### Step 2: Gather Case Context

**From the attorney prompt:** Parse whatever the attorney provides — client name, docket number, the charged offense(s), what other crimes evidence the State seeks to introduce, and the defense theory.

**From the State's Prieur notice (when uploaded):** Extract and catalog:
- Each act or offense the State seeks to introduce
- Which 404(B)(1) exception the State claims for each
- The level of specificity — does it identify specific items of evidence, or is it a "document dump"?
- Whether the notice was timely filed
- Whether it describes the acts with the particularity required by Prieur

**From discovery files (when available):** Look for:
- **Police reports** — details of the other acts the State references; look for inconsistencies, weak identification, lack of corroboration
- **Client's criminal history** — prior convictions vs. uncharged conduct; arrests that did not result in conviction; dismissed or nolle prosequi charges
- **Witness statements** — who is the source for the other acts? What credibility issues exist?
- **The charged offense details** — essential for arguing lack of similarity, relevance, or connection to the other acts

**From case analysis (when available):** Check for:
- Phase 2 Report 3 (Immediate Red Flags) — any 404(b) issues already identified
- Phase 2 Constitutional Issues Scan
- Witness Cross-Reference — witnesses who appear in both the charged and other acts

### Step 3: Analyze Each Item of Evidence

For every item of other crimes evidence the State seeks to introduce, work through the six-requirement framework above. This analysis drives the argument structure.

**For each item, answer:**

1. **Notice adequacy:** Did the State specifically identify this item and connect it to a specific exception, or is it buried in a general notice?

2. **Stated purpose — is it legitimate or pretextual?**
   - *Motive:* Does the other act actually establish a motive for the charged offense? Or is the connection speculative?
   - *Opportunity:* Does it show the defendant had the means or access? Or is it mere propensity reasoning disguised as opportunity?
   - *Intent:* Is intent genuinely at issue? If the defendant has not raised a defense negating intent (accident, mistake, lack of specific intent), the State cannot use 404(b) to "prove" what is not disputed.
   - *Preparation:* Does it show the defendant took preparatory steps for the charged offense? Or is it unrelated prior conduct?
   - *Plan / scheme / system:* Is there a genuine signature or modus operandi connecting the acts? Mere general similarity is insufficient — Louisiana requires a "peculiar and distinctive quality" or "such connection with the charged crime as to be of independent relevance." The more generic the similarity, the weaker the plan argument.
   - *Knowledge:* Does the other act show the defendant knew something material (e.g., the substance was a controlled substance)? Or is it cumulative?
   - *Identity:* Is identity genuinely at issue? If the defendant does not dispute being present, 404(b) identity evidence is irrelevant.
   - *Absence of mistake or accident:* Has the defense raised mistake or accident? If not, this exception does not apply.
   - *Res gestae / integral act:* Is the other act so intertwined with the charged offense that the State truly cannot present its case without it? This is a narrow exception — not a backdoor for character evidence.

3. **Material fact at issue:** Is the purpose the State claims actually contested in this case?

4. **Proof the defendant committed it:** What is the State's evidence that the defendant actually committed the other act? Bare allegations, uncorroborated accusations, or arrests without conviction may be insufficient.

5. **Probative vs. prejudicial (Art. 403):** Even if the evidence clears every hurdle, does the marginal probative value justify the grave prejudice of placing uncharged conduct before the jury?

### Step 4: Draft the Opposition / Motion in Limine (.docx #1)

The Opposition (or Motion in Limine) is a short, formal filing — typically 3-5 pages. It frames the issue and requests relief.

**Structure:**

```
[CAPTION — per shared protocols]

DEFENDANT'S OPPOSITION TO STATE'S NOTICE OF INTENT TO
INTRODUCE OTHER CRIMES EVIDENCE PURSUANT TO LA. C.E. ART. 404(B)
— OR —
DEFENDANT'S MOTION IN LIMINE TO EXCLUDE OTHER CRIMES EVIDENCE

NOW INTO COURT, through undersigned counsel, comes defendant [CLIENT NAME],
who respectfully opposes the State's Notice of Intent to Introduce Evidence
of Other Crimes, Wrongs, or Acts pursuant to La. C.E. Art. 404(B) [or:
who respectfully moves this Honorable Court to exclude evidence of other
crimes, wrongs, or acts] and in support thereof states the following:

I.    INTRODUCTION
      [2-3 sentences: what the State seeks to introduce, why it should be
       excluded, what constitutional and evidentiary principles are at stake]

II.   BACKGROUND
      [The charged offense — brief summary. What the State's notice seeks
       to introduce. Identify each item of other crimes evidence by number
       or category.]

III.  SUMMARY OF ARGUMENT
      [Brief preview of the legal deficiencies in the State's position.
       Organize by item of evidence if multiple items are challenged.]

IV.   PRAYER FOR RELIEF
      WHEREFORE, defendant [CLIENT NAME] respectfully prays that this
      Honorable Court:
      (1) Deny the State's request to introduce evidence of other crimes,
          wrongs, or acts at trial;
      (2) [If notice is inadequate:] Order the State to provide adequate
          notice in compliance with State v. Prieur and specifically
          identify each item of evidence and the exception relied upon,
          per State v. Goffner;
      (3) Conduct a pretrial hearing pursuant to Prieur with specific,
          individualized rulings on each item of evidence;
      (4) Exclude [specific evidence] as inadmissible under La. C.E.
          Art. 404(B) and Art. 403;
      (5) Grant such other relief as the Court deems just and proper.

[CERTIFICATE OF SERVICE — per shared protocols]
[SIGNATURE BLOCK — per shared protocols]
```

**If generating a defense Motion in Limine** (preemptive, no State notice yet):
- Replace "Opposition" language with "Motion in Limine to Exclude"
- Explain what evidence the defense anticipates the State will seek to introduce
- Argue that the evidence should be excluded regardless of how the State frames it
- Request that the court prohibit the State from referencing the evidence without prior approval outside the presence of the jury

### Step 5: Draft the Memorandum in Support (.docx #2)

The Memorandum is the substantive legal brief — typically 10-25 pages depending on the number of items challenged and complexity of the arguments.

**Structure:**

```
[CAPTION — per shared protocols]

MEMORANDUM IN SUPPORT OF DEFENDANT'S OPPOSITION TO STATE'S
404(B) NOTICE [or: MOTION IN LIMINE TO EXCLUDE OTHER CRIMES EVIDENCE]

I.    INTRODUCTION
      [Frame the constitutional stakes. The general exclusionary rule exists
       because other crimes evidence carries a "substantial risk of grave
       prejudice." Prieur, 277 So.2d at 128. The State's burden is heavy
       and the court must carefully scrutinize every item.]

II.   STATEMENT OF FACTS
      [Detailed factual narrative. Two sections:
       A. The Charged Offense — what the defendant is actually on trial for
       B. The Other Acts Evidence — what the State seeks to introduce,
          described with specificity. Cite the State's notice and any
          discovery by Bate stamp.]

III.  LEGAL STANDARD
      [The 404(B) framework. Read references/404b-citations.md for the
       complete citation library. Key elements to cover:
       - General exclusionary rule (Art. 404(B)(1); Prieur)
       - Notice and hearing requirements (Prieur; Goffner)
       - Independent relevance requirement (Martin; Rose)
       - State's burden to prove defendant committed the other acts (Galliano)
       - Art. 403 balancing test
       - Louisiana's heightened scrutiny of other crimes evidence]

IV.   ARGUMENT
      [Apply the law to the facts. Organize by ground of challenge.
       Each section should:
       - State the legal rule
       - Apply it to the specific facts
       - Anticipate and rebut the State's likely response
       - Conclude with why this evidence must be excluded]

      A. THE STATE'S NOTICE IS INADEQUATE
         [If applicable. Argue specificity under Prieur and Goffner.
          Attack "kitchen sink" notices. Demand item-by-item identification
          and exception-by-exception specification.]

      B. THE EVIDENCE DOES NOT SERVE A LEGITIMATE PURPOSE
         [For each item: the stated purpose is either inapplicable to this
          case or is a pretext for character evidence.]

         1. [Item/Category 1] — [Why the stated exception fails]
         2. [Item/Category 2] — [Why the stated exception fails]
         ...

      C. THE EVIDENCE LACKS INDEPENDENT RELEVANCE TO A MATERIAL
         FACT AT ISSUE
         [The purpose the State claims is not genuinely contested.
          If the defendant has not raised the defense that the exception
          is designed to rebut, the evidence is irrelevant.]

      D. THE STATE CANNOT PROVE THE DEFENDANT COMMITTED THE OTHER ACTS
         [If applicable. Attack the quality of evidence supporting the
          other acts — uncorroborated allegations, dismissed charges,
          acquittals, credibility problems.]

      E. THE PROBATIVE VALUE IS SUBSTANTIALLY OUTWEIGHED BY
         UNFAIR PREJUDICE (LA. C.E. ART. 403)
         [Even if the evidence passes every other test, the jury will
          use it for the forbidden purpose — to conclude that the defendant
          is a bad person who probably committed the charged offense.
          The prejudicial effect is devastating and the probative value
          is marginal at best, especially where the State has other
          evidence to prove the same point.]

V.    CONCLUSION
      [Summarize the deficiencies. Reiterate specific relief requested.]

[CERTIFICATE OF SERVICE — per shared protocols]
[SIGNATURE BLOCK — per shared protocols]
```

**Key rules for the Memorandum:**
- Lead with the strongest argument. If the notice is a "kitchen sink" dump, lead with notice inadequacy under Goffner — it's a threshold issue that can moot the substantive arguments.
- Address each item of evidence individually. The Fifth Circuit in Goffner made clear that courts must rule on each item specifically — mirror this in the argument structure.
- Anticipate the State's arguments. The prosecution will claim the evidence is "integral to the narrative" or "necessary to explain the context." Beat them to it — explain why the State can present its case without this evidence.
- Use the State's own characterization against them. If the State's notice uses vague language, quote it to show inadequacy. If the State claims "plan" but the acts have nothing distinctive in common, highlight the generic nature.
- Emphasize the prejudice. Other crimes evidence is uniquely dangerous because jurors cannot easily compartmentalize it. The risk that jurors will convict based on character rather than proof of the charged offense is the core reason the exclusionary rule exists.
- Cite both Louisiana Supreme Court and Circuit Court authority. Louisiana courts have been increasingly strict about 404(B) — the Goffner line of cases from the Fifth Circuit is particularly powerful.

### Step 6: Citation Research

Use a layered approach:

**Layer 1 — Training knowledge:** Start with well-established 404(B) precedent. Read `references/404b-citations.md` for the organized citation library.

**Layer 2 — DEVONthink:** Search for citations used in prior firm filings:
```
Search in "404 B - Other Crimes" group
Search: "404" OR "Prieur" OR "other crimes" in "06 - Law & Research"
```

**Layer 3 — Web search for recent authority:** Search for recent Louisiana 404(B) case law, particularly from the circuit covering the case. Focus on decisions from the past 2 years that may have refined the *Prieur* framework or modified the burden analysis.

After assembling citations, flag any that may need currency verification:
`[VERIFY CITATION — confirm this case has not been overruled or modified]`

### Step 7: Generate the .docx Files

Read the `docx` skill (SKILL.md) for document creation instructions.

**Formatting requirements:**
- US Letter (8.5" x 11"), 1-inch margins
- Font: Times New Roman, 12pt body text, 14pt headings
- Double-spaced body text (court filing)
- Left-aligned text (no full justification)
- Page numbers centered in footer
- Caption on first page of each document
- Each document starts on page 1

**File naming:**
- Opposition: `Opposition to 404(B) Notice - [Client Last Name] - [Date].docx`
- Motion in Limine: `Motion in Limine - 404(B) - [Client Last Name] - [Date].docx`
- Memorandum: `Memorandum in Support - 404(B) - [Client Last Name] - [Date].docx`

### Step 8: Attorney Review Flags

Before presenting the output, mark all items that need attorney attention:

- `[VERIFY — confirm this fact with client/discovery]` — factual assertions not directly sourced
- `[VERIFY CITATION — confirm current validity]` — case law that may have been modified
- `[ATTORNEY TO COMPLETE]` — signature block, specific dates, bar number
- `[STRATEGIC DECISION]` — whether to challenge notice adequacy vs. substance, whether to request a continuance for inadequate notice, which items to prioritize
- `[RESEARCH NEEDED]` — areas where additional legal research would strengthen the argument

### Step 9: Save and Integrate

**If part of an active case folder:**
- Save both documents to `02 - Pretrial Notebook/01 - Pleadings/`
- Update the LWOP Worksheet's Motions section if applicable
- Create a Clio task: *"Review and File 404(B) Opposition — [Client Name]"*
- Cross-reference with Report 3 (Immediate Red Flags) if one exists

**If standalone:**
- Save to the current working folder / outputs directory

**Present to the attorney with a summary:**
- Filing type (Opposition vs. Motion in Limine)
- Number of items of other crimes evidence challenged
- Key arguments and the legal basis for each
- Primary authorities cited
- Items flagged for attorney attention
- Prieur hearing date (if known)
- Whether a prior firm template was used as the base

---

## Common 404(B) Attack Vectors

These are the most effective lines of attack organized by the exception the State typically claims. Use these as a checklist when analyzing the State's notice.

### "Motive"
- The other act does not logically establish a motive for the charged offense
- The alleged motive is speculative or requires too many inferential leaps
- The other act shows general criminal disposition, not specific motive
- The prejudicial impact of revealing the other act far outweighs the marginal value of establishing motive, especially where motive can be shown through other evidence

### "Intent"
- Intent is not genuinely at issue — the defendant has not claimed accident or mistake
- The charged offense requires only general intent, which can be inferred from the act itself
- Using prior acts to "prove" intent is propensity reasoning in disguise
- The doctrine of chances should not be used to circumvent the exclusionary rule

### "Plan / Scheme / System"
- The acts are not sufficiently similar — mere general resemblance is insufficient
- Louisiana requires a "peculiar and distinctive quality" or modus operandi
- Common criminal methods shared by thousands of offenders do not establish a "plan"
- The similarity is in the type of crime, not in a distinctive method of commission

### "Knowledge"
- Knowledge is not genuinely disputed
- The other act does not logically establish knowledge relevant to the charged offense
- Knowledge can be proved through other means without the prejudice of other crimes evidence

### "Identity"
- Identity is not at issue — the defendant does not dispute being present
- The other acts lack the distinctive signature necessary for identity evidence
- The identifying characteristics are too common to be probative

### "Absence of Mistake or Accident"
- The defendant has not raised mistake or accident as a defense
- The State is preemptively "rebutting" a defense that does not exist
- This exception applies only when the defendant actually claims the act was innocent

### "Res Gestae / Integral Act"
- The other act is not genuinely intertwined with the charged offense
- The State can present its case coherently without reference to the other act
- "Context" and "background" are not recognized exceptions — they are character evidence in disguise
- The res gestae exception is narrow and should not be stretched to admit what the enumerated exceptions exclude

---

## Integration with Other Skills

| Skill | How It Integrates |
|-------|------------------|
| `dw-criminal-defense-crim` | Phase 2 Report 3 (Red Flags) may identify 404(b) issues |
| `dw-suppression-motion-crim` | If 404(b) evidence was obtained through a constitutional violation, suppression is the primary remedy; 404(b) exclusion is an alternative |
| `dw-cross-exam-architect-crim` | If 404(b) evidence is admitted despite opposition, build cross-examination to minimize its impact |
| `dw-brady-giglio-auditor-crim` | Undisclosed favorable evidence may undermine the other acts the State seeks to introduce |
| `docx` | Document generation — read for .docx creation instructions |
| `dw-shared-protocols-crim` | Caption, signature, COS, notice of hearing, proposed order, citation style, filing conventions, output path |
| DEVONthink | Template-First search in `404 B - Other Crimes` folder |
| TextExpander | `;draft` (skill-specific; caption/sig/cos now via shared protocols) |

---

*This skill reflects Daniels & Washington 404(B) Opposition Generator Version 1.0 (March 2026). Update whenever 404(B) case law or firm procedures change.*


---

## Output Location

Use the output path formula from `dw-shared-protocols-crim/references/output-path-formula.md`. Filed motions go to `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/`. See shared protocols for CASE_ROOT resolution, filename conventions, and post-write reporting format.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **404b-citations.md** — 404(B) citation library: Louisiana opposition authority (Prieur framework foundational cases) with DEVONthink links to firm copies; cite-check before filing
