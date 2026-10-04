# Repository Coding Agent Instructions

Repository-specific instructions override global guidance where they are more specific.

## Repository Overview

Describe:

- what this repository does
- major applications/services/packages
- primary languages and frameworks
- important directories
- ownership boundaries

## Build, Test, and Validation

Document the normal commands for:

- install/setup
- targeted E2E tests
- full E2E suite
- typecheck
- lint
- format
- build
- local run/smoke test

Retain only E2E behavioral tests. Every unit test created is temporary, regardless of purpose; none may remain in a completed change. They may guide development, but remove them and exclusively used support code after corresponding E2E coverage passes. Preserve still-required assertions, failure cases, and repository gates. Keep migration of existing non-E2E tests within authorized scope.

## Architecture Rules

Document:

- where new behavior should be added
- where new behavior should not be added
- existing patterns to follow
- boundaries between modules/services/packages

## Change Rules

Document:

- branch/submission expectations
- generated files
- dependency policy
- migration policy
- release/versioning policy

## Reference Docs

List relevant repo docs and their authority level:

- `docs/architecture.md` — [authoritative/advisory/historical]
- `docs/testing.md` — [authoritative/advisory/historical]
- `docs/security.md` — [authoritative/advisory/historical]
