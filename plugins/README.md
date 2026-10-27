# Companion marketplace plugin

Use the maintained Codex marketplace release of **Intuitive Software Design** alongside this playbook. The Python installer manages the playbook's standalone skills and five agents; the Codex plugin manager manages this companion separately.

| Field | Value |
| --- | --- |
| Name | Intuitive Software Design |
| Publisher | ArcanEdge AI |
| Canonical plugin selector | `intuitive-software-design@openai-curated-remote` |
| Verified marketplace version | 1.3.1 on 2026-10-27 |
| Source | [ArcanEdge-AI/intuitive-software-design](https://github.com/ArcanEdge-AI/intuitive-software-design) |
| License | Apache-2.0; retained by the marketplace package |

The marketplace plugin supplies these eight skills:

- `intuitive-software-design`
- `purpose-first-redesign`
- `user-task-walkthrough`
- `product-mental-model`
- `decision-support-design`
- `multi-role-workflow`
- `connected-experience-design`
- `behavioral-evaluation`

## Install and verify

In Codex, open the plugin marketplace, find **Intuitive Software Design** by ArcanEdge AI, and install or enable that release. Reuse it when it is already available.

On a Codex CLI version that supports the plugin subcommands, use:

```text
codex plugin list --marketplace openai-curated-remote --json
codex plugin add intuitive-software-design@openai-curated-remote
```

Check the actual installed row's plugin ID, version, installed state, and enabled state. A cached directory alone does not prove installation. A newer marketplace release may supersede the verified version above; do not install an older local snapshot merely to match it. The [official skills and plugins guidance](https://learn.chatgpt.com/docs/skills-and-plugins?surface=cli) describes the supported product surfaces.

Keep the marketplace package as the source of truth. This repository does not vendor another copy of its eight skills or register a replacement local plugin. Report account, catalog, connection, or host limitations as incomplete companion setup rather than claiming that the Python installer verified them.

## Retire an older local installation

Only when the user authorizes removal of that exact installation, verify the marketplace release is installed and enabled, then use the supported plugin manager. For the older local registration:

```text
codex plugin remove intuitive-software-design@local
```

Verify the exact local entry is gone and the marketplace release remains enabled. Do not remove other variants or unrelated plugins. Preserve customized source before retiring a local cache. Do not remove a local installation automatically just because a marketplace release exists.
