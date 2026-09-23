---
name: legacy-path-retirement
description: Use when deciding whether to retain, migrate, or remove superseded code, duplicate writers, compatibility fallbacks, or old contracts during an authorized change. Trace current dependencies and retention requirements; separate code retirement from data disposal and correctness safeguards.
---

# Legacy Path Retirement

Prefer one clean, authoritative implementation within the affected scope. Preserve or add a compatibility path only for a demonstrated current dependency or an explicit retention requirement, not hypothetical users or the mere existence of old code or data.

This skill supports both analysis and authorized implementation. An audit or diagnosis remains read-only. It does not authorize unrelated cleanup, breaking a required contract, destructive data changes, publication, or deployment.

## Establish Scope and Current Requirements

Identify the requested change, candidate obsolete paths, intended authoritative replacement, repository support commitments, product stage, and authorized actions. Do not infer pre-production status or disposable data from a development environment.

Pre-production usually makes a direct consolidation practical when there are no supported older consumers. It does not eliminate current integrations, useful configuration, release constraints, or correctness requirements. Production may require a bounded migration; that is an evidence-based dependency, not an excuse to keep every legacy path.

## Separate the Decisions

| Concern | Decision |
| --- | --- |
| Superseded code, duplicate writers, outdated forms or contracts, compatibility fallbacks | Retain, migrate, or remove based on current dependency evidence and explicit requirements |
| Current development data and useful configuration | Preserve or migrate deliberately; reset or delete only with authority for the exact data and consequences |
| Correctness safeguards | Preserve their guarantees even when the implementation changes; they are not compatibility debt |

Safeguards include stable identifiers and references, authorization, input and upload validation, persistence integrity, retry/idempotency behavior where required, and orphan cleanup. Do not keep an obsolete implementation merely because it currently houses a necessary guarantee; carry that guarantee into the authoritative path and test it.

## Trace Dependencies Before Choosing

Start with the candidate path and inspect relevant evidence:

- callers, imports, routes, entry points, configuration, feature flags, dynamic dispatch, and scheduled jobs
- readers and writers, schemas, migrations, stored formats, fixtures, and generated contracts
- supported clients, external integrations, deployed versions, active work, and release or rollback requirements when relevant
- repository guidance and explicit user retention requirements

Expand only where evidence or material risk requires it. A symbol search is a starting point, not proof of non-use. Missing telemetry or inaccessible consumers leave uncertainty; they do not establish that a path is obsolete. Old tests and documentation may describe superseded behavior, so establish whether that behavior is still required.

For each candidate, record the bounded dependency conclusion and its evidence: demonstrated dependency, explicit retention requirement, no current dependency found after relevant checks, or unresolved dependency. Do not turn a lack of information into either permanent compatibility or permission to delete.

## Choose Retain, Migrate, or Remove

- **Retain:** a supported consumer or explicit requirement still needs the old behavior. Keep the smallest necessary boundary. For a transitional adapter, record its dependent consumer, rationale, and observable removal condition in the existing task record or maintained docs.
- **Migrate:** current consumers or useful data can move to the authoritative implementation within scope and authority. Validate that handoff before retiring the old path.
- **Remove:** relevant checks establish that the superseded path has no required current dependency, and removal is part of the authorized change. Remove its obsolete call sites, wiring, and tests without cleaning unrelated systems.
- **Defer the affected decision:** material dependency evidence or destructive-action authority is missing. State the exact gap and minimum next check or approval; continue independent authorized work.

Question whether a proposed compatibility check or fallback is needed before hardening it. Do not add more guards around a path that should instead be retired.

## Keep Data Disposition Independent

Existing development records do not justify permanent dual writers or compatibility layers. Decide whether they contain useful data or configuration and choose a deliberate preservation or migration strategy.

A request to simplify code is not permission to reset a database, drop stored files, remove user configuration, or discard unmapped records. Before destructive data work, resolve exact targets, dependencies, consequences, recovery options, and authority. Follow repository migration policy; do not erase historical migrations or durable contract history simply because runtime code is obsolete.

If useful data depends on the old path, migrate it or report the dependency rather than deleting the path prematurely. If data value or reset authority is unresolved, preserve it and describe the blocker without inventing a permanent fallback.

## Implement and Verify Within Scope

When implementation is authorized:

- move required callers and guarantees to the authoritative path
- remove only confirmed obsolete code and machinery made unused by that change
- update affected contracts, fixtures, tests, and current documentation to the accepted behavior
- verify actual call paths and persistence or reload behavior where applicable, not only compilation
- test meaningful failures and safeguards, including authorization, invalid input, reference integrity, and cleanup when affected
- check that duplicate writes, competing sources of truth, and retired-path wiring are gone from the affected surface

Retain required regression tests. Replace tests that only enforce obsolete behavior with tests for the accepted contract; do not change an authoritative acceptance requirement merely to obtain a pass.

## Completion Record

Use the existing plan or final report, not a new tracking system. Capture:

- the authoritative implementation and affected scope
- each material retain/migrate/remove decision with dependency evidence
- useful data or configuration retained, migrated, or explicitly approved for reset
- correctness guarantees preserved and checks actually run
- any retained transitional compatibility and its removal condition
- unresolved consumers, evidence gaps, approval gates, or behavior not verified
