# Sync Impact Report
<!--
Version change: 1.0.0 -> 1.1.0

- Modified principles:
- PRINCIPLE_1_NAME (template placeholder) -> I. Clarity & Simplicity
- PRINCIPLE_2_NAME (template placeholder) -> II. Code Quality & Maintainability
- PRINCIPLE_3_NAME (template placeholder) -> III. Test-First Standards
- PRINCIPLE_4_NAME (template placeholder) -> IV. Consistent User Experience
- PRINCIPLE_5_NAME (template placeholder) -> V. Minimal Necessary Complexity

Added / Filled sections:
- Additional Constraints (filled)
- Development Workflow & Quality Gates (expanded)
- Constitution Check (defined)
- Documentation Requirement (new)

Removed sections:
- None removed; template placeholders were replaced with concrete text.

Templates reviewed and sync status:
- `.specify/templates/plan-template.md` ✅ updated (Constitution Check tightened)
- `.specify/templates/spec-template.md` ✅ updated (added Constitution Compliance)
- `.specify/templates/tasks-template.md` ✅ updated (tests mandated)
- `.specify/templates/agent-file-template.md` ✅ reviewed (no changes required)
- `.specify/templates/commands/*.md` ⚠ pending (no command templates found; add if the project uses command scaffolds)

Follow-up TODOs:
- TODO(RATIFICATION_DATE): provide the original ratification date for the
	Constitution (insert ISO date YYYY-MM-DD).
- If the repository uses command templates, add them under
	`.specify/templates/commands/` and update plan-template references.
-->

# Project Constitution

## Core Principles

### I. Clarity & Simplicity (NON-NEGOTIABLE)
Code MUST be written for human readers first. Functions and modules MUST be
small, well-named, and focused. Complexity is a cost: prefer explicit,
declarative code over clever optimizations. When a complex solution is chosen,
it MUST be documented with a short rationale, trade-offs, and measurable goals.

Rationale: Clear code reduces onboarding time, lowers review friction, and
reduces defects over the lifetime of the codebase.

### II. Code Quality & Maintainability
All production code MUST pass static analysis and formatting checks defined by
the project. Pull requests MUST be reviewed by at least one maintainer and be
small enough to be reviewed effectively (recommendation: under 400 lines of
change). Public APIs and modules MUST include concise documentation and
examples. Deprecations MUST follow the Versioning policy below.

Rationale: Automated quality checks plus human review keep technical debt
manageable and make future changes predictable.

### III. Test-First Standards (NON-NEGOTIABLE)
Tests MUST be written for every new feature and for bug fixes that affect
behavior. Tests SHOULD be authored before implementation (TDD) where feasible:
write failing tests first, then implement until they pass. Projects MUST include
unit, integration, and contract tests at appropriate layers; critical flows
MUST have end-to-end verification or user scenario tests.

Quality gates: CI MUST run all tests and block merges on failing tests. Test
coverage targets are advisory and MUST be evaluated per-project; however, core
libraries must maintain meaningful coverage and tests that assert behavior,
not implementation details.

Rationale: Tests are executable specifications that enable safe refactors and
reliable releases.

### IV. Consistent User Experience
User-facing behavior (APIs, CLIs, GUIs) MUST be consistent across the product:
error messages, validation patterns, configuration semantics, and telemetry
naming MUST follow documented conventions. Accessibility, clear error
reporting, and helpful defaults are required for user-facing features.

Rationale: Consistency reduces cognitive load for users and support teams and
enables predictable integrations across components.

### V. Minimal Necessary Complexity (YAGNI + Justification)
Design for the simplest solution that meets requirements. Introduce additional
architecture or tooling only when a measurable need or risk justifies it. Any
added complexity MUST include a documented migration plan, cost estimate, and
sunset criteria.

Rationale: Avoid premature abstraction and unnecessary frameworks that
increase maintenance burden.

### VI. Use Emojis in Output
Add emojis in program output when possible.
Be happy!

## Additional Constraints

- Technology neutrality: The Constitution is technology-agnostic. Use stable,
	actively maintained tools and prefer well-known libraries unless a specific
	rationale exists.
- Security & privacy: Security best practices MUST be followed; secrets MUST
	never be committed; sensitive data handling MUST be documented and reviewed.
- Backwards compatibility: Public interfaces SHOULD remain stable across patch
	releases; breaking changes MUST follow the Versioning policy and include a
	migration plan.


## Development Workflow & Quality Gates

- Branching: Feature branches SHOULD be short-lived. PR titles MUST reference
	the spec/plan and include a concise summary and testing instructions.
- PR Review: At least one approving review from a project maintainer is
	required. Reviews MUST verify adherence to the Constitution (see
	"Constitution Check" below).
- Testing: Tests MUST be present and runnable locally; CI MUST run all tests
	and linters. Tests for critical flows are blocking for releases.
- Releases: Release notes MUST list breaking changes, rationale, and migration
	steps when applicable.

- Documentation: User-facing documentation MUST be created or updated and
	merged to the `master` branch at the same time as any PR that introduces
	user-visible behavior changes or configuration changes. PRs that change
	behavior MUST include a link to the updated documentation and tests or CI
	checks SHOULD verify that the documentation builds (when a docs build is
	supported). If documentation cannot be produced prior to merge, the PR MUST
	include a documented mitigation plan and an explicit short deadline for
	completion.

### Constitution Check (required for PRs touching non-trivial code)

- Checklist for reviewers to include in PR description:
	- [ ] Principle: Does the change preserve clarity and simplicity?
	- [ ] Quality: Does it pass linters/static analysis and include docs?
	- [ ] Tests: Are tests present and do they meaningfully cover behavior?
	- [ ] UX: Are user-facing changes consistent with conventions?
	- [ ] Complexity: If complex, is there a written justification + plan?

## Governance

- Amendments: Changes to this Constitution MUST be proposed in a PR that
	includes (a) the proposed text, (b) a migration/communication plan, and
	(c) a rationale. Amendments require approval from at least two project
	maintainers and a recorded vote or comment thread resolving objections.
- Versioning policy: The Constitution itself follows semantic versioning:
	- MAJOR when principles or governance are removed/redefined (breaking).
	- MINOR when new principles or substantive sections are added.
	- PATCH for wording, clarifications, or non-substantive fixes.
- Compliance review: Periodic reviews (recommended once per major release)
	MUST verify projects and templates continue to align with the Constitution.

**Version**: 1.1.0 | **Ratified**: TODO(RATIFICATION_DATE): provide original adoption date | **Last Amended**: 2025-11-19
