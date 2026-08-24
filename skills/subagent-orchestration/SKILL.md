---
name: subagent-orchestration
description: Use for repository work when Codex subagents are available. Delegates bounded execution while keeping root accountability, inherited scope and authority, explicit model ceilings, disjoint ownership, and evidence-backed acceptance.
---

# Subagent Orchestration

Use this skill when subagents are available for repository work. Keep the root main agent responsible for framing, architecture, routing, integration, verification, authority-bound actions, final acceptance, and the user-facing report.

Read only the reference needed for the current decision:

- [references/subagents.md](references/subagents.md) for decomposition, assignment fields, ownership, acceptance, retry, and completion rules
- [references/model-routing.md](references/model-routing.md) before selecting a child profile, model, or reasoning effort

For substantial fan-out or genuine dependencies, use `$task-graph-orchestration`. For conflicts among independent Codex tasks, use `$multi-session-coordination`. If an auxiliary checkout is proposed or already task-owned, use `$worktree-lifecycle` before acting.

## Essential Contract

- Give each child one bounded, verifiable completion subset with explicit scope, non-goals, permissions, workspace, ownership, evidence, stop conditions, and acceptance criteria.
- Keep each child equal to or narrower than its parent in scope, access, authority, approval boundary, model rank, and reasoning effort.
- Keep sibling writes disjoint and serialize real conflicts.
- Verify claims and edits against primary evidence before accepting them.
- Do not let delegation replace main-agent judgment or expand the user's authority.
