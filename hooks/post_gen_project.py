"""Post generation hook."""
import os
import re
import subprocess
import sys
from pathlib import Path
from textwrap import dedent

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m"
INFO = "\x1b[1;34m"
HINT = "\x1b[3;35m"
SUCCESS = "\x1b[1;32m"
ERROR = "\x1b[1;31m"
MSG_DELIMITER = "=" * 80


def _error(msg: str) -> str:
    """Format error message."""
    return f"{ERROR}{msg}{TERMINATOR}"


def _success(msg: str) -> str:
    """Format success message."""
    return f"{SUCCESS}{msg}{TERMINATOR}"


def _info(msg: str) -> str:
    """Format info message."""
    return f"{INFO}{msg}{TERMINATOR}"


def run_cmd(command: str, shell: bool, cwd: str) -> bool:
    proc = subprocess.run(command, shell=shell, cwd=cwd, capture_output=True)
    if proc.returncode:
        # Write errors to the main process stderr
        print(_error(f"\nError while running {command}:"), file=sys.stderr)
        sys.stderr.buffer.write(proc.stderr)
        print("\n", file=sys.stderr)
    return False if proc.returncode else True


def initialize_git():
    """Apply black and isort to the generated codebase."""
    print(_info("Git repository"))
    steps = [
        ["Initialize", ["git", "init", "."], False, "."],
        ["Add files", ["git", "add", "."], False, "."],
    ]
    for step in steps:
        msg, command, shell, cwd = step
        print(f" - {msg}")
        result = run_cmd(command, shell=shell, cwd=cwd)
        if not result:
            sys.exit(1)


def main():
    """Final fixes."""
    print(f"{MSG_DELIMITER}")
    print("")
    initialize_git()
    print("")
    print(f"{MSG_DELIMITER}")
    msg = dedent(
        f"""
        {_success('New distribution "{{ cookiecutter.distribution_title }}" was generated')}

        Now, code it, push to your organization.

        Sorry for the convenience,
        The Plone Community.
    """
    )
    print(msg)
    print(f"{MSG_DELIMITER}")


if __name__ == "__main__":
    main()
