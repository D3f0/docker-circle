from pathlib import Path
from subprocess import check_output
def test_version():
    assert True


def test_bar():
    assert False, "This test is not passing"


def test_ownership():
    ls_output = check_output('ls -l /test-results')
    print(ls_output)
