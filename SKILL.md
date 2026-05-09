---
name: agent-anchor
description: Crash-proof dashboard for OpenClaw. Your AI agent's memory that survives everything. Automatically snapshots state every 3 minutes so your agent resumes exactly where it left off after restarts. Features: task tracker, terminal view, cron job monitoring, activity calendar, click-to-expand on any item.
---

# Agent Anchor

Crash-proof dashboard for OpenClaw. Your AI agent's memory that survives everything.

## What It Does

Agent Anchor keeps your OpenClaw agent running smoothly — even through crashes, restarts, and interruptions. It continuously snapshots state so your agent resumes exactly where it left off.

## Features

- **Crash Recovery** — Automatically saves state every 3 minutes
- **Task Tracker** — Organize tasks into In Progress, Staged, and Completed
- **Terminal View** — See live system status
- **Cron Job Monitoring** — Click any job to see details, fix errors with one click
- **Activity Calendar** — Look back at your agent's history by date
- **Click-to-Expand** — Inspect any task or cron job for full details

## Quick Install

```bash
cd ~/.openclaw/skills
openclaw skills list
# Find "agent-anchor" and note the source path
# Then serve the dashboard:
cd ~/.openclaw/skills/agent-anchor
python3 -m http.server 3456
```

Then open http://localhost:3456

## Auto-Sync Setup (For Your Agent)

Add this to your heartbeat to keep the dashboard live:

```python
import json, os
from datetime import datetime, timezone

STATE = os.path.expanduser("~/.openclaw/skills/agent-anchor/state-anchor.json")

def sync_state():
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    if os.path.exists(STATE):
        with open(STATE) as f: s = json.load(f)
    else:
        s = {'tasks':{},'cronJobs':[],'auditLog':[],'systemLog':[]}
    s['lastUpdated'] = now
    s['syncMeta'] = {'lastSync': now, 'syncInterval': '3min', 'source': 'heartbeat'}
    t = datetime.now(timezone.utc).strftime('%I:%M %p')
    s.setdefault('auditLog', []).append({'time': f'5/9/2026, {t}', 'action': 'Heartbeat sync', 'tag': 'done'})
    s['auditLog'] = s['auditLog'][-20:]
    with open(STATE, 'w') as f: json.dump(s, f, indent=2)
```

Call `sync_state()` on every heartbeat poll.

## What Shows on the Dashboard

When your agent syncs, the dashboard shows:
- **Tasks** — In Progress, Staged, Completed (from heartbeat context)
- **Cron Jobs** — All scheduled jobs with status
- **Calendar** — History of everything your agent did
- **Terminal** — Live status messages

The dashboard polls `state-anchor.json` every 10 seconds — no extra setup needed.

## Customization

Edit `state-anchor.json` to customize:
- Task categories (inProgress, staged, completed)
- Revenue streams
- Contacts (hot, warm, cold)
- Cron jobs to monitor

## Price

$19 one-time via Stripe or $19 USDC on Base network

## Support

DM @theia_metariot on X/Twitter

---

Built by MetaRiot — Culture for the decentralized age.