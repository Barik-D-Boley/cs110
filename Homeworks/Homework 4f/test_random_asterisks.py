from byu_pytest_utils import max_score, with_import


@max_score(1)
@with_import
def test_random_asterisks_zero(random_asterisks):
    text = " ".join(["a" * i for i in range(1000)])
    result = random_asterisks(text, 0)
    assert result.count("*") == 0


@max_score(1)
@with_import
def test_random_asterisks_one(random_asterisks):
    text = " ".join(["a" * i for i in range(1000)])
    result = random_asterisks(text, 1)
    assert result.count('*') / len(result) > 0.99


@max_score(1)
@with_import
def test_random_asterisks_half_a(random_asterisks):
    text = " ".join(["a"] * 1000)
    result = random_asterisks(text, 0.5)
    result = ''.join(result.split())  # remove all whitespace
    assert 0.45 < result.count('*') / len(result) < 0.55


@max_score(1)
@with_import
def test_random_asterisks_half_aa(random_asterisks):
    text = " ".join(["aa"] * 1000)
    result = random_asterisks(text, 0.5)
    result = ''.join(result.split())  # remove all whitespace
    assert 0.45 < result.count('*') / len(result) < 0.55


@max_score(1)
@with_import
def test_random_asterisks_half_aaa(random_asterisks):
    text = " ".join(["aaa"] * 1000)
    result = random_asterisks(text, 0.5)
    result = ''.join(result.split())  # remove all whitespace
    assert 0.45 < result.count('*') / len(result) < 0.55
