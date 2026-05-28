# Rec 02 — Timeline Builder: Add Certainty Column

## Summary
Add a **Certainty** column to the timeline that tracks how confident the defense can be that an event actually occurred as described. Distinct from Confidence (timestamp precision) — Certainty tracks event reliability.

## Certainty Ratings
- **CONFIRMED**: Multiple independent sources corroborate, or device-generated record with no contradiction
- **PROBABLE**: Single reliable source (Tier 1-2) with no contradiction, or multiple Tier 3-4 sources in agreement
- **DISPUTED**: Sources disagree on whether or timing of event
- **UNCONFIRMED**: Single Tier 3-4 source only, or based on inference
- **ALLEGED**: Assertion by a party with an interest in the outcome

## Files Modified

### 1. `dw-timeline-builder/SKILL.md`
- Added Certainty column to Step 3 Event Extraction table
- Added Certainty Ratings definition section after Confidence Levels
- Added Certainty to Step 5A Chronological Master Timeline column list

### 2. `dw-criminal-defense/SKILL.md`
- Added Certainty to Phase 3 Step 1 Timeline columns list

### 3. `dw-criminal-defense/references/color-coding.md`
- Added Certainty column header color (Dark Green #006400) to Timeline Sheet headers
- Added Certainty Dropdown Cell Colors section with color specs for all 5 values

### 4. `dw-data-contracts/SKILL.md`
- Added Certainty column to Contract 4 Timeline Sheet schema (Dropdown type, Required)
