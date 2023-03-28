from byu_pytest_utils import max_score, run_python, compare_files, this_folder, test_files


@max_score(5)
def test_postal_routing_unknown_bin():
    obs_file = "postal_bins.observed.txt"
    run_python(this_folder / "postal_routing.py", test_files / "addresses.txt", obs_file)
    compare_files(test_files / "postal_bins.expected.txt", obs_file)


@max_score(5)
def test_postal_routing_again():
    obs_file = "postal_bins_again.observed.txt"
    run_python(this_folder / "postal_routing.py", test_files / "more_addresses.txt", obs_file)
    compare_files(test_files / "postal_bins_again.expected.txt", obs_file)
