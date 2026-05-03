# Module G — Key Event Detection

*REPLICATES MirandaAI's automatic key event flagging*

**Runs on all file types.** Automatically detect and timestamp these event categories:

| Event Type | Detection Patterns |
|------------|-------------------|
| **Traffic Stop** | "License and registration," "Do you know why I pulled you over," engine/siren sounds described |
| **Arrest** | "You're under arrest," "Turn around," "Hands behind your back," handcuff sounds |
| **Search** | "Mind if I search," "Consent to search," "Step out of the vehicle," "What's in your pocket" |
| **Use of Force** | "Stop resisting," "Get on the ground," "Taser," physical altercation, screaming |
| **Pursuit** | Running, "Stop," "He's running," heavy breathing |
| **Sobriety Test** | "Walk heel to toe," "Follow my finger," "Breathalyzer," "Blow into this" |
| **Weapon Discovery** | "Gun," "knife," "weapon found," "What is this" |
| **Drug Discovery** | "What's this substance," "Is this yours," field test references |
| **Medical Event** | "Are you hurt," "Call an ambulance," "He's bleeding," medical complaint |
| **Witness Contact** | "Did you see what happened," "Can you tell me," witness statements |
| **911 Content** | Caller description, reported crime, location, suspect description |

For each detected event:
```
KEY EVENT [KE-001]
File: [name] @ [timestamp]
Type: [from table above]
Description: [What happened in 1–2 sentences]
Speakers Involved: [list]
Defense Relevance: [Why this matters — e.g., "No consent given before search"]
```
