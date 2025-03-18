from calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

from calculator import subtract

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1

from calculator import multiply

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0
