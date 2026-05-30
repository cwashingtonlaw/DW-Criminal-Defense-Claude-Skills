# MODULE C — Snapchat

| Architecture Feature | Defense Implications |
|---------------------|---------------------|
| **Ephemeral by Design** | Snaps are deleted from servers after viewing (or after 30 days if unopened). Chat messages are deleted after both parties leave the chat (unless saved). This creates a fundamental preservation problem: if law enforcement did not send a preservation letter before the content expired, it is gone from Snapchat's servers permanently. |
| **Snap Map / Location** | Snap Map shares location data when enabled. However, location can be spoofed (developer mode, GPS spoofing apps), and Snap Map updates only when the app is actively open — it does not provide continuous location tracking. |
| **Memories & My Eyes Only** | Users can save Snaps to "Memories" (cloud-backed) or "My Eyes Only" (PIN-protected). Forensic extractions may or may not capture these depending on extraction type and device encryption state. |
| **Data Retention** | Snapchat retains: account metadata, login/logout logs, Snap send/receive timestamps (but not content after viewing), friend lists, and search history. Content is only available if preserved before expiration. |
| **Screenshot Notifications** | Snapchat notifies users when a screenshot is taken. If the prosecution's evidence is a screenshot, the defendant may have been notified — verify whether this notification is documented and whether it contradicts the prosecution's timeline. |
