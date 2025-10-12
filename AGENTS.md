# Repository Guidelines

## Project Structure & Module Organization
Keep all production code in `src/`. Each challenge or feature belongs in its own aptly named module, e.g., `src/two_sum.py`. Group reusable helpers under subpackages to limit long relative imports. Place tests in `tests/` mirroring the source tree (`tests/test_two_sum.py` covers `src/two_sum.py`). Exclude ad-hoc notebooks or datasets from version control unless they are reproducible and under size limits.

## Build, Test, and Development Commands
Install tooling with `python -m pip install -r requirements.txt` (Python 3.12+). Run formatters before every commit:
- `black src` — normalize code layout.
- `ruff check src --fix` — apply Ruff’s lint, import, and correctness rules.
- `ruff format src` — align with Ruff’s 2025-compatible Black parity.
Execute the regression suite with `pytest`. Scope runs with `pytest tests/test_two_sum.py -k scenario_name`. Capture coverage data using `pytest --cov=src --cov-report=term`.

## Coding Style & Naming Conventions
Target modern Python (3.12/3.13) idioms: prefer `match` for structured branching, `dataclasses` or `typing.TypedDict` for data modeling, and `typing.Self`/`TypeAliasType` when useful. Start new modules with `from __future__ import annotations` for postponed evaluation. Stick to `snake_case` for files and symbols; keep filenames import-safe (avoid leading digits or hyphens). Functions should remain small and pure with docstrings describing intent and edge conditions. Let Ruff enforce lint rules—treat warnings as bugs rather than muting them.

## Testing Guidelines
Write `pytest` tests for every behavior change. Name files `test_<module>.py` and keep assertions focused on observable outcomes. Cover edge cases (empty collections, large inputs, invalid types) and add regression tests for any bug you fix. When introducing async code, use `pytest.mark.asyncio`. Do not merge until `pytest` and coverage checks succeed locally without `xfail`.

## Commit & Pull Request Guidelines
Craft concise, present-tense commit messages (`solve two sum`, `wire ruff check`). Keep commits scoped to a single concern. Pull requests should summarize motivation, outline the solution, and link tracking issues. Include reproduction steps for bug fixes and terminal output or screenshots when behavior changes. Confirm formatters, Ruff, and tests all pass before requesting review.

## 2025 Python Best Practices
Configure shared tooling in `pyproject.toml` when the project grows—Ruff, Black parity, and pytest all read from it. Favor lightweight, composable functions over inheritance-heavy designs. Use `pydantic` or `attrs` only when validation is required; otherwise lean on dataclasses plus type hints. Prefer context managers and `pathlib.Path` for IO, and guard CLI entry points with `if __name__ == "__main__":` so modules stay importable for testing.
