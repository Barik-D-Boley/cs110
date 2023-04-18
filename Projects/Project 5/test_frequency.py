from byu_pytest_utils import max_score, test_files, dialog


@max_score(10)
@dialog(
    test_files / "simple.frequency.dialog.txt",
    "frequency.py",
    test_files / "simple.txt"
)
def test_frequency_simple(group_name): ...


@max_score(10)
@dialog(
    test_files / "message.frequency.dialog.txt",
    "frequency.py",
    test_files / "message.txt"
)
def test_frequency_message(group_name): ...


@max_score(10)
@dialog(
    test_files / "1Nephi.frequency.dialog.txt",
    "frequency.py",
    test_files / "1Nephi.txt"
)
def test_frequency_nephi(group_name): ...
