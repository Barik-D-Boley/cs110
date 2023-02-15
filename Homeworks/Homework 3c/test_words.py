from byu_pytest_utils import max_score, check_io, test_files


@max_score(7)
def test_words():
    check_io(
        test_files / "words.txt",
        "words.py"
    )
