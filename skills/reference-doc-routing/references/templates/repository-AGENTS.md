# Repository Coding Agent Instructions

Follow the host's instruction hierarchy first. Within the same authority level, apply repository-specific instructions where they are more specific than global guidance.

Keep the sections your project needs. Record requirements a contributor could miss when reading the code, tests, or documentation.

## Repository Overview

Identify the components this guidance covers and any ownership boundaries that affect where a change belongs.

## Build, Test, and Validation

Give the setup, build, and validation commands, including targeted and full E2E runs, or link to the project’s existing command list. Include the working directory and environment when they affect the result.

Use existing checks first. Each proposed new case should catch a credible wrong result the others miss. E2E is the default for retained behavioral tests. If the maintainers have explicitly approved a focused exception, name the specific rule here and explain why a supported entry point cannot exercise it adequately. This template grants no exception. Preserve required coverage, failure cases, and existing test gates.

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
