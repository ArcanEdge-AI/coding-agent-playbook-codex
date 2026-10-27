# Public Evidence

This area separates three related but different forms of evidence:

- **Field use:** ArcanEdge uses these patterns in real engineering work.
- **Private field evidence:** deeper records from client and unreleased-product work remain private and are not a public evidence dump.
- **Public reproducibility:** benchmark fixtures and run records let others inspect the playbook's observable behavior without access to private code.

Public runs can measure the prompt, root plan, task graph, model routing, bounded delegation, tests, independent review, correction cycles, final validation, and outcome. They may record account usage only when exact before-and-after evidence was captured.

This repository does not publish private repositories, source, credentials, internal implementation details, confidential client information, or unredacted private logs. Missing evidence is recorded as missing, not estimated.

## Reproduce or contribute

Start with [Benchmark 001](./BENCHMARK-001.md). Its first measured record, [Benchmark 001 Run 001](./BENCHMARK-001-RUN-001.md), documents one execution on 2026-08-17 and links to [implementation PR #1](https://github.com/ArcanEdge-AI/coding-agent-playbook-benchmarks/pull/1). The run recorded that PR as public, open, and unmerged; this is not a current status claim.

For a new run, use a separate public fixture at the documented baseline. Preserve unrelated local work before any reset. Record the result with [RUN-TEMPLATE.md](./RUN-TEMPLATE.md). Community runs may be submitted through [Share a Playbook Run](https://github.com/ArcanEdge-AI/coding-agent-playbook-codex/issues/new?template=share_playbook_run.md). Public fixture links and artifacts are welcome; private repositories are not required.

See [METHODOLOGY.md](./METHODOLOGY.md) for the capture rules and limits of these records.
