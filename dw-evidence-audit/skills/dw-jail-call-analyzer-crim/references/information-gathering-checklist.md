# Information Gathering Checklist

Read this file at STEP 1 (Information Gathering Protocol) — it holds the full ranked Essential / Strategic / Contextual checklist (items 1-13) to collect before auditing.

### Essential (Must Have Before Auditing)

1. **Call Log / Vendor Export**
   - CSV, XLSX, or PDF call detail record from the jail's vendor
   - Must contain at minimum: call ID, date/time, originating PIN/inmate number, dialed number, duration, completion status
   - Vendor name (Securus, GTL/ViaPath, NCIC, IC Solutions, Telmate, CPCSDS) — column conventions vary
   - Date range covered — must extend at least from booking through the most recent production cutoff

2. **Audio Files (or Pre-Existing Transcripts)**
   - Full set of WAV/MP3/AAC recordings, named by call ID where possible
   - If audio is not pre-transcribed, route through `dw-transcript-router-crim` → `dw-transcript-pipeline-rev-crim` BEFORE running this skill at scale; transcripts are required for any sampling tier above log-only
   - If transcripts already exist (Rev, Verbit, in-house), confirm they are linked to call IDs

3. **Charges & Defense Theory**
   - Specific charges with statutory citations (e.g., La. R.S. 14:30.1 — Second Degree Murder)
   - One-paragraph defense theory pulled from `dw-case-brain-crim` — what happened from the defense perspective and what facts the defense must hold or avoid conceding
   - Identification of the contested elements (what the State must prove that the defense disputes)

4. **Recipient Identification Sheet**
   - Map of dialed numbers to known recipients (mother, girlfriend, co-defendant, witness, attorney, bondsman)
   - Where recipient is unknown, flag for investigator follow-up — call patterns to unknown numbers may be more revealing than calls to known recipients
   - Special flag for any number associated with: a State's witness, a co-defendant, a victim or victim's family, or counsel

5. **Production Posture**
   - Date the calls were produced in discovery
   - Whether the State has flagged specific calls for trial use (often produced as a "highlight reel" subset)
   - Any 14th JDC / 12th JDC / Orleans CDC pretrial order limiting use of jail calls

### Strategic (Request if Not Provided)

6. **Booking & Custody Timeline**
   - Date of arrest, date of booking, facility(ies), housing assignments
   - Any transfers between facilities (each transfer often resets PIN; calls may split across vendor accounts)
   - Whether the client has been in continuous custody or had any release / re-booking events

7. **Co-Defendant Call Sets**
   - Whether co-defendants are in custody and producing their own calls
   - Whether the State has cross-referenced co-defendant calls — three-way or relay communications often surface only when both sides are reviewed

8. **Witness List & Threat Matrix Status**
   - Most recent State's witness list (from Bill of Particulars, *res gestae* notice, or trial subpoena list)
   - Whether `dw-witness-threat-matrix-crim` has been built; if so, load the Top 10 CRITICAL/HIGH names so calls to or about those witnesses get priority routing

9. **Attorney-Client Call Marking**
   - Vendor logs typically auto-mark numbers registered as attorney lines (Securus "Privileged" flag, GTL "Atty" flag)
   - Confirm whether D&W's main line, the assigned attorney's cell, and any consulting expert lines are properly registered
   - Any unregistered attorney-line calls require Module F privilege analysis

10. **Prosecution Flagged-Call List**
    - If the State has identified specific call IDs as trial exhibits, those calls are auto-promoted to full-review tier regardless of other criteria
    - Request the list early; it shapes the entire audit

### Contextual (Gather from Uploaded Files)

11. **Three-Way Call Indicators**
    - Vendor flags for three-way connect attempts (often blocked but logged)
    - Audible third-party voices, phone-to-phone bridging, "hold on let me get her" patterns
    - Three-way calls to a witness through a relay are a Module D red flag

12. **Coded Language Indicators**
    - Repeated unusual nicknames, place-names, or numerical references
    - Pre-existing investigator notes on family slang or street terminology used by the client's circle

13. **Volume & Duration Metrics**
    - Total call count, total audio hours, distribution by recipient, distribution by week
    - Sudden spikes (e.g., a flurry of short calls the day before a hearing) often correlate with tampering or coordination attempts

**Present missing info as a ranked checklist before auditing.** If essential items 1-5 are missing, do not audit — ask for them first. If audio exists but no transcripts and no transcript pipeline has been run, STOP and route the user to `dw-transcript-router-crim` first; this skill does not transcribe.
