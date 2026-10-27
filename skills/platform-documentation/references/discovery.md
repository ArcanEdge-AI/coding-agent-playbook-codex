# Discovery and relationship coverage

Use the portions relevant to the agreed scope. For a platform inventory, account for each area as inspected, pending, inaccessible, out of scope, or not applicable with a reason. A category marked not applicable requires supporting context; an unread repository is pending, not absent.

Apply the skill's source-only boundary before this inventory. Discover from executable implementation and machine-consumed contracts/configuration. Inventory prose-document paths without opening them; freeze source findings before any optional documentation comparison. A file under docs/ is implementation input only when actual code consumes it as configuration/contract; prove that consumer rather than treating its location or format as authority. Comments or identifiers can locate code but do not independently establish that behavior executes.

## Coverage map

| Area | Investigate where applicable |
| --- | --- |
| Purpose and boundaries | Business purpose, user outcomes, vocabulary, constraints, external responsibilities, and success criteria |
| People and access | User types, organizations/tenants, ownership, role/capability checks, approvals, overrides, delegation, and operator responsibilities |
| Capabilities and interfaces | Features, screens/navigation, nested panels/settings, first-run dialogs, public and administrative surfaces, APIs, CLI/mobile experiences, files, accessibility/localization behavior, and help |
| User journeys | Discovery, onboarding, prerequisites, decisions, task completion, confirmation, return visits, and support |
| Workflows and handoffs | Actor/system steps, assignments, approvals, manual/off-platform work, escalation, and handoff evidence |
| Business rules and logic | Calculations/units, validation, eligibility, limits, defaults, precedence, exceptions, pricing/entitlements when present |
| States and lifecycles | Full implemented state set, allowed/denied transitions, human/system triggers, authority, audit actor/time writes and what approval separation is actually enforced, effective versus processing time, expiration, cancellation, reopening, reversibility, archive/delete behavior |
| Data and relationships | Entities/fields including optional/nullable/defaulted or immutable values, identifiers, cardinality, ownership/isolation, source of truth, lineage/transformation, validation, storage, import/export, retention/deletion; distinguish persisted model fields from exposed editing controls |
| Architecture and dependencies | Repository/module/service boundaries, entry points, shared libraries, consumers, generated artifacts, dependency/configuration sources |
| Integrations and automation | External contracts, authentication mechanisms, callbacks/webhooks, events, queues, scheduled jobs, notifications, synchronization, idempotency and timing |
| Failure and recovery | Rejections versus transient transport failures, stored-session recovery, missing inputs, partial success, duplicates, cancellation races, timeouts, retry limits, dead letters, recovery, rollback, manual reconciliation |
| Security and privacy | Authentication vs authorization, tenant isolation, sensitive data, audit trails, access revocation, and applicable policy/legal obligations with evidence |
| Environments and delivery | Setup/build tooling, dependencies, configuration/flags, infrastructure, local/staging/production differences, migrations, release/promotion/rollback |
| Operations and support | Monitoring/alerts, troubleshooting, support ownership, incidents, maintenance, backups/restoration, service limits and escalation |
| Verification | Acceptance criteria, meaningful tests, execution evidence, supported versions, known limitations, and unverified paths |
| Decisions and history | Relevant change history, recorded rationale, rejected alternatives, tradeoffs, constraints, superseded decisions, and revisit conditions |
| Existing documentation | Destinations, audiences, authority by subject, discoverability, coverage, contradictions, broken examples/links, duplication, obsolete procedures |

Inspect beyond the file tree: routes/commands, dependency manifests, schemas/migrations, jobs, feature flags, deployment configuration, tests and executable external contracts can reveal behavior missing from the visible UI. Current operational notes, design records, support documents and existing maps are comparison targets after the baseline, not discovery leads. Inventory excluded or inaccessible surfaces without silently adding them to the task.

Cross-check major flows against their rendered child panels, dialogs, account settings and secondary actions. Confirm callers and gates; a component file alone does not prove an exposed journey. Account for consequential surfaces with an inventory item or an explicit inspection gap. When a downstream process consumes configurable reference data, trace who creates or changes it and how that affects later results; mentioning the consumer does not document the contributor's task.

For broad work, first enumerate actual registrations and consequential interfaces: routes and nested action bindings; API/command exports; forms and contributor tools; persisted entities/policies; scheduled handlers and build/release jobs. Record each registration source and the entries found, then reconcile every in-scope entry to a coverage unit or a justified exclusion. Inspect actual instantiated callers before deciding an entry is inactive. This census is the source end of the existing coverage record, not a competing feature list.

Reconcile those bindings with named handlers, consequential called helpers and automatic entries in each relevant component: initialization, state-driven rendering/effects, deferred callbacks, disposal and host/request/test hooks. Record the symbol or registration locator, trigger/guard, consequential effect and owning unit, or a justified non-applicability decision. A hook or helper incidentally included in another claim's source range is still unaccounted for until its own behavior is reconciled.

Use one coverage unit per meaningful reader task/variant/operation or system contract. For a family, enumerate exposed create/start, review, correct/update, cancel/remove and recovery operations across its variants before selecting worked examples. Also account for non-UI contributor, authorization, data transformation, timing and delivery contracts needed by the requested audiences. Shared policy or calculation claims may serve several units; link them rather than duplicating facts. Do not omit a contract because another unit already mentions its broad topic.

Inspect breadth first: trace a source-available unit through control/trigger, guards, writes/downstream effects and outcome, record its claims, then move to the next unit. Deepen exceptional paths as their consequences require. Only after this sweep should examples receive extra polish. Share procedure steps only after comparing actual callers/handlers proves equivalence. An input table or one deeply traced sibling does not complete the other correction paths. Include identity/self-exclusion, preserved/recomputed values, parent-child effects and when writes occur during editing, confirmation or cancellation. Trace onboarding/recovery through usable state and re-entry, and contributor work through creation, maintenance and removal. Distinguish atomic, sequential and optimistic changes and what partial failure leaves behind.

For each selected form/transition compare initialized values, no-action defaults, success short-circuits and normalized state with its model, serializer and write payload. Capture optional fields even when unexposed, including whether omission preserves, clears or defaults them. Follow child input bounds to parent dates/state and the actual guard. Keep these outcomes distinguishable in the unit's compact branch/field table rather than hiding them inside a broad setup or CRUD label; separate IDs are unnecessary unless a real consumer requires them.

Keep consequential variants as compact branch rows: condition, effective behavior, source locator, and reader treatment or gap. Include steps skipped or bypassed when a prerequisite is already satisfied, optional steps and later completion paths; the ordinary first-time sequence alone is insufficient. Trace initial defaults, resets and mode changes through instantiated state and production callers to rendered controls/renderer choice. A helper or its test does not establish active behavior without that connection. Follow independent reads when one failure can coexist with another result, including how read failures become completeness/error signals passed into requests, stored results and visible warnings. Distinguish unknown or failed retrieval from confirmed empty data. For persisted state, record canonical/metadata/cache precedence, fallback triggers and any normalization or promotion before routing.

For broad generation, source-available uninspected units remain work to do, rather than an optional frontier created to shorten the answer. Missing runtime access does not prevent source-based instructions when controls, handlers and outcomes can be traced. If a real input/session limit prevents completion, preserve a checkpoint listing outstanding units, impact and exact next inspection point; describe delivery as partial and resume those units when work continues. Do not claim the original broad request completed by changing it to one worked family. A genuinely bounded user request still needs only its affected units and dependencies.

## Close source obligations before authoring

For every in-scope unit, inspect the complete relevant implementation, using callers and consumers to set its boundary. Record the consequential obligations in the existing coverage/evidence record; do not create a second inventory. Check these relationships where applicable:

- Entry/control and eligibility -> validation/default/normalization -> selected query fields, bounds and ordering -> writes or downstream calls -> returned result -> caller state/cache/readback -> visible outcome.
- Successful, empty, missing, rejected and failed branches, including enclosing catch/finally and effects that can throw before the intended return. A returned warning and a thrown exception can lead to different outer responses. Carry preceding guards and returns into each branch's effective condition; its local predicate does not include inputs already handled by an earlier exit.
- State transitions across repeated use, changed selection and interrupted work. Inspect copy/update semantics: omitted or null arguments may preserve identifiers, while a separate sentinel clears them. Trace the resulting submit/update choice, not just the loader's apparent intent.
- Parent/child identity and overlapping guards across create and edit callers. Compare the identifier actually excluded with the records the guard queries; a generic update can also drop discriminator fields.
- Each authorization layer, request validation boundary, typed response and client parser. A UI gate, database policy, service filter and transport status establish different contracts.
- Every consequential selection/aggregation stage: cap, order, ties, truncation/count meaning, parsing/fallback and denominator. Inspect structured eligibility, selected-source membership and context release separately from identity hashing or presentation. Follow configuration lookup failure, unknown values and no-match behavior into the effective output.

Stop expanding a unit when the requested reader tasks and consequential contracts at these boundaries are accounted for, rather than when a file or broad topic has been mentioned. Do not catalogue unrelated implementation trivia. Revisit any unit whose evidence covers only a subset of the relevant implementation. Available source work must be finished for a broad completion claim; unavailable runtime or organizational facts remain explicit boundaries.

### Identify the boundary before sharing a fact

Give each consequential contract a compact boundary identity in the existing record: producer, consumer and stage. The same field, section name or status can mean different things in persistence, normalization, deterministic assembly, generated wording, transport, client validation and rendering. A canonical server constraint does not prove an identical client check. An output-membership rule is not a prose-selection rule; fingerprint inclusion is not admission. Merge or share claims only after code proves the relevant behavior equivalent. Otherwise retain separate stage-specific claims and link them.

Before closing a unit, reconcile its consequential callees and actual branches/properties with the coverage record. Follow builders, adapters, formatters, parsers and canonicalizers that determine membership, precedence, order, output composition or failure. Check ordinary switch cases as well as missing-value fallbacks. For serialized or derived collections, account for each used key, source precedence, conversion, rounding, sorting and empty result where consequential. For configuration/build inputs, follow the consumed value and effective version/default; for migrations, record affected rows, transformations, old/new constraints, transaction and rerun behavior. Comments about backup or validation remain assertions unless observed. A file-level inspected mark or one accurate output field cannot close the remaining source-available work. Keep outstanding callees/properties as the unit's exact frontier.

### Inventory the actual boundary fields

For each consequential exposed or persisted interface, enumerate its actual fields/parameters before choosing which ones to describe: request and response wrappers/items, form payloads, model/serializer writes, configuration, job/release inputs and consumer-facing derived data. Follow every sibling, optional/defaulted field and explicit rejection branch in the implementation. A general string, range or validation statement does not account for another field or a different input/output boundary.

In the existing unit record, keep a compact field/branch table with actual name, type/units, initialized or omitted value, normalization and accepted bounds, active validator/consumer locator, success/write and rejected/empty/failure outcome, and reader treatment. Combine columns or link shared contracts when useful. This is source-obligation discovery, not a second claim inventory. Account for each consequential field with treatment or a source-supported applicability decision. Do not manufacture cosmetic-field obligations or reduce a public contract to a selected handful of fields. Include exact error/status payloads and returned warnings versus thrown failures where they affect use or diagnosis.

Reconcile properties within each field, not only field names: type, nullability, default, parse/coercion, accepted/rejected range and observable effect can vary independently. Retain independently consequential properties as distinct outcomes or clauses in a compact field/branch table; sharing a row does not permit skipping a property's meaning, and separate IDs/duplicated excerpts are not required. Inspect the actual expressions: validation before or after clamping, truncation versus parsing, scalar-versus-embedded precedence and null-preserving copy semantics can change the outcome. A conditional assignment does not prove an output field is absent when an earlier base object or spread supplies it. Record source-supported non-applicability rather than silently dropping a consequential property. Internal forwarding and cosmetic details do not become standalone prose obligations merely because they are enumerable. Shared defaults or a generic validation sentence do not supply this reconciliation.

For forms, trace initialization, changes, reset/re-entry and submission separately. Check whether submit recomputes validation, invokes a callback, reads a stored validity/error flag or sends only a subset of fields. Trace client checks and server admission independently. A validator's existence or a required label does not prove that untouched, cleared or previously valid state is rejected on submit. State the enforced condition and any active path that bypasses it; preserve intended input guidance without converting it into a universal enforcement claim.

Trace final feedback and automatic navigation through their local guards too. A screen may select, suppress or replace a shared error message, or schedule navigation when required state is missing. Preserve the actual predicate, fallback, threshold and callback-time guard; a shared error mapper or provider rejection does not establish the screen's behavior.

### Check conversion and assigned-output boundaries

Before closing a model, parser, builder or formatter, reconcile the actual expressions with these applicable outcomes in the existing field/branch table. Do not turn the checklist into a second inventory.

- **Type and value are different steps.** An accepted type or successful cast does not prove the parser accepts its content. Trace required fields through both failures. For optional fields distinguish absent/null, accepted nonnull, wrong type and rejected value; a null default does not imply failed nonnull parsing becomes null. Check whether each operation is inside the relevant catch, and which later fields/effects are skipped if it throws. Do not describe a language parser as stricter calendar validation or coercion than its actual expression proves.
- **Inspect assigned fields, not nearby intent.** For each consequential derived output inspect its actual right-hand side, every conditional/else or switch arm, initial/spread values, and the exact stage where it is assigned. A group key, hash, display label or filter may share a name without assigning the same output field. Follow earlier guards and the builder's input shape: a run can be nonempty without requiring multiple observations. Keep construction, later filtering/consolidation and final presentation separate.
- **Compare consumers with their own fallback.** A shared stored value can feed a title, list, body, export or server/client path with different defaults or guards. Trace each actual consumer and preserve its type/value handling, positive/nonempty predicate, legacy fallback and exceptional result. Missing data, nonpositive data and wrong-type data need not be equivalent.

Read the implemented success, ordinary fallback and exceptional exit, then state those meanings in the appropriate reader reference. Generic type, validation, grouping or failure assurances do not close these boundaries.

### Compare consumers and interacting guards

For a shared entity used by several surfaces or stages, compare each actual consumer: selected/query field, date/timezone and endpoints, empty/null handling, ordering/cap/count meaning, parsing/defaults, error path and visible or returned result. A dashboard, report, export and analysis may interpret the same optional value differently. Put those differences in the existing linked units; do not use one stage's bound, fallback or state rule as evidence for another.

Compose the caller's selected identity/state with every called guard and write. Enumerate the affected record set, the actual excluded identity, parent/child membership and what can stop the write before later effects occur. A correct generic rule plus a separate edit description does not document their interaction. Trace selection through its exact record/body lookup, no-match fallback and returned result; do not imply that a later filter was part of the earlier query or that another candidate is tried when the code returns immediately.

## Capture a workflow

For each important flow, record enough of the following to trace the complete task. Omit irrelevant fields rather than filling templates with invented information.

- Identity and purpose; intended audience and outcome.
- Actors, tenant/ownership scope, authority, and responsible handoff roles.
- Entry point, trigger, prerequisites, permissions, inputs and units/defaults.
- Ordered actions, decision conditions, meaningful branches, and state transitions.
- Reads/writes, external calls, generated artifacts, notifications, delayed jobs, and manual work.
- Output, persisted result, confirmation/readback, and completion evidence.
- Rejections, interrupted/partial paths, retries/duplicates, cancellation, recovery, escalation, irreversible points.
- Evidence locators, applicable snapshot/environment, discrepancies and unknowns.

For reports, charts, summaries, searches and exports, trace displayed measures to calculations and selected records to actual query fields. Compare category/mode-specific renderers and visible presentation as well as numerical meaning. Publish each time-filtered surface's anchor/week-start rule, calendar span, endpoint inclusion and timezone where consequential; weekly or monthly labels alone are not a range contract, and another surface's range may differ. Define counted calendar duration separately from elapsed-span validation, including inclusive versus exclusive counting. Capture units, aggregation/denominator and missing-value treatment beside the reader's interpretation. Distinguish event/domain dates from creation, recording and processing timestamps; a date-picker label does not prove a query field. Trace derived values to inputs rather than inferring meaning from labels.

Validate numbers and formulas at their active consumers. Trace each documented limit from the specific input/output field through its validation and caller; similarly named constants may constrain another boundary or be unused. For an aggregate, inspect parsing, fallback/imputation, filtering, summation and denominator: missing rows, invalid values and explicit zero may contribute differently. Do not replace that behavior with an assumed valid-only calculation. Keep any static arithmetic illustration distinct from an executed result.

For automated decisions or generated advice, follow the pipeline from deterministic eligibility to accepted output: evidence unit/count, thresholds, text-input gates, rule precedence, selection, generation attempts, independent review/validation and rejection/fallback outcomes where present. Distinguish eligibility from wording, stored history from replay eligibility, and implementation thresholds from domain or clinical recommendations. A status inventory alone does not explain why an output is accepted, withheld or retried. External service calls establish the invoked contract, not unobserved provider behavior.

Trace later-stage filters against the values actually selected upstream, including intersections, empty results and no-match/no-effect branches. When multiple records qualify, inspect actual query order, limits and tie-breaks rather than implying arbitrary or latest selection. Follow the chosen record into referenced content and its effective version/update identity. Saved active configuration need not affect an output; document the condition for its use and what happens when no selected item qualifies. Do not imply that framing, presentation or configuration feeds back into an earlier eligibility decision unless code does so.

Trace both directions when needed: a UI action should reach its persisted/downstream effect, while a job or webhook should lead back to the capability, owner, and user-visible outcome it serves. A committed record and a delivered notification are different outcomes.

For important automatic transitions, capture the initiating condition, identity/permissions used, effective timestamp, no-input outcome, downstream work and what remains committed if that work fails. For authentication recovery, distinguish a rejected stored session from an unreachable identity service before documenting sign-in or retry guidance.

Trace ongoing work by its actual resource owner: acquisition/registration, callback, replacement/rescheduling, self-stop and owner cleanup where implemented. Start/restart behavior does not cover cancellation, unsubscription or disposal; account for each applicable path and its guard separately. Preserve the actual lifecycle trigger: hiding, navigating away, stopping and disposing are not interchangeable without a traced binding. For repeated callbacks, distinguish the state inspected by a guard from later mutations and effects; reaching a threshold does not prove cleanup occurred in that same callback. Connect client cadence, server validity windows and timeout/cap rules; inspect what a transport error, authority refusal or changed eligibility actually does to local work. A server renewal contract alone does not establish client retry/stop behavior. For first-run or repeat notices, follow the missing/outdated-version condition, save result, error display and later change path.

For recovery, renewal or reopening, inspect the actual transition handler and its called guards. Record the complete conditions that permit recovery and the states that prohibit it: actor/ownership, current parent state, authorization or participant approvals, withdrawal/closure markers, and relevant clocks where checked. Separate a recoverable lapse from terminal closure, original limits from rolling validity, and startup eligibility from recovery eligibility and later write admission. Preserve each condition that changes the reader's retry/restart decision; a generic assertion that an open or valid record recovers is insufficient unless its meaning is explicitly defined. Source comments may locate this contract but cannot replace inspection of the guards.

Before claiming a rejection or terminal result, trace the entire exit through enclosing catch/finally blocks and callers. An awaited cleanup, write or external call before the return can throw into a fallback that produces a different result, including success. Record the guard, pre-return side effects, catch scope and fallback return; distinguish lookup failure from explicit refusal when a catch treats both alike. Document the actual exceptional path without claiming unobserved provider/session effects or fixing application code as part of documentation.

Freezing a findings baseline preserves provenance; it does not prohibit further source inspection. If authoring exposes an unsupported consequential step, inspect its implementation and append a source-located supplement or leave that procedure explicitly partial. Keep the frozen bytes unchanged and never fill the gap from existing documentation.

## Relationship model

A table, linked Markdown, or small diagram is sufficient. For larger scopes use stable project-local IDs to connect capabilities, journeys, rules, states, entities, services, documents, and evidence. Do not invent a graph database or tool dependency.

Example relationship statements (illustrative, not system facts):

- A requester creates a service request; the organization owns it.
- An administrator authorizes a state transition subject to a rule.
- A handler writes a record and emits an event; a worker consumes the event.
- A notification provider returns delivery evidence; an operator reconciles failures.
- A developer reference defines the shared contract; two task guides link to it.

Capture direction, meaningful conditions, ownership, and evidence. A generic arrow labelled "uses" rarely explains a consequential boundary. Show actor lanes for handoffs, a state diagram for lifecycle rules, a sequence for asynchronous calls, or an entity diagram for data relationships when that representation answers the reader's question.
