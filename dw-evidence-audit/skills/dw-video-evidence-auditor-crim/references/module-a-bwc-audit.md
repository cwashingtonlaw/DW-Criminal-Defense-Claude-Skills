# MODULE A — Body-Worn Camera Audit

## Activation Compliance

The single most important BWC audit question: **was the camera activated when policy required it to be?**

**Pre-Event Buffer:**
Most BWC systems record a continuous pre-event buffer (typically 30 seconds to 2 minutes of video without audio). When an officer presses the record button, the buffer is saved as the beginning of the recording. This means:
- The recording starts with a buffer period that has video but no audio — this is normal and expected
- The buffer length reveals how long before the officer pressed record the camera was already capturing
- If the buffer is shorter than the system's configured buffer length, the camera may have been recently powered on — raising the question of why it wasn't already running

**Activation Gap Analysis:**
For each officer's BWC, map the timeline:

```
ACTIVATION GAP ANALYSIS — Officer [Name/Badge]
Camera System: [Axon Body 3 / Motorola V300 / etc.]
Configured Buffer: [30 sec / 60 sec / 120 sec]

DISPATCH ─────────── ARRIVAL ─────────── KEY EVENT ─────────── ARREST
[time]                [time]               [time]                [time]
     |←── GAP 1 ──→|     |←── GAP 2 ──→|      |←── GAP 3 ──→|
     no recording        recording active       camera off?

GAP 1: [Duration] — dispatch to first recording. Policy requires activation [when?]
GAP 2: [Duration] — any mid-incident gaps (camera turned off/on)
GAP 3: [Duration] — any post-key-event gaps before booking/transport recording
```

**Policy Compliance Checklist:**
- [ ] Camera activated upon dispatch or arrival (per agency policy)?
- [ ] Camera remained active throughout the entire encounter?
- [ ] If camera was deactivated mid-encounter, was the reason documented?
- [ ] Camera active during all uses of force?
- [ ] Camera active during all statements by the defendant?
- [ ] Camera active during all searches (person, vehicle, premises)?
- [ ] Camera active during Miranda warnings (if given)?
- [ ] Camera active during transport?
- [ ] If multiple officers responded, do all officers' cameras account for the full incident?

**Common BWC Systems — Technical Details:**

| System | Buffer | Resolution | Battery Life | Storage | Key Defense Notes |
|--------|--------|-----------|-------------|---------|-------------------|
| Axon Body 3 | 30s-120s (configurable) | Up to 1080p | ~12 hrs | Cloud (Evidence.com) | Axon metadata includes GPS, accelerometer data; Evidence.com audit log shows every access/export |
| Axon Body 4 (Axon 4) | 30s-120s | Up to 1080p+ | ~12 hrs | Cloud (Evidence.com) | Live streaming capability — was it used? Audit log available |
| Motorola V300 | 30s-120s | Up to 1080p | ~12 hrs | CommandCentral Vault | GPS metadata; auto-activation triggers configurable |
| Motorola Si500 | 30s-120s | Up to 1080p | ~12 hrs | CommandCentral Vault | Integrated with radio — can auto-activate on radio events |
| WatchGuard V300 | Configurable | Up to 1080p | Varies | Local/cloud | Older systems may have lower resolution |
| Getac | Varies | Up to 1080p | Varies | Local/cloud | Less common; verify specifications |

## Perspective & Content Limitations

BWC footage is not a neutral recording of events — it is a recording from the officer's chest or shoulder, facing the direction the officer faces, with the limitations of a wide-angle lens mounted on a moving human body.

**Field of View:**
- Most BWCs use a wide-angle lens (120°-140° horizontal FOV)
- Wide-angle creates barrel distortion at the edges — objects appear farther away and smaller at the periphery than they actually are
- The camera captures what is in front of the officer — it does not capture what is behind, to the side, or above/below the officer's line of sight
- When an officer turns their head, the camera (mounted on the chest/shoulder) may not follow — creating a mismatch between what the officer saw and what the camera captured

**Audio Limitations:**
- BWC microphones are omnidirectional but have limited range — typically reliable to 10-15 feet in quiet environments, significantly less in noisy conditions
- Wind noise, traffic, crowds, and radio chatter can render audio unintelligible
- The officer's own voice is always closest to the microphone — creating a volume imbalance where the officer sounds clear but the subject may be barely audible
- Pre-event buffer has NO audio — anything said during the buffer period is lost

**Low-Light / Night Performance:**
- BWC infrared capability varies by model — some switch to IR automatically, some require manual activation
- IR mode produces monochrome video that loses color information
- Transition between well-lit and dark areas causes auto-exposure adjustment delays — creating periods of over- or under-exposed footage
- Flashlight-mounted cameras create a cone of illumination that makes everything outside the cone invisible

**Motion & Stability:**
- During foot pursuits, physical altercations, or any rapid movement, BWC footage becomes chaotic — frames blur, perspective shifts rapidly, and it becomes extremely difficult to determine spatial relationships
- Jurors watching stabilized, slow-motion replay in a courtroom experience the footage very differently from the officer experiencing real-time, unstabilized motion

---

## Moved from SKILL.md — Module A summary

The single most important BWC audit question: **was the camera activated when policy required it to be?** Map activation gaps across the timeline (dispatch → arrival → key event → arrest), apply the Policy Compliance Checklist (use of force, statements, searches, Miranda, transport), and assess perspective and content limitations (field of view, audio range, low-light performance, motion stability) that shape what the camera captured versus what the officer experienced.
