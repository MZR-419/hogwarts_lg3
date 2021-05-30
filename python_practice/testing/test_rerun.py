import pytest


def test_a():
    print("aaaaaa")

def test_b():
    assert False

@pytest.mark.flaky(reruns=5)
def test_example():
    # import random
    # assert random.choice([True, False])
    assert False

def test_assume():
    pytest.assume(1 == 4)
    pytest.assume(2 == 4)
    pytest.assume(4 == 4)