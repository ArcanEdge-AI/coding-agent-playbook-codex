# Handoff Context Contract

Use this contract to decide what belongs in the new chat. Adapt headings to the work; do not add empty sections merely to satisfy a template.

## Evidence Labels

- **Verified current:** observed now from the repository, current command output, or a read-only connected service.
- **User-reported current:** explicitly stated by the user but not independently refreshed in this turn.
- **Historical:** tied to an older run, branch, release, document, or observation time.
- **Unverified:** plausible but unsupported or blocked by missing access.

State contradictions rather than choosing the more convenient source. For live-versus-source differences, record both.

## Material Context Inventory

### Purpose and status

- The user's actual goal and why the work exists.
- Current verdict: completed, in progress, blocked, failed, or inconclusive.
- What “done” means, especially any live acceptance boundary.

### Work and findings

- Changes made, analyses completed, and artifacts produced.
- Causal findings and the evidence that supports them.
- Research, simulations, comparisons, and alternatives explored.
- Approaches rejected or paused, with the reason they should not be rediscovered as new ideas.

### Validation

- Exact tests, builds, migrations, replays, audits, or live checks.
- Counts, outcomes, warnings, dependency/runtime context, and observation time.
- Known pre-existing failures and the comparison proving they are pre-existing.
- What the evidence proves and what remains unproven.

### User decisions and boundaries

- Approved direction, corrections, and non-negotiable behavior.
- Explicitly rejected interpretations or implementations.
- Actions already authorized and actions that still require approval.
- Safety, privacy, credential, customer-data, or production boundaries.

### Continuity anchors

- Repository/project path and current workspace.
- Branch/ref, commit, upstream, ahead/behind, dirty state, and preserved worktrees.
- PR, issue, run, release, deployment, environment, and evidence-ledger identifiers.
- Important files, plans, prompts, fixtures, and reports with exact paths.
- Connected-service identity and access state without secret values.

### Remaining work

- Open risks and missing evidence.
- The smallest correct next action.
- Preconditions and acceptance criteria for that action.
- Stop conditions that produce FAIL, INCONCLUSIVE, or a request for user direction.

## Repository Handoff Rules

- Do not tell the next chat to use a dirty primary checkout when a clean task worktree is the verified source of truth.
- Identify unrelated local changes and explicitly preserve them.
- Do not create a duplicate PR when an existing PR owns the work.
- Do not claim a branch is current without refreshing its remote state when that check is cheap.
- Separate source validation, CI, merge, deployment, and live acceptance as different states.

## Final Prompt Ending

End the seeded prompt with instructions equivalent to:

> Acknowledge the inherited state, refresh drift-prone facts, and state the exact next gate. Do not begin any merge, deployment, external mutation, destructive action, or newly expanded implementation without the user's authority.

## Completeness Check

Before creating the thread, confirm:

- every “finished” claim has an evidence handle;
- material failures and warnings are present;
- the next chat can locate the authoritative workspace and artifacts;
- current, historical, user-reported, and unverified facts are distinguishable;
- all user decisions that affect implementation or acceptance are preserved;
- no credential or unnecessary sensitive data appears;
- the new chat can continue without rereading the entire old transcript.
