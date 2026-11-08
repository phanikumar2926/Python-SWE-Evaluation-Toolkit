import sys
from pathlib import Path

TASK_DIR = Path(__file__).resolve().parents[1] / "candidate"
sys.path.insert(0, str(TASK_DIR))

from duplicate_detection import find_duplicates


def test_find_duplicates():
    assert set(find_duplicates([1, 2, 2, 3, 3, 4])) == {2, 3}


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4]) == []


def test_empty_list():
    assert find_duplicates([]) == []


def test_duplicate_appears_once():
    assert set(find_duplicates([5, 5, 5, 5])) == {5}


def test_large_list():
    numbers = list(range(10000)) + [100, 200, 300]

    assert set(find_duplicates(numbers)) == {100, 200, 300}