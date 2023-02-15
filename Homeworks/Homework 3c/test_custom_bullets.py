from byu_pytest_utils import max_score, check_io, test_files


@max_score(7)
def test_custom_bullets():
    check_io(
        test_files / "custom_bullets.txt",
        "custom_bullets.py"
    )