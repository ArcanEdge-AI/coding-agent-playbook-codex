# Technical Debt Audit: [System or repository]

**Audit mode:** [Single Repository / Multi-Repository / Workspace-System / Targeted]
**Audit boundary:** [Repositories, paths, and categories]
**Evidence date:** [YYYY-MM-DD]
**Audit state:** [Complete / In progress / Targeted complete]
**Ledger:** [Absolute path or durable link]

## A. Executive Summary

[Overall condition, highest risks, recurring themes, architectural observations, and highest-value remediation opportunities.]

## B. Audit Scope

| Repository | Path | Branch or ref | Commit | Working-tree state | Major technologies |
| --- | --- | --- | --- | --- | --- |

**Inclusions:** [Policy]

**Exclusions:** [Policy and reasons]

**Targeted categories, if any:** [Categories or N/A]

## C. Repository Coverage

| Repository | Files Discovered | Files Accounted For | Detailed Review | Classified Only | Unable to Review |
| --- | ---: | ---: | ---: | ---: | ---: |

[Explain every meaningful exception.]

## D. GitNexus Coverage

| Repository | Indexed | Graph Appears Current | Graph Used | Cross-Repo Evidence |
| --- | --- | --- | --- | --- |

[Explain unavailable, incomplete, stale, missing, or contradictory graph coverage.]

## E. System Architecture Observations

[Only the components, boundaries, processes, persistence, and dependencies needed to understand the findings.]

## F. GitNexus Knowledge-Graph Analysis

### Architectural Hotspots

[Materially useful hotspots, or N/A with reason.]

### Important Execution Processes

[Processes that materially affected the audit.]

### Highest-Blast-Radius Areas

[Graph-estimated reach plus direct-source verification.]

### Graph / Source Contradictions

[Meaningful contradictions and disposition.]

### Graph-Assisted Findings

[Findings that GitNexus discovered, strengthened, reduced, disproved, or reprioritized.]

## G. Technical Debt Register

| ID | Finding | Category | Severity | Priority | Effort | Blast Radius | Evidence State |
| --- | --- | --- | --- | --- | --- | --- | --- |

## H. Detailed Findings

## TD-NNN: [Concise title]

**Repository:** [Repository]
**Area:** [Area]
**Category:** [Category]
**Severity:** [Critical / High / Medium / Low]
**Priority:** [P0 / P1 / P2 / P3]
**Effort:** [Small / Medium / Large]
**Blast Radius:** [Local / Module / Repository / Multi-repository]
**Evidence State:** [Confirmed / Strongly Supported / Needs Verification]
**Evidence Sources:** [S / G / T / D / C / H]

### Evidence

- [Exact path, symbol, line, test, configuration, history, or graph relationship]

### Current Behavior

[Observed implementation behavior.]

### Why This Is Technical Debt

[Concrete engineering cost, risk, maintenance burden, reliability/correctness problem, or demonstrated limitation.]

### Impact

[Consequence if unresolved.]

### GitNexus Context

[Relevant symbols, clusters, processes, relationships, impact depth, or N/A.]

### Source Verification

[What direct repository evidence confirmed or contradicted.]

### Recommended Direction

[Smallest reasonable remediation; do not implement.]

### Dependencies / Sequencing

[Prerequisites, linked findings, coordinated repositories, or N/A.]

## I. Repository-by-Repository Analysis

[Patterns per repository without repeating detailed findings.]

## J. Cross-Repository Findings

[Contracts, schemas, architecture, duplication, deployment, ownership, or N/A.]

## K. Root Causes / Debt Clusters

[Grouped causes and their affected findings/locations.]

## L. Recommended Remediation Sequence

### Wave 1 - Risk Reduction

[Correctness, security, data integrity, and production reliability.]

### Wave 2 - Structural Simplification

[Harmful complexity/duplication, obsolete paths, and demonstrated boundary debt.]

### Wave 3 - Confidence Improvements

[Meaningful tests, observability, operations, deployment, documentation, and developer workflow.]

### Wave 4 - Opportunistic Cleanup

[Lower-impact work best paired with related changes.]

## M. Quick Wins

[Only verified small, low-risk, high-value items with limited impact.]

## N. Items Requiring Verification

| Suspected concern | Why evidence is insufficient | Evidence required |
| --- | --- | --- |

## O. Audit Limitations

[Inaccessible files, missing systems, runtime gaps, stale graphs, excluded repositories, or other uncertainty.]

## P. Audit Ledger

[Durable ledger reference plus final reconciliation result.]

## Final Verification Record

- Repository coverage reconciliation: [Result and command]
- GitNexus coverage/freshness review: [Result]
- High-severity revalidation: [Result]
- Finding deduplication/root-cause consolidation: [Result]
- Recommendation simplicity/sequencing review: [Result]
- Report validator: [Result and command]
- Source mutations performed: None
