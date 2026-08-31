# Investigation Seed

Read at SKILL.md MODULE E — Investigation Seed; holds the seed-contents table and the routing to the investigator tasking skill.

The intake conversation produces the **seed input** for `dw-defense-investigator-tasking-crim`. The seed is not the full investigation plan — it is the raw lead list. The investigator tasking skill turns it into prioritized assignments.

### Seed contents

| Category | What goes into the seed |
|---|---|
| **Witnesses** | Every person the client named or mentioned, with any contact info, last-known location, relationship to client/victim/co-defendants, and what the client thinks they saw or know |
| **Locations** | Every address, business, intersection, vehicle the client placed themselves or others at — with timestamps where possible |
| **Video sources** | Identified body-worn camera (which officer), dashcam, station video, business surveillance (which business, which entrance, which day), residential camera, doorbell camera, traffic cameras |
| **Devices** | Every device touched — what's in police custody, what's in client/family custody, what's been wiped or factory-reset |
| **Alibi witnesses** | If alibi is in play, every person who can place the client elsewhere, and any documentary corroboration (timestamps on receipts, GPS on phone, check-ins) |
| **Character witnesses** | Persons who can speak to client's reputation, employment, community standing — for bond hearings and (later) sentencing mitigation |
| **Records** | Records the investigator should pull — employment records, medical records, school records, military records, treatment records, prior counsel files |
| **Inconsistencies the client flagged** | Anywhere the client thinks the State has it wrong — these are investigative priority |

**Route:** Pass the seed to `dw-defense-investigator-tasking-crim` once retention is final. The investigator tasking skill produces the task list, witness questionnaires, scene checklists, and records-request packets.
