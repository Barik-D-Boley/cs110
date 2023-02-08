from byu_pytest_utils import check_io, max_score, test_files


@max_score(5)
def test_wendys():
    check_io(
        test_files / 'wendys.txt',
        'wendys.py'
    )
