# Module A — Juror Questionnaire Analysis

## A.1 — Parsing and Cataloging

For each juror questionnaire uploaded, extract and organize the following data points into a structured juror profile:

**Identification Data:**
- Juror number / seat number
- Full name
- Parish of residence / neighborhood
- Age / date of birth
- Race / ethnicity (as reported or observable -- for Batson tracking only)
- Gender (for J.E.B. tracking only)

**Employment and Education:**
- Current occupation and employer
- Spouse/partner occupation and employer
- Educational background (highest level, field of study)
- Military service history
- Prior or current law enforcement employment (juror, spouse, family)
- Prior or current employment with DA's office, public defender, court system, corrections

**Personal and Family:**
- Marital status and family composition
- Children (ages, if provided)
- Community organizations, church membership, civic involvement
- Hobbies and interests (may reveal personality traits relevant to deliberation style)

**Legal System Exposure:**
- Prior jury service (civil or criminal, verdict reached, foreperson)
- Prior involvement as a party, witness, or victim in a criminal case
- Prior involvement as a party in a civil case
- Family members or close friends in law enforcement, prosecution, judiciary, corrections, or criminal defense
- Family members or close friends who have been charged with or convicted of a crime
- Family members or close friends who have been victims of crime (type of crime)

**Case-Specific Responses:**
- Knowledge of the case, parties, witnesses, or attorneys
- Opinions about the type of crime charged
- Views on law enforcement credibility
- Views on the criminal justice system generally
- Ability to follow the law as instructed (burden of proof, presumption of innocence, right to remain silent)
- Any hardship claims (medical, financial, caregiving, employment)
- Open-ended narrative responses

## A.2 — Red Flag Identification

For each juror, flag responses that indicate potential defense concerns:

**Automatic Red Flags (require immediate attention):**

| Response Pattern | Concern | Action |
|-----------------|---------|--------|
| Current or former law enforcement (juror or immediate family) | Authority bias; prosecution identification; may view evidence through investigator lens | Cause challenge under Art. 798(2) if LE connection is sufficiently close; targeted voir dire if not |
| Current or former DA office employee | Implied bias -- automatic cause challenge | Art. 798(2) |
| Victim of same type of crime charged | Victim identification bias; emotional decision-making; may project own experience onto facts | Cause challenge if cannot be fair (Art. 797(2)); intensive voir dire |
| Expressed opinion about defendant's guilt/innocence | Formed opinion -- cause challenge | Art. 797(2) |
| States cannot follow presumption of innocence | Will not accept law -- cause challenge | Art. 797(4) |
| States defendant should testify to prove innocence | Does not accept 5th Amendment right | Art. 797(4); targeted rehabilitation risk |
| Close relationship with victim, witness, or party | Relationship bias -- automatic cause challenge | Art. 797(1); Art. 798(3) |
| States cannot consider full range of verdicts | Will not accept law | Art. 797(4) |

**Elevated Concern Flags (require targeted voir dire):**

| Response Pattern | Concern | Voir Dire Focus |
|-----------------|---------|----------------|
| Family member in law enforcement (not immediate) | Deference to police testimony | Explore whether juror can critically evaluate LE testimony |
| Prior jury service resulting in conviction | May be conditioned to convict; may assume role of "experienced juror" | Ask about deliberation experience, whether they felt pressure, what they learned |
| Strong statements about "law and order" or crime in community | Punishment orientation; may prioritize conviction over careful deliberation | Explore whether views would affect ability to presume innocence |
| Active in victim advocacy organizations | Victim identification; may bring external framework to case evaluation | Explore whether advocacy work would influence deliberation |
| Expresses distrust of defense attorneys or "the system" | May view defense function with suspicion; may discount defense arguments | Explore views on defense counsel's constitutional role |
| Works in healthcare, social work, education (in cases involving children or vulnerable victims) | May apply professional diagnostic frameworks; may over-identify with alleged victim | Explore ability to separate professional experience from juror role |
| No higher education combined with highly technical case | May defer to expert witnesses without critical evaluation | Assess comfort with technical evidence, willingness to question experts |
| Strong religious convictions (in cases involving moral judgment) | May apply moral rather than legal standards; may have difficulty with reasonable doubt | Explore whether religious beliefs would affect ability to follow legal instructions |

## A.3 — Juror Profile Cards

For each juror analyzed, produce a **Juror Profile Card** in this format:

```
================================================================
JUROR PROFILE CARD
================================================================
Juror #:        [Number]
Name:           [Full Name]
Seat:           [If assigned]
Rating:         [STRIKE / CAUTION / ACCEPTABLE / FAVORABLE]
----------------------------------------------------------------

DEMOGRAPHICS
Age:            [Age]
Race/Ethnicity: [As reported — Batson tracking only]
Gender:         [As reported — J.E.B. tracking only]
Parish:         [Residence]
Education:      [Highest level / field]
Occupation:     [Current]
Spouse Occ:     [If applicable]

LEGAL SYSTEM CONNECTIONS
LE Connections:     [Detail any law enforcement ties]
Legal Profession:   [Any attorneys, judges, court staff in family]
Prior Jury Service: [Detail — type, verdict, foreperson]
Crime Victim:       [Detail — type, relationship, how long ago]
Criminal History:   [Family/friend involvement with criminal system]

CASE-SPECIFIC CONCERNS
[Bulleted list of concerning responses with
questionnaire question numbers / page references]

BIAS INDICATORS
[ ] Authority Bias (deference to LE/prosecution)
[ ] Victim Identification (personal crime experience)
[ ] Punishment Orientation (law-and-order mindset)
[ ] Confirmation Bias (pre-formed opinion)
[ ] 5th Amendment Hostility (expects defendant testimony)
[ ] Burden Shifting (expects defense to prove innocence)
[ ] Other: [specify]

CAUSE CHALLENGE GROUNDS
[Art. 797/798 analysis — see Module B]

RECOMMENDED VOIR DIRE QUESTIONS
[Top 3-5 follow-up questions — see Module D]

STRIKE RECOMMENDATION
Rating:     [STRIKE / CAUTION / ACCEPTABLE / FAVORABLE]
Basis:      [One-paragraph summary of reasoning]
Priority:   [If STRIKE — rank among all strike recommendations]
================================================================
```

**Rating Definitions:**

| Rating | Definition | Action |
|--------|-----------|--------|
| **STRIKE** | Juror presents unacceptable risk to the defense. Cause challenge should be attempted first; if denied, use peremptory strike. | Challenge for cause; if denied, prioritize for peremptory |
| **CAUTION** | Juror has concerning indicators but may be rehabilitable or may serve defense interests in specific ways. Requires intensive voir dire before final assessment. | Targeted voir dire; reassess after responses |
| **ACCEPTABLE** | Juror does not present identifiable defense concerns. Not ideal but not harmful. | Accept unless better alternatives exist or strike count allows |
| **FAVORABLE** | Juror profile suggests openness to defense themes — skepticism of authority, personal experience with system overreach, empathy for accused, strong reasonable doubt orientation. | Protect from State strikes; consider as anchor juror |
