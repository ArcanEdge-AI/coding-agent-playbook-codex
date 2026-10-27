# Production readiness evidence lanes

Use this reference to define success criteria before gathering evidence. Omit a lane only when it is genuinely out of scope and record the reason as N/A.

## Contents

1. Evidence quality and freshness
2. Core evidence lanes
3. Production mutation gate
4. Browser acceptance pattern
5. Evidence packet checklist
6. Common false-green traps

## 1. Evidence quality and freshness

Rank evidence in this order:

1. Live primary evidence: cloud metadata, read-only SQL, API responses, browser observations, current workflow runs.
2. Immutable release evidence: merged commits, image digests, signed artifacts, downloaded run artifacts, hashes.
3. Current source evidence: code, tests, workflows, migrations, configuration contracts.
4. Historical evidence: prior reports, screenshots, earlier workflow runs, handoff notes.

Use historical evidence to select checks, not to claim current pass status. Re-check any fact that can drift cheaply. Label expensive or inaccessible evidence as Not validated rather than guessing.

## 2. Core evidence lanes

| Lane | Questions to answer | Strong evidence | Passing condition |
| --- | --- | --- | --- |
| Requirements | What contract defines ready? What is explicitly prohibited? | Plans, API contracts, release packet, runbook, user approval | Required references read completely; scope and approval boundary stated |
| Repository state | What code and local changes exist now? | `git status -sb`, HEAD/upstream/remote SHA, diff names | Exact revision known; unrelated work preserved; release source identifiable |
| Identity | Which account and principal are active? | Cloud identity command, Git hosting identity | Identity matches the intended client and account before queries or mutations |
| Infrastructure | Are resources available, encrypted, protected, and correctly located? | Provider metadata, resource IDs, region, engine/version, backup status | Required resources healthy; protection and encryption match contract |
| Release provenance | Is the artifact immutable and tied to canonical source? | Merge commit, build run, image digest, labels/attestations | Source revision and artifact digest match the approved release |
| Database ledger | What ran, how often, and in what order? | Read-only ledger query or trusted catalog workflow | Expected rows exactly once and ordered; checksums match; no unexpected rows |
| Database catalog | Do schemas, objects, constraints, indexes, grants, and roles converge? | Read-only catalog with explicit pass/fail counts | Every required check passes and zero checks fail |
| Runtime guards | Can services mutate schema or provision accounts at startup? | Environment metadata and sanitized runtime inspection | Safe mode enabled; automatic migration/sync/provisioning disabled as required |
| Runtime stability | Are required services running without database or permission faults? | Sanitized bounded log counts, container/task status | Required services running; zero relevant failure signals in the stated window |
| Routing and health | Are public and internal routes reachable? | HTTP status matrix, identity-provider discovery | Every required route returns the expected status and content type |
| Authentication | Is login issued by the correct realm/tenant and client? | Real login URL, issuer claim, client/audience, session result | Correct issuer; required role present; prohibited elevated roles absent |
| Authenticated APIs | Do all read-only owner endpoints work? | Exact endpoint/status matrix | Every required request returns the expected status and response shape |
| Denial and RBAC | Are anonymous and non-admin roles rejected? | 401/403 response matrix, focused middleware tests | Anonymous is 401; disallowed roles are 403; admin is allowed |
| Redaction | Do responses avoid secrets and unnecessary PII? | Allowlisted field names, sensitive-field scan, bounded samples | Only approved fields are present; no secret, credential, or private-state fields |
| Browser routes | Does the real user journey work? | Existing-profile browser login, exact paths, headings, shell, state checks | Login lands correctly; all required routes hydrate; no retained loader/error |
| Browser network | Does the frontend call service-owned APIs only? | Sanitized network origin/path/status summary | Expected service prefixes; successful responses; zero database protocol/host signals |
| Logout | Does the session end and protected shell disappear? | Final URL and visible control/state assertions | Public root restored; login visible; protected shell absent |
| Backup/rollback | Is a usable pre-release recovery point retained? | Snapshot/backup ID, encryption, source, `available` status | Backup complete before release; restore procedure known but not executed without approval |
| Post-release | Does live state remain healthy after mutation? | Fresh catalog, runtime, API, browser, and resource metadata | Every affected lane revalidated after release |

## 3. Production mutation gate

Record a target-bound release manifest before mutation:

| Field | Required value |
| --- | --- |
| Client/account | Exact account and verified principal |
| Environment | Exact production environment name |
| Resource | Exact instance, cluster, service, or project ID |
| Region/location | Exact provider region or location |
| Database/service | Exact logical target |
| Source revision | Full commit SHA |
| Artifact | Immutable digest or equivalent |
| Release path | Exact script or workflow |
| Change range | Exact migrations or release delta |
| Prerequisites | Rehearsal and lower-environment run IDs |
| Backup | Exact encrypted snapshot/backup ID |
| Confirmation | Exact target-bound confirmation string |
| Explicit exclusions | Restore, app deploy, credentials, accounts, unrelated infrastructure, cleanup |

Before applying, prove the known baseline and exact pending delta. After applying, prove the expected final state. Never use a broad `latest` tag, mutable branch-only reference, or generic confirmation for a production mutation.

## 4. Browser acceptance pattern

Use the browser mechanism requested by the user. When the task depends on an installed extension or existing profile, do not silently switch to standalone automation.

Capture only sanitized facts:

- Authentication issuer or realm URL without codes or tokens
- Landing URL and exact protected pathname
- Required shell labels and controls
- Route, heading, loading, empty, error, and alert state
- Network origin, pathname, method, status, and service prefix without headers or query secrets
- Logout URL and disappearance of protected controls

Do not print browser storage, authorization headers, JWTs, credentials, response bodies containing PII, or raw network event objects. Decode tokens in memory and output only allowlisted claims or booleans.

For action routes, prove that controls render and gates behave. Do not submit approvals, exports, publishes, payments, messages, or destructive actions unless the user specifically authorizes that business mutation.

## 5. Evidence packet checklist

Retain or link:

- Requirements and release contract paths
- Repository path, branch, HEAD, upstream, and status
- Cloud identity and resource metadata commands
- Baseline and post-release ledger/catalog artifacts
- Workflow and job URLs with conclusions and head SHAs
- Pull request and merge commit URLs
- Immutable artifact digests and source labels
- Snapshot/backup metadata
- Sanitized runtime scan and time window
- API endpoint/status matrix and token-claim booleans
- RBAC and redaction summary
- Browser route and network summary
- Local artifact paths and SHA-256 hashes
- Exact commands used, with secret values omitted
- Safety statement and smallest next remediation

Store evidence in a new timestamped or run-ID path. Do not overwrite prior evidence because pre-release and post-release artifacts serve different purposes.

## 6. Common false-green traps

- Treating a healthy service as proof of canonical database parity
- Treating a successful build as proof of deployment
- Treating documentation or old screenshots as live validation
- Checking only an aggregate health endpoint while owner APIs fail
- Checking admin success without testing anonymous or non-admin denial
- Reporting a token role without verifying issuer or prohibited roles
- Sampling a SPA before hydration and recording transient loading as failure or success
- Printing raw network events or response bodies to prove ownership
- Creating a snapshot but applying before it becomes available
- Running a canonical script without proving the exact pending delta
- Reusing a mutable image tag instead of a digest
- Calling an intentionally fail-closed no-op workflow a product failure
- Declaring all green while Required, Failed, Not validated, or Blocked lanes remain
