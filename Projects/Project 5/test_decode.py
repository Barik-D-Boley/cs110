from byu_pytest_utils import max_score, test_files, this_folder, run_python, compare_files
from test_encode import do_encode_test


@max_score(10)
def test_decode_simple():
    do_encode_test(
        "decode.py",
        "codex.csv",
        "simple.encoded.expected.txt",
        "simple.txt",
        "simple.decoded.observed.txt"
    )


@max_score(10)
def test_decode_message():
    do_encode_test(
        "decode.py",
        "codex.csv",
        "message.encoded.expected.txt",
        "message.txt",
        "message.decoded.observed.txt"
    )


@max_score(10)
def test_decode_nephi():
    do_encode_test(
        "decode.py",
        "codex.csv",
        "1Nephi.encoded.expected.txt",
        "1Nephi.txt",
        "1Nephi.decoded.observed.txt"
    )
