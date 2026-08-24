---
name: worktree-lifecycle
description: Manage Git worktrees created or used during a Codex task, including justified creation, exact ownership, integration, safe removal, and evidence-backed preservation.
---

# Worktree Lifecycle

Use this skill before creating, adopting, repurposing, integrating, preserving, moving, or removing an auxiliary worktree.

Read [references/worktrees.md](references/worktrees.md) for the complete lifecycle and safety gates. Use [references/worktree-manifest.md](references/worktree-manifest.md) only when a durable ledger is justified; a concise plan entry is enough for a small task.

## Essential Contract

- Start in the current workspace with an auxiliary-worktree budget of zero.
- Treat worktrees as isolation tools, not delegation units.
- Let only the root raise the finite budget, issue permits, and create, adopt, repurpose, move, or remove a task-owned auxiliary.
- Reuse a compatible task-owned checkout or serialize work when that is sufficient.
- Give descendants the exact assigned workspace; they report additional isolation needs upward.
- Before completion, integrate and safely remove every task-created auxiliary whose gates pass, or preserve it with its exact owner, path, branch or HEAD, blocker, and next action.
- Never treat a host-managed primary or user-owned existing checkout as disposable.
