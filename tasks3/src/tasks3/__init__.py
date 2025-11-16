"""
Task Manager - A command-line task management application.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional

def inc(n: int) -> int:
    """Increment function for testing."""
    return n + 1


class Task:
    """Represents a single task."""
    
    def __init__(
        self,
        task_id: int,
        description: str,
        priority: str = "medium",
        due_date: Optional[str] = None,
        assigned_to: Optional[str] = None
    ):
        self.id = task_id
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.completed = False
        self.created = datetime.now().isoformat()
        self.subtasks: List[Dict] = []
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary."""
        return {
            'id': self.id,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'assigned_to': self.assigned_to,
            'completed': self.completed,
            'created': self.created,
            'subtasks': self.subtasks
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary."""
        task = cls(
            task_id=data['id'],
            description=data['description'],
            priority=data.get('priority', 'medium'),
            due_date=data.get('due_date'),
            assigned_to=data.get('assigned_to')
        )
        task.completed = data.get('completed', False)
        task.created = data.get('created', datetime.now().isoformat())
        task.subtasks = data.get('subtasks', [])
        return task
    
    def add_subtask(self, description: str):
        """Add a subtask."""
        subtask = {
            'description': description,
            'completed': False,
            'created': datetime.now().isoformat()
        }
        self.subtasks.append(subtask)
    
    def complete_subtask(self, subtask_index: int) -> bool:
        """Mark a subtask as completed."""
        if 0 <= subtask_index < len(self.subtasks):
            self.subtasks[subtask_index]['completed'] = True
            return True
        return False


class TaskManager:
    """Manages a collection of tasks."""
    
    def __init__(self, filename: str = 'tasks.json'):
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        if not os.path.exists(self.filename):
            self.tasks = []
            return
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in data]
        except (json.JSONDecodeError, KeyError):
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(self.filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)
    
    def add_task(
        self,
        description: str,
        priority: str = "medium",
        due_date: Optional[str] = None,
        assigned_to: Optional[str] = None
    ) -> Task:
        """Add a new task."""
        task_id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(task_id, description, priority, due_date, assigned_to)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                return True
        return False
    
    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        task = self.get_task(task_id)
        if task:
            task.completed = True
            self.save_tasks()
            return True
        return False
    
    def list_tasks(
        self,
        show_all: bool = False,
        priority: Optional[str] = None,
        assigned_to: Optional[str] = None
    ) -> List[Task]:
        """List tasks with optional filters."""
        filtered = self.tasks
        
        if not show_all:
            filtered = [t for t in filtered if not t.completed]
        
        if priority:
            filtered = [t for t in filtered if t.priority == priority]
        
        if assigned_to:
            filtered = [t for t in filtered if t.assigned_to == assigned_to]
        
        return filtered
    
    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by keyword."""
        query_lower = query.lower()
        return [t for t in self.tasks if query_lower in t.description.lower()]
    
    def set_priority(self, task_id: int, priority: str) -> bool:
        """Set task priority."""
        if priority not in ['low', 'medium', 'high']:
            return False
        
        task = self.get_task(task_id)
        if task:
            task.priority = priority
            self.save_tasks()
            return True
        return False
    
    def set_due_date(self, task_id: int, due_date: str) -> bool:
        """Set task due date."""
        task = self.get_task(task_id)
        if task:
            task.due_date = due_date
            self.save_tasks()
            return True
        return False
    
    def assign_task(self, task_id: int, person: str) -> bool:
        """Assign task to someone."""
        task = self.get_task(task_id)
        if task:
            task.assigned_to = person
            self.save_tasks()
            return True
        return False


def main():
    """Main entry point for the application."""
    import sys
    
    if len(sys.argv) < 2:
        print("Task Manager")
        print("Usage: uv run tasks3 <command> [args]")
        print("Commands: add, list, complete, delete, search, priority, due, assign")
        return
    
    manager = TaskManager()
    command = sys.argv[1].lower()
    
    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: uv run tasks3 add <description>")
            return
        description = ' '.join(sys.argv[2:])
        task = manager.add_task(description)
        print(f"✓ Task added: {task.description} (ID: {task.id})")
    
    elif command == 'list':
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print(f"\n{'='*60}")
            print("TASKS")
            print(f"{'='*60}")
            for task in tasks:
                status = "✓" if task.completed else "○"
                print(f"{status} [{task.id}] {task.description}")
                print(f"   Priority: {task.priority.upper()}")
                if task.due_date:
                    print(f"   Due: {task.due_date}")
                if task.assigned_to:
                    print(f"   Assigned to: {task.assigned_to}")
                print()
    
    elif command == 'complete':
        if len(sys.argv) < 3:
            print("Usage: uv run tasks3 complete <id>")
            return
        try:
            task_id = int(sys.argv[2])
            if manager.complete_task(task_id):
                print(f"✓ Task {task_id} marked as completed")
            else:
                print(f"Error: Task {task_id} not found")
        except ValueError:
            print("Error: Task ID must be a number")
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: uv run tasks3 delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
            if manager.delete_task(task_id):
                print(f"✓ Task {task_id} deleted")
            else:
                print(f"Error: Task {task_id} not found")
        except ValueError:
            print("Error: Task ID must be a number")
    
    elif command == 'search':
        if len(sys.argv) < 3:
            print("Usage: uv run tasks3 search <keyword>")
            return
        query = ' '.join(sys.argv[2:])
        tasks = manager.search_tasks(query)
        if not tasks:
            print(f"No tasks found matching '{query}'")
        else:
            print(f"\nFound {len(tasks)} task(s):")
            for task in tasks:
                status = "✓" if task.completed else "○"
                print(f"{status} [{task.id}] {task.description}")
    
    elif command == 'priority':
        if len(sys.argv) < 4:
            print("Usage: uv run tasks3 priority <id> <low/medium/high>")
            return
        try:
            task_id = int(sys.argv[2])
            priority = sys.argv[3].lower()
            if manager.set_priority(task_id, priority):
                print(f"✓ Task {task_id} priority set to: {priority.upper()}")
            else:
                print(f"Error: Invalid priority or task not found")
        except ValueError:
            print("Error: Task ID must be a number")
    
    else:
        print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()