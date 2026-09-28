---
name: task-graph-orchestration
description: Use for complex coding tasks with substantial fan-out, multiple genuine dependencies, broad file or repository scope, multi-layer consolidation, separate implementation and verification paths, or an approval-gated irreversible action. Compiles an instruction-only task graph, executes only ready work, preserves completeness through fan-in, and retries only invalidated work. Skip for small or genuinely linear tasks.
---

# Task Graph Orchestration

Use instructions and Markdown to make complex work topology explicit. Do not introduce a graph database, scheduler, runner, schema package, or orchestration framework. A work node is a bounded outcome, not automatically a separate agent.

## Decide Whether to Use a Formal Graph

Use a formal graph when the task has substantial fan-out, several real dependencies, broad audit or transformation scope, layered consolidation, separate implementation and verification paths, or an approval-gated action.

Skip formal graph mode when the task is small, genuinely linear, dominated by one coherent design judgment, limited to tightly coupled writes, or cheaper to execute than to maintain as a graph. Skipping graph mode does not waive relevant skills or verification, and graph mode does not require delegation.

## Establish the Preflight

1. Inspect the request, repository state, applicable instructions, validation surfaces, and existing ownership.
2. Use the multi-session-coordination skill first when related tasks, branches, worktrees, pull requests, or active-work records may affect ownership or contracts.
3. Define the overall goal and observable success criteria.
4. Identify actions requiring explicit approval because they are audience-facing, destructive, irreversible, sensitive, production-impacting, materially costly, or outside existing authority.
5. Read references/templates/task-graph.md before creating a formal graph artifact.
6. Use the worktree-lifecycle skill when any node proposes or owns an auxiliary worktree.

Keep a medium graph in the working plan or response. For long-running, multi-phase, or multi-session implementation, create .codex/task-graphs/<task-slug>.md only when repository policy permits that local coordination artifact. Do not create a repository artifact for an informational question or when the task does not authorize changes.

## Compile the Graph

Define each meaningful node with:

- a stable identifier
- one bounded goal
- required inputs and authoritative sources
- the produced artifact or decision
- an observable acceptance condition
- only the upstream nodes whose accepted output it consumes
- read scope and write or mutable-state ownership
- an executor: root by default, or one directly assigned helper when delegation has a concrete benefit
- a verification gate proportionate to risk
- a current state
- an exact workspace, plus a root-issued worktree permit only when an auxiliary checkout is justified

Use states consistently: Proposed, Ready, Running, Complete, Failed, Blocked, or Superseded.

Audit every proposed edge:

> Can the downstream node correctly begin without consuming an accepted output or decision from the upstream node?

If yes, do not add a dependency merely to preserve narrative order. Track overlapping writes, shared mutable state, schema or interface ordering, external ownership, resource limits, and approval gates as hidden constraints.

Add fan-in nodes where several accepted outputs must be combined. Add independent verification nodes when risk or blast radius warrants them. Identify the completion-controlling path and current ready set.

## Execute Ready Work

Execute only nodes whose dependencies and hidden constraints are satisfied.

The main agent completes coherent work directly by default. Use helpers sparingly, only when independent evidence, parallel progress, or context reduction justifies the coordination and review overhead, or governing instructions require independent assistance:

- use a direct root-to-helper assignment
- apply the subagent-orchestration skill and its assignment contract
- set a finite helper-launch and retry allowance
- assign disjoint ownership or serialize conflicting writes
- select and establish the approved task-based model and reasoning effort at Standard speed
- require the helper to execute directly without spawning descendants
- verify the returned artifact before accepting it

Graph planning does not authorize helpers, worktrees, spending, or broader permissions. A graph may contain many nodes and use no helpers. Runtime capacity is a constraint, not a reason to queue speculative work.

## Verify and Retry Selectively

Validate each necessary handoff and the final combined result. When a gate fails:

- preserve accepted outputs whose inputs remain valid
- revise or rerun the failed work
- repeat downstream work only when its consumed input changed
- recompile the affected graph portion when the failure reveals a missing edge
- stop unchanged retries when evidence shows the approach is not progressing

Retries and replacements remain within the finite helper allowance when delegated. Expand execution cost only for an identified new dependency, invalidated gate, or changed user scope; obtain user approval immediately before a material expansion.

Before completion, reconcile node states, required approval gates, helper assignments, and every task-created auxiliary worktree.

## Enforce Approval Gates

Complete safe inspection, reversible preparation, and validation before a gate when useful. Immediately before the gated action, present the exact target, scope, consequences, material cost, audience, and recovery path when one exists. Approval for a plan or earlier node does not authorize a broader action.

## Respect Instruction-Only Limits

This skill provides planning semantics, not a deterministic runtime. Recheck repository state, ownership, node inputs, and approval status at consequential transitions. Do not describe the graph as mechanically enforced.
