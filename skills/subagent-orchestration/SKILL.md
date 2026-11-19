---
name: subagent-orchestration
description: Use when considering or carrying out bounded delegation. Uses subagents sparingly when a concrete benefit justifies the overhead or independent assistance is required, with task-based model routing, finite scope, and main-agent verification.
---

# Subagent Orchestration

The main agent is the primary implementer and owns the requested outcome end to end. Use subagents sparingly, only when a bounded assignment's concrete benefit outweighs its context, coordination, latency, and review cost or governing instructions require independent assistance.

Consulting a role profile for a different perspective does not require this delegation workflow. The main agent can apply the profile's role guidance directly while retaining its configured settings and task authority. Use the workflow below only when considering or carrying out actual delegation; a perspective change does not satisfy an independent-verification gate.

Use the [delegation reference](references/subagents.md) for assignment and acceptance guidance and [model routing](references/model-routing.md) to select a helper's execution settings.

## Decide Whether to Delegate

Delegate only when a bounded helper has a concrete benefit:

- independent evidence or focused review
- genuinely parallel progress on non-conflicting work
- reduced main-agent context for a large, separable investigation

Do not delegate merely because helpers are available, a task is large, a role is unused, or a graph contains several nodes. Keep tightly coupled design and implementation with the main agent. Do not outsource work already completed.

Before spawning, define the bounded result, acceptance check, expected benefit, exact scope and workspace, and a finite helper-launch and retry allowance.

## Use Flat Assignments

Use direct root-to-helper assignments. Bundled helpers execute their assigned work and do not spawn descendants. A separate, explicitly authorized recursive workflow requires a bounded manifest, ownership, routing, verification and resource controls, and must not exceed two delegated generations.

Give each helper a bounded question or implementation slice with a defined result. An expressly requested read-only review can cover the whole candidate, even when that opinion is the remaining deliverable. Limit inputs, access, permissions, write scope, workspace, and spending to the assignment. Root retains integration, acceptance, and final delivery.

Serialize overlapping writes. Disjoint bounded writers may share the current workspace when the runtime and repository allow it. Use an auxiliary worktree only through the root-owned worktree-lifecycle process.

## Route Every Helper Explicitly

For every delegated execution, retry, or replacement, use the default task table or an authorized per-task selection under [model routing](references/model-routing.md). Check profile precedence before launch. Verify the child's actual model and effort from runtime evidence before relying on its work. Keep root's selected settings and the assigned role's instructions.

If the requested settings are unavailable, mismatched, or unverifiable, hold the affected assignment. Complete other authorized work and report the missing route or independent check. Only root may reassign within the remaining authority and budget.

Progress and result messages must not alter parent or peer settings. Use team collaboration messaging or the normal final return. Keep destination model and reasoning overrides out of separately authorized task reports.

## Assignment Contract

Capture these six items in one concise assignment:

1. **Goal and acceptance:** bounded result, acceptance check, and expected benefit.
2. **Context:** necessary facts, inputs, paths, interfaces, and accepted evidence.
3. **Skills and methods:** applicable skills, required references, and real graph dependencies.
4. **Scope and authority:** permitted reads/writes, non-goals, constraints, and stop conditions.
5. **Ownership and route:** helper ID or permit, exact workspace, ownership, verified model/effort, and place within the finite launch/retry allowance.
6. **Return:** artifact or findings, primary evidence, checks run, and unresolved issues.

Pass only necessary context. Do not copy full histories, transcripts, or long logs.

## Execute and Accept

1. Confirm delegation has a concrete benefit and capacity is available.
2. Select the appropriate bundled role or an explicitly requested specialist. Preserve its instructions on the chosen route.
3. Dispatch only work whose real dependencies are satisfied.
4. Continue useful non-conflicting root work while the helper runs.
5. Inspect the returned artifact, evidence, scope compliance, and checks.
6. Reject, revise, or retry work that does not meet its acceptance condition.
7. Count retries and replacements against the finite allowance. Identify what failed and what will change. Only root may expand the allowance for a new dependency, invalidated gate, or changed user scope. Obtain specific approval immediately before a material cost expansion.
8. Reuse valid results and avoid repeating unchanged failed approaches.
9. Inspect the combined diff and validate integrated behavior.
10. Reconcile every helper attempt and task-created auxiliary worktree before completion. Close optional task-owned helpers when their output is no longer needed. Preserve their work, and keep any required independent check open.

Require independent verification for consequential access-boundary changes, irreversible migrations, comparable risk, and repository-mandated review. Choose evidence or a qualified reviewer appropriate to that risk. Preserve separate human approvals. Report an unmet gate if the required check is unavailable.

Never accept a helper conclusion solely because it sounds confident.
