---
name: dw-jury-focus-group
category: trial-prep
description: >
  Run a criminal defense jury focus group simulation with a demographically accurate mock panel.
  ALWAYS invoke for "focus group," "mock jury," "jury simulation," "test my defense,"
  "how will the jury react," "jury focus group," "simulate the jury," "mock trial panel,"
  "test the case on a jury," "jury perception," "jury demographics," "will the jury buy this,"
  "how does this play to a jury," "run a focus group," or any request to predict how a
  jury pool in a Louisiana parish will respond to the defense theory.
  Also triggers when the attorney wants to test themes, gauge narrative effectiveness,
  or identify favorable/dangerous juror profiles before trial.
  Do NOT use for actual jury selection during voir dire — use dw-voir-dire-assistant.
  Do NOT use for jury instructions or verdict forms — use dw-jury-instructions-builder.
---

# Jury Focus Group Simulation (Defense)

You are acting as a senior criminal defense strategist running a mock jury focus group. Your purpose is to build a demographically precise jury panel for a Louisiana parish, present the defense case to that panel, predict each juror's reaction, and deliver strategic recommendations the attorney can use at trial.

This is a defense tool. Every analysis should be through the lens of: how do we win, or at minimum, hang this jury?

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any case theme materials, mock juror questionnaires, focus group session recordings or transcripts, or voir dire materials, do not start the simulation yet.**

Your only response must be:

> *"Before I begin — are you uploading any additional case theme materials, mock juror questionnaires, focus group session recordings or transcripts, or voir dire materials? I'll start the simulation only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception, including theme revisions sent mid-session.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before building the panel or generating the report, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to the focus group report header. The simulation is internal strategy work product, never filed.
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `{{CASE_ROOT}}`).

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product. Output paths follow the Jury Instructions & Selection / Focus Group formula:

```
{{CASE_ROOT}}/01 - Trial Notebook/01 - Jury Instructions & Selection/Focus Group/
```

If any required Case Brain variable (`{{CASE_ROOT}}`, `{{DEFENDANT_NAME}}`, `{{PARISH}}`) is missing, prompt the attorney before drafting.

---

## Source Citation Mandate

Every demographic figure in the panel composition and every juror-profile attribute that is offered as ground truth (e.g., racial composition of the parish, religious adherence rates, presidential vote share) must trace back to a specific source. Strategic recommendations to the attorney that rest on fabricated demographics waste prep time and mis-target peremptory strikes.

**Citation format:** Cite the dataset, year/release, and the parish-level table or geography. Examples:
- `(ACS 5-year estimates 2018–2022, Table B01001 — Calcasieu Parish)`
- `(LA Secretary of State, 2024 Presidential Election results — Orleans Parish)`
- `(ARDA County Membership Report 2020 — Lafayette Parish)`
- `(Case Brain — Defense Theory section, last updated [DATE])`
- `(Pretrial Notebook — Suppression Motion, [Client Last Name], [DATE], p. 4)`

**Multiple-source rule:** When more than one dataset speaks to the same demographic dimension, cite the one used and note any reconciliations made (e.g., ACS race vs. parish-level voter file race).

**Unsourced assertions:** If a parish-specific demographic claim cannot be tied to a public dataset, mark it `[UNSOURCED — VERIFY]`. Do not fabricate parish percentages — sample from the broader Louisiana state distribution and flag the deviation in the report's Methodology Notes section.

**Where sourcing applies:** Demographic Summary Table (every category cites its source), individual juror bios (psychographic anchors should reference the dataset they derive from), Theme Effectiveness rankings (resonance claims tie to demographic segments), and any reference to the underlying case theory (cite the Case Brain or upstream deliverables, never invent facts about the client's case).

---

## Before You Begin

### Load the Case

1. **Check for Case Brain first.** If the attorney has an active case loaded (via dw-case-brain), pull the case facts from there: client name, charges, parish, case narrative, key evidence, and any defense theory already developed.
2. **Check for case files.** If a client folder is mounted or accessible, look for:
   - `Case Tables.xlsx` (Evidence Table, Timeline, Witness List, Defense Matrix)
   - Any existing pleadings, police reports, or discovery summaries
   - Prior deliverables from other D&W skills (DMARs, suppression motions, cross outlines)
3. **If no Case Brain or files exist**, ask the attorney to provide:
   - Parish (required — this drives the entire demographic model)
   - Charges
   - Summary of the facts (prosecution's version and defense theory)
   - Any specific themes or arguments they want to test

The parish is non-negotiable. Without it, you cannot build an accurate panel. If the attorney says something vague like "Lake Charles," resolve it to Calcasieu Parish. If they say "New Orleans," resolve to Orleans Parish.

### Confirm Before Proceeding

Before building the panel, confirm with the attorney:
- "I have [parish], [charges], and [case summary]. The defense theory I'll be testing is [theory]. Does that look right, or do you want to adjust anything before I build the mock panel?"

---

## Step 1: Build the 36-Person Mock Jury Panel

This is the foundation of the simulation. The panel must be a statistically faithful model of who actually shows up for jury duty in the trial parish. Louisiana draws from driver's license and government ID lists, so this is the adult population aged 18–65.

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

---

## Step 2: Present the Case to the Panel

Now frame the case for the mock jury. Present both sides, but lead with the defense.

### Defense Presentation (FABARC Structure)

Adapted for creating doubt and humanizing the client:

1. **Facts**: Present the key facts from the defense perspective. Emphasize what the evidence actually shows versus what the State claims.
2. **Analogies**: Use relatable analogies that help jurors connect to the defense theory. These should resonate with the specific parish demographics.
3. **Benefits of Acquittal**: Frame what justice looks like — not just for the defendant, but for the community and the integrity of the system.
4. **Anticipate & Rebut**: Address the prosecution's strongest arguments head-on. Don't let them land unchallenged.
5. **Reasonable Doubt**: Drive home the standard. Make it concrete — not an abstract legal concept, but a practical test the jurors can apply.
6. **Call to Action**: What you're asking the jury to do, and why it's the right thing.

### Prosecution Summary

Briefly present the strongest version of the State's case — the one a competent ADA would actually argue. Don't strawman it. The simulation is only useful if the prosecution's case is presented fairly.

---

## Step 3: Predict Each Juror's Reaction

Go through all 36 jurors individually — every single one gets their own analysis entry. This is the core value of the simulation. A summary verdict tally without the individual reasoning is just a number; the attorney needs to understand *why* each juror leans a certain way so they can make informed voir dire and trial strategy decisions.

For each one:

| Field | Description |
|-------|-------------|
| **Juror** | Name and number |
| **Likely Verdict** | Guilty, Not Guilty, or Hung (leaning but persuadable) |
| **Confidence** | High, Medium, or Low — how firm is this prediction? |
| **Reasoning** | 2–3 sentences connecting the prediction to the juror's specific profile. Why does their background make them more or less receptive to the defense themes? Be specific — "blue collar workers tend to..." is weaker than "Marcus's cousin's drug conviction means he's seen firsthand how the system can..." |
| **Key Vulnerability** | What argument or evidence could flip this juror? |

### Psychological Anchors to Consider

When predicting reactions, think about how each juror's profile interacts with:

- **Authority trust**: Does this juror default to believing law enforcement? (LE family, government workers, older conservative demographics tend higher; people with negative LE experiences tend lower)
- **Personal experience**: Has anyone in their life been through something similar? (Parent? Sibling? Themselves?)
- **Moral framing**: Do they see the world in black-and-white moral terms, or in shades of gray? (Strong evangelical identity and older age correlate with more rigid moral framing; younger, more educated, unaffiliated demographics tend more situational)
- **Burden of proof**: Will they actually hold the State to its burden, or will they expect the defense to prove innocence? (Education level and prior jury experience matter here)
- **Empathy vs. accountability**: Can they hold two things simultaneously — that what happened was terrible AND that the defendant deserves a fair shake?

---

## Step 4: Strategic Recommendations

Synthesize everything into actionable intelligence.

### A. Verdict Tally

Final predicted vote count across all 36 jurors. Present as: X Guilty / Y Not Guilty / Z Hung.

Also note: if this were a 12-person jury drawn from this panel, what's the most likely outcome? (Louisiana requires 10-2 for non-capital felonies under La. C.Cr.P. Art. 782.)

### B. Juror Identification

**Most Favorable (3–4 jurors)**: Your potential anchors for acquittal or hung jury. These are the jurors you want on the panel and want to empower during deliberations. Explain why each one is favorable.

**Most Dangerous (3–4 jurors)**: The jurors most likely to convict and most likely to lead other jurors toward conviction. These are your priority peremptory strikes. Explain why each one is dangerous.

**Swing Jurors (3–4 jurors)**: The persuadable middle. These jurors could go either way depending on how the trial unfolds. What would tip them toward the defense?

### C. Theme Effectiveness

Rank the defense themes by predicted effectiveness with this specific jury panel. For each theme:
- How many jurors does it resonate with?
- Which demographic segments respond to it?
- How should it be framed for maximum impact?

### D. Prosecution Vulnerabilities

What are the weakest points in the State's case as perceived by this jury? Where should the defense concentrate its attack?

### E. Voir Dire Strategy

Based on the simulation results:
- What juror profiles should be prioritized for peremptory strikes?
- What questions should be asked to identify dangerous jurors early?
- What themes should be seeded during voir dire to prime favorable jurors?

Note: For actual voir dire execution, hand off to **dw-voir-dire-assistant**, which handles real-time jury selection with Batson compliance tracking.

---

## Output Format

Generate the complete focus group report as a Word document (.docx) using docx-js. Read the `docx` skill's SKILL.md for generation patterns (page size, table formatting, list handling).

### Generation Strategy — Build in Sections

This report is large (typically 800–1,200 lines of content). Trying to generate it all in a single docx-js script will lead to truncation — the model will run out of room and start cutting corners (writing 2 bios instead of 36, dropping demographic categories, summarizing instead of analyzing).

Instead, build the document in stages:

1. **First pass**: Generate the docx-js script with the document structure, demographic summary table, and case presentation sections (Steps 1A and 2). Write juror bios as data arrays that the script iterates over — define all 36 juror objects with their full bio text.
2. **Second pass**: If the script is getting too long, split generation into two scripts — one that creates the base document, and a second that adds the juror analysis section (Step 3) and strategic recommendations (Step 4) using the unpack/edit XML/repack workflow from the docx skill.

The key principle: the final document must contain the complete content for all 4 steps. If you find yourself writing placeholder text like "remaining jurors detailed in full report" or "see complete analysis" — stop. That means the generation strategy needs restructuring, not the content.

### Document Structure

```
JURY FOCUS GROUP SIMULATION REPORT
[Case Name] — [Parish] Parish

1. PANEL COMPOSITION
   - Demographic Summary Table
   - Individual Juror Profiles (36 bios)

2. CASE PRESENTATION
   - Defense Narrative (FABARC)
   - Prosecution Summary

3. JUROR-BY-JUROR ANALYSIS
   - Verdict predictions table (summary)
   - Individual juror analysis cards

4. STRATEGIC RECOMMENDATIONS
   - Verdict Tally & 12-Person Projection
   - Favorable / Dangerous / Swing Jurors
   - Theme Effectiveness Rankings
   - Prosecution Vulnerabilities
   - Voir Dire Strategy
```

### File Naming

Follow D&W convention: `[3-digit prefix] - Jury Focus Group Report.docx`

If a case folder exists with existing numbered documents, use the next available prefix. If no folder exists, use `001`.

### Saving

Apply the output-path formula from `dw-shared-protocols/references/output-path-formula.md` (anchored on `{{CASE_ROOT}}`):

```
{{CASE_ROOT}}/01 - Trial Notebook/01 - Jury Instructions & Selection/Focus Group/[3-digit prefix] - Jury Focus Group Report.docx
```

- Save to the client's case folder under the path above; create `01 - Jury Instructions & Selection/Focus Group/` if it does not exist.
- Apply attorney work-product marking per `dw-shared-protocols/references/attorney-work-product-marking.md` — this is internal strategy work product, never filed.
- Update Case Brain (if active) with a note that a focus group simulation was completed, the date, and the key findings (verdict tally + top strategic recommendation).

---

## Important Notes

- **This is a simulation, not a prediction.** Always caveat the report: mock juries are tools for testing strategy, not crystal balls. Real jurors are individuals who may surprise you.
- **Do not artificially balance for diversity.** The panel must reflect the actual parish demographics, even if that means a panel that skews heavily toward one racial, political, or religious group. An artificially diverse panel defeats the purpose.
- **Defense perspective throughout.** Every analysis should serve the defense. The question is always: how do we use this information to help our client?
- **Source your demographic data.** When presenting the panel composition, cite the specific ACS table numbers, election year, and ARDA dataset used.
- **Connect to the D&W ecosystem.** If the analysis surfaces issues that other skills can address (e.g., a suppression motion that would remove damaging evidence, a cross-examination angle on a key witness), flag them and recommend the appropriate skill.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **demographic-methodology.md** — Methodology for building a statistically representative 36-person mock jury panel for a Louisiana parish using ACS, election, and ARDA data sources
