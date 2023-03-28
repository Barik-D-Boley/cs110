from byu_pytest_utils import max_score, this_folder, test_files, run_python, compare_files


@max_score(2)
def test_replace_word_sells_sold():
    infile = test_files / 'replace_word.input.txt'
    observed = 'replace_word_sells_to_sold.observed.txt'
    expected = test_files / 'replace_word_sells_to_sold.expected.txt'
    run_python(this_folder / 'replace_word.py', infile, observed, 'sells', 'sold')
    compare_files(expected, observed)


@max_score(2)
def test_replace_word_seashells_lemonade():
    infile = test_files / 'replace_word.input.txt'
    observed = 'replace_word_seashells_to_lemonade.observed.txt'
    expected = test_files / 'replace_word_seashells_to_lemonade.expected.txt'
    run_python(this_folder / 'replace_word.py', infile, observed, 'seashells', 'lemonade')
    compare_files(expected, observed)

