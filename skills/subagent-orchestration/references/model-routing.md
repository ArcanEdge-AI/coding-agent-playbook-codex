# Codex Subagent Model Routing

Every delegated subagent execution must explicitly select a verified bundled profile pinned to `gpt-5.6-luna` with `max` reasoning, or pass those values as explicit child-execution settings. This applies to each role, retry, and replacement that launches or reruns a helper. It does not apply to ordinary tool calls, progress or task-reporting messages, or follow-up communication. The root model and effort may vary independently; they do not change the helper route.

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

1. Record the actual root model and effort only when the task record needs that provenance. Root routing does not create a model or effort ceiling for helpers.
2. Before dispatching, define the bounded result, acceptance check, expected benefit, exact scope and workspace, and finite helper-launch and retry allowance.
3. Use direct root-to-helper assignments. Bundled helpers execute directly and do not spawn descendants.
4. Keep every assignment equal to or narrower than the root task in inputs, data access, permissions, scope, non-goals, authority, approval boundary, ownership, and workspace.
5. Dispatch only work whose dependencies are satisfied and that fits the remaining allowance plus runtime, safety, and ownership capacity. When capacity is full, do not queue speculative helpers.
6. Before retrying, identify what failed and what will change. A replacement remains root-authorized, consumes the finite allowance, and uses the same verified Luna/max route.

This is a Codex-specific routing rule. Codex supports explicit model and reasoning-effort arguments on child-execution launches as well as those TOML fields, so this repository fixes every child execution route to Luna/max independently of the root session. A verified pinned profile supplies that route when launch-time overrides are unavailable. Do not use this document to prescribe or describe routing in the independently maintained Claude Code edition.

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

No helper may silently change its execution model or effort, fall back to a parent setting, or request a model escalation. Any replacement or reroute remains root-owned and must select a verified Luna/max profile or use explicit Luna/max child-execution settings.

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
Expected benefit:
Goal:
Context:
Scope:
Non-goals:
Permissions:
Finite helper-launch and retry allowance:
Declared ownership or read scope:
Exact assigned workspace and worktree permit ID when applicable:
Acceptance condition:
Evidence required:
Escalation conditions:
Output format:
Return format:
```

## Acceptance Check

Before accepting delegated work, confirm:

- the child execution selected a verified profile pinned to `gpt-5.6-luna`/`max`, or explicitly passed those values as child-execution settings
- parent-model and parent-effort inheritance were not used unintentionally for child execution
- progress and task-reporting messages omitted model, reasoning, thinking, and analogous destination-setting overrides and did not alter a parent or peer task
- the assignment's expected benefit and place within the finite allowance were recorded
- the helper executed directly and did not spawn descendants
- write ownership was disjoint or conflicting work was serialized
- the subagent used its exact assigned workspace and did not create, repurpose, move, or remove a worktree
- the stated acceptance condition passed
- the subagent stayed within scope and authority
- claims are supported by primary evidence
- any edits are minimal and task-related
- the main agent independently reviewed material findings and edits
