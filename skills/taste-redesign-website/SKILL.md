---
name: taste-redesign-website
description: Redesign an existing website with Taste through brief questions or project autofill, a baseline audit, an approved plan, and before-and-after checks on the protected experience.
---

# Redesign a website with Taste

Use the installed [Taste design and verification guide](../design-taste-frontend/SKILL.md) for the business-kind table, design recipes, build, and checks. This workflow adds separate approvals for the audit and the redesign plan. In the examples, replace `<taste>` with the absolute path to that sibling skill, `<evidence>` with a task-owned scratch directory outside the website and any active Taste build, and other placeholders with the site's actual values.

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

## Step 1. Audit the existing site

Record the affected routes, page states, and source or URL used for the baseline. Use a working local preview when available. A supplied public URL can provide read-only visual evidence. Run checks that exercise controls against a safe preview. Keep preapproval evidence in scratch and leave the website and its gate untouched.

Capture each affected route in the same state at **1440×900, 1024×768, 820×1180, 768×1024, and 390×844**. Repeat the screenshot command for each pair with its actual width, height, and filename. Use a separate directory per route when capturing several. The examples show a local preview URL.

```text
node "<taste>/scripts/shoot.mjs" --url "<before-url>" --w 820 --h 1180 --out "<evidence>/before/820x1180.png"
node "<taste>/scripts/consistency.mjs" "<before-url>" --page <kind> --category "<what is sold>" --primary "<main action>" --widths 1440,1024,820,768,390 --rhythm-widths 1440,820,768,390 --out "<evidence>/before/consistency"
```

Open the images and read the measurements. Lint the available HTML or copy source. Record the current colors, type, radii, logo, signature interactions, and voice. Trace navigation and conversion paths, including form fields and destinations. Identify the routes, titles, headings, and anchors that matter for SEO, any broken layouts or links, and which findings justify a change. Mark unavailable evidence. Present the audit and wait for the user's approval before proposing a plan.

## Step 2. Propose the redesign after audit approval

Recommend Preserve, Overhaul, or Greenfield-with-content-preserved. Describe what will change in type, color, layout, and interactions, what will survive, and how the chosen scope answers the audit. Keep the site's URLs, primary navigation labels, form field names and behavior, logo, legal copy, and protected headings and anchors. List any proposed exception individually for approval, including changes to established brand type or accent.

When proposing a new palette or kit type pairing, run the deal from `<evidence>`. It writes history and can arm or join a build in its working directory or an ancestor. Disable shared history for this proposal. Use the guide's business kind and a supported trade, omitting `--trade` if none fits.

```text
node "<taste>/scripts/start.mjs" deal --page <kind> --trade "<trade>" --history .taste-skill/history.json --no-recent
```

Record proposed palette and type IDs alongside the current values. When preserving a supplied palette or custom typeface, record the actual tokens or font family. Wait for approval of the plan and its specific exceptions before editing the website or arming its gate.

## Step 3. Implement the approved plan

Work in the existing project and stack. Arm the gate on the affected local route. This example uses a built page in `dist` and names the asset root so root-relative links work. For a server-rendered page, use the running local preview URL and omit `--root`.

```text
node "<taste>/scripts/gate.mjs" --start dist/index.html --root dist --kind <kind> --category "<what is sold>" --primary "<main action>"
```

Use the approved IDs with the guide's `css` command for a new palette and pairing. For supplied brand colors and an approved kit pairing, generate tokens with the following command. Keep a protected custom font in the site's styles. Apply only approved exceptions and use the project's existing navigation and form contracts.

```text
node "<taste>/scripts/start.mjs" brand --page <kind> --bg "<background-hex>" --ink "<ink-hex>" --accent "<accent-hex>" --type <approved-type-id>
```

## Step 4. Compare and verify

Rebuild the production page. Repeat the baseline captures and measurements for the same routes, states, and five viewport pairs under `<evidence>/after`. Open each before-and-after pair. Apply the guide's full consistency, layout, copy, and performance checks to the finished page. Review motion and reduced-motion behavior where used. Exercise links, menus, form validation, and the submission path on the authorized preview. Report any unexercised destination.

```text
node "<taste>/scripts/shoot.mjs" --url dist/index.html --root dist --w 820 --h 1180 --out "<evidence>/after/820x1180.png"
node "<taste>/scripts/gate.mjs" dist/index.html --root dist
```

Run the manual gate against the current build and follow its three-round default. At `GATE: OPEN`, stop fixing and report the remaining failures. Its additional 320-pixel check covers narrow-screen interactions and overflow. Report the final `GATE:` line first, with open failures, waivers and reasons, retained warnings, and any missing evidence.

In the written audit, identify visible improvements and regressions with the route and viewport where each occurred. List changes to protected URLs, navigation labels, forms, headings, anchors, accent, typography, logo treatment, and legal copy against their specific approvals. Verify zero U+2014 and U+2013 characters in newly written content. Report occurrences in protected copy separately.
