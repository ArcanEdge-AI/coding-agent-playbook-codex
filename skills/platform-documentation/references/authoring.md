# Audience-aware documentation

Select documents from reader tasks and existing project conventions. Start with a navigable index if several documents are needed. Avoid empty sections and duplicate handbooks. An inventory or evidence ledger supports the guides; it does not substitute for usable instructions.

## Audience routing

| Reader | Questions the documentation should answer | Useful outputs |
| --- | --- | --- |
| User | What can I accomplish? What do I need? What do I do next? What does this status/error mean? How do I know it worked? | Getting started, task guides, journey maps, feature help, troubleshooting |
| Admin | Who may do this? How do I configure or approve it? What is the impact? How do I monitor, audit, recover, or escalate? | Administration guide, access matrix, configuration reference, approval/maintenance/recovery SOPs |
| Developer | How do I run and change this? Where is behavior implemented? What are the contracts and invariants? How do I verify and release it? | Setup guide, architecture/domain/data references, API/event contracts, implementation flows, testing/deployment/troubleshooting guides |

Match administrator scope to the platform: organization admins may not operate infrastructure, access every tenant, or retrieve credentials. Identify those boundaries. Include business context for developers and concrete task language for users. Keep internals in the documents whose readers need them, using links for deeper detail.

An internal reader may be served by an evidenced CLI or API workflow. Do not present internal commands as a verified end-user interface when no such supported interface is available. If UI access is missing, label UI instructions unverified and avoid invented buttons or screenshots.

## Executable task guides and SOPs

Use a concise task guide for ordinary actions and a fuller SOP when repeatability, handoffs, operational impact, or recovery warrants it. A useful procedure provides:

- Purpose, intended actor, trigger, scope/applicability, and useful owner/reviewer information.
- Prerequisites: access, inputs, initial state, relevant configuration, tools, and required approvals.
- Steps in execution order with grounded labels/commands/examples and expected intermediate results.
- Decision branches: the condition, responsible actor, and next action.
- Consequences/irreversible points where they affect a decision.
- Relevant failure, interruption, timeout, duplicate, cancellation and recovery instructions, including known retry limits.
- Completion evidence: what to observe or read back, and what still needs a human/external handoff.
- Escalation and unresolved limitations, with supporting references.

Do not call a procedure validated just because the prose is complete. If required steps are unknown, provide the evidenced portion and identify the specific missing input; label the procedure draft/partial. Never invent a recovery command, approval policy, backup capability, or escalation owner.

Before marking an important task documented, reconcile its guide against the discovered branches: when/for whom it appears (including version or eligibility changes), the exact interaction sequence, persisted success/readback, failed or partial save, and the reader's next action. Put each consequential branch in the procedure or a specific linked reference; a ledger mention alone is insufficient. Record missing reader treatment as partial rather than treating an evidence citation as instructions.

Draft from the coverage units, rather than choosing topics again during writing. For a broad request, give every inspected in-scope task/variant/operation its usable reader treatment before expanding a favorite example. A compact shared procedure plus source-proven variant branches is acceptable; a list of inputs plus one full sibling is insufficient. Reconcile starting state, actual control/sequence, branch, persisted result/readback and relevant failure for each exposed operation. Include skipped/bypassed setup alternatives and upstream maintenance where needed. Explain range anchors/endpoints and elapsed-versus-calendar counts where readers choose or interpret them, with the developer calculation linked when useful. Keep eligibility/acceptance contracts shared and user outcomes plain; method names or ledger facts alone are not completion, correction or recovery instructions.

At an optional choice, explain the consequences of enabling, declining or disabling it at the point where the reader decides. State which capabilities/access change, which ordinary tasks and existing records remain available, and whether/how the choice can be reversed. Trace both the state change and independent access checks for the tasks claimed to be unaffected; the absence of a local write alone is not proof that access is preserved. Keep any uninspected consequence explicit rather than implying either loss of access or a blanket guarantee. A success/failure procedure is still incomplete if the reader cannot tell what declining means for their main task.

Trace each consequential UI action from its rendered initiating control through the handler, any confirmation, and the persisted result/readback. Record the actor/state, actual control type and label, handler locator, confirmation label or none, and outcome locator in the working evidence record; a compact row is enough. Creation forms, saved-record rows and edit dialogs may expose the same property through different controls. Verify the surface the procedure actually names rather than borrowing another surface's widget or label. Distinguish navigation/control, dialog title, confirmation button, result message and caller-supplied API literals versus text a person must type. Do not substitute a confirmation label for its initiating control. When wording varies by state, give the condition or describe the action without inventing a fixed label.

## Developer references

Document contracts at the level needed to use or change them: inputs/outputs and relevant optional/defaulted fields, identifiers, units, errors/completeness signals, authorization, full lifecycle states and audit writes, persistence, selection precedence/content versioning, side effects, configuration, timing/retries, and compatibility consumers where applicable. A stored field need not have a UI control; an audit stamp need not enforce independent approval. Include setup and verification commands that exist in the project. Explain environment-specific behavior and boundaries between source proof, local execution, and deployment evidence.

Examples must match the actual interface and working directory. Label synthetic IDs/data and prerequisites. Keep secret values out. Distinguish supported procedures from illustrative pseudocode and hypothetical recommendations.

When examples share state across documents or actors, name the handoff checkpoint and expected state. Mark alternate branches explicitly and keep cancellation, deletion, or other terminal examples from consuming the record needed by a later happy-path example; use a separate disposable record/store where practical. Validate the linked sequence through the handoff, not just commands inside one guide. If examples were only inspected or equivalent flows exercised, say so rather than claiming the documented walkthrough was executed.

## Capture work and decisions

Use supplied conversation, diffs, commits, primary artifacts, execution evidence and explicit decisions for the requested work history. Do not use existing platform documentation to infer implementation findings or historical rationale. Do not imply access to unavailable chats or infer that all local changes belong to this session.

Capture the meaningful chronology and resulting state: objective, starting problem, completed work, workflow/behavior changes, affected interfaces/documents, consequential choices, checks actually run, limitations, remaining work and next step. Preserve quantities, units, qualifications, approvals, and evidence boundaries.

For a consequential decision, preserve its context, recorded rationale, considered alternatives, tradeoffs, status, and revisit condition when available. Label reconstructed explanations as inference and missing rationale as unknown. Distinguish attempted/abandoned approaches from the accepted result. Preserve useful history without turning a failed attempt into current operating instructions.

## Reader walkthrough

For every requested audience with applicable tasks, walk at least the important documented tasks from a plausible starting point. Recheck the final prose directly against the relevant rendered controls/handlers and recovery guards after summarizing; an earlier accurate finding or a general self-check statement does not validate the resulting instructions. Check navigation/discoverability, prerequisites, role and state boundaries, ordered actions, expected results, failure guidance, and completion confirmation. Preserve conditions that change whether recovery is allowed in the guide or a specific linked contract; shorthand such as open, valid or eligible must resolve to those conditions. Inspect referenced commands and links. Exercise real entry points only within authorization; retain the distinction between a source walkthrough and executed behavior.

Reconcile every consequential source outcome with the actual reader passage at its producer/consumer stage. Conditions, effects and limits must be distinguishable; a shared field/branch table can state and verify several outcomes without detached per-clause appendices. Source locators and an evidence ledger do not supply missing instructions. Use a concrete near-miss comparison for ambiguous, conflated or disputed meanings rather than writing an alternative and repeated quote for every ordinary fact.

Check optional fields and conversion failures, ordinary derived-field assignments, consumer-specific defaults and enclosing exception paths explicitly. A successful cast is not successful parsing; a null branch is not a fallback for malformed nonnull input; documenting a grouping key is not documenting an output assignment. Keep default/ordinary, missing/empty and exceptional outcomes at their own boundary. Follow awaited pre-return effects through catches before promising always, rejects or succeeds.

After an edit, preserve the passage's already-correct facts and qualifications, read its new assertions and neighbors, and reconcile affected audience views. An accurate technical qualification does not neutralize a contradictory unconditional user sentence. Keep steps natural for readers and link precise shared contracts where needed. A source-supported correction replaces false meaning explicitly; retention never requires retaining an error or a previous claim count.

Finish with the evidence reference's compact source-led review/repair loop. Revisit actual registrations and relevant handlers/callers for unindexed branches and sibling variants, rather than checking only drafted topics. Broad high-assurance work needs its warranted independent source-first review; narrow edits need affected-flow verification. Reuse valid unchanged evidence, check changed meanings and their context, and record remaining material gaps honestly. Do not create a new blind run or full duplicate ledger after each repair.

Keep evidence detail accessible without flooding ordinary instructions with code locations. One coverage map and a concise verification summary can support several readable guides. Separate actual procedures, evidence limits and proposed improvements.
