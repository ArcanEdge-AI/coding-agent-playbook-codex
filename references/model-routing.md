# Codex Subagent Model Routing

Every delegated subagent execution must explicitly select a verified bundled profile pinned to `gpt-5.6-luna` with `max` reasoning, or pass those values as explicit child-execution settings. This applies to each role, depth, retry, and replacement that launches or reruns a child. It does not apply to ordinary tool calls, progress or task-reporting messages, or follow-up communication. The root model and effort may vary independently; they do not change the child execution route.

## Why Explicit Routing Is Required

Codex custom-agent fields such as `model` and `model_reasoning_effort` may inherit from the parent session when omitted. A direct child-execution route must therefore pass the fixed values:

```text
model = "gpt-5.6-luna"
reasoning_effort = "max"
```

Use the host's equivalent argument names when required, but keep both values explicit in the child-execution settings. The bundled profile names remain compatible aliases; selecting a profile whose fields are verified as Luna/max is also an explicit child-execution route.

If a host cannot accept explicit child-execution model and effort values, select a verified bundled Luna/max profile. If the loaded profile is stale or cannot be verified, use an explicit child-execution route that can or stop and report the routing limitation rather than silently inheriting a profile or parent setting.

## Fixed Profile Route

Every bundled profile pins the same route so profile defaults and child executions agree:

| Profile alias | Model | Reasoning | Intended work |
| --- | --- | --- | --- |
| `docs`, `docs_luna` | `gpt-5.6-luna` | `max` | Documentation lookup and source extraction. |
| `planner`, `planner_luna` | `gpt-5.6-luna` | `max` | Bounded planning and validation strategy. |
| `engineer`, `engineer_luna` | `gpt-5.6-luna` | `max` | Small, isolated implementation. |
| `tester`, `tester_luna` | `gpt-5.6-luna` | `max` | Targeted reproduction and validation analysis. |
| `reviewer`, `reviewer_luna` | `gpt-5.6-luna` | `max` | Evidence-backed bounded review. |

The aliases retain their existing filenames and names for compatibility. The fixed route does not remove the role boundaries: the main agent retains architecture, high-impact judgment, integration, and final acceptance.

## Selection Rules

1. At root depth 0, record the actual root model and effort when the task record needs that provenance. Root routing does not create a model or effort ceiling for children.
2. Maintain a finite task manifest and total spawned-node budget counting every depth-1 and depth-2 node. Only root issues child permits or expands that budget.
3. Give every child a root-issued permit, parent ID, child ID, strict non-empty completion subset, declared ownership or read scope, a verified Luna/max profile selection or explicit Luna/max child-execution settings, and an acceptance condition. Sibling write ownership must be disjoint.
4. Keep each child equal to or narrower than its parent in inputs, data access, permissions, scope, non-goals, authority, approval boundary, ownership, and workspace.
5. Depth 1 may execute directly or manage a declared local subtree. Depth 2 executes directly and cannot spawn. Depth 3 and deeper are prohibited.
6. Dispatch only ready, permitted nodes that fit the remaining budget and runtime, safety, and ownership capacity. When capacity is full, do not queue speculative descendants.
7. Retry a failed node with its original ID and permit while its inputs remain valid. A root-authorized replacement gets a new permit and budget entry but still selects a verified Luna/max profile or explicit Luna/max child-execution settings; it never changes the model or reasoning of the parent or a peer task.

This is an intentional Codex-specific divergence from the companion Claude Code playbook. Codex supports explicit model and reasoning-effort arguments on child-execution launches as well as those TOML fields, so this repository fixes every child execution route to Luna/max independently of the root session. A verified pinned profile supplies that route when launch-time overrides are unavailable. The companion playbook keeps its native role and model controls separately; do not copy its routing schema into Codex files.

## Keep With the Main Agent

Do not delegate final ownership of:

- architecture and system design
- security-sensitive or access-control decisions
- authentication, authorization, privacy, payments, or billing
- destructive operations
- data migrations or persisted-schema strategy
- concurrency, locking, queues, caching, or background-job design
- public API compatibility
- release or production-impacting configuration
- large or high-impact refactors
- final acceptance of meaningful changes

A supporting subagent may gather evidence for these areas, but the main agent must make and verify the decision.

## Escalation

A subagent must stop and report when:

- requirements are materially ambiguous
- primary evidence conflicts
- the task exceeds its assigned scope
- the conclusion cannot be independently verified
- the work becomes security-sensitive, destructive, or production-impacting
- the task requires architectural or cross-system judgment
- the host cannot honor explicit Luna/max child-execution settings

No descendant may silently change its execution model or effort, fall back to a parent setting, or request a model escalation. Any replacement or reroute remains root-owned and must select a verified Luna/max profile or use explicit Luna/max child-execution settings.

## Reporting and Follow-up Messages

Subagents must not alter a parent or peer task's model or reasoning settings. Use team `collaboration.send_message` or the normal final return for progress and task reporting. If separately authorized task reporting uses `send_message_to_thread`, omit `model`, `thinking`, and analogous destination-setting overrides entirely; do not echo the sender's model, guess or reassert the parent's model, or change settings as a workaround. A follow-up message to an existing worker need not repeat its verified execution route.

Correct:

```text
Child execution: select a verified Luna/max profile (or pass explicit child-execution settings).
Task report: send_message_to_thread({ threadId: parentId, prompt: "..." })
```

The task-reporting call above is allowed only when separately authorized and intentionally omits model, effort, thinking, and destination-setting overrides.

Incorrect:

```text
send_message_to_thread({ threadId: parentId, prompt: "...", model: "gpt-5.6-luna", thinking: "max" })
```

The incorrect form can override the destination task's model or reasoning settings.

## Required Assignment Fields

```text
Role:
Selected profile or model: [Verified bundled profile alias or explicit gpt-5.6-luna route]
Reasoning effort: max
Why this selection is suitable:
Goal:
Context:
Lineage and inherited constraints:
Parent ID / child ID:
Completion subset:
Scope:
Non-goals:
Permissions:
Root-issued permit ID and manifest budget status:
Declared ownership or read scope and sibling non-overlap:
Exact assigned workspace and worktree permit ID when applicable:
Acceptance condition:
Evidence required:
Escalation conditions:
Output format:
Parent return bundle:
```

## Acceptance Check

Before accepting delegated work, confirm:

- the child execution selected a verified profile pinned to `gpt-5.6-luna`/`max`, or explicitly passed those values as child-execution settings
- parent-model and parent-effort inheritance were not used unintentionally for child execution
- progress and task-reporting messages omitted model, reasoning, thinking, and analogous destination-setting overrides and did not alter a parent or peer task
- the root-issued permit, parent/child IDs, and manifest budget are recorded
- the completion subset is non-empty and strictly smaller than the parent's remaining subset
- sibling write ownership is disjoint
- the subagent used its exact assigned workspace and did not create, repurpose, move, or remove a worktree
- the stated acceptance condition passed
- the subagent stayed within scope and authority
- claims are supported by primary evidence
- any edits are minimal and task-related
- the main agent independently reviewed material findings and edits
