from src.code_review__web.code_review_project.epylint.epylint import py_run


def test_pylint_console() -> None:
    pylint_stdout, pylint_stderr = py_run('file_for_test.py', return_std=True)
    print(f"Result {pylint_stdout.getvalue(), pylint_stderr.getvalue()}")  # noqa: T201


test_pylint_console()
