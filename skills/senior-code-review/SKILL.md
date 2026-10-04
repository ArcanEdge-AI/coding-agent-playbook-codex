---
name: senior-code-review
description: Use before finalizing a meaningful code change. Reviews the final diff for correctness, scope control, maintainability, validation gaps, safety risk, performance risk, accessibility risk, and subagent claims that still need verification.
---

# Senior Code Review Skill

Use this skill before finalizing meaningful code changes.

Review the final diff for:

- unrelated changes
- accidental formatting churn
- generated, vendored, compiled, or package-owned files
- missing or weak validation
- redundant tests, fixtures, or mocks; tests preserving abandoned partial fixes or implementation details rather than intended final behavior
- any created unit test left in the completed change, regardless of its purpose or label; isolated integration tests retained, unused unit-test support code, or cleanup before corresponding E2E assertions pass
- unused imports, variables, types, functions, or files caused by the change
- naming clarity
- consistency with existing patterns
- incomplete fixes that minimize the diff while leaving required behavior unresolved
- abstractions without a demonstrated boundary, invariant, meaningful duplication, or variability
- substantial flow replacements without evidence of a significant benefit over improving the existing implementation, accounting for migration, verification, and maintenance costs
- unnecessary change amplification across unrelated components
- material technical debt without its scope, rationale, and follow-up condition
- speculative configurability
- behavior changes beyond the request
- API compatibility required by supported consumers or explicit commitments
- legacy paths or fallbacks retained without demonstrated dependencies, or removed despite unresolved consumers
- support commitments invented for hypothetical users, obsolete test accounts, fixtures, or intermediate development versions
- code retirement that discards useful data without authority or weakens necessary correctness safeguards
- migration risk
- safety risk
- performance risk
- accessibility regressions
- subagent claims that were not independently verified
- helper launches or retries that exceeded the recorded finite allowance or were not reconciled
- unnecessary helper use whose concrete benefit does not justify context, coordination, and review overhead
- child execution outside the approved task-based model/effort choices, conflicting profile overrides, or permissions, scope, authority, or workspace expansion beyond the parent assignment
- progress or task-reporting messages that set `model`, `reasoning_effort`, `thinking`, or analogous destination-setting overrides, or altered a parent or peer task
- task-created auxiliary worktrees without integration evidence and a verified `removed` or exact-blocker `preserved` disposition

Ask:

```text
Would I approve this in code review?
```

If not, fix the issue or report the remaining risk clearly.

Recommend retained E2E tests only for an identified important behavior or realistic regression risk that existing coverage does not establish, including relevant failure and boundary cases. Every unit test created is temporary, regardless of purpose; none may remain in a completed change. Verify their still-required assertions in passing E2E coverage before removing them and exclusively used support code. Keep migration of existing non-E2E suites within authorized scope. Build, lint, type checking, and static validation remain appropriate. Preserve required assertions and repository gates, and never treat deleting a failing test as resolving its failure.

Final report format:

```text
Summary:
- Changed X to do Y.

Verification:
- Ran: [command or check]
- Result: [passed/failed/not run, with reason]

Notes:
- [Assumptions, unrelated issues, subagent usage, follow-ups, or risk notes if any]
```
