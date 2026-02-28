"""Unit tests for the calculator.

These tests focus on:
- normal happy paths (ints + floats)
- negative numbers
- zero handling
- divide-by-zero error behavior
"""

import pytest

from mypackage.calculator import add, subtract, multiply, divide





@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-2, 3, 1),
        (0, 0, 0),
        (-2.5, -1.5, -4.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, 5),
        (5, 10, -5),
        (2.5, 1.5, 1.0),
        (0, 7, -7),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 4, 12),
        (-3, 4, -12),
        (0, 999, 0),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (-10, 2, -5),
        (10, -2, -5),
        (-10, -2, 5),
    ],
)
def test_divide_int_result(a, b, expected):
    assert divide(a, b) == expected


def test_divide_float_result():
    # 1 / 3 is repeating decimal so use approx
    assert divide(1, 3) == pytest.approx(0.3333333333, rel=1e-9)


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

