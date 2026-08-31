# Quick Reference — Key SQLite Database Paths by Platform and Forensic Tool WAL Handling

Read this file when identifying case-relevant databases (Steps 1-4) and when documenting tool deficiencies (Step 5) — it holds the iOS and Android database path tables and the forensic tool WAL-handling comparison.

### iOS (common case-relevant databases)
| Database | Path | Contains |
|----------|------|----------|
| sms.db | /private/var/mobile/Library/SMS/sms.db | iMessage and SMS/MMS |
| call_history.db | /private/var/mobile/Library/CallHistoryDB/CallHistory.storedata | Call logs |
| AddressBook.sqlitedb | /private/var/mobile/Library/AddressBook/AddressBook.sqlitedb | Contacts |
| Safari/History.db | /private/var/mobile/Library/Safari/History.db | Browse history |
| locationd/consolidated.db | /private/var/mobile/Library/Caches/locationd/consolidated.db | Location data |
| Photos.sqlite | /private/var/mobile/Media/PhotoData/Photos.sqlite | Photo metadata, GPS |
| ChatStorage.sqlite | WhatsApp app container | WhatsApp messages |

### Android (common case-relevant databases)
| Database | Path | Contains |
|----------|------|----------|
| mmssms.db | /data/data/com.android.providers.telephony/ | SMS/MMS |
| contacts2.db | /data/data/com.android.providers.contacts/ | Contacts |
| calllog.db | /data/data/com.android.providers.contacts/ | Call logs |
| msgstore.db | /data/data/com.whatsapp/ | WhatsApp messages |
| wa.db | /data/data/com.whatsapp/ | WhatsApp contacts |
| History | /data/data/com.android.chrome/app_chrome/Default/ | Chrome history |

Each of these databases may have a companion -wal and -shm file. Every one of them is a potential source of recovered deleted data.

---

## Quick Reference — Common Forensic Tool WAL Handling

| Tool | WAL Handling | Defense Concern |
|------|-------------|-----------------|
| **Cellebrite UFED/PA** | Auto-merges WAL on import | Destroys original WAL transaction history; no option to preserve pre-merge state in standard workflow |
| **MSAB XRY** | Auto-merges WAL; known merge errors | Documented cases of phantom artifacts from incorrect WAL merge; may produce false records |
| **Magnet AXIOM** | Auto-merges; preserves original as option | Better than Cellebrite/XRY, but default behavior is still destructive; verify examiner enabled preservation |
| **SQLite Forensic Explorer** | Preserves WAL; independent frame analysis | Gold standard for defense work; parses WAL unused space; visual transaction timeline |
| **Belkasoft Evidence Center** | Preserves WAL; carves all three zones | Strong independent verification tool; parses freelist and unallocated space |
| **Oxygen Forensic Detective** | Configurable WAL handling | Verify configuration used; can preserve or merge depending on settings |
