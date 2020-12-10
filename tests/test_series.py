from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series

def test_version():
    assert __version__ == '0.1.0'

# -------Fibonacci-------
# happy path
def test_fib_with_an_int():
    actual = fibonacci(3)
    expected = 2
    assert expected is actual, "Happy path test passes for fib seq"

#expected failure
def test_fib_with_a_str():
    actual = fibonacci("hi")
    expected = "Error"
    assert expected is actual, "Expected failure test passes"

#edge case
def test_fib_with_a_zero():
    actual = fibonacci(0)
    expected = 0
    assert expected is actual, "Edge case test passes"




# ------Lucas------
#happy path
def test_lucas_with_an_int():
    expected = 2
    actual = fibonacci(3)
    assert expected is actual, "Happy path test passes for lucas seq"

#expected failure
def test_lucas_with_a_str():
    actual = fibonacci("hi")
    expected = "Error"
    assert expected is actual, "Expected failure test passes"

#edge case
def test_lucas_with_a_two():
    actual = fibonacci(2)
    expected = 1
    assert expected is actual, "Edge case test passes"




# ------Sum Series------
#happy path
def test_sum_series_with_a_single_int():
    expected = 1
    actual = sum_series(2)
    assert expected is actual, "Happy path test passes for sum series seq"

def test_series_with_optional_params():
    expected = 53
    actual = sum_series(5, 6, 7)
    assert expected is actual, "Happy path test passes for sum series seq"

#expected failure
def test_sum_series_with_a_str():
    actual = sum_series("hi")
    expected = "Error"
    assert expected is actual, "Expected failure test passes"

#edge case
def test_sum_series_with_a_zero():
    actual = sum_series(0)
    expected = 0
    assert expected is actual, "Edge case test passes"