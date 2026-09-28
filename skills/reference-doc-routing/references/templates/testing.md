# Testing Strategy

## Test Commands

Document targeted and full validation commands.

State which checks are mandatory, which changes trigger broader checks, and when accepted results can be reused. Start with the smallest meaningful checks and run affected required gates after the final relevant change; avoid full-suite runs after every small edit.

## Test Types

Describe available test layers:

- unit
- integration
- end-to-end
- visual/snapshot
- typecheck
- lint/static analysis
- build/smoke

## Test Conventions

Document naming, structure, fixtures, mocks, and setup patterns.

Retain tests for intended final behavior, important rules, and realistic regression risks. Focused unit tests for lasting business rules are appropriate. Reuse or extend existing coverage, and distinguish mocked checks from evidence of actual integration. Do not add a permanent test for every helper or partial implementation.

As the implementation changes, update, consolidate, or remove tests and fixtures that only preserve abandoned fixes. Preserve still-required assertions and explicit coverage gates. Temporary diagnostic checks need not be committed as lasting tests.

## Regression Testing

For bugs, prefer reproduction or regression tests when feasible.

## Snapshot Rules

Do not update snapshots blindly. Inspect diffs and confirm they match intended behavior.

## Known Constraints

Document slow tests, flaky tests, unavailable environments, or validation gaps.
