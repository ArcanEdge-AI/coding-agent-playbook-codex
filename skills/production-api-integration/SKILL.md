---
name: production-api-integration
description: Review API and integration readiness for production, including request validation, response consistency, status codes, auth, authorization, pagination, rate limiting, idempotency, webhooks, third-party failures, timeout handling, retry behavior, sensitive data exposure, and API documentation.
---

# Production API Integration

## Core purpose

Improve API predictability, integration safety, and failure handling without unnecessary breaking changes.

## Use this skill when

- The production pass needs API or integration review.
- The repository exposes APIs, consumes APIs, uses webhooks, or depends on third-party services.
- The user wants APIs production-ready and predictable.

## Do not use this skill when

- The application has no API or integration layer.
- The task is only frontend styling.
- The requested change would break public API behavior without approval.

## Check for

- Request validation
- Response shape consistency
- Correct HTTP status codes
- Error response consistency
- Pagination
- Rate limiting
- Authentication
- Authorization
- Idempotency for sensitive operations
- Timeout handling
- Third-party failure handling
- Webhook signature validation
- API documentation gaps
- Breaking change risks
- Retry behavior
- Sensitive data exposure
- Internal error leakage
- Contract drift between client and server

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Inspect route definitions, controllers, service clients, middleware, schemas, and API docs.
2. Identify critical API flows.
3. Identify external integrations and webhooks.
4. Classify findings as Blocker, High, Medium, or Low.
5. In an authorized remediation task, fix safe in-scope issues; for assessment-only requests, report them without editing:
   - missing validation
   - inconsistent errors
   - missing status handling
   - timeout gaps
   - obvious auth checks
   - webhook validation gaps
6. Add relevant tests when making authorized API behavior changes; in assessment mode, report coverage gaps.
7. Document breaking-change risks separately.
8. Update API docs for authorized API changes; in assessment mode, report documentation gaps.

## Severity guidance

Classify as Blocker when API behavior creates critical security, data loss, payment, auth, or production availability risk.

Classify as High when API flaws create serious release risk or likely production incidents.

Classify as Medium when improvements should be scheduled soon.

Classify as Low for optional consistency or documentation polish.

## Guardrails

- Do not break API contracts without explicit approval.
- Do not remove auth or validation to make tests pass.
- Do not leak internal errors to clients.
- Do not retry non-idempotent operations without safeguards.
- Do not log secrets or sensitive payloads.
- Do not hide integration failures as successful responses.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- API readiness summary
- Integration risk summary
- Safe fixes applied
- Tests added or updated
- Remaining API risks
- Files changed and reasons