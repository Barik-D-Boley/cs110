from byu_pytest_utils import max_score, check_io, test_files


@max_score(6)
def test_student_ratings():
    check_io(
        test_files / "student_ratings.txt",
        "student_ratings.py"
    )
