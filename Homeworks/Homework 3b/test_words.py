from byu_pytest_utils import max_score, test_files, check_io


@max_score(10)
def test_words():
    check_io(
        test_files / "words.txt",
        "words.py",
    )
