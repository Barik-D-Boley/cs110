from byu_pytest_utils import max_score, run_python, this_folder


def get_num_function_calls(filename, function):
    with open(filename) as file:
        num_calls = 0
        for line in file:
            if "def" not in line and function + "(" in line and ")" in line:
                num_calls += 1
    return num_calls


@max_score(5)
def test_write_your_own():
    num_calls = get_num_function_calls(this_folder / "write_your_own.py", "input")
    assert num_calls >= 3, "Your code should prompt input at least three times"
    output = run_python('write_your_own.py', stdin="1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11")
    assert len(output.splitlines()) >= 3, "Your code should print at least three lines of output"
