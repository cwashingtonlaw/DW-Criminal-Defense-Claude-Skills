# Discovery Production Tracker and Prioritized Missing Items Report

**Living ledger of all discovery demanded, produced, outstanding, late, or never produced.**

This tracker is the operational heart of the compliance monitor. It converts abstract discovery obligations into concrete, trackable items.

---

## DISCOVERY PRODUCTION TRACKER — [Case Name] / [Case No.]

| Item # | Category | Description | Demanded (Date) | Produced (Date) | Status | Days Outstanding | Notes |
|--------|----------|-------------|-----------------|-----------------|--------|-------------------|-------|
| 1 | Statements (Art. 716) | Defendant's written statements to NOPD | 3/1/2024 | 3/8/2024 | RECEIVED | 0 | 2-page statement; appears complete |
| 2 | Statements (Art. 716) | Defendant's interrogation audio/video | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Critical — likely exists; withheld? |
| 3 | Police Reports (Art. 718) | Initial arrest report | 3/1/2024 | 3/8/2024 | RECEIVED | 0 | Complete report; 8 pages |
| 4 | Police Reports (Art. 718) | Supplemental detective reports | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Multiple reports expected; none produced |
| 5 | Photographs (Art. 718) | Crime scene photographs | 3/1/2024 | 3/15/2024 | LATE | 0 | Produced 14 days late; 47 photos |
| 6 | Photographs (Art. 718) | Photographs of defendant at time of arrest | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Should exist per arrest report |
| 7 | 911 Calls (Art. 718) | 911 call audio and transcript | 3/1/2024 | 3/8/2024 | RECEIVED | 0 | 2 calls; audio clear |
| 8 | Dispatch Records (Art. 718) | Dispatch radio recordings | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Essential; likely retained |
| 9 | Scientific Tests (Art. 719) | Drug analysis report | 3/1/2024 | 3/22/2024 | LATE | 0 | Produced 21 days late |
| 10 | Scientific Tests (Art. 719) | Lab bench notes for drug testing | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Underlying data; critical |
| 11 | Scientific Tests (Art. 719) | DNA report | 3/1/2024 | PENDING | OUTSTANDING | 35+ | No DNA alleged; confirm not performed |
| 12 | Witness Statements (Art. 720) | Written statement from Officer Martinez | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Will be needed before trial |
| 13 | Witness Statements (Art. 720) | Interview notes from alleged victim | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Prior inconsistent statement possible |
| 14 | Officer Records | Prior complaints against Sgt. Brown | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Potentially Brady material |
| 15 | Brady/Giglio | All exculpatory evidence | 3/1/2024 | NONE | DISPUTED | 35+ | DA claims none exists; assert Brady order |

---

## STATUS LEGEND

| Status | Definition |
|--------|-----------|
| **RECEIVED** | Item produced in full, complete, and timely |
| **OUTSTANDING** | Item demanded; no production to date |
| **PARTIALLY PRODUCED** | Item produced but appears incomplete or edited |
| **LATE** | Item produced but after 10-day deadline |
| **NEVER PRODUCED** | Item demanded; deadline passed; no indication of production |
| **DISPUTED** | State claims item doesn't exist or is privileged; dispute pending |
| **UNDER REVIEW** | State claims item under review/redaction; timeline unclear |

---

## AUTOMATED FLAGS

The tracker should automatically flag items that are:

- **Outstanding 30+ days** — Use reminder language: "Item outstanding beyond 10-day statutory deadline"
- **Outstanding 60+ days** — Escalate: "Potential motion to compel or sanctions warranted"
- **Outstanding 90+ days** — Critical: "Presumptively withheld; consider Brady violation"
- **Partially produced** — Query: "Is production complete? Request clarification"
- **Produced late** — Calculate: "Item late by [X] days. Assess prejudice and need for continuance"

---

## COMPLIANCE METRICS

Calculate automatically:

- **Total items demanded:** [Count]
- **Items received:** [Count] ([%])
- **Items outstanding:** [Count] ([%])
- **Items late:** [Count] with average delay of [X] days
- **Estimated compliance:** [%] of demand satisfied

**Interpretation:**
- 95%+ compliance: Adequate (monitor for pattern)
- 75-94% compliance: Deficient (consider motion to compel)
- 50-74% compliance: Significantly deficient (motion to compel + sanctions recommended)
- <50% compliance: Presumptive Brady violation; consider writ application

---

## PRIORITIZED MISSING ITEMS REPORT

After updating the discovery ledger, generate a Prioritized Missing Items Report that synthesizes all outstanding discovery items into a defense-focused deliverable. This transforms raw ledger data into an actionable list ranked by defense impact.

For each missing item (e.g., body-cam footage, dispatch logs, lab notes, personnel files, 911 audio):

- **Item Description:** What is missing and why it should exist (cite the source document that references or implies its existence)
- **Priority Ranking:**
  - **CRITICAL** — Constitutional materiality (Brady/Giglio material, exculpatory evidence)
  - **HIGH** — Direct impact on defense theory at trial
  - **MEDIUM** — Corroborative value or impeachment potential
  - **LOW** — Administrative completeness
- **Source Citation:** The specific demand, report, or document that references or implies the item should have been produced — e.g., `(Arrest Report, p. 3, para. 2 — references "dash cam recording" but no video produced)` or `(Defense Discovery Demand, 03/01/2026, Item #14)`
- **Deadline Urgency:** Days until next court date or discovery deadline

This report feeds directly into the **dw-criminal-defense** Phase 2 Report 7 (Table of Missing Discovery) and triggers the Auto-Action Missing Discovery Demand Letter. Route CRITICAL items immediately to **dw-brady-giglio-auditor**.
