from taskmgr.models import Task


def test_task_serialization():
    t = Task(id=1, title="Test", description="desc")
    d = t.to_dict()
    assert d["id"] == 1
    assert d["title"] == "Test"
    assert "createdAt" in d and "updatedAt" in d
