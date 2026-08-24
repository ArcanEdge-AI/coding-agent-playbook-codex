# Install Coding Agent Playbook — Codex Edition

Install the Codex plugin first. The plugin is the canonical package for skills, detailed references, and reusable templates.

## 1. Add the Marketplace and Install the Plugin

Register this repository as a Codex marketplace source:

```text
codex plugin marketplace add ArcanEdge-AI/coding-agent-playbook-codex
```

Then open the Codex app's Plugins UI and install **Coding Agent Playbook — Codex Edition**.

The repository marketplace points at the repository root, whose `.codex-plugin/plugin.json` declares `skills/` as the plugin payload. Do not copy that tree into `.agents/skills` or another user skill directory; parallel discovery of the same skills can create duplicate selectors and independently updated copies.

After installation, start a new Codex task if the skills do not appear immediately. Invoke a skill with `$skill-name` or browse `/skills`.

## 2. Optional Companion Configuration

The plugin schema does not currently document bundling personal custom-agent TOMLs or modifying a user's global `AGENTS.md`. This repository therefore retains small companion installers for only those optional targets:

```text
$CODEX_HOME/
  AGENTS.md                                      # full mode only; one marked section
  .coding-agent-playbook-codex-managed-files.tsv
  agents/
    planner.toml
    planner-luna.toml
    engineer.toml
    engineer-luna.toml
    reviewer.toml
    reviewer-luna.toml
    tester.toml
    tester-luna.toml
    docs.toml
    docs-luna.toml
```

Path resolution:

- `CODEX_HOME`: use `$CODEX_HOME` when set, otherwise the user's `.codex` directory.
- `USER_SKILLS_HOME`: recognized only to locate legacy playbook-managed skill files during a manifest-backed migration; no skills are installed there now.

Invoke `$install-coding-agent-playbook` after installing the plugin, or run the scripts directly as described below.

### Full mode

Full mode is the default. It installs or updates:

- the lean global behavior from `custom-instructions/global-coding-agent-instructions.md` inside one marked section of `$CODEX_HOME/AGENTS.md`
- the ten personal custom-agent TOMLs under `$CODEX_HOME/agents/`
- the managed-file manifest, which now contains only the custom-agent files

Existing content outside the marked section is preserved. Re-running full mode replaces that section instead of appending a duplicate.

Codex loads a non-empty `$CODEX_HOME/AGENTS.override.md` instead of the sibling `AGENTS.md`. When that override is present, full mode stops before making changes rather than reporting inactive global guidance as installed. Reconcile or remove the override first, or use support-only mode when only the custom agents are wanted.

### Support-only mode

Use support-only mode only when the user explicitly wants the custom agents without this playbook's global instruction section.

Support-only mode:

- installs or updates the custom-agent TOMLs
- removes an existing current or legacy playbook-owned section from `$CODEX_HOME/AGENTS.md`
- preserves all unrelated global content
- fails closed when markers are duplicated, incomplete, reversed, or otherwise malformed

Support-only mode does not add a pointer section. The plugin already exposes the situational workflows natively.

## Preview, Then Install

Inspect the dry-run output before allowing the companion installer to write.

### macOS, Linux, or WSL

```bash
git clone https://github.com/ArcanEdge-AI/coding-agent-playbook-codex.git
cd coding-agent-playbook-codex
bash install/install.sh --full --dry-run
bash install/install.sh --full
```

Explicit support-only mode:

```bash
bash install/install.sh --support-only --dry-run
bash install/install.sh --support-only
```

### Windows PowerShell

```powershell
git clone https://github.com/ArcanEdge-AI/coding-agent-playbook-codex.git
cd coding-agent-playbook-codex
pwsh -ExecutionPolicy Bypass -File install/install.ps1 -Full -DryRun
pwsh -ExecutionPolicy Bypass -File install/install.ps1 -Full
```

Explicit support-only mode:

```powershell
pwsh -ExecutionPolicy Bypass -File install/install.ps1 -SupportOnly -DryRun
pwsh -ExecutionPolicy Bypass -File install/install.ps1 -SupportOnly
```

## Backups, Ownership, and Legacy Retirement

The companion installers back up an existing target before changing it. Backups use a timestamped `.bak.<timestamp>` suffix beside the original file.

The managed-file manifest records each current custom-agent file and its repository SHA-256. During later updates:

- current files are replaced with backups when content changes
- files removed from the current bundle are retired only when they still match the previously recorded hash
- customized formerly managed files are preserved with a warning
- files never recorded as playbook-managed are not removed

Previous releases managed `references`, `skills`, and `agents` roots. The installers continue to recognize all three roots while reading an existing current or legacy manifest. This allows unchanged obsolete reference and skill copies to be backed up and retired during the transition to plugin ownership. Customized legacy copies remain in place for manual reconciliation.

If no previous manifest establishes ownership, existing unlisted files are preserved. An older `.codex-agent-playbook-managed-files.tsv` is migrated after a successful update.

## Validation Checklist

After plugin installation, verify in the Codex app that:

- the plugin is installed from the registered marketplace
- `$install-coding-agent-playbook` and the six engineering workflow skills are available
- invoking `/skills` does not show a second manually copied set from this playbook

After a companion install, verify:

- full mode has exactly one current marker pair in `$CODEX_HOME/AGENTS.md`
- full mode stopped without changes if a non-empty `$CODEX_HOME/AGENTS.override.md` would take precedence
- support-only mode has neither current nor legacy playbook markers
- `$CODEX_HOME/.coding-agent-playbook-codex-managed-files.tsv` exists and lists each current `agents` file once
- all ten expected `$CODEX_HOME/agents/*.toml` files exist
- every installed agent TOML parses and defines `model` plus `model_reasoning_effort`
- every manifest entry matches its repository source SHA-256
- every formerly managed path is absent, retired unchanged with a backup, or preserved with an explicit customization warning

Restart Codex or open a new task when updated instructions, skills, or custom agents are not visible in the current task.

## Removal

Remove the plugin through the Codex app's Plugins UI. That removes the plugin-provided skills and references as one package.

For companion configuration, remove only the playbook-owned targets:

1. Edit `$CODEX_HOME/AGENTS.md` and remove the section between the `coding-agent-playbook-codex` start and end markers, if present.
2. Delete the ten named playbook agent TOMLs listed in this guide, after confirming they are still playbook-owned rather than customized replacements.
3. Delete `$CODEX_HOME/.coding-agent-playbook-codex-managed-files.tsv` after the managed files have been reconciled.

Do not delete the entire `$CODEX_HOME/agents`, `$CODEX_HOME/references`, or user skill directory; those locations may contain unrelated or customized files.

## Lifecycle Hooks

This package intentionally installs no hooks. Plugin installation and companion configuration are explicit user-invoked operations, and the current scripts do not implement a background lifecycle behavior that warrants a hook.
