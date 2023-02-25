from byu_pytest_utils import max_score, check_io, test_files


@max_score(4)
def test_personal_library1():
    check_io(
        test_files / "personal_library1.txt",
        "personal_library.py"
    )


@max_score(4)
def test_personal_library2():
    check_io(
        test_files / "personal_library2.txt",
        "personal_library.py"
    )
