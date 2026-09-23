# Task Graph: [Task Name]

Use this template only for work that benefits from a formal instruction-only task graph. Keep small or genuinely linear work in the normal working plan.

## Graph Metadata

- Goal: [One concrete outcome]
- Owner: [Main agent or coordinating task]
- Repository and workspace: [Current verified context]
- Applicable instructions: [Paths or sources]
- Status: [Proposed / Active / Blocked / Complete]
- Last updated: [Timestamp or execution checkpoint]
- Graph-mode reason: [Why this structure is justified]
- Multi-session preflight: [Not needed / completed with evidence / blocked]
- Helper-launch and retry allowance: [0 when no delegation is planned, otherwise finite count]
- Auxiliary-worktree budget: [Finite count; default 0]

## Success Criteria

- [Observable criterion]
- [Required validation]
- [Required user-visible result]

## Nodes

| ID | Bounded outcome | Inputs | Produced artifact or decision | Acceptance condition | Depends on | Reads | Writes or mutable state | Executor | Verification gate | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N0 | [Work] | [Authoritative inputs] | [Output] | [Observable rule] | None | [Scope] | [Scope or None] | [Root or directly assigned helper] | [Evidence] | Ready |

A node is a work outcome, not automatically an agent. Use states consistently: Proposed, Ready, Running, Complete, Failed, Blocked, or Superseded.

## Dependency Edges

| From | To | Consumed artifact or decision |
| --- | --- | --- |
| N0 | N1 | [Why N1 cannot correctly begin without accepted N0 output] |

Do not add an edge solely to mirror list order.

## Hidden-Constraint Review

- Shared file writes: [None or exact conflicts]
- Shared mutable state: [Ports, services, environments, locks, credentials, rate limits, or cost]
- Schema, interface, migration, or contract ordering: [None or exact dependency]
- External task, branch, worktree, or pull-request ownership: [None or exact constraint]
- Approval-gated actions: [None or exact action and authority]

## Current Ready Set

- [Node IDs whose dependencies and hidden constraints are satisfied]

## Optional Helper Assignments

Remove this section when no helpers are used.

| Node | Helper role | Bounded benefit | Exact workspace and scope | Luna/max route | Acceptance check | Attempt |
| --- | --- | --- | --- | --- | --- | --- |
| N0 | [Role] | [Independent evidence, parallel progress, or context reduction] | [Workspace and ownership] | [Verified profile or explicit settings] | [Evidence] | 1 |

Use direct root-to-helper assignments. Helpers execute their assignment directly and do not spawn descendants. Retries consume the finite allowance. Record what failed and what changes before retrying.

## Worktree Lifecycle

Worktrees are not delegation units. Start with the current workspace and an auxiliary-worktree budget of zero. Only root may issue a worktree permit or create, adopt, repurpose, move, or remove an auxiliary worktree.

| Worktree permit | Node or owner | Canonical path | Base ref and SHA | Branch or HEAD | Isolation reason | Integration target | Cleanup condition | State |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W1 | [Owner] | [Exact path] | [Ref and SHA] | [Branch or detached SHA] | [Why sharing or serialization fails] | [Accepted handoff] | [Required evidence] | [proposed / active / removed / preserved] |

Remove the placeholder row when no auxiliary worktree exists.

## Execution Ledger

| Node | Attempt | Result | Evidence or produced artifact | Downstream nodes invalidated |
| --- | --- | --- | --- | --- |
| N0 | 1 | [Complete / Failed / Blocked] | [Path, command result, diff, or finding] | [None or IDs] |

## Completeness Check

- Expected node IDs: [IDs]
- Accepted node IDs: [IDs]
- Missing node IDs: [IDs or None]
- Failed node IDs: [IDs or None]
- Blocked node IDs: [IDs or None]
- Superseded node IDs: [IDs or None]

## Approval Gates

| Gate | Action | Exact scope and consequence | Required authority | Status |
| --- | --- | --- | --- | --- |
| G1 | [Action] | [Target, audience, cost, permanence, and recovery path] | [User or system authority] | Blocked |

If no approval-gated action exists, write None and remove the placeholder row.

## Fan-In and Final Verification

- Consolidation nodes: [IDs and expected inputs]
- Integrated validation: [Commands, runtime checks, or inspection]
- Independent verification: [Helper or direct evidence, or reason not needed]
- Final diff reviewed: [Yes / No]
- Required nodes and gates complete: [Yes / No]
- Every task-created auxiliary worktree has a verified disposition: [Yes / No / N/A]
