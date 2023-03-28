from byu_pytest_utils import max_score, run_python, compare_files, this_folder, test_files


@max_score(5)
def test_auto_correct():
    obs_file = "neat.observed.txt"
    run_python(this_folder / "auto_correct.py", test_files / "sloppy.txt", obs_file)
    compare_files(test_files / "neat.expected.txt", obs_file)


@max_score(5)
def test_auto_correct_again():
    obs_file = "neat_again.observed.txt"
    run_python(this_folder / "auto_correct.py", test_files / "another_sloppy.txt", obs_file)
    compare_files(test_files / "neat_again.expected.txt", obs_file)
