from byu_pytest_utils import compare_files, max_score, test_files, run_python, this_folder


@max_score(2)
def test_filter_nan_small():
    input_file = test_files / "nan_small.input.txt"
    observed = "nan_small.observed.txt"
    run_python(this_folder / "filter_nan.py", input_file, observed, "*")
    expected = test_files / "nan_small.expected.txt"
    compare_files(expected, observed)


@max_score(3)
def test_filter_nan_large():
    input_file = test_files / "nan_large.input.txt"
    observed = "nan_large.observed.txt"
    run_python(this_folder / "filter_nan.py", input_file, observed, "*")
    expected = test_files / "nan_large.expected.txt"
    compare_files(expected, observed)
