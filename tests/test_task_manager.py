import sys
from pathlib import Path

import pytest

TASK_DIR = Path(__file__).resolve().parents[1] / "candidate"
sys.path.insert(0, str(TASK_DIR))

from task_manager import TaskManager


def test_add_task():
    manager = TaskManager()

    task_id = manager.add_task("Learn Python")

    assert task_id == 1
    assert manager.list_tasks()[0]["description"] == "Learn Python"


def test_empty_task_rejected():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.add_task("")


def test_complete_task():
    manager = TaskManager()
    task_id = manager.add_task("Learn SQL")

    assert manager.complete_task(task_id) is True
    assert manager.list_tasks()[0]["completed"] is True


def test_missing_task():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.complete_task(999)


def test_multiple_tasks():
    manager = TaskManager()

    first = manager.add_task("Learn Python")
    second = manager.add_task("Learn SQL")

    assert first == 1
    assert second == 2
    assert len(manager.list_tasks()) == 2