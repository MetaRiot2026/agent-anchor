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
cd ~/.openclaw/workspace
mkdir -p agent-anchor
cd agent-anchor
# Then serve the dashboard:
python3 -m http.server 3456
```

Then open http://localhost:3456

## Setup

1. Copy the `agent-anchor/` folder to your OpenClaw workspace
2. Run `python3 -m http.server 3456` in the folder
3. Open http://localhost:3456
4. The dashboard will start tracking state automatically

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