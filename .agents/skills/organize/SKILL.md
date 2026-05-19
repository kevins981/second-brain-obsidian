---
name: organize
description: Use only when the user explicitly asks to organize, restructure, rename, or clean up the folder layout of this Obsidian vault.
---

# Organize Skill

Organize means improving the vault's folder and file structure so information is easier to find.

Use this skill only when the user explicitly asks for organization, restructuring, folder cleanup, file moves, or renames.

## Principle

Organization should make retrieval easier, not create a taxonomy for its own sake.

Prefer simple, shallow structure. Do nothing if the current organization is already good enough.

## Before Changes

Before moving or renaming files:

1. Check `git status`.
2. If there are uncommitted changes, tell the user what changed.
3. Ask whether to commit and push the current state before reorganizing.

This gives the user a checkpoint before disruptive file moves or renames.

## Workflow

1. Inspect `raw_sources/` and `knowledge_base/`.
2. Read the relevant index files if present:
   - `raw_sources/raw_sources_index.md`
   - `knowledge_base/knowledge_base_index.md`
3. Look for natural groupings, such as common projects, concepts, source types, meetings, research areas, or workflows.
4. Decide whether organization would actually help.
5. If the current organization is fine, say so and do not make changes.
6. If changes would help, propose a small organization plan.
7. Ask for user approval before creating folders, moving files, renaming files, or changing note paths.
8. After approved changes, update affected links and index files.

## Raw Sources

For `raw_sources/`, organizing into folders by common concepts or source types is often useful.

Examples of possible groupings include research, meetings, strategy, product, reports, or a specific project area. These are examples, not required categories.

Do not assume file names are accurate. Use file contents, indexes, and the user's guidance to decide what belongs together.

## Knowledge Base

For `knowledge_base/`, be more conservative.

Use subfolders when they clearly make notes easier to navigate, but do not create deep folder trees too early. Links and indexes may be enough.

If moving or renaming knowledge-base notes, preserve traceability:

- Update links that point to moved notes.
- Keep links back to relevant raw sources.
- Update `knowledge_base/knowledge_base_index.md`.

## Approval Required

Ask for approval before:

- Creating new folders.
- Moving files.
- Renaming files.
- Changing note paths.
- Reorganizing multiple files at once.

When proposing changes, keep the plan short and concrete. Explain why the new structure would be easier to use.
