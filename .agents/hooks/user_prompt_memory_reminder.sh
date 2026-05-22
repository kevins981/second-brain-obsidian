#!/usr/bin/env bash

cat <<'EOF'
System Reminder: Check whether the user's latest message indicates a durable preference, workflow preference, correction, or operational fact worth remembering. If so, ask the user to confirm whether they want it saved. If confirmed, update `knowledge_base/user_preferences.md` or `knowledge_base/agent_memory.md` according to `AGENTS.md`. If the user says "remember this" or similar phrases, you must save this somewhere. Otherwise, continue.
EOF

exit 0
