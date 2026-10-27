---
name: session-cleanup
description: Use at the end of substantial coding work or when asked for a final cleanup or integrity pass over the current branch/work delta; compare against a verified integration baseline, remove in-scope debris and unnecessary complexity, preserve unrelated changes, and report validation honestly. It is not an audit after every edit or authorization for destructive cleanup.
metadata:
  short-description: Final cleanup and integrity review
---

# Session Cleanup

Use this skill at the end of substantial coding work or when the user asks for a deliberate cleanup and integrity pass. The work may have spanned a long-running session, multiple context compactions, many commits, interrupted runs, or more than one coding agent.

Do not use conversational memory as the boundary of the cleanup. Define the work from repository evidence.

The purpose of this skill is to leave the changed portion of the codebase in the smallest, clearest, production-appropriate state that satisfies the demonstrated requirement: no accidental debris, abandoned approaches, speculative compatibility paths, redundant abstractions, or unnecessary complexity.

Read the supplied methodology reference for the checks relevant to the current work delta: [post-session-cleanup-methodology.md](references/post-session-cleanup-methodology.md). Its numbered sections are the detailed procedure and its Completion Report is the required reporting shape.

## Scope and authority

- Establish the repository's verified integration baseline before cleanup. Prefer `staging` when it exists and repository evidence shows it is the normal integration target; otherwise use `main` or the repository's verified primary integration branch. Do not choose a baseline solely because of its branch name.
- Find the merge base between the current branch and the verified baseline. Treat the complete committed delta from that merge base through current `HEAD`, together with staged, unstaged, and untracked changes, as the primary cleanup surface. This is the **work delta**.
- Long-running work may span multiple context compactions or sessions. Never shrink the cleanup surface to only what the current conversation remembers.
- If the current branch is itself the integration baseline or there is no meaningful committed divergence, use the verified working-tree changes and explicit task evidence as the work delta. If the baseline remains uncertain, report that uncertainty and do not claim a clean completion.
- Preserve unrelated edits, staging, and user files, including files with mixed ownership. If ownership is uncertain, report it and continue independently verified work; do not silently rewrite or delete it.
- "Clean" means the work delta contains no unexpected debris, unresolved work-delta defect, abandoned implementation, or unnecessary complexity that should reasonably be removed now. It does not mean an empty Git status. Do not automatically stage, commit, discard, reset, or deploy.
- A cleanup request permits reversible, in-scope cleanup. An explicit inspection-only request remains read-only. Existing approval carries forward only within the stated scope; do not invent a universal approval gate.
- Never use destructive reset, clean, stash, or history manipulation, and do not make implicit production or deployment changes. Scope security checks to touched surfaces and do not expose secrets.
- Prefer the smallest complete correction and the smallest maintainable implementation surface. Preserve complexity only when required for correctness, security, data integrity, accessibility, maintainability, or a demonstrated compatibility requirement. Do not redesign, blanket-format, add dependencies merely for cleanup, or repair unrelated pre-existing issues.
- Prefer one canonical implementation path. Remove work-delta code that exists only because implementation churn, experimentation, or an abandoned design left it behind.
- Do not add compatibility behavior for hypothetical users, old data, API consumers, deployments, or integrations. New compatibility code requires evidence of a real supported dependency.
- Valid compatibility evidence includes currently deployed older versions, real persisted data using the old representation, active consumers using the old contract, documented supported-version requirements, an active migration window, or equivalent repository/runtime evidence.
- Confirm that the consumer or data actually requires continued support. Obsolete test accounts, fixtures, and hypothetical users are not support commitments; use `legacy-path-retirement` to separate that decision from data preservation or an authorized reset. Alpha status does not justify rebuilding the flow.
- "Someone might use it," "for backwards compatibility," "to be safe," "future-proofing," or similar speculation is not sufficient evidence.
- Existing baseline compatibility code is not automatically junk. Before removing it, verify callers, data, supported clients, deployments, migrations, configuration, and dynamic usage. If its necessity cannot be established either way, leave the pre-existing path unchanged and report the uncertainty.
- Branch history is not production history. Code introduced and superseded entirely within an unmerged development branch does not require backwards compatibility merely because an earlier commit used it.

## Review sequence

1. Establish the verified baseline and reconstruct the full work delta before editing. Determine the intended outcome, changed paths, ownership, and change classes. Include committed branch changes, staged/unstaged/untracked work, files, renames, configuration, dependencies, schemas/migrations, tests, docs, generated artifacts, and tooling.
2. Read the methodology sections selected by the routing tables below. Apply every relevant check; a small visible diff is not a reason to skip an affected section.
3. Remove or correct clear work-delta-introduced debris, defects, abandoned approaches, speculative compatibility code, and unnecessary complexity. Before each cleanup mutation, verify ownership and usages; preserve unrelated baseline behavior and record pre-existing problems separately. Re-review the resulting baseline comparison and status.
4. Validate with the project's defined commands, starting with the smallest relevant checks and then the broader required gates. Record actual pass, fail, unrun, or uncertain outcomes and classify each failure or blocker as work-delta-introduced, pre-existing, environmental/tooling, or unknown when evidence is insufficient. A material changed behavior that cannot be validated cannot be called complete and clean.
5. Report blockers and unresolved ownership or compatibility evidence plainly. Do not turn inability to inspect or validate into a success claim, and do not silently expand scope to make the report look clean.

### Methodology routing

For every work delta:

| Sections | Required focus |
| --- | --- |
| 1 | Verify the baseline and reconstruct committed, staged, unstaged, and untracked changes. |
| 2–5 | Find introduced debris, abandoned paths, speculative compatibility, unnecessary complexity, and code-quality defects. Verify ownership and usage before removal. |
| 11–12 | Review test value and failure/boundary coverage; run required affected checks. Every created unit test is temporary. Carry required assertions into passing E2E coverage before removing it and exclusively used support code. Keep existing-suite migration scoped. |
| 13–16 | Check affected docs against reality, classify deferred-work markers, inspect repository hygiene, and review the result from the next developer's perspective. |
| 17 | Before each extra cleanup change, ask: "Is this necessary to correctly complete, simplify, stabilize, or clean up the current work delta?" Leave unrelated issues alone. |

For affected behavior or boundaries:

| Section | When to apply | Required focus |
| --- | --- | --- |
| 6 | Behavior, inputs, network calls, permissions, retries, or state transitions changed. | Errors, realistic edge cases, and partial failures. |
| 7 | Persistence, APIs, schemas, migrations, serialization, or state management changed. | Data integrity and canonical state; old-state support requires demonstrated compatibility evidence. |
| 8 | A security or file-safety boundary was touched. | Secrets, authentication, authorization, ownership, input handling, logs, dynamic execution, and file safety. Do not expand into an unrelated audit. |
| 9 | Dependencies or configuration changed. | Packages, lockfiles, environment variables, build settings, and deployment configuration. |
| 10 | UI behavior changed. | Actual loading, empty, error, success, disabled, navigation, responsive, keyboard, accessibility, focus, and mutation flows. Source inspection alone is insufficient. |

## Evidence and stopping rules

- Base conclusions on the verified baseline comparison, current source, repository history, status, configuration, tests, and runtime evidence; do not rely on session memory alone.
- Treat search matches as leads. Confirm callers, dynamic references, configuration loading, persisted data, deployment/support requirements, and compatibility requirements before deleting pre-existing behavior.
- Do not preserve work-delta compatibility code merely because an earlier commit on the same unmerged branch used an older interface or representation.
- Keep validation evidence tied to the changed behavior and distinguish a failed check from a check that could not run.
- If a work-delta defect is found, fix it only when the correction is reversible, in scope, and verifiable; then repeat the affected checks and review the baseline diff.
- If ownership, baseline, compatibility evidence, or material behavior remains unresolved, stop short of a clean-completion claim and put the uncertainty in the report.

## Required report

Return exactly these categories, even when a category is empty:

## Cleaned Up

List meaningful cleanup performed.

## Validation

List checks actually run and their outcomes.

## Problems Found

List defects, incomplete work, accidental technical debt, abandoned approaches, speculative compatibility paths, or unnecessary complexity discovered.

## Remaining Issues

Separate work-delta-introduced issues, pre-existing issues, and optional future improvements, with reasons for anything left unresolved.

## Final State

Choose exactly one of:

- `complete and clean`
- `complete with documented remaining issues`
- `not yet safe to consider complete`

Use `not yet safe to consider complete` for required work-delta defects or material unvalidated behavior; documented remaining issues may use a complete state only when they do not block validated requirements.

Do not claim success when required validation was not performed or material changed behavior remains unverified.
