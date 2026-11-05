import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "tasks" / "bug-fixing")
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