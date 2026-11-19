# Codex Task-Based Model Routing

Use subagents sparingly, only when a bounded assignment's concrete benefit outweighs its context, coordination, latency, and review cost, or a governing instruction requires independent assistance. A role perspective can be applied directly by the main agent without launching a helper.

## Choose by the Actual Task

Optimize for the total cost of an accepted result: input and reasoning tokens, repeated context, retries, corrections, coordination, and verification. A lower token price or a higher reasoning setting does not establish better value. Choose sufficient capability upfront without a mandatory cheap attempt first. Use comparable task evidence when available; do not invent savings or run paid comparisons without authority.

Use these default routes when no authorized per-task model and reasoning effort were specified.

| Task | Default model | Reasoning setting |
| --- | --- | --- |
| Source lookup, file mapping, log summaries, rerunning a known check | `gpt-6.2-sol` | Light |
| Bounded planning, implementation, choosing checks, or diagnosing a reproducible failure | `gpt-6.2-sol` | Medium |
| Coupled changes, difficult debugging, substantial review, or conflicting evidence | `gpt-6.2-sol` | High |
| Hard architecture questions, persistent debugging, complex cross-system reasoning | `gpt-6-astra` | Extra High |

Light is the app's reasoning label; use `low` for `model_reasoning_effort` in TOML and supported launch fields. Medium, High, and Extra High use `medium`, `high`, and `xhigh`. Do not write `light` as a configuration value.

High-impact judgments remain with the main agent even when a helper contributes evidence.

The user or an authorized maintainer may select an exact model and reasoning effort for one assignment within actual host, organization, and spending limits. That selection applies to that assignment. Changing the shipped defaults requires a separate policy decision. Model availability alone grants no authority to substitute or increase cost.

## Profile Defaults and Effective Settings

Each role has one profile with an explicit default:

| Profile | Default model | Reasoning | Typical delegated scope |
| --- | --- | --- | --- |
| `docs` | `gpt-6.2-sol` | Light | Locate an authoritative source and extract the relevant facts. |
| `planner` | `gpt-6.2-sol` | Medium | Identify dependencies and decide how to verify a bounded change. |
| `engineer` | `gpt-6.2-sol` | Medium | Trace the affected code and implement a scoped change. |
| `tester` | `gpt-6.2-sol` | Medium | Choose a check and determine whether a failure comes from the product, the test, or its setup. |
| `reviewer` | `gpt-6.2-sol` | High | Trace consequences across callers and weigh conflicting evidence before reporting a defect. |

Apply an authorized per-task selection first. Otherwise use the task table to match effort to the work. For example, rerunning a known check fits Light. Tracing an intermittent failure across services can justify High. Keep one bundled profile per role.

On hosts using Codex custom-agent files, explicit `model` and `model_reasoning_effort` values in the file can override spawn arguments. Verify precedence before dispatch. Use a matching profile, or a supported explicit launch that carries the relevant role instructions, scope, and safeguards without a conflicting profile override. Never assume passing a different model alongside a fixed profile changes the effective model.

After dispatch, verify the actual child model and reasoning effort from trustworthy runtime metadata or an equivalent host receipt before substantive work or acceptance. Requested launch arguments, a profile name, and the child's self-description are insufficient evidence. If the route differs or cannot be verified, stop that assignment. Root can perform independent authorized work or make an authorized reassignment within the remaining allowance. A specifically requested opinion or required independent check remains outstanding until an eligible reviewer supplies it.

Reading a role perspective does not change the main agent's model, reasoning, permissions, or ownership and does not count as independent verification. Preserve the main agent's user-selected settings; recommend a change when useful and let the user select it.

## Selection and Retry Rules

1. Establish that the helper is useful, authorized, and within the finite launch/retry allowance before selecting its route. Task size, available roles, and graph nodes do not require delegation.
2. Record the bounded result, acceptance check, expected benefit, exact scope and workspace, model, and reasoning effort in the existing assignment.
3. Use direct root-to-helper assignments. Helpers do not spawn descendants or broaden their inputs, access, scope, permissions, or ownership.
4. Dispatch only ready work within available capacity. Serialize conflicts and do not queue speculative helpers.
5. Before retrying or reassigning, identify what failed and what will change. Reuse accepted evidence. Avoid chains of attempts that repeat the same misunderstanding.
6. Only root may reassign within the selection and finite allowance authorized for the task. Honor an explicitly selected route. Obtain specific approval immediately before a material cost expansion. Keep parent and peer settings unchanged.

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

- a necessary fact or user-owned choice remains unresolved after checking available evidence
- conflicting evidence materially prevents the assigned conclusion
- the task exceeds its assigned scope
- the conclusion cannot be independently verified
- the work becomes security-sensitive, destructive, or production-impacting
- a consequential architectural or cross-system decision exceeds the assigned review or implementation authority
- the host cannot establish the selected model and reasoning effort

Helpers return evidence and a blocker when a task or route is unsuitable. They may not change their own execution settings or silently fall back to inherited settings. The main agent decides whether an in-scope correction, reassignment, or direct contribution is possible within existing authority.

## Reporting and Follow-up Messages

Subagents must not alter a parent or peer task's model or reasoning settings. Use team `collaboration.send_message` or the normal final return for progress and task reporting. If separately authorized task reporting uses `send_message_to_thread`, omit `model`, `thinking`, and analogous destination-setting overrides entirely; do not echo the sender's model, guess or reassert the parent's model, or change settings as a workaround. A follow-up message to an existing worker need not repeat its verified execution route.

Correct:

```text
Child execution: establish the approved task-selected model and reasoning effort.
Task report: send_message_to_thread({ threadId: parentId, prompt: "..." })
```

The task-reporting call above is allowed only when separately authorized and intentionally omits model, effort, thinking, and destination-setting overrides.

Incorrect:

```text
send_message_to_thread({ threadId: parentId, prompt: "...", model: "<child model>", thinking: "<child effort>" })
```

The incorrect form can override the destination task's model or reasoning settings.

## Required Assignment Fields

```text
Goal and acceptance: [Bounded result, acceptance check, expected benefit.]
Context: [Necessary facts, inputs, paths, interfaces, accepted evidence.]
Skills and methods: [Applicable skills, required references, real dependencies.]
Scope and authority: [Reads/writes, permissions, non-goals, constraints, stop conditions.]
Ownership and route: [Role and helper ID or permit, exact workspace, read/write ownership,
  verified profile or explicit model/effort, why it fits, place in launch/retry allowance.]
Return: [Artifact or findings, primary evidence, checks run, unresolved issues.]
```

## Acceptance Check

Before accepting delegated work, confirm:

- the effective model and reasoning effort match the approved task choice
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

Check model availability and authority on the host where the helper will run. See OpenAI’s [custom-agent precedence documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents), [model and reasoning labels](https://learn.chatgpt.com/docs/models#pick-a-reasoning-effort), [GPT-6.2 prompting guide](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra), and [configuration values](https://learn.chatgpt.com/docs/config-file/config-reference).
