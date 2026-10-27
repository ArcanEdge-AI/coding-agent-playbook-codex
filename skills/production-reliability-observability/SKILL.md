---
name: production-reliability-observability
description: Audit and improve reliability, error handling, graceful failure behavior, logging, monitoring hooks, health checks, audit trails, timeout behavior, fallback states, and observability readiness during a production pass. Use when the codebase needs to fail safely and be diagnosable in production.
---

# Production Reliability Observability

## Core purpose

Improve production resilience and make failures easier to detect, diagnose, and recover from.

## Use this skill when

- The production pass needs reliability or observability review.
- The user wants the application to fail safely in production.
- The repository has missing error handling, logging, health checks, fallback behavior, or monitoring gaps.

## Do not use this skill when

- The issue is only visual polish.
- The issue is only dependency management.
- The user wants a new monitoring platform added without repository context.

## Check for

- Missing error boundaries
- Unhandled promise rejections
- Missing try/catch around risky operations
- Poor API error handling
- Missing loading states
- Missing empty states
- Missing fallback states
- Retry logic for unstable services
- Poor logging
- Sensitive data in logs
- Missing health checks
- Missing monitoring hooks
- Missing audit logs for sensitive actions
- Third-party service failure behavior
- Missing timeout handling
- Background job failure handling
- Partial failure handling

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Inspect app entry points, API boundaries, service clients, background jobs, and third-party integrations.
2. Identify where failures would affect critical user flows.
3. Classify findings as Blocker, High, Medium, or Low.
4. Apply safe in-scope fixes only when remediation is authorized; for an assessment, report them:
   - defensive error handling
   - fallback states
   - improved structured logging
   - health check endpoints if consistent with the stack
   - timeout handling where straightforward
   - safer third-party failure handling
5. Avoid adding new external services unless already used or explicitly requested.
6. Report documentation and risk changes; modify project files only for authorized remediation or requested artifacts.
7. Run validation.

## Severity guidance

Classify as Blocker when failure handling creates data loss, security exposure, broken critical flows, or inability to operate production.

Classify as High when missing observability or reliability creates serious operational risk.

Classify as Medium when improvements are valuable but not release-blocking.

Classify as Low for optional hardening or cleanup.

## Guardrails

- Do not swallow errors silently.
- Do not log sensitive data.
- Do not make failures look successful.
- Do not add noisy logs that obscure real production issues.
- Do not claim monitoring exists unless integrated or documented.
- Do not introduce a new observability vendor without approval.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Reliability findings
- Observability gaps
- Safe fixes applied
- Health check or logging notes
- Remaining monitoring recommendations
- Files changed and reasons