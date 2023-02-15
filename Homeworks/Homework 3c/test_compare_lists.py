from byu_pytest_utils import max_score, check_io, test_files


@max_score(2)
def test_compare_lists_fruit():
    check_io(
        test_files / "compare_lists_fruit.txt",
        "compare_lists.py"
    )


@max_score(2)
def test_compare_lists_vegetables():
    check_io(
        test_files / "compare_lists_vegetables.txt",
        "compare_lists.py"
    )


@max_score(2)
def test_compare_lists_equal():
    check_io(
        test_files / "compare_lists_equal.txt",
        "compare_lists.py"
    )
