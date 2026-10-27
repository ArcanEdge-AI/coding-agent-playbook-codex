---
name: production-documentation-onboarding
description: Review and improve documentation for production readiness and developer onboarding, including README accuracy, setup instructions, environment variables, testing, build, deployment, architecture overview, troubleshooting, contribution guidance, known risks, release notes, and handoff documentation.
---

# Production Documentation Onboarding

## Core purpose

Make the repository easier to run, test, deploy, maintain, and hand off.

## Use this skill when

- The production pass needs documentation review.
- The user wants the repository understandable for future developers.
- Setup, testing, deployment, architecture, or troubleshooting documentation is missing or stale.

## Do not use this skill when

- The task is only code implementation.
- The user explicitly asks not to change docs.
- Documentation cannot be grounded in repository files.

## Check for

- README accuracy
- Local setup instructions
- Environment variable documentation
- Test instructions
- Build instructions
- Deployment instructions
- Architecture overview
- Troubleshooting notes
- Contribution guidelines
- Known risks and limitations
- Release checklist references
- Manual QA instructions
- Onboarding instructions
- Dependency installation notes
- Database setup notes
- Migration instructions

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Inspect existing documentation.
2. Compare docs against actual repository scripts and configuration.
3. Identify missing or stale instructions.
4. Classify documentation gaps as Blocker, High, Medium, or Low.
5. When documentation changes are requested or part of authorized remediation, update them to reflect real commands and project structure. Assessment-only requests report gaps and proposed text.
6. Do not invent setup steps that are not supported by the repository.
7. Report documentation gaps in the requested format; create or update `DOCUMENTATION_GAPS.md` only when that artifact is in scope.
8. Link to production-readiness files where helpful.

## Severity guidance

Classify as Blocker when missing documentation prevents safe setup, deployment, release, or rollback.

Classify as High when missing documentation creates serious release or onboarding risk.

Classify as Medium when documentation should improve soon but does not block release.

Classify as Low for optional clarity or polish.

## Guardrails

- Do not document guessed commands as facts.
- Do not expose secret values.
- Do not over-document obvious details.
- Do not replace useful existing docs without preserving important content.
- Keep documentation practical and developer-facing.
- Document unknowns honestly.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Documentation readiness summary
- README updates where needed
- Environment variable names and purpose
- Setup, test, build, and deployment notes
- Remaining documentation gaps
- Files changed and reasons