---
name: production-testing-qa
description: Audit and improve production QA readiness through complete end-to-end flows, existing required repository checks, critical user journeys, realistic failure and boundary coverage, flaky or skipped tests, manual QA, and honest validation summaries. Use for production-readiness assessments and authorized test improvements.
---

# Production Testing QA

## Core purpose

Identify behavioral coverage gaps, add practical E2E tests for high-risk areas when authorized, and document validation status. Keep assessment-only work read-only.

## Use this skill when

- The production pass needs testing and QA review.
- The user wants confidence that the codebase is safe to release.
- Critical user flows need automated tests or manual QA steps.

## Do not use this skill when

- The task is only code cleanup.
- The task is only deployment configuration.
- The user does not want tests added or run.

## Check for

- E2E coverage of important business rules through supported UI, API, or CLI entry points
- Complete API, service, and database flows with relevant dependencies and observable outcomes
- End-to-end tests for critical user journeys
- Broken tests
- Skipped tests
- Flaky tests
- Missing test setup documentation
- Untested authentication flows
- Untested authorization rules
- Untested error states
- Untested edge cases
- Missing regression coverage for core behavior

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Identify test framework and commands.
2. Inspect existing test structure.
3. Identify critical user flows from routes, UI, API, docs, or product structure.
4. Classify test gaps as Blocker, High, Medium, or Low.
5. For authorized remediation, check whether existing coverage exposes the identified failure. Extend a real flow only for a credible gap. In assessment mode, run authorized existing checks and report missing coverage.
6. Avoid writing brittle tests that only assert implementation details.
7. Run the narrowest useful test command after changes.
8. Run broader validation before final summary when practical.
9. Report validation results in the requested deliverable; update `TESTING_SUMMARY.md` only when that artifact is in scope.

## Critical flow heuristic

Prioritize test coverage for flows involving:

- Signup
- Login
- Logout
- Password reset
- Account settings
- Billing or payment
- Data creation
- Data editing
- Data deletion
- Permissions
- Admin actions
- File uploads
- External integrations
- Webhooks
- Deployment-critical configuration

## Severity guidance

Classify as Blocker when tests reveal failing critical flows, failing builds, or release-blocking validation failures.

Classify as High when critical flows lack coverage and would be expensive, risky, or embarrassing to break in production.

Classify as Medium when useful coverage is missing for non-critical flows.

Classify as Low for nice-to-have coverage or test cleanup.

## Guardrails

- Start with zero new permanent tests. For each proposed case, name a credible wrong result the remaining checks would accept. E2E is the default. A lasting focused test needs an explicit repository policy for a specified rule impractical to cover adequately at a supported entry point.
- For a failed check, verify the expected behavior independently of the test and reproduce the exact case when feasible. Fix a genuine product defect. Correct or discard faulty task-created tests while preserving real requirements. Give a new optional harness at most one evidence-based correction for a setup failure. If that fails the same way, stop the approach. Production changes need a product or design reason.
- Remove temporary diagnostics and their exclusively used support once required assertions have passing coverage. Keep unresolved behavior and mandatory failures open.
- Preserve existing mandatory repository suites until migration is authorized and replacement coverage passes. Do not bulk-delete pre-existing unit or isolated integration tests. Build, lint, types, and static validation remain useful checks.
- Do not delete failing tests unless they are clearly obsolete and documented.
- Do not weaken assertions to force passing tests.
- Do not mock away the behavior being tested.
- Do not claim coverage exists without evidence.
- Prefer meaningful coverage over high coverage percentages.
- Document unavailable test tooling honestly.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Test coverage findings
- Tests added or updated
- Commands run and results
- Manual QA checklist
- Remaining test gaps
- Files changed and reasons
