---
name: ingest
description: Use when new raw sources are added, when the user asks to discuss or work from a source file, or when source material should be incorporated into the knowledge base.
---

# Ingest Skill

Ingest means turning source material into situated, traceable knowledge.

Use this skill when the user adds or points to source material, such as meeting notes, reports, exports, research notes, PDFs, transcripts, or drafts.

## Principle

First understand the source and where it fits. Then help with the user's immediate goal. After that, update the knowledge base when useful.

Do not assume a source is current, accurate, relevant, or authoritative just because it exists.

Read the source and relevant context before asking for editing permission. Do not ask permission just to inspect files.

Before editing `knowledge_base/`, `raw_sources/`, or index files, tell the user the concrete changes you plan to make and ask for permission.

## Starting Point

Use the vault's standing instructions and context files as described in `AGENTS.md`.

Read the source enough to understand what it appears to contain. Then read the relevant indexes and nearby notes to understand how it fits:

- `raw_sources/raw_sources_index.md`
- `knowledge_base/knowledge_base_index.md`
- Related notes or sources, as needed

## Two Common Modes

### Task-First Ingest

Use this when the user wants to do something immediate with the source, such as discuss it, extract decisions, answer questions, compare it to existing notes, or draft something from it.

In this mode:

- Understand the source and nearby context.
- Ask only the questions needed to do the immediate task well.
- Do the requested task first.
- Then propose any knowledge-base or index updates and ask for permission before making them.

### Knowledge-First Ingest

Use this when the user mainly wants the source added to the knowledge base.

In this mode:

- Understand the source and nearby context.
- Ask short, easy-to-answer questions about how the source should be treated.
- Propose the knowledge-base notes or index updates you plan to make after reading the source and nearby context.
- Ask for permission before making those edits.
- Link knowledge-base notes back to the raw source so the original material remains traceable.

## Useful Questions

Ask questions that help the user give quick judgment, such as:

- What do you want to get out of this source?
- Is this current enough to rely on?
- Should this be treated as a primary source, rough notes, background context, or archive?
- Should this update existing notes, create new notes, or just be indexed for now?

These are examples, not a fixed script. Ask what the situation calls for.

## Updates

When ingest changes the vault, update the relevant index files:

- `raw_sources/raw_sources_index.md`
- `knowledge_base/knowledge_base_index.md`

If the interaction reveals a durable preference or operational fact, update the relevant memory file:

- `knowledge_base/user_preferences.md`
- `knowledge_base/agent_memory.md`

After edits, ask whether the user wants the changes pushed to GitHub.
