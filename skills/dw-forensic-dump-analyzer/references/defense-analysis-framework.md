# Defense Analysis Framework — Data Category Deep Dive

This reference provides the detailed analytical checklist for each data category, organized by the eight defense lenses. The SKILL.md provides the high-level framework; this document tells you exactly what to look for and how to look for it.

---

## TABLE OF CONTENTS
0. [Data Provenance: Local vs. Cloud](#0-provenance)
1. [Communications (SMS/MMS/iMessage)](#1-communications)
2. [Chat Applications](#2-chat-applications)
3. [Call Logs & Voicemail](#3-call-logs)
4. [Contacts](#4-contacts)
5. [Location Data](#5-location-data)
6A. [Photos & Screenshots](#6a-photos)
6B. [Video Intelligence](#6b-video)
7. [Browser History & Search](#7-browser)
8. [Application Data](#8-app-data)
8A. [Financial App Data](#8a-financial)
8B. [Health & Fitness Data](#8b-health)
8C. [Personal Data Apps (Notes, Calendar, Email, Voice Memos)](#8c-personal)
9. [System Artifacts & Logs](#9-system)
9.1A. [Notification History](#91a-notifications)
9A. [Application Usage & Screen Time](#9a-appusage)
10. [Timeline Construction Methodology](#10-timeline)
11. [Deleted Data Interpretation & Defense Analysis](#11-deleted-data)

---

## 0. Data Provenance: Local vs. Cloud {#0-provenance}

### Understanding Data Source Classification

Mobile device forensic extractions typically contain two distinct classes of data, each with different chain-of-custody implications:

- **LOCAL:** Data stored in on-device flash memory. Extracted directly from the physical device via Cellebrite, GrayKey, or similar tools. Chain of custody: examiner → device → Cellebrite backend.
- **CLOUD:** Data pulled from cloud services (iCloud, Google Account, Samsung Cloud, OneDrive, Dropbox, third-party backups) during extraction. Chain of custody: Cellebrite → cloud API/authentication → data.

The provenance distinction is critical under La. C.E. Art. 901(B)(9) because cloud and local data require different authentication foundations. The State often conflates them without disclosure.

### Identifying Cloud-Sourced Data in Extractions

#### File Path Indicators

Look for these patterns in Cellebrite exports, file listings, or Cellebrite HTML reports:

- File paths containing `/cloud`, `/backup`, `/sync`, `/icloud`, `/google`, `/samsung`
- Database names: `com.apple.cloudkit.*`, `com.google.*`, `com.samsung.android.cloud`
- Cellebrite sections labeled "Cloud Accounts," "Synced Data," "Backup," "Google Account," "iCloud"
- CSV column headers referencing "cloud," "backup," "synced," or cloud service names
- Cellebrite UFDR reports with separate "Cloud" tabs or sections distinct from device data

#### Common Cloud Data Sources

| Source | Service(s) | Typical Content | Extraction Method |
|--------|-----------|-----------------|-------------------|
| **iCloud Messages** | Apple | SMS/iMessage synced across devices | Cloud API (requires authentication) |
| **iCloud Photos** | Apple | Photos/videos synced; may include deleted items | Cloud API |
| **Google Location History** | Google | GPS timeline; NOT stored on device | Google account auth required |
| **Google Photos** | Google | Synced photos; may differ from device DCIM | Google account auth |
| **WhatsApp Backup** | Google Drive / iCloud | Encrypted backup; not local DB | Cloud API + decryption |
| **Samsung Cloud** | Samsung | Contacts, messages, photos, health data | Cloud API |
| **OneDrive / Dropbox** | Microsoft / Dropbox | Synced files/docs | Cloud API |
| **Google Drive** | Google | Synced files/docs | Cloud API |
| **Messenger Backup** | Facebook | Messenger threads | Cloud API or local if extracted directly |

### Authentication Chain Implications

#### Local Data Authentication

```
LOCAL DATA CHAIN OF CUSTODY
────────────────────────────────────────────
1. Device obtained and secured (initial custody)
2. Device connected to extraction tool (Cellebrite, GrayKey, etc.)
3. Extraction performed (logical, file-system, or physical)
4. Data hash verified against extraction artifact
5. Extracted files imported into analysis software
Result: Single examiner fingerprint; device-specific; defensible chain
────────────────────────────────────────────
```

**Defense implication:** Local data has a straightforward chain. Challenge any breaks: Was the device sealed? Was extraction in a controlled environment? Was the hash verified by an independent analyst?

#### Cloud Data Authentication

```
CLOUD DATA CHAIN OF CUSTODY
────────────────────────────────────────────
1. Device obtained; cloud credentials identified (or API key used)
2. Examiner authenticates to cloud service (Cellebrite, examiner account, API)
3. Cloud API queried; data returned to Cellebrite/examiner tool
4. Data merged into extraction output
Result: Cloud service provider (Google, Apple, Samsung) as intermediate custodian
        Cellebrite's cloud API accuracy not independently verified
        No device-specific hash verification
────────────────────────────────────────────
```

**Defense implication:** Cloud data requires demonstrating:
- **(1) Account ownership:** The cloud account belongs to the defendant, not someone with access to their phone
- **(2) Completeness of sync:** All relevant data was actually synced to the cloud (vs. stored locally only)
- **(3) Accuracy of extraction:** The extraction tool correctly queried and returned cloud data without modification, truncation, or corruption
- **(4) Cloud provider's logs:** If available, cloud provider logs should confirm what was synced and when

### Critical Defense Challenges for Cloud Data

#### Multi-Device Contamination

Cloud services allow data sharing across multiple devices on the same account. **iCloud data pulled during extraction may include:**
- Messages synced from the defendant's iPad or Mac
- Photos uploaded from a second iPhone owned by the same account holder
- Location history from a shared family account
- Contacts and calendar entries from multiple devices

**Defense issue:** If the charge rests partly on cloud data, the State must establish that the specific data came from THIS device, not another device on the same account. Example: "Defendant's iCloud photos from 3/15 include images taken from an iPad at a different location — can we confirm which device shot each photo?"

#### Deleted Data in Cloud

Cloud services often retain deleted items longer than devices do (or retain them indefinitely in backups/archives).

**Defense advantage:** iCloud Photos keep deleted photos for 30 days in a "Recently Deleted" folder. If the State found a photo in cloud backup that's not on the device, it may have been deleted from the device but retained in cloud storage. Timestamp of deletion matters for alibi.

**Defense disadvantage (if not carefully examined):** The State may cite cloud-stored photos as evidence the defendant possessed/created them, without clarifying whether the photo was actually on the phone at the time of the alleged offense.

#### Incomplete Cloud Sync Documentation

The State often fails to disclose:
- Whether cloud sync was enabled on the device
- When the last cloud sync occurred
- Whether all data was synced or only a subset (selective sync settings)
- Time lag between device activity and cloud sync (iCloud may sync with delays)

**Defense strategy:** Demand the cloud provider's logs showing sync timestamps, if available.

### Warrant & Consent Issues

#### Scope Limitation

If the warrant authorized extraction of "the physical device" but did NOT explicitly authorize extraction of cloud accounts:

- Local data: clearly within scope
- Cloud data: potentially outside scope — examiner may have exceeded warrant authority

**Suppression angle:** File a motion to suppress cloud-derived data as exceeding warrant scope.

#### Missing Separate Cloud Consent

Some examiners pull cloud data without obtaining separate consent or warrant for the cloud account itself:

- Local extraction consent: obtained
- Cloud account consent: not documented

**Suppression angle:** Cloud data pulled without separate authorization may be suppressible under Fourth Amendment.

#### Defendant vs. Account Holder

If the phone belonged to the defendant but a parent, spouse, or another person owns the cloud account, the defendant may not have consented to cloud extraction.

**Suppression angle:** If the defendant didn't authorize the cloud account, cloud data may be suppressible.

### Defense Analysis Workflow: Local vs. Cloud

**For each data category in the extraction:**

1. **Identify provenance:** LOCAL or CLOUD?
2. **Flag cloud sources:** Note in your findings any data pulled from cloud services
3. **Assess chain of custody:** Is the chain for cloud data weaker? Are there gaps in authentication?
4. **Check for multi-device contamination:** Could other devices on the same account have contributed this data?
5. **Demand cloud logs:** For critical cloud-derived findings, subpoena cloud provider records confirming sync/access
6. **Section 4 notation:** In the final report's Authentication Chain section, flag cloud-sourced data separately with authentication caveats

### Common Prosecution Misinterpretations

| Claim | Reality |
|-------|---------|
| "Cloud backup shows defendant had the photo" | Cloud may retain deleted photos longer than device; could have been deleted from device but kept in cloud |
| "iCloud Messages prove defendant sent the text" | iMessage requires account ownership AND device authentication; but iCloud syncs across devices — may have been sent from iPad, not the iPhone |
| "Google Location History shows defendant was at the scene" | Location History is NOT on the device; it's a Google service. Requires Google account auth, separate warrant, separate chain of custody |
| "Cloud data is automatically backed up; therefore it's definitely there" | Cloud sync depends on settings (disabled by default for some services); sync may fail; partial sync is possible |
| "Cellebrite pulled the data, so it's reliable" | Cellebrite's cloud API querying is proprietary; accuracy not independently audited; no device hash verification for cloud data |

### Checklist: Cloud Data Flag & Authentication

When cloud-derived data appears in the State's case:

- [ ] Identify which data sources are cloud vs. local
- [ ] Note the data source in your findings report
- [ ] Document the extraction tool's cloud authentication method
- [ ] Check Cellebrite report for cloud provider logs/API responses (if any)
- [ ] Assess whether the warrant covered cloud extraction
- [ ] Identify any multi-device contamination risks
- [ ] Demand cloud provider logs for critical findings (subpoena if necessary)
- [ ] Flag in Section 4 (Authentication Chain) any cloud data with weaker chain of custody
- [ ] Consider suppression motion if cloud data was extracted without warrant/consent for cloud account

---

## Timestamp Authority Hierarchy {#timestamp-hierarchy}

### The Problem

A single forensic artifact—a photograph, message, file, or call record—can contain 5+ timestamps from different sources. Cellebrite exports, HTML reports, and SQL databases each present timestamps that may differ significantly. The State cites whichever timestamp supports their narrative. The defense must know which timestamp is actually authoritative and why.

**Critical defense issue:** Incorrect timestamp interpretation can place the defendant at the crime scene when they were actually elsewhere, or can exclude critical evidence because a timestamp was misread.

### The Hierarchy: Authoritative Sources (Most → Least)

#### 1. EXIF DateTimeOriginal (Photos/Videos)

**Authority level: HIGHEST**

- Written by the camera hardware at the moment of capture
- Embedded in the image file itself (EXIF metadata)
- Hardest to forge without leaving digital traces (would require hex-editing the binary file)
- **This is THE timestamp for when a photo or video was created**

**Defense use:**
- If the State claims a photo was taken at time X, always extract the full EXIF data and verify DateTimeOriginal
- A forensic examiner may cite the filesystem "created" timestamp while EXIF shows a different time — the EXIF time is correct
- If EXIF is absent (stripped by messaging app, screenshotted, or downloaded from social media), note this in your report — it indicates origin issues

#### 2. EXIF DateTimeDigitized (Photos/Videos)

**Authority level: VERY HIGH**

- Records when the image was digitized (usually identical to DateTimeOriginal for modern phone cameras)
- If DateTimeDigitized ≠ DateTimeOriginal, investigate: the image may have been edited, scanned from a physical photo, or format-converted
- Can indicate post-capture processing

**Defense use:**
- If these two timestamps conflict, it's a red flag: something happened to the image between capture and digitization
- Document any discrepancy in your findings

#### 3. Cellebrite-Parsed Creation Timestamp (Database Records)

**Authority level: HIGH (for messages, calls, app data)**

- Extracted directly from the app's SQLite database (e.g., message "sent" timestamp from sms.db, call log timestamp from contacts.db)
- Reliable because it comes from the app's own authoritative record
- **But:** Subject to UTC offset error if the examiner misconfigured the system timezone or failed to account for DST transitions

**Defense use:**
- For messages and calls, Cellebrite's parsed timestamp (from the database) is more reliable than the filesystem timestamp
- Always verify whether the timestamp is UTC or local time — cross-reference Cellebrite's documentation or the original database query to confirm
- If a UTC offset error occurred, all timestamps shift by 1 hour or more (especially at DST transitions)
  - Example: If the examiner configured UTC-5 but the phone was actually in UTC-4 (during DST), all parsed timestamps are shifted by 1 hour

#### 4. Filesystem Created (Birth Time)

**Authority level: MODERATE**

- Recorded when the file was first written to the filesystem
- **iOS (APFS):** Preserves birth time accurately through most operations; reasonably reliable
- **Android (ext4):** Birth time support varies by device/Android version; less trustworthy
- **Problem:** Can be reset by file copy, backup/restore, app update, or cloud sync operations

**Defense use:**
- Filesystem created time is useful as a secondary check, but should not be the sole timestamp cited
- If a photo's EXIF and filesystem "created" timestamps differ by hours or days, investigate: the file may have been copied, restored from backup, or synced from the cloud
- For evidence with no EXIF (e.g., documents, downloads), filesystem created becomes more important

#### 5. Filesystem Modified (mtime)

**Authority level: LOW-MODERATE**

- Records the last time the file content was modified
- **Unreliable for evidence of user activity:** A photo "modified" yesterday may have been TAKEN months ago. The modification could be:
  - Cloud sync (automatic photo sync to iCloud or Google Photos)
  - Thumbnail regeneration (OS caching)
  - Backup/restore operation
  - File copy or transfer

**Defense use:**
- NEVER use mtime as evidence of when content was created or when a user accessed a file
- If the State cites an mtime to prove the defendant had/created content at time X, challenge it: mtime only shows when the file was last touched by ANY process, not user intent
- Always compare mtime against EXIF and filesystem created time; if they differ significantly, it indicates background OS activity

#### 6. Filesystem Accessed (atime)

**Authority level: UNRELIABLE**

- Recorded when the file was last read/accessed
- **Extremely unreliable on mobile:** iOS and Android background processes constantly access files for:
  - Indexing (Spotlight on iOS, Google Search on Android)
  - Thumbnail generation
  - Backup/restore cycles
  - Virus scanning
  - App cache rebuilding

**Defense use:**
- **NEVER use atime as evidence of user activity**
- atime is essentially useless for forensic analysis on mobile devices
- If the State attempts to cite atime as proof of defendant accessing content, challenge it immediately as scientifically unreliable

#### 7. Cloud Sync Timestamp

**Authority level: LOW**

- Records when a file was synced to/from iCloud, Google Photos, OneDrive, Dropbox, etc.
- Tells you WHEN THE SYNC HAPPENED, not when the content was created or first possessed
- **Critical distinction:** A photo synced today could have been taken a year ago; a document synced last week could have been created months earlier

**Defense use:**
- If the State cites a cloud sync timestamp as proof the defendant had content at time X, challenge it: the sync time is not the creation time
- Example defense argument: "The State shows this photo was synced to iCloud on March 15. But EXIF DateTimeOriginal shows it was taken on January 3. The sync timestamp proves only that iCloud received the file on March 15, not that the defendant had the photo on March 15."
- Sync timestamps CAN be useful for timeline purposes (showing when the defendant's cloud account had the file), but not as evidence of possession or creation

#### 8. Cellebrite "Last Modified" in Export

**Authority level: LOW**

- The timestamp shown in Cellebrite's HTML report or CSV export in a "Last Modified" or "Modified Date" column
- Usually represents the filesystem mtime (see above), not the creation time
- **Common examiner error:** Conflating "Last Modified" with "when the message was sent" or "when the photo was taken"
- This is especially problematic because Cellebrite's table view is often the first thing prosecutors and juries see

**Defense use:**
- If the State's expert cites Cellebrite's "Last Modified" column as proof of creation/possession timing, challenge them:
  - "Isn't the 'Last Modified' timestamp just the filesystem mtime?"
  - "Could this mtime be changed by a backup/restore or cloud sync operation?"
  - "What does the EXIF DateTimeOriginal show for this photo?"
- Always require the expert to dig deeper than Cellebrite's export table

### When Timestamps Conflict — Resolution Rules

#### EXIF vs. Filesystem Created

**Winner: EXIF DateTimeOriginal**

- EXIF is written by the camera hardware at capture; filesystem created can be reset
- If they differ by hours or days, the filesystem time was likely reset by restore/copy/sync
- Always cite EXIF DateTimeOriginal as the authoritative capture time

#### Cellebrite Parsed Timestamp vs. Filesystem

**For messages/calls:** Cellebrite parsed wins (comes from the app's database)
**For media files:** EXIF wins (if available); otherwise filesystem created

#### Multiple EXIF Timestamps Disagree

**Investigate immediately:**
- DateTimeOriginal ≠ DateTimeDigitized: The photo was likely edited or format-converted after capture
- Document both timestamps and note the discrepancy in your findings
- Verify whether the image properties show editing history

#### No EXIF Metadata at All

**Interpretation:**
- The photo was likely received via messaging app (which strips EXIF), screenshotted, or downloaded from social media
- This is crucial context: EXIF stripping indicates the photo originated externally and was then imported to the device
- Note this in your findings — it significantly affects conclusions about when/how the defendant acquired the image

#### UTC vs. Local Time Mismatch

**Common error: Examiner misconfigured the timezone**

Cellebrite and mobile forensics require the examiner to set the device's timezone during extraction. If the examiner used the wrong timezone (or failed to account for DST), ALL parsed timestamps are shifted.

**How to detect:**
- Check the extraction report for the timezone setting used
- Cross-reference against the device's actual timezone (can be verified from settings, carrier info, or app data)
- Look for known events to verify: if a text references a TV show that aired at 8 PM but the timestamp shows 9 PM, the offset may be wrong
- **DST transition error:** If extraction occurred near a DST boundary (spring forward/fall back), verify the offset is correct for the date in question

**Defense use:**
- If you detect a timezone offset error, ALL timestamps in the extraction are suspect
- File a supplemental report flagging the error
- Demand re-extraction or re-analysis with the correct timezone
- Use this to argue systemic unreliability: "If the examiner got the timezone wrong, how can we trust any timestamp in this extraction?"

### Conflicting Timestamps Checklist

**When you find timestamps that don't align:**

- [ ] Identify all timestamps present (EXIF original, EXIF digitized, filesystem created, filesystem modified, database parsed, cloud sync)
- [ ] Determine which source is most authoritative for this artifact type
- [ ] Check whether the discrepancy is explainable (e.g., EXIF original = capture time; filesystem modified ≠ capture time due to cloud sync)
- [ ] Verify the examiner's timezone configuration — is it correct for the device and date in question?
- [ ] If timestamps differ by > 1 hour, investigate: backup/restore, cloud sync, editing, or timezone error
- [ ] Document your findings: which timestamp you accept as authoritative and why

### Programmatic Check — Timestamp Audit

Use this Python pattern to flag timestamp conflicts in forensic analysis:

```python
from datetime import datetime, timedelta

def timestamp_audit(artifact_metadata):
    """
    Flag timestamp conflicts for a single artifact (photo, message, file, etc.).
    Returns a list of conflicts and recommendations.

    artifact_metadata: dict with keys like:
        - 'exif_original': str or datetime (when photo was taken)
        - 'exif_digitized': str or datetime (when digitized)
        - 'fs_created': str or datetime (filesystem birth time)
        - 'fs_modified': str or datetime (filesystem mtime)
        - 'fs_accessed': str or datetime (filesystem atime)
        - 'cloud_sync_time': str or datetime (when synced to cloud)
        - 'db_parsed_timestamp': str or datetime (from app database)

    Returns: dict with 'conflicts' list and 'authoritative_timestamp' recommendation
    """

    conflicts = []
    timestamps = {}

    # Parse and normalize all timestamps to datetime objects
    for key, value in artifact_metadata.items():
        if value:
            try:
                if isinstance(value, str):
                    ts = datetime.fromisoformat(value.replace('Z', '+00:00'))
                else:
                    ts = value
                timestamps[key] = ts
            except (ValueError, AttributeError):
                pass

    if not timestamps:
        return {'conflicts': [], 'authoritative_timestamp': None, 'reason': 'No timestamps found'}

    # Check for conflicts > 1 hour between key pairs
    conflict_pairs = [
        ('exif_original', 'fs_created'),
        ('exif_original', 'db_parsed_timestamp'),
        ('db_parsed_timestamp', 'fs_modified'),
        ('exif_original', 'cloud_sync_time'),
    ]

    for ts1_key, ts2_key in conflict_pairs:
        if ts1_key in timestamps and ts2_key in timestamps:
            diff = abs((timestamps[ts1_key] - timestamps[ts2_key]).total_seconds() / 3600)
            if diff > 1:  # > 1 hour difference
                conflicts.append({
                    'pair': (ts1_key, ts2_key),
                    'diff_hours': round(diff, 2),
                    'note': 'Investigate: file may have been copied, restored, or synced'
                })

    # Determine authoritative timestamp based on artifact type
    authoritative = None
    reason = ''

    if 'exif_original' in timestamps:
        authoritative = timestamps['exif_original']
        reason = 'EXIF DateTimeOriginal (written by camera hardware at capture)'
    elif 'db_parsed_timestamp' in timestamps:
        authoritative = timestamps['db_parsed_timestamp']
        reason = 'Database-parsed timestamp (from app record; verify UTC offset)'
    elif 'fs_created' in timestamps:
        authoritative = timestamps['fs_created']
        reason = 'Filesystem created (birth time; can be reset by restore/copy)'
    else:
        authoritative = max(timestamps.values())
        reason = 'Filesystem modified (least reliable; may indicate OS background activity)'

    return {
        'conflicts': conflicts,
        'authoritative_timestamp': authoritative,
        'reason': reason,
        'all_timestamps': {k: v.isoformat() for k, v in timestamps.items()}
    }

# Example usage:
artifact = {
    'exif_original': '2025-01-15T14:32:00-06:00',
    'fs_created': '2025-03-10T09:18:00-05:00',
    'fs_modified': '2025-03-10T09:18:15-05:00',
    'cloud_sync_time': '2025-03-10T14:45:00Z',
}

result = timestamp_audit(artifact)
if result['conflicts']:
    print("⚠ Timestamp conflicts detected:")
    for conflict in result['conflicts']:
        print(f"  {conflict['pair']}: {conflict['diff_hours']} hours apart")
    print(f"\nAuthoritative: {result['authoritative_timestamp']}")
    print(f"Reason: {result['reason']}")
```

### Defense Applications

**Scenario 1: State Claims Photo Was Taken at Time X (During Crime Window)**

1. Extract full EXIF metadata (use `exiftool`, `identify`, or mobile forensics tool)
2. Compare EXIF DateTimeOriginal against the timestamp cited by the State
3. If different:
   - Challenge the State's timestamp in cross-examination
   - Argue the EXIF is authoritative
   - If EXIF shows the photo was taken OUTSIDE the crime window, it's powerful alibi evidence
4. If EXIF is absent:
   - Note that EXIF stripping indicates external origin (received via messaging, social media, or screenshot)
   - Reduces reliability of the State's timeline

**Scenario 2: State Claims Message Was Sent at Time X (During Crime Window)**

1. Identify how the timestamp was derived: database parsed, filesystem, or export table?
2. Verify the examiner's timezone configuration — is it correct?
3. Cross-reference against known events:
   - If the message says "watching the news" and a timestamp shows 9 PM but the news aired at 8 PM, the offset may be wrong
   - If the recipient's phone shows the message arriving at 8:00 PM (their timezone), but the defendant's device shows 9:00 PM (due to timezone difference or offset error), flag this
4. If timestamps don't align, demand clarification in the State's response or expert deposition

**Scenario 3: State Claims File Was Created/Possessed at Time X (Filesystem "Created" Timestamp)**

1. Check whether the file has EXIF metadata (photos/videos)
   - If yes, EXIF DateTimeOriginal is authoritative; if different from filesystem, the file was copied/restored
2. Look for evidence of backup/restore:
   - Do multiple files in the extraction have the SAME "created" timestamp? (Indicates bulk restore event)
   - Check the device backup logs or iCloud activity
3. Look for cloud sync evidence:
   - Check cloud sync timestamps; if file sync time ≈ filesystem created time, the file was likely restored from cloud
4. In your report: "The State cites the filesystem 'created' timestamp of [X]. However, this timestamp is unreliable because: [file was copied/restored/synced from backup], and the actual creation time is [EXIF DateTimeOriginal or other authoritative source]."

**Scenario 4: Timestamps Cluster Suspiciously (50 Files with Identical Created Timestamps)**

This is a red flag for bulk operations, not individual user actions.

- Identical timestamps indicate a restore/backup event, not separate file creations
- Document this: "All 50 files have the identical filesystem 'created' timestamp of [X], suggesting a bulk restore operation on [date Y], not creation of individual files at that time."
- This is powerful for the defense: it undermines the State's narrative that the defendant created/collected these files over time

---


## 1. Communications (SMS/MMS/iMessage) {#1-communications}

### What to Extract
- Full message text with sender/recipient phone numbers
- Timestamps (sent, delivered, read — distinguish between them)
- Message direction (incoming vs. outgoing)
- Delivery status (sent, delivered, read, failed)
- Group message participants
- MMS attachments (photos, videos, audio, contacts shared)
- Deleted messages recovered from SQLite WAL files or unallocated space

### Defense Analysis Checklist

**Alibi & Timeline:**
- [ ] Map all message activity during the critical time window — active texting from a location inconsistent with the crime scene is powerful alibi evidence
- [ ] Look for messages that reference plans, location, or activities during the relevant period ("I'm at home," "just left work," "on my way to [alibi location]")
- [ ] Check for automated messages (delivery confirmations, appointment reminders) that timestamp the client's activity
- [ ] Note message gaps — a normally active texter going silent could support the State's narrative OR could indicate sleep, work, driving, or phone being off/dead

**Third-Party Suspects:**
- [ ] Identify unknown numbers that appear during the critical window
- [ ] Look for threatening or concerning messages from anyone other than the client
- [ ] Check for messages discussing conflicts, debts, or disputes involving third parties
- [ ] Search for messages where the client discusses threats from others

**State's Narrative Contradictions:**
- [ ] Compare message content and timing against witness statements — do witnesses claim communications that don't appear in the records?
- [ ] Check whether the State cherry-picked messages out of a longer thread — read the FULL conversation for context
- [ ] Identify messages the State omitted from their summary that change the meaning of included messages
- [ ] Verify whether the State correctly attributed message direction (incoming vs. outgoing)

**Client State of Mind:**
- [ ] Read the tone and content of messages in the hours/days before the incident
- [ ] Look for expressions of normal daily life (making plans, discussing routine matters) inconsistent with criminal planning
- [ ] Identify any messages showing emotional distress, intoxication, confusion, or coercion
- [ ] Check for messages showing the client's intentions ("going to bed," "heading to work tomorrow")

**Victim Credibility:**
- [ ] Map the COMPLETE communication history between client and victim — not just the State's selected excerpts
- [ ] Look for victim-initiated contact (calls, messages) that contradicts claims of fear
- [ ] Check for affectionate, neutral, or reconciliatory messages between them
- [ ] Identify inconsistencies between what the victim told police and what the message records show
- [ ] Look for messages where the victim makes admissions or contradicts their own statements

**Self-Defense Indicators:**
- [ ] Search for messages where the client reports threats, aggression, or fear of the victim or others
- [ ] Look for messages to friends/family seeking help or expressing fear before the incident
- [ ] Check for messages documenting prior violent incidents
- [ ] Identify messages showing the client attempting to de-escalate

**Gaps & Missing Data:**
- [ ] Identify conversations with missing messages (replies without originating messages, or vice versa)
- [ ] Check for unusual time gaps in otherwise continuous conversations
- [ ] Note if the extraction captured SMS but missed iMessage (or vice versa) — common extraction limitation
- [ ] Flag conversations that appear truncated or start mid-thread

### Programmatic Analysis (When CSV/Excel Data Available)

```python
# Key analyses to run on structured message data:

# 1. Activity timeline during critical window
# Filter messages to crime date ± 24 hours, sort chronologically

# 2. Communication frequency analysis
# Messages per hour/day with the victim, key contacts, unknown numbers

# 3. Keyword search
# Search for case-relevant terms: location names, weapon terms,
# victim name, co-defendant names, alibi-relevant phrases

# 4. Contact pattern analysis
# Who did the client communicate with most frequently?
# Any new contacts appearing near the incident date?

# 5. Response time analysis
# Average response time to victim vs. others — sudden changes
# in pattern may indicate relationship dynamics

# 6. Gap detection
# Identify periods with zero activity on a normally active device
```

---

## 2. Chat Applications {#2-chat-applications}

### Platform-Specific Considerations

**WhatsApp:**
- End-to-end encrypted — extraction quality depends heavily on method
- Check for: message timestamps, read receipts (blue checks), last seen status, group memberships
- Media files may be stored separately from message databases
- Deleted messages may show as "This message was deleted" placeholders

**Facebook Messenger:**
- Check for: message reactions, read receipts, active status timestamps
- Messenger Rooms/calls may have separate logging
- Secret Conversations use separate encryption — may not be extracted

**Signal:**
- Disappearing messages feature — absence of messages may be a feature, not deletion
- Minimal metadata by design — less to extract but also less for prosecution
- If Signal data IS present in extraction, note how it was obtained (implications for methodology audit)

**Snapchat:**
- Messages designed to disappear — extraction may capture only fragments
- Check for: saved messages (Memories), chat logs, friend lists, Snap Map location data
- Media attachments may be recoverable even after "disappearing"

**Instagram DMs:**
- Check for: message threads, story replies, voice messages, shared posts
- "Vanish mode" messages may not be captured
- Account activity log may show login locations and times

**Telegram:**
- Secret chats are device-specific and encrypted — check if captured
- Regular chats are cloud-based — may require server-side records
- Self-destruct timer on messages — similar to Signal disappearing messages

### Defense Analysis (All Chat Apps)

Apply the same eight-lens analysis as SMS/MMS, plus:

- [ ] **Platform authentication:** Verify that the account shown in the extraction actually belongs to the client — check account creation date, phone number linkage, email verification
- [ ] **Multi-device access:** Many chat apps allow multiple devices — messages may have been sent from a different device (computer, tablet) than the phone
- [ ] **Disappearing messages context:** If the client used disappearing messages, this is a platform FEATURE, not evidence of concealment. Note the client's settings and whether this was their default across all conversations (habit, not targeted deletion)
- [ ] **Group context:** Messages in group chats must be read in the context of the full group conversation — a response to someone else's message may appear incriminating out of context
- [ ] **Forwarded messages:** Check whether messages were forwarded vs. composed — a forwarded threatening message is very different from an authored one

### Programmatic Analysis (Chat App Data)

```python
# Key analyses for chat app data:

# 1. Cross-platform message matching
# Compare message content/timing across apps — same conversation
# on SMS and WhatsApp reveals backup communications

# 2. Disappearing message audit
# Check app config databases for auto-delete settings
# If enabled globally (not just victim thread), it's habit, not concealment

# 3. Account ownership verification
# Extract account identifiers (phone number, email, username)
# Compare against known client info to confirm attribution

# 4. Group chat context extraction
# For messages the State cites from group chats, extract the full
# surrounding conversation (10 messages before and after minimum)
# to establish what the client was actually responding to

# 5. Media attachment inventory
# Catalog all media files sent/received with timestamps
# Cross-reference against photo gallery to distinguish
# captured vs. received content
```

---

## 3. Call Logs & Voicemail {#3-call-logs}

### What to Extract
- All calls: incoming, outgoing, missed, rejected
- Phone numbers with contact name associations
- Call duration (0-second calls = didn't connect or went to voicemail)
- Timestamps (start time, and end time if available)
- Call type (cellular, VoIP, FaceTime, WhatsApp call, etc.)
- Voicemail recordings and transcriptions if available

### Defense Analysis Checklist

**Alibi & Timeline:**
- [ ] Map all calls during the critical window — active phone calls establish the client was conscious, responsive, and potentially at a specific location (via cell tower data during the call)
- [ ] Check call durations — a 45-minute call during the alleged crime window is strong alibi evidence
- [ ] Look for calls to/from businesses (pizza delivery, ride-share, employer) that can be independently verified
- [ ] FaceTime/video calls are especially valuable — they confirm the client was looking at their phone

**Third-Party Suspects:**
- [ ] Identify unfamiliar numbers calling the victim (on victim's phone) or the client
- [ ] Check for burner phone patterns — short calls to the same number at unusual hours
- [ ] Look for calls between potential co-conspirators that don't involve the client

**Frequency Analysis:**
- [ ] Build a call frequency chart: who does the client call most? How does this compare to the State's narrative about relationships?
- [ ] Identify changes in call patterns around the incident date — sudden increase or decrease in contact with specific people
- [ ] Check for calls to attorneys, crisis hotlines, domestic violence hotlines, or mental health services

**Gaps & Anomalies:**
- [ ] Zero-duration calls may indicate calls rejected by the recipient or network issues — not necessarily "hang-ups"
- [ ] Missing calls (calls visible on carrier records but not on device) may indicate selective deletion or extraction failure
- [ ] Multiple rapid calls to the same number may indicate urgency, fear, or attempts to reach someone for help

### Voicemail Content Analysis

Voicemail recordings and transcriptions are frequently overlooked but can contain critical defense evidence:

- [ ] **Saved voicemails from victim:** May contain admissions, threats, tone-of-voice indicating aggression or intoxication, or statements inconsistent with what the victim told police
- [ ] **Saved voicemails from witnesses:** Prior inconsistent statements recorded in the witness's own voice — powerful impeachment material
- [ ] **Voicemail timestamps:** When a voicemail was left vs. when it was listened to — establishes whether the client heard certain information before or after the incident
- [ ] **Voicemail transcriptions:** If the device auto-transcribed voicemails, extract and compare against any police summary — transcription errors may have led to misinterpretation
- [ ] **Deleted voicemails:** If recoverable, check whether deletion was selective (only crime-relevant) or routine (clearing storage)
- [ ] **Voicemails to the client during critical window:** If someone left the client a voicemail during the alleged crime time, the caller expected the client to be available — potentially inconsistent with the State's theory of what the client was doing

Flag all voicemail recordings for attorney review — tone of voice, emotional state, and background noise cannot be assessed from transcription alone.

### Programmatic Analysis (Call Log Data)

```python
# Key analyses for structured call log data:

# 1. Critical window call timeline
# Filter to crime date ± 24h, sort chronologically
# Include: number, direction, duration, type (cell/VoIP)

# 2. Frequency analysis with baseline comparison
# CRITICAL: Never present call frequency as "high" or "unusual"
# without computing the baseline first
import pandas as pd
df['date'] = pd.to_datetime(df['timestamp']).dt.date
daily_freq = df.groupby(['contact', 'date']).size().reset_index(name='calls')
baseline = daily_freq[daily_freq['date'] < critical_start].groupby('contact')['calls'].mean()
# Compare crime-window frequency against baseline per contact

# 3. Contact pattern analysis
# Identify: top contacts by volume, new contacts near incident,
# contacts with sudden frequency changes

# 4. Duration anomaly detection
# Flag calls with unusual duration (very short: missed/rejected;
# very long during critical window: alibi evidence)

# 5. VoIP vs. cellular split
# Some contacts may appear ONLY in VoIP logs (WhatsApp, FaceTime)
# and not in the cellular call log — ensure both are checked

# 6. Carrier record cross-check preparation
# Export device call log in format ready to compare against
# carrier CDRs when they arrive — flag any device-only or
# carrier-only calls for investigation
```

---

## 4. Contacts {#4-contacts}

### What to Extract
- Contact names, phone numbers, email addresses
- Contact creation dates and modification dates
- Contact groups or labels
- Contact photos
- Notes or custom fields
- Recently added vs. long-standing contacts
- Deleted contacts (if recoverable)

### Defense Analysis Checklist

- [ ] **Who IS in the contacts:** Presence of victim, co-defendants, witnesses as saved contacts establishes known relationships (not random encounters)
- [ ] **Who is NOT in the contacts:** If a phone number the State attributes to the client's associate is NOT saved as a contact, this may undermine claims of close association
- [ ] **Contact creation dates:** A recently added contact may show when a relationship began — relevant to timeline of alleged conspiracy or relationship duration
- [ ] **Nicknames and labels:** How the client saved contacts (affectionate nicknames for victim, labels like "work" or "family") can show relationship character
- [ ] **Duplicate numbers under different names:** May indicate the client didn't know two contacts were the same person

### Programmatic Analysis (Contacts Data)

```python
# 1. Contact creation timeline
# Sort contacts by creation date to see when relationships formed
# Flag contacts added in the weeks before the incident

# 2. Cross-reference contacts against key people
# Match phone numbers from call/message logs against contact names
# Identify frequently contacted numbers NOT saved as contacts (burners, new contacts)

# 3. Contact group analysis
# If contacts are labeled/grouped, extract group membership
# to map the client's social network structure

# 4. Deleted contact recovery
# If SQLite contacts database is available, query for
# deleted records in WAL or freelist pages
```

---

## 4.1: SIM Card Data {#4-1-sim}

### What SIM Data Contains

SIM card data extracted from Cellebrite includes:

- **ICCID (Integrated Circuit Card Identifier)** — uniquely identifies the SIM card itself; changes when the SIM is replaced
- **IMSI (International Mobile Subscriber Identity)** — identifies the subscriber to the carrier; also changes with SIM replacement
- **MSISDN** — the phone number assigned to the SIM by the carrier
- **Stored contacts** — SIM can store a limited number of contacts (usually 250 max); these are independently maintained from phone contacts
- **Last dialed numbers (LDN)** — stored on SIM independently of the phone's call log; typically 10-20 entries, easily overwritten
- **SMS stored on SIM** — limited storage (usually 20-50 messages); common on older phones or specific carrier configurations
- **SIM application toolkit data** — carrier-specific services and menu options
- **Carrier/network information** — network access code (NAC), service provider data

### Where in Cellebrite

SIM data typically appears in these locations within a Cellebrite extraction:

- **Extraction summary section** — High-level SIM identifiers (ICCID, IMSI, phone number) often appear at the top of reports
- **Dedicated SIM section** — If present, labeled "SIM Card," "SIM Information," or "SIM Data"
- **Contacts tab** — Contacts sourced from the SIM are marked with source "SIM Card" or "SIM Storage" (distinct from "Phone Storage" or "Cloud" contacts)
- **Call logs section** — Last dialed numbers may appear separately under "SIM Last Dialed" or integrated into the main call log with source attribution

Some extractions may consolidate SIM data; others split it across multiple sections. Always check the extraction index or search for "SIM" or "ICCID" keywords.

### Defense Analysis Checklist

- [ ] **SIM ICCID/IMSI matches carrier records** — Obtain carrier records (via discovery or subpoena) and verify the ICCID and IMSI in the Cellebrite extraction match the carrier's records for the account in question. Mismatch indicates the wrong SIM was in the device or the SIM was replaced between extraction and carrier records.
- [ ] **SIM-stored contacts vs. phone contacts** — Compare contacts present on SIM to contacts in the phone's main contact list. SIM contacts are older and rarely updated. Absence from the phone but presence on SIM may indicate a long-standing relationship or an older contact the client de-prioritized.
- [ ] **Last dialed numbers (LDN) on SIM vs. phone call log** — Cross-reference the SIM's last dialed numbers against the phone's full call log. Discrepancies suggest the SIM was placed into a different device (LDN would have different entries than the current phone's call log).
- [ ] **SIM swap history** — Investigate whether the SIM was recently changed. Check dates: Did the ICCID change between the incident date and extraction date? Was a new SIM activated on the account? SIM changes may indicate the defendant obtained a replacement device or passed the phone to someone else.
- [ ] **Dual SIM detection** — Does the device have two SIM slots? Was a second SIM present during the critical time period? Dual-SIM phones can have two active numbers; only extracting one SIM misses half the device's communication potential.
- [ ] **eSIM vs. physical SIM** — Modern phones support eSIM (embedded, programmable). If the device has eSIM capability, did the extraction capture eSIM data separately? eSIM data extraction varies by method; physical SIM extraction is more reliable.
- [ ] **SIM lock status** — Was the SIM PIN-locked? PIN-protected SIMs require authentication to install in another device. SIM lock status can indicate whether the SIM could have been easily transferred to another phone.

### Defense Value

- **Independent call record:** SIM-stored last dialed numbers provide a call log that exists independently of the phone's own call log. If the phone's call log has been truncated, cleared, or recovered from unallocated space with gaps, the SIM's LDN offers a second, uncorrupted source of evidence about who was called from that device.
- **Historical contacts:** SIM contacts may preserve relationships that were deleted from the phone's contact list. The presence of a contact on the SIM but not the phone may indicate a relationship the client wanted to de-emphasize but that existed during the period when the SIM was in use.
- **Device continuity verification:** SIM ICCID is a permanent hardware identifier on the physical card. If the ICCID in the Cellebrite extraction differs from what the carrier lists for that account, this raises critical questions: Was the wrong SIM extracted? Was the SIM swapped between devices? Was the extraction performed on a device the defendant doesn't actually own?
- **Device continuity challenge:** If the SIM last dialed numbers differ significantly from the current phone's call log, this suggests the SIM spent time in a different device — directly challenging the assumption that all data on the extracted phone was generated by the defendant while the SIM was present.

### Prosecution Misinterpretation Watch

- [ ] **SIM contact absence ≠ unknown relationship:** Absence of a contact on the SIM does NOT mean the person wasn't in the defendant's known contacts. Modern phones store thousands of contacts in phone/cloud storage; the SIM stores at most 250. Absence on the SIM is expected for the vast majority of contacts and proves nothing.
- [ ] **SIM LDN limitations:** SIM last dialed numbers have very limited storage (typically 10-20 entries, easily overwritten by new calls). The State cannot argue that absence of a number from the SIM's LDN proves the number was never called — the limited storage and overwrite behavior make SIM LDN unreliable as a comprehensive call history.
- [ ] **SIM storage is manual and obsolete:** SIM contacts must be manually stored on the SIM by the user. They represent an older snapshot of the client's contacts. Do not assume SIM contact presence/absence reflects the client's current relationships or associations.

---

## 5. Location Data {#5-location-data}

**IMPORTANT: This skill performs initial extraction and organization of location data only. All deep analysis — tower coverage, RF propagation, directional antenna challenges, Carpenter issues — is handled by dw-cell-site-geolocation-auditor.**

### What to Extract and Organize for Handoff
- Cell tower connection records (Cell ID, LAC, MCC, MNC, timestamps)
- GPS coordinates (from photos, maps app, location services)
- Wi-Fi connection history (SSID names, timestamps, MAC addresses)
- Google Location History / Apple Significant Locations
- App-based location data (Uber/Lyft pickup/dropoff, check-ins, weather app locations)
- Bluetooth device connections (proximity to known devices)

### Initial Defense Screening (Before Handoff)

- [ ] **Crime window coverage:** Is there ANY location data during the alleged crime window? If yes, extract and organize for handoff. If no, note the gap.
- [ ] **Pattern of life:** Compile location data for the 2-4 weeks before the incident to establish the client's routine — where they normally go, when, and how often
- [ ] **Alibi location data:** Any location pings at an alibi location during the critical window — flag as HIGH PRIORITY for geolocation auditor
- [ ] **Travel feasibility:** If the State claims the client traveled from Point A to Point B, calculate whether the phone data timestamps make this physically possible
- [ ] **Wi-Fi connections:** Named Wi-Fi networks (home, work, businesses) provide more precise location evidence than cell towers — "connected to Starbucks_WiFi at 9:14 PM" is specific
- [ ] **App-based location:** Uber/Lyft records, food delivery confirmations, fitness app routes — these often have precise GPS and are independently verifiable

### Organize for Handoff
Create a chronological location data table:

```
TIMESTAMP          | SOURCE           | LOCATION DATA              | DEFENSE NOTE
────────────────────────────────────────────────────────────────────────────────
2024-03-15 20:00   | Cell Tower       | CID: 12345, LAC: 678      | Pre-incident
2024-03-15 20:15   | Wi-Fi Connect    | "HomeNetwork_5G"           | Client at home
2024-03-15 20:45   | GPS (photo EXIF) | 30.4515° N, 91.1871° W    | Client at home
2024-03-15 21:30   | Cell Tower       | CID: 12346, LAC: 678      | Crime window
...
```

### Programmatic Analysis (Location Data)

```python
# 1. Chronological location timeline
# Merge all location sources (cell, GPS, Wi-Fi, app) into
# one unified timeline sorted by timestamp

# 2. Wi-Fi network name matching
# Extract all SSIDs connected to and match against known
# locations (home, work, businesses, alibi locations)

# 3. GPS clustering
from scipy.cluster.hierarchy import fclusterdata
# Cluster GPS points to identify frequently visited locations
# Compare clusters against known key locations

# 4. Travel feasibility calculator
from geopy.distance import geodesic
# Given two location pings, calculate minimum travel time
# Compare against time between pings to assess feasibility
# of State's claimed movements

# 5. Location gap detection
# Identify periods with no location data on a device that
# normally produces regular location pings
# Cross-reference against device power state and network status
```

---
### 5A. Wi-Fi Connection History

**CRITICAL ALIBI EVIDENCE:** Wi-Fi connection logs place the client at specific locations with high precision — far more reliable indoors than GPS. Unlike cell tower data (which can be miles off), Wi-Fi says "your phone was connected to this specific network." Unlike GPS (unreliable indoors, can be spoofed), Wi-Fi requires physical proximity to the router.

#### What to Extract and Organize

Cellebrite extracts Wi-Fi connection history under **Device Information > Wireless Networks**. For each connection, extract:
- **SSID**: The network name (e.g., "SmithHome-5G", "Starbucks WiFi", "CompanyNetwork")
- **BSSID**: The MAC address (hardware identifier of the router — allows you to verify the exact location of that router)
- **Connection timestamps**: When the phone connected to and disconnected from the network
- **Password history**: If the phone saved the password (useful for distinguishing networks the client intentionally used vs. networks the phone auto-connected to)
- **Security type**: Whether the network was open, WEP, WPA, WPA2 (helps verify the network's authenticity — official networks use strong security)
- **Last known connection**: The most recent time the phone connected to this network

#### Wi-Fi as Location Evidence

A Wi-Fi connection is **location evidence** because the phone only connects when within 30–100 feet of the router (typical range). Named networks indicate probable location:

- **"SmithHome-5G"** + connection at 8:47 PM = client's phone was at home
- **"Starbucks_WiFi"** + connection at 9:30 PM = client was at that Starbucks (the specific location, if franchised)
- **"CompanyNet"** + connection during work hours = client at work location
- **Disconnection** = phone left that location (when combined with next connection, proves travel)

#### Defense Analysis Checklist

- [ ] **Connections during critical window:** Did the client's phone connect to a network during the alleged crime window? Each connection = location placement (subject to range limitations — see Limitations below)
- [ ] **Home Wi-Fi patterns:** Connection to home Wi-Fi at 9:15 PM + disconnection at 6:00 AM = proves the client was home overnight. This is a powerful alibi, especially when prosecution claims the client was elsewhere
- [ ] **Work Wi-Fi routine:** Does the client's phone regularly connect to work Wi-Fi during business hours? Establishes pattern of life corroborating employment
- [ ] **Commercial venue timestamps:** Starbucks, restaurants, hotels, airports — specific named networks place the client at real, verifiable locations with independent businesses that may have security cameras or receipts
- [ ] **Network gaps:** Periods with no Wi-Fi connection — may indicate driving (outside all Wi-Fi range) or outdoor activity
- [ ] **Cross-reference with cell tower & GPS:** If Wi-Fi, GPS, and cell tower all show the client at the same location at the same time, the corroboration is extremely strong
- [ ] **Prosecution misinterpretation:** Ensure the prosecution isn't claiming that a Wi-Fi connection proves the client was using the phone personally. A phone can be connected to home Wi-Fi while sitting on a table (not being used) — this proves the phone was at home, not that the client was actively using it

#### Limitations to Highlight in Defense

- **Wi-Fi range:** Standard routers reach 30–100 feet. A connection to "HomeNetwork" proves the phone was within range of the home router, but the client could have been in the driveway, on the porch, or in a neighbor's house near the router
- **Phone left behind:** The most damaging limitation: the phone could be connected to home Wi-Fi while the client is elsewhere. The prosecution will argue this. Counter by: (a) showing the defendant's phone was with them via other data (calls, text messages sent, app activity, other location markers); (b) showing the client was at that location via witness testimony or receipts; (c) combining Wi-Fi with call logs (a call placed during the Wi-Fi connection is harder to explain away — the client was likely there)
- **Auto-connect:** Modern phones auto-connect to previously used Wi-Fi networks when in range. A connection doesn't necessarily mean the client intentionally used that network — though repeated reconnections suggest the client frequents that location
- **Shared networks:** Public Wi-Fi networks (airport, mall, Starbucks) don't uniquely identify a location as strongly as home or work networks. If multiple Starbucks use the same SSID, the data shows the network but not which Starbucks. (BSSID solves this — each router has a unique MAC address — but Cellebrite may not extract BSSID clearly)
- **Time precision:** Connection timestamps are typically accurate to the minute, making them useful for timeline corroboration

#### Prosecution Misinterpretation to Watch For

**Prosecution argument:** "The defendant's phone was connected to home Wi-Fi at 11 PM, proving he was at home while the crime occurred at his ex-partner's house."

**Defense counter:**
1. "The phone was at home, but we have [witness testimony / receipts / other evidence] that the client was at [alibi location]. The phone was left on the nightstand."
2. "The Wi-Fi connection alone proves location of the phone, not the location of the user. Absent additional evidence that the client was personally using the phone (active calls, message sending, etc.), the prosecution can't prove the user was with the device."
3. "The connection was auto-connect — the phone connects to home Wi-Fi whenever in range, which could include the driveway, neighbor's house, or the street in front of the home. This doesn't narrow the location."

#### Alibi Construction Example

```
SCENARIO: Client charged with assault at victim's home on 2024-03-15 at 11:00 PM.

EVIDENCE:
- Wi-Fi connection: Client's phone connected to "SmithHome-5G" at 10:47 PM
- Wi-Fi connection: Client's phone disconnected from "SmithHome-5G" at 6:12 AM (next day)
- No intervening Wi-Fi connections
- Call log: Client received an incoming call at 10:52 PM while connected to home Wi-Fi (answered, 3-minute duration)
- Message data: Client received text messages at 11:15 PM and 11:47 PM while connected to home Wi-Fi
- Witness testimony: Client's roommate states the client was in the house all evening

DEFENSE NARRATIVE:
"The evidence shows that my client's phone connected to his home Wi-Fi network, SmithHome-5G, at 10:47 PM on March 15th and remained connected until 6:12 AM the following morning. During this 8-hour period, he received an incoming phone call and multiple text messages, and he answered the call. This places the client at home during the entire alleged window of the assault. Unlike GPS or cell tower data, which can be imprecise, Wi-Fi connection logs show the device within physical proximity to the home router. The continuous connection throughout the night, combined with the client's incoming communications and witness testimony, establishes a clear alibi."
```

---

## 6A. Photos & Screenshots {#6a-photos}

### What to Extract
- Photo files with full EXIF metadata (GPS, timestamp, camera model, orientation)
- Screenshots (timestamps, what was captured)
- Downloaded images and their source URLs
- Media creation date vs. file modification date
- Deleted photos recovered from unallocated space
- Cloud-synced photos (iCloud Photos, Google Photos indicators)
- Live Photo still frames (the video component goes in Section 6B)

### Defense Analysis Checklist

**EXIF Metadata Mining:**
- [ ] GPS coordinates in photos taken during the critical window — precision alibi evidence
- [ ] Camera direction/orientation data — may establish what the client was looking at
- [ ] Timestamps — photo taken at the alibi location during the crime window is powerful
- [ ] Serial/burst photos — rapid sequence indicates real-time capture, not staged

**Content Analysis:**
- [ ] Photos showing the client at an alibi location (selfies, group photos with timestamps)
- [ ] Photos showing the client's physical condition (no injuries before alleged assault, injuries consistent with self-defense)
- [ ] Screenshots of threatening messages received from others
- [ ] Photos documenting prior incidents (damage, injuries, threatening notes)
- [ ] Photos the State will use — assess what they actually show vs. what the State will claim

**Photo Integrity:**
- [ ] Check whether photo was received (downloaded) vs. captured (taken by this device's camera) — EXIF camera model should match the device
- [ ] Cloud sync timestamps may differ from capture timestamps — don't confuse when a photo was synced with when it was taken
- [ ] Screenshots may capture content the client didn't create — a screenshot of a threatening text IS the threatening text, but it was received, not authored
- [ ] Cached images from browsing are NOT photos the client sought out — they may be ads, tracking pixels, or thumbnails from link previews

### Programmatic Analysis (Photo Data)

```python
# 1. EXIF metadata extraction
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
# For each photo: extract GPS coords, timestamp, camera model,
# orientation, and software version
# Flag photos where camera model does NOT match the device
# (indicates received, not captured)

# 2. GPS-stamped photo timeline
# Extract all photos with GPS coordinates during critical window
# Plot on timeline alongside other location data

# 3. Screenshot detection
# Screenshots have specific EXIF signatures (no camera model,
# device screen resolution, specific software tags)
# Catalog what was screenshotted and when — may contain evidence
# of threatening messages, social media posts, or research

# 4. Photo origin classification
# Classify each photo: captured (camera), received (message),
# downloaded (browser/app), synced (cloud), screenshot
# Based on: EXIF data, file path, creation method metadata

# 5. Deleted photo recovery check
# If SQLite photo database available, check for deleted entries
# with intact metadata but removed file pointers
```

---

## 6B. Video Intelligence {#6b-video}

Videos on a phone are among the most powerful pieces of defense evidence — and among the most overlooked. Unlike a text message or call log entry, a video captures continuous, timestamped reality: where the phone was, what was happening around it, who was present, what was being said, and how long it lasted. A 3-minute selfie video recorded at a gas station during the crime window is stronger alibi evidence than a hundred text messages.

### What to Extract

- **All video files** from the extraction: camera recordings, screen recordings, received videos, chat media, social media saves, Live Photo video components, voice/video memos
- **Video metadata**: creation timestamp, duration, GPS coordinates, camera model, resolution, frame rate, codec, audio track presence
- **File system context**: file path (reveals source — DCIM/Camera vs. Downloads vs. WhatsApp Media), creation date vs. modification date, file size
- **Deleted videos** recovered from unallocated space or SQLite databases
- **Cloud-synced video indicators** (iCloud, Google Photos upload timestamps)
- **Thumbnail/preview images** — even if the original video was deleted, the system may retain a thumbnail

### Step 1: Run Video Inventory

Use `scripts/preprocessing.py` → `inventory_video_files()` to catalog every video in the extraction. This produces a classified inventory before you open a single file.

### Step 2: Extract Metadata for Each Video

Use `scripts/preprocessing.py` → `extract_video_metadata()` for each video file. Key fields:

| Metadata Field | Defense Significance |
|---------------|---------------------|
| **Duration** | A 15-minute continuous recording proves the phone owner was at that location for 15 minutes. The State can't claim "he was at the crime scene" if he was recording a video somewhere else for the entire window. |
| **GPS coordinates** | Precision alibi — more accurate than cell tower data. GPS in video metadata comes from the device's GPS chip at the moment of recording. |
| **Creation timestamp** | When the recording started. Cross-reference against the critical window. |
| **Resolution & frame rate** | Distinguishes device-recorded video (matches device specs) from received/downloaded video (different specs). |
| **Audio track** | Whether the video captured ambient sound. Audio can contain voices, conversations, background noise that establishes environment. Flag for attorney review — audio content can't be fully assessed programmatically. |
| **Camera model** | Like photos, camera model in metadata should match the device. Mismatch means the video was received, not recorded on this phone. |

### Step 3: Build Video Timeline

Use `scripts/preprocessing.py` → `build_video_timeline()` to arrange all videos chronologically and flag those within the critical window.

### Defense Analysis Checklist — Videos

**Alibi & Timeline (highest priority for videos):**
- [ ] Any videos recorded during the critical window — timestamp + duration + GPS = powerful alibi trifecta
- [ ] Videos that show the client's surroundings (background details that identify location independently of GPS)
- [ ] Continuous recording duration — a 10-minute video means the phone wasn't being used for anything else during that time
- [ ] Screen recordings during the critical window — if the client was screen-recording a game or social media, they weren't committing a crime
- [ ] Live Photos (iOS) — the 1.5-3 second video clip embedded in each Live Photo captures a brief moment of reality with audio. These are timestamped and GPS-tagged just like regular photos

**Video Content Assessment:**
- [ ] **Flag all videos from the critical window for attorney review.** Describe what can be determined from metadata and filename, but the attorney needs to see the actual content.
- [ ] Videos showing the client's physical condition (no visible injuries before alleged assault, visible injuries consistent with self-defense)
- [ ] Videos capturing interactions between client and victim (tone, body language, context)
- [ ] Videos of the crime scene or relevant location at a different time (establishes baseline conditions)
- [ ] Selfie videos / video messages that show the client's demeanor and emotional state
- [ ] Videos sent to or received from the victim — full relationship context, not just the State's selected clips

**Audio Track Analysis:**
- [ ] Does the video have an audio track? (Check `has_audio` in metadata)
- [ ] If audio is present, flag for attorney: ambient voices, conversations, music, TV/radio (establishes environment), sounds of distress or calm
- [ ] Video calls (FaceTime recordings, WhatsApp video calls) — these prove two-party interaction at a specific time
- [ ] Voice/video memos — the client may have recorded thoughts, events, or evidence in real time

**Received vs. Recorded:**
- [ ] Classify each video: recorded on this device (DCIM/Camera path, matching camera model) vs. received (chat media folder, downloaded, different resolution/codec)
- [ ] Videos received from the victim or key witnesses may contain admissions, threats, or context the State ignores
- [ ] Social media videos saved from others' accounts — note they document what the client was viewing, not what they created

**Screen Recordings:**
- [ ] Screen recordings capture what was on the phone's display — they may show message conversations, app activity, or browsing that the extraction didn't capture elsewhere
- [ ] Timestamps on screen recordings establish the client was actively using their phone at that moment
- [ ] Screen recordings of threatening messages or social media posts are evidence the client preserved — this cuts against "consciousness of guilt" arguments about deleted messages

**Video Editing & Integrity:**
- [ ] Check for signs of video editing: does the codec match what the device natively records? (e.g., iPhone records H.265/HEVC; an H.264 re-encode suggests editing)
- [ ] File modification date significantly later than creation date may indicate post-capture editing
- [ ] Abnormally small file size for the resolution and duration may indicate re-encoding or compression
- [ ] Metadata stripping — if a video has no EXIF data at all, it may have been processed through an app or service that strips metadata (common for videos shared via social media)

**Gaps & Missing Videos:**
- [ ] Are there thumbnails or database entries for videos that no longer exist in the extraction?
- [ ] Does the Photos.sqlite (iOS) or media database (Android) reference video files that weren't extracted?
- [ ] Were videos selectively excluded from the production? Compare extraction manifest against what was produced — flag for Brady/Giglio if the State chose which videos to disclose
- [ ] Check for iCloud/Google Photos references to videos not present locally — may need cloud warrant return to obtain

### Prosecution Misinterpretation Watch — Video-Specific

**Video presence ≠ video creation:** A video in the Downloads folder or a chat media folder was received, not recorded. The State may present a received video as something the client "had" without clarifying the client didn't create it.

**Deleted video ≠ concealment:** Apply the same analysis as deleted messages — check whether the client routinely manages storage, whether auto-delete was enabled, whether the deletion was selective or part of a bulk cleanup.

**Video metadata timestamps:** Same timezone and DST caveats as all other timestamps. Additionally, some video apps (Snapchat, Instagram) strip or replace metadata — a video's file system date may not reflect when it was originally recorded.

**Duration misrepresentation:** The State may reference a video's existence without noting its duration. A 2-second accidental recording is very different from a 5-minute intentional capture. Always report duration alongside existence.

### Programmatic Analysis (Video Data)

```python
# Use the preprocessing.py video functions for structured analysis:

from scripts.preprocessing import inventory_video_files, extract_video_metadata, build_video_timeline

# 1. Full video inventory
video_files = [f for f in all_files if Path(f).suffix.lower() in VIDEO_EXTENSIONS]
inventory = inventory_video_files(video_files)

# 2. Extract metadata for each video
metadata_list = [extract_video_metadata(v['path']) for v in inventory]

# 3. Build timeline with critical window flagging
timeline = build_video_timeline(metadata_list, critical_start, critical_end)

# 4. Identify critical window videos
critical_videos = [v for v in timeline if v.get('in_critical_window')]

# 5. Classify by origin
camera_vids = [v for v in inventory if v['video_type'] == 'camera_recording']
received_vids = [v for v in inventory if v['video_type'] in ('received', 'chat_media', 'social_media')]
screen_recs = [v for v in inventory if v['video_type'] == 'screen_recording']

# 6. Duration analysis — total recording time during critical window
# This is powerful: if the client has 45 minutes of video recordings
# during a 1-hour critical window, they were holding their phone
# and recording, not committing a crime
critical_recording_time = sum(v.get('duration_seconds', 0) for v in critical_videos
                              if v.get('video_type') in ('camera_recording', 'screen_recording'))

# 7. GPS extraction from videos — plot alongside other location data
gps_videos = [v for v in metadata_list if v.get('gps_raw')]
```

---

## 7. Browser History & Search Queries {#7-browser}

### What to Extract
- URLs visited with timestamps
- Search queries (Google, Bing, etc.) with timestamps
- Bookmarks
- Download history
- Cookies and cached content
- Autofill data
- Private/incognito mode indicators (absence of expected history may indicate private browsing, which is normal privacy behavior, NOT consciousness of guilt)

### Defense Analysis Checklist

**Context Is Everything:**
- [ ] ALWAYS read search queries in context of adjacent searches — a search for "how to clean blood" that follows "nosebleed won't stop" has an innocent explanation
- [ ] Check whether the search was typed or auto-suggested — auto-complete can generate alarming-looking queries from innocent partial inputs
- [ ] Cookies ≠ visits — cookie presence indicates a site was loaded (possibly via ad, redirect, or tracking pixel), not that the user intentionally navigated there
- [ ] Cached images ≠ viewed images — browsers cache thousands of images the user never sees (ad networks, tracking pixels, link preview thumbnails)

**Defense-Favorable Browser Evidence:**
- [ ] Searches consistent with innocent activity during the critical window ("pizza near me," "movie times," "weather tomorrow")
- [ ] Searches that support the defense narrative ("self-defense laws," "restraining order how to get," "domestic violence hotline")
- [ ] Browsing activity that places the client at home or engaged in normal life during the alleged crime
- [ ] Absence of the kind of searches the State's theory would predict (if the State claims premeditation, the absence of planning-related searches is notable)

**What the State Will Misuse:**
- [ ] Isolated searches taken out of context
- [ ] Searches from days or weeks before the incident presented as "premeditation"
- [ ] Shared-device searches attributed to the client (verify: was anyone else using this device?)
- [ ] Auto-complete artifacts treated as intentional queries

### Programmatic Analysis (Browser Data)

```python
# 1. Search query session reconstruction
# Group search queries by session (queries within 5 minutes of
# each other are likely the same research session)
# Present sessions as units — shows context around any
# query the State will highlight

# 2. Adjacent search context
# For any search query the State flags, extract the 5 searches
# before and 5 after — this is the context that changes meaning

# 3. Browsing activity during critical window
# Filter all URLs and searches to crime date ± 24h
# Active browsing during the alleged crime = alibi evidence

# 4. Shared device indicators
# Check for searches in multiple languages, drastically different
# topics, or searches during times client was confirmed elsewhere
# (may indicate someone else used the device)

# 5. Auto-complete vs. intentional query detection
# Auto-complete suggestions appear in some extraction formats
# differently from typed queries — distinguish them
# Flag any query that may be an auto-complete artifact
```

---

## 8. Application Data {#8-app-data}

### Key App Categories

**Financial Apps (Venmo, Cash App, banking):**
- Transaction history with timestamps and locations
- Transfers to/from relevant individuals
- Balance history around relevant dates
- Defense use: financial transactions can establish timeline, location, and relationships

**Navigation Apps (Google Maps, Waze, Apple Maps):**
- Search history, recent destinations, saved locations
- Route history with start/end times
- Estimated vs. actual travel times
- Defense use: route data is precise timeline evidence; "no route to crime scene" is powerful

**Ride-Share (Uber, Lyft):**
- Trip history with precise pickup/dropoff locations and times
- Driver information (independent witness)
- Defense use: independently verifiable alibi evidence with GPS precision

**Fitness/Health Apps:**
- Step counts and activity levels with timestamps
- Heart rate data (stress/activity indicators)
- Sleep tracking data
- Defense use: step count showing sedentary activity during alleged crime; sleep data showing client was asleep

**Social Media:**
- Posts, stories, check-ins with timestamps
- DMs (see Chat Applications section above)
- Login activity logs (IP addresses, device types, locations)
- Defense use: public posts/check-ins are timestamped alibi evidence; login locations provide location data
- **Hand off authentication challenges to dw-social-media-auditor**

**Notes/Memo Apps:**
- Saved notes with creation and modification timestamps
- Deleted notes (recoverable from SQLite)
- Defense use: notes showing the client's plans, thoughts, or to-do lists inconsistent with criminal intent

**Calendar:**
- Events, appointments, reminders
- Event locations
- Defense use: scheduled events at alibi locations; established routine

### Defense Analysis for All Apps
- [ ] Check app install dates — when was the app first installed? Was it present before, during, and after the incident?
- [ ] Distinguish automatic app activity from user-initiated activity
- [ ] Verify account ownership — is the logged-in account actually the client's?
- [ ] Check for multiple accounts or profiles on the same app
- [ ] Note apps that were uninstalled around the incident date — but also note that app cleanup is normal device management

### Programmatic Analysis (App Data)

```python
# 1. Financial transaction timeline
# Extract all financial app transactions (Venmo, Cash App, etc.)
# with timestamps, amounts, recipients, and descriptions
# Map to timeline — transactions establish location and activity

# 2. Ride-share trip extraction
# Parse Uber/Lyft databases for trip history
# Extract: pickup/dropoff coords, times, driver info
# These are independently verifiable alibi records

# 3. Fitness/health data extraction
# Step counts by hour, heart rate data, sleep tracking
# Step count during alleged crime window can establish
# whether client was active (walking) or sedentary

# 4. Navigation app history
# Extract recent destinations, route history, saved locations
# from Google Maps, Waze, Apple Maps databases
# "No route to crime scene in search history" is notable

# 5. App install/uninstall timeline
# Parse app management databases for install dates,
# last-opened dates, and uninstall events
# Apps installed long before incident and never opened are noise

# 6. Calendar/reminder extraction
# Extract events, appointments, reminders
# Events at alibi locations are schedule evidence
# "Alarm set for 6:00 AM" suggests planning for a normal day
```

---

## 8A. Financial App Data {#8a-financial}

Financial app data is often the most underutilized category in phone dumps. Every Venmo payment, Cash App transfer, or Zelle transaction creates a timestamped, location-tagged record of real-world activity. A Zelle payment at 9:15 PM proves the client was on their phone conducting a financial transaction at that exact moment — and the recipient can independently verify it happened.

### What to Extract
- Cash App: transaction history (sent/received), Bitcoin transactions, account activity, linked bank info
- Venmo: payment feed (timestamps, recipients, amounts, notes), friend list, linked accounts
- Zelle: transfer history with timestamps and recipient info
- PayPal: transaction log, invoices, payment requests
- Apple Pay / Google Pay: transaction history with merchant names and locations
- Banking apps: transaction logs, login timestamps, check deposits (photo captures with timestamps)
- Cryptocurrency wallets: transaction IDs, wallet addresses, timestamps

### Defense Analysis Checklist

**Alibi & Timeline:**
- [ ] Transactions during the critical window — a Cash App payment at 9:22 PM means the client was on their phone at 9:22 PM
- [ ] Merchant transactions with locations (Apple Pay at a gas station, food delivery order) — places the client at a specific business
- [ ] Food delivery app orders (DoorDash, UberEats) with delivery addresses — proves location
- [ ] Ride-share payments (Uber, Lyft) — ride history includes pickup/dropoff locations and times
- [ ] ATM withdrawals — bank apps log ATM locations and timestamps

**Third-Party Suspects:**
- [ ] Payments to/from unknown individuals around the incident date
- [ ] Unusual financial activity from people connected to the case
- [ ] Cash App / Venmo notes that reference case-relevant people or events

**Victim Credibility / Relationship:**
- [ ] Payment history between client and victim — regular payments may show nature of relationship
- [ ] Venmo notes between parties (people write revealing things in Venmo notes)
- [ ] Financial disputes or refund requests that indicate conflict

**State's Narrative Contradictions:**
- [ ] If the State claims the client was at the crime scene, but Apple Pay shows a transaction at a different location at the same time
- [ ] Financial records that contradict witness statements about the client's whereabouts

**What Hurts Us:**
- [ ] Payments that could be characterized as drug transactions (round numbers, coded Venmo notes)
- [ ] Financial patterns the State will try to use as circumstantial evidence

### Programmatic Analysis (Financial Data)

```python
# 1. Transaction timeline — extract all financial app transactions
#    and plot chronologically against critical window
# 2. Location extraction — pull merchant locations from Apple Pay/
#    Google Pay, ATM locations from banking apps
# 3. Contact cross-reference — match payment recipients against
#    known contacts, victim, witnesses, co-defendants
# 4. Pattern analysis — regular vs. unusual transactions
#    (with baseline comparison, as always)
```

---

## 8B. Health & Fitness Data {#8b-health}

Health data from Apple Health, Google Fit, Fitbit, or similar apps records continuous biometric and activity data that the phone owner usually doesn't think about — which makes it highly credible as evidence. Step counts prove walking, heart rate data proves physical exertion or rest, and sleep data proves the client was in bed. This data is difficult to fabricate because it's collected passively by sensors.

### What to Extract
- Step counts with timestamps (Apple Health, Google Fit, Fitbit, Samsung Health)
- Heart rate data with timestamps (Apple Watch, Fitbit, wearables)
- Sleep data (bedtime, wake time, sleep stages)
- Workout records (type, duration, start/end times, GPS routes for outdoor activities)
- GPS-tracked exercise routes (running, cycling, walking)
- Stand/move/exercise ring data (Apple Watch)
- Elevation/floor climbing data
- Blood oxygen, ECG, or other medical sensor data

### Defense Analysis Checklist

**Alibi & Timeline:**
- [ ] Step count data during the critical window — zero steps during a period when the State claims the client was walking/running proves they were stationary. Conversely, continuous step data proves they were on their feet and moving.
- [ ] Workout GPS routes — if the client was on a tracked run during the crime window, the GPS breadcrumb trail is continuous alibi evidence
- [ ] Sleep data showing the client was asleep during the alleged offense
- [ ] Heart rate data — resting heart rate during the crime window is inconsistent with violent physical activity

**Client State of Mind / Physical State:**
- [ ] Heart rate spikes may indicate stress, fear, or physical exertion — context-dependent
- [ ] Blood alcohol content logging (some apps track this)
- [ ] Medication reminders and adherence tracking

**State's Narrative Contradictions:**
- [ ] If the State claims the client ran from the scene, but step count shows zero activity
- [ ] If the State claims a violent struggle, but heart rate data shows resting levels
- [ ] Wearable device GPS data that contradicts cell tower placement

**Prosecution Misinterpretation Watch:**
- [ ] Wearable data can be misleading — the device records the wearer's data, but if the client wasn't wearing it, the data doesn't apply. Verify the client was wearing the device.
- [ ] Step counts can be generated by arm motion (not just walking) — the State or defense shouldn't overstate precision
- [ ] Heart rate is affected by many factors (caffeine, medications, anxiety) — elevated heart rate ≠ guilt

### Programmatic Analysis (Health Data)

```python
# Apple Health data is typically exported as XML (export.xml)
# Google Fit data as JSON or CSV from Takeout

# 1. Parse health data into timestamped records
# 2. Filter to critical window ± 24 hours
# 3. Plot step count timeline — identify active vs. stationary periods
# 4. Overlay heart rate data if available
# 5. Extract sleep records spanning the incident date
# 6. Pull GPS workout routes and compare to case-relevant locations
```

---

## 8C. Personal Data Apps {#8c-personal}

Notes, calendars, reminders, voice memos, and email on the phone often contain the most candid, unguarded information — things people write to themselves or say aloud when they think no one is listening.

### What to Extract

**Notes Apps (Apple Notes, Google Keep, Samsung Notes, third-party):**
- Note content, creation date, modification dates
- Shared notes and collaborators
- Deleted notes (recoverable from SQLite databases)
- Handwritten notes (Apple Pencil / stylus input)
- Embedded images, sketches, scanned documents within notes

**Calendar / Reminders:**
- All calendar events with dates, times, locations, attendees
- Recurring events (establishes routine)
- Reminders with due dates and completion status
- Shared calendars and invitations

**Voice Memos:**
- Recording timestamps and durations
- Audio content (flag for attorney review — cannot assess programmatically)
- File names (some users label their memos descriptively)

**Email:**
- Email accounts configured on the device
- Sent/received emails during the critical window
- Email timestamps (independent of text message timeline)
- Attachments sent or received

### Defense Analysis Checklist

**Notes:**
- [ ] Notes written during or near the critical window — real-time journaling, to-do lists, or emotional processing
- [ ] Notes documenting threats, incidents, or concerns about the victim or others (contemporaneous documentation is powerful)
- [ ] Deleted notes — what did the client write and then remove? Apply same deletion analysis as messages (habit vs. targeted)
- [ ] Notes the State will try to use — read in full context, not excerpted

**Calendar:**
- [ ] Calendar events during the critical window — establishes what the client expected to be doing
- [ ] Work schedule entries that corroborate alibi
- [ ] Appointments with specific locations and times
- [ ] Recurring events that establish routine (baseline evidence)
- [ ] Shared calendar events that other people can independently verify

**Voice Memos:**
- [ ] Any voice memos recorded during or near the critical window — flag for immediate attorney review
- [ ] Voice memos documenting prior incidents, threats, or the client's emotional state
- [ ] Duration of voice memos — like videos, a long recording proves the client was holding their phone
- [ ] Background audio in voice memos may capture environment, voices, or events

**Email:**
- [ ] Emails sent/received during the critical window (parallel timeline to text messages)
- [ ] Work emails that establish the client was engaged in professional activity
- [ ] Emails with location-aware signatures or auto-responses ("Sent from my iPhone" with location)

---

## 9. System Artifacts & Logs {#9-system}

### What to Extract
- Device power on/off events
- Screen lock/unlock events
- Battery charge/discharge patterns
- Network connection history (cellular, Wi-Fi, Bluetooth)
- App usage logs (screen time, foreground/background)
- Notification logs
- Alarm and timer settings
- Device settings changes

### Defense Analysis Checklist

- [ ] **Power events:** Device power-off during the crime window may mean the phone was off (client asleep, phone dead) or may mean the device was powered down deliberately — context from other evidence determines which interpretation is appropriate
- [ ] **Screen unlock patterns:** Frequency and timing of screen unlocks can establish the client's general activity pattern — deviation from normal may be significant
- [ ] **Battery levels:** Battery at 2% explains a sudden cessation of phone activity better than "consciousness of guilt"
- [ ] **Network connections:** Wi-Fi connections to known networks establish location; Bluetooth connections to known devices establish proximity to specific people or vehicles
- [ ] **Alarm settings:** An alarm set for 6:00 AM is evidence of planning for a normal next day — inconsistent with planning to commit a crime that night
- [ ] **App usage data:** Screen time reports showing which apps were used and when can establish the client's activity timeline independently of message content

### Programmatic Analysis (System Artifacts)

```python
# 1. Power event timeline
# Extract all power on/off, screen lock/unlock events
# Map against critical window — active device use = presence

# 2. Network connection history
# Parse Wi-Fi connection log for network names and timestamps
# Parse Bluetooth pairing log for connected devices
# Both establish proximity to known locations/people/vehicles

# 3. Battery level reconstruction
# If battery state logs available, reconstruct charge curve
# Battery at 2% explains phone going dark better than
# "consciousness of guilt" — always check this first

# 4. Screen time / app usage aggregation
# Aggregate app foreground time during critical window
# Active app use during alleged crime time is alibi evidence
# Present as: "At 9:14 PM, client was actively using Netflix
# for 23 minutes" — inconsistent with committing a crime

# 5. Notification log extraction
# Parse notification database for incoming alerts
# Notifications from apps can timestamp activity even when
# the user didn't open the app
```

---

## 9.1A: Notification History {#91a-notifications}

### What it Contains

Cellebrite exports notification logs under **Device Information** or **Application Data** (varies by extraction type and OS). Each notification record typically includes:
- App name / identifier
- Notification title and body text
- Timestamp (when notification was delivered to the device)
- Delivery status
- Interaction status (tapped/opened, dismissed, ignored, not interacted with)
- Message ID or thread ID (for messaging app notifications)

### Where in Cellebrite

Notification history location varies by OS and extraction method:

**iOS:** Device Information > Notifications, or under individual app data folders
**Android:** Device Information > Notifications, or within app-specific SQLite databases (varies by manufacturer and Android version)

Some extractions may label this as "Notification Log," "Push Notifications," "Alert History," or "App Alerts" — check multiple locations if the standard path is empty.

### Why Notification Data is Critical for Alibi Evidence

Notifications are powerful because they generate independent, timestamped records from third-party services:

- **Delivery proof:** A notification received proves the phone was powered on and receiving data at that moment
- **Active engagement proof:** If the client *tapped* (opened) a notification, this proves they were actively holding and looking at the phone at that specific timestamp — far stronger than passive message receipt
- **Third-party timestamp validation:** Notifications from Uber, DoorDash, Amazon, and banking apps can be independently verified via subpoena to those services, creating corroboration
- **Routine/alibi anchoring:** Notifications about familiar activities (delivery confirmations, meeting alerts, routine alarms) establish the client was engaged in normal life

### Defense Analysis Checklist

**Alibi & Timeline:**
- [ ] **Notifications received during critical window** — Proves phone was on and receiving data (passive evidence)
- [ ] **Notifications tapped/opened during critical window** — Proves active user engagement; someone was looking at the phone at that exact moment (active evidence)
- [ ] **Alarm notifications** — Scheduled alarms firing during the critical window prove the phone was at expected location per routine (e.g., "Wake-up alarm fired at 6:30 AM at home")
- [ ] **Delivery/rideshare notifications** — Uber arrival, DoorDash delivery, Amazon package notifications provide independent timestamp + potential location evidence
- [ ] **Security/smart home notifications** — Ring doorbell, Nest camera, security system alerts can trigger subpoena of external footage corroborating the client's location or activity
- [ ] **Banking/payment notifications** — Transaction confirmations with amounts, merchants, and timestamps establish what the client was doing with their money at that moment
- [ ] **Calendar reminder notifications** — Proves scheduled events existed and were active in the device at that moment

**Prosecution Misinterpretation Watch:**
- [ ] **Notification receipt vs. interaction:** Notifications can be received without the phone being in the defendant's hands (e.g., phone left at home still receives push notifications from apps). This is PASSIVE evidence.
- [ ] **Distinguish receipt from engagement:** A notification tapped/opened requires ACTIVE user engagement. A client opening a text notification at 9:24 PM proves they were looking at the phone at 9:24 PM — far stronger than merely receiving it.
- [ ] **Dismissal counts as interaction:** If a notification was explicitly dismissed (not just ignored/auto-cleared), this shows the client was actively managing their notifications
- [ ] **"Notifications can be delayed":** This is sometimes true, but third-party service notifications (Uber, DoorDash, banks) are typically delivered in real-time. Always distinguish between app-to-device notifications (may be delayed) and network-based notifications (usually real-time).

**Cross-Reference Value:**
- [ ] **Uber/Lyft notifications** — Can be verified via subpoena to Uber/Lyft showing pickup/dropoff location and time
- [ ] **DoorDash/Amazon/delivery notifications** — Subpoena confirms delivery address and timestamp
- [ ] **Banking notifications** — Subpoena to bank confirms transaction location (if captured), amount, and timestamp
- [ ] **Messaging app notifications** — Cross-reference against message content in SMS/iMessage/WhatsApp logs to confirm they match
- [ ] **Calendar reminders** — Cross-reference against calendar events in the device to confirm scheduled activities

### Alibi Value Example

"At 9:23 PM, the defendant's phone received a push notification from Amazon confirming delivery of order #[X] to their home address. At 9:24 PM, the notification was tapped (opened), proving the defendant actively engaged with the notification. This demonstrates the defendant was actively using their phone at their home address at 9:24 PM — inconsistent with the State's allegation they were at the crime scene [X miles away] at that time."

**With third-party corroboration:** "The Amazon notification timestamp can be independently verified via subpoena to Amazon, which will confirm the exact delivery time and address. Ring doorbell footage from the defendant's address [if available] may also corroborate the delivery and the defendant's presence."

---

## 9A. Application Usage & Screen Time {#9a-appusage}

### What to Extract

Cellebrite exports application usage logs under **Device Information > Application Usage**. This data captures:
- App name / bundle identifier / package name
- Launch timestamp (when app came to foreground)
- Foreground duration (seconds/minutes the app was actively in use)
- Termination timestamp (when app left foreground)
- Total session duration
- App category / classification (social, productivity, entertainment, etc.)

This is distinct from installed apps — an app may be installed but never launched, or launched once. App *usage* is what matters defensively.

### Why App Usage Data is Gold for Alibi Evidence

App usage logs prove active, engaged phone use at a specific timestamp. Unlike:
- **Received messages:** The client may have been sleeping when a message arrived
- **Incoming calls:** The client may not have answered
- **Location pings:** Passive — phone updates location in background without user interaction

App usage requires the phone owner to:
1. **Unlock the device**
2. **Launch or switch to the app**
3. **Interact with it** (scrolling, typing, tapping)
4. **Keep it active** for the duration recorded

A forensic analyst looking at app usage logs sees: *"At 9:14 PM, Instagram was in foreground for 23 minutes"* — this proves:
- The phone was unlocked
- The phone owner was actively engaged
- They were holding/looking at the phone for 23 minutes
- They could not have been elsewhere committing a crime simultaneously

### Defense Analysis Checklist

**Alibi & Timeline:**
- [ ] **Critical window app usage:** Did any apps show active foreground use during the alleged crime window? This is among the strongest alibi evidence.
- [ ] **Duration analysis:** How long was each app active? A 45-minute Instagram session during the crime window proves continuous engagement.
- [ ] **App switching patterns:** Look for normal, habitual patterns — client switching between apps shows conscious, intentional behavior inconsistent with being at a crime scene.
- [ ] **Compare against baseline:** Did the client use apps at this time of day normally? Heavy evening social media use is normal; using fitness apps at 3 AM would be unusual.

**Baseline Comparison:**
- [ ] **Typical active apps by hour:** Does the app usage profile during the crime window match the client's usual pattern?
- [ ] **Total screen-on time:** How much total screen time was the device in use? Compare to baseline hours.
- [ ] **App frequency deviations:** Did the client use apps they normally use, or was there a sudden change in app usage patterns?
- [ ] **Sleep period detection:** If device shows zero app usage from, e.g., 11 PM to 6 AM consistently, this establishes the client's sleep window.

**Prosecution Misinterpretation Watch:**
- [ ] **"Phone was idle":** Prosecution may claim the phone was not in active use during the crime window. Cellebrite app usage logs directly contradict this — produce the logs.
- [ ] **"App usage gaps mean concealment":** A 2-hour gap in app usage may simply mean the client was sleeping, driving, working, or in a movie. Baseline comparison explains gaps.
- [ ] **"Apps can run in background":** True, but Cellebrite captures *foreground* usage — time when the app is actively displayed to the user. This is the alibi gold.
- [ ] **"Client could have shared the phone":** If baseline shows the client uses Netflix at 9 PM every evening, then usage at 9 PM during the crime window fits the baseline. Shared device claims require independent evidence.

**Gaps & Missing Data:**
- [ ] **Cellebrite extraction method:** Logical extractions capture app usage from iOS app usage statistics databases and Android usage_stats. File system extractions may miss this data. Note the limitation.
- [ ] **Device reset / factory reset:** If the device was reset, app usage logs older than the reset date will be lost.
- [ ] **App data expiration:** Some devices only retain 30 days of app usage history; older data may not be present.

### Programmatic Analysis (App Usage Data)

```python
# 1. Critical window app timeline
# Filter app usage to crime date ± 4 hours
# Sort chronologically by launch timestamp
# For each app session: timestamp, app name, duration
# Flag any app sessions during crime window as alibi evidence

# 2. Foreground duration aggregation
# Sum total "screen on" time from app usage logs
# This is actual engaged use (not passive background process)
# Present as: "Device was in active app use for X hours
# during the crime window — inconsistent with [alleged activity]"

# 3. App-by-app frequency analysis
# Which apps did the client use most?
# Create hourly heatmap: which hours did each app see use?
# Compare against baseline: is crime-window app usage normal?

# 4. Sleep pattern detection from app usage gaps
# If logs show zero app activity from 11:30 PM to 6:30 AM
# consistently across the baseline period, client's sleep
# window is 11:30 PM – 6:30 AM. Map against crime window.

# 5. App switching rate
# Frequency of app switches indicates conscious, engaged use
# A client rapidly switching between apps shows intentional behavior
# High app-switch rate during alleged crime window = strong alibi

# 6. Baseline comparison
# Compute app usage profile for baseline period:
# - Apps used per day
# - Total foreground duration per day
# - Most-used apps by hour
# Compare against crime window to identify deviations

# 7. Category-based analysis
# Group apps by function: social, productivity, entertainment, utility
# Did the client use their normal mix of apps or a different mix?
# Sudden shift to different category may indicate anomaly
```

### Cellebrite-Specific Extraction Notes

**iOS (iPhone/iPad):**
- Stored in: `/private/var/mobile/Library/CoreSpotlight/CoreSpotlight.db` (searchable index) and app-specific usage stats
- Cellebrite logical extraction captures usage statistics maintained by iOS
- Data retained: Typically 30 days in iOS 11+; full history on earlier versions
- Reliability: High — iOS maintains precise foreground/background timestamps

**Android:**
- Stored in: `/data/system/usagestats/` directory (usage_stats files)
- Cellebrite logical extraction parses UsageStatsManager database
- Data retained: Typically 30 days; may vary by device manufacturer
- Reliability: High — Android UsageStats is the official app usage audit log

**Extraction Limitations:**
- **Logical only:** File system extractions may miss app usage logs
- **Physical/chip-off:** May capture deleted app usage logs from unallocated space (rare)
- **Cloud backups:** iCloud/Google Drive backups do NOT typically include app usage logs
- **App cache:** App usage logs are system files, not user-facing — factory resets or major OS updates clear them

### Prosecution Vulnerabilities in App Usage Claims

1. **Burden of proof on State:** If the State claims the client was at the crime scene, but app usage logs show continuous engagement elsewhere, the State's narrative is contradicted by objective forensic data.
2. **Specificity of alibi:** App usage is more specific than location data alone — it proves not just presence, but active engagement and consciousness.
3. **Cross-corroboration:** App usage often corroborates location (e.g., "Netflix in-use at home" + Wi-Fi connected to home network = dual confirmation).
4. **Timing precision:** App launch timestamps are precise to seconds — more precise than cell tower pings.

---

## 9.1B: Keyboard Cache, Clipboard & Typing Artifacts

### What These Sources Contain

**Keyboard cache / learned words**: Words the user typed frequently enough for the keyboard to learn them. iOS and Android maintain local dictionaries of user-typed words for predictive text.

**Autocorrect history**: Words that were autocorrected, revealing intended vs. actual text.

**Clipboard history**: Text and images copied to the clipboard (some Android phones maintain clipboard history; iOS is more ephemeral).

**User dictionary**: Custom words manually added by the user.

**Draft messages**: Partially typed messages that were never sent (may be recoverable from app databases).

### Where in Cellebrite

Under Device Information > User Dictionaries, or within individual app databases. Samsung Keyboard, Gboard, and SwiftKey each store data differently.

### Defense Analysis Checklist

- [ ] **Keyboard learned words** — any words related to charged conduct? (Absence = defense favorable)
- [ ] **Clipboard contents during critical window** — what was copied?
- [ ] **Draft/unsent messages** — did the defendant type something and delete it before sending?
- [ ] **Autocorrect patterns** — do they reveal the defendant's typical language vs. someone else using the phone?
- [ ] **Language patterns** — can keyboard data help establish or refute shared device claims?

### Defense Value

**Absence of charge-related vocabulary** is defense favorable ("keyboard learned 15,000 words over 2 years — zero are related to [charged conduct]")

**Keyboard language patterns** can help establish identity (one user's typing patterns vs. another's on a shared device)

**Draft messages** may reveal state of mind or intentions that were never communicated

### Prosecution Misinterpretation Watch

- Keyboard cache contains words from ALL contexts — a word appearing in the cache doesn't mean it was typed in a criminal context (could be from a news article, autocomplete suggestion, or text received and re-typed)
- Clipboard contents are transient and may be from any app context
- The keyboard learns from everything typed, including search queries, form fields, and notes — not just messages

### Limitations

- Keyboard cache is volatile — resets on app updates, keyboard changes, or factory reset
- Not all extraction types capture keyboard data
- iOS keyboard cache is more limited than Android

---

## 10. Timeline Construction & Pattern of Life Baseline Methodology {#10-timeline}

### Building the Pattern of Life Baseline (REQUIRED — Run Before Critical Window Analysis)

The baseline establishes what "normal" looks like for this device. Without it, nothing found in the critical window can be called unusual, and nothing the State calls "suspicious" can be rebutted.

**Baseline Period:** Select 2–4 weeks of data from BEFORE the alleged offense, excluding any atypical periods (vacations, hospitalizations, known life disruptions).

**Step 1: Compute communication baselines**
```python
import pandas as pd

# Daily message volume
baseline_period = df[(df['timestamp'] >= baseline_start) & (df['timestamp'] < baseline_end)]
daily_msgs = baseline_period.groupby(baseline_period['timestamp'].dt.date).size()
avg_daily_msgs = daily_msgs.mean()
std_daily_msgs = daily_msgs.std()

# Per-contact frequency
contact_freq = baseline_period.groupby('contact').size().sort_values(ascending=False)
# Top contacts with their average daily/weekly frequency

# Hourly activity pattern
hourly_pattern = baseline_period.groupby(baseline_period['timestamp'].dt.hour).size()
# Identifies normal active hours vs. quiet hours
```

**Step 2: Compute call baselines**
```python
# Daily call volume, average duration, top contacts
# Same structure as messages — establishes what "normal calling" looks like
# CRITICAL: This baseline defeats "high frequency" arguments by the State
```

**Step 3: Compute location baselines**
```python
# Identify regularly visited locations (home, work, frequent stops)
# Establish normal daily movement patterns
# Compute: what percentage of time is the client at each location?
```

**Step 4: Compute activity window baselines**
```python
# First activity each day, last activity each day
# Normal quiet periods (sleeping hours, work hours if no phone use at work)
# This determines whether gaps during the critical window are normal
```

**Step 5: Generate the baseline summary**
Output the Pattern of Life Baseline table specified in SKILL.md Step 3.5. This summary travels with every subsequent analysis step and anchors all "unusual activity" findings.

**Using the Baseline During Critical Window Analysis:**
- Any claim that activity was "unusual" must cite the specific baseline metric it deviates from
- Any gap in activity must be compared against normal quiet periods before being flagged as suspicious
- Any "high frequency" contact must be compared against the baseline frequency for that contact AND the client's overall contact patterns
- The baseline itself may be the defense's best evidence — a routine, predictable pattern of life inconsistent with criminal planning

### Building the Critical Window Timeline

The critical window is the alleged crime date/time ± a reasonable buffer (typically ± 6-24 hours depending on the charge and the State's theory).

**Step 1: Collect all timestamped data points within the critical window**
- Messages (sent, received, read)
- Calls (start, duration)
- Location pings (cell tower, GPS, Wi-Fi)
- Photos/videos (capture time)
- App activity (usage logs, transactions)
- System events (power, unlock, network)
- Browser activity (page loads, searches)

**Step 2: Normalize timestamps**
- Verify all timestamps are in the same time zone
- Account for DST transitions if the critical window spans one
- Note any timestamps from carrier records vs. device records (may use different time bases)
- Flag any timestamp anomalies (out-of-sequence events, impossible time jumps)

**Step 3: Build the unified chronological timeline**
- Sort all events chronologically
- Color-code by source type (message = blue, call = green, location = red, etc.)
- Flag defense-favorable events prominently
- Annotate gaps (periods with no activity)

**Step 4: Overlay the State's narrative**
- Map the State's claimed sequence onto the timeline
- Identify conflicts (the State says X happened at 9:15 PM, but the phone shows the client was texting from a different location at 9:12 PM)
- Calculate feasibility (could the client have traveled from the last phone ping to the crime scene in the time the State claims?)

**Step 5: Build the defense counter-narrative**
- Using the phone data, construct the most favorable-to-defense timeline of events
- Identify which data points are strongest and which require corroboration
- Note what additional evidence would strengthen the defense timeline (surveillance video, witness testimony, carrier records)

---

## 11. Deleted Data Interpretation & Defense Analysis {#11-deleted-data}

### Why Deleted Data Requires Special Treatment

Prosecution routinely argues "deletion = consciousness of guilt." This oversimplification ignores the fundamental reality of mobile devices: data deletion happens constantly, often automatically, and almost never because a user committed a crime.

The defense needs a structured framework to rebut this bias because:

1. **Automatic deletion is ubiquitous** — Modern mobile devices delete data without any user action as part of normal operation (storage management, app cache cleanup, message expiration, system lifecycle events).

2. **Deletion doesn't equal absence of innocence** — The absence of evidence is not evidence of absence. A defendant who knew about an investigation might delete communications, but so might a defendant who values privacy, manages storage, or simply reset their phone during a normal upgrade cycle.

3. **Recovery is probabilistic** — "Deleted" in forensic extraction reports doesn't mean the data definitely existed or that the content can be definitively reconstructed. Recovery from SQLite free pages or WAL journals is subject to overwriting, fragmentation, and data decay.

4. **Volume context is critical** — If 0.4% of messages show "deleted" status across 50,000 messages, that's consistent with normal attrition. If 95% are deleted, that's a different story. The baseline matters.

### Automatic Deletion Mechanisms (Reasons Data Gets Deleted WITHOUT User Action)

Defense must be prepared to articulate these mechanisms to the jury, expert witnesses, and the court:

#### iMessage Thread Cleanup (iOS Auto-Manages Storage)
- iOS automatically culls old iMessage conversations to maintain storage efficiency
- Older messages in long-running conversations are silently deleted by the OS, not the user
- Even if the user NEVER deleted messages, old iMessage data disappears
- **Defense framing:** "iMessage management is automatic on iOS. The presence of deleted messages does not indicate the user deleted them."

#### App Updates That Clear Caches/Databases
- Updates to social media apps, messaging apps, and communication platforms frequently reset local databases
- When an app updates, local cached data may be purged as part of standard update procedure
- User installs an update to WhatsApp; the app's local cache resets automatically
- **Defense framing:** "App updates routinely clear cached data. This is not user-initiated deletion."

#### Storage Management (Low-Space Auto-Cleanup)
- When a device approaches storage capacity, iOS and Android automatically delete cached data, temporary files, and old app data
- Photos, videos, and app databases may be auto-deleted to free space before the user is even aware of low storage
- System operates autonomously to prevent device malfunction
- **Defense framing:** "Modern phones automatically delete old data when storage is low. This is a device maintenance feature, not evidence of concealment."

#### System Message Auto-Expiration (OTP Codes, Verification Texts)
- One-time passwords, two-factor authentication codes, and verification texts are designed to auto-delete after a set period
- Banking apps, email verification, social media login codes expire automatically from the message database
- User doesn't delete these; the system does
- **Defense framing:** "Verification and authentication texts auto-expire by design. Their absence is not concealment."

#### Snapchat/Ephemeral App Design (Auto-Delete Is the Feature, Not Concealment)
- Snapchat, Telegram, Signal, and other ephemeral-by-default apps are designed so messages disappear automatically
- If the client used Snapchat primarily, the absence of messages is a direct result of the app's business model, not the user's attempt to conceal
- Extraction shows no messages because the platform doesn't store them permanently
- **Defense framing:** "Snapchat is designed so messages disappear. The client using Snapchat is consistent with how millions of people use the platform, not evidence of guilt."

#### WhatsApp Media Auto-Download Expiration
- WhatsApp automatically deletes downloaded media files after a set retention period (default 30 days for some file types)
- Media attachments in conversations may appear as deleted even though the user never touched them
- **Defense framing:** "WhatsApp's media retention settings automatically delete downloaded files. This is app default behavior."

#### Factory Reset as Normal Phone Lifecycle
- Phone trade-ins, carrier upgrades, troubleshooting, and battery replacement frequently trigger factory resets
- User exchanges old iPhone for new iPhone at Apple Store → old phone factory reset
- User trades old Android for new model → factory reset as part of trade-in
- User restores phone from backup → old data on device is erased
- **Defense framing:** "The phone was reset during [date], which coincides with a [carrier upgrade / troubleshooting session / trade-in]. Factory resets are routine when upgrading phones."

#### Samsung Wellbeing Deletion During Factory Reset
- Samsung phones running One UI include a "Wellbeing" feature that offers automatic cleanup/factory reset options
- Users may unknowingly trigger data deletion through this system feature
- **Defense framing:** "Samsung's Wellbeing feature includes automatic cleanup options. If a reset occurred, this may explain the deleted data without user intent."

#### iOS "Offload Unused Apps" Feature
- iOS has a built-in feature to automatically offload and reinstall apps to save storage space
- When an app is offloaded, its local data is deleted automatically
- User may not know this feature is enabled or may not understand its implications
- **Defense framing:** "iOS automatically offloads apps to save storage. When an app is reinstalled, its local data is gone."

#### Carrier Message Retention Limits
- Carriers automatically delete SMS messages from their servers after a retention period (typically 30 days to 6 months depending on the carrier)
- Even if the message extraction includes carrier records, messages older than the retention window won't appear
- This is carrier infrastructure, not user behavior
- **Defense framing:** "Carriers automatically delete SMS records after their retention period. The absence of old messages reflects carrier policy, not user deletion."

### Cellebrite Recovery Context

Understanding how forensic extraction reports "deleted" data is critical for defense:

#### "Deleted" Status in Cellebrite Means Carved from SQLite WAL, Free Pages, or Unallocated Space

When Cellebrite reports a message as "deleted," it typically means:
- The entry was found in SQLite write-ahead log (WAL) journals (intermediate database states)
- The entry was found in free/unallocated disk pages (previously written, now marked for deletion)
- The entry was partially recovered from fragmented data
- The entry's timestamp, context, or complete content may be reconstructed or inferred

This is **NOT** definitive proof that the user deleted it, that it was intentionally concealed, or that its original content is correctly recovered.

#### Recovery Is Probabilistic — Not All Deleted Data Is Recoverable

- Not all deleted data remains recoverable — much is overwritten, fragmented, or lost
- Data that IS recovered may be partial (fragments without complete context)
- Multiple database snapshots may show conflicting states — which represents the "true" deletion event?
- Partial recovery should be flagged in defense analysis; fragments without full context are weaker evidence than complete records

**Defense position:** "Of the estimated [X] messages that may have existed on this device during the critical period, Cellebrite recovered [Y] intact messages and [Z] deleted/fragmented messages. This recovery is incomplete and probabilistic. The absence of a recovered message doesn't prove the user deleted it — it may have been overwritten, lost to fragmentation, or inaccessible to forensic recovery methods."

#### WAL Journal Entries May Show Database States, Not Individual User Actions

- SQLite write-ahead logs show database transactions, not individual message deletions
- A single "delete" transaction in the WAL may reflect iOS auto-cleanup, not a user pressing "delete message"
- Multiple deletions in rapid succession in the WAL may indicate automatic bulk cleanup (storage management), not targeted concealment
- **Defense position:** "The deleted messages appear in SQLite transaction logs but cannot be definitively attributed to user action. They may reflect automatic system cleanup."

### Defense Analysis Checklist for Deleted Data

Apply this checklist systematically to every deleted-data argument the prosecution raises:

**Volume & Baseline Context**
- [ ] Total deleted records by category (messages, calls, photos, videos, contacts, browsing history)
- [ ] Total non-deleted records in the same category (to calculate deletion percentage)
- [ ] Deletion percentage: If [N deleted] / ([N deleted] + [N existing]) = X%, is X% consistent with normal attrition? (1-5% is normal; 50%+ is unusual)
- [ ] Baseline comparison: During pre-incident period, what was the normal message volume and deletion rate? Has the deletion pattern changed significantly?

**Content Characterization of Deleted Items**
- [ ] What is the content of recoverable deleted messages? (Mundane daily activity? System notifications? Incriminating? Exculpatory?)
- [ ] Do deleted messages contain case-relevant keywords or are they routine/system content?
- [ ] Are the deleted messages predominantly with the victim, co-defendants, or a broad cross-section of contacts?
- [ ] Exculpatory deletion: Were any deleted messages potentially exculpatory (establishing alibi, negating prosecution theory, or supporting self-defense)?

**Deletion Pattern Analysis: Bulk Deletion Event vs. Normal Attrition**
- [ ] Timeline of deletion: Do all/most deleted messages have timestamps suggesting deletion within a narrow window (bulk deletion event), or are they scattered across many dates (normal attrition)?
- [ ] Targeted vs. broad: Were specific conversations deleted (e.g., all messages with the victim), or were deletions scattered across many conversations?
- [ ] Factory reset indicator: Do the deleted messages correlate with a factory reset event? (If so, this reframes deletion as normal phone lifecycle, not concealment.)
- [ ] App update correlation: Do deletion dates correlate with app updates? (If so, this reframes deletion as automatic app maintenance.)

**Timeline of Deletion: Correlation With Investigation Notice**
- [ ] When did the client know of the investigation? (Arrest date? Search warrant service? Police contact?)
- [ ] Did bulk deletion occur BEFORE the client knew of investigation (consistent with normal maintenance), AFTER notice (potential consciousness of guilt), or cannot be determined?
- [ ] If deletion occurred after investigation notice, was there a legitimate reason? (Traded phone, reset for troubleshooting, storage full, app updated, etc.?)

**Comparison to Non-Deleted Data Volume**
- [ ] Total messages in the critical window: [N]
- [ ] Deleted messages: [M]
- [ ] Deletion rate: M / (N + M) = X%
- [ ] If the deletion rate is <5%, the volume context strongly supports a "normal attrition" defense
- [ ] If the deletion rate is >50%, the bulk deletion is concerning and requires explanation (factory reset, app update, storage management)

**Exculpatory Content in Deleted Data**
- [ ] Were any deleted messages potentially favorable to the defense? (Establishing alibi, contradicting the victim, supporting self-defense claim, etc.?)
- [ ] If exculpatory content was deleted, by whom? (The user or automatic system processes?)
- [ ] If the user deleted exculpatory data, this is a Brady violation or favorable for defense credibility arguments — was the deletion targeted at exculpatory evidence, or was it indiscriminate?

**Cross-Source Verification**
- [ ] Do deleted SMS messages appear in carrier records? (Carriers retain records independent of device storage)
- [ ] Do deleted messages appear in other devices, cloud backups, or third-party accounts? (If the "deleted" message also appears in the victim's phone, cloud backup, or email, it wasn't really deleted — just removed from this device)
- [ ] Do deleted call logs appear in carrier records?
- [ ] If cross-source verification shows the message wasn't deleted from carrier/third-party records, this undermines the "deletion = consciousness of guilt" narrative

**Factory Reset Analysis**
- [ ] Was there a factory reset of the device? When?
- [ ] Does the reset date correlate with phone upgrade (carrier switch, trade-in, new device purchase)?
- [ ] Does the reset date correlate with troubleshooting (phone malfunction, bricking, water damage)?
- [ ] Does the reset date correlate with the investigation timeline?
- [ ] If the reset was a normal phone lifecycle event (trade-in, upgrade, troubleshooting), frame it accordingly

### Prosecution Rebuttal Templates

Prepare these scripts to rebut predictable prosecution arguments:

#### "Defendant Deleted Messages"

**Prosecution Argument:** "The defendant deliberately deleted messages to conceal the crime, showing consciousness of guilt."

**Defense Rebuttal Template:**
> "Of approximately [50,000] messages on this device, [200] show deleted status in the forensic extraction. That represents [0.4%] of all messages. For context, iOS automatically manages message storage, and this deletion rate is entirely consistent with normal storage management on iPhone. Additionally, the deleted messages that were recoverable contain [description of content: system notifications, routine daily activity, etc.]. There is no evidence that the defendant targeted specific conversations for deletion. The volume and content of deleted messages indicate automatic system cleanup, not deliberate concealment."

**Stronger position (if recovered deleted content is mundane):**
> "The forensic extraction recovered [X] deleted messages. Review of these recovered messages shows they are predominantly [app notifications, delivery confirmations, system messages, etc.]. These are not messages the defendant would have a reason to conceal. If the defendant was attempting to cover up [the alleged crime], deletion would target conversations with [the victim / co-defendants], but the deletion pattern is random across all contacts."

#### "Defendant Factory-Reset the Phone"

**Prosecution Argument:** "The defendant factory-reset the device to destroy evidence, showing consciousness of guilt."

**Defense Rebuttal Template:**
> "The forensic examination indicates a factory reset occurred on [date]. This date is [N days before/after] the investigation began. On [same date or nearby date], [client traded in phone to carrier / upgraded from old device to new device / experienced phone malfunction requiring reset / sought technical support]. Factory resets are routine when upgrading phones or troubleshooting device issues. The timing of this reset correlates with [legitimate reason], not with the defendant's knowledge of the investigation."

**Alternative (if reset is before investigation notice):**
> "The factory reset occurred on [date], weeks before law enforcement contacted the defendant or executed any search warrant. The defendant would have had no reason to anticipate an investigation at that time. The reset is consistent with normal phone maintenance and upgrade cycles, not consciousness of guilt."

#### "Defendant Deleted Search History"

**Prosecution Argument:** "The defendant deleted search history, showing they were researching how to cover up the crime or researching the victim."

**Defense Rebuttal Template:**
> "Browser history is automatically managed by [Safari / Chrome / Firefox]. Deleting browsing data is a default privacy feature that many users enable routinely. The fact that search history is absent does not indicate the defendant was researching anything incriminating — it indicates the defendant used a common privacy feature. Additionally, [if available: defendant's browsing data recovered by forensics shows routine activity: shopping, news, social media, etc., consistent with normal device use]."

#### "Defendant Used Third-Party Deletion Apps"

**Prosecution Argument:** "The defendant installed a message deletion app, showing they were trying to conceal communications."

**Defense Rebuttal Template:**
> "Many users install privacy or cleanup apps for legitimate reasons: managing storage, protecting privacy, and cleaning up cache and junk files. Installation of such an app does not indicate the defendant was attempting to conceal evidence of a crime. [If app data available: The app was used [infrequently / as part of routine maintenance], consistent with general device cleanup, not targeted message deletion]."

### When Deletion IS Concerning (Honest Assessment for Attorney Discussion)

Defense counsel must be honest about when deletion patterns are genuinely suspicious. These situations require mitigation strategies with the attorney:

#### Targeted Deletion of Specific Conversations With Victim/Complainant While Preserving Others

**Red flag pattern:**
- All or nearly all messages with the victim/complainant are deleted
- Messages with other contacts remain intact
- Deletion pattern is clearly selective

**How to address with attorney:**
- This pattern is harder to defend as "automatic deletion" or "normal attrition"
- Explore whether the client has a legitimate explanation (victim-initiated request to delete, privacy preferences for sensitive relationship, anger/breakup leading to deletion)
- Prepare expert testimony on conversation-level privacy settings or app-specific features that might selectively delete conversations
- Consider whether exculpatory content was in the preserved messages, which may offset the damage of targeted deletion

#### Deletion Timestamps Correlating With Notice of Investigation

**Red flag pattern:**
- Bulk deletion occurred shortly after arrest, search warrant service, or police contact
- Deletion is clearly not routine maintenance; it's clustered in a narrow time window after investigation awareness

**How to address with attorney:**
- This is the hardest pattern to defend — it suggests the client knew about the investigation and deleted relevant data
- Explore alternative explanations: Did the client's phone malfunction and require reset? Was the phone traded in? Was there an app crash that prompted deletion?
- If no alternative explanation exists, discuss with attorney whether to stipulate deletion occurred (and address its prejudicial nature during jury instructions) vs. contesting it
- Prepare expert testimony on automatic vs. manual deletion to create reasonable doubt about user intent

#### Use of Third-Party Wiping Tools (Evidence Destruction Apps)

**Red flag pattern:**
- Installation of apps like "Eraser," "Permanent Eraser," or similar data destruction tools
- App was actively used around the time of the investigation

**How to address with attorney:**
- This is difficult to defend as innocent privacy management because the app is purpose-built for evidence destruction
- Research the app's marketing and user reviews — does it explicitly promise to hide criminal activity, or is it a generic privacy tool?
- Discuss with client whether they have a legitimate explanation for using the app (general privacy concerns, overly cautious about data security, etc.)
- Prepare for the reality that a jury may infer consciousness of guilt from this evidence — attorney may choose to address it directly (client wanted privacy) or to minimize its importance (minimal app use, other explanations for evidence absence)

#### Selective Deletion Pattern That Removes Only Incriminating Content

**Red flag pattern:**
- Messages with the victim that discuss motive, plan, or incriminating details are deleted
- Messages with other contacts on the same date remain intact
- Pattern is clearly selective to case-specific content

**How to address with attorney:**
- Discuss this honestly — if the pattern is truly selective to case content, it's very difficult to defend
- Explore whether ANY exculpatory or neutral content was also deleted (to support "indiscriminate" deletion argument)
- Research whether specific apps or devices have features that might selectively delete based on keywords or content
- Prepare for the likelihood that a jury will infer consciousness of guilt — work with attorney on how to minimize impact (jury instructions on inference, expert testimony on automatic deletion possibilities, alternative explanations)

### Programmatic Analysis (Deleted Data)

```python
# Key analyses for deleted data forensics:

# 1. Deleted message volume and percentage
deleted_count = len(df[df['status'] == 'deleted'])
total_count = len(df)
deletion_percentage = (deleted_count / total_count) * 100
# Flag if >20% or <1% (unusual patterns in either direction)

# 2. Deletion date clustering
# Group deleted messages by deletion date (if recoverable)
# Check if all deletions occurred in narrow time window (bulk deletion)
# or scattered across many dates (normal attrition)
deletion_dates = df[df['status'] == 'deleted']['deletion_date'].value_counts()
# High variance in deletion dates = normal attrition
# All deletions in 1-2 dates = bulk deletion event

# 3. Deleted content characterization
# Keyword search in recovered deleted message content
case_keywords = ['victim_name', 'weapon', 'location', 'time_indicators']
deleted_case_hits = df[(df['status'] == 'deleted') &
                       (df['content'].str.contains('|'.join(case_keywords), case=False))]
# If deleted messages lack case-specific keywords, deletion is likely routine

# 4. Comparison with non-deleted volume
deleted_by_contact = df[df['status'] == 'deleted'].groupby('contact').size()
existing_by_contact = df[df['status'] != 'deleted'].groupby('contact').size()
# If victim contact appears in both deleted AND existing messages, deletion is not targeted

# 5. Factory reset timeline
# Extract device logs for power-on, system events, software updates
# Correlate timestamps of bulk deletion with factory reset, app update, or low-storage events

# 6. Cross-platform message verification
# Search carrier records, cloud backups, other devices
# If "deleted" message appears in carrier records or backup, it wasn't deleted from the ecosystem
```

---

*This reference is loaded by the dw-forensic-dump-analyzer skill during Step 3 analysis. Each section corresponds to a data category in the extraction and provides the detailed checklist for all eight defense lenses.*
