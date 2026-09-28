---
name: subagent-orchestration
description: Use when considering or carrying out bounded delegation. Uses subagents sparingly when a concrete benefit justifies the overhead or independent assistance is required, with task-based model routing, Standard speed, finite scope, and main-agent verification.
---

# Subagent Orchestration

The main agent is the primary implementer and owns the requested outcome end to end. Use subagents sparingly, only when a bounded assignment's concrete benefit outweighs its context, coordination, latency, and review cost or governing instructions require independent assistance.

Consulting a role profile for a different perspective does not require this delegation workflow. The main agent can apply the profile's role guidance directly while retaining its configured settings and task authority. Use the workflow below only when considering or carrying out actual delegation; a perspective change does not satisfy an independent-verification gate.

Consult references/subagents.md for the full assignment and acceptance guidance and references/model-routing.md before launching a helper.

## Decide Whether to Delegate

Delegate only when a bounded helper has a concrete benefit:

- independent evidence or focused review
- genuinely parallel progress on non-conflicting work
- reduced main-agent context for a large, separable investigation

Do not delegate merely because helpers are available, a task is large, a role is unused, or a graph contains several nodes. Keep tightly coupled design and implementation with the main agent. Do not outsource work already completed.

Before spawning, define the bounded result, acceptance check, expected benefit, exact scope and workspace, and a finite helper-launch and retry allowance.

## Use Flat Assignments

Use direct root-to-helper assignments. Bundled helpers execute their assigned work and do not spawn descendants. Recursive orchestration is outside this default workflow and requires separate explicit authorization and controls.

Each helper assignment must be a non-empty, strictly smaller part of the remaining work and no broader than the root task in inputs, data access, permissions, scope, non-goals, authority, ownership, workspace, or approval boundary.

Serialize overlapping writes. Disjoint bounded writers may share the current workspace when the runtime and repository allow it. Use an auxiliary worktree only through the root-owned worktree-lifecycle process.

## Route Every Helper Explicitly

Select each delegated execution, retry, and replacement by the task table in references/model-routing.md: GPT-6 Luna/high, Sol/medium, Sol/high, or Astra/xhigh. Use Standard speed only, with no Max, Ultra, or Fast. Minimize total completion cost, including retries and corrections. Use a matching profile or supported explicit route; verify effective settings because profile values can override spawn arguments. Preserve the main agent's selected configuration.

If the route cannot be established, keep the work with the main agent and report any separately required independent-verification gap.

Progress and result messages must not alter parent or peer settings. Use team collaboration messaging or the normal final return. Keep destination model and reasoning overrides out of separately authorized task reports.

## Assignment Contract

Provide one concise contract containing:

- goal and acceptance condition
- necessary context and authoritative inputs
- applicable skills and real graph dependencies
- permitted reads and writes
- non-goals and stop conditions
- exact workspace and ownership
- verified task-selected model, reasoning effort, and Standard speed
- place within the finite launch/retry allowance
- required evidence and return format

Pass only necessary context. Do not copy full histories, transcripts, or long logs.

## Execute and Accept

1. Confirm delegation has a concrete benefit and capacity is available.
2. Select the appropriate Planner, Engineer, Reviewer, Tester, or Docs profile.
3. Dispatch only work whose real dependencies are satisfied.
4. Continue useful non-conflicting root work while the helper runs.
5. Inspect the returned artifact, evidence, scope compliance, and checks.
6. Reject, revise, or retry work that does not meet its acceptance condition.
7. Before retrying, identify what failed and what will change.
8. Reuse valid results and avoid repeating unchanged failed approaches.
9. Inspect the combined diff and validate integrated behavior.
10. Reconcile every helper attempt and task-created auxiliary worktree before completion.

High-impact changes require independent verification proportionate to risk. If the required check is unavailable, report the unmet gate instead of claiming completion.

Never accept a helper conclusion solely because it sounds confident.
