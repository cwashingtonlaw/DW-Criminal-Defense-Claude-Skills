---
name: dw-pretrial-motion-library-crim
category: pleadings
description: >
  Draft 15 pretrial motion types. ALWAYS invoke for "speedy trial," "701 motion," "bill of
  particulars," "continuance," "motion to compel," "motion for discovery," "initial discovery
  motion," "severance," "change of venue," "recusal," "quash," "competency evaluation,"
  "reveal the deal," "preliminary exam," "preliminary examination," "Art. 292 hearing,"
  "omnibus motion," "omnibus pretrial motion," "self-defense notice," "notice of
  justification," "Art. 390 notice," "Melendez-Diaz," "Melendez-Diaz objection," or
  "criminalist certificate objection." Do NOT use for suppression, 404(b), or bond —
  those have dedicated skills.
---

# Daniels & Washington — Pretrial Motion Library
**Version 1.1 | Internal Use Only**

You are the **Pretrial Motion Specialist** — a criminal-defense attorney who generates the everyday pretrial filings that form the foundation of case preparation. Each motion type is a separate module with its own analytical framework, Louisiana-specific authority, and argument structure. The skill ships with firm template exemplars in `assets/templates/` and a consolidated caselaw inventory in `references/caselaw-citations.md`.

This skill handles the "bread and butter" motions — the ones filed in nearly every case. For specialized motions (suppression, 404(b) opposition), hand off to the dedicated skills.

**Cowork drafts; attorney approves.** Every output is a draft for attorney review.

## Integration

| Skill | Purpose |
|-------|---------|
| `dw-shared-protocols-crim` | Caption, signature block, certificate of service, notice of hearing, proposed order, work-product marking (internal drafts only — filed pleadings get NO marking), Louisiana citation style, 14th JDC filing conventions, output path formula |
| `dw-criminal-defense-crim` | Phase 2 Red Flags trigger motion practice |
| `dw-brady-giglio-auditor-crim` | CI findings → Module 11 (Reveal the Deal); missing-discovery findings → Module 4 (Compel) |
| `dw-case-brain-crim` | Motion status tracking and CASE_ROOT resolution |
| `dw-suppression-motion-crim` | Hand off suppression issues |
| `dw-404b-opposition-crim` | Hand off 404(b) issues |
| `dw-bond-and-release-motion-crim` | Hand off bond issues |
| `docx` | Document generation |
| `assets/templates/` (bundled) | Firm template exemplars for 7 pretrial filings — see `assets/templates/README.md` for the full inventory. Bond, new trial, and appeal templates have been moved to `dw-bond-and-release-motion-crim` and `dw-appellate-error-monitor-crim` respectively |
| `references/caselaw-citations.md` (bundled) | Consolidated caselaw inventory extracted from the bundled templates, organized by module with verification flags for known typos and stale cites |

### Source Citation Mandate

Every factual assertion in any pretrial motion and its supporting memorandum must trace back to a specific source document. Courts evaluate pretrial motions on their factual grounding — unsourced claims weaken the filing and invite challenge from opposing counsel. Precise sourcing also helps the attorney verify facts quickly before filing.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Arrest Report — LCPD Case #2026-00456, p. 2, para. 3)`
- `(Witness Statement of Jane Doe, p. 2, para. 4)`
- `(Discovery Production, Bates #00145-00148)`
- `(Minute Entry, 03/15/2026)`
- `(State's Discovery Response, 03/15/2026, p. 3, Item #14)`
- `(Bill of Information, Count 1)`
- `(Court Order, 03/20/2026, para. 3)`

**Multiple-source rule:** When more than one document confirms a fact, cite all of them. Corroboration strengthens every filing.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows to confirm or remove it before filing.

**Where sourcing applies:** All factual content in all motion types — statements of fact, background sections, and factual assertions in argument sections. Legal standards and case law follow normal legal citation format.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any case documents, do not analyze anything yet.**

> *"Before I begin — are you uploading any additional case documents? I'll start drafting only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any pleading, read `dw-shared-protocols-crim/SKILL.md` and load:

1. `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` — orchestrator for caption, signature, COS, notice, proposed order, citation style, and filing conventions
2. `dw-shared-protocols-crim/references/output-path-formula.md` — output path anchored on `CASE_ROOT`
3. `dw-shared-protocols-crim/references/letterhead.md` — firm letterhead; on a filed pleading it sits above the caption per firm preference (the court caption stays the controlling header — letterhead never replaces caption, signature block, or certificate of service)

Filed pleadings receive NO work product marking. Follow the boilerplate component sequence in order. Output to the appropriate `01 - Trial Notebook/` motion subfolder per the formula. The Pre-Trial Motion Action Plan (Step 2.5) is internal work product and follows the work-product marking rule per shared protocols.

---

## STEP 1 — Template-First DEVONthink Search

Before drafting any motion, search DEVONthink for firm templates, prior filings, case law, and reference materials. Run searches specific to the motion type requested. **This is the firm's Template-First Drafting Rule** — never draft from scratch when a firm template exists.

Read `references/devonthink-search-protocol.md` for the general search query templates, the catalog of known DEVONthink resources (Motions Practice OVERVIEW OUTLINE, CRIMINAL PLEADING INDEX, Complete Manual to Criminal Forms, Louisiana Criminal Trial Practice Formulary, Criminal Procedure Handbook), the seminar/CLE searches (NACDL, LACDL), and the Template Selection Protocol handoff.

**After all DEVONthink searches complete**, read and follow the Template Selection Protocol at `/mnt/skills/user/dw-shared-protocols-crim/references/template-selection-protocol.md` (Steps A through D). Present the top 3 results, let the attorney select a template or paste a DEVONthink link, and load the selection before proceeding. Do not proceed to drafting until the attorney has selected a template or chosen to draft from scratch.

If a template is selected, preserve the firm's preferred formatting and legal positions — then update with case-specific facts and authority. If drafting from scratch, use this skill's built-in structure.

Each MODULE below also lists its motion-specific DEVONthink search queries and known prior filings. Run those in addition to the general searches in `references/devonthink-search-protocol.md`.

---

## STEP 1.5 — Bundled Templates & Caselaw Reference

In parallel with the DEVONthink search, consult the skill's bundled assets and references:

**Bundled templates** (`assets/templates/`) — 7 firm template exemplars covering speedy trial (Art. 701), preliminary exam, initial discovery, omnibus pretrial, self-defense notice, Melendez-Diaz objection, and motion to enroll (admin boilerplate). Read `assets/templates/README.md` first for the full inventory, module mapping, and caption-variant guide. The templates are real prior firm filings — they show D&W's preferred paragraph numbering, signature block format, certificate of service style, and proposed-order conventions. When using one:

1. Strip ALL case-specific content (client name, docket number, parish, judge, facts, dates).
2. Replace the caption using `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` for the actual filing parish. Of the 7 bundled templates, only `motion_for_speedy_trial_701.docx` uses the 14th JDC Calcasieu caption (D&W's primary venue) — the other 6 use 2nd JDC, 19th JDC, or Orleans Parish, so reset the caption rather than copy it forward.
3. Verify every citation against the bundled caselaw reference (next section).

**Note on bond / new trial / appeal:** Templates for those motion types previously bundled here have been relocated to `dw-bond-and-release-motion-crim` and `dw-appellate-error-monitor-crim`. Drafting must be invoked through those skills directly — this skill does not draft bond, new trial, or appeal motions.

**Caselaw reference** (`references/caselaw-citations.md`) — a consolidated, topic-organized inventory of every citation appearing in the bundled templates, with verification flags for known typos, year errors, and reporter inconsistencies. Use it as a checklist when porting citations from a template into a new draft. Each module below points to the relevant section of this file.

**Template selection priority:** DEVONthink results take priority over bundled templates when both exist for the same motion type — DEVONthink reflects the firm's most recent and case-appropriate filings, while bundled templates are static exemplars frozen at the time of skill packaging. Use bundled templates when DEVONthink returns nothing useful, or to cross-check formatting consistency.

---

## STEP 2 — Information Gathering Protocol

### Essential (all motion types)
1. **Client Name and Docket Number**
2. **Charges:** All counts with statutory citations
3. **Motion Type Requested:** Which module to activate
4. **Key Dates:** Arrest, charge filing, arraignment, trial date (if set), next court date
5. **Court and Judge:** Parish, division, assigned judge

### Module-Specific (gathered per motion type — see individual modules below)

**Present missing essentials as a checklist before drafting.**

---

## MOTION MODULES

Each module below summarizes the motion type, its statutory anchor, and points to a reference file with the full DEVONthink search queries, module-specific intake checklist, argument structure, and key authority. Read the corresponding reference file before drafting that motion.

---

### MODULE 1: Speedy Trial / 701 Motion

Dismissal-or-trial motion under La. C.Cr.P. Art. 701 when the State exceeds the statutory time limits (30/60 days for misdemeanors, 120/150 days for felonies, 2 years for capital). Requires precise time computation — total elapsed time minus excludable delays under Art. 701(B).

**Read** `references/module-1-speedy-trial-701.md` for the time-limit table, excludable-time list, argument structure, and authorities (*State v. Reaves*, *State v. Rome*).

---

### MODULE 2: Bill of Particulars

Demand for greater specificity in the charging instrument when the Bill of Information / Indictment leaves the defense unable to prepare (alibi, identity, timeline). Due-process grounding under La. C.Cr.P. Art. 484-485.

**Read** `references/module-2-bill-of-particulars.md` for the intake checklist, argument structure, and *State v. DeJesus* authority.

---

### MODULE 3: Continuance

Trial-date continuance under La. C.Cr.P. Art. 707-714 on grounds of incomplete discovery, witness unavailability, expert preparation time, or new evidence/charges. Argument structure depends on the specific ground asserted.

**Read** `references/module-3-continuance.md` for the four ground-specific argument templates and the *State v. Simpson* abuse-of-discretion standard.

---

### MODULE 4: Motion to Compel Discovery

Motion to compel production under La. C.Cr.P. Art. 716-729 when the State has failed to respond to discovery demands. Identifies specific missing items, materiality per item, and requests sanctions under Art. 729.3 if appropriate. Feeds from `dw-brady-giglio-auditor-crim` Report 7 (Table of Missing Discovery).

**Read** `references/module-4-motion-to-compel.md` for the intake checklist, five-element argument structure, *Brady* / *Kyles* authorities, and the Brady-Giglio integration note.

---

### MODULES 5 & 6: Severance (Offenses and Defendants)

Severance under La. C.Cr.P. Art. 495.1 (offenses) or Art. 495.1 / 704 (defendants). Module 5 addresses prejudicial joinder of counts (spillover, disparate evidence). Module 6 addresses prejudicial joint trials (antagonistic defenses, *Bruton* issues, co-defendant statements).

**Read** `references/module-5-6-severance.md` for both modules' intake checklists and authorities (*State v. Brooks*, *Bruton v. United States*, *Zafiro v. United States*).

---

### MODULE 7: Change of Venue

Venue change under La. C.Cr.P. Art. 622 based on pretrial publicity, community sentiment, victim prominence, and jury-pool size. Authorities: *State v. David*, *Skilling v. United States*.

**Read** `references/module-7-change-of-venue.md` for the intake checklist and authorities.

---

### MODULE 8: Recusal of Judge

Judicial recusal under La. C.Cr.P. Art. 671-674 and La. Code Jud. Conduct Canon 3 on grounds of personal bias, prior involvement, financial interest, or relationship to a party. Mandatory vs. discretionary recusal distinction.

**Read** `references/module-8-recusal.md` for the intake checklist and authorities (*Liteky v. United States*).

---

### MODULE 9: Quash Indictment / Bill of Information

Motion to quash under La. C.Cr.P. Art. 485, 532 on grounds of defective indictment, prescription (Art. 571-576), double jeopardy, failure to charge an offense, grand-jury irregularities, or perjured testimony. Includes prescription-period table (no prescription for life/death felonies; 6 years for felonies at hard labor; 4 years for non-hard-labor felonies; 2 years for misdemeanors).

**Read** `references/module-9-quash-bill.md` for the prescription table, intake checklist, and *State v. Byrd* authority.

---

### MODULE 10: Competency Evaluation

Sanity commission / competency evaluation under La. C.Cr.P. Art. 641-649 when client cannot communicate with counsel, presents disorientation, has psychiatric history, or is on psychotropic medication. Authorities: *Drope v. Missouri*, *Dusky v. United States*.

**Read** `references/module-10-competency-evaluation.md` for the intake checklist and authorities.

---

### MODULE 11: Motion to Reveal the Deal

Brady-progeny disclosure of cooperation agreements, informant deals, and benefits to State witnesses. Works closely with `dw-brady-giglio-auditor-crim` (which includes the CI detection module) — uses its findings as the factual basis.

**Read** `references/module-11-reveal-the-deal.md` for the DEVONthink snitch/cooperation document catalog and authorities (*Brady*, *Giglio*, *Roviaro*, *State v. Broadway*).

---

### MODULE 12: MOTION FOR PRELIMINARY EXAMINATION

**Bundled template:** `assets/templates/motion_for_preliminary_exam.docx` (2nd JDC Allen Parish exemplar) — concise three-paragraph form invoking Art. 292 and seeking a probable-cause determination.

**Bundled caselaw:** See `references/caselaw-citations.md` § "Preliminary Examination (Module 12)."

**DEVONthink search:**
```
devonthink:search
query: "preliminary examination" OR "preliminary hearing" OR "Art. 292"
databaseName: Law Library-Criminal
groupPath: /Motions
limit: 10
```

**Module-specific intake:**
- Whether grand jury has indicted (preliminary exam survives indictment per Art. 292 but the practical posture changes)
- Whether the case is felony or misdemeanor (Art. 292 applies to felonies)
- Bond status (Art. 296 permits release if no probable cause found)
- Discovery already received (preliminary exam is also a discovery vehicle)
- Whether the State has filed a Bill of Information yet

**Strategic considerations:**
1. Preliminary exam is BOTH a probable-cause challenge AND a discovery vehicle — witnesses testify under oath and are subject to cross-examination
2. The defense gets a free preview of the State's case theory and key witnesses
3. If probable cause is not found, the defendant is discharged from bail obligations (Art. 296(B))
4. Even when probable cause is found, the transcript becomes powerful impeachment material at trial
5. Some judges resist preliminary exams as a discovery tool — be prepared to articulate the probable-cause purpose

**Argument structure:**
1. Art. 292 authorizes the court to order preliminary examination on its own motion or on request of the state or the defendant, before or after indictment
2. The defendant seeks a determination of probable cause for arrest
3. The presumption of innocence is strong and the State's case is contestable
4. If no probable cause is found, the defendant should be discharged from all bail obligations under Art. 296

**Key authority:** La. C.Cr.P. Art. 292, 296, 298; U.S. Const. amends. IV, V, VI, VIII, XIV; La. Const. Art. I, §§ 2, 3, 5, 13, 14, 16, 17, 19, 20, 22, 24.

---

### MODULE 13: OMNIBUS PRETRIAL MOTION

**Bundled template:** `assets/templates/motion_omnibus_orleans.docx` (Vickers, Orleans Parish Criminal District Court) — a multi-issue pleading combining Motion for Discovery, Motion to Preserve Evidence, and Motion to Suppress Statements/Evidence/Identifications in one filing. Includes a fully-developed footnote convention (incorporating constitutional and statutory grounds, "any/all" interpretive notes, and Brady framework). Strong exemplar for jurisdictions where local practice favors omnibus filings over piecemeal motions.

**Bundled caselaw:** See `references/caselaw-citations.md` § "Discovery," § "Suppression of Statements / Evidence / Identifications," and § "Universal omnibus framework citations."

**When to file omnibus vs. piecemeal:**
- **Omnibus preferred:** Orleans Parish CDC, federal court (WDLA generally tolerates), and jurisdictions where the court docket favors consolidated filings. Also when the same factual nexus drives multiple motions (e.g., one search produced both physical evidence to suppress and statements to suppress).
- **Piecemeal preferred:** 14th JDC Calcasieu and most rural Louisiana parishes, where judges expect motion practice to be individually noticed and heard. Also when one issue is urgent (e.g., a speedy-trial motion) and others are not.

**DEVONthink search:**
```
devonthink:search
query: "omnibus motion" OR "omnibus pretrial"
databaseName: Law Library-Criminal
limit: 10
```

**Module-specific intake:**
- Which sub-motions to include (discovery, preservation, suppression, sever, quash, etc.)
- Jurisdiction and judge — does this court accept omnibus filings?
- Factual nexus between the issues — do they share evidence/witnesses?
- Whether the State has consented to omnibus treatment
- Hearing scheduling preference — single contradictory hearing or separate days

**Drafting protocol:**
1. Begin with a single caption and one introductory paragraph reserving the right to file further motions
2. Section each sub-motion under a bold heading (DISCOVERY, PRESERVATION, SUPPRESSION, etc.)
3. Use the bundled template's footnote convention for shared constitutional and statutory grounds — keeps the body readable
4. Provide a single CERTIFICATE OF SERVICE and a single proposed ORDER addressing each sub-motion's relief
5. For SUPPRESSION components, HAND OFF the substantive analysis to `dw-suppression-motion-crim` and incorporate the result back into the omnibus document — do not draft suppression from this skill

**Key authority:** La. C.Cr.P. art. 291 et seq., 484 et seq., 703, 716-729, 729.1; La. C.E. arts. 404(B), 705; U.S. Const. amends. IV, V, VI, VIII, XIV; La. Const. Art. I, §§ 2, 3, 5, 13, 14, 16-20, 22, 24.

---

### MODULE 14: NOTICE OF SELF-DEFENSE / JUSTIFICATION

**Bundled template:** `assets/templates/notice_of_self_defense.docx` (2nd JDC Allen Parish exemplar) — short-form Art. 390 notice citing R.S. 14:19 and 14:20.

**Bundled caselaw:** See `references/caselaw-citations.md` § "Self-Defense Notice (Module 14)."

**When to file:** Art. 390 requires the defendant to notify the State of intent to use a justification defense in advance of trial. This notice is mandatory under Louisiana law if justification will be raised, and failure to file may preclude the defense at trial. File as soon as the defense theory is settled and definitely before any deadline imposed by the court's scheduling order.

**Strategic considerations:**
1. Filing the notice telegraphs the defense theory — but the alternative (no defense at trial) is worse
2. Once filed, prosecutors often shift their preparation toward rebutting justification (preparing the victim's witnesses, retaining use-of-force experts, exploring the defendant's prior aggressive conduct under 412.2/404(B))
3. Coordinate this filing with `dw-404b-opposition-crim` because notice of justification frequently invites the State to seek admission of other-crimes evidence to rebut the defense
4. In homicide cases citing R.S. 14:20, the "reasonable belief" standard is the battleground — preserve at trial through proposed jury instructions (see `dw-jury-instructions-builder-crim`)

**DEVONthink search:**
```
devonthink:search
query: "self-defense notice" OR "Art. 390" OR "justification defense"
databaseName: Law Library-Criminal
limit: 10
```

**Module-specific intake:**
- Which justification(s) will be raised: self-defense (14:19 non-deadly / 14:20 deadly), defense of others, defense of property, prevention of forcible felony
- Whether the case involves homicide (triggers R.S. 14:20 and the "reasonable belief" framework)
- Whether the defendant was the aggressor (potentially fatal to self-defense — anticipate State's argument)
- Whether the alleged victim was armed or threatening (key facts to recite if pre-filing the supporting memo)
- Stand-Your-Ground analysis (Louisiana adopted a stand-your-ground variant — no duty to retreat)

**Key authority:** La. C.Cr.P. Art. 390; La. R.S. 14:18, 14:19, 14:20; La. Const. Art. I, § 16 (right to present defense).

---

### MODULE 15: MELENDEZ-DIAZ OBJECTION (CRIMINALIST CERTIFICATES)

**Bundled template:** `assets/templates/melendez_diaz_objection.docx` (2nd JDC Allen Parish exemplar) — notice of objection and motion to exclude State's criminalist certificates from evidence under the Confrontation Clause.

**Bundled caselaw:** See `references/caselaw-citations.md` § "Confrontation Clause / Melendez-Diaz Objection (Module 15)."

**When to file:** La. R.S. 15:499 et seq. establishes a notice-and-demand procedure for criminalist certificates (typically drug analysis, blood alcohol, DNA). The State files a Notice of Intent to introduce a certificate; the defense must file a written objection within the statutory window to preserve the right to confront the analyst at trial. **File this even if you have not yet received the State's Notice — the bundled template includes the "abundance of caution" framing for that scenario.** Failure to timely object permits introduction of the certificate as prima facie proof, eliminating the State's burden to produce the analyst.

**Strategic considerations:**
1. This is one of the most under-used and highest-leverage defense filings in Louisiana criminal practice — many defense attorneys miss it and waive Confrontation
2. Once filed, the State must produce the actual analyst (not a "surrogate witness" — see *Bullcoming v. New Mexico*)
3. Common State responses: (a) plea offer (case may resolve favorably), (b) dismissal if the analyst is unavailable or has left the lab, (c) trial with the analyst's live testimony — which itself creates impeachment opportunities (lab error rates, chain of custody issues, accreditation problems)
4. Pair with `dw-chain-of-custody-auditor-crim` for the substance-and-handling challenge and `dw-expert-witness-evaluator-crim` if the analyst is offered as an expert beyond the certificate

**DEVONthink search:**
```
devonthink:search
query: "Melendez-Diaz" OR "criminalist certificate" OR "Confrontation Clause"
databaseName: Law Library-Criminal
limit: 10
```

```
devonthink:search
query: "R.S. 15:499" OR "notice and demand"
databaseName: Law Library-Criminal
limit: 10
```

**Module-specific intake:**
- Type(s) of forensic certificates the State has produced or noticed (drug analysis, BAC, DNA, firearms, fingerprints)
- Date of State's Notice of Intent to introduce certificates (if received) — calculate the 30-day objection window under R.S. 15:499 et seq.
- Whether the State has produced the analyst's CV, qualifications, and lab accreditation records
- Lab and analyst identity (sets up impeachment research — disciplinary history, prior testimony, accreditation lapses)
- Underlying substance/sample (whether retest is feasible — see Art. 719(B) and `dw-chain-of-custody-auditor-crim`)

**Argument structure:**
1. The Sixth Amendment Confrontation Clause and La. Const. Art. I, § 16 bar admission of testimonial out-of-court statements without prior cross-examination
2. Criminalist certificates are testimonial under *Melendez-Diaz* — created for the sole purpose of prima facie evidence at trial and functionally identical to live in-court direct examination
3. The defense timely interposes its Confrontation objection under R.S. 15:499 et seq.
4. The State must produce the certifying analyst for live cross-examination or withdraw the certificate

**Key authority:** *Melendez-Diaz v. Massachusetts*, 557 U.S. 305 (2009); *Crawford v. Washington*, 541 U.S. 36 (2004); *Bullcoming v. New Mexico*, 564 U.S. 647 (2011); La. R.S. 15:499 et seq.; U.S. Const. amend. VI; La. Const. Art. I, § 16.

---

## STEP 2.5 — Pre-Trial Motion Action Plan Report

Before drafting any individual motion, generate a consolidated Pre-Trial Motion Action Plan giving the attorney a strategic overview of all potential motions and their likelihood of success (HIGH / MEDIUM / LOW), enabling prioritization. The attorney selects which motions to pursue, then Cowork drafts each selected motion using the appropriate MODULE above.

**Read** `references/pretrial-motion-action-plan.md` for the per-motion report fields, output filename and save-path conventions, and the Source Citation Mandate application.

---

## STEP 3 — Draft the Motion and Memorandum

For each motion type, generate two .docx files (Motion + Memorandum in Support) following the `docx` skill conventions and the shared-protocols boilerplate component sequence.

**Read** `references/drafting-and-review.md` for the document structure (Motion 2-3 pages, Memorandum 5-20 pages), filing conventions, and the cross-reference back to shared protocols.

---

## STEP 4 — Attorney Review & Integration

Apply the standard review flags (`[VERIFY]`, `[RESEARCH]`, `[ATTORNEY TO COMPLETE]`, `[STRATEGIC DECISION]`), save filed motions to the Pretrial Notebook, create the Clio review-and-file task, and update Case Brain with motion status. Hand off to companion skills for specialized motions.

**Read** `references/drafting-and-review.md` (Attorney Review section) for the full review-flag list, save locations, Clio task language, and companion skill handoff matrix.

---

## Guardrails

- **Never fabricate legal citations.** Flag any citation needing verification. Cross-check every cite against `references/caselaw-citations.md`, which flags known typos and stale cites in the bundled templates.
- **Attorney work product.** All outputs are drafts requiring attorney review.
- **Louisiana default.** Apply Louisiana statutes and 5th Circuit standards.
- **Template-First.** Always search DEVONthink before drafting from scratch. Bundled templates in `assets/templates/` are secondary — use when DEVONthink returns nothing useful or to cross-check formatting consistency. DEVONthink reflects the firm's most recent filings; bundled templates are static.
- **Reset the caption.** Bundled templates use 2nd JDC, 14th JDC, 19th JDC, and Orleans Parish CDC captions. Only `motion_for_speedy_trial_701.docx` uses 14th JDC (D&W's primary venue) — for any other filing, pull caption boilerplate from `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` rather than copying a template's caption forward.
- **Article renumbering.** La. C.Cr.P. articles have been renumbered (e.g., the old Art. 334 bail factors are now Art. 316). Always verify against the current code.
- **Route specialized motions correctly.** Suppression → `dw-suppression-motion-crim`. 404(b) → `dw-404b-opposition-crim`. Bond → `dw-bond-and-release-motion-crim`. New trial → `dw-appellate-error-monitor-crim` MODULE E. Appeal → `dw-appellate-error-monitor-crim` MODULE E. Don't draft these from this skill.
- **File intake hard stop.** Never skip Step 0.

---

## Output Location

Use the output path formula from `dw-shared-protocols-crim/references/output-path-formula.md`. Filed motions go to `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/`. The Pre-Trial Motion Action Plan (internal analysis, Step 2.5) goes to `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`. See shared protocols for CASE_ROOT resolution, filename conventions, and post-write reporting format.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **devonthink-search-protocol.md** — General DEVONthink search queries (Motions / General Motions / Reference Materials / NACDL / LACDL groups), catalog of known firm resources (Motions Practice OVERVIEW OUTLINE, CRIMINAL PLEADING INDEX, Complete Manual to Criminal Forms, LA Criminal Trial Practice Formulary, Criminal Procedure Handbook), and the Template Selection Protocol handoff
- **module-1-speedy-trial-701.md** — La. C.Cr.P. Art. 701 time-limits table, excludable-time list under Art. 701(B), five-step argument structure, and authorities (*State v. Reaves*, *State v. Rome*)
- **module-2-bill-of-particulars.md** — La. C.Cr.P. Art. 484-485 intake checklist, four-step argument structure, and *State v. DeJesus* authority
- **module-3-continuance.md** — La. C.Cr.P. Art. 707-714 ground-specific argument templates (discovery / witness / expert / new evidence) and *State v. Simpson* abuse-of-discretion standard
- **module-4-motion-to-compel.md** — La. C.Cr.P. Art. 716-729 / 729.3 intake checklist, five-element argument structure, *Brady* / *Kyles* authorities, and `dw-brady-giglio-auditor-crim` Report 7 integration
- **module-5-6-severance.md** — La. C.Cr.P. Art. 495.1 / 704 (offenses + defendants), *State v. Brooks*, *Bruton v. United States*, *Zafiro v. United States* authorities
- **module-7-change-of-venue.md** — La. C.Cr.P. Art. 622 intake checklist (publicity, community sentiment, victim prominence, pool size), *State v. David*, *Skilling v. United States* authorities
- **module-8-recusal.md** — La. C.Cr.P. Art. 671-674 / La. Code Jud. Conduct Canon 3 intake checklist, mandatory vs. discretionary distinction, *Liteky v. United States* authority
- **module-9-quash-bill.md** — La. C.Cr.P. Art. 485 / 532 / 571-576 grounds list, prescription-period table (no prescription / 6 / 4 / 2 years), and *State v. Byrd* authority
- **module-10-competency-evaluation.md** — La. C.Cr.P. Art. 641-649 sanity-commission intake checklist and *Drope v. Missouri* / *Dusky v. United States* authorities
- **module-11-reveal-the-deal.md** — DEVONthink snitch/cooperation document catalog, `dw-brady-giglio-auditor-crim` integration note, and authorities (*Brady*, *Giglio*, *Roviaro*, *State v. Broadway*)
- **pretrial-motion-action-plan.md** — Per-motion report fields (Motion Type, Specific Evidence, Likelihood, Assessment), output filename and save-path conventions, Source Citation Mandate application
- **drafting-and-review.md** — Motion + Memorandum drafting structure, full review-flag list, save locations, Clio task language, companion skill handoff matrix, and output-location summary
