# Cloud vs. Local Data Provenance Reference

## Classification & Authentication Impact

When parsing the extraction, classify each data source as LOCAL (on-device flash storage) or CLOUD (pulled from iCloud, Google account, Samsung Cloud, or third-party cloud backups during extraction):

| Data Source | Provenance | Auth Impact | Defense Considerations |
|------------|-----------|-------------|----------------------|
| SMS/MMS stored in native database | LOCAL | Standard extraction auth | Native to device storage |
| iCloud Messages (synced) | CLOUD | Separate cloud auth chain needed — when was sync last performed? | May include items deleted from device |
| Photos in DCIM folder | LOCAL | Standard extraction auth | Native to device storage |
| iCloud Photos (synced) | CLOUD | Cloud auth — photos may include items deleted from device but retained in cloud | May be older than device deletion |
| Google Location History | CLOUD | Google account auth — not the device itself | Requires separate Google account warrant/consent |
| WhatsApp local database | LOCAL | Standard extraction auth | Native to device storage |
| WhatsApp cloud backup | CLOUD | Encrypted backup — separate key and chain of custody | Different chain than local extraction |
| Health data (Apple Health DB) | LOCAL | Standard extraction auth | Native to device storage |
| iCloud Keychain / Passwords | CLOUD | Sensitive — separate cloud auth | Requires cloud account authentication |

## Why This Matters

- Cloud data may include records NOT on the physical device (synced from another device, retained after deletion)
- Cloud data has a different chain of custody (Cellebrite → cloud API → data, vs. Cellebrite → device flash → data)
- Cloud sync timestamps may differ from device timestamps
- The State sometimes conflates cloud-sourced data with device-local data without disclosing the provenance
- If cloud data was pulled without a separate warrant/consent for the cloud account, it may be suppressible

## Action for Analysis

For each data category, note whether the records came from local storage or cloud sync. Flag any cloud-sourced data in the report's Authentication Chain section (Section 4) as requiring separate authentication foundation.