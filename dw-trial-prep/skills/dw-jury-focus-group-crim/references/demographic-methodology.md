# Demographic Methodology for Mock Jury Panel Construction

## Purpose

This document describes how to build a statistically representative 36-person mock jury panel for a Louisiana parish. The goal is to model the jury pool that would actually appear for jury duty — drawn from driver's license and government ID lists — not an idealized or artificially balanced panel.

## Data Sources

### Primary: U.S. Census Bureau American Community Survey (ACS)

The ACS 5-year estimates are the gold standard for parish-level demographics. Use the most recent available release.

| Demographic | ACS Table | Notes |
|-------------|-----------|-------|
| Age & Sex | S0101 | Age groups by sex for 18–65 population |
| Race/Ethnicity | B03002 | Hispanic/Latino origin by race |
| Educational Attainment | S1501 | Population 25+ by education level |
| Household Income | S1901 | Income brackets |
| Children in Household | S1101 | Households with own children under 18 |
| Homeownership | S2502 | Owner vs. renter occupied |
| Occupation | S2401 | Occupation by broad category |
| Employment Status | S2301 | Labor force participation |

**How to access:** data.census.gov → Search by table ID → Filter to parish (county equivalent in Louisiana) → Select most recent 5-year estimates.

**Key adjustment:** The ACS reports on the total population, but Louisiana jury pools draw from adults 18–65 with a valid driver's license or government ID. Filter age ranges accordingly and note that populations without government ID (undocumented residents, some elderly, some homeless) are effectively excluded from the jury pool.

### Political Identification: Parish Election Results

Louisiana doesn't have party registration in the same way as some states, so derive political identification from voting behavior.

**Source:** Louisiana Secretary of State election results (voterportal.sos.la.gov) for the most recent presidential election.

**Method:**
1. Pull the parish-level vote totals for Republican, Democrat, and third-party/other candidates
2. Republican vote share → Republican %
3. Democrat vote share → Democrat %
4. Third-party + non-voters (adjusted for turnout) → Independent %

**Example (Calcasieu Parish, hypothetical):**
- Republican: 62% of votes cast
- Democrat: 35% of votes cast
- Other: 3%
- Adjusted for ~60% turnout and non-partisan leaners: ~55% R, ~30% D, ~15% I

This is an approximation. Voting behavior and party identification aren't identical, but for modeling purposes this is the best parish-level proxy available.

### Religion: Association of Religion Data Archives (ARDA)

**Source:** ARDA U.S. Religion Census (thearda.com) — county-level religious adherence data.

**Categories to model:**
- **Evangelical Protestant**: Southern Baptist Convention, Assemblies of God, Church of Christ, Pentecostal denominations, independent evangelical churches
- **Mainline Protestant**: United Methodist, Presbyterian (USA), Episcopal, ELCA Lutheran, Disciples of Christ
- **Catholic**: Roman Catholic (dominant in southern Louisiana parishes — Acadiana, New Orleans, and the River Parishes)
- **Unaffiliated**: No religious affiliation (growing nationally, but still below national average in most Louisiana parishes)
- **Other**: Historically Black Protestant denominations (National Baptist Convention, AME, COGIC), Jewish, Muslim, Hindu, Buddhist, LDS, Jehovah's Witnesses

**Louisiana-specific note:** The state has a sharp religious geography. Parishes south of I-10 and along the Mississippi tend heavily Catholic (Cajun/Creole heritage). North Louisiana parishes are predominantly Evangelical Protestant (Southern Baptist, Pentecostal). This distinction matters enormously for jury psychology — Catholic jurors in Louisiana tend to be somewhat more communitarian and less punitive than Evangelical jurors, though this is a generalization with many exceptions.

### Fox News Viewership: Modeled Proxy

There is no parish-level Fox News viewership data. Model it as a proxy variable derived from:
- **Political ID**: Republican-leaning jurors are significantly more likely to be Fox News viewers
- **Age**: Viewership skews 45+ across all political affiliations
- **Education**: Slight inverse correlation with education level among conservative viewers

**Suggested model:**
| Political ID | Age 18–44 | Age 45–65 |
|-------------|-----------|-----------|
| Republican | 40% | 65% |
| Democrat | 5% | 10% |
| Independent | 15% | 30% |

Be transparent in the report that Fox News viewership is modeled, not measured.

## Panel Construction Process

### Step 1: Build the Probability Model

For each demographic category, convert the parish-level data into probability distributions. Example for a parish that is 70% White, 25% Black, 3% Hispanic, 2% Other:

```
P(White) = 0.70
P(Black) = 0.25
P(Hispanic) = 0.03
P(Other) = 0.02
```

Do this for every category. Some categories have interdependencies (e.g., race and political ID are correlated). Where data supports it, model conditional probabilities rather than treating categories as independent. At minimum, model these correlations:

- Race × Political ID (Black voters in Louisiana are overwhelmingly Democratic)
- Race × Religion (Black communities are disproportionately Evangelical Protestant or Historically Black Protestant)
- Education × Income (strong positive correlation)
- Age × Fox News viewership
- Political ID × Fox News viewership

### Step 2: Generate 1,000 Simulated Jurors

Using the probability model, generate 1,000 synthetic juror profiles. Each profile has a value for every demographic category.

For correlated variables, use conditional probabilities. For example:
- First draw Race
- Then draw Political ID conditional on Race
- Then draw Religion conditional on Race
- Then draw Education
- Then draw Income conditional on Education
- Etc.

### Step 3: Sample 36 Jurors

Use stratified sampling to select 36 jurors from the 1,000-person pool such that the final panel matches the parish proportions within ±1 juror per category.

**Validation check:** After sampling, verify every demographic category. If any category is off by more than 1 juror, resample. The ±1 tolerance accounts for rounding (36 jurors can't perfectly represent fractional percentages).

### Step 4: Generate Bios

For each of the 36 selected jurors, write a two-paragraph narrative bio. The bio should:
- Weave all demographic attributes into a natural story (not a bullet list)
- Include a first name and last initial appropriate to the juror's demographic profile
- Reference real local geography (neighborhoods, schools, employers, churches) appropriate to the parish
- Include at least one "narrative hook" — something that makes this juror memorable and potentially relevant to case strategy (e.g., a family member with a criminal record, a job in healthcare, a strong church community)
- Vary in style and detail — not every bio should follow the same template

## Louisiana Parish Quick Reference

Some parishes with distinctive demographics that affect jury composition:

| Parish | Key Characteristic |
|--------|--------------------|
| Calcasieu | Petrochemical/blue collar, politically conservative, racially mixed |
| Caddo | Shreveport metro, significant Black population, politically split |
| East Baton Rouge | State capital, university town, racially diverse |
| Jefferson | Suburban New Orleans, historically white flight, trending more diverse |
| Lafayette | Heart of Acadiana, Catholic, Cajun heritage, oil & gas economy |
| Orleans | New Orleans, majority Black, heavily Democratic, culturally unique |
| Ouachita | Monroe metro, North Louisiana, conservative, Evangelical |
| Rapides | Alexandria, military influence (Fort Johnson), racially mixed |
| St. Tammany | Northshore, affluent, overwhelmingly white and conservative |
| Tangipahoa | Hammond area, mixed rural/college town, moderate |

This is not exhaustive — Louisiana has 64 parishes, each with its own character. Always use actual ACS data rather than relying on generalizations.
