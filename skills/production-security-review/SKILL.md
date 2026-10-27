---
name: production-security-review
description: Perform a production security pass on a codebase, including secrets, authentication, authorization, input validation, injection risks, XSS, CORS, sensitive logging, dependency vulnerabilities, rate limiting, sessions, cookies, webhook validation, and unsafe file handling. Use during production-readiness reviews or security hardening before release.
---

# Production Security Review

## Core purpose

Identify production security risks, fix safe issues only when remediation is authorized, and document remaining risks without exposing sensitive values.

## Use this skill when

- The production pass needs security review.
- The repository handles users, authentication, authorization, private data, files, payments, private APIs, tokens, credentials, or sensitive operations.
- The user wants security hardening before release.

## Do not use this skill when

- The user asks for offensive security, exploit creation, credential theft, or bypass instructions.
- The request is only about code style or documentation.
- The repository is unavailable.

## Check for

- Committed secrets, API keys, tokens, private keys, credentials, or certificates
- Unsafe environment variable handling
- Missing input validation
- Authentication gaps
- Authorization gaps
- Insecure direct object access
- XSS risks
- SQL injection risks
- NoSQL injection risks
- Command injection risks
- Template injection risks
- Path traversal risks
- Unsafe file upload handling
- Weak CORS configuration
- Sensitive data in logs
- Dependency vulnerabilities
- Missing rate limiting
- Missing CSRF protection where applicable
- Weak session, cookie, or token handling
- Webhook signature validation gaps
- Overly permissive admin or service-role access

## Secret-handling rule

Never print actual secret values.

If a secret is discovered, report only:

- File path
- Variable name or key name
- Risk level
- Rotation recommendation

Treat exposed production secrets as Blockers.

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Inspect environment files, config files, auth code, API routes, middleware, logging, upload paths, and dependency manifests.
2. Run available dependency audit commands if configured.
3. Identify security-sensitive user flows.
4. Classify findings as Blocker, High, Medium, or Low.
5. Fix safe in-scope issues where remediation is authorized; assessment-only requests report them without edits:
   - missing validation
   - unsafe logs
   - overly permissive CORS
   - missing authorization checks where straightforward
   - insecure defaults
   - webhook validation gaps
6. Document required secret rotation.
7. When security remediation or test changes are authorized, add or update relevant tests. Assessment-only work reports coverage gaps.
8. Record risks in the requested deliverable; update project readiness/risk files only when those artifacts are in scope.

## Severity guidance

Classify as Blocker when a flaw exposes secrets, bypasses critical auth, permits unauthorized sensitive data access, risks data loss, or enables practical production compromise.

Classify as High when a flaw seriously weakens production security but does not clearly create immediate critical compromise.

Classify as Medium when a security improvement is important but not release-blocking.

Classify as Low for hardening recommendations or defense-in-depth improvements.

## Guardrails

- Do not expose secrets.
- Do not weaken authentication, validation, authorization, or permissions to make tests pass.
- Do not introduce a new auth framework unless explicitly required.
- Do not perform destructive account or data operations.
- Do not claim a security scan is complete if only static review was possible.
- Do not log sensitive request or response payloads.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Security findings by severity
- Safe fixes applied
- Required secret rotations
- Dependency vulnerability summary
- Remaining security risks
- Files changed and reasons