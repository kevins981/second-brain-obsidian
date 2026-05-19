---
name: housekeeping
description: Keep this Obsidian vault's knowledge base healthy and up to date. Use when the user asks for housekeeping, wiki cleanup, index updates, memory cleanup, vault health checks, or keeping the knowledge base managed.
---

# Housekeeping Skill

Housekeeping means keeping the vault trustworthy, navigable, current, and synced.

Use this skill when the user asks for housekeeping, wiki cleanup, index maintenance, memory cleanup, or a knowledge-base health check.

Key principle: if unsure, ask the user.

When doing housekeeping, report what you did in each step. Be specific enough that the user can see what was checked, what changed, and what still needs judgment.

## Step 1: Read Context

Read the standing context files if present:

- `knowledge_base/vault_context.md`
- `knowledge_base/user_preferences.md`
- `knowledge_base/agent_memory.md`

Report which files were read and which were missing.

## Step 2: Check Git State

Use git to inspect what changed since the last committed state.

Report:

- Modified files
- New files
- Deleted files
- Whether changes appear related to housekeeping or are likely user changes

Do not include unrelated user changes in a housekeeping commit unless they are part of the housekeeping work.

## Step 3: Index Maintenance

Check the two index files:

- `raw_sources/raw_sources_index.md`
- `knowledge_base/knowledge_base_index.md`

Compare the index files against the actual files in `raw_sources/` and `knowledge_base/`.

Look for:

- New files missing from indexes
- Deleted or renamed files still listed in indexes
- Files whose summaries no longer match their contents
- Missing currentness, role, uncertainty, or useful cross-links

Update indexes when files are added, removed, renamed, or meaningfully changed.

For indexed files, include useful fields such as:

- File path
- Short description
- Purpose or role, if known
- Currentness or uncertainty, if known
- Relevant cross-links, if useful

Report what was checked and what index entries were added, removed, or updated.

Do not assume a raw source is current, relevant, or authoritative just because it exists.

## Step 4: Recency and Relevance Review

Review whether important files may be outdated, superseded, or no longer relevant.

Common signals include:

- A source appears older than related notes or sources.
- Multiple files discuss the same topic but seem to disagree.
- An index marks a file as uncertain, background-only, outdated, or unverified.
- A note depends heavily on a raw source whose status is unclear.
- A file has not been touched in a while but still influences active knowledge-base notes.

Ask short, structured questions rather than guessing. For example:

- Is this still current enough to rely on?
- Has this been superseded by a newer source?
- Should this remain active context, move to background, or be treated as archive?

Update the relevant index entries and knowledge-base notes based on the user's answers.

Report which files were flagged for user judgment and what updates were made.

## Step 5: Preference and Memory Maintenance

Review:

- `knowledge_base/user_preferences.md`
- `knowledge_base/agent_memory.md`

For each file, report:

- Whether the file exists
- Current character count
- Approximate soft limit: 5,000 characters
- Whether consolidation is needed

`user_preferences.md` is for durable preferences about how the user wants the agent to communicate, make decisions, structure notes, and handle workflow.

Each `user_preferences.md` entry should include a date and status:

- `tentative`: the user said or implied it once; follow it cautiously.
- `confirmed`: the user explicitly stated it or corrected the agent about it.
- `standing`: repeated preference, important default, or something the user clearly wants preserved long-term.

`agent_memory.md` is for durable operational memory about this vault, including conventions, recurring workflows, setup facts, and lessons learned.

Each `agent_memory.md` entry should include a date. Categories are optional; only add them if they make the entry clearer.

If either file is getting long:

- Remove duplicates.
- Rewrite to be more compact and concise.
- Merge overlapping entries.
- Remove one-off or session-specific details.
- Move detailed project knowledge into a regular knowledge-base note.
- Leave a short link from memory to the detailed note when useful.

Do not store secrets, credentials, large raw data, or temporary debugging context in memory files.

Report any entries added, removed, rewritten, or moved.

## Step 6: Wiki Health Check

Health-check the knowledge base.

Look for:

- Contradictions between pages.
- Stale claims that newer sources may have superseded.
- Orphan pages with no useful inbound or outbound links.
- Important concepts mentioned repeatedly but lacking their own page.
- Missing cross-references between related notes.
- Data gaps that could be filled with a web search or a new source.
- Questions the user may want to investigate next.

When the answer depends on user judgment, ask a short, structured question instead of guessing.

Report findings, even if no edits are needed.

## Step 7: Make Focused Edits

Make focused edits only where they directly improve housekeeping.

Avoid unrelated cleanup. Avoid reorganizing folders unless the user explicitly asked for organization or the change is a small, obvious part of housekeeping.

Report every file edited.

## Step 8: Sync to GitHub

After housekeeping edits are complete:

1. Review `git status`.
2. Commit the housekeeping changes with a concise message.
3. Push the commit to GitHub.

Report the commit hash and push result.
