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
- unused imports, variables, types, functions, or files caused by the change
- naming clarity
- consistency with existing patterns
- incomplete fixes that minimize the diff while leaving required behavior unresolved
- abstractions without a demonstrated boundary, invariant, meaningful duplication, or variability
- unnecessary change amplification across unrelated components
- material technical debt without its scope, rationale, and follow-up condition
- speculative configurability
- behavior changes beyond the request
- API compatibility
- migration risk
- safety risk
- performance risk
- accessibility regressions
- subagent claims that were not independently verified
- finite-manifest nodes, root permits, or total-budget use that were not reconciled
- child call that did not select a verified Luna/max profile or explicit `gpt-5.6-luna`/`max` route, or permissions, scope, authority, or workspace expansion beyond the parent assignment
- task-created auxiliary worktrees without integration evidence and a verified `removed` or exact-blocker `preserved` disposition

Ask:

```text
Would I approve this in code review?
```

If not, fix the issue or report the remaining risk clearly.

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
