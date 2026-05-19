---
name: reflect
description: Review the five most recent local conversation logs and surface useful reflection candidates, especially user preferences, agent memory, workflow patterns, and product learnings. Use when the user asks to reflect, review recent conversations, update memory from conversations, or calibrate the second-brain agent from past interactions.
---

# Reflect Skill

Reflect means reviewing recent user-agent conversations to find durable learnings.

Use this skill when the user explicitly asks to reflect, review recent conversations, learn from recent conversations, update memory from conversations, or calibrate the second-brain agent.

## Principle

Keep reflection lightweight and judgment-based.

The goal is not to summarize every conversation. The goal is to identify what should help the agent complete future tasks better, work more efficiently, and match the user's preferences more closely.

## Inputs

Use the five most recent conversation logs from:

```text
conversations/*.jsonl
```

Each line is one message:

```json
{"timestamp":"...","role":"user","message":"..."}
{"timestamp":"...","role":"assistant","message":"..."}
```

If fewer than five logs exist, use all available logs.

Ignore hidden files, `.gitignore`, hook state, and Codex's global trace files unless the user explicitly asks for them.

## Workflow

1. Read the standing context files:
   - `knowledge_base/vault_context.md`
   - `knowledge_base/user_preferences.md`
   - `knowledge_base/agent_memory.md`
2. Find the five most recent `conversations/*.jsonl` files.
3. Read the conversation logs in chronological order.
4. Inspect relevant context when needed to better understand context from past conversations
   - Open only the notes needed to understand the conversation.
5. Extract durable candidates to self-improve
   - User preferences: communication style, workflow expectations, pet peeves, recurring corrections.
   - Agent memory: vault conventions, setup facts, recurring workflows, tooling facts.
   - Product or strategy learnings: ideas that belong in normal knowledge-base notes, not memory files.
   - Open questions: things that need the user's judgment before saving.
6. Filter out:
   - One-off task details.
   - Temporary implementation steps.
   - Raw source summaries.
   - Secrets, credentials, tokens, or private keys.
   - Large copied conversation excerpts.
7. Present a concise reflection report before editing anything.

## Report Format

Start with a short answer:

- How many conversation logs were reviewed.
- Whether there are worthwhile memory/preference candidates.

Then present your findings, and proposed changes to the user. Ask clarification questions if needed. 

## Editing Rule

After presenting the report, ask the user which candidates they want saved.

Before changing any memory, preference, raw source, index, or knowledge-base file, show the concrete proposed changes and ask for confirmation.

After edits, ask whether the user wants the changes pushed to GitHub.
