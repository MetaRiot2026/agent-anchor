#!/usr/bin/env python3
"""
Agent Anchor Sync Script
Run this on your agent's heartbeat to keep the dashboard updated.
Place in your workspace scripts/ folder and call from heartbeat.
"""
import json
import os
from datetime import datetime, timezone

STATE_FILE = os.path.expanduser("~/.openclaw/skills/agent-anchor/state-anchor.json")

def sync_state(agent_context=None):
    """
    Sync agent state to the dashboard state file.
    Call this from your heartbeat cron.
    
    Args:
        agent_context: dict with keys like 'tasks', 'cronJobs', 'revenue', etc.
                      If None, reads from current state and updates timestamp only.
    """
    # Load existing state or create fresh
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            state = json.load(f)
    else:
        state = {'version': '1.0.0', 'tasks': {}, 'cronJobs': [], 'auditLog': [], 'systemLog': []}
    
    # Update timestamp
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    state['lastUpdated'] = now
    state['syncMeta'] = {
        'lastSync': now,
        'syncInterval': '3 minutes',
        'source': 'heartbeat'
    }
    
    # If agent_context provided, merge it in
    if agent_context:
        for key in ['tasks', 'cronJobs', 'auditLog', 'systemLog', 'revenue', 'contacts']:
            if key in agent_context:
                state[key] = agent_context[key]
    
    # Add sync entry to audit log
    time_str = datetime.now(timezone.utc).strftime('%I:%M %p')
    if 'auditLog' not in state:
        state['auditLog'] = []
    state['auditLog'].append({
        'time': f'{datetime.now(timezone.utc).strftime("%m/%d/%Y, ")}{time_str}',
        'action': 'Heartbeat sync — dashboard updated',
        'tag': 'done'
    })
    
    # Keep last 20 audit entries
    if len(state['auditLog']) > 20:
        state['auditLog'] = state['auditLog'][-20:]
    
    # Save
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)
    
    return now

if __name__ == "__main__":
    result = sync_state()
    print(f"Agent Anchor synced: {result}")