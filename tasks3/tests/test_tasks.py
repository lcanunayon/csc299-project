"""
Tests for the Task Manager application.
"""

import os
import tempfile
import pytest
from tasks3 import inc, Task, TaskManager


class TestIncFunction:
    """Tests for the inc function."""
    
    def test_inc(self):
        """Test that inc increments by 1."""
        assert inc(5) == 6
    
    def test_inc_negative(self):
        """Test inc with negative numbers."""
        assert inc(-1) == 0
    
    def test_inc_zero(self):
        """Test inc with zero."""
        assert inc(0) == 1


class TestTask:
    """Tests for the Task class."""
    
    def test_task_creation(self):
        """Test creating a basic task."""
        task = Task(1, "Test task")
        assert task.id == 1
        assert task.description == "Test task"
        assert task.priority == "medium"
        assert task.completed is False
        assert task.subtasks == []
    
    def test_task_with_priority(self):
        """Test creating a task with priority."""
        task = Task(1, "Urgent task", priority="high")
        assert task.priority == "high"
    
    def test_task_with_due_date(self):
        """Test creating a task with due date."""
        task = Task(1, "Deadline task", due_date="2025-12-31")
        assert task.due_date == "2025-12-31"
    
    def test_task_with_assignment(self):
        """Test creating a task with assignment."""
        task = Task(1, "Assigned task", assigned_to="Alice")
        assert task.assigned_to == "Alice"
    
    def test_add_subtask(self):
        """Test adding a subtask."""
        task = Task(1, "Main task")
        task.add_subtask("Subtask 1")
        assert len(task.subtasks) == 1
        assert task.subtasks[0]['description'] == "Subtask 1"
        assert task.subtasks[0]['completed'] is False
    
    def test_complete_subtask(self):
        """Test completing a subtask."""
        task = Task(1, "Main task")
        task.add_subtask("Subtask 1")
        task.add_subtask("Subtask 2")
        
        result = task.complete_subtask(0)
        assert result is True
        assert task.subtasks[0]['completed'] is True
        assert task.subtasks[1]['completed'] is False
    
    def test_complete_subtask_invalid_index(self):
        """Test completing a subtask with invalid index."""
        task = Task(1, "Main task")
        task.add_subtask("Subtask 1")
        
        result = task.complete_subtask(5)
        assert result is False
    
    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task(1, "Test task", priority="high")
        data = task.to_dict()
        
        assert data['id'] == 1
        assert data['description'] == "Test task"
        assert data['priority'] == "high"
        assert data['completed'] is False
    
    def test_task_from_dict(self):
        """Test creating task from dictionary."""
        data = {
            'id': 1,
            'description': "Test task",
            'priority': 'low',
            'due_date': '2025-12-01',
            'assigned_to': 'Bob',
            'completed': False,
            'created': '2025-11-15T10:00:00',
            'subtasks': []
        }
        
        task = Task.from_dict(data)
        assert task.id == 1
        assert task.description == "Test task"
        assert task.priority == "low"
        assert task.due_date == "2025-12-01"
        assert task.assigned_to == "Bob"


class TestTaskManager:
    """Tests for the TaskManager class."""
    
    @pytest.fixture
    def temp_file(self):
        """Create a temporary file for testing."""
        fd, path = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        yield path
        if os.path.exists(path):
            os.remove(path)
    
    @pytest.fixture
    def manager(self, temp_file):
        """Create a TaskManager instance with temporary file."""
        return TaskManager(temp_file)
    
    def test_add_task(self, manager):
        """Test adding a task."""
        task = manager.add_task("New task")
        assert task.id == 1
        assert task.description == "New task"
        assert len(manager.tasks) == 1
    
    def test_add_multiple_tasks(self, manager):
        """Test adding multiple tasks."""
        task1 = manager.add_task("Task 1")
        task2 = manager.add_task("Task 2")
        task3 = manager.add_task("Task 3")
        
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
        assert len(manager.tasks) == 3
    
    def test_add_task_with_priority(self, manager):
        """Test adding a task with priority."""
        task = manager.add_task("Urgent", priority="high")
        assert task.priority == "high"
    
    def test_get_task(self, manager):
        """Test retrieving a task by ID."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        
        task = manager.get_task(2)
        assert task is not None
        assert task.description == "Task 2"
    
    def test_get_task_not_found(self, manager):
        """Test retrieving a non-existent task."""
        task = manager.get_task(999)
        assert task is None
    
    def test_delete_task(self, manager):
        """Test deleting a task."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        
        result = manager.delete_task(1)
        assert result is True
        assert len(manager.tasks) == 1
        assert manager.get_task(1) is None
    
    def test_delete_task_not_found(self, manager):
        """Test deleting a non-existent task."""
        result = manager.delete_task(999)
        assert result is False
    
    def test_complete_task(self, manager):
        """Test completing a task."""
        task = manager.add_task("Task 1")
        assert task.completed is False
        
        result = manager.complete_task(1)
        assert result is True
        assert task.completed is True
    
    def test_complete_task_not_found(self, manager):
        """Test completing a non-existent task."""
        result = manager.complete_task(999)
        assert result is False
    
    def test_list_tasks_incomplete_only(self, manager):
        """Test listing only incomplete tasks."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.complete_task(1)
        
        tasks = manager.list_tasks(show_all=False)
        assert len(tasks) == 1
        assert tasks[0].description == "Task 2"
    
    def test_list_tasks_all(self, manager):
        """Test listing all tasks."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.complete_task(1)
        
        tasks = manager.list_tasks(show_all=True)
        assert len(tasks) == 2
    
    def test_list_tasks_by_priority(self, manager):
        """Test filtering tasks by priority."""
        manager.add_task("Task 1", priority="high")
        manager.add_task("Task 2", priority="low")
        manager.add_task("Task 3", priority="high")
        
        tasks = manager.list_tasks(priority="high")
        assert len(tasks) == 2
        assert all(t.priority == "high" for t in tasks)
    
    def test_list_tasks_by_assignment(self, manager):
        """Test filtering tasks by assignee."""
        manager.add_task("Task 1", assigned_to="Alice")
        manager.add_task("Task 2", assigned_to="Bob")
        manager.add_task("Task 3", assigned_to="Alice")
        
        tasks = manager.list_tasks(assigned_to="Alice")
        assert len(tasks) == 2
        assert all(t.assigned_to == "Alice" for t in tasks)
    
    def test_search_tasks(self, manager):
        """Test searching tasks by keyword."""
        manager.add_task("Buy groceries")
        manager.add_task("Buy books")
        manager.add_task("Read books")
        
        tasks = manager.search_tasks("buy")
        assert len(tasks) == 2
        
        tasks = manager.search_tasks("books")
        assert len(tasks) == 2
    
    def test_search_tasks_case_insensitive(self, manager):
        """Test that search is case-insensitive."""
        manager.add_task("Important Meeting")
        
        tasks = manager.search_tasks("meeting")
        assert len(tasks) == 1
        
        tasks = manager.search_tasks("IMPORTANT")
        assert len(tasks) == 1
    
    def test_set_priority(self, manager):
        """Test setting task priority."""
        task = manager.add_task("Task 1")
        assert task.priority == "medium"
        
        result = manager.set_priority(1, "high")
        assert result is True
        assert task.priority == "high"
    
    def test_set_priority_invalid(self, manager):
        """Test setting invalid priority."""
        manager.add_task("Task 1")
        
        result = manager.set_priority(1, "invalid")
        assert result is False
    
    def test_set_due_date(self, manager):
        """Test setting task due date."""
        task = manager.add_task("Task 1")
        assert task.due_date is None
        
        result = manager.set_due_date(1, "2025-12-31")
        assert result is True
        assert task.due_date == "2025-12-31"
    
    def test_assign_task(self, manager):
        """Test assigning a task."""
        task = manager.add_task("Task 1")
        assert task.assigned_to is None
        
        result = manager.assign_task(1, "Alice")
        assert result is True
        assert task.assigned_to == "Alice"
    
    def test_persistence(self, temp_file):
        """Test that tasks persist across manager instances."""
        # Create first manager and add tasks
        manager1 = TaskManager(temp_file)
        manager1.add_task("Task 1", priority="high")
        manager1.add_task("Task 2", priority="low")
        
        # Create second manager and verify tasks loaded
        manager2 = TaskManager(temp_file)
        assert len(manager2.tasks) == 2
        assert manager2.tasks[0].description == "Task 1"
        assert manager2.tasks[0].priority == "high"
        assert manager2.tasks[1].description == "Task 2"
    
    def test_empty_task_list(self, manager):
        """Test operations on empty task list."""
        assert len(manager.tasks) == 0
        assert manager.list_tasks() == []
        assert manager.search_tasks("test") == []
        assert manager.get_task(1) is None