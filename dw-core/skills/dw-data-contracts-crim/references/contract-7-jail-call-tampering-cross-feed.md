# Contract 7: Jail-Call Tampering-Risk Cross-Feed — Full Schema

Read from the SKILL.md **Contract 7: Jail-Call Tampering-Risk Cross-Feed** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producer:** `dw-jail-call-analyzer-crim` (Module D)
**Consumer:** `dw-witness-threat-matrix-crim` (Post-Cross Refresh Mode and initial-build threat scoring)

### Purpose

When `dw-jail-call-analyzer-crim` Module D identifies witness-contact attempts, threats, coaching, or coordination patterns in jail-call recordings, those findings must flow into `dw-witness-threat-matrix-crim` so that affected witnesses' Vulnerability scores are updated and the Top 5 ranks per witness type reflect the new tampering signal.

### Filename Pattern

`Jail-Call Tampering Risk Cross-Feed — [Client Last Name] [Date].md`

Saved alongside the jail-call audit at `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

### Required Header

- `Schema Version: 1.0`
- `Date Generated: <ISO-8601>`
- `Producer: dw-jail-call-analyzer-crim`
- `Consumer Hint: dw-witness-threat-matrix-crim (Refresh Mode)`
- `Client Name`
- `Docket Number`
- `Total Calls Analyzed: <int>` (across all sampling tiers)

### Required Fields per Tampering-Risk Entry

One row per identified witness-contact event:

| Field | Type | Description |
|---|---|---|
| `witness_id` | string | Witness identifier matching the entry in `Case Tables.xlsx` Witness List |
| `witness_name` | string | Full witness name (sanity-check field; `witness_id` is authoritative) |
| `event_timestamp` | ISO-8601 | When the call/event occurred (call start time) |
| `severity` | enum | `CRITICAL` (direct threat or explicit coaching) / `SIGNIFICANT` (indirect contact attempt or coordinated messaging) / `MODERATE` (third-party message relay) / `MINOR` (mention without contact attempt) |
| `pattern_type` | enum | `direct-contact` / `indirect-contact-via-relay` / `three-way-call` / `threat` / `coaching` / `coordination` / `intimidation` / `bribery` |
| `call_id` | string | Source call ID for citation back to recording |
| `timestamp_range` | string | In-call timestamp range (e.g., `03:24-03:41`) where the event occurred |
| `quote` | string | Verbatim quote (or summary if not transcribable) |
| `recommended_action` | enum | `notify-court` / `motion-revoke-bail` / `add-to-witness-protection-request` / `cross-exam-fodder` / `no-action-document-only` |

### Consumer Behavior

`dw-witness-threat-matrix-crim` Post-Cross Refresh Mode (and initial-build mode) must:

1. Match each `witness_id` to its row in the threat matrix
2. Increase that witness's Vulnerability score by `severity` (CRITICAL=+3, SIGNIFICANT=+2, MODERATE=+1, MINOR=+0.5)
3. Add the `quote` and `call_id`/`timestamp_range` to the witness's "Tampering Signals" column
4. If the cumulative tampering score moves the witness across a Top 5 boundary, re-rank
5. If `recommended_action` is `notify-court` or `motion-revoke-bail`, surface as a HIGH-priority alert in the refresh output

### Schema Drift Policy

Bump Schema Version on any breaking change (renamed/removed required field, changed enum semantics). Consumer skills should refuse to parse a higher major version than they recognize.
