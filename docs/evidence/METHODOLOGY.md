# Evidence Methodology

Each public run record must identify:

- **Baseline:** benchmark identifier, date, Playbook version or commit, Codex version where available, starting repository commit, and exact user task.
- **Execution:** root model and reasoning effort, subagent roles/models/efforts, task graph and dependencies, agent count, and worktree usage.

Capture exact start and end times with timezone. Derive elapsed time from those values. Also record:

- **Changes:** human interventions, commits, files changed, and additions/deletions where available.
- **Validation:** tests and results, applicable typecheck/build/lint results, independent findings, correction cycles, and final checks.
- **Limits:** environmental limitations, failures, and unresolved findings.

## Evidence rules

- Preserve primary artifacts or stable references where public disclosure permits: task text, commands, sanitized logs, diffs, review findings, and validation output.
- Use exact captured values. If a field was not captured, state `Not captured`; if it does not apply, state `Not applicable`. Do not reconstruct exact values from memory.
- When reporting account usage observations, capture before-and-after evidence from the same account context and describe the observation without attributing causation.
- Keep a correction and review trail: identify independent findings, the disposition of each finding, and the validation performed after corrections.
- Redact or omit secrets, private code, credentials, confidential client information, private repository identifiers, private logs, and details not authorized for publication.

## Repeatable procedure

1. Freeze the fixture and Playbook baselines; capture before evidence and exact start time.
2. Start a fresh session with the exact task; record routing and human interventions as they occur.
3. Obtain independent review, record corrections and their disposition, then run final validation and capture end evidence.
4. Publish the run record with every missing field explicitly marked `Not captured` or `Not applicable`.

## What This Does Not Prove

A single run does not prove universal cost savings, universal token savings, universal speed improvements, causation, superiority over standard Codex, superiority over another coding agent, or identical results on other repositories. A controlled comparison requires a separately designed control with equivalent task, baseline, environment, capture method, and acceptance criteria.
