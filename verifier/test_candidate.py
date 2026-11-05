
import sys
import random
from pathlib import Path

import pytest

# Load the candidate implementation
TASK_DIR = Path(__file__).resolve().parents[1] / "candidate"
sys.path.insert(0, str(TASK_DIR))

from discount_calculator import calculate_discount


@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (100, 10, 90),
        (100, 25, 75),
        (200, 5, 190),
        (500, 15, 425),
        (1000, 50, 500),
        (75, 20, 60),
        (100, 100, 0),
        (100, 0, 100),
        (0, 50, 0),
        (99.99, 10, 89.991),
    ],
)
def test_discount_calculation(price, discount, expected):
    assert calculate_discount(price, discount) == pytest.approx(expected)


@pytest.mark.parametrize(
    "price, discount",
    [
        (-100, 10),
        (100, -1),
        (100, 101),
    ],
)
def test_invalid_inputs(price, discount):
    with pytest.raises(ValueError):
        calculate_discount(price, discount)


def test_deterministic_varied_inputs():
    rng = random.Random(42)

    for _ in range(100):
        price = round(rng.uniform(1, 10000), 2)
        discount = rng.randint(0, 100)

        expected = price * (1 - discount / 100)

        result = calculate_discount(price, discount)

        assert result == pytest.approx(expected)
