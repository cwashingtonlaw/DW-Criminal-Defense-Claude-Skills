# Mapping & Visualization Guidance

Cell site evidence is inherently spatial — juries need to see coverage areas, tower locations, and the relationship between the data and the prosecution's claims. While this skill does not generate maps directly, it provides guidance for creating effective defense visual exhibits.

## Defense Mapping Exhibit Checklist

**What the prosecution's map probably shows (and why it's misleading):**
- A tower icon at the site location with a narrow wedge pointing in the sector's azimuth direction
- The crime scene marked within the wedge
- An implied conclusion that the phone was "at" the crime scene

**What the defense map should show:**
- [ ] The **full coverage area** of the relevant sector — not just the azimuth direction, but the realistic RF coverage footprint (request this from a defense RF expert or use propagation modeling tools)
- [ ] The defendant's claimed location (home, work, etc.) plotted relative to the same sector coverage area — if it falls within the same coverage area, the CSLI data does not distinguish between the two locations
- [ ] **All towers** the phone connected to during the relevant period, with coverage areas shown — this provides context and may show the phone connecting to towers inconsistent with the prosecution's claimed location
- [ ] Overlap zones where multiple sectors or towers cover the same area — demonstrating that tower selection is not deterministic
- [ ] For tower dumps: the geographic area captured by the dump, with the number of innocent devices highlighted
- [ ] For geofence warrants: the geofence boundary with the accuracy radii of captured data points overlaid — showing that some devices "inside" the geofence may actually have been outside it

## Recommended Defense Expert Types

| Evidence Type | Expert Discipline | What They Provide |
|--------------|-------------------|-------------------|
| Historical CSLI | RF engineer / Cell site analyst | Propagation analysis, drive testing, coverage mapping, rebuttal of prosecution analyst |
| Tower dump | RF engineer + data analyst | Coverage area analysis, statistical context for innocent device capture |
| Cell site simulator | RF engineer + surveillance technology expert | CSS detection, methodology challenge, NDA/parallel construction exposure |
| GPS tracking | GPS/GNSS engineer | Accuracy assessment, multipath analysis, data integrity review |
| Geofence warrant | Digital forensics expert + location data analyst | Data source analysis, accuracy assessment, scope challenge |
| Wi-Fi positioning | Network engineer | Access point verification, database accuracy assessment |
