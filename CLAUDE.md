# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Early-stage FastAPI service intended to host an LLM prediction endpoint, paired with Locust for performance testing. Python 3.12, dependencies managed by `uv` (see `uv.lock` and `.python-version`).

## Commands

Dependencies are declared in `pyproject.toml` and locked in `uv.lock`. Use `uv` rather than raw `pip`.

- Install / sync deps: `uv sync`
- Run the API in dev (auto-reload, FastAPI CLI from `fastapi[standard]`): `uv run fastapi dev main.py`
- Run the API in prod mode: `uv run fastapi run main.py`
- Run a one-off script / REPL inside the env: `uv run python ...`
- Performance test with Locust: `uv run locust -f <locustfile.py> --host http://127.0.0.1:8000` (no locustfile is checked in yet; create one alongside `main.py` when needed).

There is no test suite, linter, or formatter wired up — do not invent commands for them. The README's numbered list is a personal scratch checklist, not authoritative documentation.

## Architecture

- `main.py` — single-module FastAPI app exposing `GET /` and `POST /predict`. `/predict` currently echoes `data["name"]` and is a placeholder for real model inference; treat it as the integration point when wiring an LLM in.
- `notebooks/` — exploratory Jupyter notebooks; not imported by the app.
- `pyproject.toml` / `uv.lock` / `.python-version` — uv-managed environment pinned to Python 3.12.

The codebase is intentionally tiny — most "structure" you might expect (routers, schemas, model loading, config) does not exist yet. When adding it, prefer extending `main.py` first and only split into modules once there's a concrete reason to.
