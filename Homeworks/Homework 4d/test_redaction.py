from byu_pytest_utils import compare_files, max_score, test_files, run_python, this_folder


@max_score(1)
def test_redaction_small_picked():
    input_file = test_files / "redaction_small.input.txt"
    observed = "redaction_small_picked.observed.txt"
    run_python(this_folder / "redaction.py", input_file, observed, "picked")
    expected = test_files / "redaction_small_picked.expected.txt"
    compare_files(expected, observed)


@max_score(1)
def test_redaction_small_peter():
    input_file = test_files / "redaction_small.input.txt"
    observed = "redaction_small_peter.observed.txt"
    run_python(this_folder / "redaction.py", input_file, observed, "Peter")
    expected = test_files / "redaction_small_peter.expected.txt"
    compare_files(expected, observed)


@max_score(1)
def test_redaction_large_the():
    input_file = test_files / "redaction_large.input.txt"
    observed = "redaction_large_the.observed.txt"
    run_python(this_folder / "redaction.py", input_file, observed, "the")
    expected = test_files / "redaction_large_the.expected.txt"
    compare_files(expected, observed)


@max_score(2)
def test_redaction_large_and():
    input_file = test_files / "redaction_large.input.txt"
    observed = "redaction_large_and.observed.txt"
    run_python(this_folder / "redaction.py", input_file, observed, "and")
    expected = test_files / "redaction_large_and.expected.txt"
    compare_files(expected, observed)
