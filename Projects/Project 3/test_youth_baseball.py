from byu_pytest_utils import max_score, test_files, check_io


@max_score(50)
def test_input_output_1():
    check_io(
        test_files / "baseball1.txt",
        "youth_baseball.py"
    )


@max_score(50)
def test_input_output2():
    check_io(
        test_files / "baseball2.txt",
        "youth_baseball.py"
    )
