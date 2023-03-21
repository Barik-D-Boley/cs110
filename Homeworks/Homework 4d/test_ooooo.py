from byu_pytest_utils import compare_files, max_score, test_files, run_python, this_folder


@max_score(2)
def test_ooooo_small():
    input_file = test_files / "ooooo_small.input.txt"
    observed = "ooooo_small.observed.txt"
    run_python(this_folder / "ooooo.py", input_file, observed)
    expected = test_files / "ooooo_small.expected.txt"
    compare_files(expected, observed)


@max_score(3)
def test_ooooo_large():
    input_file = test_files / "ooooo_large.input.txt"
    observed = "ooooo_large.observed.txt"
    run_python(this_folder / "ooooo.py", input_file, observed)
    expected = test_files / "ooooo_large.expected.txt"
    compare_files(expected, observed)
