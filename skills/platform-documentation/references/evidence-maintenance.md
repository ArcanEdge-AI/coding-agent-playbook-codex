# Evidence, coverage and efficient verification

## Evidence boundary

Code and machine-consumed definitions establish behavior at the inspected snapshot. Runtime observations establish what happened for their inputs, roles, environment and time. A test definition is an assertion, a historical pass is historical, and a user requirement is requested behavior. Existing documentation is a comparison target after source discovery, never a source of implemented facts. Inference and missing rationale must be labeled.

Use full repository-relative file paths with symbols or valid line ranges; shared evidence keys are acceptable if their mapping is unambiguous. Record a source ref/snapshot and meaningful local differences without inventing Git or deployment access. Separate inspected, unavailable, excluded and genuinely absent inputs; check a named missing-input claim against the actual inventory. An unavailable runtime does not excuse source-available work.

## One current coverage record

Prefer a compact Markdown table or existing project record. Keep the source census and its task/operation/variant reconciliation together, not in competing inventories. A useful row contains:

| Task or contract | Sources and actual boundary | Consequential branches/data | Reader location | Source/review state and next gap |
| --- | --- | --- | --- | --- |
| A meaningful task/operation/variant | Entry/handler and relevant producer, consumer and stage | Conditions, results, defaults, failure/partial effects and differences that matter | Guide/reference section, or missing | Inspected/reviewed/partial/unavailable/excluded, with specific reason |

Record enough census detail to account for all in-scope exposed entries and consequential non-UI contracts. Group equivalent registrations or internal forwarding only when their actual behavior proves equivalence. Keep independently useful outcomes distinguishable in rows or clauses; the map cannot claim a family covered because one member is documented. Conversely, ordinary parameter forwarding, cosmetic literals and implementation-local assignments do not each need a new obligation unless they affect use, administration, development or diagnosis.

Keep source inspection, current reader treatment and runtime verification as separate states. Update current reader statuses after review rather than carrying forward candidate-unseen or pending labels as if they were current verdicts. A preserved earlier source snapshot is historical evidence, not a second current status ledger.

For blind/high-assurance work preserve one source baseline before candidate access, one initial candidate identity and the final result or normal versioned diff. A revision plus relevant working changes or a single snapshot is usually enough identity evidence. Do not create a manifest, alias index or full archive at every checkpoint. Add discoveries and source corrections to the current record with a concise before/after reason; retain meaningful history without duplicating every intermediate export.

## Review the meaning, not the volume

Apply these checks to every discovered consequential outcome, using the workflow/boundary row as the review unit. A reader passage can treat several outcomes; each must actually be distinguishable. Atomic meaning does not require one JSON object, quote and alternative per property.

- Read the actual guide/reference passage in context, not the claim metadata. Can a reader find the relevant condition, effect and any qualification needed at this stage? A topic, identifier, source citation or parent approval cannot supply missing words.
- Compare it with the actual producer/consumer implementation, including enclosing guards/returns/catch/finally. Distinguish type acceptance from value parsing, missing/null from rejected nonnull input, ordinary assignments from grouping/selection and neighboring consumers' fallbacks. Use discovery's boundary checks rather than inferring these from names.
- Inspect consequential assertions in the passage back to code, including extra promises added during writing. Reuse the same canonical facts for forward coverage and reverse assertion review; do not build a second full author-claim inventory just to duplicate the first.
- Where a boundary is ambiguous, easily conflated, disputed or newly repaired, name a plausible alternative and point to the actual words ruling it out. Keep exact excerpts when useful for disputed meaning or automated checking. Routine unambiguous contracts need a clear review decision and reader location, not repeated prose certificates.
- Before reporting an omission, search the current reader set and linked shared references. Credit equivalent meaning at the correct boundary; report poor navigation separately. Related wording at a different stage, or an accurate qualification contradicted elsewhere, is insufficient.
- Revisit the source census and full relevant handlers/callers, independent of the drafted topic list. Check unindexed siblings, automatic/resource-owner paths and exposed operations. A retained subset is not whole-platform closure. Record concrete new gaps, not a ceremonial closure checkbox.

Use appropriate depth for impact and complexity. This changes how much proof to write, not which source-available tasks or material contracts are in scope. Supporting/internal metadata may receive a concise applicability reason instead of invented audience prose. Deferred required meaning remains partial.

## Compact verification loop

1. **Source baseline and draft.** Inspect scope and build the source-led coverage map before existing document comparison. Draft the requested reader documents from that map. Keep genuine unknown interfaces explicit.
2. **One review.** For broad high-assurance work, use one bounded independent source-first reviewer when available and authorized. It derives its own task/boundary notes from code before seeing the candidate, then checks the complete source-available task scope and consequential prose. It may use compact tables; it need not recreate an author's per-field JSON inventory. Give no prior results, suspected omissions or answer keys to a blind reviewer. If independence is required but unavailable, disclose the unmet gate.
3. **Consolidate findings.** Return a concise set of material issues with primary source, actual/missing reader words, effect on the reader and affected flows. Do not emit a separate report for each role, clause, correction or helper invocation. Code outranks review opinion; verify findings before editing.
4. **Repair once as a batch.** Correct code-backed issues in the canonical documents and affected audience views. Preserve valid content and record meaningful source corrections. Do not retain a false claim merely to retain a count. Keep the original evaluation draft separate when first-draft scoring matters.
5. **Recheck the changed meanings and affected context.** Follow changed dependencies/consumers, compare actual final passages and confirm the consolidated issues resolved or explicitly open. Preserve valid unchanged decisions. A late new family requires source discovery of that family and its effects; it does not justify replaying unchanged work. Do not start a new blind reviewer for every repair.
6. **Finish current mechanics and delivery.** Run applicable source-location, link, command/example and accounting checks once for the final changed artifact set. Reuse a passing result if its inputs/scope remain identical. Resolve failures with the narrowest valid correction/recheck. Deliver documents and one verification summary with scope, snapshot, checks, findings disposition and limits.

Default to this single review/repair/recheck loop. Before large work, set an effort/iteration allowance consistent with the user's constraints and host controls. Additional iterations need an identified new material dependency or invalidated result and a changed approach. Do not manufacture further audits after acceptance, silently stop at a known gap, or spend an unbounded sequence chasing an undefined 100%.

## Preserve meaning during edits

For a changed passage, identify its already-correct conditions, effects and limits before replacing or shortening it. A short checklist in the current finding/coverage row or the visible diff is sufficient. Read the whole resulting passage and neighbors afterward: every prior correct meaning must remain, unless code supports an explicit correction. Check new statements too. Split dense prose into a compact field/branch table when that improves retention.

Unchanged text/source alone permits reuse only when the relevant source contract, shared dependencies and reader context are still valid. A helper, enclosing catch, role rule or cross-link change can invalidate a fact even if its local line is unchanged. Trace those dependencies; recheck the affected set, which may be broad. Do not revalidate the whole platform for a local clarification with no broader effect. Never infer retained semantics from IDs, counts, a parent verdict or matching keywords.

Keep one accepted current record. When a source proposition was wrong, replace it with the source-supported meaning and a concise correction; no need for parallel alias graphs unless actual consumers or an evaluation require them. Archived drafts need clear historical status, not repeated locator repair. Validate current reader/evidence references and any historical citation explicitly relied on for a current claim. If an immutable historical citation was wrong, annotate it once with the supported correction; do not recursively rescan every prior report and correction receipt. Do not ship bad current citations under a historical excuse.

## Mechanical tools when useful

The bundled helpers are optional for structured records. Do not create hundreds of claim records solely to satisfy a tool. A compact coverage map with inspected sources, reader locations and semantic review can be checked directly. Mechanical checks do not establish discovery completeness, semantic support, atomicity, UI accuracy, justified exclusions or runtime correctness.

`check_source_paths.py` checks structured file/line locators and scans Markdown for source-looking candidates:

```text
python <skill>/scripts/check_source_paths.py --source-root <source> --docs-root <readers> --output <source-check.json>
```

Optionally add `--records <claims.json> <units.json>` for JSON arrays whose rows have `id` and nonempty `sources`. Every relied-on locator must resolve to its actual source file and valid bounds. Classify unresolved Markdown candidates (defect, evidenced output/route or illustration); do not treat a successful subset as full compliance. Compare cited formats with scanner coverage: it includes Dart and lockfiles, but unmatched suffixes, extensionless references and other citation styles need a separate check only when actually cited. Symbols and paths can reduce brittle copied line ranges. Check semantic support separately.

`check_reader_treatments.py` is available when an existing structured contract index or explicit acceptance requirement warrants exact excerpt/accounting checks. Use one current nonduplicated export, not competing indexes:

- Units: `{id, task, sources, audiences, inspection, claim_ids, reason?}`. `inspection` is `inspected/partial/pending/inaccessible/excluded/not_applicable`; non-inspected states need a reason.
- Claims: `{id, unit_id, facet, condition, outcome, qualifier, claim, sources, audiences}`. Canonical unit membership is explicit; `qualifier` may be empty. Use a row per independently consequential contract when using this schema, not per irrelevant scalar.
- Treatments: `{id, status, reader_file, reader_excerpt, reader_check}` for `documented`; `partial/excluded/disputed` require a specific `reason`. Excerpts must occur in an explicitly listed actual reader file, not the audit record. Supporting/excluded dispositions need real applicability reasons.

```text
python <skill>/scripts/check_reader_treatments.py --docs-root <output> --coverage <units.json> --claims <claims.json> --treatments <treatments.json> --readers <guide.md> <reference.md> --output <output/check.json>
```

`--output` for the reader checker must be inside `--docs-root` and must not overwrite inputs/readers. Omit it to capture stdout elsewhere, including for a sealed corpus. Read the compact result fields; do not dump huge arrays into conversation context. The helper's partial/indexed unit labels are accounting results, not current semantic verdicts; maintain real source-closure/reader states in the current coverage map. Green literal matches do not validate meaning. Use equivalent direct checks if Python is unavailable.

Neither helper checks local Markdown navigation or proves a command works. Validate referenced links/anchors and command argv, working directory, inputs/environment, stateful handoffs and expected effects. Execute application procedures only within task authority. Do not call a command validated when it was only source-inspected.

## Correction, refresh and resumption

For correction, freeze code-derived findings before opening document targets; compare relevant claims and then repair the appropriate canonical document. Classify stale/incorrect docs, missing docs, intended-versus-implemented differences, version/environment conflicts and unknowns. New facts prompted by a document still need independent code evidence. Preserve stable links and useful history; inspect consumers before retiring duplicates. Do not silently fix the application.

For refresh, follow changed behavior/data/permissions/interfaces/configuration through affected guides, SOPs, references, examples and diagrams. Search for competing old promises and invalidate only checks whose inputs or context changed. Keep applicability metadata useful: audience, source snapshot, environment where relevant, actual verification and known revalidation triggers. Do not invent owners or mandatory schedules.

For resumption, preserve the request/scope, current map and documents, accepted evidence/checks, unresolved issues and exact next frontier. Recheck changed inputs; do not replay unchanged discovery, clone ledgers or reload an entire transcript. Store no credentials or unnecessary personal information.

Finish when requested reader tasks and discovered consequential source-available contracts have usable treatment, affected checks pass and no known material contradiction/omission remains. Source-available gaps are work, not external unknowns. Passing workflow gates is not a percentage of all possible documentation: define any requested denominator from meaningful discovered scope, exclude nothing silently, distinguish initial generation from repaired acceptance and qualify runtime/deployed uncertainty. Held-out final evaluations remain fixed after final handoff; repairing a failed final result cannot rewrite its grade.
