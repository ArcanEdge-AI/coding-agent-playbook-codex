---
name: taste-new-website
description: Use when the user wants Taste's staged workflow for a new website, including brief questions or project autofill, design approval, a Next.js page, and written design audits.
---

Run the new-website workflow from the Taste Skill prompt guide. Read the sibling [design-taste-frontend skill](../design-taste-frontend/SKILL.md) for the installed Taste release's design rules and commands. Resolve `<skill>` in those commands to that installed skill's folder, and run them from the project root. If the dependency is missing, report it before starting. Follow governing instructions and the user's project constraints.

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

Use Taste's “Read the brief and the project,” “Write the argument,” and “Draw the direction” steps. Deal options with the sibling skill's [draw command](../design-taste-frontend/scripts/draw.mjs) and `--options 3`, using the brief's sector and section roles. Present the proposed option ID, a one-sentence design direction, and why it fits the audience and content.

Stop and request the user's approval of this direction. Do not create or edit the website before that approval. If the user changes the brief or direction, incorporate the change before proceeding.

## Step 2: Build after approval

Commit the approved option with the same draw arguments and `--direction <chosen id>` in place of `--options`. Build one Next.js page with at least eight sections that fit the product and at least four layout families. Follow the resulting direction sheet and Taste's “Build it, still” and “Move” steps. Use project imagery or authorized, credited assets according to Taste's imagery guidance. Keep one consistent theme across the page.

## Step 3: Verify

Report each audit in writing:

- Dash audit: zero U+2014 em dashes or U+2013 en dashes in the produced content.
- Follow Taste's “Gate” and “Look” steps. Lint the source and inspect the production build at the default 1440, 768, and 390 pixel widths. Run the scene check when the page uses scroll scenes. Open the screenshots, write the critique using Taste's rubric, and record inspector failures or warnings and their disposition. Repeat affected checks after fixes and after adding motion.
- Section layout repetition: list the layout family of every section.
- Hero discipline: check headline line count, subtext word count, and whether the primary CTA is visible without scrolling.

Any Fail prevents completion. Correct in-scope failures and rerun the affected checks, or report the specific blocker. Do not mark an unverified item Pass.

Source: [Taste Skill prompt guide](https://www.tasteskill.dev/guide), captured 2026-10-06. This skill adds interactive intake and optional project autofill to the guide's new-website workflow.
