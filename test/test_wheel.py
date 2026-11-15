import importlib.util
import subprocess
import sys
from pathlib import Path


def test_importable():
    for importable in ["openroad", "odb", "openroad_bin"]:
        assert importlib.util.find_spec(importable) is not None, (
            f"was not able to find {importable}"
        )


def test_bin_solo():
    import openroad_bin.__main__

    wrapper = Path(openroad_bin.__main__.__file__)

    bin = wrapper.parent / "openroad"
    bin.unlink(missing_ok=True)

    SOLO_TEST_STR = "solo test ok"
    p = subprocess.Popen(
        [sys.executable, wrapper, "-no_splash", "-exit"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        encoding="utf8",
    )
    p.stdin.write(f'puts "{SOLO_TEST_STR}"\n')
    p.stdin.close()
    result = p.wait()
    assert result == 0, "openroad had a non-zero exit"
    solo_stdout = p.stdout.read()
    assert SOLO_TEST_STR in solo_stdout, (
        f"did not find '{SOLO_TEST_STR}' in stdout, found '{solo_stdout}'"
    )


def test_bin_multi():
    import openroad_bin.__main__

    wrapper = Path(openroad_bin.__main__.__file__)

    bin = wrapper.parent / "openroad"
    bin.unlink(missing_ok=True)

    MULTI_TEST_STR = "multi test %d ok"
    processes = []
    for i in range(3):
        p = subprocess.Popen(
            [sys.executable, wrapper, "-exit"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            encoding="utf8",
        )
        p.stdin.write(f'puts "{MULTI_TEST_STR}"\n' % i)
        p.stdin.close()
    assert all(p.wait() == 0 for p in processes), (
        "one or more openroad parallel processes had a non-zero exit"
    )
    for i, process in enumerate(processes):
        multi_stdout = process.stdout.read()
        current_test = MULTI_TEST_STR % i
        assert current_test in multi_stdout, (
            f"did not find '{current_test}' in stdout for process {i}, found '{multi_stdout}'"
        )
