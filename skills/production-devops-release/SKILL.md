---
name: production-devops-release
description: Review DevOps, CI/CD, deployment, release, rollback, environment configuration, build scripts, validation commands, branch protection assumptions, monitoring readiness, secret management assumptions, health checks, and production/staging separation during a production-readiness pass.
---

# Production DevOps Release

## Core purpose

Verify release mechanics and document deployment, rollback, and environment readiness.

## Use this skill when

- The production pass needs DevOps or release-readiness review.
- The user wants the repository ready to build, deploy, roll back, and operate.
- The repository has deployment config, CI/CD config, Docker files, hosting files, or environment setup.

## Do not use this skill when

- The task is only application code cleanup.
- The user does not want deployment or CI/CD reviewed.

Missing credentials limit live deployment checks, not use of this review skill. Mark those checks unavailable and complete independent static review. Do not deploy or claim live validation without access and authority.

## Check for

- Build commands
- Test commands
- Lint commands
- Typecheck commands
- CI/CD configuration
- Environment variable requirements
- Production and staging separation
- Docker, deployment, or hosting configuration
- Rollback process
- Branch protection assumptions
- Release checklist
- Monitoring and alerting readiness
- Deployment documentation
- Secret management assumptions
- Health check configuration
- Preview environment support
- Migration deployment order

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Identify package manager, build system, and deployment files.
2. Inspect CI/CD workflows.
3. Inspect environment configuration.
4. Identify production-required variables without exposing values.
5. Run available build and validation commands where safe.
6. Classify findings as Blocker, High, Medium, or Low.
7. If requested as project artifacts or required by the authorized remediation, create or update the following; otherwise include their relevant content in the assessment response:
   - `RELEASE_CHECKLIST.md`
   - `DEPLOYMENT_NOTES.md`
8. Document rollback steps or rollback gaps.
9. Record risks in the requested deliverable; update `RISK_REGISTER.md` only when a repository report is in scope.

## Severity guidance

Classify as Blocker when the app cannot be built, deployed, configured, or rolled back safely enough for production.

Classify as High when release mechanics are fragile or likely to cause production incidents.

Classify as Medium when deployment documentation or automation should improve soon.

Classify as Low for optional release polish.

## Guardrails

- Do not deploy unless explicitly asked.
- Do not modify production infrastructure directly.
- Do not expose secret values.
- Do not claim CI/CD works unless validated or clearly documented as unverified.
- Do not add new deployment platforms without approval.
- Do not assume production environment values.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Release readiness summary
- CI/CD risks
- Deployment risks
- Required environment variables by name only
- Rollback notes
- Validation results
- Files changed and reasons