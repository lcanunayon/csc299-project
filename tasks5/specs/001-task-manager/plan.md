```markdown

# Implementation Plan: Task Manager

**Branch**: `001-task-manager` | **Date**: 2025-11-19 | **Spec**: `specs/001-task-manager/spec.md`

## Summary

Implement a small, well-tested CLI Task Manager that exposes CRUD operations
for a `Task` model. Focus on clarity, test-first development, and minimal
complexity. CLI will support human-readable output and an optional `--json`
mode for automation.

## Task Model (canonical)

Task fields (names and public contract):

- `id` (string|int): unique identifier (system-assigned).
- `title` (string): required short title.
- `description` (string, optional): longer details.
- `completed` (boolean): completion flag; default `false`.
- `createdAt` (ISO 8601 string): timestamp at creation (system-generated).
- `updatedAt` (ISO 8601 string): timestamp at last modification (system-generated).

Note: Keep the model small and serializable to JSON for CLI `--json` output.

## Technical Context

- Language/Version: Recommend Python 3.11 for quick iteration; other languages
  are acceptable if the team prefers.
- Primary Dependencies: `click` or `argparse` for CLI, `sqlite3` (stdlib) or a
  simple JSON file persistence; `pytest` for tests.
- Storage: Default to an embedded SQLite file (durable, zero-deps); provide a
  JSON file mode for lightweight development/testing.
- Testing: `pytest` for unit/integration; CLI acceptance tests use subprocess
  helpers to assert exit codes and stdout/stderr.
- CI: Run linters + `pytest`; optionally build docs for a docs gate.

## Constitution Check (how plan satisfies principles)

- Clarity & Simplicity: Small model and explicit command verbs (`add`, `list`,
  `show`, `update`, `delete`).
- Code Quality: Add linters and formatting, require PRs <400 LOC where possible.
- Test-First Standards: Each story includes failing tests before implementation.
- Consistent UX: Document CLI help, error messages, and `--json` semantics.
- Minimal Complexity: No external services or sync in MVP; any escalation must
  include a migration plan and cost estimate.

## CLI Command Mapping (explicit)

- `task add --title "TITLE" [--description "DESC"] [--json]` → create task
- `task list [--completed true|false] [--json]` → list tasks (filter: completed)
- `task show <id> [--json]` → show full task
- `task update <id> [--title "TITLE"] [--description "DESC"] [--completed true|false] [--json]` → update fields
- `task delete <id> [--force]` → delete task (prompt unless `--force`)

Each command: `--help`; exit codes (0 success, >0 error); `--json` for
stable machine-readable output. CLI must validate inputs and return
meaningful error messages.

## Project Structure (suggested)

```text
src/
  taskmgr/
    __main__.py        # CLI entrypoint
    cli.py             # command definitions and input validation
    models.py          # Task dataclass + serialization helpers
    store.py           # persistence API (create,list,get,update,delete)
    output.py          # formatting helpers (human/json)

tests/
  unit/
  integration/
  cli/

docs/
  quickstart.md
  cli-help.md
```

## Phase Work Breakdown (test-first)

Phase 1 — Setup

- T001 Initialize project layout and `pyproject.toml` (or equivalent).
- T002 Configure linters (`ruff`/`flake8`) and formatter (`black`).
- T003 Add CI: run linters + `pytest` on PRs.

Phase 2 — Foundation (blocking)

- T010 Implement `models.py` with `Task` dataclass and serialization.
- T011 Implement `store.py` interface and an in-memory implementation.
- T012 Add unit tests for model serialization and store interface (tests/unit).

Phase 3 — Core CLI (MVP: P1 stories)

- T020 Write failing CLI acceptance test for `task add` (cli/acceptance).
- T021 Implement `task add` → `store.create` and ensure `createdAt`/`updatedAt` set.
- T022 Add unit/integration tests and quickstart snippet.

- T030 Write failing CLI acceptance test for `task list`.
- T031 Implement `task list` with optional `--completed` filter.

- T040 Write failing CLI acceptance test for `task show <id>`.
- T041 Implement `task show` and tests.

Phase 4 — Update & Delete (P2)

- T050 Write failing CLI acceptance test for `task update <id>`.
- T051 Implement update behavior; ensure `updatedAt` is refreshed.

- T060 Write failing CLI acceptance test for `task delete <id>`.
- T061 Implement delete behavior; add `--force` option and confirmation.

Phase 5 — Polish & Cross-cutting

- T100 Add `--json` output mode for all commands and add contract tests.
- T101 Add docs: `docs/quickstart.md` and `docs/cli-help.md`.
- T102 Add integration tests covering full user journeys.
- T103 Ensure docs build in CI (Constitution requirement) and link docs in PRs.

## Tasks for the First PR (small, reviewable)

- Initialize the repo (`pyproject.toml`, `README.md`) and CI skeleton.
- Add `models.py` (Task dataclass) + unit tests (should fail initially if TDD).
- Add `store.py` with an in-memory implementation + unit tests.
- Add minimal `cli.py` with `task add` wiring to store (tests should drive implementation).

Stop for review: ensure PR description includes Constitution Check (link to
`specs/001-task-manager/spec.md`), tests, and updated docs snippet.

## Testing Strategy

- Unit tests: model behavior, store behavior, helpers.
- CLI acceptance tests: run the CLI as a subprocess to assert exit codes,
  stdout/stderr, and side effects (persistence).
- Integration tests: combine commands to exercise user stories end-to-end.

## Success Criteria (how we will know it's done)

- All acceptance scenarios from `spec.md` are implemented and tested.
- CLI commands behave as documented, returning correct exit codes and JSON
  output when requested.
- Documentation (quickstart + CLI help) is present and builds in CI.

## Risks & Mitigations

- Risk: Over-engineering persistence. Mitigation: start with SQLite/in-memory
  JSON and keep store abstraction to swap later.
- Risk: Long-lived PRs increase merge conflicts. Mitigation: keep PRs small
  and test-first.

---

**Notes**: This plan follows spec-kit conventions: explicit user stories,
testable requirements, Constitution compliance, and a clear incremental
delivery path.

```
