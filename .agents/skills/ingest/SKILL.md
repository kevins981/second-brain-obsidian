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

## Proactive Ingest Default

When a new source is added, make a best-effort classification and recommendation after reading the source and nearby context. The user should not have to classify sources from scratch.

Do not hand the user open-ended classification work, such as asking whether a source is current, relevant, or authoritative, unless the answer materially affects the next action and cannot be reasonably inferred.

Instead, state:

- What the source appears to be.
- How it seems to relate to the existing knowledge base.
- The recommended treatment.
- What uncertainty remains.
- The concrete next action you propose.

Use cautious labels when needed, but still move the work forward.

Ask the user to decide only when:

- Multiple plausible treatments would lead to meaningfully different edits.
- The source may be sensitive, stale, or private.
- You are about to change maintained knowledge in a way that affects product direction, strategy, or other high-impact conclusions.
- The source contradicts existing maintained notes.

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
- Recommend how the source should be treated after reading it and nearby context.
- Ask short, easy-to-answer confirmation questions only at real decision points.
- Propose the knowledge-base notes or index updates you plan to make.
- Ask for permission before making those edits.
- Link knowledge-base notes back to the raw source so the original material remains traceable.

## Useful Questions

Prefer recommendation-shaped questions that help the user give quick judgment.

Instead of asking:

- Should this update existing notes, create new notes, or just be indexed for now?

Say:

- I recommend indexing this source now and creating a separate maintained note because it introduces a distinct angle. Does that sound right before I edit maintained notes?

These are examples, not a fixed script. Ask what the situation calls for.

## Updates

When ingest changes the vault, update the relevant index files:

- `raw_sources/raw_sources_index.md`
- `knowledge_base/knowledge_base_index.md`

If the interaction reveals a durable preference or operational fact, update the relevant memory file:

- `knowledge_base/user_preferences.md`
- `knowledge_base/agent_memory.md`

After edits, ask whether the user wants the changes pushed to GitHub.
