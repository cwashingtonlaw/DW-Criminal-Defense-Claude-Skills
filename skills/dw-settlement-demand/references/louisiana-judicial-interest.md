# Louisiana Judicial Interest

How to compute judicial interest on a Louisiana personal-injury claim and present it in the demand.

---

## Legal foundation

**La. R.S. 13:4203** — Legal interest shall attach from the date of judicial demand on all judgments sounding in damages, "ex delicto" (i.e., tort).

**La. R.S. 13:4202** — Sets the annual judicial-interest rate. The Commissioner of Financial Institutions determines the rate on the first business day of October each year, set at 3.25 percentage points above the Federal Reserve's discount rate. The new rate takes effect the following January 1.

**Practical effect for PI:**
- Interest starts on the date the petition / lawsuit is filed (judicial demand).
- The rate changes annually on January 1.
- Interest compounds simply (not compounded), per Louisiana judgments.
- For mediation papers, the firm computes JI through the mediation date (or through today's date if mediation is unscheduled) and adds it to the demand.
- For pre-suit demands, interest has not yet started accruing — the demand can either (a) skip the JI section, (b) write "TBD upon judicial demand," or (c) compute hypothetical JI as if suit had been filed on a representative date for negotiating purposes (rare).

---

## Annual Louisiana Judicial-Interest Rates

The firm's recent demand papers cite these rates. The skill should refresh this table each year by checking the LSBA's published rate. The rates below are accurate as of the firm's last review; verify against the Louisiana State Bar Association's current published rate before using in a draft.

| Year | Rate |
|------|------|
| 2010 | 3.75% |
| 2011 | 4.00% |
| 2012 | 4.00% |
| 2013 | 4.00% |
| 2014 | 4.00% |
| 2015 | 4.00% |
| 2016 | 4.00% |
| 2017 | 4.25% |
| 2018 | 5.00% |
| 2019 | 6.00% |
| 2020 | 5.75% |
| 2021 | 3.50% |
| 2022 | 3.50% |
| 2023 | 6.50% |
| 2024 | 8.75% |
| 2025 | 8.25% |
| 2026 | [verify with LSBA — published December of prior year] |

**Important:** verify the current year's rate against `https://www.lsba.org/members/judicialinterestrate.aspx` before publishing the demand. Rates have moved sharply in recent years.

---

## Calculation Formula

For each calendar year (or portion thereof) that the claim has been in suit:

```
Daily Rate          = Principal × (Annual Rate ÷ 365)
Year's Interest     = Daily Rate × Days-in-Period

Where Days-in-Period = number of days from the later of (a) judicial-demand date and (b) Jan 1 of that year, through the earlier of (c) Dec 31 of that year and (d) the target date (today / mediation date).
```

Sum all years' interest = Total Judicial Interest.

For demand purposes, the **principal** is typically the total of (Past Medicals + General Damages + Past Lost Wages) — judicial interest does not run on future damages from the date of judicial demand under Louisiana law for most tort cases, though there are nuances. **Best practice:** compute JI on the special damages and general damages only, exclude future medicals and future lost wages, and note the methodology in a footnote so the defense doesn't waste time arguing it.

---

## Worked Example

**Scenario:** Suit filed July 1, 2023. Principal subject to JI = $1,000,000. Compute JI through today (May 12, 2026).

**Year 2023** (July 1 → Dec 31 = 184 days; rate 6.50%):
- Daily rate = $1,000,000 × (0.0650 / 365) = $178.08/day
- 184 days × $178.08 = **$32,766.85**

**Year 2024** (Jan 1 → Dec 31 = 366 days, leap year; rate 8.75%):
- Daily rate = $1,000,000 × (0.0875 / 366) = $239.07/day
- 366 days × $239.07 = **$87,500.00**

**Year 2025** (Jan 1 → Dec 31 = 365 days; rate 8.25%):
- Daily rate = $1,000,000 × (0.0825 / 365) = $226.03/day
- 365 days × $226.03 = **$82,500.00**

**Year 2026** (Jan 1 → May 12 = 132 days; rate [check LSBA]; assume 7.50% for illustration):
- Daily rate = $1,000,000 × (0.0750 / 365) = $205.48/day
- 132 days × $205.48 = **$27,123.29**

**Total Judicial Interest through May 12, 2026: $229,890.14**

---

## How to Present in the Demand

For `mode = demand` (compact):
> **E. JUDICIAL INTEREST**
>
> Pursuant to La. R.S. 13:4203, [Plaintiff] is entitled to judicial interest on all amounts awarded, accruing from the date of judicial demand of [Date]. As of [today's date], judicial interest on the special damages and general damages principal of $[Principal] is computed as follows:
>
> | Year | Days | Rate | Interest |
> |------|------|------|----------|
> | [Year] | [###] | [#.##%] | $ [Amount] |
> | ... | ... | ... | ... |
> | **Total** | | | **$[Total JI]** |

For `mode = mediation_paper` (more narrative + footnote):
> **V. JUDICIAL INTEREST**
>
> Under La. R.S. 13:4203, legal interest attaches to all tort judgments from the date of judicial demand. [Plaintiff] filed suit on [Date]. From that date through [today's date or mediation date], judicial interest at the rates set by La. R.S. 13:4202 has accrued on the [Principal] of $[Principal] as follows:
>
> [Year-by-year breakdown as above]
>
> **Total Judicial Interest accrued through [Date]: $[Total JI].**

For pre-suit demands (no judicial demand yet):
> **E. JUDICIAL INTEREST**
>
> Should this matter proceed to suit and judgment, [Plaintiff] will be entitled to judicial interest from the date of judicial demand pursuant to La. R.S. 13:4203, at the annual rates published by the Louisiana Commissioner of Financial Institutions under La. R.S. 13:4202.

---

## Edge Cases

### Suit filed mid-year, mediation mid-year
Compute partial-year interest at the start and end. Example: filed June 15; mediation August 20 of next year — that's three partial periods (Year 1: June 15 – Dec 31; Year 2: Jan 1 – Dec 31; Year 3: Jan 1 – Aug 20).

### Pre-judgment vs. post-judgment interest
The R.S. 13:4202 rate applies to both. For demand purposes, only pre-judgment interest matters (case hasn't been to judgment yet).

### Workers' comp cases
Interest runs differently for comp benefits — outside the scope of this skill. Flag and refer to the appropriate WC framework if applicable.

### Federal court tort claims (USDC)
Louisiana law on judicial interest applies in diversity cases (Erie doctrine). The same rate and methodology apply.

### Settlement during a tax year
JI stops accruing on settlement. Compute through the settlement date if one is set.

---

## Strategic Considerations

- **Compute it fully whenever possible.** Adds an "objective" math anchor to the demand. Even a small JI total ($20k–$50k) on a soft-tissue case feels less negotiable than the "discretionary" general-damages number.
- **In years of high rates (2023–2025), JI accumulates fast.** A $1M case sitting in suit for two years at 8%+ rates accrues $160k+ in JI alone.
- **Defense can argue prejudgment-interest is set aside in settlement.** True, but the inclusion in the demand frames it as part of the value of the case.
- **Don't compute JI on future damages.** Defense will challenge it and the attorney will lose credibility on the math.
- **Round to dollars in the table, not pennies.** The JI math is approximate enough that pennies look like false precision.
