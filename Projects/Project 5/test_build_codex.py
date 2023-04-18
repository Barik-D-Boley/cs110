from byu_pytest_utils import max_score, this_folder, run_python
import string


@max_score(10)
def test_build():
    codex_file = this_folder / "codex.observed.csv"
    codex_file.unlink(missing_ok=True)
    run_python("build_codex.py", codex_file)

    sources = []
    targets = []
    with open(codex_file) as file:
        for line in file:
            s, t = line.strip().split(',')
            sources.append(s)
            targets.append(t)

    for c in string.ascii_lowercase:
        if c not in sources:
            raise Exception(f'"{c}" not found as key in codex')

    for c in string.ascii_lowercase:
        if c not in targets:
            raise Exception(f'"{c}" not found as value in codex')
