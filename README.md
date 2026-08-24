<p align="center">
  <img src="./assets/coding-agent-playbook-codex-hero.png" alt="Coding Agent Playbook — Codex Edition hero banner" width="100%" />
</p>

<h1 align="center">Coding Agent Playbook — Codex Edition</h1>

<p align="center">
  <strong>Run Codex like an engineering team, not one giant agent.</strong>
</p>

<p align="center">
  An open-source engineering operating model for Codex: progressive-disclosure skills, model-aware subagents, bounded delegation, independent review, and validation.
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#the-operating-model">Operating Model</a> ·
  <a href="#codex-native-structure">Codex-Native Structure</a> ·
  <a href="#public-evidence">Evidence</a> ·
  <a href="#repository-structure">Repository Structure</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Codex-Edition-6E7BFF" alt="Codex Edition" />
  <img src="https://img.shields.io/badge/Subagents-Orchestrated-00C2FF" alt="Subagents Orchestrated" />
  <img src="https://img.shields.io/badge/Skills-Progressive%20Disclosure-4ECDC4" alt="Skills use progressive disclosure" />
  <a href="https://github.com/ArcanEdge-AI/coding-agent-playbook-claude-code"><img src="https://img.shields.io/badge/Claude%20Code-Edition-D97706" alt="Claude Code Edition" /></a>
  <img src="https://img.shields.io/badge/License-MIT-2ECC71" alt="MIT License" />
</p>

---

## Install

The primary installation path is the Codex plugin marketplace:

```text
codex plugin marketplace add ArcanEdge-AI/coding-agent-playbook-codex
```

Then open the Codex app's Plugins UI and install **Coding Agent Playbook — Codex Edition**. The plugin provides the skills and their supporting references as one native package.

After installation, use the skills explicitly by name when useful, for example:

```text
$subagent-orchestration
$task-graph-orchestration
$worktree-lifecycle
$multi-session-coordination
$reference-doc-routing
$senior-code-review
```

Codex can also select a skill from its description when the request matches.

### Optional companion configuration

The current plugin schema documents skills, but it does not document bundling personal custom-agent TOMLs or modifying the user's global `AGENTS.md`. Those remain an optional companion installation.

Invoke:

```text
$install-coding-agent-playbook
```

The skill previews the requested mode first, then uses the repository's Bash or PowerShell companion script. Full mode manages a lean marked section in the global `AGENTS.md` plus personal custom agents. Support-only mode installs custom agents and removes this playbook's marked global section if present.

Full mode stops before changing files when a non-empty global `AGENTS.override.md` would cause Codex to ignore the managed `AGENTS.md` section.

See [INSTALL.md](./INSTALL.md) for exact commands, migration behavior, validation, and safe removal.

## The Operating Model

The root agent acts as the senior engineer. It owns understanding, architecture, decomposition, routing, integration, validation, final acceptance, and the user-facing report. Supporting roles handle bounded planning, engineering, testing, documentation, and independent review; they do not replace root judgment or human authority.

<p align="center">
  <img src="./assets/codex-engineering-team.svg" alt="Operating model: a user works through a root senior engineer, bounded supporting roles, root integration, validation, correction, and final result." width="100%" />
</p>

The default engineering loop remains:

```text
Understand → Plan → Implement → Verify → Review → Report
```

The playbook favors the smallest clear change that fits the codebase, preserves unrelated work, and can be proved with primary evidence.

## Codex-Native Structure

This edition uses Codex's own loading and packaging mechanisms:

- `.codex-plugin/plugin.json` declares a skills-only plugin.
- `.agents/plugins/marketplace.json` makes the repository installable as a Codex marketplace source.
- top-level `skills/` is the plugin payload; each workflow keeps detailed procedures in its own `references/` directory and output templates in `assets/`.
- `custom-instructions/global-coding-agent-instructions.md` contains only durable always-on behavior and routes situational procedures to skills.
- `agents/*.toml` remains an optional set of personal custom-agent profiles installed by the companion scripts.

The repository intentionally does not duplicate `skills/` under `.agents/skills`. Installing the same skill through both plugin and repository discovery could produce duplicate selectors and two independently updated copies.

Codex discovers `AGENTS.md` files through its directory walk; it does not provide an import directive between instruction files. The optional global installer therefore maintains one small, clearly marked section in the user's global file while the plugin carries procedural material on demand.

Current Codex documentation gives the discovered project instruction chain a default 32 KiB `project_doc_max_bytes` ceiling. This package keeps its optional global contribution small, but maintainers should still account for repository and directory-level instructions that Codex layers for a task.

No lifecycle hooks are included. The current companion setup is a user-invoked install/update operation, so a hook would add enforcement and side effects without replacing a real lifecycle requirement.

## What's Inside

| Area | Path | Purpose |
| --- | --- | --- |
| Plugin manifest | `.codex-plugin/plugin.json` | Declares the Codex skills package. |
| Repository marketplace | `.agents/plugins/marketplace.json` | Makes this repository addable as a Codex marketplace source. |
| Skills | `skills/` | Native invocable workflows with progressively disclosed references and assets. |
| Optional global guidance | `custom-instructions/` | Lean durable behavior installed only when requested. |
| Optional custom agents | `agents/` | Terra and Luna profiles for planning, engineering, review, testing, and documentation. |
| Companion installers | `install/` | Manage only the optional global section and personal custom agents. |
| Public evidence | `docs/evidence/` | Reproducible benchmark and run-record format. |
| Repository guidance | `AGENTS.md` | Instructions for maintaining this public playbook. |

## Skill Map

| Skill | Use it for | Detailed content |
| --- | --- | --- |
| `$subagent-orchestration` | Bounded delegation, routing, ownership, and acceptance | `skills/subagent-orchestration/references/` |
| `$task-graph-orchestration` | Genuine dependencies, fan-out, fan-in, and approval gates | `skills/task-graph-orchestration/references/` |
| `$worktree-lifecycle` | Justified auxiliary worktrees and safe disposition | `skills/worktree-lifecycle/references/` |
| `$multi-session-coordination` | Related work across independent Codex tasks | `skills/multi-session-coordination/references/` |
| `$reference-doc-routing` | Selecting authoritative context and reusable repo-doc templates | `skills/reference-doc-routing/references/` and `assets/templates/` |
| `$senior-code-review` | Independent final review | `skills/senior-code-review/SKILL.md` |
| `$install-coding-agent-playbook` | Optional global guidance and personal custom agents | `skills/install-coding-agent-playbook/SKILL.md` |

### Repo-specific guidance

Copy and adapt the repository instruction template when starting a project:

```text
skills/reference-doc-routing/assets/templates/repository-AGENTS.md
```

Fill in the real build commands, test commands, architecture rules, generated-file rules, and release expectations for that repository.

## Custom Agent Model

The optional `agents/` bundle provides Terra and Luna variants of five roles:

| Role | Responsibility |
| --- | --- |
| Planner | Bounded decomposition, risks, sequencing, and validation strategy |
| Engineer | Small, well-specified implementation |
| Reviewer | Evidence-backed correctness and scope review |
| Tester | Reproduction, test execution, failure analysis, and gap finding |
| Docs | Focused repository and authoritative documentation lookup |

Every TOML profile pins an explicit Codex model and `model_reasoning_effort`. The complete task-level routing policy lives only in [the subagent-orchestration references](./skills/subagent-orchestration/references/model-routing.md), where it is loaded when delegation is relevant.

## Task Graphs, Worktrees, and Parallel Tasks

Use `$task-graph-orchestration` for complex work with real dependency edges or substantial fan-out. Its workflow and reusable graph template live together under `skills/task-graph-orchestration/references/`.

Use `$worktree-lifecycle` before acting on an auxiliary worktree. Worktrees are isolation tools, not delegation units; the detailed creation, integration, preservation, and removal gates live under `skills/worktree-lifecycle/references/`.

Use `$multi-session-coordination` when independent Codex tasks may be changing shared contracts, files, schemas, dependencies, or user flows. The skill owns discovery coverage, change maps, conflict detection, ownership, sequencing, and integration verification. The former copy-paste coordination prompt is no longer needed.

## Why This Exists

AI coding agents often fail in predictable ways:

- coding before understanding the codebase
- over-engineering simple requests
- refactoring unrelated code
- trusting summaries instead of primary evidence
- claiming validation that did not run
- delegating vague work or blindly accepting delegated output
- allowing parallel changes to develop incompatible contracts
- loading every procedure into every task, whether relevant or not

This playbook makes the durable behavior small and routes situational mechanics through Codex skills.

## Developed Through Real-World Use

The Coding Agent Playbook grew out of ArcanEdge's day-to-day use of coding agents on real software engineering work, not synthetic prompting exercises. ArcanEdge uses these patterns while developing production systems, including work supporting [United Tradesmen](https://www.arcanedge.ai/work/united-tradesmen), a live construction workforce and operations platform, as well as unreleased internal products.

Client and unreleased-product repositories remain private. [ArcanEdge](https://www.arcanedge.ai/) and [United Tradesmen](https://unitedtradesmen.org/) provide the public context; this repository does not publish private source, implementation details, or internal engineering records.

## Public Evidence

[`docs/evidence/`](./docs/evidence/README.md) defines a compact benchmark and run-record format so outside developers can inspect prompts, routing, delegation, review, corrections, validation, and outcomes without private repository access.

[Benchmark 001](./docs/evidence/BENCHMARK-001.md) has one published measured record: [Benchmark 001 Run 001](./docs/evidence/BENCHMARK-001-RUN-001.md). Its fixture baseline is frozen at [`benchmark-001-baseline-v1`](https://github.com/ArcanEdge-AI/coding-agent-playbook-benchmarks/tree/benchmark-001-baseline-v1) and [exact commit](https://github.com/ArcanEdge-AI/coding-agent-playbook-benchmarks/commit/2a7244f0106cf7f4e106a832b737028144d28389). The evidence framework makes results inspectable; it does not claim universal cost, token, speed, or quality advantages.

## Harness Editions

Coding Agent Playbook ships as separate harness-native editions. This repository is the Codex edition. The companion [Claude Code edition](https://github.com/ArcanEdge-AI/coding-agent-playbook-claude-code) carries the same engineering principles through that harness's documented mechanisms.

## Repository Structure

```text
.
├── .agents/plugins/marketplace.json
├── .codex-plugin/plugin.json
├── AGENTS.md
├── CONTRIBUTING.md
├── INSTALL.md
├── LICENSE
├── README.md
├── agents/
│   ├── docs.toml
│   ├── docs-luna.toml
│   ├── engineer.toml
│   ├── engineer-luna.toml
│   ├── planner.toml
│   ├── planner-luna.toml
│   ├── reviewer.toml
│   ├── reviewer-luna.toml
│   ├── tester.toml
│   └── tester-luna.toml
├── assets/
├── custom-instructions/
│   └── global-coding-agent-instructions.md
├── docs/evidence/
├── install/
│   ├── install.ps1
│   └── install.sh
└── skills/
    ├── install-coding-agent-playbook/
    ├── multi-session-coordination/
    ├── reference-doc-routing/
    ├── senior-code-review/
    ├── subagent-orchestration/
    ├── task-graph-orchestration/
    └── worktree-lifecycle/
```

Each skill owns its detailed references and assets. There is no separate top-level reference tree or copy-paste prompt directory.

## Contributing

Keep contributions generic, reusable, safe for public use, and aligned with current Codex documentation. Do not add private project details, internal URLs, sensitive access material, local machine quirks, or one-off incident logs. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT © 2026 ArcanEdge AI. See [LICENSE](./LICENSE).

## Status

This is a living playbook. Treat it as a strong baseline, not a universal law:

```text
Lean global behavior + on-demand skills + local repository truth + evidence-backed validation
```
