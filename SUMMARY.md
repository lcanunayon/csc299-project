SUMMARY.md
Development Process Summary

This project was developed through an iterative, test-driven, AI-assisted workflow that combined multiple modes of coding assistance: direct ChatGPT conversations, GitHub Copilot completions, and continuous test feedback. Over the course of implementing the task manager CLI and supporting modules, the development process moved through planning, structured coding, debugging, CI automation, and refinement.

Initial Planning and Specification

I began by clarifying the project goals: design a task manager system with models, storage, CLI commands, and full test coverage across multiple assignment phases (tasks3, tasks4, tasks5). I used ChatGPT in “planning/explaining” mode to break the project into clear components: data models, storage interface, task manager logic, and CLI UX. ChatGPT helped me restate specifications in my own words, list expected module responsibilities, and identify where tests would expect certain method signatures or behaviors.

AI Coding Assistance

I used two main forms of AI assistance:

1. ChatGPT (conversational mode)

I relied heavily on ChatGPT for:

breaking apart assignment PDFs into actionable steps

explaining failing tests

designing architecture (store layer, CLI flow, model classes)

debugging complex errors (e.g., ModuleNotFoundError, path issues, packaging layouts)

generating CI workflow files

reviewing commits and suggesting next steps

This mode was extremely valuable for problem-solving and interpreting errors.

2. GitHub Copilot (inline + chat side panel)

I used Copilot mainly for:

generating boilerplate functions

autofilling repetitive data-class code

writing argparse boilerplate for the CLI

completing test-driven implementations based on docstrings

inserting JSON store helpers

suggesting small refactors

Copilot was good at speeding up small tasks but unreliable for understanding the “bigger picture.” It sometimes generated incorrect logic or functions that didn't match test expectations. ChatGPT was far better for conceptual guidance.

Testing and Debugging

I ran tests continuously using pytest -q in PowerShell. Early on, I hit issues where tests in tasks3 and tasks5 failed due to missing modules or incorrect directory structures. ChatGPT helped diagnose the missing __init__.py files, editable installs (pip install -e .), and PYTHONPATH issues. As the codebase grew, tests exposed logic mistakes in add/update/remove task logic, JSON serialization, and CLI command behavior.

Testing became the driving force behind most design decisions—especially for edge cases like nonexistent task IDs, empty stores, or CLI argument formatting.

CI and Project Packaging

Toward the end, I added:

a GitHub Actions CI workflow (test + install)

a proper packaging layout (src/taskmgr)

a tested entry point for the CLI

ChatGPT generated the initial workflow YAML, which I then adjusted manually.

What Worked

Using ChatGPT as a planning and debugging partner

Test-driven development exposing problems early

Copilot for accelerating boilerplate and repetitive code

Breaking work into branches (e.g., 001-task-manager)

Using editable installs to fix module import issues

What Didn’t Work / False Starts

Running pytest before setting up packaging (caused early confusion)

Trying to “fix” tasks3 tests even though only tasks5 mattered

Copilot generating wrong method signatures that did not match specs

Multiple Git conflicts when pushing before pulling

Misconfigured CI at first due to wrong working directory

Final Reflection

My development process ended up being a mix of human reasoning, AI-assisted planning, AI-assisted code generation, and strict adherence to automated tests. The strongest combination was ChatGPT for high-level reasoning + Copilot for local code suggestions + continuous pytest feedback. This created a disciplined, iterative development cycle that improved both code quality and my understanding of full-stack Python project structure.
