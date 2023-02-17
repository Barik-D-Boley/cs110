from byu_pytest_utils import max_score, check_io, test_files


@max_score(10)
def test_counting_grouse():
    check_io(
        test_files / "counting_grouse.txt",
        "counting_grouse.py"
    )