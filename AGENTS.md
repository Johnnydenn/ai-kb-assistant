# AGENTS.md — repository constitution

Rules and contracts for AI coding agents working in this repository.
Read this file before touching any code.

## Project

`ai-kb-assistant` — a question-answering service over a company knowledge base.
Python 3.11+, FastAPI, pytest, ruff.

## Commands

| Purpose | Command |
|---|---|
| Install (dev) | `pip install -e ".[dev]"` |
| Verify (lint + tests) | `python scripts/check.py` |
| Run service | `uvicorn kb_assistant.app:app --reload` |

`python scripts/check.py` is the single source of truth for "is this change acceptable".
A change is not done until it exits with code 0.

## Working rules

1. **Think before coding.** State assumptions. If a requirement is ambiguous, ask — do not guess.
2. **Simplicity first.** Minimum code that solves the stated problem. No speculative abstractions.
3. **Surgical changes.** Touch only what the task requires. No drive-by reformatting or refactoring.
4. **Goal-driven.** Turn every task into a verifiable check; run it before claiming success.
5. **Small commits.** One logical change per commit, message in imperative mood
   (`add /ask endpoint`, not `added stuff`).

## Safety rules (non-negotiable)

- **Ask for confirmation before destructive commands**: `rm -rf`, `git reset --hard`,
  `git push --force`, dropping or truncating data, rewriting history, deleting branches.
- **Never commit secrets.** `.env` is git-ignored; only `.env.example` belongs in the repository.
- **Never log secrets or personal data.** Read configuration from environment variables.
- **Do not weaken checks to make them pass.** Fixing a failure by loosening a test or a lint rule
  requires explicit human approval.
- **Never push to `main` directly.** Work happens on a branch and lands through a pull request.

## Workflow

1. Branch: `feature/<short-name>` or `fix/<short-name>`.
2. Implement, then `python scripts/check.py` → must be green.
3. Commit, push the branch, open a pull request describing *what* and *why*.
4. Human reviews and merges.

Initial repository bootstrap (first commit) is the only exception: it lands on `main`
because a pull request needs an existing base branch.

## Structure

```
src/kb_assistant/   application code (importable package)
tests/              pytest suites, mirroring the source layout
scripts/            developer entry points
```
