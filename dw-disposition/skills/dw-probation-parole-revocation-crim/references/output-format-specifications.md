# Output Format Specifications

Three deliverables, produced as needed. All are **internal attorney work product** — apply the marking per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`. Any filed pleading spun out of them (motion to continue, opposition to revocation, writ application) follows `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` instead (no work-product marking on filed pleadings).

**Save path (per `dw-shared-protocols-crim/references/output-path-formula.md`):**
`{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

**Filenames:**
- `YYYY-MM-DD - Revocation Defense Memo - [Client].md`
- `YYYY-MM-DD - Revocation Hearing Prep Outline - [Client].md`
- `YYYY-MM-DD - Proposed Alternative-Sanctions Plan - [Client].md`

---

## 1. Revocation Defense Memo

```
[ATTORNEY WORK PRODUCT MARKING]

REVOCATION DEFENSE MEMO — [Client] — [Docket / DOC #]
Prepared: [date] | Track: Probation (14th JDC Div. _) / Parole (Committee on Parole)
Governing versions: Art. 900 version [___] / R.S. 15:574.9 version [___]  [flag if unconfirmed]

I.   POSTURE — supervision term & expiration; custody status; hold/detainer;
     hearing date(s); CLOCK STATUS (from dw-deadline-engine-crim, if present)
II.  ALLEGATION AUDIT TABLE (Module A)
     | # | Alleged violation | Condition (verbatim) | Proof source | Hearsay level |
     | Staleness | Deficiencies | Severity | Contest / Concede-mitigate / Silent |
III. CLASSIFICATION & EXPOSURE (Module B)
     Per-allegation technical/non-technical call; tier position; sanction cap;
     the technical-vs-full-revocation delta in numbers
IV.  CONSTITUTIONAL / PROCEDURAL ISSUES (Morrissey-Gagnon map; Bearden;
     notice; timing; term-expiration)
V.   CREDIT & TIME MATH (Module D worked computation)
     [ATTORNEY TO VERIFY against DPS&C master record]
VI.  NEW-OFFENSE COORDINATION (Module F) — sequencing recommendation,
     5th Amendment plan, global-resolution posture
VII. RECOMMENDED STRATEGY & OUTCOME MAP (Module E) — with [STRATEGIC DECISION]
     flags for attorney judgment calls
VIII. SOURCE INDEX — every document cited, per the Source Citation Mandate
```

## 2. Hearing Prep Outline

Sections per Module C-1: posture block; contest/concede map; State's witnesses with cross plans; confrontation demands (scripted objections + good-cause finding requests); defense witnesses & exhibits with subpoena status; mitigation package index; **preservation checklist** (notice objection, disclosure demand, confrontation findings, Bearden inquiry, written-findings request, notice of intent + writ return date). One page per witness maximum for cross plans; route full cross architecture to `dw-cross-exam-architect-crim`.

## 3. Proposed Alternative-Sanctions Plan

Attorney-reviewable proposal (and, on attorney approval, a hand-up version for the court/committee — hand-up version drops the work-product marking and any strategy commentary):

```
PROPOSED ALTERNATIVE-SANCTIONS PLAN — [Client]
1. THE ASK — specific disposition mapped to the Art. 900 menu / committee options
2. THE SHOWING — verification attachments (bed date, employer letter, program
   intake, payment plan) — each item sourced or marked [RECORDS NEEDED]
3. THE SAFEGUARD — review setting / status date the client consents to
4. CREDIT MATH — Module D computation attachment
5. NO-ADMISSION CLAUSE — plan is offered in mitigation; no factual admission
   regarding contested allegations [screen per Module F]
```

## Post-write reporting

After writing any deliverable, report per shared protocols: full path written, documents relied on, open `[VERIFY ...]` / `[RECORDS NEEDED]` / `[STRATEGIC DECISION]` flags, and the deadlines fed to or reconciled with `dw-deadline-engine-crim`.
