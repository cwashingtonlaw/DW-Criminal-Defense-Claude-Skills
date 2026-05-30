# MODULE C — Surveillance / CCTV Audit

## System & Recording Integrity

Surveillance video raises a different set of challenges from BWC footage. The camera is stationary (usually), but the recording systems are often older, lower quality, and managed by non-law-enforcement entities.

**Timestamp Accuracy:**
- CCTV systems are notorious for inaccurate timestamps. Clocks drift, daylight saving time changes are missed, and initial setup may have been incorrect.
- Demand documentation of how the system clock was verified against an independent time source (NTP server, cell phone clock, CAD timestamp comparison).
- If the CCTV timestamp differs from CAD/dispatch timestamps by more than a few seconds, flag it — the temporal relationship between the video and reported events is unreliable.

**Recording Schedule & Retention:**
- Was the system recording continuously or on motion detection? Motion-detection recording creates gaps during periods of no movement — which may coincide with critical moments.
- What is the system's retention period? If footage was requested after the standard retention period, was it still available? If not, when was it overwritten — could it have been preserved with a timely request?
- If law enforcement was aware of relevant surveillance footage and failed to preserve it before the retention period expired, this is a spoliation argument.

**Export Integrity:**
- How was the footage exported from the surveillance system? Native format vs. converted format?
- Native format typically requires proprietary player software — was that software provided to the defense?
- Converted formats (MP4, AVI) involve re-encoding that can alter timestamps, frame rates, and image quality. Was the conversion process documented?
- Were any frames or segments removed during export? Does the file's metadata show editing artifacts?

**Multi-Camera Systems:**
- If the system has multiple cameras, were all relevant camera angles provided? Were any cameras non-functional?
- Can footage from different cameras be synchronized to create a composite timeline?
- Were camera coverage maps or placement diagrams provided?

## CCTV Audit Checklist
- [ ] Timestamp verified against independent source
- [ ] Recording mode documented (continuous vs. motion-detection)
- [ ] Retention policy documented — was footage preserved timely?
- [ ] Export method documented — native or converted?
- [ ] If converted, was conversion process and software documented?
- [ ] All relevant camera angles provided?
- [ ] Non-functional cameras identified and documented?
- [ ] Proprietary player provided (if native format)?
- [ ] Chain of custody from system owner to law enforcement documented?
- [ ] System maintenance and calibration records available?
