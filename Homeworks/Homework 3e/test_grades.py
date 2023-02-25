from byu_pytest_utils import max_score, check_io, test_files


@max_score(6)
def test_grades():
    check_io(
        test_files / "grades.txt",
        "grades.py"
    )
