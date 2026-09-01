# Parole Revocation — Committee on Parole Framework (La. R.S. 15:574.7–574.11)

Parole revocation is an **administrative proceeding before the Committee on Parole** (Board of Pardons and Committee on Parole), not the sentencing court. The Morrissey floor applies directly. Statutory citations below were checked against published Louisiana text in August 2026; subsection letters shift between amendments, so cite to the article generally or confirm the subsection in the current text before filing.

**Landscape note:** 2024 Second Extraordinary Session legislation sharply restricted parole eligibility for offenses committed **on or after August 1, 2024** [VERIFY CITATION — confirm the act number of the 2024 2nd Ex. Sess. parole-restriction act], and amended the revocation statute (Acts 2024, 2nd Ex. Sess., No. 8; further amended by Acts 2025, No. 158, eff. June 8, 2025). Most current revocation clients were released under pre-2024 law — confirm which regime governs the client's release and violation dates.

## R.S. 15:574.7 — Custody and supervision; violations; administrative sanctions

- Parolees remain in the legal custody of DPS&C under Division of Probation and Parole supervision.
- On an alleged violation the parolee **may be arrested and must be given a prerevocation (preliminary) hearing within a reasonable time, at or reasonably near the place of the alleged violation or arrest, to determine probable cause to detain pending the committee's orders** — the codified Morrissey preliminary hearing. Audit whether it happened, where, when, and what evidence was presented; a skipped or rubber-stamped prerevocation hearing is a lead issue.
- The statute also authorizes **administrative sanctions** for parole technical violations parallel to Art. 899.1 (waiver + admission + consent; capped jail sanctions) [VERIFY — confirm the current parole administrative-sanction caps before quoting values].

## The parole hold / detainer

A parole-violation warrant lodges as a **detainer** ("parole hold") that blocks release on any new charge's bond — there is no bail from a parole hold. Practical consequences the memo must address: (a) time pressure runs against the client while the hold pins them in jail; (b) custody time on the hold feeds the credit math (Module D); (c) the only pressure valves are the prerevocation hearing, a request to the committee to lift the hold, and speed on the final hearing.

## R.S. 15:574.9 — Revocation of parole; committee panels; return-to-custody hearing; credit; technical revocation

- **Panels:** revocation is decided by committee panels; check quorum/vote requirements in the current text [VERIFY — confirm current panel-composition rules].
- **Return-to-custody / final hearing:** the parolee is entitled to a final revocation hearing before the committee. A **written waiver of the hearing constitutes an admission** and results in revocation — never let a client sign one unreviewed.
- **Counsel:** the parolee has the right to consult with and be represented by retained counsel or counsel appointed under La. R.S. 15:179 [VERIFY CITATION — confirm the appointment cross-reference].
- **Timing limit:** other than for a felony conviction committed while on parole, revocation action **must be initiated before the parole term expires**. Late-initiated revocations are void — always run the supervision-expiration date (reconcile with the `dw-deadline-engine-crim` CLOCK STATUS block).
- **Technical-violation revocation caps — current text (as amended through Acts 2025, No. 158):** 1st technical violation ≤ **90 days**; 2nd ≤ **120 days**; 3rd or subsequent ≤ **180 days**; substance-abuse treatment program service capped at **180 days** [VERIFY — confirm each figure in the current text before quoting]. Served **without diminution of sentence or credit for time served prior to the revocation** [VERIFY — confirm this credit language]. The term runs from the date the committee orders revocation; on completion the offender **returns to active parole supervision** for the remainder of the original term. **Exclusions:** the caps do NOT apply to offenders on parole for a crime of violence (La. R.S. 14:2(B)) or a sex offense (La. R.S. 15:541). *Justice-Reinvestment-era versions used far shorter tiers (15/30/45 days [VERIFY — confirm the prior-version values]) — version-check against the violation date.*
- **Credit on full (non-technical) revocation:** the parolee serves the remainder of the sentence; treatment of "street time" (time served in good standing on parole) has changed across amendments — the 2017 Justice Reinvestment reforms granted credit for time on parole in good standing, and post-2024 amendments must be checked before computing [VERIFY — confirm current R.S. 15:574.9 credit-for-time-served text for full revocations]. **No credit for any period the parolee was a fugitive from justice.** Credit is given for pre-hearing time in **actual custody** on the violation (local, state, or out-of-state facility). Worked example: `references/module-d-credit-and-street-time.md`.

## R.S. 15:574.10 — Felony conviction while on parole

Conviction (in Louisiana, another state, federal, or foreign court) of an offense committed while on parole that would be a Louisiana felony → **parole is deemed revoked automatically**; no discretionary decision remains. Defense consequences: (a) the fight shifts entirely to the new charge (Module F) — a plea to a felony on the new case *is* a parole revocation, and that consequence belongs in every plea-advice memo (route to `dw-plea-negotiation-analyzer-crim`); (b) misdemeanor resolutions of the new charge avoid automatic revocation.

## R.S. 15:574.11 — Finality; judicial review

- Committee parole decisions are generally final; the statute's title is "Finality of committee determinations; venue; jurisdiction and procedure; peremptive period; service of process."
- **Judicial review of a revocation** lies in the district court (venue per the statute — petitions are filed in the Nineteenth Judicial District Court, East Baton Rouge Parish [VERIFY — confirm venue provision]); review is **by the court without a jury and confined to the revocation record**. Build the record at the hearing — nothing new comes in on review.
- **Peremptive period:** a petition alleging denial of a revocation hearing under R.S. 15:574.9 must be filed within **90 days of the revocation**; later petitions are dismissed **with prejudice**. Calendar this the day the committee rules (feed to `dw-deadline-engine-crim`). A district-court form for these petitions appears at La. Dist. Ct. Rules Appendix 60.8 [VERIFY — confirm the appendix number].
- Grounds are narrow — procedural: denial of the revocation hearing or of Morrissey minima — so every procedural objection must be made and preserved *at* the committee hearing.
