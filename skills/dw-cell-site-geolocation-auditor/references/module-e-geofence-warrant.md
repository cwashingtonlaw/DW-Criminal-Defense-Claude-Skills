# Module E — Geofence Warrant Audit

Geofence warrants (also called "reverse location warrants") are a relatively new investigative technique where law enforcement asks a technology company (most commonly Google) to identify all devices present within a defined geographic area during a defined time window.

## How Geofence Warrants Work (Google / Sensorvault)

Google's implementation is the most common and follows a three-step process:

1. **Step 1:** Law enforcement defines the geographic area (geofence) and time window. Google searches its Sensorvault database and returns anonymized device identifiers and location data points for all devices within the geofence.
2. **Step 2:** Law enforcement reviews the anonymized data and narrows the list, requesting additional location data (expanded time window or travel patterns) for specific anonymized devices.
3. **Step 3:** Law enforcement identifies specific devices of interest and requests de-anonymization — Google provides the account holder's identifying information.

## Geofence Warrant Audit Points

**Scope and Particularity:**
- [ ] How large was the geographic area defined in the geofence? (A geofence encompassing a city block in a dense area may capture hundreds of devices)
- [ ] How long was the time window? (Broader windows capture more innocent users)
- [ ] Was the geofence drawn to match the crime scene, or was it expanded to include surrounding areas?
- [ ] How many total devices were captured in the initial return?
- [ ] What criteria were used to narrow from Step 1 to Step 2, and from Step 2 to Step 3? Were these criteria objective or subjective?

**Data Source and Accuracy:**
- [ ] What data sources contributed to the location points? (Google Location History uses a blend of GPS, Wi-Fi, cell, and Bluetooth — accuracy varies by source)
- [ ] Does each data point include an accuracy estimate? Were points with large accuracy radii (50+ meters) used to place a device within the geofence?
- [ ] Could a device physically outside the geofence appear inside it due to location estimation error?
- [ ] Were any devices excluded that should have been included, or vice versa?

**Legal Challenges:**
Geofence warrants face serious constitutional challenges, and the law is still developing:

- **Particularity:** The 4th Amendment requires warrants to particularly describe the place to be searched and the persons or things to be seized. A geofence warrant that captures all devices in an area is arguably a "general warrant" — the very thing the 4th Amendment was designed to prevent.
- ***United States v. Chatrie***, 590 F. Supp. 3d 901 (E.D. Va. 2022) — the most comprehensive judicial analysis of geofence warrants to date. The court found the geofence warrant was an unconstitutional general search but applied the good-faith exception. The analysis is highly useful even where the result was not suppression.
- **5th Circuit:** Monitor for circuit-specific geofence rulings. Several state courts have begun addressing geofence warrants.
- **State law:** Some states have enacted legislation specifically addressing geofence warrants — check whether Louisiana has done so.
