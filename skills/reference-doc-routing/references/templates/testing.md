# Testing Strategy

## Test Commands

Document targeted and full E2E commands, plus build, lint, type checking, and static validation commands.

State which checks are mandatory, which changes trigger broader checks, and when accepted results can be reused. Start with the smallest meaningful checks and run affected required gates after the final relevant change; avoid full-suite runs after every small edit.

## Retained Test Policy

Retain only end-to-end (E2E) behavioral tests. Do not retain unit or isolated integration suites. Exercise complete supported flows through real UI, API, or CLI entry points, relevant dependencies, and observable results such as persistence or user-visible state. Direct helper calls and mocked internal flows do not count as E2E evidence.

Build, lint, type checking, and static validation remain appropriate checks. Visual or snapshot assertions may be part of an E2E flow; they do not establish the entire flow by themselves.

## Test Conventions

Document E2E naming, structure, fixtures, environment setup, dependency boundaries, and disposable test-data cleanup.

Reuse or extend existing E2E coverage for intended final behavior, important business rules, meaningful failures, boundary cases, and realistic regression risks. Do not add a permanent test for every helper or partial implementation.

## Temporary Unit Tests and Cleanup

Every unit test created is temporary, regardless of its purpose or who creates it. None may remain in a completed change. Unit tests may guide development or diagnosis; map their still-required behavioral assertions to corresponding E2E cases. Once those cases pass, remove all created unit tests and any fixtures, mocks, helpers, or dependencies used only by them before completing the change. Do not remove support code still used by E2E tests or production. Classify tests by exercised behavior, not filenames or labels; renaming a unit test does not make it E2E.

Migrate existing non-E2E suites only within authorized scope after replacement coverage passes. Investigate failing tests before removal; do not weaken required assertions or disable repository gates to obtain a pass. If E2E execution is unavailable or blocked, report the gap and unfinished cleanup rather than treating unit coverage as the completed solution.

As the implementation changes, update, consolidate, or remove E2E tests and fixtures that only preserve abandoned fixes. Preserve still-required assertions and explicit coverage gates.

## Regression Testing

For bugs, prefer an E2E reproduction or regression test when feasible. Verify the actual success, failure, and boundary outcomes affected by the fix.

## Snapshot Rules

Do not update snapshots blindly. Inspect diffs and confirm they match intended behavior.

## Known Constraints

Document slow tests, flaky tests, unavailable environments, or validation gaps.
