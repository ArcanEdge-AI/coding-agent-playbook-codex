---
name: handoff
description: Start a new Codex chat with the complete material context from the current work when the user asks for a handoff, a fresh continuation chat, or everything worked on, researched, explored, validated, and verified.
---

# Handoff

Move the current work into a new chat without losing decisions, evidence, failures, workspace state, or the real next gate. When Codex app thread tools are available, actually create, verify, and open the new chat; do not stop at drafting a prompt.

The request to start a new chat authorizes thread creation, context seeding, titling, and navigation. It does not authorize code changes, merge, deployment, external publication, cloud mutation, destructive cleanup, or continuing the underlying project work.

## Establish Current Truth

Before composing the handoff:

1. Treat the completed conversation, repository, connected services, memory, and user statements as distinct evidence sources.
2. Recheck cheap drift-prone facts that materially affect the next chat: repository path, branch/ref, commit, upstream, dirty state, PR/check/review status, deployment state, active worktree, and relevant external access state.
3. Preserve the distinction between verified current, user-reported, historical, and unverified facts. Never upgrade source changes, a merge, or prior test output into deployed acceptance.
4. Preserve unrelated local work. Record dirty or user-owned paths without cleaning, resetting, moving, staging, or overwriting them.

Read [references/context-contract.md](references/context-contract.md) before assembling the context package.

## Build the Context Package

Include all material context needed to continue correctly, not a transcript dump. Capture:

- the objective and current verdict;
- work completed and its exact artifacts;
- research, experiments, alternatives, and causal findings;
- validations run, exact outcomes, warnings, and evidence boundaries;
- user decisions, approvals, rejected approaches, and non-negotiable invariants;
- repository, worktree, branch, PR, release, and external-system anchors;
- failures, dead ends, pre-existing defects, and why they were classified that way;
- unresolved risks, missing evidence, and the precise next gate;
- authorization boundaries and actions the new chat must not infer.

Use exact file paths, identifiers, commits, PRs, run IDs, test counts, and evidence locators when they materially prevent rediscovery or mistakes. Remove repetition and conversational noise. Never include credentials, tokens, private keys, session cookies, sign-in links, device codes, secret values, customer prose, or unnecessary sensitive payloads.

## Create the New Chat

Create a fresh chat with a self-contained context package. A fork carries prior history and is not a fresh handoff. Use this order:

1. **Select the project safely:** List projects first and match the current repository by exact path. For a Git project, default to a worktree. Use an existing branch/ref only when it is the verified active scope; use working-tree state only when the handoff must include current uncommitted files; otherwise use the project's default branch. Never invent a branch.
2. **Create the thread:** Seed a fresh project thread with the complete context package and a clear next gate.
3. **Handle asynchronous creation:** A create action may return a `clientThreadId` while setup is pending. Never pass it to a tool that requires a real `threadId`. Poll/list threads and identify the new one from its requested title, project, path, creation time, and summary. Avoid creating a duplicate while setup is in progress.
4. **Title and open it:** Give the thread a short, unambiguous title, then navigate the app to that thread.

If no thread-creation capability exists, provide one self-contained copy-paste prompt and say clearly that the chat was not created. Create a workspace handoff file only when the user requests one or when a durable artifact is necessary and the destination is safe.

## Verify the Handoff

Do not claim success from a create response alone.

- Read the new thread and confirm the context prompt is present.
- Confirm the thread has a real `threadId`, expected workspace/project, and requested title.
- Confirm it is active, ready, or has produced its acknowledgement.
- Ensure the new prompt tells the next agent to recheck live state before acting.
- Ensure no underlying merge, deployment, report launch, cloud mutation, publication, or destructive action started automatically.
- Do not archive or delete the source thread unless the user separately asks.

Finish with a concise confirmation naming the new thread and its ID.
