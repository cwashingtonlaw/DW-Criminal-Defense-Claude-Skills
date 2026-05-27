# Workflow Integration

## Master Evidence Table Entries

For each piece of social media evidence audited, generate a row for the Master Evidence Table in `Case Tables.xlsx` with:
- **Doc #:** sequential per naming convention
- **Evidence Type:** "Social Media — [Platform] — [Type: Screenshot/Records/Extraction]"
- **Description:** brief content summary including what the State claims it proves
- **Review Priority:** HIGH for any social media evidence the State intends to use at trial
- **Defense Relevance:** FLAG if authentication is weak; FAVORABLE if content supports defense theory; NEUTRAL otherwise

## Issue Codes (Required — Always Include)

Every audit report must include an explicit **Issue Codes** section assigning codes from the D&W taxonomy. This is not optional — the Master Evidence Table depends on these codes for filtering and tracking. List each applicable code with a one-line explanation of why it applies to this case.

Available codes for social media evidence:

- **AUTH** — Authentication challenge (Art. 901)
- **HEAR** — Hearsay objection (no custodian certification)
- **4AMD** — Fourth Amendment (warrantless access to social media)
- **BRDY** — Brady/Giglio (platform records not disclosed that may be exculpatory)
- **COC** — Chain of custody gap
- **SPOL** — Spoliation (ephemeral content lost due to delayed preservation)
- **ID** — Identity/attribution dispute
- **CNTX** — Context challenge (cropped/incomplete evidence)
- **FABR** — Fabrication concern (screenshot integrity)
- **META** — Metadata gap or stripped metadata

Format the section like this in every report:
```
📋 ISSUE CODES FOR MASTER EVIDENCE TABLE
- AUTH — [Why it applies in this case]
- ID — [Why it applies in this case]
- FABR — [Why it applies in this case]
[...all applicable codes]
```

## Cross-Examination Chapter Seeds (Required — Always Include)

Every audit report must generate at least one **CROSS CHAPTER SEED** for each critical finding, formatted exactly as shown below for seamless handoff to the **dw-cross-exam-architect** skill. This is the integration point between the audit and trial prep — without these seeds, the cross-exam architect has to start from scratch. Always use this exact format:

```
CROSS CHAPTER SEED — [Finding Title]
Witness Type: Law Enforcement / Expert / Civilian (Social Media Evidence)
Chapter Goal: [What this chapter must establish]
Key Questions:
  Q1: [Question targeting the deficiency]
  Q2: [Follow-up that locks in the concession]
  Q3: [Question establishing the significance of the gap]
Source: [Evidence reference — Bate stamp if available]
Impeachment Note: [If witness's testimony contradicts platform architecture or metadata]
Legal Authority: [La. C.E. Art. 901 / Art. 803(6) / specific standard]
```

Tag every seed: `[READY FOR CROSS-EXAM ARCHITECT — pass to dw-cross-exam-architect skill]`

Generate seeds for at minimum: (1) authentication failure, (2) account attribution gap, and (3) any platform-specific vulnerability identified in the audit. More seeds are better — the cross-exam architect can always consolidate.
