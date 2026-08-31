# Module A — Inventory & Classification Procedure

Read this file at MODULE A — it holds steps A.1 (ingest the call log), A.2 (deduplicate), A.3 (map audio to call ID), A.4 (classify recipients), and A.5 (volume metrics).

### A.1 Ingest the Call Log

- Identify the vendor from column headers and ID format. Securus, GTL/ViaPath, NCIC, IC Solutions, Telmate, and CPCSDS each have distinct conventions documented in the reference file.
- Normalize column names to the D&W canonical schema: `call_id`, `start_ts`, `end_ts`, `duration_sec`, `pin`, `dialed_number`, `recipient_name_vendor`, `completion_status`, `recording_path`, `vendor_flags`, `facility`.
- Confirm the date range matches the production posture (Step 1, Item 5). Gaps in the date range — especially around hearing dates — are themselves a finding (was the call list cherry-picked?).

### A.2 Deduplicate

Calls can appear multiple times when (a) the same call traverses two vendor systems on facility transfer, (b) the State produced both a raw export and a "cleaned" export, or (c) call attempts vs. completed calls are double-counted. Deduplicate on `(start_ts, pin, dialed_number, duration_sec)` tuple. Flag any near-duplicate that differs only in `completion_status` — the failed-attempt log is itself a tampering signal.

### A.3 Map Audio to Call ID

Audio files typically follow one of three naming patterns: `<call_id>.wav`, `<pin>_<yyyymmddhhmmss>.mp3`, or vendor-specific hex strings. Build the `call_id → audio_path` map and report any mismatches: calls in the log without audio (suppression / production deficiency) and audio files without log entries (ghost calls — sometimes legitimate, sometimes not).

### A.4 Classify Recipients

Every dialed number maps to a recipient category:

- **Family — neutral** (parents, siblings, children, spouse with no witness overlap)
- **Family — witness-adjacent** (family members who are also on the State's witness list or who are likely to be called)
- **Co-defendant** (current or charged)
- **State witness — civilian**
- **State witness — law enforcement** (rare but happens — usually a tipster relationship)
- **Victim or victim's family**
- **Romantic partner** (high admission-density category — frequently emotional, frequently incriminating)
- **Attorney line** (Module F)
- **Commercial** (bondsman, bail bond company, commissary, vendor service line)
- **Unknown** (request investigator follow-up; treat as State witness for triage purposes until cleared)

### A.5 Volume Metrics

Generate descriptive stats:
- Total calls, total audio hours, total connected vs. attempted
- Distribution by recipient category (table)
- Distribution by week (timeline chart — flag spikes around hearings)
- Distribution by time of day
- Top 10 most-called numbers
- Top 5 longest single calls
- Top 5 shortest connected calls
