import sys
from pathlib import Path

import pytest

TASK_DIR = Path(__file__).resolve().parents[1] / "candidate"
sys.path.insert(0, str(TASK_DIR))

from user_validation import validate_user, validate_registration


@pytest.mark.parametrize(
    "name, email, age, expected",
    [
        ("Phani", "phani@example.com", 25, True),
        ("John", "john@example.com", 18, True),
        ("John", "john@example.com", 17, False),
        ("", "john@example.com", 25, False),
        ("John", "", 25, False),
        (None, "john@example.com", 25, False),
        ("John", None, 25, False),
    ],
)
def test_validate_user(name, email, age, expected):
    assert validate_user(name, email, age) == expected


def test_registration_reuses_validation():
    assert validate_registration("Phani", "phani@example.com", 25) is True
    assert validate_registration("John", "", 25) is False