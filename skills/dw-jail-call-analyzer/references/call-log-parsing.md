# Call Log Parsing Reference

Vendor-by-vendor ingestion guide for jail-call discovery productions. Used by `dw-jail-call-analyzer` Module A.

## Canonical D&W Schema

Every vendor export normalizes to this column set before downstream modules consume it:

| Canonical Field | Type | Description |
|-----------------|------|-------------|
| `call_id` | string | Vendor-issued unique identifier; normalize whitespace and case |
| `start_ts` | ISO 8601 datetime | Call start timestamp in facility local time; convert to UTC and store both |
| `end_ts` | ISO 8601 datetime | Call end timestamp; if vendor provides duration only, compute `start_ts + duration` |
| `duration_sec` | integer | Total call duration in seconds; reject negative or zero values into a "failed attempts" bucket |
| `pin` | string | Inmate PIN / SID / commissary number used to authenticate the call |
| `dialed_number` | string | E.164 normalized destination number; strip extensions for matching, retain raw form for reference |
| `recipient_name_vendor` | string | Vendor-supplied recipient name (often unreliable, e.g., the name on the commissary account, not the actual answerer) |
| `completion_status` | enum | `connected`, `attempted`, `blocked`, `dropped`, `three_way_blocked`, `voicemail`, `unknown` |
| `recording_path` | string | Relative path from production root to the WAV/MP3/AAC file |
| `vendor_flags` | string | Free-text vendor-applied flags: privileged, three-way attempt, security alert, etc. |
| `facility` | string | Facility code (e.g., CCC for Calcasieu Correctional Center, OPSO for Orleans Parish, EBRPP for East Baton Rouge Parish Prison) |

## Vendor Conventions

### Securus

The dominant vendor in Louisiana facilities. Exports as CSV or XLSX, sometimes split into multiple files when the date range exceeds the export cap.

- Call ID column: `Call ID` or `CallID` — alphanumeric, format varies by facility
- Timestamp: `Start Date Time` and `End Date Time` in facility local time; usually CT in Louisiana, but verify — federal facilities sometimes export in UTC
- PIN: `Inmate Account` or `Inmate ID`
- Dialed number: `Called Number` — leading `1` may or may not be present; normalize
- Recipient: `Called Party Name` — comes from the called number's commissary account if registered; often blank
- Duration: `Talk Time` (seconds) plus separate `Connect Time` (seconds spent dialing/ringing); use Talk Time for the duration_sec field
- Privileged calls: marked with `Privileged Flag = Y` if the dialed number was registered as an attorney line; if unregistered, the call records normally and the flag is blank — this is the most common attorney-client exposure
- Three-way attempts: `3-Way Attempt = Y` — the system detects but does not always block
- Recording path: `Recording File` column or derived from a `Recordings/<yyyy>/<mm>/<call_id>.wav` directory tree

### GTL / ViaPath (formerly Global Tel*Link)

Second-most-common in Louisiana. Branded as "ViaPath" since 2022 but log headers often still read "GTL."

- Call ID: `EventID` — numeric, often 10-12 digits
- Timestamp: `CallStart` and `CallEnd` — facility local; verify against booking records
- PIN: `BookingNumber` or `OffenderID`
- Dialed number: `DialedNumber`
- Recipient: `CalledPartyName` (often blank) and `CalledPartyAddress` (sometimes contains city/state)
- Duration: `Duration` (seconds, but occasionally HH:MM:SS — sniff the column)
- Completion: `Status` with values `Completed`, `Refused`, `BlockedNumber`, `InsufficientFunds`, `3WayDetected`, `LiveMonitor` — note that `LiveMonitor` indicates a facility staff member listened in real time
- Recording path: `RecordingURL` (web link) or local path — productions vary

### NCIC (Network Communications International Corp)

Common in smaller parish jails. Exports as CSV.

- Call ID: `RecordID` or `CDR_ID`
- Timestamp: single `CallTime` field combining start; duration computed separately
- PIN: `InmatePIN`
- Dialed number: `Destination`
- Duration: `Length` in MM:SS format — convert to seconds
- Status: `Outcome` with values `Connected`, `NoAnswer`, `Busy`, `Blocked`, `ThreeWayDetect`
- Recording path: usually `<call_id>.wav` in a flat directory; smaller facilities sometimes produce as a single concatenated archive

### IC Solutions

Found in some Louisiana facilities and federal pretrial holding.

- Call ID: `Call_Reference` — alphanumeric with embedded date stamp
- Timestamp: `Call_Date` and `Call_Time` as separate fields — concatenate
- PIN: `Inmate_Number`
- Dialed number: `Dial_Number`
- Duration: `Talk_Seconds`
- Status: `Disposition`
- Recording path: derivable from call reference via documented IC Solutions URL pattern

### Telmate

Less common in Louisiana but appears in some federal cases.

- Call ID: `id`
- Timestamp: `start_time` (UTC by default — convert to facility local for analyst readability)
- PIN: `inmate_id`
- Dialed number: `to_number`
- Duration: `duration` (seconds)
- Status: `status`
- Recording: `recording_url`

### CPCSDS / Custom Parish Systems

A handful of Louisiana parishes run in-house systems or contracts with regional vendors. When a production does not match any of the above, request the vendor name and column dictionary from the prosecutor in writing — do not guess at the schema. Productions from non-mainstream vendors sometimes omit duration, completion status, or the recipient name field entirely; flag those omissions in the audit's Methodology section.

## Deduplication Logic

Calls duplicate across productions for predictable reasons:

1. **Facility transfer.** When the client moves between facilities (parish jail → state DOC intake → state prison, or pretrial holding → main parish jail), the new facility issues a new PIN and the call record may appear in both vendors' exports for an overlapping window. Deduplicate on `(start_ts UTC, dialed_number, duration_sec)` ignoring vendor / call_id.

2. **Raw vs. cleaned exports.** Prosecutors sometimes produce both a raw vendor dump and a "responsive subset." Identify and prefer the raw export; flag any call in the cleaned export that is missing from the raw export — that is itself a discovery anomaly.

3. **Attempt vs. completed.** A failed attempt followed by a completed call to the same number 30 seconds later is two calls, not one. Do not deduplicate by recipient + nearby timestamp; the failed-attempt log carries independent forensic value.

4. **Re-billing entries.** Some vendors create a second log entry when a call is re-billed (e.g., a refund processed for a dropped call). The duration will be 0 or the completion_status will be `re_bill`. Treat as ledger noise; suppress from the analysis manifest but retain in the raw archive.

Deduplication output must report: total records ingested, duplicates removed, rationale for each deduplication rule fired.

## Audio-to-Call-ID Mapping

Three common patterns:

- **Direct.** `<call_id>.wav` in a flat directory or a `Recordings/yyyy/mm/<call_id>.wav` tree. Securus and many GTL exports.
- **Composite.** `<pin>_<yyyymmddhhmmss>.mp3`. Reconstruct call_id by joining to the log on `(pin, start_ts)`. NCIC and some smaller vendors.
- **Hex-string.** `<32-character-hex>.wav` with no obvious relation to the log. Usually accompanied by a separate manifest file mapping hex → call_id; if absent, request from prosecutor.

Map every audio file to a call_id; map every log entry to an audio file. Report:

- Calls in log without audio (production deficiency — flag for `dw-discovery-compliance-monitor`)
- Audio files without log entries (ghost calls — sometimes legitimate test calls or system audio, sometimes meaningful; spot-check a sample)
- Audio files that exist but are unplayable (corrupted, zero-byte, or wrong codec)
- Audio files where the duration in the file header materially diverges from the duration in the log (recording truncation — flag for *Brady* concern)

## Date-Range Validation

Confirm the production date range covers:

- From: at least the date of booking (request booking record from `dw-court-jail-tracker` if not in hand)
- To: at least the most recent production cutoff stipulated by the prosecutor

Gaps of more than 24 hours in the date range — especially gaps coinciding with a hearing, a co-defendant's proffer, or a known major case event — are themselves a finding. Note in Methodology and consider a discovery motion.

## Time Zone Hygiene

Louisiana facilities operate in CT (CST/CDT). Some vendor exports are in UTC; some are in facility local; some are in the inmate's enrolled home-state time. Confirm by spot-checking a known event (e.g., a call right after a hearing the attorney attended) and reconcile. Store both UTC and facility-local in the canonical schema. Display times in the audit report in facility local with the time zone abbreviation appended, e.g., `2026-04-15 09:24 CT`.

## Recipient ID Sheet Build

For every unique dialed number in the corpus:

- Apply the vendor-supplied name as a starting point
- Cross-reference against any defense-investigator notes
- Cross-reference against the State's witness list
- Cross-reference against `dw-witness-threat-matrix` if built
- Apply the recipient category from the SKILL.md Module A.4 list
- Where the recipient is unknown, mark as `UNKNOWN — investigator follow-up required` and treat as State witness for triage purposes

Persist the recipient ID sheet as Appendix B of the audit report and as a standalone XLSX in the same output folder, so the trial team can update it as new identifications occur.

## Edge Cases

- **Conference numbers.** Some facilities allow inmates to pre-register conference call numbers (e.g., legal aid hotlines, religious counselors). These usually carry a privileged flag. Verify by checking the facility's published list of approved numbers.
- **Spanish-language calls.** Note in the Methodology section if the corpus includes non-English calls. Transcript pipeline must be configured for the appropriate language; route through `dw-transcript-pipeline-rev` with the language code set explicitly.
- **Calls cut off at system maximum.** Most facilities cap individual calls at 15 minutes. A call that hits the cap and is followed within 60 seconds by a re-dial to the same number is a continuation, not a separate substantive call; cluster them in the analysis.
- **Calls from another inmate's PIN.** If the corpus includes calls authenticated under a different inmate's PIN but featuring the client's voice, that is a separate finding (PIN sharing is a facility rule violation and is itself probative). Flag for Module B.
