---
name: feature-branch-lifecycle
description: Use when a feature, change, or update may use one or more development branches and must be integrated, validated, promoted through long-lived integration and production branches, and cleaned up safely.
---

# Feature Branch Lifecycle Skill

Use this skill to keep feature assembly out of long-lived branches and to make promotion and cleanup explicit.

Read `references/branching-rule.md` before creating the branch structure, opening an integration or promotion pull request, or deleting temporary branches.

## Applicability Gate

Before applying the branching model, inspect:

- applicable repository instructions
- the default, current, integration, and production branches
- relevant remotes, pull requests, branch protections, and worktrees
- active work that may still depend on a temporary branch

Use the repository's actual branch names. The examples use `staging` and `main`.

If the repository does not have an established long-lived integration and production branch model, do not create or rename those branches merely because this skill is available. Follow a more specific repository workflow or obtain an explicit maintainer decision.

## Lifecycle Invariants

When the model applies:

```text
development branches
        ↓
feature integration branch
        ↓
long-lived integration branch (for example, staging)
        ↓
long-lived production branch (for example, main)
```

- Create the feature integration branch from the current integration branch.
- Create feature-scoped development branches from the feature integration branch.
- Merge development branches only into the feature integration branch.
- Validate the complete intended change on the feature integration branch before promotion.
- Promote the feature integration branch to the integration branch with one pull request.
- Promote to the production branch only from the integration branch.
- Never delete permanent integration or production branches.
- Delete temporary local and remote branches only after the cleanup gates pass and authority exists for the exact deletion.

## Related Skills

- Use `multi-session-coordination` when independent Codex tasks or other owners are working on related branches.
- Use `worktree-lifecycle` when any participating branch is checked out in an auxiliary worktree. A branch and a worktree are not interchangeable lifecycle units.
- Use `task-graph-orchestration` when integration, validation, promotion, and cleanup form part of a broader dependency graph.

## Required Result

Track and report:

- the resolved branch roles and exact branch names
- the base and destination of each temporary branch
- complete-feature validation evidence
- pull-request and merge state
- cleanup eligibility and final disposition for each temporary branch
- any missing authority, failed gate, or active dependency that requires preservation

The branching rule defines required sequencing. It does not provide blanket authority to create remote infrastructure, open or merge pull requests, delete branches, or promote production.
