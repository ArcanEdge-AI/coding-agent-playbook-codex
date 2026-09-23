The primary global coding-agent behavior may be configured in Codex Personalization > Custom instructions or in this AGENTS.md file.

Supporting references live inside their owning skill packages under the Codex home:

- `skills/reference-doc-routing/references/README.md` — map of packaged reference docs
- `skills/reference-doc-routing/references/engineering-design.md` — selective design questions and examples for complete solutions and justified complexity
- `skills/subagent-orchestration/references/model-routing.md` — mandatory explicit Luna/max subagent routing, escalation, and acceptance rules
- `skills/subagent-orchestration/references/subagents.md` — subagent delegation rules, assignment template, and acceptance checklist
- `skills/worktree-lifecycle/references/worktrees.md` — root-owned task-local worktree budgeting, permits, integration, cleanup, and preservation rules
- `skills/feature-branch-lifecycle/references/branching-rule.md` — development-branch integration, complete-feature validation, promotion, and safe temporary-branch cleanup
- `skills/multi-session-coordination/references/multi-session-coordination.md` — discovery, thread naming, ownership, sequencing, conflict detection, and integration guidance for independent project threads
- `skills/reference-doc-routing/references/reference-doc-routing.md` — how to decide which docs to consult and how to treat them
- `skills/reference-doc-routing/references/templates/` — templates for repository-level architecture, testing, access-control, design-system, release, API, and data-model docs
- `skills/*/references/templates/` — skill-owned active-work, task-graph, and worktree-manifest templates

Reusable skills live under `skills/`, including:

- `subagent-orchestration`
- `task-graph-orchestration`
- `worktree-lifecycle`
- `feature-branch-lifecycle`
- `legacy-path-retirement` — dependency-based retain, migrate, or remove decisions with separate data-retention and correctness safeguards
- `multi-session-coordination`
- `reference-doc-routing`
- `senior-code-review`

Custom Codex subagents live under `agents/`, including the base and `-luna` planner, engineer, reviewer, tester, and docs profiles.

Reference documents are supporting context, not automatic truth. The main agent remains accountable for orchestration, final diff, validation, acceptance, and the final response.

Configure every delegated helper execution through a verified Luna/max profile or explicit child-execution settings, independently of the root model or effort. This requirement does not apply to tool calls or reporting messages. Helpers must preserve parent and peer settings, execute their assignment directly without spawning descendants, and omit destination model and reasoning overrides from separately authorized task reports.

The auxiliary-worktree budget starts at zero. Only root may issue a worktree permit or create, adopt, repurpose, move, or remove an auxiliary worktree. Before the final response, remove each task-created auxiliary under verified safety gates or preserve it with its exact owner, path, branch or HEAD, blocker, and next action.
