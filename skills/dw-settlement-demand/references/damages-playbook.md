# Damages Playbook

How to build each damages component — past medical specials, future medicals, lost wages, future earning capacity, general damages, judicial interest. This is the math layer of the demand.

---

## 1. Past Medical Expenses

### Source-of-truth rule
The single source of truth is the firm's Medical Expense Worksheet (or equivalent ledger). All other per-provider totals reconcile to that worksheet. If the worksheet does not exist yet, build it from the medical-chronology + per-provider billing statements.

### Per-provider table format

| S. No | Provider | Specialty | Start Date | End Date | Total Charges |
|-------|----------|-----------|------------|----------|---------------|
| 1 | Acadiana Orthopedic | Orthopedic Surgery | 03/15/2023 | 11/22/2024 | $48,512.00 |
| 2 | Vermaelen Chiropractic | Chiropractic | 03/20/2023 | 09/10/2024 | $9,560.24 |
| ... | ... | ... | ... | ... | ... |
| | | | | **Grand Total** | **$58,072.24** |

Sort by start date ascending. Show provider's specialty in a second column when there are 4+ providers — it helps the adjuster categorize.

### Adjustments
- **Write-offs / contractual adjustments.** Show the *billed* charges in the table, not the *paid* amounts. La. follows the collateral source rule in most contexts — the plaintiff is entitled to recover the reasonable value of medical services, which is typically the billed amount. Flag this for attorney decision if the defense has a specific basis to challenge billed amounts.
- **Subrogation / liens.** Do NOT subtract liens from the demand number — the gross claim is what's demanded. Liens get resolved on the back end. Reference outstanding lienholders only if it's strategically useful (rare in the demand itself; common in the cover letter).
- **Bate-stamp citations.** If the chronology Bate-stamped the records, cite the Bates range for each provider in a footnote.

---

## 2. Future Medical Expenses

Pick the approach that best fits the evidence:

### 2a. Single line item (cleanest, most credible)
When a treating physician has recommended one specific procedure with a quoted cost:

> Plaintiff's treating orthopedic surgeon, [Dr. Name], has recommended lumbar fusion surgery at L4-L5 (CPT 22633). The estimated cost of this procedure is $100,000.00 inclusive of facility, surgeon, anesthesia, hardware, and post-operative care. (See [Surgeon] Operative Recommendation, [Date].)

### 2b. Lump-sum estimate (when supported by a life-care planner or treating physician opinion)
When a global future-care opinion exists:

> [Dr. Name] has opined that [Client] will require ongoing pain management, physical therapy, and likely revision surgery over the remainder of [Client]'s life. Based on the future-care plan and projected utilization, [Client]'s future medical expenses are estimated at $250,000.00. (See Life-Care Plan, [Date].)

### 2c. Polk-style projection table (most persuasive when supported)
When there are recurring procedures with documented per-procedure costs and a life-expectancy figure:

| Procedure | Frequency | Cost / Procedure | Cost / Year | Lifetime Cost (× [Life Exp.] years) |
|-----------|-----------|------------------|-------------|-------------------------------------|
| Cervical facet injections | 4×/year | $2,800 | $11,200 | $629,440 |
| Lumbar epidural steroid injections | 3×/year | $3,500 | $10,500 | $590,100 |
| Physical therapy | 24 visits/year | $185 | $4,440 | $249,576 |
| ... | ... | ... | ... | ... |
| **Total Projected Future Medical** | | | | **$1,469,116** |

Anchor the life-expectancy figure on SSA tables or a treating physician's opinion. Cite the source in a footnote under the table.

### 2d. No supportable future medical
Write `Not factored in` or `TBD pending vocational / life-care planner opinion.` Never invent a number.

---

## 3. Past Lost Wages

### Source-of-truth rule
A signed employer-verification letter with hours/days missed + hourly or salaried rate is the strongest source. Pay stubs (covering pre- and post-injury periods) are second-best. W-2s show annual totals but not granular lost time.

### Calculation methods

**Method A — Lump-sum from employer letter:**
> [Client] was unable to work from [Date] to [Date] as a direct result of the injuries sustained in the subject crash. Per the attached employer-verification letter from [Employer], [Client] lost [Hours] of work. At [Client]'s hourly rate of $[Rate]/hour, this represents a past lost wages of $[Amount]. (See Exhibit __ — Employer Verification Letter dated [Date].)

**Method B — Daily build:**
> [Client] missed work on the following dates as documented by treating-physician work-restrictions notes:
> | Date(s) | Hours Lost | Provider Note (Bates) |
> |---------|-----------|-----------------------|
> | 3/15/23 – 3/22/23 | 40 hr | (Smith Ortho, 3/15/23, Bates ###) |
> | ... | ... | ... |
> | **Total** | **___ hr** | |
> 
> At [Client]'s rate of $[X]/hour, past lost wages total $[Amount].

**Method C — Salaried / per-day:**
> [Client], a salaried [job title] earning $[Annual]/year ($[Daily-rate]/day), missed [N] days of work due to the subject crash. Past lost wages: $[Amount].

---

## 4. Future Lost Earning Capacity

### Method A — Vocational opinion (cleanest)
> [Vocational Expert Name] has opined that [Client]'s injuries have resulted in a permanent loss of earning capacity of $[Amount]/year. Over [Client]'s remaining worklife of [N] years (per [source]), future lost earning capacity totals $[Total]. (See [Vocational Expert] Report dated [Date].)

### Method B — W-2 history + worklife multiplier (the firm's Antoine 2017 method)
1. Pull the last 6 years of W-2 income.
2. Compute the mean.
3. Multiply by remaining worklife years.

| Year | W-2 Income |
|------|-----------|
| 2018 | $58,420 |
| 2019 | $61,300 |
| 2020 | $59,150 |
| 2021 | $63,800 |
| 2022 | $67,200 |
| 2023 | $69,500 |
| **6-year average** | **$63,228** |

> Per BLS worklife tables, a [Age]-year-old [male/female] of [Client]'s educational level has an expected worklife of [N] years. [Client]'s post-injury work restrictions (per [Source]) reduce earning capacity by approximately [%]. Future lost earning capacity:
>
> $63,228 (avg annual) × [N] years × [%] reduction = **$[Total]**

### Method C — No supportable claim
If the plaintiff has returned to full-duty work without lost earning capacity, write: "Not factored in — [Client] returned to full-duty work on [Date]." This actually helps the demand: it shows the firm is disciplined about what to claim.

### Discount to present value
For large future-loss numbers, the defense will argue the projection must be discounted to present value. The firm's typical posture is to present the gross number and address discount-to-present-value only if the defense raises it. For mediation papers, the attorney can optionally present both gross and discounted figures.

---

## 5. General Damages — Body-Region Bucketing

See `louisiana-quantum-cases.md` for the quantum-case library organized by body region.

### Determining bucket count
| Case profile | Suggested buckets |
|--------------|-------------------|
| Pure soft-tissue, single body region | 1 bucket (SOFT TISSUE) |
| Soft-tissue + minor contusion / scarring | 1–2 buckets |
| Multi-region cervical + lumbar without surgery | 2 buckets (or 1 combined CERVICAL AND LUMBAR) |
| Surgical case (one surgery) | 2 buckets (the surgical region + any non-surgical region) |
| Multi-surgery / multi-region | 3+ buckets, one per significant region |
| TBI + orthopedic | At least 2: TBI + the orthopedic region |
| Catastrophic / multiple body systems | 4–6 buckets — be specific (e.g., SOFT TISSUE / CERVICAL FUSION / LUMBAR SURGERY / KNEE / SHOULDER / TBI) |

### Per-bucket math
For each bucket:
1. Pull 4–8 quantum cases from `louisiana-quantum-cases.md` with similar injuries and treatment.
2. Note the awards.
3. Pick a recommendation amount that's in the upper-middle of the comp-case range — not the highest, not the lowest. This is defensible.
4. Write the recommendation as: *"Considering the foregoing cases... a compromise of $[X] would adequately compensate [Client] for [body region] injuries (past and future)."*

### Anchoring techniques
- **Anchor by repetition** — every case parenthetical ends with the $ award. Reader sees the number 5 times in a single section.
- **Anchor with the high cases first** — leads with the most-on-point high-award case so the reader's first numeric impression is the largest.
- **Closing-paragraph anchor** — the recommendation sentence is the last $ figure the reader sees before moving on.

### De-duplication
Never cite the same case twice across buckets — defense will note it and treat it as sloppiness. If a single case covers two body regions, pick the bucket where it lands cleanly.

---

## 6. Pain & Suffering Calculation (Optional / Fallback Only)

**The firm's primary general-damages method is quantum-case anchoring by body-region bucket (Section 5 above).** Multiplier and per-diem methods are documented here for completeness but they do NOT appear in the firm's corpus and should be treated as fallback frameworks for unusual cases (e.g., no on-point quantum case exists for the injury profile, or the attorney wants a secondary check on the bucket recommendation amounts). Default to quantum-case anchoring; use these only when asked.

### Multiplier method
General damages = Special damages × multiplier
- 1.5× — minor injuries, full recovery, no surgery
- 2.0–2.5× — soft-tissue with extended treatment, no surgery
- 3.0–4.0× — significant injuries, one surgery, lingering symptoms
- 4.0–5.0× — major injuries, multiple surgeries, permanency
- 5.0× and above — catastrophic, permanent disability, TBI, paralysis

> Applying a [N]× multiplier to [Client]'s past medical specials of $[X] yields a general-damages estimate of $[X × N].

### Per-diem method
General damages = Daily rate × days of impact

| Phase | Daily Rate Basis | Days | Subtotal |
|-------|------------------|------|----------|
| Acute pain (immediate post-crash through surgery) | $500/day (severe pain, hospital and surgical recovery) | 90 days | $45,000 |
| Chronic pain (post-surgical recovery, PT) | $250/day | 365 days | $91,250 |
| Long-term residual pain | $100/day | 5 years × 365 days = 1,825 days | $182,500 |
| **Total per-diem general damages** | | | **$318,750** |

Use the multiplier method when the case is squarely in a typical injury band. Use per-diem when the recovery timeline is well-documented and finite, or for cases with documented disability days.

For permanent / lifelong-impact cases, per-diem requires care: use a conservative daily rate ($50–$150) over the plaintiff's remaining life expectancy.

---

## 7. Loss of Consortium (spouse joining)

If the plaintiff's spouse has joined the suit:

> [Spouse Name] is the spouse of [Plaintiff Name]. The injuries to [Plaintiff] have deprived [Spouse] of [Plaintiff]'s society, services, sexual relations, and companionship. Louisiana courts have recognized loss-of-consortium damages in similar cases as follows:
> - [Case, cite] — awarded $[X] for loss of consortium following [injury]
> - ...
>
> A compromise of $[X] would adequately compensate [Spouse] for [his/her] loss of consortium.

---

## 8. Loss of Household Services

> Per the Bureau of Labor Statistics, the replacement cost of household services (cleaning, cooking, laundry, child care, lawn care, etc.) for a household of [size] is approximately $[X]/week or $[Y]/year. [Plaintiff] has been unable to perform these services for [N] weeks/months/years. Loss of household services to date: $[Z]. Future loss (if permanent): $[W] over [N] years.

Use only when there's specific documentation that the plaintiff was the primary household-services provider and has been unable to perform those tasks.

---

## 9. Property Damage

Usually settled separately, but include in the demand if it remains open:
- Vehicle repair cost (if repairable)
- ACV / total-loss valuation (if total)
- Diminished value (if claimed)
- Personal-property loss (items in the vehicle damaged in the crash)
- Rental car / loss-of-use

---

## 10. Out-of-Pocket Expenses

Often missed in demands. Include when documented:
- Co-pays and deductibles paid
- Prescription out-of-pocket
- Mileage to medical appointments (current IRS rate × miles)
- Medical equipment, braces, slings, etc.
- Modifications to home/vehicle for accessibility
- Childcare during medical appointments

---

## 11. Judicial Interest

See `louisiana-judicial-interest.md` for the annual rate table and worked calculation. Always compute fully for mediation papers; one-line acknowledgment is acceptable for pre-suit demands.

---

## 11.5. RECAP Table Row Discipline

The RECAP table at the end of the demand should include ONLY the line items being claimed. Do not show "$0.00" lines for categories where no claim exists — that signals to the defense that the firm considered the category and chose not to claim, which can undercut later amendment.

Drop the row entirely when no claim is being made. Verified in Monroe 2023 (which omits the PAST LOST WAGES line because Mr. Monroe had no past wage loss to claim).

Always-required rows: PAST MEDICAL EXPENSES, GENERAL DAMAGES, TOTAL.
Conditional rows: FUTURE MEDICAL EXPENSES, PAST LOST WAGES, FUTURE LOST WAGES, JUDICIAL INTEREST.

If a row IS included, never write "$0.00" — write the actual amount OR a label like "TBD at trial" or "Not factored in" if the amount is non-zero but unliquidated. If the amount is genuinely zero and there is no future claim, omit the row.

**On JI on future damages:** Louisiana law on whether judicial interest runs on future damages from the date of judicial demand is contested. The conservative practice — and the firm's practice in Brooks 2020 and Hopes 2020 — is to compute JI ONLY on past medicals + past lost wages + general damages, and to exclude future medicals and future lost wages from the JI principal. State this methodology in a one-line footnote under the JI table to foreclose the defense's argument before it starts.

---

## 12. Final Math Reconciliation (mandatory before output)

Before generating the .docx, verify:
- [ ] Per-provider table totals equal the Past Medical Expenses line on RECAP
- [ ] Future Medical Expenses line on RECAP equals the future-meds calculation total
- [ ] Past Lost Wages on RECAP equals the wages calculation total
- [ ] Future Lost Wages on RECAP equals the future-earnings calculation total
- [ ] General Damages on RECAP equals the SUM of body-region bucket recommendations
- [ ] Judicial Interest on RECAP equals the JI calculation total
- [ ] RECAP total equals (and the demand sentence cites) the same demand number
- [ ] For mediation papers: trial-anchor in the two-step demand equals the RECAP total; today-number is the discounted resolution figure

If anything fails, fix and re-verify. Math is the easiest credibility-kill in a demand.
