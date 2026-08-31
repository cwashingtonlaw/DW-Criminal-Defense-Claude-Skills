# Video Source Classification

Read at STEP 2 (Video Source Classification) of `dw-video-evidence-auditor-crim/SKILL.md` — the Video Source Matrix and the CONSPICUOUS ABSENCE flag template.

### Video Source Matrix

| Source Type | Common Systems | Key Audit Concerns | Audit Module |
|-------------|---------------|-------------------|--------------|
| **Body-Worn Camera** | Axon (Body 2/3/4), Motorola (V300/Si500), Getac, Utility | Activation compliance, buffering gaps, perspective limits, officer control of camera angle | Module A |
| **In-Car / Dash Cam** | Axon Fleet, WatchGuard, Coban, L3 Mobile-Vision | Trigger events, forward-only perspective, audio range limits, wireless mic pairing | Module B |
| **Surveillance / CCTV** | Hikvision, Dahua, Axis, Genetec, Milestone, Avigilon | Timestamp accuracy, compression artifacts, export integrity, retention/overwrite cycles | Module C |
| **Interview Room** | iRecord, Axon Interview, agency-specific systems | Recording continuity, Miranda documentation, off-camera conversations, audio quality | Module D |
| **Civilian / Cell Phone** | Varies (iPhone, Android, Ring/Nest doorbell, dashcam apps) | Authentication, metadata integrity, selective recording, chain of custody from civilian to LE | Module E |

### Conspicuous Absence Flags

When the incident type strongly implies video should exist but does not appear in discovery:

> **CONSPICUOUS ABSENCE — [Source Type]:** [Agency] equips officers with [BWC system / dash cam / etc.]. Officer [name/badge] responded to this incident but no [video type] appears in discovery. Determine: was the camera activated and footage not disclosed (*Brady* concern)? Was the camera not activated (policy violation)? Was footage recorded and subsequently lost, deleted, or overwritten (spoliation)? Flag for: Missing Discovery Demand + cross-examination of the officer and video custodian.
