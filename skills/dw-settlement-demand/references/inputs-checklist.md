# Inputs Checklist

Every input the skill needs to draft a complete demand or mediation paper, ranked.

Mark each item as **PROVIDED** (attorney supplied directly), **AVAILABLE-IN-FILES** (extractable from uploaded documents), or **MISSING**. Do not proceed to drafting any body section until every Essential item is at least AVAILABLE-IN-FILES.

---

## Essential — drafting cannot begin without these

### Routing
- [ ] **Mode**: `demand` | `mediation_paper` | `hybrid`
- [ ] **Document-type banner** (matches mode): SETTLEMENT DEMAND LETTER / SETTLEMENT OFFER / MEDIATION POSITION PAPER
- [ ] **Confidentiality marking** (mediation papers only): yes/no on "PERSONAL AND CONFIDENTIAL"
- [ ] **Response deadline** (demand only): 15 days / 30 days / none

### Caption
- [ ] **Plaintiff name(s)** (and preferred reference style — Mr./Mrs./Ms. Lastname; Title Case throughout vs. ALL CAPS in facts section)
- [ ] **Defendant name(s)** and role (driver, employer, premises owner, etc.)
- [ ] **Case number / docket number** (if suit filed)
- [ ] **Division letter**
- [ ] **Court** (e.g., "14th JDC, Calcasieu Parish" or "USDC, WDLA, Lake Charles Division")
- [ ] **Mediation firm matter no.** (PDDS / MAPS / etc.) — for mediation routing
- [ ] **Firm file no.**
- [ ] **Mediation date / time / location** — for mediation papers

### Addressee blocks
- [ ] **Defense counsel** — name, firm, street address, city/state/zip, phone, fax, email
- [ ] **Mediator** (for `mediation_paper`/`hybrid` or when `demand` is being mediated) — name, organization, address, phone, fax, email
- [ ] **Claims adjuster / carrier** (alt to defense counsel for pre-suit demands) — name, carrier, claim number, address, phone, fax, email

### Firm info (one-time per firm — cache after first session)
- [ ] Firm name
- [ ] Firm address (street, city, state, zip)
- [ ] Signing attorney name + direct phone
- [ ] Other firm attorney(s) listed on letterhead + direct phones
- [ ] Firm fax
- [ ] Firm general email
- [ ] Signing attorney bar number (optional — only included if firm convention is to include it)

### Crash / incident facts
- [ ] **Date of crash**
- [ ] **Time of crash**
- [ ] **Location** (street, intersection, mile marker, parish, state)
- [ ] **Mechanism** (rear-end / failure-to-yield / left-turn / pull-out / head-on / sideswipe / curve-overshoot / pedestrian / workplace / premises liability / dog bite / etc.)
- [ ] **Plaintiff's lawful action at moment of impact** (e.g., stopped at red light, traveling in their lane within the speed limit)
- [ ] **Defendant's wrongful action** (e.g., following too closely, ran stop sign, distracted by phone)
- [ ] **Officer / agency** that investigated, report number
- [ ] **Citations issued** (statute, to whom, paid or contested)
- [ ] **Vehicle damage** — repair estimate or total-loss valuation
- [ ] **Posted speed limit / weather / roadway condition** (from crash report)

### Liability statutes (for `mediation_paper` / `hybrid` LAW subsection)
- [ ] Applicable Louisiana traffic statute(s) — see `louisiana-statutes.md` for the menu

### Injuries
- [ ] **List of diagnoses** with ICD-10 codes (skill builds the table)
- [ ] **Body regions implicated** — drives the GD bucket split (cervical / lumbar / thoracic / shoulder / knee / hip / wrist / hand / TBI / pelvis / chest / soft tissue / scarring / etc.)
- [ ] **Surgeries/procedures performed** (with CPT codes if available, dates, surgeons)
- [ ] **Future surgeries/procedures recommended** (with cost estimate and life-expectancy basis if doing the projection table)
- [ ] **Permanency rating** (if assigned by a treating physician — percentage impairment to the whole person or to a specific body region)
- [ ] **Pre-existing conditions** affecting any injured body region

### Treatment
- [ ] **Per-provider table** — provider name / dates of treatment / number of visits / total charges (skill builds it; sources from the medical-expense worksheet and the per-provider records)
- [ ] **Medical Chronology .docx** (strongly preferred — if not available, raw medical records + chronology will be built inline; if neither is available, flag and request)

### Special damages — past
- [ ] **Past medical expenses total**
- [ ] **Past lost wages total** (or "not factored in")

### General damages — supporting facts
- [ ] **ADL impact list** — at minimum 3 domains affected; ideally the 8-domain Brooks-style breakdown
- [ ] **Pain-and-suffering daily-life specifics** (sleep, mood, intimacy, hobbies, parenting, etc.)

### Demand number
- [ ] **Total demand** (today number)
- [ ] **Trial anchor number** (for `mediation_paper` and `hybrid` only) — typically 1.2× to 2× the today number

---

## Strongly Recommended

### Liability strengthening
- [ ] **Police/crash report PDF** — for officer's narrative quote and citation detail
- [ ] **Witness statements** — for corroboration list
- [ ] **Defendant deposition transcript** — for admissions block-quote
- [ ] **Scene photos** — described with Exhibit numbers
- [ ] **Vehicle damage photos** — described with Exhibit numbers
- [ ] **Crash diagram** — described or attached
- [ ] **Defendant's employer info** (for course-and-scope cases) — employer name, defendant's job title, defendant's licensure status, employer's knowledge of any disqualifying factor

### Medical strengthening
- [ ] **Specific MRI / CT / X-ray findings** — verbatim quotes
- [ ] **Surgical operative reports** — verbatim quotes of relevant findings
- [ ] **Treating physician's permanency opinion** — verbatim quote with the date and source
- [ ] **Treating physician's causation opinion** — verbatim quote
- [ ] **Specialist consult reports** — for ortho, neuro, pain management, neuropsych, etc.

### Future damages
- [ ] **Life-care plan** (if available) — line items, totals, life expectancy basis
- [ ] **Vocational opinion** — for future earning-capacity claims
- [ ] **SSA worklife / life-expectancy tables** (referenced by life-care planner or to be applied by the skill)
- [ ] **6-year W-2 history** — for future-lost-wages projection using the firm's Antoine 2017 method

### Plaintiff humanization
- [ ] **Client block-quote** — a strong deposition passage in the plaintiff's own voice (for mediation papers)
- [ ] **Before/After narrative** — 2–3 sentences on who the plaintiff was before vs. after the crash
- [ ] **Family/dependent info** — for sole-provider / single-parent framing
- [ ] **Photos of plaintiff pre- and post-injury** — described as Exhibits

### Posture
- [ ] **Known policy limits** — capture each policy as `{carrier, type (primary / UM / UIM / umbrella / employer), limit}`; real cases often have multiple layers
- [ ] **Any prior policy-limits demand** that was rejected — date, amount, defense response (for the "ignored the policy limits" framing)
- [ ] **Suit-filing date** (for judicial-interest computation)
- [ ] **Comparative-fault exposure** — defense's anticipated apportionment argument
- [ ] **Co-plaintiffs** (if multi-plaintiff case) — name each co-plaintiff (spouse, child, passenger) and whether they have separate injury claims, loss-of-consortium claims, or both; the skill drafts the primary plaintiff's portion and flags co-plaintiff portions as separate sections to be addressed

---

## Optional / Strategic

- [ ] **Insurance policy declarations** (Decs page) — for clear policy-limits citation
- [ ] **Prior settlement correspondence** — for "they ignored our prior demand" framing
- [ ] **Prior offer history** — defense's prior offer numbers, dates
- [ ] **Defense expert reports** (with weaknesses to neutralize)
- [ ] **Plaintiff's prior accident history** (to address eggshell-plaintiff defense)
- [ ] **Loss of consortium claim** (spouse joining)
- [ ] **Loss of household services** — Bureau of Labor Statistics rate × hours lost
- [ ] **Property damage** — vehicle repair, total loss valuation, diminished value, personal property damaged
- [ ] **Out-of-pocket expenses** — co-pays, deductibles, mileage to medical appointments, prescriptions
- [ ] **Health insurance / Medicaid / Medicare liens** (for transparency on the net-to-client analysis)

---

## Source-of-truth ranking (if two sources disagree)

When two case-file sources give different values for the same item, defer in this order:

1. **Treating physician's operative or imaging report** (for medical findings)
2. **Provider's billing statement** (for charges)
3. **Medical Expense Worksheet** (consolidated)
4. **Medical Chronology .docx** (consolidated)
5. **Attorney's input during this session** (correcting an error in the file)
6. **Defense-prepared documents** (treat as suspect — they may be manipulated)

If any conflict is material, stop and ask the attorney to resolve before drafting.

---

## Cache file (one-time per case)

The skill should write a `case-context.json` to the case folder after the first run so subsequent runs (revisions, mode-switches, follow-up demands) can pre-fill the routing and caption block:

```json
{
  "firm": { "...firm-info..." },
  "client": { "...names, age, occupation, pronouns..." },
  "case_caption": { "...parties, docket, division, court..." },
  "crash": { "...date, time, location, mechanism..." },
  "body_regions": ["cervical", "lumbar", "TBI"],
  "providers": [ {"name": "", "dates": "", "charges": 0}, ... ],
  "past_meds_total": 0,
  "future_meds_total": 0,
  "lost_wages_past": 0,
  "lost_wages_future": 0,
  "general_damages": { "soft_tissue": 0, "cervical_lumbar": 0, "TBI": 0 },
  "judicial_interest": 0,
  "policy_limits": [ {"carrier": "", "type": "primary", "limit": 0}, {"carrier": "", "type": "UM", "limit": 0} ],
  "prior_offers": [],
  "today_number": 0,
  "trial_anchor": 0
}
```
