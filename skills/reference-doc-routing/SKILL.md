---
name: reference-doc-routing
description: Use when a task may need engineering-design, architecture, testing, access-control, design-system, API, release, data-model, subagent, or worktree-lifecycle reference documents. Helps select relevant docs, classify authority, and pass concise context to subagents.
---

# Reference Doc Routing Skill

Use this skill to choose and apply reference documents without polluting the main context.

Consult `references/README.md` for the packaged reference catalog and `references/reference-doc-routing.md` for the complete authority and conflict-resolution guidance. For non-trivial or consequential design choices, consult `references/engineering-design.md`. Use the starter files listed in the catalog when creating repository-owned reference documents.

Workflow:

1. Identify which parts of the task need reference context.
2. Find relevant global and repository-level docs.
3. Classify each document as authoritative, advisory, or historical.
4. Read only relevant sections when possible.
5. Summarize useful context for the current task.
6. Pass only relevant document paths or sections to subagents.
7. Require implementation-relevant claims to be checked against current code, tests, schemas, configuration, or runtime behavior.
8. Report conflicts between docs and primary evidence.

Primary evidence includes:

- current code
- tests
- schemas
- configuration
- logs
- build output
- typecheck output
- runtime behavior
- authoritative external documentation
