---
name: taste-new-website
description: Use when the user wants Taste's staged workflow for a new website, including brief questions or project autofill, design approval, a Next.js page, and written design audits.
---

Run the new-website workflow from the Taste Skill prompt guide. Use the installed `design-taste-frontend` skill as the source of design rules for this task. Resolve the sibling `design-taste-frontend/SKILL.md` beside this installed skill. If the dependency is missing, report it before starting the design workflow. Follow governing instructions and the user's project constraints.

## Collect the brief

If the invocation selects `auto`, fill the brief from the current project. If it selects `questions`, ask the brief questions. Otherwise, first offer these two choices and wait for the user's selection:

- Fill the brief from this project.
- Answer the brief questions myself.

Use any additional invocation text or answers already given in this chat. Do not repeat questions that are already answered. Use the available question UI when supported; otherwise ask in chat and wait.

Collect these six fields:

1. Page kind: landing page, portfolio, or marketing site?
2. Product: its name and a one-sentence description?
3. Audience: who will read or use it?
4. Vibe: two to four concrete adjectives, such as minimalist, editorial, or restrained?
5. References: actual URLs or product names that anchor the aesthetic, or none?
6. Avoid: specific patterns or visual choices to avoid, or none?

For `auto`, inspect relevant read-only project evidence: PRODUCT.md, DESIGN.md, README, package and framework files, existing routes, visible copy, components, and public brand assets. Populate all six fields where the evidence supports them. Distinguish documented facts from inferred suggestions and unknowns. Ask only about material gaps or conflicting evidence, together in one concise follow-up. Do not invent product claims, customers, references, or brand facts. An empty project still needs a brief from the user.

Once intake is complete, show the filled brief with any assumptions, then enter Step 1. Filling the brief does not approve implementation.

## Step 1: Design read

State the design direction in one sentence. State DESIGN_VARIANCE, MOTION_INTENSITY, and VISUAL_DENSITY, with a one-line explanation for each value.

Stop and request the user's approval of this direction. Do not create or edit the website before that approval. If the user changes the brief or direction, incorporate the change before proceeding.

## Step 2: Build after approval

Build one Next.js page with at least eight sections that fit the product. Use at least four different layout families across the page. Use real images: an available, authorized image-generation tool first, then seeded Picsum images if needed. Keep one consistent theme across the whole page.

## Step 3: Verify

Report each audit in writing:

- Dash audit: zero U+2014 em dashes or U+2013 en dashes in the produced content.
- Taste Pre-Flight Check, Section 14: mark every item Pass or Fail with a one-line justification tied to observed evidence.
- Section layout repetition: list the layout family of every section.
- Hero discipline: check headline line count, subtext word count, and whether the primary CTA is visible without scrolling.

Any Fail prevents completion. Correct in-scope failures and rerun the affected checks, or report the specific blocker. Do not mark an unverified item Pass.

Source: [Taste Skill prompt guide](https://www.tasteskill.dev/guide), captured 2026-10-06. This skill adds interactive intake and optional project autofill to the guide's new-website workflow.
