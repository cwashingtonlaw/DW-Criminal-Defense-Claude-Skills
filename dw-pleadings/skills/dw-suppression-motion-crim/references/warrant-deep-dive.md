# Warrant Deep-Dive — Search Warrant Constitutional Audit

Read by `dw-suppression-motion-crim` at the WARRANT DEEP-DIVE step (Search & Seizure — Audit Mode or Motion Mode) whenever a search warrant is uploaded or referenced; it holds the four-corners probable cause audit, particularity & scope audit, Franks analysis, execution audit, Leon preemption, the Warrant Audit Report output spec, and the Search Warrant Legal Standards Quick Reference table.

#### Four Corners Probable Cause Audit

The affidavit must establish probable cause **within its four corners** — information known to the judge at signing.

**Conclusory Language Scan** — Classify every factual assertion:
- **Factual:** Specific, verifiable facts with source attribution
- **Conclusory:** Bare assertions without supporting facts (e.g., "Based on my training and experience, the residence is used for drug trafficking")
- **Boilerplate:** Generic law enforcement language recycled across warrants
- **Hearsay (attributed):** Secondhand info with source identified and reliability established
- **Hearsay (unattributed):** Secondhand info without adequate source reliability

Flag every conclusory and boilerplate statement — these are the weak joints. An affidavit built primarily on conclusions fails probable cause under *Illinois v. Gates*, 462 U.S. 213 (1983).

**Nexus Analysis** — Probable cause requires nexus between three elements:
1. **Crime** — evidence that a crime has been or is being committed
2. **Evidence** — specific items that constitute evidence of that crime
3. **Location** — reason to believe the evidence is at the place to be searched

The most common deficiency is a weak nexus to **location**. When the affidavit uses "training and experience" to bridge the gap, flag as conclusory nexus.

**Informant Reliability (Aguilar-Spinelli / Gates)** — If affidavit relies on CI/anonymous tip:
- Basis of Knowledge: How does the CI know? Personal observation? Secondhand?
- Reliability / Track Record: Prior accurate information? How many times?
- Corroboration: What independent police work corroborated the CI's claims?
- Staleness of CI Contact: When did the CI last observe the activity?

**Staleness Analysis** — Flag as stale when:
- Single drug transaction > 2 weeks before warrant with no intervening surveillance
- Property crime evidence > 30 days old with no evidence of continued possession
- Digital evidence references > 60-90 days old
- Affidavit's most recent factual allegation is substantially older than the warrant date

#### Particularity & Scope Audit

- **Place:** Specific, identifiable location? Multi-unit buildings — unit specified? Vehicles — identified by make/model/plate/VIN? Digital devices — specific devices or "any and all"?
- **Things to Be Seized:** Specific categories tied to the crime? Or catch-all language ("any and all evidence," "any contraband")? Flag overbreadth per *Groh v. Ramirez*, 540 U.S. 551.
- **Scope of Execution vs. Authorization:** Compare warrant scope against what actually happened. Officers search beyond authorized areas? Seize items not described? Digital examination exceed temporal/subject-matter scope?

#### Franks v. Delaware Analysis

Under *Franks v. Delaware*, 438 U.S. 154 (1978):

**Prong 1:** Affiant made false statement or omitted material facts **deliberately or with reckless disregard for truth**.
**Prong 2:** If false statement excised (or omission added), remaining content insufficient for probable cause.

**What to look for:**
- Dates/times/locations not matching police reports or other discovery
- Affiant's observations contradicted by body cam, radio logs, or other officers
- Overstated CI reliability
- Mischaracterized lab results or criminal history
- Material omissions: CI criminal history, exculpatory surveillance, failed corroboration attempts, other suspects, changed tenants

Cross-reference every factual claim against all discovery. Flag: `[FRANKS CANDIDATE — [description]]`

#### Execution Audit

- **Knock-and-Announce:** Did officers comply? Wait time? (*Wilson v. Arkansas*; *United States v. Banks* — 15-20 seconds minimum). No-knock authorization: specific articulable facts or boilerplate?
- **Timing:** Night warrant authorized per La. C.Cr.P. Art. 163? Executed within 10-day window?
- **Force:** Proportionate? Occupants detained — how long? Non-targets (children, elderly) present?
- **Return & Inventory:** Complete inventory prepared? Filed with court? Matches evidence room? Items in evidence not on inventory (or vice versa)?

#### Good Faith Exception (Leon) Preemption

For each deficiency, assess whether *Leon*, 468 U.S. 897 (1984) saves the warrant. Leon does NOT apply when:
1. Magistrate was misled by affiant's false statements (Franks)
2. Magistrate wholly abandoned judicial role (rubber stamp)
3. Affidavit "so lacking in indicia of probable cause" that belief in it was entirely unreasonable — the **bare bones** affidavit
4. Warrant "so facially deficient" that executing officers could not presume it valid

#### Warrant Audit Report Output (Audit Mode Only)

When in Audit Mode, produce a .docx report with:
- Warrant Overview (court, judge, affiant, dates, location, authorized items)
- Section 1: Probable Cause Analysis (four corners, conclusory findings, nexus, informant reliability, staleness) — Rating: SUFFICIENT / DEFICIENT / BARE BONES
- Section 2: Particularity & Scope — Rating: ADEQUATE / DEFICIENT / FACIALLY INVALID
- Section 3: Franks Analysis — Viability: STRONG / ARGUABLE / WEAK / N/A
- Section 4: Execution Audit — Rating: COMPLIANT / DEFICIENT / CRITICAL VIOLATIONS
- Section 5: Leon Preemption — Survivability: LIKELY / ARGUABLE / UNLIKELY
- Section 6: Suppression Roadmap (constitutional basis, factual support, applicable law for each deficiency)
- Section 7: Cross-Examination Ammunition (for affiant and executing officers)
- Section 8: Defense Action Items (motions, Franks hearing request, missing discovery, expert needs)
- Section 9: Discovery Gap Report

File naming: `[3-digit prefix] - Search Warrant Audit - [Client Last Name].docx`
Location: `02 - Pretrial Notebook/03 - Case Analysis & Notes`
Mark: per `attorney-work-product-marking.md` in shared protocols (internal deliverable)

After producing the audit report, offer: *"This warrant has [X] deficiencies. Want me to draft the suppression motion based on these findings?"*

### Search Warrant Legal Standards Quick Reference

| Issue | Authority |
|-------|-----------|
| Probable cause (totality of circumstances) | *Illinois v. Gates*, 462 U.S. 213 (1983) |
| Particularity requirement | U.S. Const. Amend. IV; La. Const. Art. I, Sec. 5 |
| Franks hearing (false affidavit) | *Franks v. Delaware*, 438 U.S. 154 (1978) |
| Good faith exception | *United States v. Leon*, 468 U.S. 897 (1984) |
| Bare bones affidavit (no good faith) | *United States v. Satterwhite*, 980 F.2d 317 (5th Cir. 1992) |
| Knock and announce | *Wilson v. Arkansas*, 514 U.S. 927 (1995) |
| Wait time before forced entry | *United States v. Banks*, 540 U.S. 31 (2003) |
| Overbreadth / facial invalidity | *Groh v. Ramirez*, 540 U.S. 551 (2004) |
| Staleness of probable cause | *United States v. Bremner*, 195 F.3d 221 (5th Cir. 1999) |
| Informant reliability | *Illinois v. Gates*; *Aguilar v. Texas*; *Spinelli v. United States* |
| Cell phone search warrant required | *Riley v. California*, 573 U.S. 373 (2014) |
| Digital evidence particularity | *United States v. Ganias*, 824 F.3d 199 (2d Cir. 2016) |
| Nighttime search warrants (LA) | La. C.Cr.P. Art. 163 |
| Warrant execution window (LA) | La. C.Cr.P. Art. 163 (10 days) |
| Return and inventory requirement | La. C.Cr.P. Art. 167 |
| Anticipatory warrants | *United States v. Grubbs*, 547 U.S. 90 (2006) |
