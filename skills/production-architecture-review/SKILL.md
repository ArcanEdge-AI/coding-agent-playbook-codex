---
name: production-architecture-review
description: Review architecture, module boundaries, dependency structure, framework patterns, coupling, folder organization, scalability risks, and deferred refactor needs during a production-readiness pass. Use when assessing whether the codebase structure can safely support production release and near-term maintenance.
---

# Production Architecture Review

## Core purpose

Identify architecture risks and recommend or apply only safe structural improvements.

## Use this skill when

- The production pass needs architecture review.
- The user wants to know whether the codebase structure is production-safe.
- The repository may have poor module boundaries, circular dependencies, dependency bloat, or risky framework patterns.

## Do not use this skill when

- The task is only code cleanup.
- The task is only security scanning.
- The task is only DevOps or deployment validation.
- The user wants a full rewrite.

## Check for

- Unclear module boundaries
- Business logic mixed into UI, routing, or controller layers
- Circular dependencies
- Overly coupled modules
- Framework anti-patterns
- Inconsistent folder structure
- Dependency bloat
- Deprecated packages
- Risky package versions
- Duplicated architectural patterns
- Missing separation between domain, infrastructure, and presentation concerns
- Areas likely to block future scaling or feature work

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Inspect repository layout.
2. Identify major application layers.
3. Identify package manager and dependency files.
4. Review dependency graph where tooling exists.
5. Identify architectural seams and high-risk coupling.
6. Classify findings as Blocker, High, Medium, or Low.
7. Recommend deferred refactors separately from required production fixes.
8. Implement structural fixes only within authorized remediation scope. A production blocker establishes severity, not permission to change code during an assessment.
9. Include architecture notes in the requested deliverable; modify project documentation only when authorized.

## Severity guidance

Classify as Blocker when architecture prevents building, deploying, securing, or operating a critical production flow.

Classify as High when architecture creates serious production risk, such as auth logic being bypassable due to poor boundaries or critical services being too tightly coupled to test.

Classify as Medium when refactoring would improve maintainability but is not release-blocking.

Classify as Low for minor folder, naming, or organization improvements.

## Guardrails

- Do not perform large rewrites.
- Do not move many files unless necessary.
- Do not introduce a new architecture style into an existing codebase without clear justification.
- Do not upgrade major dependencies unless the risk requires it.
- Prefer documenting future refactors over destabilizing the release.
- Preserve working behavior.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Architecture summary
- Dependency risk summary
- Production-blocking architecture risks
- Deferred refactor list
- Safe structural fixes
- Files changed and reasons