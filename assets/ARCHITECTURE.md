# Architecture Diagram

```text
Participants
     |
     v
Camp Wi-Fi or VPN (authorized lab only)
     |
     v
Challenge Gateway
     |
     +--> Linux / Networking
     +--> Web Lab
     +--> Forensics Files
     +--> Crypto Notes
     +--> Reverse Engineering VM
```

## Safety Zones

- All lab addresses should be private or documented test ranges.
- Public internet access should be disabled for vulnerable systems.
- Organizer controls should be separate from participant access.
