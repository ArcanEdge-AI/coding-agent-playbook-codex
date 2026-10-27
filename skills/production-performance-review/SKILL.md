---
name: production-performance-review
description: Review and improve production performance and scalability, including slow queries, missing indexes, N+1 patterns, pagination, bundle size, asset optimization, unnecessary API calls, caching, expensive renders, memory leaks, blocking work, and startup costs. Use when preparing a codebase for production speed and scale.
---

# Production Performance Review

## Core purpose

Identify production performance risks and apply safe optimizations without changing product behavior.

## Use this skill when

- The production pass needs performance review.
- The user wants the app checked for production speed or scalability risks.
- The repository has database, API, frontend, asset, or rendering performance concerns.

## Do not use this skill when

- The task is only security or documentation.
- The user asks for speculative optimization without evidence.
- Performance cannot be evaluated from available code or commands.

## Check for

- Slow or inefficient queries
- Missing database indexes
- N+1 query patterns
- Missing pagination
- Large frontend bundles
- Unoptimized images or assets
- Unnecessary API calls
- Expensive frontend renders
- Avoidable re-renders
- Blocking synchronous work
- Missing caching opportunities
- Memory leaks
- Startup performance issues
- Background job opportunities
- Excessive network payloads
- Inefficient loops in critical paths

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Identify stack and performance-relevant tooling.
2. Inspect data access patterns.
3. Inspect API and frontend loading patterns.
4. Inspect asset and bundle configuration.
5. Identify performance risks in critical user flows.
6. Classify findings as Blocker, High, Medium, or Low.
7. When optimization changes are authorized, implement safe in-scope optimizations only; otherwise report the evidence and recommendation:
   - pagination where obviously needed
   - query cleanup
   - index recommendations or safe index additions
   - asset references
   - obvious caching improvements with safe invalidation
   - frontend render improvements where clearly justified
8. Document larger changes as deferred recommendations.
9. Run available validation.

## Severity guidance

Classify as Blocker when performance prevents critical production flows from working or risks immediate outage.

Classify as High when performance creates serious production risk under expected usage.

Classify as Medium when performance should be improved soon but is not release-blocking.

Classify as Low for optional optimization opportunities.

## Guardrails

- Do not optimize blindly.
- Do not add caching that risks stale or incorrect data without clear invalidation.
- Do not introduce new infrastructure unless required.
- Do not change user-visible behavior for performance unless explicitly justified.
- Prefer measurable improvements where tooling allows.
- Do not add complex optimization patterns for minor gains.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Performance findings
- Safe optimizations applied
- Larger deferred recommendations
- Validation results
- Remaining scalability risks
- Files changed and reasons