# Search Strategies by Motion Type

This reference provides tailored search queries for each D&W motion-drafting skill. When the case law researcher is called by another skill, use these as starting templates and adapt to the specific facts.

## CourtListener Query Patterns

CourtListener supports three search modes. Use them in combination:

**Semantic search** (best for natural language — use this first):
- Phrase the query as you'd describe the legal issue to a colleague
- Example: "officer extended traffic stop beyond its purpose to wait for drug dog without reasonable suspicion"
- Filter by court: `lasc`, `la1coa`-`la5coa`, `ca5`, `lawd`, `lamd`, `laed`

**Keyword search** (Boolean operators for precision):
- Supports AND, OR, NOT, quotes for exact phrases
- Filter by date range, court, judge name
- Example: `"traffic stop" AND ("extended" OR "prolonged") AND "drug dog" court:lasc,la3coa`

**Hybrid search** (combines both — use for complex issues):
- Semantic understanding + required keywords
- Example: semantic query "traffic stop extended for drug dog" with required keywords ["reasonable suspicion", "Rodriguez"]

**Citation verification** (run on every case going into a filing):
- Input: case citation string (e.g., "State v. Hunt, 2019-00355 (La. 10/22/19)")
- Returns: confirmation of existence, correct citation format, case metadata

**Citing cases** (build citation chains for strong authority):
- Input: cluster ID from a prior search result
- Returns: all cases that cite the input case, sorted by relevance
- Use this to track how a legal principle has developed and whether the trend is favorable

## Table of Contents
1. [Suppression — Fourth Amendment](#suppression-fourth-amendment)
2. [Suppression — Fifth Amendment](#suppression-fifth-amendment)
3. [404(b) Opposition](#404b-opposition)
4. [Bond and Pretrial Release](#bond-and-pretrial-release)
5. [Sentencing Mitigation](#sentencing-mitigation)
6. [Expert Witness / Daubert](#expert-witness--daubert)
7. [Eyewitness Identification](#eyewitness-identification)
8. [Habitual Offender](#habitual-offender)
9. [Pretrial Motions (General)](#pretrial-motions-general)
10. [Jury Instructions](#jury-instructions)

---

## Suppression — Fourth Amendment

### Common Sub-Issues and Query Templates

**Warrantless search — vehicle exception**:
```
case.dev: "automobile exception" OR "vehicle search" AND "probable cause" --jurisdiction louisiana
case.dev: "Carroll doctrine" Louisiana search vehicle --jurisdiction louisiana
CourtListener semantic: "warrantless vehicle search automobile exception probable cause Louisiana"
CourtListener keyword: "automobile exception" AND "probable cause" court:lasc,la3coa
DEVONthink: "automobile exception" OR "vehicle search" in Law Library-Criminal
```

**Traffic stop — scope and duration**:
```
case.dev: "traffic stop" AND ("extended" OR "prolonged" OR "exceed scope") --jurisdiction louisiana
case.dev: "Rodriguez v. United States" Louisiana --jurisdiction "5th circuit"
CourtListener semantic: "officer extended traffic stop beyond original purpose to wait for drug dog without reasonable suspicion"
CourtListener keyword: "traffic stop" AND ("extended" OR "prolonged") AND "scope" court:lasc,la1coa,la2coa,la3coa,la4coa,la5coa
CourtListener citing: [find citing cases for Rodriguez v. United States in Louisiana/5th Circuit]
Consensus: NOT NEEDED
```

**Consent search — voluntariness**:
```
case.dev: "consent search" AND "voluntariness" AND ("coercion" OR "authority") --jurisdiction louisiana
case.dev: "State v. Owen" OR "Schneckloth v. Bustamonte" Louisiana
DEVONthink: "consent search" OR "voluntary consent" in Law Library-Criminal
```

**Warrant — probable cause deficiency**:
```
case.dev: "search warrant" AND "probable cause" AND ("insufficient" OR "stale" OR "bare bones") --jurisdiction louisiana
case.dev: "Franks hearing" AND "material misrepresentation" --jurisdiction louisiana
DEVONthink: "Franks" OR "warrant probable cause" in Law Library-Criminal
```

**Good faith exception**:
```
case.dev: "good faith exception" AND "Leon" --jurisdiction louisiana
case.dev: "State v. Johnson" AND "good faith" AND "warrant" --jurisdiction louisiana
```

**Cell phone search — Riley/Carpenter**:
```
case.dev: "Riley v. California" OR "cell phone search" AND "warrant" --jurisdiction louisiana
case.dev: "Carpenter v. United States" AND "cell site" AND "warrant" --jurisdiction "5th circuit"
```

---

## Suppression — Fifth Amendment

### Common Sub-Issues and Query Templates

**Miranda — custody analysis**:
```
case.dev: "Miranda" AND "custody" AND ("reasonable person" OR "free to leave") --jurisdiction louisiana
case.dev: "State v. Manning" OR "Stansbury v. California" custody Miranda --jurisdiction louisiana
CourtListener semantic: "Miranda custody analysis whether suspect was free to leave reasonable person standard"
CourtListener keyword: "Miranda" AND "custody" AND "free to leave" court:lasc,la3coa,ca5
```

**Miranda — invocation of rights**:
```
case.dev: "invocation" AND ("right to counsel" OR "right to silence") AND "unambiguous" --jurisdiction louisiana
case.dev: "Davis v. United States" OR "Berghuis v. Thompkins" --jurisdiction "5th circuit"
```

**Voluntariness of confession**:
```
case.dev: "involuntary confession" AND ("coercion" OR "threats" OR "promises") --jurisdiction louisiana
case.dev: "totality of circumstances" AND "confession" AND "voluntariness" --jurisdiction louisiana
CourtListener semantic: "involuntary confession obtained through coercion threats or promises totality of circumstances"
CourtListener keyword: "involuntary" AND "confession" AND ("coercion" OR "threats" OR "promises") court:lasc,ca5
Consensus: "false confessions" AND "interrogation techniques" OR "Reid technique reliability"
Consensus: "police interrogation" AND "coercion" AND "confession" year_min: 2010
```

**Juvenile interrogation**:
```
case.dev: "juvenile" AND ("Miranda" OR "confession" OR "interrogation") --jurisdiction louisiana
case.dev: "J.D.B. v. North Carolina" AND "juvenile custody" --jurisdiction "5th circuit"
Consensus: "juvenile interrogation" AND "suggestibility" OR "false confession" year_min: 2010
Consensus: "adolescent brain development" AND "decision making" AND "criminal justice"
```

---

## 404(b) Opposition

### Common Sub-Issues and Query Templates

**Prieur notice requirements**:
```
case.dev: "Prieur notice" OR "State v. Prieur" AND "other crimes" --jurisdiction louisiana
case.dev: "Article 404" AND "notice requirement" AND "timeliness" --jurisdiction louisiana
CourtListener semantic: "Prieur notice requirements for other crimes evidence under Article 404(B) timeliness and specificity"
CourtListener keyword: "Prieur" AND "notice" AND "404" court:lasc,la1coa,la2coa,la3coa,la4coa,la5coa
DEVONthink: "Prieur" OR "404" OR "other crimes" in group "/404 B - Other Crimes/"
```

**Balancing test / undue prejudice**:
```
case.dev: "404(B)" AND "probative value" AND "prejudicial effect" --jurisdiction louisiana
case.dev: "undue prejudice" AND "other crimes" AND "balancing" --jurisdiction louisiana
```

**Specific exceptions (tailor to what the state is arguing)**:
```
# Intent exception
case.dev: "404(B)" AND "intent" AND ("specific intent" OR "general intent") --jurisdiction louisiana

# System/plan exception
case.dev: "404(B)" AND ("system" OR "plan" OR "scheme") AND "other crimes" --jurisdiction louisiana

# Identity/modus operandi exception
case.dev: "modus operandi" AND "404(B)" AND "identity" AND "signature" --jurisdiction louisiana

# Knowledge exception
case.dev: "404(B)" AND "knowledge" AND "other crimes" --jurisdiction louisiana
```

---

## Bond and Pretrial Release

```
case.dev: "bond reduction" AND ("Article 316" OR "Article 341") --jurisdiction louisiana
case.dev: "excessive bail" AND "pretrial detention" --jurisdiction louisiana
case.dev: "pretrial release" AND ("conditions" OR "electronic monitoring") --jurisdiction louisiana
DEVONthink: "bond" OR "bail" OR "pretrial release" in Law Library-Criminal
Consensus (if applicable): "pretrial detention" AND "outcomes" OR "risk assessment" year_min: 2015
```

---

## Sentencing Mitigation

```
case.dev: "Article 894.1" AND "sentencing factors" --jurisdiction louisiana
case.dev: "Dorthey" AND "excessive sentence" AND "constitutional" --jurisdiction louisiana
case.dev: "youthful offender" AND "sentencing" AND ("mitigation" OR "Miller") --jurisdiction louisiana
DEVONthink: "sentencing" OR "mitigation" OR "894.1" in Law Library-Criminal
Consensus: "criminal rehabilitation" AND "recidivism reduction" year_min: 2015
Consensus: "adverse childhood experiences" AND "criminal behavior" OR "incarceration"
Consensus: "adolescent brain development" AND "maturity" AND "sentencing" (for young defendants)
Consensus: "trauma informed" AND "criminal justice" AND "sentencing"
```

---

## Expert Witness / Daubert

```
case.dev: "Daubert" OR "Foret" AND "reliability" AND "Article 702" --jurisdiction louisiana
case.dev: "[specific methodology]" AND ("unreliable" OR "error rate" OR "peer review") --jurisdiction louisiana
DEVONthink: "Daubert" OR "expert" OR "702" in Law Library-Criminal

# Consensus queries depend on the specific expert discipline:
Consensus (DNA mixtures): "DNA mixture interpretation" AND "error rate" OR "probabilistic genotyping"
Consensus (bite marks): "bite mark analysis" AND "reliability" OR "error rate"
Consensus (hair microscopy): "microscopic hair analysis" AND "forensic" AND "accuracy"
Consensus (ballistics): "firearm toolmark" AND "error rate" OR "reliability"
Consensus (fingerprints): "latent fingerprint" AND "error rate" OR "examiner accuracy"
Consensus (arson): "fire investigation" AND "pour patterns" OR "flashover" AND "methodology"
Consensus (drug recognition): "drug recognition expert" AND "accuracy" OR "validation"
Consensus (blood spatter): "bloodstain pattern analysis" AND "reliability" OR "accuracy"
```

---

## Eyewitness Identification

```
case.dev: "Manson v. Brathwaite" OR "Neil v. Biggers" AND "eyewitness" --jurisdiction louisiana
case.dev: "photo array" AND ("suggestive" OR "due process") --jurisdiction louisiana
case.dev: "showup identification" AND "unnecessarily suggestive" --jurisdiction louisiana
case.dev: "State v. Henderson" AND "eyewitness" (NJ framework — persuasive)
CourtListener semantic: "eyewitness identification suggestive photo array lineup procedure due process reliability"
CourtListener keyword: "eyewitness" AND ("suggestive" OR "photo array" OR "lineup") court:lasc,la3coa,ca5
CourtListener citing: [find citing cases for Manson v. Brathwaite and Neil v. Biggers in Louisiana]
DEVONthink: "eyewitness" OR "identification" OR "lineup" in Law Library-Criminal
Consensus: "eyewitness identification" AND "accuracy" AND "factors" year_min: 2010
Consensus: "cross-race effect" AND "eyewitness" OR "own-race bias"
Consensus: "weapon focus effect" AND "eyewitness memory"
Consensus: "confidence accuracy" AND "eyewitness identification"
Consensus: "double blind lineup" AND "administrator influence"
Consensus: "stress" AND "eyewitness memory" AND "accuracy"
```

---

## Habitual Offender

```
case.dev: "habitual offender" AND "Article 529.1" --jurisdiction louisiana
case.dev: "predicate conviction" AND ("Boykin" OR "valid guilty plea") --jurisdiction louisiana
case.dev: "cleansing period" AND "habitual offender" --jurisdiction louisiana
case.dev: "enhanced sentence" AND "habitual" AND "constitutional" --jurisdiction louisiana
DEVONthink: "habitual" OR "529.1" OR "predicate" in Law Library-Criminal
```

---

## Pretrial Motions (General)

**Speedy trial**:
```
case.dev: "speedy trial" AND "Barker v. Wingo" AND "factors" --jurisdiction louisiana
case.dev: "Article 701" AND "time limitation" AND "speedy trial" --jurisdiction louisiana
```

**Motion to compel discovery**:
```
case.dev: "motion to compel" AND "discovery" AND ("Article 716" OR "Article 718" OR "Article 719") --jurisdiction louisiana
```

**Severance**:
```
case.dev: "severance" AND ("co-defendants" OR "Bruton") --jurisdiction louisiana
case.dev: "Article 704" AND "severance" AND "prejudice" --jurisdiction louisiana
```

**Change of venue**:
```
case.dev: "change of venue" AND "pretrial publicity" AND "prejudice" --jurisdiction louisiana
```

---

## Jury Instructions

```
case.dev: "responsive verdicts" AND "[specific charge]" --jurisdiction louisiana
case.dev: "lesser included offense" AND "[specific charge]" --jurisdiction louisiana
case.dev: "self-defense instruction" AND "justification" AND "Article 20" --jurisdiction louisiana
case.dev: "Ramos v. Louisiana" AND "unanimous verdict" (for non-unanimous verdict challenges)
DEVONthink: "jury instructions" OR "jury charges" OR "responsive verdicts" in Law Library-Criminal
```
