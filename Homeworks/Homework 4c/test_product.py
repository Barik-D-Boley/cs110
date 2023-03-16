from byu_pytest_utils import max_score, test_files, dialog


@max_score(1)
@dialog(test_files / 'prod.txt', 'product.py', '1', '2', '3', '4')
def test_product(group_name): ...


@max_score(1)
@dialog(test_files / 'another_prod.txt', 'product.py', '2', '-2', '2', '4')
def test_another_product(group_name): ...

