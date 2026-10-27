---
name: production-database-integrity
description: Review database schema, migrations, constraints, indexes, transactions, rollback safety, data integrity, retention, soft deletes, seed data, PII handling, and persistence-layer risks during a production-readiness pass. Use when reducing data loss, migration, consistency, or rollback risk before release.
---

# Production Database Integrity

## Core purpose

Identify data integrity risks and improve schema, migration, and persistence safety without destructive changes.

## Use this skill when

- The production pass needs database or persistence review.
- The repository uses a database, ORM, migrations, persistent storage, or data models.
- The user wants to reduce data loss, migration, consistency, or rollback risk.

## Do not use this skill when

- The application has no persistence layer.
- The task is only frontend polish.
- The user asks for destructive data changes without explicit approval.

## Check for

- Schema consistency
- Unsafe migrations
- Missing constraints
- Missing indexes
- Weak validation
- Race conditions
- Transaction safety
- Backup assumptions
- Rollback risks
- Soft delete behavior
- Data retention concerns
- Personally identifiable information handling
- Seed data safety
- Migration ordering
- Orphaned records
- Inconsistent application-level versus database-level rules
- Unsafe default values
- Missing uniqueness guarantees

## Destructive-change rule

Do not create destructive migrations without explicit approval.

Do not drop columns, tables, indexes, or data unless explicitly approved.

Any migration must include rollback notes.

Treat data loss risk as a Blocker.

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Identify database technology, ORM, schema files, migration files, seed files, and data access layer.
2. Inspect schema and migration history.
3. Review critical write paths for transaction safety.
4. Identify data integrity assumptions that only exist in application code.
5. Classify findings as Blocker, High, Medium, or Low.
6. Recommend constraints, indexes, or migration changes.
7. In authorized remediation, implement only safe non-destructive changes. For an assessment, report proposed changes without modifying source, schema, or data.
8. Add tests for authorized data-integrity behavior changes; report missing coverage during an assessment.
9. Report rollback and deployment implications; update project notes only for authorized changes or requested artifacts.

## Severity guidance

Classify as Blocker when there is data loss risk, unsafe migration risk, or broken persistence for critical flows.

Classify as High when data correctness, rollback, or consistency risks are serious but not immediately destructive.

Classify as Medium when database improvements are important but not release-blocking.

Classify as Low for cleanup or future schema polish.

## Guardrails

- Do not assume production data shape.
- Do not run destructive commands.
- Do not create migrations that cannot be rolled back or explained.
- Do not hide data integrity risks as normal cleanup.
- Prefer explicit constraints over implicit assumptions.
- Do not expose PII in reports or logs.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- Database risk summary
- Migration safety notes
- Safe schema or validation changes
- Rollback considerations
- Remaining data risks
- Files changed and reasons