# Codex Task-Based Model Routing

Use subagents sparingly, only when a bounded assignment's concrete benefit outweighs its context, coordination, latency, and review cost, or a governing instruction requires independent assistance. A role perspective can be applied directly by the main agent without launching a helper.

## Choose by the Actual Task

Optimize for the total cost of an accepted result: input and reasoning tokens, repeated context, retries, corrections, coordination, and verification. A lower token price or a higher reasoning setting does not establish better value. Choose sufficient capability upfront without a mandatory cheap attempt first. Use comparable task evidence when available; do not invent savings or run paid comparisons without authority.

| Task | Model | Reasoning setting |
| --- | --- | --- |
| Narrow lookup, extraction, file mapping, log summaries | `gpt-6.1-sol` | Light |
| Clear implementation, local fixes, bounded planning or straightforward review | `gpt-6.1-sol` | Medium |
| Coupled changes, difficult debugging, substantial review, conflicting evidence | `gpt-6.1-sol` | High |
| Hard architecture questions, persistent debugging, complex cross-system reasoning | `gpt-6-astra` | Extra High only |

Light is the app's reasoning label; use `low` for `model_reasoning_effort` in TOML and supported launch fields. Medium, High, and Extra High use `medium`, `high`, and `xhigh`. Do not write `light` as a configuration value.

**Standard speed only. Do not select Fast.** Speed is separate from reasoning effort. High-impact judgments remain with the main agent even when a helper contributes evidence.

These are approved policy choices, not a measured performance ranking for every repository. Change them only through an explicit policy decision. Do not substitute a different generation merely because it is newer or available.

## Profile Defaults and Effective Settings

Each role has one profile with an explicit default:

| Profile | Default model | Reasoning | Typical delegated scope |
| --- | --- | --- | --- |
| `docs` | `gpt-6.1-sol` | Light | Focused source lookup and extraction. |
| `planner` | `gpt-6.1-sol` | Medium | Bounded planning and real dependencies. |
| `engineer` | `gpt-6.1-sol` | Medium | Clear, isolated implementation. |
| `tester` | `gpt-6.1-sol` | Light | Focused log analysis and known-check reproduction. |
| `reviewer` | `gpt-6.1-sol` | High | Substantial bounded review. |

The task table controls selection. For example, difficult root-cause analysis assigned to a tester requires a stronger route than its default, while a straightforward review may use GPT-6.1 Sol/Medium. Do not create model-specific copies of the roles.

On hosts using Codex custom-agent files, explicit `model` and `model_reasoning_effort` values in the file can override spawn arguments. Verify precedence before dispatch. Use a matching profile, or a supported explicit launch that carries the relevant role instructions, scope, and safeguards without a conflicting profile override. Never assume passing a different model alongside a fixed profile changes the effective model.

Use the host's actual fields and controls to establish the effective model, effort, and Standard speed. Bundled files declare model and effort; they do not mechanically enforce the live speed setting. An omitted service tier does not prove that Fast is disabled in a parent or session override. Do not invent a Standard-speed configuration value or silently accept Fast when the host cannot establish the requested route. Keep the work with the main agent or report an unmet independent-verification gate.

Reading a role perspective does not change the main agent's model, reasoning, permissions, or ownership and does not count as independent verification. Preserve the main agent's user-selected settings; recommend a change when useful and let the user select it.

## Selection and Retry Rules

1. Establish that the helper is useful, authorized, and within the finite launch/retry allowance before selecting its route. Task size, available roles, and graph nodes do not require delegation.
2. Record the bounded result, acceptance check, expected benefit, exact scope and workspace, model, reasoning effort, and Standard speed in the existing assignment.
3. Use direct root-to-helper assignments. Helpers do not spawn descendants or broaden their inputs, access, scope, permissions, or ownership.
4. Dispatch only ready work within available capacity. Serialize conflicts and do not queue speculative helpers.
5. Before retrying or reassigning, identify what failed and what will change. Reuse accepted evidence. Avoid chains of attempts that repeat the same misunderstanding.
6. Only the main agent may select a different approved helper route, based on the task evidence and within the existing finite allowance. Obtain specific approval before a material cost expansion. Keep parent and peer settings unchanged.

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
- the host cannot establish the selected model, reasoning effort, and Standard speed

Helpers return evidence and a blocker when a task or route is unsuitable. They may not change their own execution settings or silently fall back to inherited settings. The main agent decides whether to complete directly, correct the assignment, or use another approved route within the existing execution and cost authority.

## Reporting and Follow-up Messages

Subagents must not alter a parent or peer task's model or reasoning settings. Use team `collaboration.send_message` or the normal final return for progress and task reporting. If separately authorized task reporting uses `send_message_to_thread`, omit `model`, `thinking`, and analogous destination-setting overrides entirely; do not echo the sender's model, guess or reassert the parent's model, or change settings as a workaround. A follow-up message to an existing worker need not repeat its verified execution route.

Correct:

```text
Child execution: establish the approved task-selected model, reasoning effort, and Standard speed.
Task report: send_message_to_thread({ threadId: parentId, prompt: "..." })
```

The task-reporting call above is allowed only when separately authorized and intentionally omits model, effort, thinking, and destination-setting overrides.

Incorrect:

```text
send_message_to_thread({ threadId: parentId, prompt: "...", model: "gpt-6.1-sol", thinking: "high" })
```

The incorrect form can override the destination task's model or reasoning settings.

## Required Assignment Fields

```text
Role:
Selected profile or model: [Verified profile or supported explicit task-selected route]
Reasoning effort: [Light, Medium, High, or Extra High from the task table; configuration: low, medium, high, or xhigh]
Speed: Standard
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

- the effective model and reasoning effort match the approved task choice, and Standard speed is established
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

## Capability References

For host behavior, consult the current [custom-agent precedence documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents), [model and reasoning labels](https://learn.chatgpt.com/docs/models#pick-a-reasoning-effort), [GPT-6.1 Sol model specification](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [configuration values](https://learn.chatgpt.com/docs/config-file/config-reference), and [speed controls](https://learn.chatgpt.com/docs/agent-configuration/speed). These explain capabilities; availability alone does not expand this playbook's approved routes.
