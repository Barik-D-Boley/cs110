from byu_pytest_utils import check_io, max_score, test_files


@max_score(10)
def test_calculator():
    check_io(
        test_files / "calculator.txt",
        "calculator.py"
    )
