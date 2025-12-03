from eductools.math_tools import add, subtract


def test_add():
    assert 3 == add(1, 2)
    assert -1 == add(1, -2)


def test_substract():
    assert -1 == subtract(1, 2)
    assert 3 == subtract(1, -2)
