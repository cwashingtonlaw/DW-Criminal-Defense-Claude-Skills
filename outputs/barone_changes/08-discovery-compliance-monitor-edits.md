# Rec 08 — Discovery Compliance Monitor: Add Discovery Bucket Column

## Summary
Add a **Discovery Bucket** classification column to the Discovery Production Tracker using the **Barone 7-Bucket System**. This enables gap analysis by category — revealing whether entire categories of discovery are missing.

## The 7 Barone Discovery Buckets

| # | Bucket | What It Covers |
|---|--------|----------------|
| 1 | Law Enforcement Reports & Statements | Incident reports, supplemental reports, arrest reports, officer statements, IA records, use-of-force, training records |
| 2 | Physical/Forensic Evidence | Lab reports, crime scene photos, autopsy/ME, chain of custody, evidence inventories |
| 3 | Digital/Electronic Evidence | BWC, dash cam, CCTV, cell phone extractions, CSLI, social media, computer forensics, GPS |
| 4 | Witness Statements & Information | Civilian statements, victim statements, informant info, 911 calls, grand jury testimony |
| 5 | Expert Reports & Analysis | CVs, reports, underlying data/bench notes, testing protocols, proficiency testing, accreditation |
| 6 | Prosecution Case File | Plea offers, correspondence, internal memos, prior statements, co-defendant statements, cooperation agreements |
| 7 | Exculpatory/Impeachment (Brady/Giglio) | Exculpatory evidence, impeachment, witness histories, officer discipline, prior inconsistent statements, deals |

## Files Modified

### 1. `dw-discovery-compliance-monitor/SKILL.md`
- Added "Discovery Bucket Classification (Barone 7-Bucket System)" subsection to MODULE B
- Full 7-bucket table with descriptions
- Bucket completeness metric description
- Cross-reference to dw-neutral-inventory Report 0
- Updated production tracker schema reference to include Discovery Bucket column

### 2. `dw-data-contracts/SKILL.md`
- Added Discovery Bucket column to Contract 6 (Discovery Compliance Ledger) Required Columns table

### 3. `dw-criminal-defense/references/case-analysis-prompts.md`
- No change needed — Report 7 (Table of Missing Discovery) already captures missing items; the bucket classification enhances the compliance monitor's tracking but doesn't change the report prompt
