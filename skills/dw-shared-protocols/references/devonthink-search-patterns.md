# DEVONthink Search Pattern Library
**Version 1.0 | D&W Skills Reference**
**Attorney Work Product | Confidential**

> **This file supplements the template-selection-protocol.md** by providing specific, tested search patterns for each D&W skill motion type and document category. Search patterns should be refined over time as the firm's DEVONthink library grows.

---

## How to Use This Library

Each entry provides multiple search patterns to try, in order from most specific to broadest. All searches run against the `Law Library-Criminal` database in DEVONthink using the `devonthink:search` tool with the query and databaseName parameters.

**Search Priority:**
1. Try the primary keyword search first
2. If results are sparse, run the tag-based search
3. If still no results, try specialized searches for specific legal issues
4. Always check the LA Criminal Trial Practice Formulary as a fallback source

---

## Search Patterns by Motion Type

### Suppression Motions (dw-suppression-motion)

**Primary searches:**

```
query: "motion to suppress" AND "Fourth Amendment"
databaseName: Law Library-Criminal
```

```
query: tag:template AND tag:suppression
databaseName: Law Library-Criminal
```

**Specialized searches by issue:**

- **Warrantless search:** `"warrantless" AND "suppress" AND ("automobile exception" OR "exigent" OR "consent" OR "plain view" OR "search incident")`
- **Franks hearing:** `"Franks" AND ("affidavit" OR "warrant" OR "material misrepresentation")`
- **Confession suppression:** `"suppress" AND ("Miranda" OR "involuntary" OR "coerced" OR "Fifth Amendment")`
- **Fruit of the poisonous tree:** `"fruit" AND "poisonous tree" AND "suppress"`
- **Traffic stop:** `"motion to suppress" AND ("traffic stop" OR "Terry" OR "reasonable suspicion")`

**Folder path:** `/Motions/Suppression/`

---

### 404(b) Opposition (dw-404b-opposition)

**Primary searches:**

```
query: "404(b)" OR "Prieur" OR "other crimes"
databaseName: Law Library-Criminal
```

```
query: tag:template AND ("404" OR "prior bad acts" OR "other crimes")
databaseName: Law Library-Criminal
```

**Specialized searches:**

- **Kitchen sink opposition:** `"Prieur" AND "opposition" AND "prejudicial"`
- **Specific crime type limitation:** `"404(b)" AND "[specific crime type]" AND "undue prejudice"`

**Folder path:** `/Motions/404b/`

---

### Bond Reduction (dw-bond-and-release-motion)

**Primary searches:**

```
query: "bond reduction" OR "bail" AND "motion"
databaseName: Law Library-Criminal
```

```
query: "Art. 316" OR "Art. 341" OR "pretrial release"
databaseName: Law Library-Criminal
```

**Specialized searches:**

- **PR bond:** `"personal recognizance" OR "own recognizance" AND "release"`
- **Excessive bail:** `"excessive bail" AND "Eighth Amendment"`

**Folder path:** `/Motions/Bond/`

---

### Pretrial Motions (dw-pretrial-motion-library)

**By motion type:**

- **Speedy trial:** `"Art. 701" OR "speedy trial" AND "motion"`
- **Bill of particulars:** `"bill of particulars" AND "motion"`
- **Continuance:** `"continuance" AND "motion" AND "criminal"`
- **Motion to compel:** `"compel" AND "discovery" AND "motion"`
- **Severance:** `"severance" AND ("Art. 461" OR "Art. 704") AND "motion"`
- **Change of venue:** `"change of venue" OR "Art. 622" AND "motion"`
- **Recusal:** `"recusal" AND ("Art. 671" OR "judge") AND "motion"`
- **Quash indictment/information:** `"quash" AND ("indictment" OR "information") AND "motion"`
- **Competency:** `"competency" OR "Art. 641" OR "mental capacity" AND "motion"`
- **Reveal the deal:** `"reveal" AND ("deal" OR "agreement" OR "cooperation" OR "informant")`

**Folder path:** `/Motions/Pretrial/`

---

### Sentencing (dw-sentencing-mitigation-specialist)

**Primary searches:**

```
query: "sentencing memorandum" OR "mitigation"
databaseName: Law Library-Criminal
```

```
query: "Art. 894.1" OR "Dorthey" OR "excessive sentence"
databaseName: Law Library-Criminal
```

**Specialized searches:**

- **Downward departure:** `"Art. 890.1" OR "mandatory minimum" AND "departure"`
- **Youthful offender:** `"youthful" AND "sentencing" AND "mitigation"`

**Folder path:** `/Motions/Sentencing/`

---

### Jury Instructions (dw-jury-instructions-builder)

**Primary searches:**

```
query: "jury instruction" OR "jury charge" AND tag:template
databaseName: Law Library-Criminal
```

```
query: "Art. 802" OR "Art. 807" OR "responsive verdict"
databaseName: Law Library-Criminal
```

**Specialized searches:**

- **Self-defense:** `"jury instruction" AND ("self-defense" OR "justification" OR "Art. 20")`
- **Lesser included offense:** `"lesser included" OR "responsive verdict" AND "Art. 814"`

**Folder path:** `/Instructions/`

---

### Post-Conviction (dw-post-conviction-relief)

**Primary searches:**

```
query: "post-conviction" OR "PCR" OR "habeas corpus"
databaseName: Law Library-Criminal
```

```
query: "Art. 930" OR "ineffective assistance" OR "2254"
databaseName: Law Library-Criminal
```

**Folder path:** `/Post-Conviction/`

---

## General Search Tips

1. **Always run both searches:** Execute the primary keyword search AND the tag-based search. Tag searches often find templates that keyword searches miss.

2. **If few results:** Broaden the search by removing date restrictions, using fewer keywords, or checking if documents are in the target folder path.

3. **If too many results:** Narrow by adding the specific legal issue, statute number, or case type. Use AND operators to combine search terms.

4. **Check the LA Criminal Trial Practice Formulary:** If DEVONthink searches return nothing, the Formulary is a reliable fallback source for standard motion types and jury instructions.

5. **After a successful motion:** Offer to save the final, attorney-approved motion as a firm template with tags `template`, `motion`, and the specific motion type (e.g., `suppression`, `404b`, `bond`).

---

## Tag Conventions

When searching or saving templates, use these standardized tags:

| Tag | Purpose |
|-----|---------|
| `template` | Reusable firm template for pleading drafting |
| `motion` | Any motion filing (use with motion-type tags) |
| `suppression` | Suppression motion template/filing |
| `404b` OR `other-crimes` | 404(b) opposition or other crimes evidence |
| `bond` | Bond reduction or pretrial release |
| `pretrial` | Pretrial motions (speedy trial, compel, etc.) |
| `sentencing` | Sentencing memorandum or mitigation |
| `instruction` | Jury instruction template |
| `post-conviction` | Post-conviction or habeas filing |
| `approved` | Attorney-approved final version |
| `formulary` | Source: LA Criminal Trial Practice Formulary |

---

## DEVONthink Tool Reference

| Tool | Use Case |
|------|----------|
| `devonthink:search` | Run keyword and tag-based searches |
| `devonthink:get_record_by_identifier` | Load template by UUID (after user selects it) |
| `devonthink:get_record_content` | Extract full text of selected template |
| `devonthink:create_record` | Save approved draft as new firm template |
| `devonthink:add_tags` | Tag saved templates with standard tags |
| `devonthink:list_group_content` | Browse `/Motions/` or `/Instructions/` folder structure |

---

## Troubleshooting Search Failures

| Problem | Solution |
|---------|----------|
| No results at all | Broaden keywords; try tag-based search; check Formulary |
| Too many results (50+) | Add specificity: statute number, case name, legal issue |
| Results are old/dated | Use tag:approved to find vetted versions; refine keywords |
| Can't find a specific motion type | Search by statute (Art. 701 for speedy trial, etc.) |
| Results are reference articles, not templates | Filter by tag:template in your search |

---

## Notes for Skill Developers

Skills that consume this library should:

1. Reference this file in the skill's SKILL.md under "References"
2. Use search patterns provided here as a starting point
3. Report back successful searches with high-quality results so patterns can be refined
4. Add new patterns when discovering queries that return unexpectedly good results
5. Keep motion type tags consistent across all searches and saved templates

---

**Search patterns should be refined over time as the firm's DEVONthink library grows. Add new patterns when you discover queries that return good results.**

**Last updated: 2026-04-06**
