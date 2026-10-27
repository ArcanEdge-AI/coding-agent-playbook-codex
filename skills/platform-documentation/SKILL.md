---
name: platform-documentation
description: "Map platforms from current implementation and generate, correct, or refresh documentation and SOPs for users, admins, operators, and developers. Capture work and decisions from primary records. Existing docs are comparison targets, never evidence for platform findings."
---

# Platform Documentation

Produce accurate documentation people can use to complete their tasks. The current implementation is the source of truth for platform behavior. Discover the requested scope, explain its consequential workflows and contracts, and expose evidence limits. A coverage ledger supports the documents; it is not the deliverable or proof of an omission-free platform.

## Keep discovery independent

Discover from executable code, rendered UI definitions, schemas/policies, machine-consumed configuration, build/deployment definitions and authorized runtime observations. Comments locate code but do not prove execution. Tests establish assertions or bounded observations, not universal behavior. Follow governing instructions without treating their product assertions as implementation evidence.

Do not use existing README files, guides, plans, requirements/design documents, runbooks, generated maps or prior results to discover, substantiate or fill gaps in platform findings. Inventory their paths without reading their contents. Preserve a source-derived baseline before opening documents as correction/comparison targets. In a blind test, also exclude earlier findings, expected answers, conversation summaries and contaminated indexes. Application-consumed prose is data only when its actual consumer proves that role.

After independent discovery, existing documents may be compared with code. Unsupported documentary assertions remain unverified; they do not prove a missing feature. Keep suspected defects, proposed behavior and recorded intent separate from actual implementation. Disclose contamination and use a fresh source-only reviewer when independence is required.

## Scope and select the work

| Mode | Result |
| --- | --- |
| Capture work | What changed, why, verification, decisions and unresolved work from supplied primary records |
| Map platform | Actors, capabilities, journeys, workflows, rules, relationships, boundaries and gaps |
| Generate | Appropriate task guides, SOPs and shared references for requested audiences |
| Correct | Code-grounded repairs to existing documents and affected links |
| Refresh | Changed behavior propagated through affected documentation |

Recover the requested repository/snapshot, audience, destination, scope, existing user changes and authorization. Ask only for material missing information. A one-guide correction needs its affected flow, not an unrelated platform audit. A whole-platform request needs breadth across the source-available platform, not a polished representative subset.

Use [references/discovery.md](references/discovery.md) for mapping/generation, [references/authoring.md](references/authoring.md) for writing or correcting reader instructions, and [references/evidence-maintenance.md](references/evidence-maintenance.md) for evidence and proportionate verification. Load only the applicable references. Broad source-first generation normally needs all three once; reuse them rather than reloading them at each checkpoint.

## Discover the behavior before writing

1. Enumerate actual entry points and consequential interfaces: routes and nested controls, handlers and automatic callbacks, APIs/commands, persisted schemas/policies, jobs and delivery definitions. Reconcile each in-scope entry to a meaningful task/operation/variant or justified exclusion in one coverage record.
2. Establish breadth before polishing examples. Follow each task through eligibility, state/defaults, validation, reads/writes, downstream effects, return/caller handling and completion/readback. Include consequential alternate, denied, interrupted, asynchronous and recovery paths. Source-available unfinished tasks remain unfinished.
3. Give shared facts a producer, consumer and stage where those distinctions affect meaning. Compare actual consumers before sharing a rule. A UI gate is not database authorization; a grouping key is not an assigned output field; a title fallback is not a detail-body fallback.
4. Before closing a boundary, inspect sibling fields and actual expressions. Check type/cast versus value/parse failures, absent/null/default branches and enclosing catch scope. For calculated or assembled outputs, inspect each consequential assigned field, ordinary and fallback branches, earlier guards and minimum input shape. Use the discovery reference's focused boundary checks.
5. Keep independently consequential outcomes distinguishable in compact branch/field tables or clear clauses. One paragraph can cover several outcomes if each is actually stated and checked. Do not create a claim ID, duplicated quote and separate review file for every scalar or clause. Internal plumbing needs a separate documentation obligation only when it changes a reader's action, interface contract, result, safety or diagnosis.

Keep one current source/coverage record linking workflows, relevant branches, evidence and reader locations. Preserve a stable source baseline for independence/resumption; later discoveries and corrections update the current record with concise provenance. Detailed bookkeeping is optional when a real acceptance requirement needs it, not the default workflow.

## Write and preserve meaning

Choose deliverables from reader tasks and platform roles. Distinguish application admins from infrastructure operators. Share authoritative technical facts through linked references rather than repeating them across handbooks. Include diagrams, examples and commands when they explain the actual implementation; never invent controls, endpoints, roles, supported operations or historical rationale.

Write usable prerequisites, actions, decisions, expected results, partial effects, failure/recovery and completion checks. Keep developer contract precision in an accessible shared reference. A ledger entry or source citation cannot replace missing reader instructions. Qualify observed runtime/deployment outcomes separately from source-supported behavior.

When correcting or summarizing, retain every correct existing condition, effect and limit. Check the whole changed passage and neighboring assertions against code; adding a correct qualification elsewhere does not neutralize an overbroad promise. Follow changed facts into their actual audience views and consumers. Preserve unrelated content and stable links.

## Verify with bounded effort

Use the evidence reference's compact verification loop: source-led closure, reader-task and consequential reverse checks, one consolidated findings pass, a repair batch, then focused rechecks of changed meanings and affected flows. Broad high-assurance work warrants a source-first independent reviewer when available; self-review must not be labeled independent. Give a blind reviewer source and scope before candidate prose, with no prior answers.

Review every discovered consequential outcome, but retain evidence at the useful workflow/boundary level. Write detailed near-miss or exact-quote proof where meaning is ambiguous or disputed, not as a universal form for every fact. Reuse valid source and whole-passage/context checks. Rerun only evidence invalidated by changed inputs, shared dependencies, readers or unresolved failures; a broad shared change can require broad rechecking.

Run applicable mechanical checks for current source citations, links, commands/examples and coverage accounting. Existing helpers are optional tools for these mechanics, not reasons to manufacture JSON claim ledgers. Green excerpts, hashes and schema checks do not establish semantic accuracy. Keep one concise verification summary; avoid recursive historical audits, copied manifests and a new freeze/review stage for each small edit.

Before substantial work, choose a finite review scope and effort/iteration allowance suited to the platform and user's constraints. Default to one independent review, one consolidated repair batch and an affected-flow recheck. If a new material family or repeated error requires more work, record what failed and how the next pass changes; preserve valid work and do not repeat an unchanged review chain. This bound does not authorize skipping known gaps or silently reducing scope. Respect host permissions and resource rules.

Finish when requested reader tasks and all discovered consequential source-available obligations have usable treatment, no known material contradiction/omission remains, affected checks pass and real external unknowns are explicit. Report initial-draft failures separately from repaired results. Do not convert the number of green gates, files or claims into a documentation completeness percentage. A requested percentage needs an explicit meaningful denominator and exclusions. No unrestricted 100% guarantee.

## Authority and delivery

Documentation work does not authorize app fixes, deployments, live data changes, messages or publication. Reading a procedure does not authorize executing it. Verify at the requested destination and distinguish static walkthroughs, executed flows and unverified external outcomes. Capture resumable unfinished work with its exact next frontier.

Describe credential names, purposes and access procedures without copying values or unnecessary personal data. Keep project secrets, private paths, incident histories and evaluation-specific answers out of this reusable skill.
