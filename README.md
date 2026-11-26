# ai-kb-assistant

A service that answers questions over a company knowledge base and always cites its sources.

Built as the capstone project of a 5-week AI engineering course: from a plain HTTP service
to a retrieval-augmented assistant with tool calling, evaluation and production hardening.

## Status

Week 1 — engineering skeleton: service structure, configuration, verification commands.

## Quickstart

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e ".[dev]"

cp .env.example .env            # fill in values locally, never commit .env
python scripts/check.py         # lint + tests
uvicorn kb_assistant.app:app --reload
```

## Verify

```bash
python scripts/check.py         # ruff + pytest, non-zero exit on failure
```

## Layout

```
src/kb_assistant/   application code
tests/              automated tests
scripts/            developer scripts (single entry point: scripts/check.py)
AGENTS.md           repository constitution for AI coding agents
.env.example        configuration template (real values live in .env)
```

## Roadmap

| Week | Focus |
|---|---|
| 1 | Skeleton, configuration, feedback loop |
| 2 | Engineering quality: unit/integration tests, security audit |
| 3 | LLM API, structured outputs, hybrid RAG |
| 4 | Agent loop, tool calling, MCP, evals |
| 5 | Observability, caching, token budgets, prompt-injection defence |
