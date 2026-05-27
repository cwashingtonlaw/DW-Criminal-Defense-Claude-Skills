# Video-by-Video Timestamp Log Format

Before the narrative audit report, generate a **detailed timestamp log** for each video file. This becomes the factual foundation for the audit and cross-examination.

## Timestamp Log Format

Produce the log as a section within the Word document (.docx) audit report, or as a separate table in the appendix if the case involves many video files.

For each video file:

```
VIDEO FILE LOG — [Filename]
Source: [BWC - Officer Name/Badge | Dash Cam - Unit # | CCTV - Location/Camera # | etc.]
System: [Axon Body 3 | Motorola V300 | Hikvision NVR | iPhone 15 | etc.]
Duration: [HH:MM:SS]
Format: [MP4 / AVI / proprietary / etc.]
Resolution: [1080p / 720p / etc.] | Frame Rate: [30fps / 15fps / etc.]
File Size: [X GB/MB]
Metadata Timestamp: [Start time per file metadata]
Verified Timestamp: [Start time per independent source, if available]

TIME        | CONTENT DESCRIPTION              | REPORT COMPARISON           | FLAG
─────────────────────────────────────────────────────────────────────────────────────
00:00-00:30 | Pre-event buffer (no audio)      | N/A                         |
00:30       | Audio begins — officer approach   | Report states arrival at    | ⚠ TIME
            |                                  | [different time]            | DISCREPANCY
01:15       | Contact with subject begins      | Report states [X]           |
01:45       | Subject makes statement "[Y]"    | Not mentioned in report     | ⚠ OMISSION
02:30       | Officer turns away — subject     | Report states officer       | ⚠ PERSPECTIVE
            | not visible for 8 seconds        | maintained visual contact   | GAP
03:00       | Use of force begins              | Report states [X]           | ⚠ DISCREPANCY
03:15-03:45 | Camera obscured (hand/body)      | Report describes events     | ⚠ CAMERA
            |                                  | during this period          | OBSTRUCTION
04:00       | RECORDING ENDS                   |                             |
─────────────────────────────────────────────────────────────────────────────────────

ACTIVATION GAPS:
• Dispatch at [time] → Recording begins at [time] = [X min] unrecorded
• Recording stops at [time] → Resumes at [time] = [X min] unrecorded

CONTENT-VS-REPORT DISCREPANCIES: [count]
PERSPECTIVE GAPS: [count] — total unviewable time: [X seconds]
AUDIO GAPS: [count] — total inaudible time: [X seconds]
```

## Flag Types

| Flag | Meaning |
|------|---------|
| ⚠ TIME DISCREPANCY | Timestamp on video contradicts timestamp in report or CAD records |
| ⚠ OMISSION | Event visible/audible on video is not mentioned in the officer's report |
| ⚠ DISCREPANCY | Event described differently in the report than what the video shows |
| ⚠ PERSPECTIVE GAP | Camera angle, obstruction, or officer position prevents viewing a key event |
| ⚠ CAMERA OBSTRUCTION | Camera physically blocked by hand, body, object, or equipment |
| ⚠ AUDIO GAP | Audio unintelligible, absent (buffer period), or obscured by noise |
| ⚠ ACTIVATION GAP | Period when camera should have been recording but was not |
| ⚠ DEACTIVATION | Officer manually stopped recording — was the reason documented? |
| ⚠ MISSING VIDEO | Video that should exist (per policy, per other evidence) does not appear in discovery |
