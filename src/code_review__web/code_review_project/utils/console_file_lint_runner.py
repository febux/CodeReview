import subprocess
from enum import Enum
from typing import Tuple


class Linter(Enum):
    PYLINT = 'pylint'
    MYPY = 'mypy'


LINTER_ARGS_MAP = {
    Linter.PYLINT: ["--disable=C0103,C0111,C0415,R0903,R0901,R1710,R1705,R0901,E1101", "--ignore=migrations", "--output-format=colorized", "--max-line-length=180"],
    Linter.MYPY: ["--follow-imports=normal", "--ignore-missing-imports", "--strict", "--disallow-subclassing-any"],
}


def console_file_lint_runner(file_path: str, linter: Linter = Linter.PYLINT) -> Tuple[str, int]:
    cmd_res = subprocess.run(
        [linter.value, file_path, *LINTER_ARGS_MAP[linter]],
        stdout=subprocess.PIPE,
        encoding='utf-8',
        check=False,
    )
    return cmd_res.stdout, cmd_res.returncode
