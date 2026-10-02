# Subagent Delegation Reference

The main agent is the primary implementer and remains accountable for task framing, design, implementation, integration, verification, authorized delivery, and the final response. Use helpers sparingly when a bounded benefit justifies their extra context, coordination, latency, and review cost, or independent assistance is required; they do not own the outcome.

## When Assistance Is Worthwhile

Use a helper when it provides one or more concrete benefits:

- independent evidence for a risky or disputed claim
- genuinely parallel progress on separable, non-conflicting work
- focused reproduction, log analysis, documentation lookup, or review
- reduced main-agent context for a large bounded investigation

Do not delegate merely because tools are available, a task is substantial, a graph has many nodes, or a role would otherwise be unused. Do not delegate tightly coupled work that requires repeated reconstruction of the same context, and do not outsource work the main agent has already completed.

No helper is required for a task to be legitimate. The main agent may directly complete coherent single-file, multi-file, or substantial work without recording an exception.

## Role Perspectives and Helper Assignments

Each profile separates reusable role guidance from rules for delegated execution. The main agent may consult the role perspective directly for a concrete question without changing its model, reasoning effort, permissions, approval gates, or ownership. It does not inherit the profile's launch settings or helper-only escalation rules by reading them. Select only useful guidance, with no required role sequence or separate report. This is self-review; preserve separately required independent verification.

| Role | Delegated mode | Best for |
| --- | --- | --- |
| planner | Read-only | Outcomes, reuse opportunities, risks, real dependencies, and completion checks. |
| engineer | Bounded write | A clearly owned implementation slice after interfaces and constraints are known. |
| reviewer | Read-only | Independent review of a bounded diff, design, or claim. |
| tester | Read-mostly | Proportionate checks, evidence evaluation, and failure diagnosis when needed. |
| docs | Read-only | Repository documentation and authoritative source lookup. |

For actual delegation, choose a role whose boundary fits the bounded assignment. A useful perspective alone does not justify launching a helper.

## Flat Delegation Boundary

Use direct root-to-helper assignments. Bundled helpers execute directly and do not spawn descendants. If a helper discovers additional work, ambiguity, a missing dependency, or a need for broader authority, it stops and reports upward.

Recursive orchestration is not part of the default workflow. It requires separate explicit authorization, a bounded manifest, ownership and routing controls, and proportionate verification. The ordinary installed profiles do not provide that authorization.

## Finite Execution Allowance

Before dispatching, root sets a finite helper-launch and retry allowance. A retry consumes the allowance even when the same helper or assignment is reused.

Expand the allowance only for an identified new dependency, invalidated gate, or changed user scope. Obtain user approval immediately before a material expansion of execution cost. Do not queue speculative work when runtime capacity is full.

## Dependency-Aware Assignments

For multi-node work, a helper may own a ready graph node or another bounded subset. Define:

| Field | Purpose |
| --- | --- |
| Goal | One concrete outcome. |
| Inputs | Only the artifacts, decisions, code, tests, or documentation required. |
| Output and acceptance | The artifact or finding and observable criteria it must satisfy. |
| Depends on | Only accepted upstream work required before starting. |
| Read/write scope | Exact ownership; serialize overlap unless isolation is verified. |
| Verification gate | Evidence required before acceptance. |
| Workspace | Exact shared workspace or root-permitted auxiliary worktree. |
| Route | Verified task-selected model and effort at Standard speed. |

A graph node does not have to be delegated. The main agent owns graph topology, readiness, integration, and final acceptance.

## Worktrees Are Separate

Start with the current workspace and an auxiliary-worktree budget of zero. A helper, retry, role, or graph node does not imply a new checkout.

Only root may raise the worktree budget, issue a permit, or create, adopt, repurpose, move, or remove a worktree. Helpers use the exact assigned workspace and report any isolation need upward. Follow the worktree-lifecycle skill for integration and final disposition.

## Task-Based Model Selection

Consult references/model-routing.md before launching a helper.

Select every delegated execution, retry, and replacement by the actual assignment using the approved task table: GPT-6.1 Sol at Light, Medium, or High, or GPT-6 Astra at Extra High. Light uses `low` in configuration. Use Standard speed only, not Fast. A profile's explicit model and effort can override spawn arguments, so establish the effective route. The main agent's user-selected model and effort remain independent.

A helper must stop if the route is unavailable. It may not silently inherit, substitute a model, lower effort, or request escalation. Progress and task-reporting messages must preserve parent and peer settings.

## Keep Consequential Ownership With Root

Root retains final ownership of:

- architecture and system design
- security, access-control, privacy, payment, and billing decisions
- destructive or irreversible operations
- migrations and persisted-schema strategy
- complex concurrency and shared-state design
- public API compatibility
- release and production-impacting configuration
- large or high-impact refactors
- final acceptance

A helper may gather bounded evidence or perform an authorized implementation slice, but root makes and verifies consequential decisions.

## Assignment Template

~~~text
Goal and acceptance:
[Bounded result and observable acceptance check.]

Expected benefit:
[Independent evidence, parallel progress, or context reduction.]

Context and authoritative inputs:
[Only necessary facts, paths, interfaces, and accepted upstream evidence.]

Skills and graph dependencies:
[Applicable skills and real dependencies, or None.]

Scope and authority:
[Permitted reads/writes, non-goals, permissions, and approval boundary.]

Ownership and workspace:
[Exact workspace and disjoint write ownership or bounded read scope.]

Child-execution route:
[Verified task-selected model, reasoning effort, and Standard speed.]

Launch/retry allowance:
[Assignment's place within the finite allowance.]

Stop conditions:
[Ambiguity, conflict, scope expansion, unavailable route, or high-impact decision.]

Return:
[Artifact or findings, primary evidence, checks run, and unresolved issues.]
~~~

## Acceptance Checklist

Before accepting helper work, verify:

- the effective route matched the task-selected model and effort at Standard speed, without unintended inheritance or conflicting profile overrides
- the helper did not spawn descendants
- the assignment stayed within scope, authority, ownership, and workspace
- claims are backed by primary evidence
- edits are minimal and task-related
- checks actually ran and support the acceptance condition
- reporting did not alter parent or peer settings
- retries and replacements stayed within the finite allowance
- any task-created auxiliary worktree has an accepted final disposition
- the main agent inspected material findings, the combined diff, and integrated behavior

A reason for not running a required check is not a passing result. Resolve disagreements through primary evidence, not confidence.
