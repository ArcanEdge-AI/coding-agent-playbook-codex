# Data Model Reference

## Entities

List major entities and ownership.

## Persistence

Document where data is stored and how it is accessed.

## Schema Changes

Document migration rules.

## Compatibility and Retirement

Identify supported readers and writers, stored formats that still matter, and explicit retention requirements. Define the authoritative path and any bounded migration; do not retain duplicate writers solely because development data exists.

## Data Retention and Migration

Record which data and useful configuration must be preserved or migrated. Specify the exact scope, consequences, recovery options, and approval required before resets or deletion. Keep data disposition separate from retiring obsolete runtime code.

## Data Integrity

Document invariants and constraints.

## Sensitive Data

Note fields requiring privacy or safety care.

## Tests and Validation

List checks that protect data behavior.
