# Charge Type Priorities & Lens Depth Specification

## Quick Reference — Data Category Priorities by Charge Type

| Charge Type | Priority Data Categories | Primary Lenses (Full Depth) | Secondary Lenses (Scan) | Chunk Override |
|-------------|------------------------|---------------------------|----------------------|---------------|
| Homicide / Manslaughter | Timeline, location, victim comms, videos, third-party | Alibi, Self-Defense, Third-Party, Contradictions | State of Mind, Victim Cred, Gaps | Location → T1 |
| Sexual Offense | Complainant comms, consent messages, relationship, videos | Victim Cred, Relationship, State of Mind, Contradictions | Alibi, Third-Party, Self-Defense | Victim comms → T1 |
| Drug Offenses | Call frequency, contacts, location, financial apps, videos | Third-Party, Contradictions, Gaps | Alibi, State of Mind, Self-Defense | Call logs → T1 |
| Robbery / Burglary | Location, communications, videos, device activity | Alibi, Timeline, Third-Party, Contradictions | State of Mind, Victim Cred | Location → T1 |
| Assault / DV | Victim comms, threats received, self-defense, videos, health data | Self-Defense, Victim Cred, State of Mind, Contradictions | Alibi, Third-Party, Gaps | Victim comms → T1 |
| Weapons Offenses | Possession comms, photos/videos/EXIF, location | Alibi, Third-Party, Contradictions | State of Mind, Self-Defense | Photos/Videos → T2 |
| LWOP-Eligible | ALL at maximum depth | **ALL eight — Full Depth** | **None — no scan mode** | Full tiers |

## Lens Depth Specification

**Full Depth (actively hunt):** The primary lenses listed in the Charge Type table above for the current charge. Run every checklist item, every programmatic analysis, every pattern check.

**Scan Depth (flag obvious finds only):** Secondary lenses not listed as primary for the current charge. Note anything that jumps out during full-depth analysis of other lenses, but do not actively hunt. This cuts analysis time roughly in half for non-priority lens-category combinations.

**Exception: LWOP-eligible cases — ALL lenses at Full Depth. No shortcuts.**