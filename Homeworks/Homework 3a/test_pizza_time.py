from byu_pytest_utils import max_score, test_files, check_io


@max_score(5)
def test_pizza_time():
    check_io(
        test_files / "pizza-time.txt",
        "pizza_time.py"
    )
