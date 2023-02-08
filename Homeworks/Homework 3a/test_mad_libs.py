from byu_pytest_utils import check_io, max_score, test_files


@max_score(5)
def test_mad_libs_short():
    check_io(
        test_files / "mad-libs-short.txt",
        "mad_libs_short.py"
    )


@max_score(5)
def test_mad_libs():
    check_io(
        test_files / "mad-libs.txt",
        "mad_libs.py"
    )
