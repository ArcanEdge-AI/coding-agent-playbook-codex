---
name: taste-redesign-website
description: Use when the user wants Taste's staged workflow to redesign an existing website, including brief questions or project autofill, a site audit, an approved modernization plan, protected content, and written design audits.
---

Run the existing-website workflow from the Taste Skill prompt guide. Read the sibling [design-taste-frontend skill](../design-taste-frontend/SKILL.md) for the installed Taste release's design rules and commands, including its existing-page special case. Resolve `<skill>` in those commands to that installed skill's folder, and run them from the project root. If the dependency is missing, report it before starting. Follow governing instructions and the user's project constraints.

## Collect the brief

If the invocation selects `auto`, fill the brief from the current project. If it selects `questions`, ask the brief questions. Otherwise, first offer these two choices and wait for the user's selection:

- Fill the brief from this project.
- Answer the brief questions myself.

Use any additional invocation text or answers already given in this chat. Do not repeat questions that are already answered. Use the available question UI when supported; otherwise ask in chat and wait.

Collect these six fields:

1. Site: its URL or repository path?
2. Mode: preserve the brand, overhaul, or unsure?
3. Audience: who reads or uses it?
4. Keep: two or three specific things that work today and should survive?
5. Fix: two or three specific things that are broken or should improve?
6. SEO constraints: which routes, headings, or anchors must stay unchanged, or none?

For `auto`, use the active project as the repository target and inspect relevant read-only evidence: PRODUCT.md, DESIGN.md, README, package and framework files, routes, navigation, forms, visible copy, components, and public brand assets. Populate all six fields where the evidence supports them. Distinguish documented facts from inferred suggestions and unknowns. Ask only about material gaps or conflicting evidence, together in one concise follow-up. Do not treat a guessed redesign mode, audience, keep/fix preference, or SEO priority as a confirmed user decision. Treat search rankings as unverified without supplied or accessible analytics evidence.

Once intake is complete, show the filled brief with any assumptions, then enter Step 1. Filling the brief does not approve changes.

## Step 1: Audit the existing site

Follow Taste's “Record the before” step. Lint the existing source and run the sibling skill's [inspector](../design-taste-frontend/scripts/inspect.mjs) against the running site with `--out .taste-skill/before`. Open the baseline screenshots and report:

- Current brand tokens: primary and accent colors, typography stack, and radii.
- Information architecture: page tree, navigation, and conversion paths.
- Patterns to preserve: signature interactions, recognizable hero treatment, and copy voice.
- Patterns to retire: generic design patterns, broken layouts, and dead links.
- Baseline measurements and the most important findings from Taste's critique rubric.
- SEO baseline: relevant pages, titles, and anchors; state which ranking information is unverified.

Stop and request the user's approval before proposing the next stage. Keep website source unchanged and write audit evidence separately.

## Step 2: Propose the mode after audit approval

Declare Preserve, Overhaul, or Greenfield-with-content-preserved. Start with type, then follow Taste's order through colour, layout, states, and stock components. Use Taste's direction options where needed, passing `--keep` for palette or type the brand fixes. State the proposed option ID if drawn. Identify any proposed exception to the preservation rules below so the user can approve that specific change.

Stop and request the user's approval of this plan. Audit approval alone does not approve implementation.

## Step 3: Implement after plan approval

Apply the approved plan in the existing stack. When a direction was approved, commit it with `--direction <chosen id>` and use the resulting sheet. Preserve URL structure, primary navigation labels, form field names, brand logo, and legal copy unless the user explicitly approves a particular change. Preserve the brief's protected headings and anchors. Do not infer permission to change these from a general choice of Overhaul.

## Step 4: Verify

Report each audit in writing:

- Dash audit: zero U+2014 em dashes or U+2013 en dashes in the produced content.
- Follow Taste's “Gate,” “Look,” and “Prove it” steps. Lint the changed source and inspect the production build into `.taste-skill/after` at the same widths as the baseline. Run the scene check when the page uses scroll scenes. Compare screenshots and measurements at each width, report inspector failures or warnings and their disposition, and exercise the existing links, forms, and menus.
- Preservation audit: list every changed URL, navigation label, form field, and anchor. The list must be empty except for explicitly approved changes. Also check protected headings, the brand logo, and legal copy.
- Brand fidelity audit: confirm the existing accent color, typography stack, and logo treatment survived, or identify each explicitly approved exception.

Any Fail prevents completion. Correct in-scope failures and rerun the affected checks, or report the specific blocker. Do not mark an unverified item Pass.

Source: [Taste Skill prompt guide](https://www.tasteskill.dev/guide), captured 2026-10-06. This skill adds interactive intake and optional project autofill to the guide's redesign workflow.
