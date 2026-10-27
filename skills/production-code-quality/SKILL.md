---
name: production-code-quality
description: Audit and improve code quality and maintainability during a production-readiness pass. Use when reviewing dead code, unused imports, lint errors, type errors, duplication, complexity, naming, formatting, debug artifacts, hardcoded values, fragile assumptions, and maintainability risks before release.
---

# Production Code Quality

## Core purpose

Identify and safely improve maintainability risks without changing product behavior.

## Use this skill when

- The production pass needs a code quality review.
- The repository has lint errors, type errors, duplication, dead code, or unclear implementation patterns.
- The user wants maintainability improved before release.

## Do not use this skill when

- The issue is primarily security, database, DevOps, API, or performance related.
- The requested change requires a broad architectural rewrite.
- The user only wants a feature implemented.

## Check for

- Dead code
- Unused files
- Unused imports
- Unused variables
- Unused dependencies
- Debug statements
- Temporary console logging
- Commented-out experimental code
- Duplicated logic
- Overly complex functions, classes, components, or modules
- Poor naming
- Inconsistent formatting
- Type errors
- Lint errors
- Hardcoded values
- Fragile assumptions
- Production-impacting TODOs or FIXMEs

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Inspect project conventions before editing.
2. Identify lint, format, typecheck, and test commands.
3. Run the narrowest useful static checks when available.
4. Produce findings classified as Blocker, High, Medium, or Low.
5. When remediation is authorized, fix safe in-scope issues first; assessment-only requests report recommendations:
   - unused imports
   - obvious dead code
   - debug logs
   - lint-safe formatting
   - type-safe cleanup
6. Do not refactor behavior-heavy code unless the risk is Blocker or High.
7. Run validation after edits.
8. Record the findings in the requested deliverable; update project readiness/risk files only when those artifacts are in scope.

## Severity guidance

Classify as Blocker when code quality issues prevent build, test, or runtime execution.

Classify as High when maintainability issues create serious production risk, such as fragile core flows, widespread type unsafety in critical paths, or debug behavior that leaks data.

Classify as Medium when cleanup is important but not release-blocking.

Classify as Low when the issue is cosmetic or future-facing.

## Guardrails

- Do not change product behavior for style-only improvements.
- Do not rename public APIs unless required.
- Do not introduce new abstractions unless they reduce a specific production risk.
- Do not perform sweeping formatting changes unless the repository already enforces that formatter.
- Preserve repository conventions.
- Do not delete code unless it is clearly unused or safely replaced.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Code quality findings
- Safe cleanup changes
- Validation results
- Deferred refactor list
- Files changed and reasons