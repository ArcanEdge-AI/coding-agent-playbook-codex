---
name: taste-redesign-website
description: Use when the user wants Taste's staged workflow to redesign an existing website, including brief questions or project autofill, a site audit, an approved modernization plan, protected content, and written design audits.
---

Run the existing-website workflow from the Taste Skill prompt guide. Use the installed `design-taste-frontend` skill as the source of design rules for this task. Resolve the sibling `design-taste-frontend/SKILL.md` beside this installed skill. If the dependency is missing, report it before starting the design workflow. Follow governing instructions and the user's project constraints.

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

Run the Taste Section 11.B audit and report it in writing:

- Current brand tokens: primary and accent colors, typography stack, and radii.
- Information architecture: page tree, navigation, and conversion paths.
- Patterns to preserve: signature interactions, recognizable hero treatment, and copy voice.
- Patterns to retire: generic design patterns, broken layouts, and dead links.
- Current DESIGN_VARIANCE, MOTION_INTENSITY, and VISUAL_DENSITY readings.
- SEO baseline: relevant pages, titles, and anchors; state which ranking information is unverified.

Stop and request the user's approval before proposing the next stage. Keep this stage read-only.

## Step 2: Propose the mode after audit approval

Declare Preserve, Overhaul, or Greenfield-with-content-preserved. List the modernization levers from Taste Section 11.D in priority order. Identify any proposed exception to the preservation rules below so the user can approve that specific change.

Stop and request the user's approval of this plan. Audit approval alone does not approve implementation.

## Step 3: Implement after plan approval

Apply the approved plan. Preserve URL structure, primary navigation labels, form field names, brand logo, and legal copy unless the user explicitly approves a particular change. Preserve the brief's protected headings and anchors. Do not infer permission to change these from a general choice of Overhaul.

## Step 4: Verify

Report each audit in writing:

- Dash audit: zero U+2014 em dashes or U+2013 en dashes in the produced content.
- Taste Pre-Flight Check, Section 14: mark every item Pass or Fail with a one-line justification tied to observed evidence.
- Preservation audit: list every changed URL, navigation label, form field, and anchor. The list must be empty except for explicitly approved changes. Also check protected headings, the brand logo, and legal copy.
- Brand fidelity audit: confirm the existing accent color, typography stack, and logo treatment survived, or identify each explicitly approved exception.

Any Fail prevents completion. Correct in-scope failures and rerun the affected checks, or report the specific blocker. Do not mark an unverified item Pass.

Source: [Taste Skill prompt guide](https://www.tasteskill.dev/guide), captured 2026-10-06. This skill adds interactive intake and optional project autofill to the guide's redesign workflow.
