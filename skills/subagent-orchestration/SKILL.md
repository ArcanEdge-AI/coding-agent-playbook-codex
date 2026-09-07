---
name: subagent-orchestration
description: Use for every repository task when Codex subagents are available. Makes the main agent the orchestrator, delegates bounded execution by default, enforces dependency-aware decomposition and fixed Luna/max routing, and requires main-agent verification.
---

# Subagent Orchestration Skill

The root main agent is the senior developer and orchestrator. It owns a finite manifest and total spawned-node budget. Where the host supports callable installed profiles, root may select a verified Luna/max profile through an `@tag` or equivalent programmatic route; this is a host capability statement, not a claim that a picker or callable route was tested. Depth 1 is a direct worker or a permitted local orchestrator. Depth 2 uses a verified Luna/max profile or explicit `gpt-5.6-luna` with `max` reasoning, executes a strict non-empty subset directly, and never spawns.

Use this skill for every repository task when subagents are available. Select a single bounded execution assignment for simple or linear work. For broader work, dispatch only nodes that satisfy the manifest, permit, budget, and capacity rules below. At the root, direct main-agent execution is allowed only when subagents are unavailable, the user explicitly forbids delegation, or a specific action cannot be delegated because required authority must remain with the main agent. Record the exact exception and limit it to that action.

When multiple independent project threads need conflict detection, ownership, sequencing, or integration guidance, use the `multi-session-coordination` skill instead. Do not spawn additional implementation agents to solve an existing parallel-work conflict.

## Dependency-Aware Delegation

Keep simple tasks simple. For work with multiple delegable parts, define each candidate work node with:

- a node identifier
- one bounded goal
- inputs and authoritative sources
- an output and acceptance condition
- only the upstream nodes that block it from starting
- write ownership or read scope
- a verification gate proportionate to risk

A dependency exists only when a node cannot correctly begin without an accepted upstream artifact or decision. Identify which nodes are safe to run in parallel and which remaining chain of blocking work controls completion.

Dispatch only ready nodes in the finite root manifest that have a root-issued permit, fit within the remaining total node budget, and fit runtime capacity, safety constraints, and verified ownership or isolation. Runtime-full is backpressure: continue ready permitted work or report the constraint; do not queue speculative descendants. Siblings require disjoint ownership.

Use the current workspace by default with an auxiliary-worktree budget of zero. A subagent, node, retry, or depth level does not imply a new checkout. Only the root may issue a separate worktree permit or create, adopt, repurpose, move, or remove a worktree. Root may authorize one active auxiliary without additional approval; two or more require user approval for the exact count and reasons. Descendants receive an exact workspace and report additional isolation needs upward. Consult `references/worktrees.md` whenever an auxiliary worktree is proposed or already task-owned.

While delegated work is running, continue available independent, non-conflicting planning, inspection, integration, or validation work in the main thread. Do not wait solely for a subagent when useful work remains. Do not invent parallel work, exceed runtime limits, or trade evidence and verification for lower latency.

When a formal task graph exists, each delegated assignment must identify its graph node, consume only declared inputs, remain within its declared read scope and write ownership, and return the declared output shape. A subagent may report a hidden dependency or invalid graph assumption, but it must not silently restructure the graph or advance blocked nodes; the main agent owns topology changes and ready-set recalculation.

## Recursive Delegation

Subagents may locally orchestrate only inside their assigned node. A local child must be equal to or narrower than its parent in goal, inputs, data access, permissions, scope, non-goals, write ownership or isolation, authority, and approval boundary. Explicitly select a verified Luna/max profile or pass `gpt-5.6-luna` with `max` reasoning for every child call; never silently inherit, change, or escalate the route. A descendant that cannot complete within its declared scope or authority stops and reports the gap.

The root alone issues child-specific permits and expands budget. Depth-1 delegation needs a permit and budget; depth-2 is leaf-only. Retry reuses its node ID and permit. A replacement is a new root-authorized node with a new permit and budget entry, and still selects a verified Luna/max profile or uses explicit Luna/max arguments. Every expansion must record a root reason limited to a newly discovered dependency, an invalidated gate, or changed user scope; a material expansion also requires immediate user approval. Keep payloads to minimum paths and accepted artifacts; reuse accepted outputs and avoid full history, transcripts, and long logs.

## Mandatory Model Routing

Before spawning a subagent, consult `references/model-routing.md` when available.

- Explicitly select a verified bundled profile pinned to `gpt-5.6-luna`/`max`, or pass those values through a generic route, for every delegated task.
- Do not rely on an unverified profile or parent inheritance for model or effort.
- If the host cannot accept explicit per-call values, use a verified bundled Luna/max profile. If it is stale or unavailable, stop and report the limitation.
- Record the actual root model when task provenance needs it; root model and effort do not alter the child route.
- Keep architecture, security-sensitive judgment, destructive operations, migrations, complex concurrency, and other high-impact decisions with the main orchestrator. Delegate only bounded evidence gathering for those areas within the declared scope and authority.
- A subagent must stop and report a capability gap; it must not silently change models or effort, fall back to the main model, or request escalation.
- Only root may authorize a replacement or reroute, and it must use a new permit and a verified Luna/max profile or explicit Luna/max arguments.

## Workflow

1. Clarify the task goal and success criteria.
2. For multi-node work, map bounded nodes, real blocking dependencies, parallel-safe nodes, the completion-controlling path, and required handoff gates.
3. At the root, assign actual execution to at least one bounded subagent when available; record any root direct-execution exception and its exact reason. A depth-1 worker executes directly when no valid, permitted strict-subset split exists. Depth 2 is a leaf and cannot spawn.
4. Choose from the Codex roles: Planner, Engineer, Reviewer, Tester, and Docs.
5. Select a verified Luna/max profile alias or explicitly pass `gpt-5.6-luna` with `max` reasoning.
6. Give each subagent a precise assignment:
   - role
   - goal
   - context
   - lineage and inherited constraints
   - selected profile or model
   - why the fixed Luna/max route is suitable
   - escalation conditions
   - scope
   - non-goals
   - permissions
   - exact assigned workspace and worktree permit ID when applicable
   - local child ownership and sibling non-overlap
   - required evidence
   - output format
   - compact parent return bundle
   - for multi-node work, the node identifier, inputs, output and acceptance condition, blocking dependencies, ownership or read scope, and verification gate
7. Launch only ready manifest nodes that have a root permit, remaining node budget, and runtime, safety, and ownership capacity; serialize real write or mutable-state conflicts unless isolation is verified.
8. Verify subagent claims against primary evidence. For meaningful implementation, use a separate verification task with only the necessary artifact, criteria, and evidence requirements when the runtime supports it; the main agent still decides acceptance.
9. If a gate fails, revise or rerun the failed node and any downstream nodes whose inputs became invalid. Do not restart unrelated nodes by default.
10. Before combining results, confirm every required input passed its designated gate, then inspect the combined diff and run validation for the integrated behavior.
11. Accept, reject, or revise against the declared scope and acceptance condition. Only root may create a replacement with a new permit and budget; it must still select a verified Luna/max profile or use explicit Luna/max arguments.
12. Before the final response, remove each task-created auxiliary worktree under the verified cleanup gates or preserve it with its exact owner, path, branch or HEAD, blocker, and next action. Do not defer task-owned cleanup to scheduled automation.
13. Report relevant subagent usage, concurrency decisions, workspace dispositions, and any escalation in the final response.

Never accept a subagent's conclusion solely because it sounds confident.
