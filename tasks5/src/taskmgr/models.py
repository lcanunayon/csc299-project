from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional, Dict, Any


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Task:
    id: Optional[int]
    title: str
    description: Optional[str] = None
    completed: bool = False
    createdAt: str = field(default_factory=now_iso)
    updatedAt: str = field(default_factory=now_iso)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> 'Task':
        return Task(
            id=d.get("id"),
            title=d["title"],
            description=d.get("description"),
            completed=d.get("completed", False),
            createdAt=d.get("createdAt", now_iso()),
            updatedAt=d.get("updatedAt", now_iso()),
        )
