from math_series.series import fibonacci
from math_series.series import lucas



def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = '0'
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = '1'
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = '1'
    assert actual == expected



def test_lucas_zero():
    actual = lucas(0)
    expected = '2'
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = '1'
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = '3'
    assert actual == expected