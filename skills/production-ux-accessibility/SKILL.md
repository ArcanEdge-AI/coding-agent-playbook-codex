---
name: production-ux-accessibility
description: Review frontend production readiness, user experience, accessibility, responsive behavior, forms, validation, loading states, empty states, error messages, keyboard navigation, screen reader basics, focus management, color contrast, browser compatibility, broken links, and critical user-flow usability.
---

# Production UX Accessibility

## Core purpose

Identify UX or accessibility issues that block or degrade critical user flows; apply fixes only within authorized remediation scope.

## Use this skill when

- The production pass needs UX or accessibility review.
- The application has frontend screens, forms, navigation, or critical user journeys.
- The user wants production polish that helps users complete key tasks.

## Do not use this skill when

- The repository has no user interface.
- The task is only backend or infrastructure.
- The user wants a full redesign instead of production-readiness polish.

## Check for

- Mobile responsiveness
- Broken layouts
- Inconsistent UI states
- Missing form validation
- Poor error messages
- Missing loading states
- Missing empty states
- Keyboard navigation
- Screen reader basics
- Color contrast
- Browser compatibility risks
- Broken links
- Focus management
- Disabled state behavior
- Critical flow usability issues
- Inaccessible controls
- Missing labels
- Confusing success states

## Default workflow

Resolve the task mode first: assessment-only work reports findings without source, test, or repository-document edits; authorized remediation applies only in-scope fixes. Release, production, and destructive operations retain their separate authority requirements.

1. Identify frontend framework and UI conventions.
2. Identify critical user flows.
3. Inspect components, pages, forms, route transitions, and state handling.
4. Classify findings as Blocker, High, Medium, or Low.
5. Prioritize issues that block task completion.
6. Apply safe in-scope fixes only when remediation is authorized; assessment-only requests report recommendations:
   - missing labels
   - missing validation text
   - loading states
   - empty states
   - focus and keyboard improvements
   - broken links
   - clearer error messages
7. Avoid redesigning the product.
8. Include relevant manual QA checks in the requested deliverable; edit a project checklist only when authorized.

## Severity guidance

Classify as Blocker when users cannot complete a critical flow.

Classify as High when UX or accessibility issues materially harm critical production usage.

Classify as Medium when improvements are important but not release-blocking.

Classify as Low for polish, consistency, or optional accessibility improvements.

## Guardrails

- Do not introduce a new design system.
- Do not make broad visual changes without approval.
- Do not reduce accessibility for visual polish.
- Do not hide validation errors.
- Preserve existing visual conventions where reasonable.
- Do not remove content or functionality to simplify the UI.

## Deliverables

Include the following in the requested assessment response or report. Update repository readiness files only when those artifacts are requested or part of authorized remediation:

- UX readiness summary
- Accessibility findings
- Safe frontend fixes
- Manual QA recommendations
- Remaining UX risks
- Files changed and reasons