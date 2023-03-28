from byu_pytest_utils import max_score, compare_files, test_files, run_python, this_folder


@max_score(3)
def test_older_customers_30():
    run_python(this_folder / "older_customers.py", test_files / "customers.csv", "thirty.observed.csv", "30")
    compare_files("thirty.observed.csv", test_files / "thirty.expected.csv")


@max_score(4)
def test_older_customers_15():
    run_python(this_folder / "older_customers.py", test_files / "customers.csv", "fifteen.observed.csv", "15")
    compare_files("fifteen.observed.csv", test_files / "fifteen.expected.csv")
