from byu_pytest_utils import max_score, test_files, this_folder, run_python, compare_files


def do_encode_test(script, codex, start, expected, observed):
    decoded_file = this_folder / observed
    decoded_file.unlink(missing_ok=True)
    run_python(
        script,
        test_files / codex,
        test_files / start,
        decoded_file
    )
    compare_files(
        test_files / expected,
        decoded_file
    )


@max_score(10)
def test_encode_simple():
    do_encode_test(
        "encode.py",
        "codex.csv",
        "simple.txt",
        "simple.encoded.expected.txt",
        "simple.encoded.observed.txt"
    )


@max_score(10)
def test_encode_message():
    do_encode_test(
        "encode.py",
        "codex.csv",
        "message.txt",
        "message.encoded.expected.txt",
        "message.encoded.observed.txt"
    )


@max_score(10)
def test_encode_nephi():
    do_encode_test(
        "encode.py",
        "codex.csv",
        "1Nephi.txt",
        "1Nephi.encoded.expected.txt",
        "1Nephi.encoded.observed.txt"
    )