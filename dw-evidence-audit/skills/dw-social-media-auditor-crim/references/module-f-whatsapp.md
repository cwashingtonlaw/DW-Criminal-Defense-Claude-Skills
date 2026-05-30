# MODULE F — WhatsApp (Meta-owned)

| Architecture Feature | Defense Implications |
|---------------------|---------------------|
| **End-to-End Encryption** | All WhatsApp messages are E2EE by default. Meta cannot produce message content — only metadata (sender/receiver numbers, timestamps, group membership). Content is available only from device-side forensic extraction or if a participant provides it. |
| **Backup Vulnerability** | WhatsApp backups to Google Drive or iCloud may not be E2EE (E2EE backup is optional and must be enabled by the user). If law enforcement obtained content from a cloud backup, verify: was E2EE backup enabled? Was the backup obtained via separate legal process to Google/Apple? |
| **Phone Number = Identity** | WhatsApp accounts are tied to phone numbers, providing stronger attribution than username-based platforms — but phone numbers can be spoofed, SIM-swapped, or shared. |
| **Disappearing Messages** | WhatsApp supports disappearing messages (24 hours, 7 days, or 90 days). If enabled, messages are deleted from both devices. Preservation timing is critical. |
