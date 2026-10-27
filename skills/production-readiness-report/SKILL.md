---
name: production-readiness-report
description: Run evidence-driven production-readiness assessments and release validations across repositories, cloud infrastructure, databases, runtime services, authentication, APIs, RBAC, browser journeys, and rollback controls. Use when Codex must prepare or update a client production-readiness report, perform a go-live audit, validate staging and production parity, assess a release gate, execute a narrowly approved production release, or issue a Passed/Failed/Not validated/Blocked pending approval matrix backed by current commands, workflow runs, artifacts, commits, digests, and live observations.
---

# Production Readiness Report

## Objective

Determine current production readiness from primary evidence, preserve approval boundaries, and leave a durable report that another engineer can independently audit. Treat documentation as requirements or historical context, never as proof that live state currently passes.

## Route bundled resources

- Read [references/evidence-lanes.md](references/evidence-lanes.md) completely before a multi-environment audit, database release, or client sign-off.
- Copy [assets/report-template.md](assets/report-template.md) when a durable report does not already exist. Adapt headings only when client conventions require it.
- Run `python scripts/validate_readiness_report.py <report.md>` before issuing the final decision. Use `--allow-placeholders` only while checking the bundled template.

## Apply non-negotiable principles

1. Verify current truth. Re-check mutable facts such as branch heads, workflow conclusions, deployed revisions, cloud identity, infrastructure status, migration ledgers, health responses, and browser behavior.
2. Separate evidence lanes. Do not let a passing UI compensate for a failed database contract, or a passing health endpoint compensate for failed RBAC.
3. Keep environments distinct. Report staging and production separately even when they use identical code.
4. Default to read-only. Treat database writes, deployments, workflow dispatches with side effects, account changes, credential changes, infrastructure changes, and destructive cleanup as unapproved until the user authorizes the exact action and target.
5. Bind approval narrowly. Record the approved environment, resource, database, revision or image digest, migration range, script, backup action, and prohibited actions. Approval for a migration does not authorize an application deployment or snapshot restore.
6. Fail closed. Stop when identity, target, revision, digest, guard variables, backup, prerequisite rehearsal, or expected baseline does not match.
7. Protect secrets. Never print credentials, tokens, connection strings, private keys, secret payloads, or sensitive response bodies. Print only metadata, booleans, counts, allowlisted fields, and sanitized paths.
8. Preserve client work. Run `git status -sb` in every inspected repository or worktree. Do not clean, revert, stage, or overwrite unrelated changes.
9. Avoid false green. Do not call a release ready while any required lane is Failed, Not validated, or Blocked pending approval.
10. Prefer no-op proof. If a suspected defect or cleanup target is already absent, record the verified no-op rather than forcing a mutation.

## Select the operating mode

### Assessment mode

Use this mode by default. Read requirements, gather current evidence, classify every lane, update the report, and stop at mutation boundaries.

### Remediation mode

Use this mode only when the user asks to fix identified defects. Make the smallest scoped change, validate it proportionally, and keep unrelated readiness findings as report items rather than expanding the implementation.

### Approved release mode

Use this mode only after exact approval. Re-run the full preflight immediately before the mutation, execute only the approved release action, then switch back to read-only post-release validation. Do not infer approval for rollback or adjacent deployment work.

## Execute the workflow

### 1. Establish scope and authority

- Identify the client, workspace, repositories, environments, cloud accounts, regions, data stores, and source-of-truth repository.
- Read all user-named plans, contracts, release packets, runbooks, and repository instructions completely before acting.
- State the current authorization boundary and list prohibited mutations.
- Create a short plan with explicit success criteria and validation for each evidence lane.

### 2. Inspect repository state

- Run `git status -sb` separately in each repository or worktree.
- Capture the local branch, HEAD, upstream, divergence, and relevant remote branch head.
- Distinguish client changes from task changes. Preserve unrelated modifications.
- Verify the exact source commit for migrations, release scripts, workflows, and application code.

### 3. Verify identity before external queries

- Verify the active cloud account and principal before cloud metadata or secret reads.
- Verify Git hosting identity and repository access before workflow or pull-request queries.
- Stop if identity does not match the approved client account or principal.
- Query secret values only when required for an authorized login or API validation; keep values in memory and clear them after use.

### 4. Build a baseline

- Capture infrastructure availability, encryption, engine/version, deletion protection, and backup posture.
- Capture deployment revisions and immutable image references.
- Capture runtime guard variables that prevent automatic migrations, schema synchronization, provisioning, or unsafe startup behavior.
- Capture the database ledger and catalog with read-only SQL or a trusted read-only workflow.
- Compare live state to the canonical source, not to an outdated environment.

### 5. Validate independent evidence lanes

Use the detailed criteria in `references/evidence-lanes.md`.

- Repository and release provenance
- Cloud identity and infrastructure metadata
- Database ledger, schema, grants, roles, and catalog parity
- Runtime service health and sanitized failure signals
- Routed frontend, service health, and identity-provider discovery
- Authentication realm or tenant, token claims, and session behavior
- Authenticated APIs, unauthenticated denial, RBAC, and response redaction
- Browser login, shell, routes, loading/success/empty/error states, network ownership, and logout
- Backup, rollback readiness, workflow evidence, and post-release proof

Use primary evidence wherever possible: command output, live metadata, read-only queries, workflow runs, downloaded artifacts, API status matrices, browser observations, and immutable hashes.

### 6. Gate any production mutation

Require all of the following before applying an approved release:

- Exact production resource, region, and database or service target
- Exact source revision and immutable artifact digest
- Exact canonical release script or deployment workflow
- Exact migration or release range
- Successful isolated rehearsal and required lower-environment release
- Healthy known baseline with no unexpected ledger or state entries
- Encrypted backup or snapshot at `available` before the release begins
- Runtime guards confirmed in their safe posture
- Target-bound confirmation that rejects any mismatch
- Explicit exclusions for deployment, credential change, infrastructure change, restore, or cleanup not included in the approval

Build the release workflow to preflight without applying first. Assert the exact already-applied set and exact pending set. Upload sanitized private evidence. Prefer immutable action revisions and concurrency protection.

If any assertion fails, stop. Do not restore, retry with broader scope, edit live credentials, or improvise around the guard.

### 7. Validate after release

- Confirm the release workflow conclusion and exact head revision.
- Download private evidence to a new local path; do not overwrite older evidence.
- Verify ledger rows exactly once and in order, expected checksums, zero unexpected rows, and full catalog convergence.
- Verify the production resource and retained backup remain healthy.
- Re-run sanitized runtime validation.
- Re-run authenticated API, denial, RBAC, and redaction checks.
- Re-run the real browser acceptance path when the release can affect user-visible behavior.
- Do not execute business mutations merely to prove a control exists. Validate enablement and gating without submitting unless the user expressly authorizes the mutation.

### 8. Produce the decision report

Lead with the decision and scope. Include:

- Date, environments, source of truth, method, and authorization boundary
- Explicit Passed, Failed, Not validated, and Blocked pending approval lists
- Environment-by-environment matrix
- Exact evidence: commands, URLs, workflow and PR links, revisions, digests, artifact paths, hashes, counts, and observations
- Freshness and whether evidence is pre-release or post-release
- Repository states and preserved unrelated changes
- Safety statement describing what did and did not mutate
- Smallest next remediation for every non-pass

Do not bury a failed or blocked production lane beneath an overall-green sentence. Mark the decision Passed only when every required in-scope lane passes with current evidence.

## Apply status semantics consistently

- **Passed**: Current primary evidence satisfies the stated contract.
- **Failed**: Current evidence proves the contract is not met.
- **Not validated**: Required current evidence was not obtained or is too stale to support a decision.
- **Blocked pending approval**: Completion requires a specific mutation or access expansion that has not been approved.
- **N/A**: The lane does not apply; explain why. Never use N/A to hide missing evidence.

A lane may be both Failed and Blocked pending approval when current state is known to be noncompliant and remediation requires unapproved action.

## Handle failures precisely

- Report the smallest remediation that directly closes the failed lane.
- Identify the exact approval, credential, artifact, target, or external change needed for a blocked lane.
- Preserve operational-but-noncompliant distinctions. A service may be healthy while canonical parity fails.
- Treat safe workflow failures as evidence only when the failure is the designed fail-closed outcome, such as an already-absent cleanup target.
- Keep tool or runner deprecation warnings separate from readiness failures unless they affect execution or violate the release contract.

## Validate the deliverable

Run:

```text
python scripts/validate_readiness_report.py <absolute-report-path>
```

Resolve all validator errors. Review warnings manually because some clients may not use Git commits, container digests, or browser evidence. Finish with a concise user-facing summary and link the durable report.
