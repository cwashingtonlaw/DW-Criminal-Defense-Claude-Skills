# Cellebrite Reader Application — Defense Analyst Reference

This reference maps the Cellebrite Reader application's data architecture to defense analysis workflows. Use this when parsing UFDR files, Cellebrite CSV/HTML exports, or reviewing Cellebrite Reader reports provided in discovery.

**Source:** Comprehensive analysis of Cellebrite Reader v7.60+ documentation, UFED Physical Analyzer manuals, and forensic community research (compiled March 2026).

---

## 1. Extraction Types and What They Limit

The extraction type determines the ceiling of available data. Always identify the extraction type first — it tells you what CAN'T be in the data, which is often more important than what is.

| Extraction Type | Data Available | What's Missing | Defense Implication |
|----------------|---------------|----------------|---------------------|
| **Logical** | Active user-facing data: current contacts, active SMS threads, recent call logs | Deleted data, hidden app data, deep system logs, WAL recovery, unallocated space | Weakest extraction — argue incomplete examination if State relies on "absence of evidence" |
| **File System** | Active databases, system files, full directory structure, partially deleted records from SQLite WAL/free pages | Deep carved artifacts, deleted partitions, unallocated space | Intermediate — WAL recovery possible but not guaranteed |
| **Physical** | Bit-by-bit memory dump: carved artifacts, deleted partitions, unallocated space, everything | Nothing (within hardware constraints) | Strongest extraction — absence of incriminating data in physical extraction is powerful defense evidence |

**Defense Rule:** If the State performed only a logical extraction and claims "no exculpatory data exists," challenge this — a logical extraction can't see deleted data, WAL records, or app-internal databases. Always check extraction type before making completeness arguments.

**Record Status Markers:** Cellebrite marks recovered records as:
- **Intact** — Active, live record
- **Deleted** — Carved from unallocated space, WAL, or free pages
- **Unknown** — Status indeterminate

---

## 2. UTC Timestamps and Time Zone Handling

**CRITICAL for timeline accuracy.**

- Mobile devices store ALL timestamps in **UTC** internally
- Cellebrite Reader applies a **global UTC offset** configured by the examiner
- This offset is applied universally across ALL tabs, conversations, and exports
- **DST transitions** must be manually accounted for — if the examiner set UTC-5 (CST) but the offense occurred during CDT (UTC-6), ALL timestamps could be off by 1 hour

**Defense Checks:**
1. What UTC offset did the examiner configure? (Check Welcome Tab / Extraction Summary)
2. Was the offset correct for the jurisdiction AND the specific date (DST-aware)?
3. Are there mixed-source timestamps? (e.g., carrier records in UTC vs. Cellebrite in local time)
4. Did the device's clock have an error? (Check system time settings vs. network time)

---

## 3. Application Interface Structure (Where Data Lives)

### Welcome Tab — Extraction Summary
First page when UFDR opens. Contains:
- Device manufacturer, model, OS firmware version
- **IMEI**, ICCID, IMSI (hardware identifiers)
- Extraction method (Logical / File System / Physical)
- Extraction timestamp and examiner identity
- Time zone settings
- **This forms the mandatory preamble of any Cellebrite-generated report**

**Defense Use:** Verify this against the lab report. Discrepancies = chain of custody challenge.

### Navigation Menu — Data Hierarchy

The left pane organizes data into these categories (record counts shown in parentheses):

```
Analyzed Data
├── Personal Information
│   ├── Calendar
│   ├── Contacts
│   ├── Notes
│   ├── Call Log
│   ├── User Accounts
│   └── User Dictionaries
├── Messaging Items
│   ├── SMS / MMS
│   ├── Email
│   ├── Instant Messages
│   └── Chats (WhatsApp, Signal, Telegram, FB Messenger, etc.)
├── Web Browser Items
│   ├── History
│   ├── Bookmarks
│   └── Cookies
├── Media Items
│   ├── Audio
│   ├── Images
│   └── Videos
├── GPS Information
│   ├── Fixes (single coordinate points from EXIF, weather apps, etc.)
│   ├── Journeys (navigation routes from Maps, Waze, etc.)
│   ├── Cellular Locations (cell tower handshakes)
│   └── Locations (Wi-Fi proximity logs)
└── Device Information
    ├── Bluetooth Pairings
    ├── Wireless Networks (saved Wi-Fi SSIDs + passwords)
    └── Application Usage (launch times, foreground duration, termination)

Data Files (sorted by file type, not by app)
├── Images, Videos, Audio, Text, Databases
├── Configurations, Applications, Documents
└── Uncategorized

File Systems (raw directory structure)
└── Root filesystem as it existed on flash storage
    └── Deleted files marked with red cross icon

Advanced Analytics / Insights
├── Installed Applications (categorized by risk: GPS spoofers, vault apps, wipers, ephemeral messaging)
├── Media Classification (ML: Weapons, Drugs, Nudity, CSA, Documents, Financial, Vehicles, Faces, Tattoos)
├── Cryptocurrency (wallet addresses, private keys, transaction hashes)
└── Project Analytics (communication frequency mapping between parties)

Timeline (cross-category chronological axis)
Map View (geospatial plotting with road/aerial/offline layers)
```

---

## 4. Column Headers by Data Category

These are the exact columns the skill will encounter when parsing Cellebrite exports. Use these to validate data completeness and identify missing fields.

### 4.1 Communications (Chats / SMS / Instant Messages)

| Column | What It Contains | Defense Value |
|--------|-----------------|---------------|
| **# (Identifier)** | Sequential ID assigned by parser | Use for source citation |
| **Participants/Name** | Sender/recipient, cross-referenced against contacts | Verify name resolution accuracy |
| **Direction/Role** | Incoming / Outgoing / Draft / System Message | Establishes who initiated contact |
| **Body Text** | Decrypted plaintext payload | Core evidentiary content |
| **Timestamp/Date** | Creation/transmission time (UTC offset applied) | Timeline reconstruction |
| **Delivered Date** | When message was delivered to recipient | Proves transmission occurred |
| **Read Date** | When message was read (from read receipts) | Proves consumption — negates ignorance claims |
| **Status** | Sent / Unsent / Read / **Deleted** | Deleted flag = carved from WAL/unallocated |
| **Source / Application** | Origin database (FB Messenger, SMS, WhatsApp, etc.) | Identifies communication platform |
| **Map Address Text** | Reverse-geocoded coordinates from geo-tagged messages | Location evidence embedded in messages |
| **Server Message ID** | Server-assigned alphanumeric ID | Cross-reference against warrant returns from platforms |

**Defense-Critical:** The `Status` column's "Deleted" flag means Cellebrite carved this from SQLite unallocated space or WAL. The State may try to use "deleted" status to imply consciousness of guilt — counter with: system auto-deletion, app updates, storage management, or the fact that the content was mundane/exculpatory.

### 4.2 Call Logs

| Column | What It Contains | Defense Value |
|--------|-----------------|---------------|
| **Phone Number** | Routing number | Contact identification |
| **Direction** | Incoming / Outgoing / Missed / Rejected | Communication flow pattern |
| **Timestamp** | Call initiation time (UTC offset applied) | Timeline |
| **Duration** | Active call length in seconds | 0 + Missed = unanswered; 10-15s = voicemail; long = substantive |
| **Call Type** | Cellular / FaceTime / WhatsApp Audio / VoIP | Determines carrier vs. app — affects subpoena targets |
| **Device IPs / MAC Address** | Network config during VoIP calls | Location/network corroboration |

**Defense-Critical:** Cellebrite aggregates BOTH native cellular calls AND VoIP (WhatsApp, Skype, Viber, FaceTime) into a single Call Log. Prosecution may cite "call frequency" without distinguishing carrier from app calls — these come from different databases with different retention periods. SSRM/dual-source duplication is common.

### 4.3 Contacts

| Column | What It Contains | Defense Value |
|--------|-----------------|---------------|
| **Name** | User-assigned label | How defendant saved the contact |
| **Phone Numbers / Emails** | Multiple arrays consolidated | Full contact profile |
| **Source** | SIM Card / iCloud / Google Contacts / WhatsApp / local | Manual curation vs. auto-sync |
| **Deleted State** | Intact / Deleted / Unknown | Contact relationship destruction analysis |

**Defense-Critical:** The `Source` field reveals whether a contact was manually added (intentional relationship) or auto-synced (passive). A contact appearing only in WhatsApp's local directory was likely auto-created when the other party joined WhatsApp — not evidence of a deliberate relationship.

### 4.4 Geospatial / Location

| Column | What It Contains | Defense Value |
|--------|-----------------|---------------|
| **Latitude / Longitude** | Exact coordinates | Alibi / proximity analysis |
| **Elevation** | Height data | Floor-level specificity in buildings |
| **Timestamp** | Temporal anchor for location | Links place to time |
| **Category / Description** | Source: Wi-Fi / geo-tagged media / mapping app / cell tower | Precision and reliability assessment |
| **Confidence / Precision** | Accuracy radius | Low = cell tower triangulation (km); High = GPS/Wi-Fi (meters) |

**Defense-Critical:** The `Confidence/Precision` column is essential. A "location" with low precision is a cell tower triangulation covering potentially miles — NOT precise placement. The State frequently overstates location precision. Always check this column and hand off to dw-cell-site-geolocation-auditor.

### 4.5 Web Browser

| Column | What It Contains | Defense Value |
|--------|-----------------|---------------|
| **URL / Domain** | Specific URL or domain accessed | Browsing behavior |
| **Visit Count** | Repetitive access frequency | Sustained interest indicator |
| **Search Term** | Plaintext search query | Intent evidence — but context required |
| **Account Identity** | Authenticated usernames/emails/handles | Device user identification |

### 4.6 File Systems / Data Files

| Column | What It Contains | Defense Value |
|--------|-----------------|---------------|
| **Icon** | File type indicator; **red cross = deleted** | Deletion status |
| **Name** | Filename | File identification |
| **Path** | Full directory path | App origin identification |
| **Size** | File size | Content type estimation |
| **Created** | File creation timestamp | Provenance |
| **Modified** | Last modification timestamp | Activity timeline |
| **Accessed** | Last access timestamp | Usage evidence |

---

## 5. Advanced Analytics / Insights Dashboard

Cellebrite's built-in analytics may have already flagged items. Review what the tool auto-detected — and more importantly, what it DIDN'T flag.

### 5.1 Installed Applications Analysis

Cellebrite categorizes apps into ~30 risk topologies. Key categories for defense:

| App Category | Defense Significance |
|-------------|---------------------|
| **GPS Spoofing apps** | If absent → location data more reliable for alibi |
| **Hidden Vault / Calculator apps** | If absent → no concealment tools |
| **Clean/Wipe utilities** | If absent → no evidence destruction tools |
| **Secure Ephemeral Messaging** (Signal, Wickr, etc.) | If absent → defendant used record-preserving platforms |
| **VPN applications** | If absent → no anonymization tools |

**Defense Rule:** The ABSENCE of high-risk app categories is powerful defense evidence. Report it in Section 5 (File Systems & App Inventory) using the "Apps NOT Found (Defense Favorable)" format.

### 5.2 Media Classification (ML-Based)

Cellebrite's ML engine auto-classifies images/videos into:
- Weapons, Drugs, Nudity, Suspected CSA, Documents, Financial/Credit Cards, Vehicles, Faces, Tattoos, Handwriting

**Confidence Score:** 0-100% slider. Results below threshold are excluded.

**Defense Implications:**
- If ML classification found ZERO CSA/exploitation material → **powerful defense evidence in sex offense cases**
- ML has false positives — adult content between consenting adults flagged as "Nudity" is NOT CSA
- The confidence score threshold matters — ask what threshold was used
- Video classification marks specific frames — check if flagged frames are out of context

### 5.3 Cryptocurrency

Scans for wallet addresses, private keys, transaction hashes. Can enrich via Chainalysis.

### 5.4 Project Analytics / Communication Mapping

Evaluates communication volume between target device and all parties. Identifies top contacts by channel (SMS vs. WhatsApp vs. email).

**Defense Use:** This is the raw data for Dashboard Section 1.2 (Top 5 Messaging Parties). If Cellebrite already generated this mapping, use it as the authoritative source.

---

## 6. Timeline and Map Features

### Timeline View
- Strips categorical boundaries — ALL events on a single chronological axis
- Graphical timebar shows data density (activity spikes visible)
- Filterable by Type, Timestamp, Party, Description, Source
- **Key technique:** Filter to show Device Events (screen unlock, charger insertion, reboot) + Communications simultaneously → proves physical interaction with device at time of message

### Map View
- Road View, Aerial View, or offline mode (TCP port 3000)
- **Wi-Fi BSSID → physical location enrichment**: Translates saved Wi-Fi access points to coordinates via geocoding databases
- **Cell Tower ID → location enrichment**: Converts tower IDs to coordinates
- Click any pin → jumps to corresponding tabular record

**Defense Implication:** Cellebrite's BSSID/cell tower geolocation is approximate. The enrichment databases may be outdated. Always verify with carrier records and hand off to dw-cell-site-geolocation-auditor.

---

## 7. Report Generation Capabilities

Understanding how Cellebrite generates reports helps identify what the State chose to include — and exclude.

### Export Formats
| Format | Use Case |
|--------|----------|
| **PDF** | Immutable legal discovery, court presentations |
| **HTML** | Interactive browser-based review with tabbed navigation |
| **Excel / XML** | Programmatic analysis, eDiscovery ingestion |
| **KML** | Google Earth geospatial plotting |
| **EML** | Email client review |
| **UFDR** | Full Cellebrite Reader bundle (can include Reader executable) |

### Key Export Configuration Flags

| Setting | What It Does | Defense Significance |
|---------|-------------|---------------------|
| **SHA-256 / MD5 Hashing** | Embeds cryptographic hash for each file | Chain of custody verification — if not enabled, challenge integrity |
| **Conversation Bubbles** | Renders chats in bubble view vs. flat table | Bubble view = jury-friendly but may decontextualize |
| **Redactions** | Auto-redacts attachments/thumbnails | Standard for CSAM — verify no exculpatory content was redacted |
| **Include Merged Items** | Consolidates cross-source data into unified views | May merge data from different reliability levels |
| **Translations** | SDL auto-translation of foreign language content | Check translation accuracy — machine translation errors |
| **Full Size Images** | Includes full-resolution images vs. thumbnails | Thumbnails may hide exculpatory detail |
| **Include Cellebrite Reader** | Embeds Reader executable with UFDR | Defense should request this if not provided |

### Selective Reporting Detection

**CRITICAL:** Cellebrite allows examiners to generate reports from TAGGED subsets of data, not the full extraction. If the State provides a Cellebrite report:

1. Check if record counts match the extraction summary totals
2. Look for tag-filtered exports (only tagged items included)
3. Compare categories present vs. categories listed on Welcome Tab
4. Missing categories = potential selective reporting → **Brady/Giglio handoff**

---

## 8. The File Info Pane — Media Forensics

When examining media, the File Info pane reveals:
- MAC timestamps (Created / Modified / Accessed)
- **Capturing Device** field — heuristic analysis of EXIF data, lens signatures, and directory paths (DCIM folder)
- Determines: **natively captured by THIS device** vs. **downloaded/received from external source**

**Defense Significance:** In exploitation cases, the Capturing Device field distinguishes between:
- **Creation** — image taken by suspect's camera (strongest prosecution evidence)
- **Possession/Receipt** — image downloaded or received (weaker, may be unsolicited)

This distinction maps directly to Dashboard Section 1.5 (Last 10 Sent/Received Media Classifications).

---

## 9. User Dictionaries — Predictive Text Cache

The operating system's predictive text learns custom words typed by the user. Cellebrite extracts this cache.

**Defense Implications:**
- Presence of a word in the dictionary does NOT prove it was typed in a criminal context
- Dictionary learns from ALL typing — including search queries, notes, messages, even form fields
- Shared device = multiple users' vocabulary merged
- Factory reset clears the dictionary — absence ≠ consciousness of guilt

---

## 10. Defense Workflow Integration

### When to Reference This Guide

| Skill Step | What to Check Here |
|-----------|-------------------|
| Step 1 (Info Gathering) | Section 1: Extraction type limits |
| Step 2 (Data Inventory) | Section 3: Expected categories vs. what's present; Section 7: Selective reporting detection |
| Step 3 (Critical Window) | Section 4: Column headers for each data category; Section 2: UTC offset verification |
| Step 3.5 (Baseline) | Section 5.4: Communication mapping for contact frequency |
| Step 5 (Handoffs) | Section 6: Map/timeline features for cell-site auditor |
| Step 6 (Report) | Section 3: Navigation hierarchy maps to report sections |

### Dashboard Section Mapping

| Dashboard Subsection | Cellebrite Source |
|---------------------|------------------|
| 1.1 Device Information | Welcome Tab → Extraction Summary |
| 1.2 Top 5 Messaging Parties | Project Analytics + Messaging Items record counts |
| 1.3 Top 10 Most Visited Locations | GPS Information → Fixes + Locations (sorted by frequency) |
| 1.4 Last 10 Calls | Call Log (sorted by timestamp, descending) |
| 1.5 Last 10 Sent/Received Media | Media Items + File Info pane (Capturing Device field) |
| 1.6 Top 5 Messaging Apps | Messaging Items → subtab record counts by Source/Application |
| 1.7 Last 10 Searches | Web Browser Items → History (filter: Search Term not null) |
| 1.8 Top 10 Bluetooth Connections | Device Information → Bluetooth Pairings |

---

*This reference is loaded by the dw-forensic-dump-analyzer skill when working with Cellebrite extraction data. It maps the Cellebrite Reader interface to the defense analysis workflow and report template sections.*
