"""Run the local quality gate: ruff first, then pytest."""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run(command: list[str]) -> int:
    """Run a command from the repository root and return its exit code."""
    return subprocess.run(command, cwd=REPO_ROOT, check=False).returncode


def main() -> int:
    """Run lint and tests, stopping at the first failure."""
    ruff_command = [sys.executable, "-m", "ruff", "check", "."]
    if _run(ruff_command) != 0:
        print(f"FAILED: {' '.join(ruff_command)}")
        print("ruff: run `python -m ruff check . --fix`, then fix any remaining issues.")
        return 1

    pytest_command = [sys.executable, "-m", "pytest", "-q"]
    if _run(pytest_command) != 0:
        print(f"FAILED: {' '.join(pytest_command)}")
        print("pytest: fix the failing tests shown above, then re-run `python -m pytest -q`.")
        return 1

    print("OK: lint + tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
