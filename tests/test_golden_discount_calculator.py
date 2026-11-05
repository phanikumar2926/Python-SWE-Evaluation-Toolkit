import sys
from pathlib import Path
import pytest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "solutions")
)

from discount_calculator import calculate_discount


def test_10_percent_discount():
    assert calculate_discount(100, 10) == 90


def test_25_percent_discount():
    assert calculate_discount(100, 25) == 75


def test_zero_discount():
    assert calculate_discount(100, 0) == 100


def test_full_discount():
    assert calculate_discount(100, 100) == 0


def test_decimal_price():
    assert calculate_discount(99.99, 10) == pytest.approx(89.991)


def test_different_price_and_discount():
    assert calculate_discount(250, 20) == 200

def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_negative_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, -10)


def test_discount_above_100():
    with pytest.raises(ValueError):
        calculate_discount(100, 110)