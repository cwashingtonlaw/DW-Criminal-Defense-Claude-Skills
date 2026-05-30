# Defense Intelligence Report — Template & Formatting Guide

This reference provides structure and formatting instructions for both the **Full Report** and **Quick Brief** output modes. Use the docx SKILL.md for technical document creation.

**CRITICAL — MANDATORY SECTIONS:** The Full Report has 29 numbered sections (Section 29 is Appendices). Every section is MANDATORY unless explicitly marked conditional. Do NOT skip sections, even if a section would be brief. An empty or placeholder section (e.g., "No cross-reference documents provided") is better than a missing section — it shows the attorney the analysis was considered and the gap is intentional, not an oversight.

**Report Consistency Rule:** Two analysts running this skill on the same data MUST produce reports with the same section structure and the same finding categories. The specific findings may differ in emphasis, but the framework must be identical. This template is the enforcement mechanism.

---

## Report Mode Selection

| Analysis Scope | Mode | Sections |
|---------------|------|----------|
| Full extraction, 3+ categories, comprehensive | **Full Report** | All 29 sections (see below) |
| 1–2 categories, targeted scope, time-pressured | **Quick Brief** | 4 sections only (see below) |

---

## Quick Brief Template

Use for small-scope or targeted analysis. No cover page, no appendices.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUICK BRIEF — PHONE DATA ANALYSIS
Daniels & Washington | CONFIDENTIAL — ATTORNEY WORK PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Case:       [Case Name / Docket No.]
Phone:      [Owner / Make / Model]
Data:       [Categories analyzed, record count, date range]
Auth:       [Examiner / Tool / Hash status — one line]
Date:       [Report generation date]

━━━━━ EXECUTIVE SUMMARY ━━━━━
[1-2 paragraphs: what was analyzed, key findings, next steps]

━━━━━ FINDINGS ━━━━━
[Numbered findings with:
 - Description
 - Source file and row/line reference
 - Strength: STRONG / MODERATE / CONTEXTUAL
 - Suggested use (cross-exam, motion, argument)]

━━━━━ ADVERSE DATA ━━━━━
[Data that hurts the defense:
 - What it shows
 - Damage level
 - Mitigation strategy]

━━━━━ ACTION ITEMS ━━━━━
[Prioritized: motions, investigation leads, expert needs,
 additional data to request, expand to full analysis?]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Naming convention (Quick Brief):**
```
[LastName]_[CaseNo]_PhoneDump_QuickBrief_[Date].docx
```

---

## Full Report Template

### Document Properties

- **Title:** Cell Phone Data — Defense Intelligence Report
- **Subtitle:** [Case Name / Docket No.]
- **Author:** Daniels & Washington
- **Classification:** CONFIDENTIAL — ATTORNEY WORK PRODUCT
- **Font:** Times New Roman or similar professional serif
- **Margins:** 1 inch all sides
- **Line Spacing:** 1.15 for body text; single for tables
- **Page Numbers:** Bottom center, format "Page X of Y"

---

## Header / Footer

**Header (every page):**
```
CONFIDENTIAL — ATTORNEY WORK PRODUCT
Daniels & Washington | [Case Name] | [Docket No.]
```

**Footer (every page):**
```
Cell Phone Data — Defense Intelligence Report | Page X of Y
Generated [Date] | AI-Assisted Analysis — Review Required
```

---

## Cover Page

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        CELL PHONE DATA
        DEFENSE INTELLIGENCE REPORT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        [Case Name]
        [Docket / Case Number]
        [Court]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        Phone Owner:     [Name]
        Device:          [Make / Model / OS Version]
        Phone Number:    [Number]
        Extraction Type: [Logical / FFS / Physical]
        Extraction Tool: [Name / Version]
        Extraction Date: [Date]
        Data Date Range: [Earliest record] to [Latest record]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        Prepared by:     Daniels & Washington
        Analysis Date:   [Date]
        Classification:  CONFIDENTIAL — ATTORNEY WORK PRODUCT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOTICE: This report was generated using AI-assisted analysis
and must be reviewed by the supervising attorney before use in
any legal proceeding. All findings should be verified against
the source data. This document is protected by attorney-client
privilege and the work product doctrine.
```

---

## Full Report Section Checklist

Before finalizing ANY Full Report, verify every section is present. The Full Report has 29 numbered sections plus appendices.

- [ ] Cover Page
- [ ] Section 1: Dashboard (case-at-a-glance)
- [ ] Section 2: Executive Summary
- [ ] Section 3: Charges & Exposure
- [ ] Section 4: Extraction Authentication Chain
- [ ] Section 5: Data Inventory & Completeness Assessment
- [ ] Section 6: File Systems & App Inventory
- [ ] Section 7: Top 10 Key Contacts Identified
- [ ] Section 8: Comprehensive Timeline
- [ ] Section 9: Critical Timeline (minute-by-minute crime window)
- [ ] Section 10: Pattern of Life Baseline
- [ ] Section 11: Critical Window Analysis (findings from crime window)
- [ ] Section 12: Key Date Analysis (other significant dates)
- [ ] Section 13: Analyzed Data (category-by-category deep dive)
- [ ] Section 14: Locations (GPS/Wi-Fi/cell site analysis)
- [ ] Section 15: Defense-Favorable Findings (organized by lens)
- [ ] Section 16: Adverse Findings (immediately after defense-favorable)
- [ ] Section 17: Prosecution Vulnerabilities
- [ ] Section 18: Gaps (timeline, data, and evidentiary)
- [ ] Section 19: Missing Data Analysis
- [ ] Section 20: Insights (cross-cutting analytical observations)
- [ ] Section 21: Tags (evidence classification index)
- [ ] Section 22: Eight-Lens Defense Analysis Matrix (summary table)
- [ ] Section 23: Cross-Reference Findings (conditional — placeholder if none)
- [ ] Section 24: Companion Skill Handoffs
- [ ] Section 25: Defense Action Items
- [ ] Section 26: Exhibit-Ready Extracts
- [ ] Section 27: Evidence Integrity
- [ ] Section 28: Reports (companion analysis requests)
- [ ] Section 29: Appendices

---

## Section Structure

### DASHBOARD (Section 1)

**MANDATORY.** The dashboard is the first analytical page(s) the attorney sees. It provides the entire case posture and device intelligence in a rapid-reference visual summary. Think of it as the "control panel" — the attorney should be able to brief a colleague on the phone dump in 60 seconds by scanning this section. Every subsection below is MANDATORY.

---

**1.1 Device Information**

| Field | Value |
|-------|-------|
| Phone Owner | [Full name] |
| Device | [Make / Model / OS Version] |
| Phone Number | [Number] |
| IMEI/MEID | [Number if available] |
| Serial Number | [if available] |
| Storage | [Total / Used / Free if available] |
| Extraction Type | [Logical / FFS / Physical / Chip-off] |
| Extraction Tool | [Name / Version] |
| Extraction Date | [Date] |
| Data Date Range | [Earliest record] to [Latest record] |
| Total Records | [N] across [N] categories |
| Hash Verified | [Yes — SHA256: xxxx / No / Unknown] |

---

**1.2 Top 5 Messaging Parties**

Ranked by total message volume across ALL messaging platforms (SMS, MMS, iMessage, FB Messenger, RCS, WhatsApp, etc.).

| Rank | Contact | Platform(s) | Messages Sent | Messages Received | Total | Relationship | Defense Relevance |
|------|---------|-------------|--------------|-------------------|-------|-------------|------------------|
| 1 | [Name/Number] | [SMS, FB Messenger] | [N] | [N] | [N] | [Relationship] | [Brief note] |
| 2 | [Name/Number] | [Platform] | [N] | [N] | [N] | [Relationship] | [Brief note] |
| 3 | [Name/Number] | [Platform] | [N] | [N] | [N] | [Relationship] | [Brief note] |
| 4 | [Name/Number] | [Platform] | [N] | [N] | [N] | [Relationship] | [Brief note] |
| 5 | [Name/Number] | [Platform] | [N] | [N] | [N] | [Relationship] | [Brief note] |

**Note:** Where the victim/complainant ranks in this table is analytically significant — a high rank suggests normalized ongoing communication; a low rank or absence undermines escalation narratives.

---

**1.3 Top 10 Most Visited Locations**

Ranked by frequency of GPS/Wi-Fi/cell site pings. Resolve coordinates to human-readable addresses where possible.

| Rank | Location | Address/Description | Visits | Date Range | Coordinates | Defense Relevance |
|------|----------|-------------------|--------|-----------|------------|------------------|
| 1 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [Home / Work / etc.] |
| 2 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |
| 3 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |
| 4 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |
| 5 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |
| 6 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |
| 7 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |
| 8 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |
| 9 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |
| 10 | [Name/label] | [Address] | [N] | [range] | [lat, lon] | [note] |

**Flag:** Any locations near schools, daycares, playgrounds, or child-related venues MUST be flagged with `[PROXIMITY ALERT]` and assessed for defense impact.

---

**1.4 Last 10 Calls**

The 10 most recent calls on the device at time of extraction (or arrest). Provides immediate snapshot of who the defendant was communicating with.

| # | Date/Time | Direction | Contact | Number | Duration | Type | Notes |
|---|-----------|-----------|---------|--------|----------|------|-------|
| 1 | [datetime] | [In/Out/Missed] | [Name] | [Number] | [mm:ss] | [Native/FB/WhatsApp] | [note] |
| 2 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |
| 3 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |
| 4 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |
| 5 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |
| 6 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |
| 7 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |
| 8 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |
| 9 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |
| 10 | [datetime] | [direction] | [Name] | [Number] | [mm:ss] | [type] | [note] |

---

**1.5 Last 10 Sent/Received Media — Classifications**

The 10 most recent media attachments (photos, videos, audio) sent or received, classified by content type. This immediately reveals whether the device contains concerning media.

| # | Date/Time | Direction | Contact | Media Type | Duration | Classification | File Size | Source App | Defense Note |
|---|-----------|-----------|---------|-----------|----------|---------------|-----------|-----------|-------------|
| 1 | [datetime] | [Sent/Rcvd] | [Name] | [Photo/Video/Audio] | [N/A or mm:ss] | [Family/Social/Meme/Adult/Concerning/System] | [size] | [SMS/FB/etc.] | [note] |
| 2 | [datetime] | [direction] | [Name] | [type] | [duration] | [classification] | [size] | [app] | [note] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Media Classification Key:**
- **Family** — Photos/videos of family activities, children (normal parenting context)
- **Social** — Memes, social media shares, group chat images
- **Adult** — Adult content between consenting adults (assess 404(b) risk)
- **Concerning** — Any media requiring immediate attorney attention (flag with `[IMMEDIATE REVIEW]`)
- **System** — Automated media (app icons, notification images, cached thumbnails)

**CRITICAL:** If ALL 10 media items are classified as Family/Social/System, state: **"ZERO concerning media in most recent transmissions — DEFENSE FAVORABLE."**

---

**1.10 Video Inventory Summary**

Quick-reference dashboard of ALL video files on the device, classified by origin and flagged for critical window overlap. This panel lets the attorney immediately see whether any video recordings are alibi-relevant.

| # | Date/Time | Duration | Type | Has GPS | Has Audio | Resolution | In Critical Window | Defense Note |
|---|-----------|----------|------|---------|-----------|------------|-------------------|-------------|
| 1 | [datetime] | [mm:ss] | [Camera/Screen Rec/Received/Chat/Social/Live Photo] | [Y/N] | [Y/N] | [WxH] | [YES/no] | [note] |
| 2 | [datetime] | [duration] | [type] | [Y/N] | [Y/N] | [res] | [YES/no] | [note] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Video Totals:**
- Camera recordings: [N] ([total duration])
- Screen recordings: [N] ([total duration])
- Received videos: [N]
- Chat media videos: [N]
- Videos in critical window: [N] ([total duration]) — **[ALIBI POTENTIAL if > 0]**

**CRITICAL:** Any video recorded during the critical window gets flagged with `[CRITICAL WINDOW — ATTORNEY REVIEW]`. A long-duration camera recording during the crime window is among the strongest alibi evidence possible — it proves the phone owner was physically holding their phone, at a GPS-verified location, for a known duration.

---

**1.11 Financial App Transaction Summary**

Quick snapshot of payment app activity if financial apps are present on the device. Transaction timestamps independently verify phone activity and can establish location via merchant data.

| App | Total Txns | Date Range | Avg Txn Amount | Critical Window Txns | Defense Note |
|-----|-----------|-----------|---------------|---------------------|-------------|
| Cash App | [N] | [range] | [$X] | [N] | [note] |
| Venmo | [N] | [range] | [$X] | [N] | [note] |
| Zelle | [N] | [range] | [$X] | [N] | [note] |
| Apple Pay | [N] | [range] | [$X] | [N] | [note] |

**If financial app data is NOT present:** State: **"Financial app data: NOT AVAILABLE — [not extracted / not present / app not installed]."**

---

**1.6 Top 5 Messaging Apps**

Ranked by total message count across all contacts.

| Rank | App | Messages | % of Total | Active Contacts | Date Range | Encryption |
|------|-----|----------|-----------|----------------|-----------|-----------|
| 1 | [App name] | [N] | [N%] | [N] | [range] | [None/E2E/Transit] |
| 2 | [App name] | [N] | [N%] | [N] | [range] | [encryption] |
| 3 | [App name] | [N] | [N%] | [N] | [range] | [encryption] |
| 4 | [App name] | [N] | [N%] | [N] | [range] | [encryption] |
| 5 | [App name] | [N] | [N%] | [N] | [range] | [encryption] |

**Defense Value:** If the defendant predominantly uses non-encrypted, record-preserving platforms (SMS, FB Messenger, RCS), state: **"Defendant's messaging profile is inconsistent with concealment — [N%] of communications on platforms that preserve full records."**

---

**1.7 Last 10 Searches**

The 10 most recent user-initiated searches (browser + in-app), excluding system/automated queries. Each search is classified for defense relevance.

| # | Date/Time | Search Term | Platform | Classification | Defense Note |
|---|-----------|------------|----------|---------------|-------------|
| 1 | [datetime] | [search query] | [Google/Safari/Chrome/YouTube/etc.] | [Mundane/Employment/Legal/Adult/Concerning] | [note] |
| 2 | [datetime] | [search query] | [platform] | [classification] | [note] |
| 3 | [datetime] | [search query] | [platform] | [classification] | [note] |
| 4 | [datetime] | [search query] | [platform] | [classification] | [note] |
| 5 | [datetime] | [search query] | [platform] | [classification] | [note] |
| 6 | [datetime] | [search query] | [platform] | [classification] | [note] |
| 7 | [datetime] | [search query] | [platform] | [classification] | [note] |
| 8 | [datetime] | [search query] | [platform] | [classification] | [note] |
| 9 | [datetime] | [search query] | [platform] | [classification] | [note] |
| 10 | [datetime] | [search query] | [platform] | [classification] | [note] |

**Search Classification Key:**
- **Mundane** — Weather, directions, shopping, entertainment, how-to
- **Employment** — Job searches, resume help, salary lookups, work-related
- **Legal** — Inmate lookups, attorney searches, case law, legal terms
- **Adult** — Adult content searches (assess 404(b) risk)
- **Concerning** — Searches requiring immediate attorney attention (flag with `[IMMEDIATE REVIEW]`)

**CRITICAL:** Distinguish user-initiated searches from system-generated queries (Gmail HTTPS pings, Taboola ad network parameters, app telemetry). System queries MUST be excluded from this table but noted in Section 13.3.

---

**1.8 Top 10 Bluetooth Connections**

Ranked by connection frequency. Bluetooth pairings reveal the defendant's daily environment — vehicles, headphones, smart home devices, and other people's devices.

| Rank | Device Name | Device Type | MAC Address | First Seen | Last Seen | Connections | Defense Relevance |
|------|------------|------------|-------------|-----------|----------|------------|------------------|
| 1 | [Name] | [Car/Headphones/Speaker/Watch/TV/Unknown] | [MAC] | [date] | [date] | [N] | [note] |
| 2 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |
| 3 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |
| 4 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |
| 5 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |
| 6 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |
| 7 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |
| 8 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |
| 9 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |
| 10 | [Name] | [type] | [MAC] | [date] | [date] | [N] | [note] |

**Defense Value:** Bluetooth pairings corroborate location and routine (e.g., daily car connection = commute pattern, work Bluetooth speaker = employment verification). Vehicle Bluetooth pairings may provide alibi evidence via infotainment system subpoena.

**Note:** If Bluetooth data is unavailable or not extracted, state: **"Bluetooth connection data: NOT AVAILABLE in this extraction — [reason if known]."**

---

**1.9 Dashboard Summary Assessment**

| Metric | Value | Assessment |
|--------|-------|-----------|
| Total Records Analyzed | [N] | — |
| Defense-Favorable Findings | [N] ([N] STRONG, [N] MODERATE, [N] CONTEXTUAL) | [Overall strength] |
| Adverse Data Points | [N] ([N] HIGH, [N] MODERATE, [N] LOW damage) | [Overall risk] |
| Data Completeness | [N/N categories complete] | [Complete / Gaps identified] |
| Incriminating Content Found | ZERO / [describe] | [DEFENSE FAVORABLE / concern] |
| CSAM/Predatory Content Found | ZERO / [describe] | [DEFENSE FAVORABLE / concern] |
| Encrypted/Hidden Apps Found | NONE / [list] | [DEFENSE FAVORABLE / concern] |
| Suspicious Location Patterns | NONE / [describe] | [DEFENSE FAVORABLE / concern] |
| Deleted Data (incriminating) | NONE / [describe] | [DEFENSE FAVORABLE / concern] |

**Top 5 Findings (quick reference):**
1. [Finding ID]: [One-line summary] — [STRONG]
2. [Finding ID]: [One-line summary] — [STRONG]
3. [Finding ID]: [One-line summary] — [STRONG]
4. [Finding ID]: [One-line summary] — [MODERATE]
5. [Finding ID]: [One-line summary] — [MODERATE]

**Top 3 Risks:**
1. [Adverse ID]: [One-line risk] — [HIGH DAMAGE]
2. [Adverse ID]: [One-line risk] — [MODERATE DAMAGE]
3. [Adverse ID]: [One-line risk] — [MODERATE DAMAGE]

**Immediate Actions Required:**
1. [Most urgent action item]
2. [Second most urgent]
3. [Third most urgent]

**Why this section matters:** Attorneys reviewing phone dump reports often have limited time. The dashboard ensures the most critical intelligence is consumed even if the attorney reads nothing else. The 8 dashboard panels (device info, messaging parties, locations, calls, media, apps, searches, bluetooth) give a complete device profile at a glance — it also serves as a briefing sheet for meetings with the client, co-counsel, or expert witnesses.

### EXECUTIVE SUMMARY (Section 2)

**MANDATORY.** Two to three paragraphs covering:
- What data was analyzed (categories, volume, date range)
- **Quantified findings summary** (e.g., "33 defense-favorable findings (14 STRONG, 11 MODERATE, 8 CONTEXTUAL) against 17 adverse data points") — always include the count and strength breakdown
- The most significant defense-favorable findings (top 5-6, each as a bold numbered paragraph with label and one-sentence description)
- **Defense theory stated explicitly** (e.g., "Defense Theory: Fabrication orchestrated to break up April (mother) from Banks")
- Adverse data summary (1 paragraph identifying the most damaging items and their mitigation posture)
- **Immediate action items** (numbered list, 3-5 highest priority)

Write this section LAST — after completing all analysis — but place it FIRST in the document. The attorney reads this first and may not read further if the case is straightforward.

**Format the top findings as bold labeled paragraphs:**
```
**(1) Zero incriminating content:** [one-sentence summary with key stats]
**(2) Real-time denial thread:** [one-sentence summary]
**(3) [Next most important finding]:** [summary]
...
```

### CHARGES & EXPOSURE (Section 3)

**MANDATORY.** Complete charge table listing ALL counts.


| Count | Charge | Statute | Victim | Exposure |
|-------|--------|---------|--------|----------|
| 1 | [Charge name] | [Statute citation] | [Victim initials, gender, DOB] | [Sentence range] |
| ... | ... | ... | ... | ... |

**Defense Theory:** State the defense theory in one sentence below the charge table.

**Why this section matters:** The charge table ensures the analyst (and attorney) never lose sight of what's at stake. It also ensures findings are mapped to specific counts — a finding that helps on Count 1 but is irrelevant to Count 3 should be noted as such.

### EXTRACTION AUTHENTICATION CHAIN (Section 4)

**MANDATORY.** This section establishes the forensic foundation for every finding in the report. It answers the threshold question: can we trust this data? Every piece of evidence derived from this extraction inherits this authentication chain unless a per-finding exception is noted. Elevating this to its own section (rather than burying it in a subsection) ensures the attorney sees it immediately and can assess whether the extraction itself is challengeable before reading any findings.

**4.1 Extraction Summary:**

```
EXTRACTION AUTHENTICATION CHAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Examiner:         [Full name, agency, credentials, lab report number]
Agency/Lab:       [e.g., CPSO Digital Forensics Unit / FBI RCFL / Private lab]
Tool/Version:     [Cellebrite UFED vX.X / Physical Analyzer vX.X / GrayKey vX.X]
Extraction Type:  [Logical / Full File System / Physical / Chip-off / Cloud]
Extraction Date:  [Date and time]
Hash Verified:    [Yes — SHA256: full hash value / No / Unknown]
Chain of Custody: [Documented — continuous / Gap: specify dates and custodians]
Lab Report:       [Report number and date / Not provided]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**4.2 Extraction Type Limitations:**

| Extraction Type | What It CAN Access | What It CANNOT Access | Impact on This Analysis |
|----------------|-------------------|---------------------|----------------------|
| Logical | User-accessible data, app exports | Deleted data, system databases, unallocated space | [assessment] |
| Full File System | All file system data, app databases | Unallocated space, some encrypted containers | [assessment] |
| Physical | Everything including unallocated space | Hardware-encrypted containers without passcode | [assessment] |

**4.3 Authentication Challenges:**
- [ ] Hash verification: [Verified / Not verified — significance]
- [ ] Chain of custody gaps: [None / describe each gap with dates]
- [ ] Multiple extractions: [Single extraction / Multiple — note tool/date differences]
- [ ] Time zone verification: [Device timezone confirmed / Discrepancy noted]
- [ ] Selective extraction indicators: [None / describe — flag for Brady/Giglio]

**4.4 Per-Finding Authentication Exceptions:**

Most findings inherit the extraction-level auth above. Only note exceptions here — findings from a different extraction, WAL recovery, cloud data with a separate chain, or data with weaker authentication.

| Finding | Exception | Additional Foundation Needed |
|---------|-----------|---------------------------|
| [Finding ref] | [What's different] | [La. C.E. Art. 901(B)(9) requirement] |

**Why this is a standalone section:** In prior report versions, the auth chain was buried in a subsection and attorneys sometimes missed critical chain-of-custody gaps. A compromised extraction chain undermines every finding in the report — the attorney needs to assess this independently before evaluating any substantive findings.

---

### DATA INVENTORY & COMPLETENESS ASSESSMENT (Section 5)

**MANDATORY.** This section establishes the universe of data. Both the attorney and any expert witness need this to understand what was analyzed and what's missing.

**5.1 Data Inventory Table:**

| Category | File | Format | Records | Date Range | Unique | Completeness |
|----------|------|--------|---------|-----------|--------|-------------|
| Messages | [filename] | CSV | [N] | [range] | [N] | Complete / Partial |
| Call Logs | [filename] | CSV | [N] | [range] | [N] | PARTIAL — [explain] |
| Searches | [filename] | CSV | [N] | [range] | [N]* | Complete (*[noise note]) |
| Browsing | [filename] | CSV | [N] | [range] | [N]* | Complete (*[noise note]) |
| Contacts | [filename] | CSV | [N] | N/A | — | Complete |
| Device Events | [filename] | CSV | [N] | [range or "NO TIMESTAMPS"] | — | [assessment] |
| App Usage / Screen Time | [filename] | CSV | [N] | [range] | — | [assessment] |
| Cookies | [filename] | CSV | [N] | [range or "NO TIMESTAMPS"] | — | Complete |
| Locations | [filename] | CSV | [N] | [range] | — | [assessment] |
| Photos | [filename] | CSV/EXIF | [N] | [range] | — | [assessment] |
| Videos | [N files] | MP4/MOV/etc. | [N] | [range] | — | [assessment] |
| Financial | [filename] | CSV | [N] | [range] | — | [assessment] |
| Health/Fitness | [filename] | XML/CSV | [N] | [range] | — | [assessment] |
| Voice Memos | [N files] | M4A/WAV | [N] | [range] | — | [assessment] |
| Notes | [filename] | DB/CSV | [N] | [range] | — | [assessment] |
| Calendar | [filename] | DB/CSV | [N] | [range] | — | [assessment] |
| Email | [filename] | DB/CSV | [N] | [range] | — | [assessment] |

**CRITICAL:** Include ALL data categories, even those marked "NOT ANALYZED" or "GUTTED." The attorney needs to know what exists, what was analyzed, and what was skipped (with the reason).

**5.2 Extraction Authentication:**

Reference Section 4 (Extraction Authentication Chain) for the full auth chain. This subsection notes only data-category-specific authentication issues.

**5.3 Deduplication Summary:**
- Messages: [N] raw → [N] unique ([N]% duplicates). Method: [describe composite key].
- Calls: [N] raw → [N] unique ([N]% duplicates). Method: [describe]. Note any duplicate database artifacts (e.g., SSRM Heating Log duplicate records with timezone offset).

**5.4 Top Contacts by Message Volume:**

| Contact | Messages | Relationship |
|---------|----------|-------------|
| [Name/Alias] | [N] | [Relationship to defendant] |
| ... | ... | ... |

**Why this subsection matters:** Top contacts establish the defendant's social world. The attorney needs to know who the primary relationships are at a glance — the volume table often reveals unexpected patterns (e.g., victim ranked #3 by volume vs. #1 would tell different stories).

**5.5 Completeness Gaps (CRITICAL flags):**

For each critical gap, use bold **CRITICAL:** or **NOTABLE:** prefix and explain:
- What data is missing or incomplete
- Why it matters to the defense
- What action to take (subpoena, re-extraction, expert recovery)

**Encrypted / Locked Container Inventory:**
| Container | App/Feature | Likely Contents | Extractable? | Defense Impact |
|-----------|------------|----------------|-------------|----------------|
| [e.g., Samsung Secure Folder] | [Knox/etc.] | [apps, photos, files] | [Y/N — why] | [Double-edged / favorable / adverse] |

**Selective Extraction Flags:**
If indicators of selective production were detected, document with specific evidence.

**Shared Device Indicators:**
If multi-user indicators were detected, document with specific evidence (e.g., Discord accounts belonging to household members logged in on defendant's device).

### FILE SYSTEMS & APP INVENTORY (Section 6)

**MANDATORY.** This section catalogs the device's software ecosystem — what apps are installed, what's been deleted, what encrypted containers exist, and what the app profile tells us about the device owner.

**6.1 Installed Apps Summary:**

| Category | Apps | Count | Defense Relevance |
|----------|------|-------|------------------|
| Messaging | [SMS, FB Messenger, Instagram DM, etc.] | [N] | [Standard platforms — preserves records] |
| Social Media | [Facebook, Instagram, TikTok, etc.] | [N] | [Normal social media use] |
| Dating | [list or NONE] | [N] | [Adult apps — 404(b) risk if present] |
| Encrypted/Privacy | [Signal, Telegram, WhatsApp, Snapchat, VPN, etc. — or NONE] | [N] | [CRITICAL — absence is defense favorable] |
| Financial | [CashApp, Venmo, banking apps, etc.] | [N] | [Transaction history potential] |
| Navigation/Location | [Google Maps, Life360, Waze, etc.] | [N] | [Location data sources] |
| Employment/Productivity | [Indeed, LinkedIn, email, etc.] | [N] | [Stable employment indicators] |
| Security/Monitoring | [Ring, Nest, Find My, etc.] | [N] | [Home security — subpoena potential] |
| Deleted Apps | [list with version numbers if available] | [N] | [Assess deletion significance] |

**6.2 Apps NOT Found (Defense Favorable):**

List apps commonly associated with exploitation/concealment that are ABSENT:
- Signal (encrypted messaging) — NOT FOUND
- Telegram — NOT FOUND
- WhatsApp — NOT FOUND
- Snapchat (auto-deleting) — NOT FOUND
- Kik (exploitation-associated) — NOT FOUND
- Any VPN apps — NOT FOUND
- Any vault/locker/hidden photo apps — NOT FOUND
- [Add others as relevant]

**Defense Value:** A person engaged in [charged conduct] would be expected to use [privacy/concealment tools]. Their complete absence demonstrates the defendant used standard, record-preserving platforms.

**6.3 Encrypted/Locked Containers:**

| Container | Feature | Extractable? | Contents Known? | Defense Impact |
|-----------|---------|-------------|----------------|---------------|
| [e.g., Samsung Secure Folder] | [Knox encryption] | [No — requires PIN] | [Unknown] | [Double-edged: State can argue concealment; Defense can argue default feature + incomplete LE examination] |

**6.4 Device Account Inventory:**
- Total accounts on device: [N]
- Stored passwords/credentials: [N]
- Notable accounts: [list accounts that reveal identity, aliases, or relationships]
- Alias accounts: [any secondary identities — assess defense impact]

### TOP 10 KEY CONTACTS IDENTIFIED (Section 7)

**MANDATORY.** This section consolidates the most important people identified across ALL data categories into a single reference. The attorney needs a quick-reference roster of who matters and why — not scattered across dashboard panels, message logs, call records, and financial transactions. Every contact listed here should be someone the defense needs to account for in trial preparation.

**7.1 Key Contacts Table:**

| # | Name / Identifier | Phone / Account | Relationship | Total Interactions | Platforms | Defense Relevance | Priority |
|---|------------------|----------------|--------------|-------------------|-----------|------------------|----------|
| 1 | [Name] | [Number/handle] | [Victim / Co-defendant / Witness / Family / Friend / Unknown] | [N msgs + N calls + N txns] | [SMS, FB, Cash App, etc.] | [Why this person matters to the defense] | CRITICAL / HIGH / MODERATE |
| 2 | [Name] | [Number/handle] | [Relationship] | [N] | [Platforms] | [Relevance] | [Priority] |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 10 | [Name] | [Number/handle] | [Relationship] | [N] | [Platforms] | [Relevance] | [Priority] |

**7.2 Contact Selection Criteria:**

Contacts are ranked by defense relevance, not just message volume. A person with 5 messages during the critical window may outrank someone with 5,000 routine messages. Selection factors:

- Communication during the critical window (highest weight)
- Relationship to victim or complainant
- Potential alibi witnesses (people who can verify the client's location/activity)
- Third-party suspect indicators
- Financial transaction counterparties during relevant period
- People the State will likely call as witnesses

**7.3 Contact Relationship Map:**

For complex cases (3+ key contacts with interconnections), include a brief narrative describing how the key contacts relate to each other and to the defendant. This helps the attorney visualize the social dynamics:

> *"[Defendant] communicated most frequently with [Contact 1 — girlfriend] and [Contact 2 — roommate]. [Contact 3 — victim] ranked [#X] by volume. [Contact 4] appears to be [Contact 3's] associate — they share a Venmo payment history. [Contact 5] is the only person who communicated with [Defendant] during the critical window."*

**7.4 Unidentified Numbers / Accounts:**

| # | Number / Account | Total Activity | Critical Window Activity | Identification Efforts | Priority |
|---|-----------------|---------------|------------------------|----------------------|----------|
| 1 | [Number] | [N interactions] | [N] | [Searched contacts, no match] | [HIGH if critical window activity] |

**Why this is a standalone section:** In prior reports, key contacts were scattered across the dashboard (Section 1.2), data inventory (Section 5.4), and individual findings. The attorney preparing for trial needs a single roster of the people who matter — with enough context to decide who to subpoena, who to investigate, and who to prepare cross-examination for.

---

### COMPREHENSIVE TIMELINE (Section 8)

**MANDATORY.** This is the master chronological reconstruction integrating ALL data sources. This section provides three timeline layers:

**8.1 Offense Window Timeline (Critical):**
The core timeline covering the alleged offense dates. Interleave ALL data sources:

| Date/Time | Source | Type | Direction | Content/Activity | Defense Value | Tag |
|-----------|--------|------|-----------|-----------------|--------------|-----|
| [datetime] | MSG | Text | [dir] | [content] | [significance] | [alibi/denial/fabrication/etc.] |
| [datetime] | BROWSE | Web | — | [URL/search] | [significance] | [tag] |
| [datetime] | CALL | Phone | [dir] | [duration, party] | [significance] | [tag] |
| [datetime] | GPS | Location | — | [coordinates, venue] | [significance] | [tag] |
| [datetime] | VIDEO | Recording | — | [filename, duration, GPS, has audio] | [significance] | [tag] |
| [datetime] | FINANCE | Transaction | [sent/rcvd] | [app, amount, recipient, note] | [significance] | [tag] |
| [datetime] | HEALTH | Biometric | — | [step count, heart rate, sleep] | [significance] | [tag] |
| [datetime] | DEVICE | System | — | [lock/unlock/camera/etc.] | [significance] | [tag] |

**8.2 Pre-Offense Timeline (Context):**
Key events from the baseline period that establish patterns, relationships, and context. Not every record — just the significant ones (e.g., fabrication indicators, relationship dynamics, third-party interference).

**8.3 Arrest Day / Disclosure Day Timeline (Critical):**
Minute-by-minute reconstruction of the arrest or disclosure day using the multi-source integration format from 8.1. This was the strongest section in the prior Banks report and MUST include:
- Messages (with full quoted text for key exchanges)
- Browsing activity interspersed chronologically
- Search queries interspersed chronologically
- Call data with durations
- Location data if available
- Device events if timestamped

**Timeline Narrative:** After each sub-timeline, include a prose narrative written as a defense-favorable account the attorney can adapt for motions or argument.

### CRITICAL TIMELINE (Section 9)

**MANDATORY.** This is the minute-by-minute reconstruction of the crime window — the single most important timeline in the report. While Section 8 provides the broad chronological overview across three layers, this section zooms in to the critical window (typically the alleged offense ± 2–4 hours) and reconstructs every available data point at maximum granularity.

The attorney uses this section to build the defense narrative of "what actually happened" during the window the State cares about. Every entry must be sourced, and every gap must be noted.

**9.1 Critical Window Definition:**

```
CRITICAL WINDOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alleged Offense:  [Description]
State's Claimed Time: [Date, Time]
Analysis Window:  [Start] to [End] (± [N] hours)
Time Zone:        [Zone — verified against device settings]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**9.2 Minute-by-Minute Reconstruction:**

Every data source is interleaved chronologically. Unlike the Comprehensive Timeline (Section 8) which summarizes, this section includes FULL content for messages, complete transaction details, exact GPS coordinates, and video metadata.

| Time | Source | Type | Detail | GPS/Location | Defense Value |
|------|--------|------|--------|-------------|--------------|
| [HH:MM:SS] | MSG | SMS Out | "[Full message text]" → [Recipient] | [coords if available] | [significance] |
| [HH:MM:SS] | VIDEO | Camera | [filename] — [duration] — audio: [Y/N] | [GPS coords] | **ALIBI — recording at [location] for [duration]** |
| [HH:MM:SS] | FINANCE | Cash App | $[amount] → [Recipient] — "[note]" | [merchant location if Apple Pay] | [significance] |
| [HH:MM:SS] | HEALTH | Steps | [N] steps in preceding 10 min — HR: [N] bpm | — | [Stationary/Active — significance] |
| [HH:MM:SS] | CALL | Incoming | [Contact] — [duration mm:ss] | — | [significance] |
| [HH:MM:SS] | BROWSE | Search | "[query]" on [platform] | — | [significance] |
| [HH:MM:SS] | DEVICE | Unlock | Screen unlocked | — | [User active] |
| [GAP] | — | — | **NO DATA: [HH:MM] to [HH:MM] ([N] minutes)** | — | **[Normal per baseline / Unusual — explain]** |

**9.3 Critical Window Gaps:**

Every gap longer than 15 minutes within the critical window gets its own entry:

| Gap Start | Gap End | Duration | Data Sources Silent | Baseline Comparison | Significance |
|-----------|---------|----------|-------------------|-------------------|-------------|
| [time] | [time] | [N min] | [All / MSG+CALL only / etc.] | [Normal sleep gap / Abnormal] | [Defense favorable / Concerning / Neutral] |

**9.4 Critical Window Narrative:**

1–2 paragraphs written as a defense-favorable account of the critical window, suitable for the attorney to adapt directly into a motion or opening statement. This narrative weaves together the timeline entries into a coherent story.

> *"Between [start] and [end], [Client]'s phone data shows continuous, verifiable activity inconsistent with the State's allegations. At [time], [Client] recorded a [N]-minute selfie video at [location — GPS verified], placing them [N] miles from the alleged crime scene. At [time], [Client] sent a Cash App payment to [Recipient] with the note '[note].' At [time], [Client]'s Apple Watch recorded [N] steps and a resting heart rate of [N] bpm, consistent with [sitting/walking] rather than [violent activity]. The only gap in activity — [time] to [time] — is consistent with [Client]'s baseline sleep pattern established in Section 10."*

**Why this is a standalone section:** The critical window is the battlefield. Having it as a dedicated, deep-dive section — separate from the broader Comprehensive Timeline — ensures the attorney can turn directly to this section and have everything they need for the most important period of the case in one place, at maximum detail.

---

### PATTERN OF LIFE BASELINE (Section 10)

**MANDATORY.** This section provides the statistical foundation that contextualizes every finding. Without it, the State can characterize normal behavior as "unusual" and the defense has no rebuttal.

**Baseline Period:** [date range, e.g., "February 1 – March 14, 2025 (42 days, pre-offense)"]
**Offense Window:** [date range, e.g., "March 15 – June 30, 2025 (108 days)"]
**Post-Offense:** [date range, e.g., "July 1–22, 2025 (22 days)"]

| Metric | Baseline | Offense Window | Change | Significance |
|--------|----------|---------------|--------|-------------|
| Messages/day | [N] | [N] | [▼/▲ N%] | [DEFENSE FAVORABLE / Normal / Artifact] |
| [Victim/key contact] msgs/day | [N] | [N] | [▼/▲ N%] | [assessment] |
| FB/app calls/day | [N] | [N] | [▼/▲ N%] | [assessment] |
| Native calls/day | [N or N/A*] | [N] | [change] | [assessment, note artifacts] |
| Late night msg % | [N%] | [N%] | [▼/▲] | [Pre-existing pattern / New / Decreased] |
| Weekend msgs/day | [N] | [N] | [▼/▲ N%] | [assessment] |
| Max silence gap | [N hr] | [N hr] | [Within range / Longer] | [Normal / Unusual] |
| Unique contacts | [N] | [N] | [▼/▲ N%] | [Life transition / Stable / Isolation] |

*Include footnotes for any data artifacts (e.g., "Native phone call log begins [date] only — no pre-offense baseline exists for carrier calls.")

**Baseline Narrative:** 1-2 paragraphs covering:
- Normal communication patterns and dominant contacts
- Whether activity INCREASED or DECREASED during offense window (critical — directly addresses prosecution escalation narrative)
- Whether late-night activity is pre-existing or new
- Whether contact network expanded or contracted and why
- Any data artifacts that distort the comparison (e.g., native call log starting mid-period)
- Which findings were strengthened or weakened by baseline comparison

### CRITICAL WINDOW ANALYSIS (Section 11)

**MANDATORY.** This section presents the analytical findings derived from the Critical Timeline (Section 9). While Section 9 is a chronological reconstruction of raw data, this section interprets what that data means for the defense. Every entry in the Critical Timeline that has defense significance gets analyzed here.

Think of Section 9 as the evidence and Section 11 as the argument.

**11.1 Critical Window Summary:**

```
CRITICAL WINDOW ANALYSIS SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Window Analyzed:     [Start] to [End]
Total Data Points:   [N] across [N] source types
Gaps in Window:      [N] totaling [N] minutes
Alibi-Quality Data:  [Y/N — describe strongest evidence]
Overall Assessment:  [STRONG DEFENSE / MODERATE DEFENSE / MIXED / CONCERNING]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**11.2 Alibi Evidence in Critical Window:**

| # | Time | Source | Evidence | Location | Strength | Notes |
|---|------|--------|----------|----------|----------|-------|
| 1 | [time] | [VIDEO/GPS/FINANCE/MSG] | [description] | [location if known] | STRONG/MOD | [note] |
| ... | ... | ... | ... | ... | ... | ... |

**11.3 Activity Inconsistent with Charged Conduct:**

For each data point that contradicts the State's theory of what the defendant was doing during the crime window:

```
CW-FINDING [N]: [Title]
Time:       [HH:MM:SS]
Source:     [Data category]
Data:       [What the record shows]
State's Theory Requires: [What the defendant must have been doing per the State]
Contradiction: [Why the data is inconsistent with the State's theory]
Strength:   [STRONG / MODERATE / CONTEXTUAL]
```

**11.4 Prosecution's Best Evidence in Critical Window:**

Identify the data points in the critical window that HELP the State, with mitigation:

| # | Time | Source | What State Will Argue | Mitigation | Damage |
|---|------|--------|----------------------|------------|--------|
| 1 | [time] | [source] | [argument] | [defense response] | HIGH/MOD/LOW |

**11.5 Critical Window Verdict:**

1–2 paragraphs: the analyst's overall assessment of what the critical window data proves or disproves. This is the defense's strongest summary of the crime window evidence, written for the attorney to adapt into argument.

**Why this is a standalone section:** Section 9 (Critical Timeline) presents raw chronological data. This section tells the attorney what that data means. Separating reconstruction from analysis prevents the attorney from having to both read and interpret simultaneously.

---

### KEY DATE ANALYSIS (Section 12)

**MANDATORY.** Beyond the critical crime window, most cases have additional dates that matter — the date of disclosure/reporting, arrest date, search warrant execution date, prior alleged incidents, and dates the State will emphasize. This section ensures every significant date gets the same analytical treatment as the crime window.

**12.1 Key Dates Identified:**

| # | Date | Significance | Data Points Available | Section 9 Treatment |
|---|------|-------------|----------------------|-------------------|
| 1 | [date] | Alleged offense | [N] | Full critical timeline |
| 2 | [date] | Disclosure/reporting | [N] | [Analyzed below] |
| 3 | [date] | Arrest | [N] | [Analyzed below] |
| 4 | [date] | Search warrant executed | [N] | [Analyzed below] |
| 5 | [date] | [Other significant date] | [N] | [Analyzed below] |

**12.2 Key Date Analysis (per date):**

For each key date beyond the crime window:

```
KEY DATE: [Date] — [Significance]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data Points: [N] across [N] source types
Time Range Analyzed: [Start] to [End]

TIMELINE SUMMARY:
[Condensed chronological reconstruction — not minute-by-minute like Section 9,
but hitting the key events]

DEFENSE-RELEVANT FINDINGS:
- [Finding with source reference]
- [Finding with source reference]

ADVERSE DATA:
- [Data point with mitigation]

BASELINE COMPARISON:
[How activity on this date compares to the Pattern of Life baseline]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**12.3 Date Cross-Correlation:**

Identify patterns across key dates:
- Communication with victim/complainant across all key dates: [pattern]
- Location patterns across key dates: [pattern]
- Behavioral changes between key dates: [pattern]
- Evidence of consciousness of innocence or guilt across dates: [pattern]

**Why this is a standalone section:** Attorneys frequently need to brief on dates beyond the crime window — disclosure day behavior, arrest day communications, and dates mentioned in the indictment. Having each key date analyzed in a single section prevents scattered analysis and ensures no significant date is overlooked.

---

### ANALYZED DATA — Category Deep Dive (Section 13)

**MANDATORY.** This section provides a detailed breakdown of each data category analyzed. While the Data Inventory (Section 5) lists what exists, this section presents what was FOUND in each category. Think of it as the evidence room — organized by type.

**13.1 Messages Analysis:**
- Total messages: [N] unique ([N] raw, [N]% duplicates removed)
- Platforms: [SMS (N), FB Messenger (N), RCS (N), etc.]
- Date range: [first message] to [last message]
- Top contacts: [table with name, count, relationship]
- Deleted messages: [N] flagged as deleted — content characterization: [incriminating/banal/system]
- Key message threads identified: [list with brief description and finding reference]
- Grooming language sweep: [ZERO hits / describe findings]

**13.2 Call Logs Analysis:**
- Total calls: [N] unique ([N] outgoing, [N] incoming, [N] missed, [N] unknown, [N] deleted)
- Date range: [range — note any truncation]
- Top contacts by call frequency: [table]
- Call duration patterns: [average duration, longest calls, marathon sessions]
- 911/emergency calls: [N] — dates and significance
- Deleted calls: [N] — characterization
- Duplicate database artifacts: [describe any SSRM/dual-source issues]

**13.3 Browsing & Search History Analysis:**
- Total browsing records: [N] ([N] unique after deduplication/noise removal)
- Total search records: [N] ([N] unique user searches vs. [N] system/Gmail noise)
- Date range: [range]
- Adult/escort sites: [list with page counts, dates, and 404(b) assessment]
- Predatory/exploitation content: [ZERO / describe — CRITICAL]
- Legal research: [describe any case/inmate/attorney searches]
- Employment searches: [describe job searching activity]
- Keyword false positive analysis: [list keywords that returned false positives with actual source]
- Notable browsing sessions: [chronological sessions with defense value]

**13.4 Contacts Analysis:**
- Total contacts: [N]
- Victim contacts: [list with how saved, nicknames]
- Life360/Family tracking contacts: [list]
- Notable contacts: [any that generate investigation leads]
- Alias/alternate identity accounts: [list]

**13.5 Cookies & Account Data:**
- Total cookies: [N]
- Notable services identified: [employer portals, security apps, dating sites, financial apps]
- Employment evidence: [cookies from employer systems]
- Home security evidence: [Ring/Nest/etc. cookies]
- Job search evidence: [Indeed/LinkedIn/etc. cookies with counts]

**13.6 Device Events:**
- Total events: [N] — [timestamped / NOT timestamped]
- Categories: [lock/unlock (N), display (N), camera (N), power (N), WiFi (N)]
- Timestamp status: [available / MISSING — impact assessment]
- Factory resets: [N] — dates if known, significance

**13.7 Video Analysis:**
- Total videos on device: [N] ([N] camera recordings, [N] screen recordings, [N] received, [N] chat media, [N] social media, [N] Live Photo clips)
- Total recording duration (camera + screen): [H:MM:SS]
- Videos with GPS metadata: [N]
- Videos with audio tracks: [N]
- Videos during critical window: [N] — total duration [H:MM:SS] — **[ALIBI ASSESSMENT]**
- Date range: [earliest video] to [latest video]

**Critical Window Videos (detailed):**

| # | Filename | Time | Duration | GPS | Audio | Type | Origin | Defense Value |
|---|----------|------|----------|-----|-------|------|--------|--------------|
| 1 | [name] | [datetime] | [mm:ss] | [coords or N/A] | [Y/N] | [Camera/Screen Rec] | [Recorded/Received] | [significance] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Video Origin Classification:**

| Origin | Count | Defense Significance |
|--------|-------|---------------------|
| Camera recordings (DCIM) | [N] | Recorded BY this phone — strongest alibi value |
| Screen recordings | [N] | Phone was in active use — proves engagement |
| Received (chat/download) | [N] | Received FROM others — not recorded by defendant |
| Social media saves | [N] | Saved from platforms — metadata stripped |
| Live Photo clips | [N] | Brief clips with GPS — verify timestamps |

**Video Integrity Notes:**
- Videos where codec does NOT match device native recording format: [N] — [list, assess if re-encoded]
- Videos with stripped metadata: [N] — [assess origin, likely social media pipeline]
- Deleted videos (database entries without files): [N] — [assess significance]
- Videos flagged for attorney content review: [N] — **[ATTORNEY REVIEW REQUIRED]**

**13.8 Financial App Data:**
- Apps present: [Cash App / Venmo / Zelle / Apple Pay / Google Pay / banking apps — or NONE]
- Total transactions across all platforms: [N]
- Date range: [range]
- Transaction volume during critical window: [N]

**Transaction Summary by App:**

| App | Transactions | Sent | Received | Amount Range | Top Recipients | Critical Window Activity |
|-----|-------------|------|----------|-------------|---------------|------------------------|
| Cash App | [N] | [N] | [N] | [$X–$Y] | [list top 3] | [N] txns — [describe] |
| Venmo | [N] | [N] | [N] | [$X–$Y] | [list top 3] | [N] txns — [describe] |
| Zelle | [N] | [N] | [N] | [$X–$Y] | [list top 3] | [N] txns — [describe] |

**Transaction Pattern Analysis:**
- Regular recurring payments (rent, bills, subscriptions): [list with amounts, recipients, frequency]
- Round-number transactions: [N] — [context: rent splits, bill sharing, or unexplained]
- Transactions with defense-relevant Venmo/Cash App notes: [list]
- Transactions to/from case-relevant parties: [list]
- Merchant transactions with location data (Apple Pay/Google Pay): [list with locations and timestamps]

**Baseline Comparison:**
- Pre-incident transaction frequency: [N/week]
- Critical window transaction frequency: [N/week]
- Change: [Normal / Spike / Drop — significance]

**If financial app data is NOT available:** State reason: [Not extracted / App not installed / Encrypted / Data gutted]. Assess whether the absence matters for the defense theory.

**13.9 Health & Fitness Data:**
- Sources: [Apple Health / Google Fit / Fitbit / Samsung Health / Apple Watch — or NONE]
- Wearable device: [Make/model if identifiable, e.g., "Apple Watch Series 7"]
- Date range: [range]
- Data types available: [Steps / Heart rate / Sleep / Workouts / GPS routes / Elevation]

**Critical Window Health Data:**

| Time | Steps (cumul.) | Heart Rate | Activity | Sleep Status | Defense Value |
|------|---------------|------------|----------|-------------|--------------|
| [time] | [N] | [N bpm] | [Stationary/Walking/Running] | [Awake/Light/Deep/N/A] | [significance] |
| ... | ... | ... | ... | ... | ... |

**Key Metrics:**
- Steps during critical window: [N] — baseline comparison: [N/hr normal vs. N/hr critical window]
- Heart rate during critical window: [range bpm] — resting baseline: [N bpm]
- Sleep data spanning crime window: [Asleep from X to Y / Not asleep / No data]
- Workout GPS routes on critical date: [None / describe with coordinates]

**Wearable Verification:** Was the device worn during the critical window? Evidence: [continuous heart rate data = worn / gap in data = possibly removed / charging indicator = off-wrist]

**Health Data Limitations (must disclose):**
- Consumer wearables are not medical-grade instruments
- Step counts can be triggered by arm motion without walking
- Heart rate is affected by caffeine, medication, anxiety, temperature
- Sleep algorithms estimate based on motion/HR — not definitive proof of sleep
- Absence of data means device wasn't recording, not that person was absent

**If health data is NOT available:** State: **"Health/fitness data: NOT AVAILABLE — [no health app / no wearable / data not extracted]."**

**13.10 Personal Data Apps (Notes, Calendar, Voice Memos, Email):**

**Notes:**
- App(s): [Apple Notes / Google Keep / Samsung Notes / other]
- Total notes: [N] | Date range: [range]
- Notes created/modified during critical window: [N] — [describe content themes]
- Deleted notes recovered: [N] — [content characterization]
- Notes documenting threats, incidents, or concerns: [N] — **[flag for attorney]**

**Calendar:**
- Calendar events during critical window: [N] — [list with times and locations]
- Recurring events establishing routine: [describe patterns]
- Work schedule entries: [list relevant ones]
- Shared calendar events (independently verifiable): [list]

**Voice Memos:**
- Total voice memos: [N] | Date range: [range]
- Voice memos during/near critical window: [N] — **[ATTORNEY REVIEW REQUIRED — cannot assess audio content programmatically]**
- Durations: [list with timestamps]
- Defense note: Voice memo recordings prove the phone owner was holding their phone and speaking. Duration establishes continuous phone possession.

**Email:**
- Email accounts on device: [list]
- Emails sent/received during critical window: [N]
- Work emails establishing professional activity: [describe]
- Emails with location indicators: [describe]

**13.11 Application Usage & Screen Time:**

**Overview:**
- Extraction source: [Cellebrite / Manual recovery / WAL file recovery]
- Total app sessions: [N]
- Unique apps used: [N]
- Date range: [earliest session] to [latest session]
- Screen-on periods captured: [Y/N]

**Critical Window App Activity:**

| Time | App Name | Duration | Session Type | Defense Value |
|------|----------|----------|--------------|--------------|
| [HH:MM:SS] | [App name] | [mm:ss] | [Foreground/Background] | ACTIVE USE — phone unlocked, user engagement |
| [HH:MM:SS] | [App name] | [mm:ss] | [type] | [significance] |
| ... | ... | ... | ... | ... |

**Critical Window Summary:**
- Total foreground time: [H:MM:SS] — the device was actively in use for [X] minutes during the alleged crime window
- Apps used: [list in chronological order]
- Most-used app: [App name], [duration] — user was actively engaged [when]
- App switching rate: [High/Normal/Low] — indicates [conscious engagement / normal use / low engagement]
- Gaps in app usage: [Gaps lasting >1 hour: [times] / No significant gaps]

**Baseline Comparison (Pattern of Life):**

| Metric | Baseline Period | Critical Window | Assessment |
|--------|-----------------|-----------------|-----------|
| Daily app sessions | [N/day average] | [N/day during crime window] | [Normal / Spike / Drop] |
| Total foreground time/day | [H:MM/day] | [H:MM on crime date] | [Normal / Unusual] |
| Peak usage hour | [HH:00–HH:59] | [Usage during crime window fell in peak/off-peak hours?] | [Normal pattern] |
| Most-used apps (top 3) | [App 1, App 2, App 3] | [Same apps or different?] | [Normal continuation] |

**Sleep Pattern Detection from App Usage:**
- Hours with ZERO app activity (baseline): [HH:00–HH:00] — established sleep window
- Hours with ZERO app activity (critical date): [HH:00–HH:00]
- Consistency: [Matches baseline sleep pattern / Different from baseline / No clear pattern]
- **Alibi Value:** If device shows zero app activity during hours consistent with the client's baseline sleep window, this corroborates alibi claims of being asleep during the alleged crime time.

**App Category Analysis:**

| Category | Examples | Sessions (Baseline) | Sessions (Critical Window) | Change |
|----------|----------|-------------------|--------------------------|--------|
| Social Media | Instagram, TikTok, Snapchat, Facebook | [N/day avg] | [N during crime window] | [Normal/Spike/Drop] |
| Communication | Messages, WhatsApp, Signal, Messenger | [N/day avg] | [N during crime window] | [Normal/Spike/Drop] |
| Entertainment | Netflix, YouTube, Spotify, Games | [N/day avg] | [N during crime window] | [Normal/Spike/Drop] |
| Productivity | Email, Calendar, Notes, Banking | [N/day avg] | [N during crime window] | [Normal/Spike/Drop] |
| Utility | Maps, Weather, Settings, Camera | [N/day avg] | [N during crime window] | [Normal/Spike/Drop] |

**Notable App Sessions:**
- [App name], [timestamp], [duration] — significant because [user was engaged in normal/expected activity]
- [App name], [timestamp], [duration] — significant because [time/duration inconsistent with prosecution theory]

**Prosecution Misinterpretation Watch:**
- "Phone was idle during the crime window" — **Contradiction:** App usage logs show [N] minutes of active foreground use during [timeframe]. Device was not idle.
- "Gaps in app usage prove consciousness of guilt" — **Context required:** Baseline comparison shows gaps of [N] hours are normal ([e.g., sleeping, working, driving]). [Specific gap] is consistent with baseline pattern.
- "Defendant could have shared the phone" — **Baseline analysis:** App usage profile during crime window (apps used, usage times, duration patterns) matches defendant's normal baseline, inconsistent with different user.

**Device Extraction Limitations:**
- Cellebrite extraction method: [Logical / File system / Physical] — **App usage logs most reliable on [method type]**
- Data retention: Typically 30 days on iOS; 30 days on Android (manufacturer-dependent)
- Gaps in extraction: [None / Describe any periods with missing data]
- WAL file recovery: [If available: recovered additional sessions not in active database]

**If app usage data is NOT available:** State reason: **"App usage data: NOT AVAILABLE — [Logical extraction not performed / Device extracted before foreground data captured / App usage logs cleared / Not supported on iOS version X]."** Assess impact on defense timeline.

### LOCATIONS — GPS, Wi-Fi & Cell Site Analysis (Section 14)

**MANDATORY.** Dedicated location analysis section. Previously location data was buried within findings — it deserves its own section because location evidence is often the most powerful alibi or timeline tool.

**14.1 Location Data Overview:**
- Total location records: [N]
- Sources: [Google Location History (N), Gmail (N), Facebook (N), GPS (N), Wi-Fi (N), Cell tower (N)]
- Date range: [range]
- Geographic concentration: [primary areas — e.g., "Orange/Vidor, TX and Lake Charles, LA"]

**14.2 Offense Date Location Analysis:**
For each alleged offense date:

| Date | Location Records | Primary Location | Coordinates | Consistent with Allegation? |
|------|-----------------|-----------------|------------|---------------------------|
| [date] | [N] points | [area/venue] | [coords] | [Yes/No — explain] |

**14.3 Suspicious Location Patterns — NONE / [describe]:**
- Proximity to schools, daycares, playgrounds, or child-related venues: [NONE / describe]
- Patterns of visiting locations associated with exploitation: [NONE / describe]
- Unusual travel patterns: [NONE / describe]

**14.4 Arrest Day Location Reconstruction:**
- Total points: [N]
- Movement pattern: [describe — e.g., "clustered at home, then moved to hospital/police station"]
- Coordinates: [key waypoints with approximate addresses]

**14.5 Key Date Location Evidence:**
| Date | Event | Location Points | GPS Area | Defense Value |
|------|-------|----------------|----------|--------------|
| [date] | [e.g., "July 4 BBQ"] | [N] | [coords/area] | [alibi / normal family activity] |
| [date] | [e.g., "July 7 waterpark"] | [N] | [coords/area] | [engaged parenting] |

**14.6 Location Data Gaps:**
- Dates with NO location data: [list]
- Dates with sparse data: [list]
- Explanation: [GPS disabled, indoor, extraction limitation, etc.]

**Handoff:** If cell tower data, geofence warrants, or CSLI is involved → dw-cell-site-geolocation-auditor

### DEFENSE-FAVORABLE FINDINGS (Section 15)

**MANDATORY subsection structure — organize findings under these headings:**
- 15.1 Alibi & Timeline (Lens 1)
- 15.2 Third-Party Fabrication & Victim Credibility (Lenses 2, 5)
- 15.3 State of Mind & Consciousness of Innocence (Lens 4)
- 15.4 Gaps in State's Case & Contradictions (Lenses 3, 7)
- 15.5 Additional Defense-Favorable Findings

**Mandatory finding categories to check (include or note 'not applicable'):**
- Deleted messages analysis (count, content characterization, does deletion = guilt?)
- Installed apps absence analysis (what privacy/encrypted/exploitation apps are NOT present?)
- Location data pattern analysis (any suspicious locations? school/daycare/playground proximity?)
- Photo forensic metadata (MediaOrigin, EXIF, file modification dates)
- Video alibi analysis (any camera recordings during critical window? Duration + GPS + audio?)
- Financial app transaction patterns (any transactions establishing timeline or location?)
- Health/fitness data (step counts, heart rate, sleep during critical window?)
- Voice memos and notes (any contemporaneous documentation of threats, events, or state of mind?)
- Communication gap analysis (any unexplained gaps? Explained by call data or other channels?)
- Employment/daily life evidence (job searching, work communications, mundane parenting)
- 911/emergency calls (any protective behavior?)
- Family tracking/monitoring apps (Life360, Find My, etc. — who invited whom?)
- Third-party harassment or interference patterns

Organize by defense lens. For each finding:

```
FINDING [Number]: [Descriptive Title]
Defense Lens: [Alibi / Third-Party / Contradiction / State of Mind /
              Victim Credibility / Self-Defense]
Strength: [STRONG / MODERATE / CONTEXTUAL]
Auth Exception: [Only if different from extraction-level auth — otherwise omit]

DATA:
  [What the phone data shows — specific records with source references]

DEFENSE VALUE:
  [Why this helps the defense — plain language]

SUGGESTED USE:
  [How to deploy: cross-exam, motion, argument, investigation lead]

SOURCE REFERENCE:
  [File name, row/line number, timestamp — verifiable citation]

FOUNDATION NOTE (La. C.E. Art. 901(B)(9)):
  [Only if auth exception exists — what additional foundation is needed
   beyond the extraction-level auth already established in Section 2]

CORROBORATION NEEDED:
  [What additional evidence would strengthen this finding]
```

### ADVERSE FINDINGS (Section 16)

**MANDATORY.** This section presents all data that hurts the defense, organized for rapid attorney assessment. Placing adverse findings in their own section — immediately after defense-favorable findings — ensures the attorney gets the full picture before reading prosecution vulnerabilities and mitigation strategies. An attorney who only reads Sections 15 and 16 should understand both the strengths and weaknesses of the phone data.

**16.1 Adverse Findings Summary:**

| # | Category | Description | Damage Level | Mitigation Available | Finding Ref |
|---|----------|-------------|-------------|---------------------|-------------|
| A-1 | [Messages/Browsing/Location/etc.] | [One-line description] | CRITICAL/HIGH/MOD/LOW | [Y/N — brief] | [ref] |
| A-2 | [Category] | [Description] | [Level] | [Y/N] | [ref] |
| ... | ... | ... | ... | ... | ... |

**16.2 Detailed Adverse Analysis:**

For each adverse finding:

```
ADVERSE FINDING A-[N]: [Descriptive Title]
Category:    [Data category]
Damage Level: [CRITICAL / HIGH / MODERATE / LOW]

THE DATA:
  [What the records actually show — specific records with source references]

HOW THE STATE WILL USE IT:
  [The prosecution's likely argument]

DAMAGE ASSESSMENT:
  [If this comes in unrebutted, what's the impact on the defense?]

MITIGATION STRATEGY:
  [How to minimize — context, explanation, challenge reliability,
   exclude under Art. 403, motion in limine]

CAN IT BE TURNED TO DEFENSE ADVANTAGE?
  [Yes/No — explain. Some adverse data has a silver lining when
   placed in full context]

CORROBORATION CHECK:
  [Does the State need additional evidence to make this stick?
   What's missing from their case on this point?]
```

**16.3 Adverse Data Totals:**

| Damage Level | Count | Mitigatable | Excludable (MIL) |
|-------------|-------|------------|-----------------|
| CRITICAL | [N] | [N] | [N] |
| HIGH | [N] | [N] | [N] |
| MODERATE | [N] | [N] | [N] |
| LOW | [N] | [N] | [N] |

**Why this is a standalone section:** In prior reports, adverse data was buried within Prosecution Vulnerabilities, which mixed the bad facts with the defense response. The attorney preparing for client meetings, plea negotiations, or trial strategy needs a clean, honest inventory of everything that hurts — separate from the spin. Section 16 gives them the bad news; Section 17 gives them the response playbook.

---

### PROSECUTION VULNERABILITIES (Section 17)

**17.1 Prosecution Misinterpretation Risks Matrix**

**MANDATORY.** Present as a table BEFORE the detailed adverse findings. This gives the attorney a one-page overview of every anticipated State claim and the defense counter:

| State's Likely Claim | Reality | Risk Level | Defense Response |
|---------------------|---------|-----------|----------------|
| [claim] | [actual data] | HIGH/MOD/LOW | [counter strategy] |

Common misinterpretation patterns to always check:
- Keyword false positives (ad networks like Taboola, system parameters, cached content)
- Factory resets as evidence destruction (vs. normal phone lifecycle)
- Call volume escalation artifacts (data truncation, app vs. carrier records)
- Late-night activity as suspicious (vs. baseline pre-existing pattern)
- Deleted data as consciousness of guilt (vs. auto-delete, system messages, normal management)
- Browsing history decontextualization (escort sites ≠ child exploitation)
- Samsung Wellbeing deletion (routine factory reset consequence)
- Video presence ≠ video creation (received videos vs. recorded; file path reveals origin)
- Video duration ignored (2-second accidental recording vs. 5-minute intentional capture)
- Video metadata stripping misinterpreted (social media pipelines strip EXIF — not deliberate sanitization)
- Financial app round numbers ≠ drug transactions (most person-to-person payments are round numbers)
- Venmo notes decontextualized (inside jokes, emoji, casual speech ≠ coded drug references)
- Transaction frequency without baseline (regular roommate splits look like "high volume" without context)
- Health data overstatement (step counts ≠ precise location; heart rate ≠ emotional state; consumer devices ≠ medical instruments)
- Absence of wearable data ≠ suspicious (people charge devices, shower, sleep without them)

**17.2 Adverse Data — What Hurts the Defense**

For each anticipated prosecution data point:

```
STATE'S LIKELY ARGUMENT: [What the prosecution will claim this data shows]

THE DATA: [What the records actually show — cite specific records]

THE PROBLEM: [Why the State's interpretation is wrong, incomplete, or misleading]
  Misinterpretation Type: [Reference to specific pattern in
                          common-misinterpretations.md]

DEFENSE RESPONSE: [How to counter — motion in limine, cross-exam, argument]

DAMAGE ASSESSMENT: [If this data comes in, how bad is it?
                    MINIMAL / CONCERNING / SIGNIFICANT / CRITICAL]

MITIGATION: [How to minimize the damage — context, explanation,
            challenge reliability, exclude under Art. 403]
```

**Adverse Findings Subsection:**
Clearly marked subsection listing data that hurts the defense. For each:
- What it shows (plainly stated)
- How the State will use it
- Damage level
- Mitigation strategy
- **Can it be turned to defense advantage?** [Yes/No — explain]

### GAPS — Timeline, Data & Evidentiary (Section 18)

**MANDATORY.** This section consolidates all gaps identified across the analysis — timeline gaps (periods with no data), data gaps (categories with missing or incomplete records), and evidentiary gaps (expected evidence that doesn't exist or wasn't produced). While gaps surface throughout the report, this section ensures the attorney has a single inventory of every hole in the record and its strategic significance.

**18.1 Timeline Gaps:**

Gaps in the chronological record where expected device activity is absent.

| # | Gap Start | Gap End | Duration | Data Sources Silent | Baseline Comparison | Significance | Action |
|---|-----------|---------|----------|-------------------|-------------------|-------------|--------|
| TG-1 | [time] | [time] | [N min/hr] | [All / MSG only / etc.] | [Normal per baseline / Abnormal] | [Defense favorable / Concerning / Neutral] | [Investigate / Explainable / Flag] |
| TG-2 | ... | ... | ... | ... | ... | ... | ... |

**18.2 Data Category Gaps:**

Categories where data is missing, incomplete, or suspiciously absent.

| # | Category | Gap Description | Expected Data | Possible Explanations | Defense Impact | Action |
|---|----------|----------------|--------------|----------------------|---------------|--------|
| DG-1 | [Category] | [What's missing] | [What should be there] | [Innocent: X / Concerning: Y] | [Impact] | [Subpoena / Re-extract / Note] |
| DG-2 | ... | ... | ... | ... | ... | ... |

**18.3 Evidentiary Gaps:**

Evidence that should exist based on the case theory but doesn't appear in the phone data.

| # | Expected Evidence | Why Expected | Absent/Present | Significance | Defense Use |
|---|------------------|-------------|---------------|-------------|------------|
| EG-1 | [e.g., "Grooming messages"] | [State alleges grooming] | ABSENT | **DEFENSE FAVORABLE — no evidence of alleged conduct** | [Cross-exam / Argument] |
| EG-2 | [e.g., "Photos of victim"] | [State alleges relationship] | ABSENT | **DEFENSE FAVORABLE** | [Cross-exam] |
| EG-3 | ... | ... | ... | ... | ... |

**18.4 Gaps Exploitable by Defense:**

Gaps that the defense can affirmatively use — evidence the State should have but doesn't, extraction limitations the State failed to disclose, or missing data categories that undermine the State's theory.

**18.5 Gaps Exploitable by Prosecution:**

Gaps that the State may try to use against the defense — unexplained silences, missing data that could be spun as evidence destruction, or periods where the defendant's digital footprint goes dark.

| # | Gap | State's Likely Argument | Defense Preemptive Response |
|---|-----|------------------------|---------------------------|
| 1 | [Gap ref] | [How State will spin it] | [Defense explanation] |

**Why this is a standalone section:** Gaps were previously scattered across timeline analysis, data inventory, and findings. Having a single gap inventory lets the attorney immediately see every hole and decide which gaps to exploit (missing grooming evidence = defense favorable), which to explain (sleep gaps = normal), and which to preempt (unexplained silences = prepare client testimony).

---

### MISSING DATA ANALYSIS (Section 19)

For each gap:

```
GAP: [Description — time period, data category, or expected record]
PERIOD: [Date/time range affected]
BASELINE COMPARISON: [Is this gap normal per the Pattern of Life baseline?]
EXPECTED DATA: [What should be there based on normal device activity patterns]
POSSIBLE EXPLANATIONS:
  - Innocent: [Phone off/dead, client asleep, extraction limitation]
  - Concerning: [Selective deletion, device tampering, data not extracted]
IMPACT: [How this gap affects the defense analysis]
RECOMMENDATION:
  [ ] Add to Missing Discovery Demand
  [ ] Request re-extraction
  [ ] Obtain carrier records to fill gap
  [ ] Investigate independently
```

### INSIGHTS — Cross-Cutting Analytical Observations (Section 20)

**MANDATORY.** Insights are analytical observations that emerge from looking ACROSS data categories — patterns that no single finding captures. These are the "so what?" observations that connect the dots.

**Format each insight as:**

```
INSIGHT [Number]: [Title]
Data Sources: [Which categories contributed to this observation]
Observation: [What the cross-category analysis reveals]
Defense Implication: [How this helps or hurts the defense]
Confidence: [HIGH — supported by multiple sources / MODERATE — supported but with gaps / LOW — inference]
```

**Mandatory insight categories to evaluate:**

1. **Behavioral Consistency:** Does the defendant's digital behavior across ALL categories tell a consistent story? (e.g., "Across messages, calls, browsing, and location data, Banks presents as a working father engaged in normal family life. Zero categories contain predatory indicators.")

2. **Escalation vs. De-escalation:** Did communication frequency, search behavior, or location patterns escalate or de-escalate during the offense window? (This is the Pattern of Life finding applied across ALL data types, not just messages.)

3. **Digital Footprint Completeness:** What does the TOTALITY of the digital footprint say about the person? (e.g., "A person with 115,000 records over 3 years who shows zero exploitation indicators across every data category is statistically significant.")

4. **Prosecution Narrative Fit:** Does the phone data support or undermine the State's theory when viewed holistically? (e.g., "The State's theory requires [X behavior] but the data shows [opposite].")

5. **Third-Party Dynamics:** What do cross-category patterns reveal about household dynamics, relationship conflicts, or third-party interference?

6. **Temporal Patterns:** What do cross-category time patterns reveal? (e.g., "Browsing activity spikes correlate with work breaks, not with child access times.")

### TAGS — Evidence Classification Index (Section 21)

**MANDATORY.** Tags provide a searchable, filterable index of every finding and data point by category. This allows the attorney to quickly pull all evidence related to a specific defense theme.

**Tag Categories:**

| Tag | Description | Findings |
|-----|------------|----------|
| `ALIBI` | Evidence placing defendant elsewhere during alleged offense | [F-5, F-6, F-7, ...] |
| `FABRICATION` | Evidence supporting fabrication defense theory | [F-8, F-10, ...] |
| `DENIAL` | Contemporaneous denials or consciousness of innocence | [F-2, F-13, ...] |
| `COOPERATION` | Evidence of willingness to cooperate with LE | [F-2, F-16, ...] |
| `NO-EVIDENCE` | Absence of expected incriminating evidence | [F-3, F-4, F-17, F-18, F-19, ...] |
| `PARENTING` | Evidence of normal parental behavior | [F-6, F-7, F-24, ...] |
| `EMPLOYMENT` | Evidence of stable employment | [F-23, ...] |
| `VICTIM-CRED` | Evidence bearing on victim/complainant credibility | [F-8, F-10, F-11, F-12, ...] |
| `THIRD-PARTY` | Evidence of third-party interference or suspects | [F-9, ...] |
| `FORENSIC-GAP` | Extraction or forensic methodology issues | [F-20, F-21, Gap-1 through Gap-6, ...] |
| `404B-RISK` | Data that could trigger 404(b)/Prieur notice | [A-1, A-2, A-3, A-5, A-6, ...] |
| `ADVERSE` | All adverse data points | [A-1 through A-8, ...] |
| `CROSS-EXAM` | Findings useful for cross-examination | [F-10, F-11, F-15, F-17, F-20, F-21, ...] |
| `MOTION` | Findings supporting pretrial motions | [A-1 → 404(b), Gap-1 → compel, ...] |
| `EXPERT-NEEDED` | Findings requiring expert testimony | [F-20, F-21, F-22, Gap-2, Gap-3, ...] |
| `SUBPOENA` | Items requiring subpoena for additional evidence | [F-24 → Ring, F-23 → Halliburton, Gap-1 → carrier, ...] |
| `VIDEO-ALIBI` | Video recordings supporting alibi (timestamp + duration + GPS) | [F-xx, ...] |
| `FINANCIAL` | Financial app data bearing on timeline, location, or pattern | [F-xx, ...] |
| `HEALTH-DATA` | Health/fitness data bearing on physical state or location | [F-xx, ...] |
| `VOICE-MEMO` | Voice memos requiring attorney review | [F-xx, ...] |

**How to use tags:** The attorney preparing for cross-examination pulls all `CROSS-EXAM` tagged findings. The attorney drafting a 404(b) opposition pulls all `404B-RISK` tagged items. The attorney briefing an expert pulls all `EXPERT-NEEDED` items.

**Tag assignment rule:** Every finding and adverse data point MUST be assigned at least one tag. Most will have 2-3 tags.

### EIGHT-LENS DEFENSE ANALYSIS MATRIX (Section 22)

**MANDATORY.** This is a one-page summary table that gives the attorney the entire case posture at a glance. Place AFTER findings and adverse data so the attorney has already read the detail.

| Lens | Key Findings | Strength |
|------|-------------|----------|
| 1. Alibi | [Finding refs and 1-line summaries] | [STRONG/MODERATE/WEAK] |
| 2. Third-Party Fabrication | [refs] | [strength] |
| 3. State Contradictions | [refs] | [strength] |
| 4. State of Mind | [refs] | [strength] |
| 5. Victim Credibility | [refs] | [strength] |
| 6. Self-Defense | [refs or N/A] | [strength or —] |
| 7. Gaps in State's Case | [refs] | [strength] |
| 8. What Hurts Us | [adverse refs with risk level] | [risk assessment] |

**Why this matters:** This table was present in one report output but missing from another. It provides the single most useful at-a-glance reference for trial preparation. It must be in every Full Report.

### CROSS-REFERENCE FINDINGS (Section 23 — Conditional)

Only include if case documents, surveillance, or body cam footage were provided for cross-referencing.

Use the documentation format from `references/cross-reference-guide.md` Section 8.

Organize by severity: CRITICAL contradictions first, then SIGNIFICANT, MODERATE, MINOR. Include video cross-references with sync offset noted.

### COMPANION SKILL HANDOFFS (Section 24)

**MANDATORY.** Present as a table for quick reference, then detail each handoff below the table:

| Skill | Purpose | Priority |
|-------|---------|----------|
| [skill name] | [what to hand off] | HIGH/MODERATE/LOW |

**Minimum handoffs to evaluate (include or explain why N/A):**
- dw-mobile-forensic-auditor (extraction methodology issues)
- dw-cross-exam-architect (cross-exam seeds for LE, victims, witnesses)
- dw-brady-giglio-auditor (disclosure obligations)
- dw-404b-opposition (if ANY adverse data could trigger 404(b) notice)
- dw-suppression-motion (if search warrant issues exist)
- dw-sqlite-recovery (if deleted databases identified)
- dw-sex-offense-specialist (if sex offense charges — strategy, jury selection, expert retention)
- dw-criminal-defense (Phase 1 Step 3, Refresh Mode — if LWOP exposure on any count and `000 - Case Profile.docx` already exists)
- dw-child-forensic-interview-auditor (if child victim forensic interview exists)
- dw-search-warrant-auditor (if search warrant in case)
- dw-video-evidence-auditor (if body cam, dash cam, or surveillance video — NOT phone-recorded video, which stays in this analysis)

Collect all handoff summaries generated during analysis:

**Geolocation Auditor Handoffs:**
[Full handoff summaries per SKILL.md Step 5 format]

**Forensic Methodology Auditor Handoffs:**
[Full handoff summaries per SKILL.md Step 5 format]

**Cross-Exam Seeds:**
[All cross-exam chapter seeds per SKILL.md Step 5 format]

**Brady/Giglio Auditor Handoffs:**
[If selective reporting, selective extraction, or undisclosed exculpatory data identified]

### DEFENSE ACTION ITEMS (Section 25)

Prioritized checklist:

```
IMMEDIATE (within 48 hours):
□ [Action item with brief explanation]
□ ...

SHORT-TERM (within 2 weeks):
□ [Action item]
□ ...

ONGOING / AS NEEDED:
□ [Action item]
□ ...

MOTIONS TO CONSIDER:
⚖ [Motion type — grounds — supporting finding reference]
⚖ ...

ADDITIONAL DATA NEEDED:
📋 [What to request — from whom — why]
📋 ...

EXPERT WITNESSES:
👤 [Expert type needed — what they would address — which findings require expert support]
👤 ...

INVESTIGATION LEADS:
🔍 [What to investigate — how — which findings generated this lead]
🔍 ...
```

### EXHIBIT-READY EXTRACTS (Section 26)

Pre-formatted evidence extracts ready for trial use. Each exhibit is designed for direct printing or courtroom projection. The attorney should be able to pull these directly into motions, opening/closing arguments, or cross-examination without reformatting.

**For each exhibit:**

```
EXHIBIT [Letter]: [Descriptive Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: [Timeline Chart / Message Thread / Call Log Excerpt /
      Location Map Data / Photo EXIF Summary / Frequency Chart]

CONTENT:
  [The exhibit itself — formatted for readability:
   - Timeline charts: chronological table with timestamps,
     source types, and content summaries
   - Message threads: full thread with context (not cherry-picked),
     sender/recipient, timestamps, read receipts
   - Call logs: filtered and annotated subset
   - Frequency charts: baseline vs. critical window comparison]

AUTHENTICATION:
  [References extraction-level auth from Section 4.
   Only detail exceptions here — secondary extraction,
   WAL recovery, different chain of custody.]
  Source File: [filename, rows/lines]

FOUNDATION REQUIREMENTS (La. C.E. Art. 901(B)(9)):
  [Only if auth exception — what additional foundation needed
   beyond extraction-level auth established in Section 4]

DEFENSE PURPOSE:
  [How this exhibit is used — which argument or cross-exam it supports]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Standard exhibit types to generate when data supports them:**
- **Exhibit A: Critical Window Timeline** — the master timeline chart for the crime date
- **Exhibit B: Key Message Thread(s)** — full conversation context for any thread the State will cite
- **Exhibit C: Call Log Annotated Excerpt** — calls during critical window with baseline comparison
- **Exhibit D: Pattern of Life Comparison** — visual showing baseline vs. crime date activity
- **Exhibit E+: Specific Findings** — any additional findings strong enough to warrant standalone exhibits

**Additional exhibit types identified from practice:**
- **Exhibit: Fabrication Timeline** — if fabrication defense: chronological demonstrative from first fabrication indicator through arrest
- **Exhibit: Family Tracking Invitation** — if family GPS/tracking app invitation exists (e.g., Life360) — powerful for cross-examination
- **Exhibit: Browsing Keyword False Positive Analysis** — technical rebuttal chart showing all false positive keyword matches with actual source URLs
- **Exhibit: Communication Channel Shift Analysis** — if text gap explained by call data or other channel
- **Exhibit: Installed App Absence Chart** — list of privacy/exploitation apps NOT found on device
- **Exhibit: Video Alibi Timeline** — chronological chart of all videos recorded during critical window with timestamp, duration, GPS, and audio track indicators. A 4-minute video at a GPS-verified location during the crime window is a visual demonstrative the jury can understand immediately.
- **Exhibit: Financial Transaction Timeline** — chronological chart of Cash App/Venmo/Zelle transactions during critical window, cross-referenced with location data from merchant transactions. Rebuts "defendant was at crime scene" when Apple Pay shows a gas station purchase across town.
- **Exhibit: Transaction Baseline Comparison** — visual comparing defendant's payment patterns (frequency, amounts, recipients) during baseline period vs. State's "suspicious" window. Demonstrates that flagged transactions are consistent with normal behavior.
- **Exhibit: Health Data Activity Chart** — step count and heart rate timeline during critical window overlaid against baseline. A flat line (zero steps, resting heart rate) during the alleged assault is powerful alibi evidence.
- **Exhibit: Video Origin Classification Chart** — visual showing how many videos were camera-recorded vs. received vs. downloaded. Rebuts State's implication that all videos on the device were the defendant's creation.

### EVIDENCE INTEGRITY (Section 27)

**MANDATORY.** Consolidated integrity summary for quick attorney reference:

- **Hash Verified:** [Full SHA256 value — chain of custody status]
- **Extraction Method:** [Filesystem / Physical / Chip-off — note limitations]
- **Time Zone:** [All timestamps in X format. Local time = Y during relevant period]
- **Deleted Data:** [N deleted messages recovered, N deleted calls. Content characterization]
- **Forensic Gaps:** [List all unextracted containers, deleted databases, undatable events]

**Per-Finding Authentication Exceptions:**

| Finding | Exception | Impact |
|---------|-----------|--------|
| [Finding ref] | [What's different about auth] | [Admissibility impact] |

---

### REPORTS — Companion Analysis Requests (Section 28)

**MANDATORY.** This section translates companion skill handoffs into actionable report requests. While Section 24 lists the technical handoffs, this section frames them as deliverable reports the attorney can request or assign.

**Report Request Format:**

| # | Report Title | Skill | Input Needed | Priority | Status |
|---|-------------|-------|-------------|----------|--------|
| R-1 | Mobile Forensic Methodology Audit | dw-mobile-forensic-auditor | This report + extraction files | HIGH | Pending |
| R-2 | Cross-Examination Outlines | dw-cross-exam-architect | This report + case documents | HIGH | Pending |
| R-3 | Brady/Giglio Compliance Audit | dw-brady-giglio-auditor | This report + discovery index | HIGH | Pending |
| R-4 | 404(b) Opposition Brief | dw-404b-opposition | This report Section 16 adverse data | HIGH | Pending |
| R-5 | Forensic Interview Protocol Audit | dw-child-forensic-interview-auditor | Forensic interview recording | HIGH | Pending |
| R-6 | Search Warrant Audit | dw-search-warrant-auditor | Search warrants (003/004) | MODERATE | Pending |
| R-7 | SQLite Database Recovery | dw-sqlite-recovery | Raw extraction databases | MODERATE | Pending |
| R-8 | Sex Offense Defense Strategy | dw-sex-offense-specialist | This report + all case documents | HIGH | Pending |
| R-9 | LWOP Defense Checklist | dw-criminal-defense (Phase 1 Step 3 Refresh Mode) | This report + client history | HIGH | Pending |
| R-10 | Suppression Motion | dw-suppression-motion | Search warrants + this report | MODERATE | Pending |

**For each report request, detail:**
- What specific issues from THIS analysis feed into the companion report
- What additional documents or data the companion skill needs
- Expected deliverable (motion, outline, audit report, etc.)
- Dependencies (e.g., "R-7 should complete before R-1 so recovered data informs the methodology audit")

### APPENDICES (Section 29)

**Appendix A: Complete Data File Inventory**
Full list of all files analyzed with file names, sizes, dates, and MD5 hashes if available.

**Appendix B: Search Terms Used**
Document all keyword searches, name searches, and number searches performed during analysis — ensures reproducibility and completeness.

**Appendix C: Programmatic Analysis Scripts**
If Python scripts were used to parse structured data, include the script logic (not full code) describing what was analyzed and how. The attorney should understand the methodology even if they can't read Python.

**Appendix D: Raw Timeline Data**
If the critical timeline was built from multiple sources, include the complete chronological data set (may be large — consider as separate Excel attachment).

**Appendix E: Authentication Chain Log**
See Section 27: Evidence Integrity for extraction-level auth and per-finding exceptions.

---

## Output Format

**MANDATORY:** The Full Report MUST be generated as a formatted Word document (.docx) using the docx skill, AND converted to PDF. Both files must be saved to the case directory.

**Naming Convention:**
```
[LastName]_[CaseNo]_PhoneDump_DefenseIntelReport_[Date].docx
[LastName]_[CaseNo]_PhoneDump_DefenseIntelReport_[Date].pdf
```

Example:
```
Johnson_24-CR-1234_PhoneDump_DefenseIntelReport_20260305.docx
Johnson_24-CR-1234_PhoneDump_DefenseIntelReport_20260305.pdf
```

---

*This reference is loaded by the dw-forensic-dump-analyzer skill during Step 6 (Report Generation). Use in conjunction with the docx SKILL.md for document formatting and creation.*
