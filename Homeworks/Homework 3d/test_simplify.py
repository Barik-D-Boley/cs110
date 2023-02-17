from byu_pytest_utils import max_score, test_files, check_io


@max_score(10)
def test_simplify():
    check_io(
        test_files / "simplify.txt",
        "simplify.py"
    )