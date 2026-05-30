# DEVONthink Search Protocol — Pretrial Motion Library

Before drafting any motion, search DEVONthink for firm templates, prior filings, case law, and reference materials. Run searches specific to the motion type requested.

## General searches (run for every motion type)

```
devonthink:search
query: "[motion type keywords]"
databaseName: Law Library-Criminal
groupPath: /Motions/General Motions
limit: 15
```

```
devonthink:search
query: "[motion type keywords]"
databaseName: Law Library-Criminal
groupPath: /Motions
limit: 15
```

```
devonthink:search
query: "[motion type keywords]"
databaseName: Law Library-Criminal
groupPath: /Reference Materials/LA Criminal Trial Practice Formulary
limit: 10
```

## Known key resources in DEVONthink

- `Motions Practice OVERVIEW OUTLINE` — comprehensive motions practice guide (General Motions group)
- `CRIMINAL PLEADING INDEX` — index of all criminal pleading forms (root level)
- `Complete Manual to Criminal Forms` — reference manual (Reference Materials)
- `Louisiana Criminal Trial Practice Formulary` — LA-specific forms (Reference Materials)
- `Criminal Procedure Handbook` — procedure reference (Reference Materials)

## Also search seminar/CLE materials

```
devonthink:search
query: "[motion topic]"
databaseName: Law Library-Criminal
groupPath: /NACDL CLE Materials
limit: 5
```

```
devonthink:search
query: "[motion topic]"
databaseName: Law Library-Criminal
groupPath: /LACDL All That Jazz
limit: 5
```

## Template Selection Protocol

**After all DEVONthink searches complete**, read and follow the Template Selection Protocol at `dw-shared-protocols-crim/references/template-selection-protocol.md` (Steps A through D). Present the top 3 results, let the attorney select a template or paste a DEVONthink link, and load the selection before proceeding. Do not proceed to drafting until the attorney has selected a template or chosen to draft from scratch.

If a template is selected, preserve the firm's preferred formatting and legal positions — then update with case-specific facts and authority. If drafting from scratch, use this skill's built-in structure.
