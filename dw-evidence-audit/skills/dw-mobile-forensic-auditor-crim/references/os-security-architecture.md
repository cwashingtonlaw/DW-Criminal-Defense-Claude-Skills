# OS Security Architecture Tables

Read at STEP 3 (OS Security Verification) of `dw-mobile-forensic-auditor-crim/SKILL.md` — the Apple iOS and Android security-layer tables with defense implications.

### Apple iOS Security Architecture

| Security Layer | Defense Implications |
|---------------|---------------------|
| **Secure Enclave Processor (SEP)** | Hardware-isolated coprocessor manages encryption keys, biometric data, and passcode verification. Keys never leave the SEP. No commercial tool can extract SEP contents directly. If the examiner claims to have bypassed SEP protections, demand: exploit documentation, tool validation for this specific iOS version, and peer review. |
| **Data Protection Classes** | iOS uses per-file encryption classes (Complete Protection, Protected Unless Open, Protected Until First Authentication, No Protection). A Logical extraction typically only accesses "No Protection" and "Protected Until First Authentication" classes. Files in "Complete Protection" (most messaging apps, health data, some photos) require device unlock state at extraction time — verify this was documented. |
| **Keychain** | Stores passwords, tokens, certificates. Accessible only via FFS+ on jailbroken devices or via GrayKey/Cellebrite Premium exploits on specific iOS versions. If keychain data appears in a Logical extraction, flag as anomalous — investigate how it was obtained. |
| **iOS Version-Specific Barriers** | Exploits are version-dependent. An exploit validated for iOS 14.x may fail silently on iOS 16.x and produce an incomplete extraction without logging the failure. Always cross-reference: device iOS version vs. tool's published supported version matrix. |
| **USB Restricted Mode (iOS 11.4.1+)** | After 1 hour without unlock, Lightning/USB-C data connection is disabled. If the device was seized powered off or locked for >1 hour, physical/FFS extraction requires a bypass of USB Restricted Mode. Was this documented? |

### Android Security Architecture

| Security Layer | Defense Implications |
|---------------|---------------------|
| **File-Based Encryption (FBE) — Android 7.0+** | Replaces Full Disk Encryption. Each file encrypted with a unique key derived from user credentials + hardware-bound key. Before First Unlock (BFU): only Device Encrypted (DE) storage accessible — no user data. After First Unlock (AFU): Credential Encrypted (CE) storage becomes accessible. Verify: was the device in BFU or AFU state at extraction? If BFU, the extraction captured almost no user-generated content. |
| **Hardware-Backed Keystore** | Similar to Apple's SEP — Titan M (Google Pixel), Knox (Samsung), TrustZone (Qualcomm). Key material is hardware-bound and cannot be extracted by software alone. |
| **Verified Boot / dm-verity** | Ensures system partition integrity. If the examiner rooted the device for extraction, dm-verity may have triggered a factory reset or flagged the boot state — potentially destroying evidence. Was this risk documented? |
| **Android Version Fragmentation** | Samsung, Google, OnePlus, etc. implement security differently atop stock Android. A tool validated for Samsung Galaxy S21 on Android 12 is NOT validated for Pixel 6 on Android 12. Always check: OEM + model + Android version + security patch level vs. tool's supported device matrix. |
| **Secure Folder / Knox (Samsung)** | Samsung devices with Knox may have a Secure Folder that operates as a separate encrypted workspace. Standard extractions — even FFS — may not access Secure Folder contents without the Secure Folder credential. Was Secure Folder presence checked? Was its content extracted or ignored? |
