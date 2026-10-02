# Repository Coding Agent Instructions

This repository is a public playbook for Codex custom instructions, reference documents, skills, and custom subagent definitions.

Repository-specific guidance overrides the global instructions where it is more specific.

## Repository Goals

- Keep the playbook useful for many teams and codebases.
- Keep global guidance tool-agnostic and durable.
- Keep repository-specific, machine-specific, and workflow-specific details out of global instructions.
- Prefer concise, practical guidance over long theory.
- Make the main agent accountable for planning, any delegation it chooses, validation, and final reporting.
- Keep the Codex subagent model aligned around `planner`, `engineer`, `reviewer`, `tester`, and `docs`.
- Use subagents sparingly, only when their concrete benefit justifies context, coordination, and review costs or an independent-assistance requirement applies.
- Give every bundled profile an explicit approved model and reasoning default. Select actual delegated routes by task: GPT-6.1 Sol at Light, Medium, or High, or GPT-6 Astra at Extra High; use Standard speed only, not Fast. Light uses `low` in configuration. Preserve the main agent's user-selected configuration.
- Keep the default delegation structure flat: root assigns bounded work directly, and bundled helpers do not spawn descendants.
- Subagent progress and result messages must preserve parent and peer settings; never attach worker model or reasoning overrides to reports.
- Keep one profile per bundled role under its standard name. Defaults do not replace task-based selection, and profile precedence must not silently override the chosen route.
- Separate reusable role perspectives from delegated-execution rules. Direct main-agent use preserves its configuration, authority, and ownership and does not count as independent verification.

## Content Rules

- Do not include sensitive access material, private local paths, internal-only URLs, full thread transcripts, or long incident logs.
- Do not hardcode project names, organization-specific workflows, or local machine quirks in global guidance.
- Do not add instructions tied to a specific issue tracker, review tool, package manager, shell, or hosting provider unless the file is explicitly an example or template.
- Use Codex terminology, paths, TOML agent schemas, model identifiers, reasoning-effort fields, and thread concepts in Codex-specific files.
- Do not copy configuration paths, file names, agent formats, model identifiers, or command vocabulary from another coding-agent environment into this repository.
- Prefer terms like "safety", "access control", and "sensitive access material" when public documentation does not need product-specific terminology.
- Keep templates reusable and clearly marked as templates.
- Treat the companion Claude Code playbook as independently maintained. Do not edit it from this repository or claim current parity without separately verified evidence.

## Validation

This repo is mostly Markdown and TOML. Before finalizing meaningful changes:

- Review Markdown headings and fenced code blocks for correctness.
- Confirm TOML files are syntactically valid when a TOML parser is available.
- Confirm every `agents/*.toml` file explicitly defines `model` and `model_reasoning_effort`.
- Confirm each of the five bundled roles has one profile under its standard name, with an explicit model/effort pair from the approved task-routing table and no Fast selection (`service_tier = "fast"` or `"priority"`).
- Confirm profiles retain clear scope and stop conditions; helpers report route issues, and only the main agent may reassign within approved routes and execution authority.
- Confirm helper-specific scope, escalation, reporting, and launch settings apply only to delegated execution; direct role use adds no mandatory sequence or separate reports.
- Confirm reporting guidance uses team messages or normal returns and omits destination-setting overrides from any separately authorized task report.
- Confirm each `SKILL.md` has YAML frontmatter with `name` and `description`.
- Confirm links and paths in `README.md` match the repository tree.
- Confirm install docs and scripts reference the current Codex agent files; installed-profile validation checks the current managed profiles without imposing playbook routing on unrelated user agents.
- Confirm the Python installer and thin PowerShell/Bash launchers default normal installs and updates to full mode, create a marked global section on first install, maintain the managed-file manifest, retire only unchanged formerly managed files, and preserve customized or unrelated files.
- Confirm installer validation covers `skills/worktree-lifecycle/references/worktrees.md`, `skills/worktree-lifecycle/references/templates/worktree-manifest.md`, and every skill-local resource path.
- Confirm the feature-branch lifecycle remains a self-contained skill, detects repository-specific branch names, preserves approval gates for remote deletion and production promotion, and is not conflated with worktree lifecycle.
- Confirm legacy-path retirement requires dependency evidence or explicit retention requirements, separates code retirement from data disposal, preserves correctness safeguards, and does not treat uncertain dependency coverage as permission to remove behavior.
- Confirm design guidance reviews the whole affected flow, improves existing implementations by default, and requires evidence of significant benefit before a substantial replacement.
- Confirm testing guidance favors the smallest meaningful checks and lasting tests for intended final behavior and realistic regression risks, removes only obsolete intermediate tests, and preserves required assertions and repository gates.
- Keep Codex policy internally consistent and document Codex-specific capability assumptions where they affect behavior.
- Search the final diff for paths, schemas, model names, and commands that belong to another coding-agent environment; remove any accidental contamination before merging.

## License

This repository is MIT licensed. See `LICENSE`. Do not change the license without an explicit maintainer decision.
