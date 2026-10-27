---
name: technical-debt-auditor
description: Perform or resume comprehensive, evidence-backed technical-debt audits of a repository, monorepo, repository group, or multi-repository system. Use for explicit technical-debt reviews, repository health or debt assessments, architectural or category-targeted debt audits, GitNexus-assisted debt analysis, whole-codebase maintainability reviews, interrupted audit continuation, and audit-grounded remediation plans. Do not use for ordinary bug fixes, normal PR or single-file reviews, feature implementation, general architecture discussion, routine refactoring, or dependency upgrades without an audit request.
---

# Technical Debt Auditor

Perform complete, evidence-backed technical-debt audits while keeping inspection separate from remediation.

Apply both governing principles:

> Use GitNexus to discover and understand relationships. Use source code to establish implementation truth. Use both to determine impact.

> Do not over-engineer it. Make it elegant, not bloated. Prefer the smallest complete solution that solves the demonstrated problem reliably.

## Route the bundled resources

- Read [references/technical-debt-audit-methodology.md](references/technical-debt-audit-methodology.md) completely before beginning a new full or targeted audit, resuming an audit whose methodology version is unknown, judging findings, or finalizing a report. It is the detailed authority for coverage, analysis, findings, severity, remediation sequencing, and verification.
- Copy [assets/audit-report.md](assets/audit-report.md) when creating the durable report.
- Let `scripts/audit_coverage.py inventory` create the working ledger. [assets/audit-ledger.csv](assets/audit-ledger.csv) documents its column contract and is a fallback header template.
- Use `scripts/audit_coverage.py reconcile --require-complete` at the final coverage gate. Use `validate-report` before delivery.

Do not load templates before they are needed, and do not duplicate the detailed methodology into working notes.

## Decide whether this skill applies

Use it when the user clearly requests a comprehensive technical-debt assessment, repository health/debt review, architectural-debt audit, targeted debt-category audit, system-wide maintainability assessment, or remediation plan based on such an audit. Natural-language equivalents count.

Do not activate it merely because ordinary work touches quality, architecture, tests, security, dependencies, or maintainability. A normal bug fix, PR review, single-file review, feature, architecture conversation, refactor, or upgrade remains ordinary work unless the user asks for an audit.

## Select the audit mode

- **Single Repository:** audit one repository comprehensively.
- **Multi-Repository:** audit every named repository independently and as one system. Never assume repository boundaries are architecture boundaries.
- **Workspace/System:** discover candidate repositories in the requested workspace, establish the system boundary, and audit only the confirmed or safely inferable boundary. Ask one concise scope question only when competing boundaries would materially change the audit.
- **Targeted Debt Audit:** apply the full evidence and coverage discipline while narrowing findings to requested categories such as architecture, testing, security, dependencies, performance, developer experience, or operational reliability. Label the result as targeted; never claim it is a complete general technical-debt audit.

For a remediation-plan request without an existing audit, establish enough audit evidence first to support the plan. Do not convert speculation into a backlog.

## Establish inputs and invocation state

At invocation:

1. Briefly state that the Technical Debt Auditor skill is being used.
2. Identify the selected mode, repositories or discovery boundary, requested categories, and report destination.
3. Record each repository path, branch/ref, commit, upstream when relevant, and working-tree state.
4. Establish file-inventory and GitNexus coverage before making completeness claims.
5. Begin ordinary read-only work without repeatedly asking permission.

Infer minor details from the workspace. Ask only when an unresolved scope choice materially changes which repositories, system, or category is in scope.

## Preserve the audit-only boundary

By default the skill authorizes inspection, search, GitNexus queries, static analysis, safe non-mutating tests or validation, audit-state and report creation outside audited source, and remediation planning.

It does not authorize source, configuration, documentation, dependency, database, infrastructure, branch, commit, pull-request, issue, deployment, external-publication, or GitNexus-index mutations. Never rebuild or refresh a GitNexus index without separate authorization.

If the request combines audit and fixes, establish the audit evidence first, then implement findings already covered by the user's bounded remediation authority. Ask only when a finding exceeds that scope or requires a new consequential decision. An audit-only request remains read-only; “fix whatever you find” does not authorize unrelated, destructive, or production actions.

## Create deterministic audit state

Store state outside every audited repository. Prefer the host-provided persistent task work directory; otherwise use `${CODEX_HOME}/state/technical-debt-auditor/<audit-id>/` (or the platform-equivalent Codex state location). Do not add audit state to production source merely for convenience.

Maintain at least:

- `scope.md`: mode, repositories, refs/commits, worktree states, inclusion/exclusion policy, categories, evidence limitations, methodology version, and output destination.
- `inventory.csv`: immutable baseline inventory produced deterministically.
- `audit-ledger.csv`: one row for every in-scope inventory item.
- `findings.md`: confirmed finding records and unresolved candidates across batches.
- `audit-report.md`: final or in-progress report.

Treat inventory scope and ignore behavior as explicit decisions. Git-tracked and non-ignored untracked files are normally in scope. Inspect ignore rules and record why ignored/vendor/generated/build/cache areas are included, excluded, or classification-only; never assume ignored means irrelevant.

Run the bundled inventory helper with explicit repository mappings. It refuses to place output inside an audited repository unless deliberately overridden:

```text
python <skill-dir>/scripts/audit_coverage.py inventory \
  --repo api=/absolute/path/to/api \
  --inventory /outside/repos/inventory.csv \
  --ledger /outside/repos/audit-ledger.csv
```

Use `--include-ignored` only when the established scope requires ignored files. The script preclassifies files conservatively; the auditor remains responsible for correcting classifications and explaining classification-only decisions.

## Resume without restarting blindly

For "resume the technical-debt audit":

1. Locate state matching the recorded repository paths and scope. If several states plausibly match and the choice changes the work, ask one routing question.
2. Read `scope.md`, the ledger, confirmed findings, and incomplete batch state.
3. Recheck repository branch/ref, commit, upstream, and worktree status.
4. Generate a new inventory snapshot rather than overwriting the baseline, then reconcile path additions/removals and repository drift.
5. Revalidate completed ledger rows affected by changed commits or working-tree files. Preserve unchanged completed work.
6. Continue the next deterministic incomplete batch and consolidate only after the ledger is complete.

Never claim continuity if state is missing or incompatible. Record the limitation and establish a new baseline when necessary.

## Use GitNexus selectively

Detect whether callable GitNexus capabilities and an apparently current index exist for each repository. Do not assume availability from a skill name, installation record, or index directory alone.

When available, use GitNexus where relationships materially help with system mapping, dependencies, callers/callees, functional clusters, execution flows, architectural hotspots, fan-in/fan-out, blast radius, dead-code investigation, root-cause relationships, and cross-repository analysis. Query with an investigative purpose; avoid repetitive graph calls when source already resolves the question.

For every material graph conclusion:

- inspect the relevant source, configuration, tests, or runtime evidence;
- state what source verification confirmed or contradicted;
- describe graph reach as graph-estimated, not guaranteed runtime impact.

If GitNexus is unavailable, incomplete, stale, missing a repository, or contradictory, record the limitation and continue with source evidence. Absence of a graph edge is never proof that no runtime relationship exists.

## Apply the evidence hierarchy

For implementation behavior, prefer:

1. direct source, configuration, or runtime evidence;
2. relevant tests;
3. GitNexus relationship evidence;
4. current architecture or design documentation;
5. historical documentation.

Lower-ranked evidence still matters. Investigate meaningful contradictions instead of discarding one source. Documentation shows intent, not necessarily current behavior; graph evidence shows discovered relationships, not necessarily runtime truth.

Use evidence-source codes `S`, `G`, `T`, `D`, `C`, and `H` and confidence states **Confirmed**, **Strongly Supported**, and **Needs Verification** exactly as defined in the methodology.

## Execute the audit

Follow the detailed methodology. At a control-plane level:

1. Establish scope, repository state, inventory, ledger, and GitNexus coverage.
2. Reconstruct the architecture and important execution flows before judging isolated files.
3. Use source structure and graph relationships to identify hotspots, then account for every in-scope file in context.
4. Evaluate applicable debt categories and cross-repository relationships.
5. Require an evidence-backed actual cost, risk, burden, limitation, or consequence for every finding.
6. Verify dead-code claims, high-severity claims, root causes, and blast radius with the additional checks in the methodology.
7. Consolidate symptoms into root-cause findings and remove stylistic, duplicative, or speculative observations.
8. Recommend the smallest reasonable remediation and order it by dependencies and risk; do not implement it.
9. Reconcile the complete ledger, validate the report, and disclose limitations before declaring completion.

The number, age, length, connectivity, or unfashionable style of code is only a signal. If "What actual problem does this cause?" has no meaningful evidence-backed answer, do not report it as technical debt.

## Batch large scopes deterministically

Never silently sample or shrink scope. Preserve the full inventory and divide work using the boundary that best retains system context: repository, application, service, package, directory, architecture boundary, or GitNexus functional cluster.

For each batch record its exact inventory subset, status, architecture context used, ledger rows completed, candidate findings, confirmed findings, and unresolved dependencies. Avoid re-review of unchanged completed rows. When context is interrupted, resume from durable state until every inventory item is accounted for. Final consolidation begins only after all batches and cross-boundary checks are complete.

## Enforce finding quality

Optimize for root-cause quality, not finding count. Do not report debt merely because another design is possible, a dependency is newer, a function or file is long, more abstraction/comments/tests could exist, naming could improve, a graph node is central, or another pattern is preferred.

Every material finding must include the methodology's required ID, location, category, severity, priority, effort, blast radius, evidence state/sources, evidence, current behavior, concrete debt consequence, impact, GitNexus context when applicable, source verification, smallest recommended direction, and sequencing.

Keep severity separate from remediation priority. Keep uncertainty visible. Consolidate symptoms that share one underlying cause.

## Produce artifacts and finish only through the final gate

Use the bundled report template as a starting point, adapting it only when the scope makes a section genuinely inapplicable. Keep the complete ledger as a separate artifact and link or reference it from the report.

Before completion:

```text
python <skill-dir>/scripts/audit_coverage.py reconcile \
  --inventory /path/to/inventory.csv \
  --ledger /path/to/audit-ledger.csv \
  --require-complete

python <skill-dir>/scripts/audit_coverage.py validate-report \
  --report /path/to/audit-report.md
```

Resolve every error. Review warnings manually. Then perform all 22 final verification checks in the methodology, including repository and GitNexus coverage, finding consolidation, architecture/flow analysis, recommendation simplicity, and high-severity revalidation.

Do not claim a complete audit when any in-scope file is pending or unaccounted for. A targeted audit may be complete for its declared category boundary while remaining explicitly non-general.
