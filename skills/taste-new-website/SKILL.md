---
name: taste-new-website
description: Build a new website with Taste through brief questions or project autofill, an approved direction, one Next.js page by default, and written visual audits.
---

# Design a new website with Taste

Use the installed [Taste design and verification guide](../design-taste-frontend/SKILL.md) for the business-kind table, design recipes, build, and checks. This workflow adds intake and a direction approval. Replace `<taste>` below with the absolute path to that sibling skill and substitute the brief's actual values for the other placeholders. Follow the user's supplied facts, brand requirements, and project constraints.

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

## Step 1. Propose the direction

From the brief, identify the business kind, trade, main action, and available photographs, product UI, or other evidence. The dealer's `<kind>` is `software`, `gaming`, `tech`, `product`, `service`, or `place`. Describe the page's argument and plan each useful section around its content.

Run the proposal deal from a task-owned scratch directory outside the website and any active Taste build. The deal writes history and can arm or join a gate in its working directory or an ancestor. Keep its local files in scratch and disable shared deal history for this run. Use a supported trade or omit `--trade` when the brief has no matching trade.

```text
node "<taste>/scripts/start.mjs" deal --page <kind> --trade "<trade>" --history .taste-skill/history.json --no-recent
```

Use the guide's layout and moment dealers there as needed. Record the actual palette and type pairing IDs and the chosen hero, section layouts, and motion. Recommend the first suitable deal under the guide's rules and explain how it fits the audience, materials, and brand.

The default deliverable is one Next.js page with at least eight sections that fit the product and at least four layout families. If the user or existing project requires a different stack or scope, name the proposed change and its reason in the direction approval.

Present the filled brief, direction, and reasons. Wait for the user's approval of the direction before changing the website, installing anything in it, or arming its project gate. Carry the approved choices into the build.

## Step 2. Build the approved page

Work in the project root and use the approved stack's build command. The example arms a Next.js static export at `out/index.html` with `out` as its asset root. The second line generates a dealt palette and pairing with a soft radius. Substitute the approved choices. For plain HTML use the actual page path. For a server-rendered route, use the project's running local preview URL and omit `--root`.

```text
node "<taste>/scripts/gate.mjs" --start out/index.html --root out --kind <kind> --category "<what is sold>" --primary "<main action>"
node "<taste>/scripts/start.mjs" css --page <kind> --palette <approved-palette-id> --type <approved-type-id> --radius soft --history .taste-skill/history.json
```

Use the emitted style links and tokens for the approved IDs. For supplied brand colors, use the guide's `brand` command with the actual colors and an approved kit type ID. Keep a required custom typeface in the site's styles. Follow the guide's recipes for the approved hero, section layouts, moments, licensed assets, and credits. Identify stand-ins and outstanding client material in the handoff.

## Step 3. Check the build and inspect the evidence

Run the guide's copy lint on the built HTML or actual copy source, plus its full consistency, layout, and performance checks on the rendered route. Exercise the primary action and review motion and its reduced-motion behavior where used. Run applicable project checks. Rebuild after changes. Capture the finished page at **1440×900, 1024×768, 820×1180, 768×1024, and 390×844**. Run the following screenshot command for each pair, changing the width, height, and filename. Open each image.

```text
node "<taste>/scripts/shoot.mjs" --url out/index.html --root out --w 820 --h 1180 --out .taste-skill/after/820x1180.png
node "<taste>/scripts/gate.mjs" out/index.html --root out
```

Run the manual gate on the current build. Follow the guide's three-round default. At `GATE: OPEN`, stop fixing and report the remaining failures. Report the final `GATE:` line first, with open failures, waivers and reasons, retained warnings, and checks that could not run. The gate also checks overflow at 320 pixels. Claim screenshot evidence only for dimensions actually captured.

In the written audit, list the layout family of each section, the hero headline's line count, subtext word count, and whether the primary action is visible without scrolling at the measured viewports. Verify zero U+2014 and U+2013 characters in newly written copy. Report any occurrence in protected supplied text separately.
