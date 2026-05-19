# Second Brain Obsidian

Starter skeleton for an Obsidian vault managed with Codex agents.

This repo is meant to become a private personal knowledge base. Do not put private notes, source material, credentials, or conversation logs in a public fork.

## Requirements

Before setup, install and authenticate:

- GitHub CLI (`gh auth login`)
- Obsidian CLI
- Codex

## Recommended Setup

Use this public repo as the skeleton, then ask Codex to create your own private GitHub repo from it.

Copy this prompt into Codex:

```text
I want to create my own private second-brain Obsidian vault from this public skeleton:

https://github.com/kevins981/second-brain-obsidian

Please set it up for me.

Assumptions:
- GitHub CLI is installed and authenticated.
- Obsidian CLI is installed and available.
- Codex is installed.
- The new repository should be private.

Steps:
1. Clone the public skeleton repo.
2. Remove its existing Git history and GitHub remote.
3. Initialize a fresh Git repo for my private vault.
4. Create a new private GitHub repository for it.
5. Commit the skeleton files.
6. Push the new private repo to GitHub.
7. Open or register the folder as an Obsidian vault if the Obsidian CLI supports that on this machine.
8. Tell me the local folder path and GitHub repo URL when finished.

Do not upload conversation logs or other ignored/generated files.
Do not change the vault structure unless needed for setup.
```

## Add Your Existing Material

After setup, put your existing materials into `raw_sources/`.

You do not need to organize them first. Dump the files in, then let the agent inspect, map, ask questions, and organize/index them.

Examples of material that can go in `raw_sources/`:

- an existing Obsidian vault
- Notion, Google Docs, or other exports
- PDFs
- reports
- meeting notes
- rough notes
- old documents

`raw_sources/` means human-owned source material. `knowledge_base/` means agent-maintained synthesized knowledge.

## Initialize The Vault

After adding your existing material, copy this prompt into Codex from the root of your private vault:

```text
You are helping me initialize this Obsidian vault as a second-brain knowledge base.

The vault has two main areas:

- `raw_sources/`: original source files I already have. These may include rough notes, PDFs, reports, exports, meeting notes, outdated documents, or an existing Obsidian vault.
- `knowledge_base/`: the clean knowledge base that you will help write and maintain over time. This may start empty.

Your job is to create three setup files and two index files:

- `knowledge_base/vault_context.md`
- `knowledge_base/user_preferences.md`
- `knowledge_base/agent_memory.md`
- `raw_sources/raw_sources_index.md`
- `knowledge_base/knowledge_base_index.md`

Do not create the final index files immediately.

First, inspect the folder structure and review the files in each folder. For each file, infer only what you can from the file contents, such as what the file appears to discuss or contain.

Then do the initialization in two steps.

## Step 1: Understand the High-Level Context and User Preferences

Before asking about individual files, ask me a small set of high-level context and preference questions.

Ask context questions such as:

- Who are you?
- What are you trying to do with this vault?
- What is your role in this project or area?
- What is the broader context for this knowledge base?
- What kinds of help do you want from this second-brain assistant?

Ask preference questions such as:

- How do you want the agent to communicate with you?
- How much detail do you usually want?
- How should the agent handle uncertainty or assumptions?
- Are there workflow preferences the agent should remember?

Use my answers to understand how the vault should be interpreted.

Ask follow-up questions if things are unclear and you believe you require more context.

After you are satisfied, create:

- `knowledge_base/vault_context.md`
- `knowledge_base/user_preferences.md`
- `knowledge_base/agent_memory.md`

`knowledge_base/vault_context.md` should capture the stable context future agents need before working in the vault, including:

- Who I am
- What I am trying to do with this vault
- My role in the project or area
- The broader context for this knowledge base
- What kinds of help I want from this second-brain assistant
- Other information I specifically discuss that is useful

For these two files, update them if needed in this initial session:
- `knowledge_base/user_preferences.md` should capture durable preferences about how I want the agent to work with me, including communication style, workflow preferences, and recurring expectations.
- `knowledge_base/agent_memory.md` should capture durable operational memory about this vault, including conventions, setup facts, recurring workflows, and lessons learned.

Do not write the index files yet.

## Step 2: Verify the Files and Populate the Knowledge Base

After you understand the high-level context, ask me short, structured verification questions about the files.

Ask about the files one by one. If there are many files, ask about one small group at a time.

For each file, ask questions like:

- Is this file still up to date?
- Is this file still relevant?
- What role should this file play: primary source, rough notes, background context, outdated context, archive, or something else?
- Does this file represent the latest version of the idea or topic it discusses?
- Should this file be treated as authoritative, uncertain, or only useful as background?

Do not ask broad questions like:

- What is this file?
- Can you explain this document?
- Tell me everything I should know about this source.

As you go through the files, you may also begin creating useful notes in `knowledge_base/`.

The exact knowledge-base files to create are up to you. Use your judgment based on the vault context, the raw source contents, and my answers.

When a knowledge-base note is based on a raw source, link back to the relevant raw source file so the original material remains traceable.

Include any knowledge-base notes you create in `knowledge_base/knowledge_base_index.md`.

After I answer and you have created any useful knowledge-base notes, create the index files.

Each index entry should include:

- File path
- Short description based on your reading and my answers
- Purpose or role based on my answers
- Whether it is current or up to date
- Whether it is relevant
- Whether it is authoritative, uncertain, or background-only
- Any remaining uncertainty

If `knowledge_base/` is empty, still create `knowledge_base/knowledge_base_index.md` with a short placeholder saying no knowledge-base notes exist yet.

Important rules:

- Do not assume filenames are accurate.
- Do not assume a file is current.
- Do not assume a file is relevant.
- Do not assume a file is authoritative.
- The file description can come from your reading.
- The file's purpose, accuracy, relevance, authority, and recency must come from my answers.
- Ask me about the files one by one. If there are many files, ask about one small group at a time.
- Update `user_preferences.md` when I share a durable preference.
- Update `agent_memory.md` when you learn a durable operational fact about this vault.
```

## What Is Included

- `AGENTS.md`: operating instructions for future agents
- `knowledge_base/`: maintained notes and agent memory placeholders
- `raw_sources/`: human-owned source material and source index placeholder
- `.codex/`: Codex hook config and helper scripts
- `.agents/skills/`: local skills for vault maintenance
- `conversations/`: ignored local conversation logs

## Daily Use

After initialization, most work falls into a few common patterns.

### Add New Material

Put new files into `raw_sources/`. You do not need to organize them first.

Then ask Codex:

```text
I added new material to `raw_sources/`.

Please use the ingest skill to inspect it, update the indexes, and create or update any useful knowledge-base notes.
```

The ingest workflow should:

- inspect the new source material
- ask questions when currentness, relevance, or authority is unclear
- update `raw_sources/raw_sources_index.md`
- create or update notes in `knowledge_base/` when useful
- update `knowledge_base/knowledge_base_index.md`
- keep source links traceable

### Ask Questions

Ask questions directly. The agent instructions tell Codex to read the standing context files, check indexes, and open relevant notes or source files before answering.

Example prompts:

```text
Using the vault context, help me understand what I know about [topic].
```

```text
Search the vault for anything related to [topic] and summarize the useful context.
```

```text
What are the main open questions or uncertainties around [topic]?
```

### Draft New Work

Use the vault to draft new documents, plans, reports, meeting prep, or other artifacts.

Example prompts:

```text
Help me draft meeting prep for [meeting/person/project] using the relevant vault context.
```

```text
Draft a report about [topic] based on the relevant files in this vault.
```

```text
Turn these notes into a cleaner knowledge-base note.
```

```text
Create a first draft of [document] using files X, Y, and Z as source material.
```

For this kind of work, Codex should search the vault first instead of relying only on the latest prompt.

## Maintenance

The vault includes local skills for recurring maintenance tasks.

### `ingest`

Use this when adding new source material.

Typical prompt:

```text
Please use the ingest skill on the new files in `raw_sources/`.
```

Use it when:

- new files were added
- existing raw source files changed meaningfully
- source material needs to be turned into maintained notes
- indexes need to reflect newly added material

### `housekeeping`

Use this to keep the vault healthy and up to date.

Typical prompt:

```text
Please use the housekeeping skill to check the vault and clean up anything that needs routine maintenance.
```

Use it when:

- indexes may be stale
- memory files may need cleanup
- changed files need review
- the vault needs a general health check
- ordinary edits should be committed and pushed

### `organize`

Use this when the folder layout has become messy and should be reorganized.

Typical prompt:

```text
Please use the organize skill to review the vault structure and propose a cleanup.
```

Use it when:

- folders have become confusing
- many files are in the wrong place
- source material needs a clearer structure
- the vault needs a broader reorganization

Do not use this for ordinary ingestion. For new files, use `ingest` first.

### `reflect`

Use this to help the agent learn from recent work.

Typical prompt:

```text
Please use the reflect skill to review recent conversations and suggest any preferences, workflow patterns, or operational memories worth saving.
```

Use it when:

- the agent should learn your preferences better
- recent conversations contain useful workflow lessons
- repeated corrections should become durable preferences
- agent behavior should be calibrated based on recent sessions
