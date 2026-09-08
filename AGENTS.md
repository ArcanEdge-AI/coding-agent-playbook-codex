# Repository Coding Agent Instructions

This repository is a public playbook for Codex custom instructions, reference documents, skills, and custom subagent definitions.

Repository-specific guidance overrides the global instructions where it is more specific.

## Repository Goals

- Keep the playbook useful for many teams and codebases.
- Keep global guidance tool-agnostic and durable.
- Keep repository-specific, machine-specific, and workflow-specific details out of global instructions.
- Prefer concise, practical guidance over long theory.
- Make the main agent accountable for planning, delegation, validation, and final reporting.
- Keep the Codex subagent model aligned around `planner`, `engineer`, `reviewer`, `tester`, and `docs`.
- Keep every custom subagent pinned to an explicit `gpt-5.6-luna` model and `max` reasoning effort so it does not inherit the main session model unintentionally.
- Require every subagent execution, including nested execution, retries, and replacements, to use `gpt-5.6-luna` with `max` reasoning, independently of the root model or effort.
- Subagent progress and result messages must preserve parent and peer settings; never attach worker model or reasoning overrides to reports.
- Preserve base and `-luna` role names as compatible profiles; every bundled profile uses Luna/max.

## Content Rules

- Do not include sensitive access material, private local paths, internal-only URLs, full thread transcripts, or long incident logs.
- Do not hardcode project names, organization-specific workflows, or local machine quirks in global guidance.
- Do not add instructions tied to a specific issue tracker, review tool, package manager, shell, or hosting provider unless the file is explicitly an example or template.
- Use Codex terminology, paths, TOML agent schemas, model identifiers, reasoning-effort fields, and thread concepts in Codex-specific files.
- Do not copy configuration paths, file names, agent formats, model identifiers, or command vocabulary from another coding-agent environment into this repository.
- Prefer terms like "safety", "access control", and "sensitive access material" when public documentation does not need product-specific terminology.
- Keep templates reusable and clearly marked as templates.
- Keep generic behavioral policy aligned with the companion Claude Code playbook. When a difference is intentional, document the concrete harness capability that requires it instead of preserving unexplained drift.

## Validation

This repo is mostly Markdown and TOML. Before finalizing meaningful changes:

- Review Markdown headings and fenced code blocks for correctness.
- Confirm TOML files are syntactically valid when a TOML parser is available.
- Confirm every `agents/*.toml` file explicitly defines `model` and `model_reasoning_effort`.
- Confirm every bundled role retains its base and `-luna` profiles and all profiles explicitly set `model = "gpt-5.6-luna"` and `model_reasoning_effort = "max"`.
- Confirm profiles include clear stop and escalation conditions without model substitution.
- Confirm reporting guidance uses team messages or normal returns and omits destination-setting overrides from any separately authorized task report.
- Confirm each `SKILL.md` has YAML frontmatter with `name` and `description`.
- Confirm links and paths in `README.md` match the repository tree.
- Confirm install docs and scripts reference the current Codex agent files.
- Confirm PowerShell and Bash installers default normal installs and updates to full mode, create a marked global section on first install, maintain the managed-file manifest, retire only unchanged formerly managed files, and preserve customized or unrelated files.
- Confirm installer validation lists include `references/worktrees.md`, `references/templates/worktree-manifest.md`, and `skills/worktree-lifecycle/SKILL.md`.
- Compare generic policy changes with the companion Claude Code playbook and either align them or record the concrete harness-specific reason for divergence.
- Search the final diff for paths, schemas, model names, and commands that belong to another coding-agent environment; remove any accidental contamination before merging.

## License

This repository is MIT licensed. See `LICENSE`. Do not change the license without an explicit maintainer decision.
