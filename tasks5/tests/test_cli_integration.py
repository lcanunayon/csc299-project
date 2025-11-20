import io
import sys
import pytest
from contextlib import redirect_stdout

from taskmgr import cli


def call_cli(args):
    f = io.StringIO()
    with redirect_stdout(f):
        rc = cli.main(args)
    return rc, f.getvalue()


@pytest.fixture(autouse=True)
def clear_store(tmp_path, monkeypatch):
    # Use an in-memory store by pointing FileStore to a tmp file path
    monkeypatch.setenv("TASKS_DATA", str(tmp_path / "tasks.json"))
    # Ensure any existing in-memory state is cleared by reloading modules if needed
    yield


def test_add_task_shows_title():
    rc, out = call_cli(["add", "Buy milk"])
    assert rc == 0
    assert "Buy milk" in out


def test_list_shows_added_task():
    call_cli(["add", "Buy milk"])
    rc, out = call_cli(["list"])
    assert rc == 0
    assert "Buy milk" in out


def test_complete_task_and_list_shows_completed():
    call_cli(["add", "A"])
    # add a 'done' command to mark completed
    rc, out = call_cli(["done", "1"])
    assert rc == 0
    rc, out = call_cli(["list"])
    assert rc == 0
    assert "completed=True" in out or "completed=true" in out


def test_done_invalid_id_returns_error_and_not_found_message():
    rc, out = call_cli(["done", "999"])
    assert rc != 0
    assert "not found" in out.lower()


def test_list_no_tasks_prints_no_tasks():
    rc, out = call_cli(["list"])
    assert rc == 0
    assert "no tasks" in out.lower() or out.strip() == ""
