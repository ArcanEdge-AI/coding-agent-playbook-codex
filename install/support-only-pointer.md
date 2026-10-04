The primary global coding-agent behavior may be configured in Codex Personalization > Custom instructions or in this AGENTS.md file.

Supporting references live inside their owning skill packages under the Codex home:

- `skills/reference-doc-routing/references/README.md` — map of packaged reference docs
- `skills/reference-doc-routing/references/engineering-design.md` — selective design questions and examples for complete solutions and justified complexity
- `skills/subagent-orchestration/references/model-routing.md` — task-based model and reasoning choices, escalation, and acceptance rules
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

Custom Codex subagents live under `agents/`, with one profile each for planner, engineer, reviewer, tester, and docs.

The main agent may consult a profile's role perspective directly without launching a helper, changing its settings or authority, or applying delegated-use restrictions to itself. Use only relevant perspectives; no role sequence or separate report is required. Self-review does not satisfy a required independent-verification gate.

Reference documents are supporting context, not automatic truth. The main agent completes work directly by default and remains accountable for the requested outcome, final diff, validation, acceptance, and the final response.

Retain E2E behavioral tests only. Every unit test created is temporary, regardless of purpose; none may remain in a completed change. They may guide development, but remove them and exclusively used support code after corresponding E2E coverage passes. Preserve required assertions and repository gates, and keep existing non-E2E migration within authorized scope. Build, lint, type checking, and static validation remain appropriate.

Use subagents sparingly when a bounded benefit outweighs the added overhead or independent assistance is required. Select each actual helper route by task using the model-routing reference: GPT-6.1 Sol at Light, Medium, or High, or GPT-6 Astra at Extra High. Light uses `low` in configuration. Establish the effective settings because profile values can override spawn arguments. Preserve the main agent's selected settings. Helpers execute directly without descendants, and reporting messages must omit destination model and reasoning overrides.

The auxiliary-worktree budget starts at zero. Only root may issue a worktree permit or create, adopt, repurpose, move, or remove an auxiliary worktree. Before the final response, remove each task-created auxiliary under verified safety gates or preserve it with its exact owner, path, branch or HEAD, blocker, and next action.
