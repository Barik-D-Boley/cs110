from byu_pytest_utils import compare_files, max_score, test_files, run_python, this_folder


@max_score(2)
def test_add_bullets_one_line():
    input_file = test_files / "add_bullets_one_line.input.txt"
    observed = "add_bullets_one_line.observed.txt"
    run_python(this_folder / "add_bullets.py", input_file, observed, "*")

    expected = test_files / "add_bullets_one_line.expected.txt"
    compare_files(expected, observed)


@max_score(3)
def test_add_bullets_multiple_lines():
    input_file = test_files / "add_bullets_multiple_lines.input.txt"
    observed = "add_bullets_multiple_lines.observed.txt"
    run_python(this_folder / "add_bullets.py", input_file, observed, "o")

    expected = test_files / "add_bullets_multiple_lines.expected.txt"
    compare_files(expected, observed)
