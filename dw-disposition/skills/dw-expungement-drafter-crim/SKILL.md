---
name: dw-expungement-drafter-crim
category: disposition
description: >
  Louisiana expungement eligibility deep screen AND motion-packet drafting under
  La. C.Cr.P. Title XXXIV (arts. 971-995). Runs the full art. 976/977/978 eligibility
  analysis (no-conviction, misdemeanor, and felony pathways, cleansing periods,
  exclusions and their exceptions, interim expungement, Art. 893/894 set-asides),
  maps costs, fee exemptions, service, and the objection window, drafts the
  uniform-form motion packet ready for attorney edit, and produces effects
  counseling plus a client letter. ALWAYS invoke for "expunge," "expungement,"
  "clear my record," "seal the record," "interim expungement," "record cleanup."
  Do NOT use for the brief closing-stage eligibility screen (dw-case-disposition-crim
  Step 5 produces that; this skill consumes it), pardons or post-conviction relief
  (use dw-post-conviction-relief-crim), or immigration effects of a record
  (use dw-padilla-advisement-crim).
---

# D&W Expungement Drafter

**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

**Version:** 1.0
**Skill Type:** Eligibility Analysis + Motion Drafting
**Jurisdictional focus:** La. C.Cr.P. Title XXXIV (arts. 971–995); 14th JDC / Calcasieu Parish local practice

## Overview

This skill takes a client's Louisiana arrest and conviction history and produces (1) a deep eligibility screen under Articles 976–978 and 985.1, (2) a cost and process map, (3) a ready-to-edit uniform-form motion packet, and (4) effects counseling with a client letter. It goes far deeper than the brief expungement-eligibility assessment **dw-case-disposition-crim** produces at case closing (its Step 5 / Module 5 Expungement Eligibility Memo). **When that memo exists, load it first and treat it as the starting inventory of charges and dispositions — then re-verify every article and date here before drafting.** The closing-stage memo is a screen; this skill is the authority for eligibility conclusions and drafting.

**DO NOT USE FOR:**
- Case-closing workflow (use **dw-case-disposition-crim** — it will route here when a client is expungement-eligible)
- Pardons, PCR, habeas, or sentence modification (use **dw-post-conviction-relief-crim**)
- Immigration consequences counseling (use **dw-padilla-advisement-crim**)

## STEP 0 — FILE INTAKE HARD STOP (Always First)

If the attorney indicates files are being uploaded (rap sheet, background check, minutes, bill of information, prior expungement orders) or an upload appears in progress, **STOP. Do not begin analysis.** Ask: *"Are all records uploaded — LSP background check, bill(s) of information, disposition minutes, and any closing-stage expungement memo? Reply 'all files in' to proceed."* Only proceed once the attorney confirms. Partial-record eligibility analysis produces wrong eligibility dates and wrong filing decisions; an erroneously filed motion wastes non-refundable statutory fees.

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — internal deliverables (deep-screen memo, process map) carry work-product marking
2. `dw-shared-protocols-crim/references/output-path-formula.md` — all output paths anchor on `{{CASE_ROOT}}`
3. `dw-shared-protocols-crim/references/letterhead.md` — the client letter (Module D) is outward-facing: firm letterhead, attorney-client privilege line, **no work-product marking** (same split dw-case-disposition-crim uses for its client letters)
4. `dw-shared-protocols-crim/references/caption-criminal-14thJDC.md` — caption for the motion packet (or the matching caption file for the parish of arrest)
5. `dw-shared-protocols-crim/references/filing-conventions-14thJDC.md` — formatting and filing mechanics
6. `dw-shared-protocols-crim/references/certificate-of-service.md` and `proposed-order.md` — service and order components

Do not proceed to Step 1 until these are loaded.

### Source Citation Mandate

Every factual assertion in the deliverables — each arrest, charge, disposition, sentence-completion date, intervening conviction, pending charge, and fee-exemption fact — must trace to a specific source document. Wrong eligibility conclusions cost the client filing fees and can misstate what an employer background check will show.

**Citation format examples:**
- `(LSP Background Check dated 08/12/2026, entry 3)`
- `(Bill of Information, Docket #12345-24, Count 1)`
- `(Minute Entry — Disposition, 14th JDC Docket #12345-24, dated 03/15/2026)`
- `(Case Disposition Expungement Eligibility Memo, p. 2)`
- `(Probation Completion Letter, LDPSC, dated 06/01/2021)`

**Unsourced assertions:** mark `[UNSOURCED — VERIFY]`. **Unverified statutes/cases:** mark `[VERIFY CITATION]`. Eligibility dates must show their arithmetic (completion date + cleansing period = eligibility date) with the source of the completion date cited.

## STEP 1 — INFORMATION GATHERING PROTOCOL

**Essential (cannot analyze without):**
- Complete arrest/charge/disposition inventory — LSP background check (dated within 60 days if filing is imminent), rap sheet, or the dw-case-disposition-crim Expungement Eligibility Memo
- For each arrest: parish of arrest, arresting agency, docket number, charges as billed vs. as convicted, disposition type and date
- For convictions: sentence terms and **date of completion** of sentence/probation/parole/deferred adjudication
- Intervening criminal history and pending charges (statewide, all parishes)
- Current custody status (incarcerated clients face filing restrictions — see Module A)

**Strategic:**
- Whether disposition used Art. 893 (felony) or Art. 894 (misdemeanor) deferral, and whether set-aside/dismissal has already been obtained
- Prior expungements obtained (what, when, which parish)
- Fee-exemption facts: acquittal after trial, DA refusal/dismissal, time-barred prosecution, indigency (in forma pauperis), pardon, factual innocence
- Client's purpose (employment, licensing, housing, firearms) — drives Module D counseling

**Contextual:**
- Out-of-parish arrests requiring separate filings; federal or out-of-state records (not reachable by Louisiana expungement — note for client letter)
- DWI records (OMV proof requirement and extra fee — Module B)

## STEP 2 — MODULE A: ELIGIBILITY DEEP SCREEN

For **each arrest incident separately**, classify the outcome and run the pathway analysis: Art. 976 (no conviction: acquittal, dismissal/quashed, nolle/DA declined including diversion completion, time-barred), Art. 977 (misdemeanor conviction: Art. 894(B) set-aside route or 5-year cleansing period; exclusions), Art. 978 (felony conviction: Art. 893(E) set-aside route, 10-year cleansing period, or first-offender pardon; crime-of-violence and sex-offense exclusions and the Art. 978 exception list), and Art. 985.1 interim expungement (felony arrest that produced only a misdemeanor conviction). Compute the eligibility date for every charge, showing arithmetic. Note the repealed frequency caps (Acts 2020, No. 78) — older guides still cite them.

**Read `references/module-a-eligibility-deep-screen.md` now** for the full article-by-article framework, exclusion/exception tables, the per-charge worksheet, and the cross-check against the closing-stage memo.

## STEP 3 — MODULE B: COST & PROCESS MAP

Map the money and the mechanics before drafting: Art. 983 fee structure ($550 statutory cap; reduced marijuana schedule), fee exemptions (acquittal, DA-refusal/dismissal, time-barred, pardon, factual innocence, trafficking victim), in forma pauperis route, DWI OMV add-on, service by the clerk on the DA / LSP Bureau of Criminal Identification and Information / arresting agency (Art. 979), the 60-day objection window and contradictory hearing (Art. 980), and realistic processing timelines.

**Read `references/module-b-cost-and-process-map.md` now** for amounts, exemption certifications, the service/objection sequence, and timeline expectations.

## STEP 4 — MODULE C: MOTION PACKET DRAFTING

Assemble the uniform-form packet (the statutory forms are mandatory — do not freestyle a motion) plus the supporting documents as ready-to-edit Word-document content: Motion for Expungement with charge tables, supplemental sheet if needed, proposed Order(s), any Motion to Set Aside under Art. 893/894 that must precede the expungement, interim-expungement forms where applicable, certificate of service, and the attachments checklist (background check, bill of information, disposition minutes, DA certification, fee-exemption proof, OMV proof for DWI). Caption per the parish of arrest.

**Read `references/module-c-motion-packet-drafting.md` now** for the packet inventory, drafting templates, and the attachments checklist.

## STEP 5 — MODULE D: EFFECTS COUNSELING + CLIENT LETTER

Draft the counseling section and the outward-facing client letter: what Louisiana expungement does (record confidential, removed from public view) and does not do (records **not destroyed**; law-enforcement/criminal-justice/prosecutor/court access continues; enumerated licensing boards retain access; **firearms rights are NOT restored by expungement alone**; federal and private databases unaffected). For collateral-consequences counseling beyond record relief — especially immigration — route to **dw-padilla-advisement-crim**.

**Read `references/module-d-effects-counseling.md` now** for the Art. 973 effects framework, the carve-out list, the firearms analysis, and the client-letter template.

## STEP 6 — OUTPUT FORMAT

All internal deliverables save under the standard formula and carry work-product marking:

1. **Expungement Deep-Screen Memo** — `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Expungement Deep Screen - [ClientLastName] - [YYYY-MM-DD].docx` (Modules A+B: per-charge eligibility table, eligibility-date arithmetic, cost map, recommended sequence)
2. **Motion packet drafts** — `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/[YYYY-MM-DD] - Motion for Expungement - [Descriptor].docx` (+ ` - Proposed Order`, ` - Certificate of Service` companions). Filed-pleading drafts carry **no** work-product marking.
3. **Client letter** — drafted inside `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Expungement Client Letter - [ClientLastName] - [YYYY-MM-DD].docx`; the letter body carries firm letterhead and privilege line, no work-product marking (mirror of the dw-case-disposition-crim letter split).

**Downstream:** record eligibility dates and filing status in **dw-case-brain-crim**; set Google Calendar reminders for future eligibility dates and the 60-day objection-window expiration; if the case is still in closing workflow, hand results back to **dw-case-disposition-crim** Step 5.

## GUARDRAILS

1. **Never state an eligibility conclusion without the underlying disposition document.** A rap-sheet line is a lead, not a disposition — pull the minutes.
2. **Every statute or amount you have not verified gets `[VERIFY CITATION]`.** Expungement fees and article numbers have been amended repeatedly (2014 overhaul, 2020 frequency-cap repeal, 2021–2023 marijuana and automation acts).
3. **Per-arrest, per-parish discipline.** One motion per arrest incident, filed in the district court of the parish of arrest. Never merge arrests into one motion.
4. **Do not promise record destruction, firearms restoration, or invisibility to licensing boards.** Module D language is mandatory in the client letter.
5. **Sequence set-asides first.** If Art. 893/894 relief is available but not yet granted, the set-aside motion precedes (or accompanies) the expungement.
6. **Fees are non-refundable — screen before filing.** If eligibility is uncertain, resolve it or advise waiting; do not file on hope.
7. **Attorney reviews, signs, and files everything.** All outputs are drafts; the attorney verifies the background check, the eligibility math, and local clerk requirements before filing.
8. **Local practice varies by clerk.** Consult `references/calcasieu-14thjdc-local-notes.md` (attorney-populated) before finalizing a 14th JDC packet.

## QUICK REFERENCES

- **module-a-eligibility-deep-screen.md** — Arts. 976/977/978/985.1 pathway analysis, 893/894 set-aside interaction, exclusions and exceptions, repealed frequency caps, automated (Clean Slate) expungement, per-charge worksheet
- **module-b-cost-and-process-map.md** — Art. 983 fees and exemptions, in forma pauperis, Art. 979 service, Art. 980 objection window and hearing, uniform forms inventory, timeline
- **module-c-motion-packet-drafting.md** — packet assembly order, motion/order/set-aside templates, attachments checklist
- **module-d-effects-counseling.md** — Art. 973 effects and carve-outs, firearms analysis, client-letter template (letterhead, outward-facing)
- **calcasieu-14thjdc-local-notes.md** — 14th JDC / Calcasieu local filing quirks (ATTORNEY-POPULATED — placeholders until filled in)

---

**Skill Version:** 1.0
**Status:** Draft — pending attorney verification of flagged citations
