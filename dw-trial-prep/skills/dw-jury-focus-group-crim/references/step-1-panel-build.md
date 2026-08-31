# Step 1 — Build the 36-Person Mock Jury Panel (Detail)

Read at Step 1 of `dw-jury-focus-group-crim/SKILL.md` — the demographic category table, data-source rules, sampling process, Step 1 output requirements, and example bio, moved verbatim from SKILL.md.

---

### Demographic Categories

Model the panel across all of the following dimensions, matching parish-level proportions within ±1 juror per category:

| Category | Values |
|----------|--------|
| Age Group | 18–24, 25–34, 35–44, 45–54, 55–65 |
| Gender | Male, Female |
| Race/Ethnicity | White (non-Hispanic), Black (non-Hispanic), Hispanic/Latino, Other |
| Education | <High School, High School, Some College/Associate, Bachelor's, Graduate+ |
| Income Bracket | <$35k, $35–50k, $50–75k, $75–150k, $150k+ |
| Children at Home | Yes, No |
| Homeownership | Own, Rent |
| Political ID | Republican, Democrat, Independent |
| Religion | Evangelical Protestant, Mainline Protestant, Catholic, Unaffiliated, Other |
| Fox News Viewer | Yes, No |
| Occupation | White Collar (Mgmt), White Collar (Non-Mgmt), Blue Collar (Skilled), Blue Collar (Service), Government, Healthcare, Not in Labor Force |

### Data Sources and Methodology

Read `references/demographic-methodology.md` for the detailed approach to sourcing parish-level data. The short version:

- **Race, age, gender, education, income, children, homeownership, occupation**: U.S. Census Bureau American Community Survey (ACS) 5-year estimates. Use the most recent available data for the specific parish.
- **Political ID**: Derive from the most recent presidential election results in the parish. Republican vote share → Republican %, Democrat vote share → Democrat %, remainder → Independent.
- **Religion**: Association of Religion Data Archives (ARDA) county-level adherence data.
- **Fox News viewership**: Model from political ID and age (higher among Republican-leaning, 45+ demographics). This is an approximation — be transparent about it.

### The Process

1. **Generate a 1,000-person simulated population** using the parish demographics as probability distributions. Each simulated juror gets a value for every category, drawn proportionally.
2. **Sample 36 jurors** from that population using stratified sampling to ensure the final panel matches parish proportions within ±1 per category.
3. **Validate** the panel against the demographic targets. If any category is off by more than 1, resample.

### Output for Step 1

**A. Demographic Summary Table**
A single table showing the count for each value in every one of the 11 demographic categories listed above. Each category must appear with every value and its count. For example, Age Group must show all 5 brackets, Race must show all 4 groups, Occupation must show all 7 types, etc. The attorney needs a complete snapshot — a partial table (showing only 3 of 11 categories) is useless.

**B. Juror Profiles — All 36, No Exceptions**
For each of the 36 jurors, write a unique two-paragraph bio in conversational prose. The bio should weave together all demographic attributes naturally — not as a data dump, but as a person. Give each juror a first name and last initial.

Every single juror must have a full bio. The attorney needs to see who these people are to make strategic decisions. Writing 2 bios and then saying "remaining 34 detailed in full report" defeats the purpose of the simulation — there is no separate "full report," this IS the report. If the document is getting long, that's expected. A 36-person panel with bios will be a substantial document. That's the point.

**Example:**
> **Juror #7 — Marcus T.** Marcus is a 42-year-old Black man who works as a shift supervisor at a petrochemical plant in Westlake. He graduated from Sam Houston High School and completed some coursework at Sowela Tech but didn't finish his degree. He owns a modest home in Mossville and has two kids in elementary school. His household income is around $55,000.
>
> Marcus is a registered Democrat but doesn't follow politics closely — he's more likely to watch ESPN than CNN or Fox News. He was raised Baptist and still attends Greater St. Mary on Sundays, though he'd describe himself as spiritual rather than strictly religious. He's been called for jury duty once before but wasn't selected. He has a cousin who did time for a drug charge, which gives him a complicated relationship with the criminal justice system.

The bios should feel like real people the attorney might encounter in voir dire. Vary the level of detail and the narrative hooks — some jurors are straightforward, others have wrinkles that could matter.
