# Install Coding Agent Playbook — Codex Edition

This file is written for both humans and AI coding agents.

The intended experience is:

```text
Install this repo into my Codex setup:
https://github.com/ArcanEdge-AI/coding-agent-playbook-codex

Follow INSTALL.md. Use full install unless I explicitly ask for support-only mode.
Preserve my existing files with backups and report exactly what changed.
```

## What Gets Installed

A full install creates or updates this user-level structure:

```text
$CODEX_HOME/
  AGENTS.md
  .coding-agent-playbook-codex-managed-files.tsv
  agents/
    planner.toml
    engineer.toml
    reviewer.toml
    tester.toml
    docs.toml

$CODEX_HOME/skills/
  subagent-orchestration/
    SKILL.md
    references/
      model-routing.md
      subagents.md
  task-graph-orchestration/
    SKILL.md
    references/templates/task-graph.md
  worktree-lifecycle/
    SKILL.md
    references/
      worktrees.md
      templates/worktree-manifest.md
  feature-branch-lifecycle/
    SKILL.md
    references/
      branching-rule.md
  legacy-path-retirement/SKILL.md
  handoff/
    SKILL.md
    agents/openai.yaml
    references/context-contract.md
  session-cleanup/
    SKILL.md
    agents/openai.yaml
    references/post-session-cleanup-methodology.md
  multi-session-coordination/
    SKILL.md
    references/
      multi-session-coordination.md
      templates/active-work-record.md
  reference-doc-routing/
    SKILL.md
    references/
      README.md
      engineering-design.md
      reference-doc-routing.md
      templates/
        *.md
  senior-code-review/SKILL.md
```

Path resolution:

- `CODEX_HOME`: use `$CODEX_HOME` if set, otherwise `~/.codex`.
- `USER_SKILLS_HOME`: use `$CODEX_HOME/skills` unless explicitly overridden.
- On Windows, resolve equivalent user-home paths safely.

## Install Modes

### Full install

Use this for normal installs and every normal update. It is the default when no mode flag is provided.

Full install:

- installs the global coding-agent instructions into `$CODEX_HOME/AGENTS.md`
- copies custom agent definitions into `$CODEX_HOME/agents/`
- copies complete, self-contained skill packages into `$CODEX_HOME/skills/`

The global instruction body is always installed inside one clearly marked Coding Agent Playbook — Codex Edition section. Existing content outside that section is preserved. Re-running a full install replaces the existing marked section instead of appending a duplicate.

After a successful run, the installer writes `$CODEX_HOME/.coding-agent-playbook-codex-managed-files.tsv` with every managed support-file path and source SHA-256. On later runs, files removed from the repository are backed up and retired only when they still match the previously installed hash. Customized formerly managed files are preserved and reported. Files that were never recorded as playbook-managed are never removed. An existing `.codex-agent-playbook-managed-files.tsv` is migrated automatically after a successful update.

When `USER_SKILLS_HOME` is not explicitly set, an update also migrates previously managed skill files from the former `$HOME/.agents/skills` default. Exact hash matches are backed up and retired after the new `$CODEX_HOME/skills` packages are installed; customized legacy files are preserved with a warning.

The first manifest-aware update has no previous ownership record, so it safely preserves existing unlisted files. Subsequent updates can distinguish unchanged retired files from user customizations.

### Retired profile aliases

The duplicate `*-luna.toml` profiles have been removed. Use `planner`, `engineer`, `reviewer`, `tester`, and `docs`; these profiles now carry reusable role perspectives and explicit task-appropriate defaults. See the [routing policy](skills/subagent-orchestration/references/model-routing.md) for approved model/effort pairs, Standard-speed requirements, and profile precedence. Update any custom prompts or configuration that select a corresponding `*_luna` name or `*-luna.toml` path to use the standard role name or file.

The existing manifest cleanup backs up and retires unchanged managed copies during an update. Customized or unlisted copies remain for manual review. The installer does not rewrite custom prompts or configuration; review those references before removing a preserved copy.

### Support-only install

Use this only when the user explicitly requests support-only mode and confirms that the full global instructions already live in Codex Personalization > Custom instructions. Do not infer support-only mode merely because an older installation or an existing `AGENTS.md` is present.

Support-only install:

- does not duplicate the full global instructions into `$CODEX_HOME/AGENTS.md`
- adds only a short reference-map pointer if useful
- still copies self-contained skills and custom agent definitions
- still updates the managed-file manifest and safely retires unchanged files removed from later playbook releases

## Human Install

Clone the repository and run the standard-library Python installer. It requires Python 3.8 or newer and no third-party packages. The PowerShell and Bash files are thin compatibility launchers that locate Python and run the same implementation.

### macOS / Linux / WSL

```bash
git clone https://github.com/ArcanEdge-AI/coding-agent-playbook-codex.git
cd coding-agent-playbook-codex
python3 install/install.py --full
```

Support-only mode:

```bash
python3 install/install.py --support-only
```

### Windows

```powershell
git clone https://github.com/ArcanEdge-AI/coding-agent-playbook-codex.git
cd coding-agent-playbook-codex
py -3 install/install.py --full
```

Support-only mode:

```powershell
py -3 install/install.py --support-only
```

## Agent Install Instructions

When an AI coding agent is asked to install this repo, it should:

1. Clone or fetch the repository from the provided URL.
2. Read this `INSTALL.md` file first.
3. Resolve `CODEX_HOME` and `USER_SKILLS_HOME`.
4. Inspect existing target files before writing.
5. Back up any existing file before changing it.
6. Use full install for both installation and update unless the user explicitly asks for support-only mode. Existing global instructions, markers, or support files are not permission to change modes.
7. Copy self-contained skills and custom agent definitions to the expected user-level locations.
8. Validate the installed files.
9. Report exactly what changed, what was skipped, and where backups were written.

Do not modify arbitrary repositories during installation. Only use a temporary clone of this repository and user-level Codex configuration locations.

## Validation Checklist

After installation, verify:

- `$CODEX_HOME/AGENTS.md` exists or was intentionally left as a pointer-only file.
- `$CODEX_HOME/.coding-agent-playbook-codex-managed-files.tsv` exists and lists every current managed support file once.
- `$CODEX_HOME/skills/reference-doc-routing/references/engineering-design.md` exists.
- `$CODEX_HOME/skills/reference-doc-routing/references/templates/repository-AGENTS.md` exists.
- `$CODEX_HOME/skills/reference-doc-routing/references/reference-doc-routing.md` exists.
- `$CODEX_HOME/skills/subagent-orchestration/references/model-routing.md` exists.
- `$CODEX_HOME/skills/subagent-orchestration/references/subagents.md` exists.
- `$CODEX_HOME/skills/worktree-lifecycle/references/worktrees.md` exists.
- `$CODEX_HOME/skills/worktree-lifecycle/references/templates/worktree-manifest.md` exists.
- `$CODEX_HOME/skills/feature-branch-lifecycle/references/branching-rule.md` exists.
- `$CODEX_HOME/skills/multi-session-coordination/references/multi-session-coordination.md` exists.
- `$CODEX_HOME/skills/multi-session-coordination/references/templates/active-work-record.md` exists.
- `$CODEX_HOME/skills/task-graph-orchestration/references/templates/task-graph.md` exists.
- `$CODEX_HOME/agents/planner.toml` exists.
- `$CODEX_HOME/agents/engineer.toml` exists.
- `$CODEX_HOME/agents/reviewer.toml` exists.
- `$CODEX_HOME/agents/tester.toml` exists.
- `$CODEX_HOME/agents/docs.toml` exists.
- Every current playbook-managed `agents/*.toml` file explicitly defines `model` and `model_reasoning_effort`; unrelated user profiles are outside this validation scope.
- Installed reporting guidance preserves parent and peer task settings and omits destination-setting overrides from reports.
- Each of the five bundled roles has one profile under its standard name with an approved model/effort pair: `gpt-6.1-sol`/`low` (Light), `gpt-6.1-sol`/`medium`, `gpt-6.1-sol`/`high`, or `gpt-6-astra`/`xhigh` (Extra High). No bundled profile explicitly selects Fast; the validator rejects its `fast` and `priority` service-tier values.
- Standard speed must be established through the host at execution time. File validation does not prove the effective live speed, and the installer does not change the main agent's model, reasoning, or speed configuration.
- `$CODEX_HOME/skills/subagent-orchestration/SKILL.md` exists.
- `$CODEX_HOME/skills/task-graph-orchestration/SKILL.md` exists.
- `$CODEX_HOME/skills/worktree-lifecycle/SKILL.md` exists.
- `$CODEX_HOME/skills/feature-branch-lifecycle/SKILL.md` exists.
- `$CODEX_HOME/skills/legacy-path-retirement/SKILL.md` exists.
- `$CODEX_HOME/skills/handoff/references/context-contract.md` exists.
- `$CODEX_HOME/skills/session-cleanup/references/post-session-cleanup-methodology.md` exists.
- `$CODEX_HOME/skills/multi-session-coordination/SKILL.md` exists.
- Each `SKILL.md` has `name` and `description` frontmatter.
- Every local resource path referenced by a skill resolves inside that skill package.
- TOML agent files are parseable if a TOML parser is available.
- Every current manifest entry matches its repository source SHA-256.
- Every formerly managed path was either absent, backed up and retired unchanged, or preserved with an explicit customization warning.

## Uninstall

This project does not currently ship an automatic uninstall command.

To remove it manually, delete:

```text
$CODEX_HOME/.coding-agent-playbook-codex-managed-files.tsv
$CODEX_HOME/agents/planner.toml
$CODEX_HOME/agents/engineer.toml
$CODEX_HOME/agents/reviewer.toml
$CODEX_HOME/agents/tester.toml
$CODEX_HOME/agents/docs.toml
$CODEX_HOME/skills/subagent-orchestration/
$CODEX_HOME/skills/task-graph-orchestration/
$CODEX_HOME/skills/worktree-lifecycle/
$CODEX_HOME/skills/feature-branch-lifecycle/
$CODEX_HOME/skills/legacy-path-retirement/
$CODEX_HOME/skills/handoff/
$CODEX_HOME/skills/session-cleanup/
$CODEX_HOME/skills/multi-session-coordination/
$CODEX_HOME/skills/reference-doc-routing/
$CODEX_HOME/skills/senior-code-review/
```

If you used full install and want to remove the global instructions, edit `$CODEX_HOME/AGENTS.md` and remove the section between the Coding Agent Playbook — Codex Edition start/end markers.
