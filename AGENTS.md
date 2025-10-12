# Repository Guidelines

## Project Structure & Module Organization
Keep all production code in `src/`. Each challenge or feature belongs in its own module, e.g., `src/two_sum.py`. Group shared utilities inside subpackages to avoid long import chains. Place exploratory notebooks or scratch work outside the repo. Add tests under `tests/`, mirroring the source tree so `tests/test_two_sum.py` exercises `src/two_sum.py`. Commit generated assets or data files only when they are deterministic and under version control limits.

## Build, Test, and Development Commands
Run formatters before every commit:
- `black src` — normalize Python formatting.
- `isort src` — organize imports.
Lint and type-check with `flake8 src`. Execute the full regression suite with `pytest`. If you need an isolated run, use `pytest tests/test_two_sum.py -k scenario_name`. Install dependencies with `python -m pip install -r requirements.txt` once that file is updated for new tooling.

## Coding Style & Naming Conventions
Use Python 3.11+ features responsibly (type hints, structural pattern matching). Follow Black’s defaults (4-space indents, double quotes where rewritten). Prefer `snake_case` for files and symbols—avoid leading digits or hyphens in filenames so modules import cleanly. Keep functions small and pure; add docstrings that clarify intent and edge cases. Align imports per `isort` and keep linting quiet; fix warnings rather than silencing them.

## Testing Guidelines
Write `pytest` tests for every new behavior. Name files `test_<module>.py` and match test functions to the code they cover. Include edge cases (empty inputs, large values) and regression tests for previously reported bugs. Measure coverage locally with `pytest --cov=src --cov-report=term`. Do not merge changes unless the suite passes without xfails.

## Commit & Pull Request Guidelines
Craft concise, present-tense commit messages (`solve two sum`, `add flake8`). Keep commits focused; split unrelated work. Pull requests should explain the motivation, outline the solution, and link any tracking issues. Provide reproduction steps for bug fixes and command output or screenshots when UI or CLI behavior changes. Confirm that formatters, linters, and tests have run successfully before requesting review.
