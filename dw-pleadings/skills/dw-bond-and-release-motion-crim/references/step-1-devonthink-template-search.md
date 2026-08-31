# Step 1 — Template-First DEVONthink Search

Read at Step 1 to run the exact DEVONthink search queries and review the known bond / bail documents in the firm library before selecting a template.

**DEVONthink searches to run:**

```
devonthink:search
query: "bond reduction" OR "bail reduction" OR "pretrial release"
databaseName: Law Library-Criminal
limit: 20
```

```
devonthink:search
query: "bond" OR "bail"
databaseName: Law Library-Criminal
groupPath: /Motions/Bond and Bail
limit: 15
```

```
devonthink:search
query: "excessive bail" OR "conditions of release" OR "personal recognizance"
databaseName: Law Library-Criminal
limit: 15
```

```
devonthink:search
query: "post plea bond" OR "bond pending appeal"
databaseName: Law Library-Criminal
limit: 10
```

```
devonthink:search
query: "Art. 334" OR "Art. 319" OR "Art. 701" OR "speedy trial release"
databaseName: Law Library-Criminal
limit: 10
```

**Known documents in DEVONthink (Bond and Bail group):**
- `Motion Against Imposition of Cash Only Monetary Condition of Bond` — challenges cash-only bond
- `Motion for Discovery in Aid of Bond Hearing` — discovery for contested hearings
- `Motion for Pre-Trial Release` — general pretrial release motion
- `Motion for a Personal Recognizance Bond` — PR bond motion
- `Motion for Bail` — general bail motion
- `Notice and Motion to Set Bond` — initial bond setting
- `Motion for Formal Bail Hearing or Bail Reduction` — formal hearing request with reduction
- `Motion Against Excessive Monetary Condition of Bond` — excessive bail challenge

**Also in the root of Law Library-Criminal:**
- `Motion For Post Plea Bond` — post-plea bond template
- `Post Plea Bond Memorandum` — memorandum supporting post-plea release
- `Order Post Plea Bond` — proposed order template
- `pretrial release and detention 08.pdf` — treatise/seminar on pretrial release
- `Pretrial Release on Conditions.docx` — conditions of release template
- `adma walsh pretrial release.pdf` — Adam Walsh Act pretrial release materials
- `Motion for Formal Bail Hearing and Order Releasing Defendant on Own Recognizance or Bail Reduction` — comprehensive bail motion

**Also search the General Motions group for related motions:**
```
devonthink:search
query: "bond" OR "bail" OR "release"
databaseName: Law Library-Criminal
groupPath: /Motions/General Motions
limit: 10
```
