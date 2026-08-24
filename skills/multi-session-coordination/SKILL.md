---
name: multi-session-coordination
description: Coordinate related work across independent Codex tasks by discovering active repository state, detecting contract and ownership conflicts, sequencing integration, and defining evidence-backed handoffs.
---

# Multi-Session Coordination

Use this skill when independent Codex tasks, branches, worktrees, or pull requests may be changing related parts of the same project. Do not use it for ordinary bounded delegation inside one task.

Read [references/multi-session-coordination.md](references/multi-session-coordination.md) for the complete discovery, evidence classification, change-map, conflict-resolution, ownership, sequencing, and integration workflow. Use [references/active-work-record.md](references/active-work-record.md) only when a repository-local fallback record is useful because direct task discovery is unavailable.

If any participating task proposes, owns, integrates, preserves, or removes an auxiliary checkout, use `$worktree-lifecycle` for that lifecycle. This skill does not grant cleanup authority over another task's or the user's workspace.

## Required Result

Return the discovery coverage, active-work map, conflicts and risks, one owner for each shared contract or contested area, implementation order, copy-ready handoffs, integration verification, and unresolved decisions. Separate confirmed evidence from inference.

Do not implement code unless the user requested implementation. Stop when inaccessible work prevents a safe compatibility decision or when a material architecture, behavior, data, safety, release, or user-visible choice remains unresolved.
