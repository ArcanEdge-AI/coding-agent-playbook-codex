# [Client] production readiness report

Date: [YYYY-MM-DD]
Scope: [Environments, systems, and release]
Source of truth: [Repository, branch, contract, or release manifest]
Method: [Live evidence, workflows, artifacts, APIs, browser]
Authorization boundary: [Read-only default and exact approved mutations]
Decision: **[PASSED | FAILED | NOT READY] — [concise reason]**

[One-paragraph executive summary that distinguishes operational health from contract compliance.]

## Status definitions and disposition

- **Passed**: Current primary evidence satisfies the stated contract.
- **Failed**: Current evidence proves the contract is not met.
- **Not validated**: Required current evidence was not obtained.
- **Blocked pending approval**: Completion requires a specific unapproved mutation or access expansion.

Current disposition:

- **Passed**: [List or none.]
- **Failed**: [List or none.]
- **Not validated**: [List or none.]
- **Blocked pending approval**: [List or none.]

## Environment result matrix

| Validation area | [Staging] | [Production] | Exact supporting evidence |
| --- | --- | --- | --- |
| Requirements and release provenance | [Status] | [Status] | [Commit, digest, contract] |
| Cloud identity and infrastructure | [Status] | [Status] | [Account, resource, region, metadata] |
| Database ledger and catalog parity | [Status] | [Status] | [Run/query, counts, unexpected rows] |
| Backup and rollback readiness | [Status] | [Status] | [Snapshot/backup metadata] |
| Runtime guards and stability | [Status] | [Status] | [Run, window, counts] |
| Routing and health | [Status] | [Status] | [URL/status matrix] |
| Authentication and token claims | [Status] | [Status] | [Realm/tenant and allowlisted claims] |
| Authenticated API sweep | [Status] | [Status] | [Passed/total and failures] |
| Unauthenticated and RBAC denial | [Status] | [Status] | [401/403 evidence] |
| Response redaction | [Status] | [Status] | [Allowlisted fields and sensitive scan] |
| Browser login, routes, and logout | [Status] | [Status] | [URLs, route totals, state observations] |
| Browser network ownership | [Status] | [Status] | [Service prefixes, statuses, DB signal count] |
| Final readiness sign-off | [Status] | [Status] | [Reason] |

## Repository and release provenance evidence

- Canonical repository: [URL/path]
- Release commit: `[full SHA]`
- Build/workflow: [URL]
- Immutable artifact: `[digest or equivalent]`
- Release script/workflow: `[path or workflow ID]`
- Rehearsal/lower-environment prerequisites: [URLs and conclusions]

## Cloud and infrastructure evidence

| Resource | Environment | Region | Status | Encryption/protection | Evidence command |
| --- | --- | --- | --- | --- | --- |
| [Resource] | [Environment] | [Region] | [Status] | [State] | `[command]` |

Verified identity:

- Account/project: `[identifier]`
- Principal: `[allowlisted identifier]`
- Verification time: `[timestamp]`

## Database evidence

- Baseline: [Expected and observed state]
- Change delta: [Exact migration range or N/A]
- Post-release ledger: [Counts, order, checksums, unexpected rows]
- Catalog: [Pass count, fail count]
- Ownership/grants/roles: [Summary]
- Read-only enforcement: [Method]

## Runtime evidence

- Required services: [List or count]
- Observation window: [Time range]
- Safe-mode guards: [Variables and expected values]
- Migration/schema-sync attempts: [Count]
- Authentication failures: [Count]
- Permission failures: [Count]
- Missing relations: [Count]
- Connection failures: [Count]

## API, RBAC, and redaction evidence

| Service | Endpoint group | Passed/total | Expected denial | Redaction result |
| --- | --- | ---: | --- | --- |
| [Service] | [Group] | [N/N] | [401/403] | [Pass/fail and fields] |

Token claims reported only as allowlisted facts:

- Issuer/realm correct: [true/false]
- Required role present: [true/false]
- Prohibited elevated role absent: [true/false]
- Expected token lifetime: [seconds or N/A]

## Browser acceptance evidence

- Browser mechanism: [Requested bridge/profile/tool]
- Login URL issuer/realm: [Sanitized URL]
- Landing URL: [URL]
- Required shell: [Observed labels]
- Routes passed: [N/N]
- Loading states cleared: [Result]
- Valid empty states: [Routes and observations]
- Visible errors/alerts: [Count and sanitized summary]
- API responses observed: [Count/status summary]
- Service prefixes: [List]
- Database-protocol/host signals: [Count]
- Logout result: [Final URL and public/protected controls]

### Route matrix

| Route | [Staging] | [Production] | Observation |
| --- | --- | --- | --- |
| `[route]` | [Status] | [Status] | [Heading/state; no mutation invoked] |

## Release and rollback evidence

- Approval: [Exact approved target and action]
- Explicit exclusions: [Restore, deployment, credentials, infrastructure, cleanup]
- Backup: [ID, source, encryption, status, creation time]
- Release run: [URL, conclusion, revision]
- Applied delta: [Exact files/versions]
- Post-release proof: [Catalog/runtime/API/browser summary]
- Restore performed: [No, unless separately authorized]

## Commands and artifacts

```text
[Exact sanitized commands]
```

| Artifact | Local path or URL | SHA-256 or immutable ID |
| --- | --- | --- |
| [Artifact] | [Path/URL] | `[hash/ID]` |

## Repository evidence

| Repository/worktree | Branch | HEAD/upstream | Status and preserved changes |
| --- | --- | --- | --- |
| [Path] | [Branch] | [SHAs] | [Clean or exact unrelated changes] |

## Safety result

[State exactly which mutations occurred, why they were authorized, and which prohibited actions did not occur. Confirm that secrets were not printed.]

## Smallest next remediation

[For each Failed, Not validated, or Blocked lane, state the smallest concrete action, required approval or access, and validation that would close it. Write "No remediation remains in scope" only when every required lane passes.]
