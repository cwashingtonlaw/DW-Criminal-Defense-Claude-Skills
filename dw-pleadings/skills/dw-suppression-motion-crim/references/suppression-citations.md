# Suppression Motion Citation Library — Louisiana & Federal Authority

**For use by `dw-suppression-motion-crim`. Internal reference. Cite-check before filing.**

This library is the Layer 1 (training-knowledge) starting point for drafting suppression motions and warrant audit reports. It is organized by the four suppression categories the parent skill handles: Search & Seizure (4th Amendment), Statements (5th Amendment), Identification (14th Amendment Due Process), and Fruit of the Poisonous Tree (*Wong Sun*). **Verify every citation against current Westlaw/Fastcase output before filing — federal and Louisiana suppression law has been refined repeatedly in recent years.**

---

## 0. Firm Authority — `Law Library-Criminal` DEVONthink Database

The firm's `Law Library-Criminal` database is the operational source for suppression work. Unlike 404(B) (where the firm keeps the foundational cases as standalone PDFs), suppression authority lives primarily in firm-drafted motion templates organized by category. Each template embeds the relevant federal and Louisiana authority — when drafting, lift the citation skeleton from the most analogous template, then refresh the case law against current research.

**Database root:** [Law Library-Criminal](x-devonthink-item://3C34A487-54B3-4D41-91EF-B83DC32F31C3)

**Key groups by suppression category:**

| Category | DEVONthink Group | What's there |
|---|---|---|
| Search & Seizure (4th Am.) — *motions* | [Motions / 4th Amendment Issues](x-devonthink-item://51CAE66C-E7AA-4BFE-9E34-9D3046F04D7F) | 60+ motion templates: auto stops, warrantless searches, Franks hearings, cell-site, geofence, FISA, drone surveillance |
| Search & Seizure — *case law / treatises* | [Search & Seizure](x-devonthink-item://EB955B5A-934B-439E-A5CF-CB5F40505E4B) | Subgroups for SILA, warrantless search, no-reasonable-grounds-to-stop; plus the *Automobile_Suppression* PDF and search-and-seizure outline |
| Statements (5th Am.) | [Motions / 5th Amendment Issues](x-devonthink-item://8BAFE1E0-BAA4-48C7-84EE-1C94366CFF3A) | Miranda suppression motions; statement-suppression templates |
| False Confessions | [Motions / False Confessions](x-devonthink-item://961A20A0-0591-49E9-B7AC-7DC9A51373E9) | Voluntariness and false-confession-specific templates |
| Identification | [Motions / Eyewitness Identification](x-devonthink-item://ACF16B84-8632-4AED-9243-24E9B00D2F40) | Wade/reliability motions, expert-notice templates, Innocence Project amicus, Manson framework briefs |
| Treatise — Louisiana Criminal Trial Practice | [Open formulary](x-devonthink-item://F43B9C6D-3D5A-44D1-B228-520090BBEEEF) | Primary template source per dw-shared-protocols-crim template selection protocol |

**Layered workflow:**

1. Read this file (Layer 1) — well-established baseline of federal + Louisiana authority.
2. Open the DEVONthink groups above and identify the firm motion template closest to the case facts (Layer 1.5 — firm authority). Lift its citation skeleton.
3. Run the DEVONthink searches in `dw-suppression-motion-crim/SKILL.md` Step "Layer 2" against this database for adjacent prior filings.
4. Web/Westlaw search (Layer 3) for any case decided after the firm's last template revision — particularly important post-*Carpenter*, post-*Riley*, post-*Strieff*.

**High-value firm templates to start from** (most-used skeletons for the four categories):

- **Search & Seizure — auto stops:** [Memo in Support of Motion to Suppress Evidence from Illegal Automobile Stop](x-devonthink-item://97303EBF-A0CB-4C4A-B02C-75DC90AB2D7E) · [Motion to Suppress Evidence from Warrantless Auto Stop](x-devonthink-item://7F6E61CE-EF0C-4D52-ADA6-DC5F2CFA5BF6) · [Motion to Suppress Traffic Stop](x-devonthink-item://D88CE6F1-5A2C-46E8-B3CC-09761C395818)
- **Search & Seizure — warrants & Franks:** [Motion for Franks Hearing](x-devonthink-item://D23D7D0E-EC14-459C-B21D-636B78C523CA) · [Motion to Suppress Custodial Statements and Evidence Seized from Invalid Search Warrant](x-devonthink-item://F567A6B7-3732-4E78-B83D-CDB0853A4684) · [Memo in Support of Motion to Suppress Evidence Seized from Home Pursuant to Warrant](x-devonthink-item://C98A5BB1-0FA9-404C-81A2-D12CCF3889DF)
- **Search & Seizure — digital:** [Motion to Suppress Digital Information from Cell Phone](x-devonthink-item://F81BE5FB-8C3A-45DD-B626-E30C87E223AF) · [Motion to Suppress Cell Phone Evidence from Warrantless Search](x-devonthink-item://604DF1D1-7FE9-4A25-AC0D-ADD42BD058D8) · [Motion to Suppress Evidence Obtained from Google Geofence Reverse Location Search Warrant](x-devonthink-item://F9BD4589-EC70-4349-8038-C86C7333F3F0) · [4th Amendment Motions Primer for Digital Evidence — OUTLINE](x-devonthink-item://BAEFD4E6-153F-4572-B88B-42D9608FE988)
- **Search & Seizure — overview outline:** [Motions to Suppress — OUTLINE](x-devonthink-item://CEB2A270-6790-48E5-BAE4-F1DCCA018BA4)
- **Statements (Miranda / Voluntariness):** [Motion to Suppress Statements and Physical Evidence Due to Violation of Miranda](x-devonthink-item://6DAD1134-8123-40F8-B116-9E3EDD625BD4) · [Memo in Support of Motion to Suppress Testimony of Defendant](x-devonthink-item://2CBE1485-53DD-43DA-8969-A0485FDE4199)
- **Identification:** [Motion to Suppress Identification Testimony or for Wade and Reliability Hearing](x-devonthink-item://517BF592-6215-481F-BA94-20871052E618) · [Memo of Law in Support of Motion to Suppress In-Court and Out of Court Identification](x-devonthink-item://459837CA-05FF-4B26-B887-7A628BF8D87A) · [Motions to Suppress in Eyewitness Identification Cases — OUTLINE](x-devonthink-item://BF238FDF-110F-4F69-B907-3C722BAB89DD) · [Brief Of Amicus Curiae The Innocence Project — Eyewitness ID](x-devonthink-item://1DA86715-1D00-4161-B5A2-B316C94B6C60)

The federal foundational cases cited below in Sections 1–4 (*Mapp*, *Katz*, *Carpenter*, *Riley*, *Franks*, *Miranda*, *Manson*, *Wong Sun*, etc.) are **not** stored as standalone PDFs in the firm database — they are cited within the templates above. When you need full text, pull from Westlaw/Fastcase. The motion templates are the firm's operational citation source.

---

## Constitutional Foundations

| Right | Federal | Louisiana |
|---|---|---|
| Search & Seizure | U.S. Const. amend. IV | La. Const. Art. I, § 5 |
| Self-Incrimination | U.S. Const. amend. V | La. Const. Art. I, § 13 |
| Due Process / ID | U.S. Const. amend. XIV | La. Const. Art. I, § 2 |
| Right to Counsel | U.S. Const. amend. VI | La. Const. Art. I, § 13 |

**Important framing note:** La. Const. Art. I, § 5 is *more protective* than the federal Fourth Amendment in several respects, including standing (Louisiana retains the "automatic standing" rule for possessory offenses) and the scope of Article 5's privacy guarantee. Always argue the Louisiana provision in addition to the federal amendment — preserving an independent state-constitutional ground prevents a U.S. Supreme Court reversal from disposing of the issue.

---

## Category 1 — Search & Seizure (4th Amendment / La. Const. Art. I, § 5)

### A. Foundational Authority

- **Mapp v. Ohio, 367 U.S. 643 (1961)** — Exclusionary rule applies to states.
- **Katz v. United States, 389 U.S. 347 (1967)** — Reasonable expectation of privacy framework.
- **Terry v. Ohio, 392 U.S. 1 (1968)** — Stop-and-frisk standard; reasonable suspicion required.
- **Carpenter v. United States, 138 S. Ct. 2206 (2018)** — Cell-site location information requires a warrant.
- **Riley v. California, 573 U.S. 373 (2014)** — Cell phone search incident to arrest requires a warrant.
- **State v. Surtain, 2009-1835 (La. 3/16/10), 31 So. 3d 1037** — Louisiana adopts and applies *Carpenter* / 4th Amendment analysis to digital searches.

### B. Warrant Requirement and Probable Cause

- **Illinois v. Gates, 462 U.S. 213 (1983)** — Totality-of-circumstances probable cause standard for search warrants.
- **Aguilar v. Texas, 378 U.S. 108 (1964)** and **Spinelli v. United States, 393 U.S. 410 (1969)** — Earlier two-prong informant-reliability test, replaced by *Gates* but still useful for parsing what the affidavit actually establishes.
- **State v. Casey, 99-0023 (La. 1/26/00), 775 So. 2d 1022** — Louisiana applies *Gates* totality test; affidavits must establish a fair probability that contraband or evidence will be found at the place to be searched.
- **State v. Manso, 449 So. 2d 480 (La. 1984)** — Probable cause must be assessed within the four corners of the affidavit; bare conclusions are not enough.

### C. Particularity Requirement

- **Maryland v. Garrison, 480 U.S. 79 (1987)** — Particularity protects against general warrants. The warrant must describe the place to be searched and items to be seized with reasonable specificity.
- **Andresen v. Maryland, 427 U.S. 463 (1976)** — Generic descriptions ("evidence of crime") are insufficient.
- **State v. Casey, 775 So. 2d at 1031** — Louisiana particularity standard; warrants describing whole computers, phones, or digital storage without protocol limits are constitutionally suspect.
- **In digital search context:** The defense should argue that warrants for "all data on the device" are general warrants in violation of particularity. *Riley* (above) supports tighter limits on cell phone searches.

### D. Franks Challenges (Affidavit Falsity)

- **Franks v. Delaware, 438 U.S. 154 (1978)** — Two-part test:
  1. Defendant makes a substantial preliminary showing that the affidavit contained false statements made knowingly or with reckless disregard for the truth.
  2. The false statements were necessary to the finding of probable cause.
  When both are met, the defendant is entitled to an evidentiary hearing; if the false statements are excised and probable cause no longer exists, the warrant must be quashed.
- **State v. Lehnen, 403 So. 2d 683 (La. 1981)** — Louisiana adopts *Franks*.
- **State v. Byrd, 568 So. 2d 554 (La. 1990)** — Louisiana refines the substantial preliminary showing standard.

**Defense tactic:** Look for omissions as well as misstatements. Officers who knew exculpatory facts (e.g., the informant had failed prior controlled buys, the surveillance was actually inconclusive) and omitted them from the affidavit can be challenged just as much as officers who lied affirmatively.

### E. Execution Compliance

- **Wilson v. Arkansas, 514 U.S. 927 (1995)** — Knock-and-announce rule.
- **Hudson v. Michigan, 547 U.S. 586 (2006)** — Knock-and-announce violation does NOT trigger federal exclusion. **However**, La. Const. Art. I, § 5 may provide independent protection. **Louisiana practitioners should preserve the state-constitutional argument**.
- **State v. Loyd, 489 So. 2d 898 (La. 1986)** — Louisiana statutory knock-and-announce authority (La. C.Cr.P. Art. 224).
- **Garrison, supra** — Officers must stop the search if they realize they are in the wrong place.

### F. Warrant Exceptions (When the State Argues No Warrant Needed)

- **Consent:** *Schneckloth v. Bustamonte*, 412 U.S. 218 (1973) (voluntariness); *State v. Owen*, 453 So. 2d 1202 (La. 1984) (Louisiana voluntariness).
- **Search incident to arrest:** *Chimel v. California*, 395 U.S. 752 (1969); narrowed by *Arizona v. Gant*, 556 U.S. 332 (2009).
- **Automobile exception:** *Carroll v. United States*, 267 U.S. 132 (1925); *State v. Tatum*, 466 So. 2d 29 (La. 1985).
- **Exigent circumstances:** *Kentucky v. King*, 563 U.S. 452 (2011); but the State cannot manufacture exigency.
- **Plain view:** *Horton v. California*, 496 U.S. 128 (1990) — must satisfy three prongs: lawful presence, immediately apparent incriminating character, lawful right of access.
- **Inventory searches:** *Colorado v. Bertine*, 479 U.S. 367 (1987); but the search must follow standardized policy.

### G. The Leon Good-Faith Exception

- **United States v. Leon, 468 U.S. 897 (1984)** — Federal good-faith exception when officers reasonably rely on a warrant later found defective.
- **State v. Casey, supra** — Louisiana adopted *Leon* in a limited form.
- **Limits on Leon (Leon's four exceptions):** No good faith when (1) the affidavit was knowingly false, (2) the magistrate abandoned the neutral role, (3) the affidavit was so lacking in probable cause that no reasonable officer could rely on it, (4) the warrant was so facially deficient that no reasonable officer could presume validity.
- **Defense argument:** Most warrant audits should be framed to fall into Leon exceptions 3 or 4 — the "bare bones" affidavit and the facially deficient warrant. Courts more readily find these than knowing falsity.

### H. Standing

- **United States v. Salvucci, 448 U.S. 83 (1980)** — Federal standing requires defendant to show personal Fourth Amendment expectation of privacy.
- **State v. Owen, 453 So. 2d 1202 (La. 1984)** — Louisiana retains "automatic standing" for possessory offenses under La. Const. Art. I, § 5. **This is a significant Louisiana-specific advantage; always argue it in possessory cases.**

---

## Category 2 — Statements (5th Amendment / La. Const. Art. I, § 13)

### A. Custodial Interrogation Framework

- **Miranda v. Arizona, 384 U.S. 436 (1966)** — Custodial interrogation requires advisement of rights.
- **Rhode Island v. Innis, 446 U.S. 291 (1980)** — Defines "interrogation" to include the functional equivalent of express questioning.
- **Berkemer v. McCarty, 468 U.S. 420 (1984)** — Routine traffic stop is not custody for *Miranda* purposes. **But** prolonged or escalating stops can become custodial.
- **State v. Anderson, 379 So. 2d 735 (La. 1980)** — Louisiana custody standard.
- **State v. Manning, 2003-1982 (La. 10/19/04), 885 So. 2d 1044** — Adopts and applies federal custody framework in Louisiana.

### B. Voluntariness

- **Colorado v. Connelly, 479 U.S. 157 (1986)** — Voluntariness requires police coercion; mental illness alone does not render confession involuntary under federal law.
- **State v. Vaccaro, 411 So. 2d 415 (La. 1982)** — Louisiana voluntariness; State must prove beyond a reasonable doubt that the statement was free and voluntary.
- **State v. Caston, 2014-2056 (La. App. 1st Cir. 9/18/15), 182 So. 3d 122** — Voluntariness factors: age, intelligence, education, mental state, length of detention, repeated interrogation, deprivation of food/sleep, threats, promises.

**Note on burden of proof:** Louisiana places the burden on the State to prove voluntariness *beyond a reasonable doubt* — a higher burden than the federal preponderance standard. **Always cite the Louisiana standard for state-court suppression hearings.**

### C. Waiver of Miranda Rights

- **Berghuis v. Thompkins, 560 U.S. 370 (2010)** — Implicit waiver allowed; silence is not invocation.
- **Davis v. United States, 512 U.S. 452 (1994)** — Invocation of right to counsel must be unambiguous.
- **State v. Lavalais, 2014-1209 (La. App. 3d Cir. 5/6/15), 165 So. 3d 295** — Applies *Davis* in Louisiana.
- **Edwards v. Arizona, 451 U.S. 477 (1981)** — Once counsel is invoked, interrogation must cease until counsel is present or the defendant initiates further communication.
- **State v. Cousan, 94-2503 (La. 11/25/96), 684 So. 2d 382** — Louisiana adopts *Edwards*.

### D. Promises, Threats, and Inducement

- **State v. Quertain, 411 So. 2d 415 (La. 1982)** — A confession induced by promises of leniency is involuntary as a matter of law.
- **State v. Dison, 396 So. 2d 1254 (La. 1981)** — Even subtle promises ("we'll talk to the DA") can render a confession involuntary.
- **State v. Bourque, 622 So. 2d 198 (La. 1993)** — Threats of prosecution against family members render confessions involuntary.

### E. Right to Counsel — 5th vs. 6th Amendment

- **Miranda right to counsel** — 5th Amendment, attaches at custodial interrogation.
- **Massiah v. United States, 377 U.S. 201 (1964)** — 6th Amendment right to counsel attaches at formal charge / first appearance.
- **State v. Hattaway, 621 So. 2d 796 (La. 1993)** — Louisiana 6th Amendment / Art. I, § 13 framework.

### F. Custodial Interview / Reid Technique Concerns

- **State v. Caston, supra** — Recognizes coercive techniques as factors in voluntariness analysis.
- See `dw-confession-interrogation-auditor-crim/references/` for the firm's full technique-analysis reference if available.

---

## Category 3 — Identification (14th Amendment Due Process)

### A. The Manson Framework

- **Neil v. Biggers, 409 U.S. 188 (1972)** — Five-factor reliability test:
  1. Witness's opportunity to view the perpetrator
  2. Witness's degree of attention
  3. Accuracy of prior description
  4. Witness's level of certainty
  5. Time between crime and confrontation
- **Manson v. Brathwaite, 432 U.S. 98 (1977)** — Refines reliability framework; suggestiveness alone is not enough — admissibility turns on overall reliability.
- **State v. Prudholm, 446 So. 2d 729 (La. 1984)** — Louisiana adopts and applies *Biggers* / *Manson*.

### B. Suggestiveness Doctrines

- **Stovall v. Denno, 388 U.S. 293 (1967)** — Showup IDs are inherently suggestive but may be permitted in narrow circumstances.
- **United States v. Wade, 388 U.S. 218 (1967)** — Right to counsel at post-indictment lineup.
- **Kirby v. Illinois, 406 U.S. 682 (1972)** — *Wade* right does not apply pre-indictment.
- **State v. Coleman, 2014-0402 (La. 2/26/16), 188 So. 3d 174** — Louisiana suggestiveness analysis; cross-racial ID concerns.

### C. Photo Array Issues

- **Simmons v. United States, 390 U.S. 377 (1968)** — Photo array suggestiveness analyzed under same framework.
- **State v. Henderson** — *(For New Jersey practitioners; persuasive elsewhere)* the **N.J. Supreme Court's *Henderson* decision (208 N.J. 208 (2011))** modernized the reliability framework to incorporate scientific research on memory, witness confidence inflation, and cross-racial bias. While Louisiana has not adopted *Henderson*, defense counsel can cite it for persuasive value, especially in conjunction with expert testimony.

### D. Suggestiveness Indicators

- Filler photos differ in age, race, body type, or photographic quality
- Subject's photo is highlighted, larger, or in a different format
- Officer comments before the ID ("we have a suspect")
- Officer feedback after the ID ("good, that's the guy")
- Single-subject showup absent exigency
- ID procedure performed by case officer rather than blind administrator

### E. Cross-Racial Identification

- **State v. Cromer, 365 So. 2d 1320 (La. 1978)** — Louisiana recognizes the unreliability of cross-racial identification but generally leaves it to jury weight rather than admissibility.
- Defense counsel should consider:
  - Expert testimony on cross-racial ID under La. C.E. Art. 702
  - Jury instruction on cross-racial ID factors
  - Pretrial motion to suppress where suggestiveness compounds the cross-racial reliability concern

---

## Category 4 — Fruit of the Poisonous Tree

### A. Foundational Doctrine

- **Wong Sun v. United States, 371 U.S. 471 (1963)** — Evidence derived from a constitutional violation is excluded as "fruit of the poisonous tree."
- **State v. Gibson, 391 So. 2d 421 (La. 1980)** — Louisiana adopts *Wong Sun*.

### B. Exceptions to Fruit Doctrine

- **Independent source doctrine:** *Murray v. United States*, 487 U.S. 533 (1988) — If the evidence was obtained from a source independent of the constitutional violation, it is admissible.
- **Inevitable discovery:** *Nix v. Williams*, 467 U.S. 431 (1984) — If the evidence would inevitably have been discovered through lawful means, it is admissible. *State v. Welsh*, 540 So. 2d 1043 (La. 1989) (Louisiana adoption).
- **Attenuation:** *Brown v. Illinois*, 422 U.S. 590 (1975) — Sufficient attenuation between the violation and discovery purges the taint. Factors: temporal proximity, intervening circumstances, purpose and flagrancy of the misconduct.
- **Utah v. Strieff, 136 S. Ct. 2056 (2016)** — Discovery of an outstanding warrant during an unlawful stop attenuates the taint. **Louisiana courts may apply *Strieff* but defense should argue the state-constitutional analysis under La. Const. Art. I, § 5 may be more protective.**

### C. Application

- **Identify the predicate violation first** (the unlawful stop, search, or interrogation).
- **Trace each piece of derivative evidence** back to the predicate.
- **For each derivative piece**, the State must establish independent source, inevitable discovery, or attenuation — or the evidence is excluded.

---

## Common Procedural Authority

### Standing to File

- **La. C.Cr.P. Art. 703** — Authority for motion to suppress.
- **La. C.Cr.P. Art. 521** — Procedure for pretrial motions.
- **State v. Robinson, 386 So. 2d 1374 (La. 1980)** — Court must hold contradictory hearing on motion to suppress before trial.

### Burden of Proof at Suppression Hearing

| Issue | Burden | Authority |
|---|---|---|
| Warrantless search | State must prove warrant exception applies | *State v. Tatum*, 466 So. 2d 29 (La. 1985) |
| Warrant search | Defendant must show probable cause defect | *State v. Casey*, 775 So. 2d 1022 |
| Confession voluntariness | State must prove voluntariness BRD | *State v. Vaccaro*, 411 So. 2d 415 |
| ID suggestiveness | Defendant must show suggestive procedure first; burden then shifts to State to show reliability | *Manson*; *Prudholm* |

### Standard of Review on Appeal

- **Mixed question** — Trial court's findings of fact are reviewed for manifest error / clear error; legal conclusions are reviewed de novo.
- **State v. Wells, 2008-2262 (La. 7/6/10), 45 So. 3d 577** — Louisiana applies abuse-of-discretion standard to ID suggestiveness rulings.

---

## Federal-Court Authority (for Federal Cases or Persuasive Value)

- **United States v. Leon, supra** — Good-faith exception.
- **United States v. Herring, 555 U.S. 135 (2009)** — Negligent recordkeeping does not trigger exclusion.
- **Davis v. United States, 564 U.S. 229 (2011)** — Reasonable reliance on then-binding precedent does not trigger exclusion.
- **United States v. Beck, 588 F.2d 549 (5th Cir. 1979)** — 5th Circuit standard for stale probable cause.
- **United States v. Allen, 625 F.3d 830 (5th Cir. 2010)** — 5th Circuit knock-and-announce / forfeiture analysis.

---

## Citation Formatting Notes (Louisiana Style)

- Use the Louisiana Citation Manual format. See `dw-shared-protocols-crim/references/louisiana-citation-style.md` for the firm's standardized format.
- For Louisiana Supreme Court decisions post-1994, include the public-domain citation: `State v. Smith, 2018-1234 (La. 6/30/19), 274 So. 3d 1`.
- Pin cite to specific pages when quoting or paraphrasing.
- For Court of Appeal decisions, identify the circuit: `State v. Smith, 18-456 (La. App. 1st Cir. 6/30/19), 274 So. 3d 100`.
- Federal: standard Bluebook format. *United States v. Leon*, 468 U.S. 897, 922 (1984).

---

## Recent Authority — Verify Currency Before Filing

This section is intentionally minimal. **Always run a current Westlaw or Fastcase search for each issue you're arguing**, particularly on:
- Cell phone, cell-site, and digital search authority (rapidly evolving post-*Carpenter*, *Riley*)
- The interaction of *Strieff* with state constitutional law
- Knock-and-announce remedies in Louisiana
- Right to counsel during digital extraction processes

After web/DEVONthink search, append current findings to the Memorandum with full citation strings.

---

*Last reviewed: 2026-04-29. Maintained by D&W. Add new citations under the appropriate category. Cite-check all authorities against current Westlaw/Fastcase output before filing — this library is a starting point, not a substitute for current research.*
