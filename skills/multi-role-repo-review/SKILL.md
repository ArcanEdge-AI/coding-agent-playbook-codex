---
name: multi-role-repo-review
description: Coordinate evidence-based multi-role software repository reviews. Use when the user asks Codex to inspect a repo/codebase/project through multiple professional perspectives, run a structured team discussion, simulate or spawn specialized review agents, assess release readiness, or produce a prioritized cross-functional action plan covering product, project management, architecture, frontend, backend, UX/UI, QA, DevOps, security, and stakeholder concerns.
---

# Multi Role Repo Review

## Overview

Use this skill to run a practical cross-functional repository review grounded only in files, commands, and documentation available in the target repo.

## Core Rules

- Inspect the repository before producing conclusions.
- Use only repository evidence: files, folders, docs, manifests, configs, source, tests, CI/CD files, TODOs, comments, generated artifacts, and command output.
- Do not invent features, users, infrastructure, requirements, business goals, or release criteria.
- If something cannot be determined from repository evidence, say so explicitly.
- Prefer specific file references over generic claims.
- Keep findings concise, practical, and prioritized.
- Treat the roles as review lenses used directly by the main agent. Keep its model, authority, and ownership unchanged. Use bounded helpers only under the governing delegation policy and the `subagent-orchestration` skill; helper availability alone is not a reason to launch them. Self-review is not independent verification.

## Inspection Workflow

1. Identify the repo root and current branch/status when git metadata is present.
2. Map the top-level structure with a shallow directory listing.
3. Read the README and visible documentation first.
4. Inspect package/dependency manifests, lockfiles, runtime version files, and build/test scripts.
5. Inspect configuration files, environment examples, lint/typecheck/test setup, and framework config.
6. Inspect source code entry points, routing, core services, data models, API boundaries, UI components, and shared utilities.
7. Inspect tests, fixtures, mocks, coverage config, and missing coverage around critical paths.
8. Inspect CI/CD, deployment, container, cloud, and infrastructure files when present.
9. Search for `TODO`, `FIXME`, `HACK`, `XXX`, `BUG`, `SECURITY`, `deprecated`, and known limitation language.
10. Run lightweight commands only when useful and safe, such as listing package scripts or running focused checks. Do not claim checks passed unless actually run.

## Role Lenses

Use these roles in the structured review:

- Product Manager: user value, apparent product scope, unclear requirements, feature completeness, prioritization.
- Project Manager / Scrum Master: delivery sequencing, planning gaps, dependencies, readiness, process risks.
- Tech Lead / Software Architect: architecture, boundaries, data flow, dependency choices, maintainability, engineering risk.
- Frontend Developer: UI implementation, client state, routing, accessibility hooks, component quality, browser-facing fragility.
- Backend Developer: APIs, persistence, validation, domain logic, integrations, error handling, server-side fragility.
- UX/UI Designer: interaction clarity, information architecture, visual consistency, accessibility, usability gaps.
- QA / Test Engineer: test strategy, missing coverage, fragile scenarios, reproducibility, release confidence.
- DevOps / Cloud Engineer: build/deploy path, runtime configuration, observability, environments, CI/CD, operational risk.
- Security Engineer: auth, authorization, secrets, dependency exposure, input validation, data handling, secure defaults.
- Stakeholder / Client Representative: business impact, adoption concerns, trust, operational fit, unresolved stakeholder questions.

For each role, identify:

- What the project appears to do.
- Key strengths.
- Risks and gaps.
- Possible bugs or fragile areas.
- Missing or weak tests.
- Unclear requirements.
- Technical debt.
- Concrete improvement suggestions.
- Questions for other roles when an issue crosses responsibilities.

## Discussion Sequence

Organize the review as a structured team discussion:

1. Each role gives a short initial assessment.
2. Roles discuss disagreements, tradeoffs, blockers, dependencies, and cross-functional questions.
3. The Tech Lead summarizes architecture and main engineering risks.
4. The Product Manager summarizes user value, business value, and priority concerns.
5. QA, Security, and DevOps identify potential release blockers.
6. The full team produces a prioritized action plan.

## Final Output

Produce these sections exactly:

### 1. Project Summary

Briefly describe what the project appears to be, based only on repository evidence.

### 2. Role-by-Role Findings

Provide findings for each role, including strengths, concerns, and recommendations.

### 3. Cross-Functional Discussion

Summarize key disagreements, tradeoffs, dependencies, and decisions discussed by the roles.

### 4. Technical Architecture Summary

Have the Tech Lead describe the apparent architecture, major components, data flow, dependencies, and architectural risks.

### 5. Key Risks

List the most important product, technical, operational, security, testing, and delivery risks.

### 6. Release Blockers

Have QA, Security, and DevOps clearly identify any blockers that should prevent release. If release readiness cannot be determined from the repo, say so.

### 7. Open Questions

List questions that need clarification before confident planning or release.

### 8. Recommended Next Steps

Provide practical next steps grounded in repository contents.

### 9. Prioritized Backlog

Create a backlog table with these columns:

| Priority | Task | Rationale | Suggested Owner | Dependencies | Evidence from Repository |
| --- | --- | --- | --- | --- | --- |

Use `High`, `Medium`, or `Low` priority. Keep evidence entries specific enough to trace back to actual repository files or observed command output.
