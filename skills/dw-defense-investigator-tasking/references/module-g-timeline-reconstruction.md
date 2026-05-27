# Module G — Timeline Reconstruction

Build a comprehensive defense timeline from investigation results.

## Timeline Construction Protocol

**Step 1: Extract Prosecution Timeline**
- Map every factual assertion from the prosecution's discovery chronologically
- Note the source for each entry (which report, which witness, which piece of evidence)
- Identify time gaps in the prosecution's timeline
- Identify unsupported time assertions (claims without corroborating evidence)

**Step 2: Build Defense Timeline**
- Map the defendant's account chronologically
- Map alibi witness accounts chronologically
- Map defense evidence chronologically
- Overlay defendant's phone records, GPS data, transaction records, and social media activity

**Step 3: Overlay and Compare**
- Identify conflicts between prosecution and defense timelines
- Identify gaps in prosecution timeline that defense can exploit
- Identify corroboration points for defense timeline
- Identify areas where prosecution timeline is supported by only a single source

**Step 4: Identify Alternative Suspect Activity**
- If applicable, map known movements of alternative suspects
- Identify opportunity windows for alternative suspects

## Timeline Output Format

```
DEFENSE TIMELINE RECONSTRUCTION

Case: State v. [Defendant]          Case No.: [Number]
Prepared by: [Investigator]         Date: [Date]

| Time | Event | Source | Prosecution Claim | Defense Position | Corroboration | Notes |
|------|-------|--------|--------------------|--------------------|---------------|-------|
| HH:MM | [Event description] | [Source document/witness] | [What prosecution says happened] | [What defense says happened] | [Supporting evidence] | [Gaps, conflicts, issues] |

TIMELINE GAPS IDENTIFIED:
1. [Description of gap — time period with no evidence from either side]
2. [Description of gap]

TIMELINE CONFLICTS IDENTIFIED:
1. [Description of conflict — prosecution says X, evidence suggests Y]
2. [Description of conflict]

INVESTIGATION TASKS GENERATED FROM TIMELINE ANALYSIS:
1. [New task to investigate gap or conflict]
2. [New task]
```
