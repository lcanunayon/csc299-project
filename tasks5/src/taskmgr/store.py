import json
import os
from typing import List, Optional, Dict, Any
from pathlib import Path
from .models import Task, now_iso


class FileStore:
    def __init__(self, path: Optional[str] = None):
        # Allow overriding the storage location via TASKS_DATA env var
        env_path = os.getenv("TASKS_DATA")
        self.path = Path(path or env_path or "data/tasks.json")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._write([])

    def _read(self) -> List[Dict[str, Any]]:
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: List[Dict[str, Any]]):
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _next_id(self, items: List[Dict[str, Any]]) -> int:
        if not items:
            return 1
        return max((item.get("id") or 0) for item in items) + 1

    def create(self, title: str, description: Optional[str] = None) -> Task:
        items = self._read()
        new_id = self._next_id(items)
        task = Task(id=new_id, title=title, description=description)
        items.append(task.to_dict())
        self._write(items)
        return task

    def list(self, completed: Optional[bool] = None) -> List[Task]:
        items = self._read()
        tasks = [Task.from_dict(d) for d in items]
        if completed is None:
            return tasks
        return [t for t in tasks if t.completed == completed]

    def get(self, id: int) -> Optional[Task]:
        items = self._read()
        for d in items:
            if d.get("id") == id:
                return Task.from_dict(d)
        return None

    def update(self, id: int, **fields) -> Optional[Task]:
        items = self._read()
        updated = None
        for i, d in enumerate(items):
            if d.get("id") == id:
                d.update(fields)
                d["updatedAt"] = now_iso()
                items[i] = d
                updated = Task.from_dict(d)
                break
        if updated:
            self._write(items)
        return updated

    def delete(self, id: int) -> bool:
        items = self._read()
        new_items = [d for d in items if d.get("id") != id]
        if len(new_items) == len(items):
            return False
        self._write(new_items)
        return True


# Simple in-memory store useful for tests
class MemoryStore:
    def __init__(self):
        self.items = []

    def create(self, title: str, description: Optional[str] = None) -> Task:
        new_id = (max((i.get("id") or 0 for i in self.items), default=0) + 1)
        task = Task(id=new_id, title=title, description=description)
        self.items.append(task.to_dict())
        return task

    def list(self, completed: Optional[bool] = None) -> List[Task]:
        tasks = [Task.from_dict(d) for d in self.items]
        if completed is None:
            return tasks
        return [t for t in tasks if t.completed == completed]

    def get(self, id: int) -> Optional[Task]:
        for d in self.items:
            if d.get("id") == id:
                return Task.from_dict(d)
        return None

    def update(self, id: int, **fields) -> Optional[Task]:
        for i, d in enumerate(self.items):
            if d.get("id") == id:
                d.update(fields)
                d["updatedAt"] = now_iso()
                self.items[i] = d
                return Task.from_dict(d)
        return None

    def delete(self, id: int) -> bool:
        before = len(self.items)
        self.items = [d for d in self.items if d.get("id") != id]
        return len(self.items) < before
