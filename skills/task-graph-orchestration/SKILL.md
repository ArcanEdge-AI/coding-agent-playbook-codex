---
name: task-graph-orchestration
description: Compile and execute an instruction-only task graph for complex coding work with genuine dependencies, substantial fan-out, layered consolidation, independent verification, or approval-gated actions. Skip small or linear work.
---

# Task Graph Orchestration

Use this skill only when graph structure materially improves completeness, concurrency, or verification. It does not add a scheduler, graph database, or enforcement runtime.

Read [references/task-graph-workflow.md](references/task-graph-workflow.md) for preflight, graph compilation, ready-set execution, fan-in, selective retry, verification, and approval gates. Read [references/task-graph-template.md](references/task-graph-template.md) only when creating a formal graph artifact.

Use `$multi-session-coordination` first when related independent Codex tasks or external ownership may create hidden edges. Use `$subagent-orchestration` for child assignment and acceptance contracts. Use `$worktree-lifecycle` when an auxiliary checkout is proposed or already task-owned.

## Essential Contract

- Give every node a bounded goal, authoritative inputs, an accepted output, real blocking dependencies, ownership or read scope, an executor, and a verification gate.
- Dispatch only ready, permitted nodes that fit the finite budget, runtime capacity, safety constraints, and verified ownership or isolation.
- Keep root topology, authority-bound decisions, integration, and final acceptance with the root main agent.
- Preserve accepted unrelated outputs when a gate fails and retry only invalidated work.
- Confirm every expected node and approval gate before completion.
