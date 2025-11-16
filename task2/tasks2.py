#!/usr/bin/env python3
"""
Enhanced command-line task management application.
Stores tasks in a JSON file with priorities, due dates, assignments, and subtasks.
"""

import json
import os
import sys
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: {TASKS_FILE} is corrupted. Starting with empty task list.")
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description, priority=None, due_date=None, assigned_to=None):
    """Add a new task."""
    tasks = load_tasks()
    
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'created': datetime.now().isoformat(),
        'completed': False,
        'priority': priority or 'medium',
        'due_date': due_date,
        'assigned_to': assigned_to,
        'subtasks': []
    }
    
    tasks.append(task)
    save_tasks(tasks)
    
    print(f"✓ Task added: {description} (ID: {task['id']})")
    if priority:
        print(f"  Priority: {priority}")
    if due_date:
        print(f"  Due: {due_date}")
    if assigned_to:
        print(f"  Assigned to: {assigned_to}")

def list_tasks(show_all=False, filter_priority=None, filter_assigned=None):
    """List all tasks or only incomplete tasks with optional filters."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    # Apply filters
    filtered_tasks = tasks
    if filter_priority:
        filtered_tasks = [t for t in filtered_tasks if t.get('priority') == filter_priority]
    if filter_assigned:
        filtered_tasks = [t for t in filtered_tasks if t.get('assigned_to') == filter_assigned]
    
    if not filtered_tasks:
        print("No tasks match the filter criteria.")
        return
    
    print("\n" + "="*70)
    print("TASKS")
    print("="*70)
    
    for task in filtered_tasks:
        if not show_all and task['completed']:
            continue
        
        priority_icons = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}
        priority_icon = priority_icons.get(task.get('priority', 'medium'), '⚪')
        status = "✓" if task['completed'] else "○"
        
        print(f"{status} {priority_icon} [{task['id']}] {task['description']}")
        print(f"   Created: {task['created'][:10]}")
        
        if task.get('priority'):
            print(f"   Priority: {task['priority'].upper()}")
        
        if task.get('due_date'):
            print(f"   Due: {task['due_date']}")
        
        if task.get('assigned_to'):
            print(f"   Assigned to: {task['assigned_to']}")
        
        if task.get('subtasks'):
            print(f"   Subtasks: {len(task['subtasks'])} total")
            for i, subtask in enumerate(task['subtasks'], 1):
                sub_status = "✓" if subtask['completed'] else "○"
                print(f"     {sub_status} {i}. {subtask['description']}")
        
        if task['completed']:
            print(f"   Status: COMPLETED")
        
        print()

def search_tasks(query):
    """Search tasks by keyword."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    query_lower = query.lower()
    matches = [t for t in tasks if query_lower in t['description'].lower()]
    
    if not matches:
        print(f"No tasks found matching '{query}'")
        return
    
    print(f"\nFound {len(matches)} task(s) matching '{query}':")
    print("="*70)
    
    for task in matches:
        priority_icons = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}
        priority_icon = priority_icons.get(task.get('priority', 'medium'), '⚪')
        status = "✓" if task['completed'] else "○"
        print(f"{status} {priority_icon} [{task['id']}] {task['description']}")
        if task.get('due_date'):
            print(f"   Due: {task['due_date']}")
        print()

def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print(f"✓ Task {task_id} marked as completed: {task['description']}")
            return
    
    print(f"Error: Task {task_id} not found.")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted_task = tasks.pop(i)
            save_tasks(tasks)
            print(f"✓ Task {task_id} deleted: {deleted_task['description']}")
            return
    
    print(f"Error: Task {task_id} not found.")

def set_priority(task_id, priority):
    """Set priority for a task."""
    valid_priorities = ['low', 'medium', 'high']
    if priority.lower() not in valid_priorities:
        print(f"Error: Priority must be one of: {', '.join(valid_priorities)}")
        return
    
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['priority'] = priority.lower()
            save_tasks(tasks)
            print(f"✓ Task {task_id} priority set to: {priority.upper()}")
            return
    
    print(f"Error: Task {task_id} not found.")

def set_due_date(task_id, due_date):
    """Set due date for a task."""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['due_date'] = due_date
            save_tasks(tasks)
            print(f"✓ Task {task_id} due date set to: {due_date}")
            return
    
    print(f"Error: Task {task_id} not found.")

def assign_task(task_id, person):
    """Assign a task to someone."""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['assigned_to'] = person
            save_tasks(tasks)
            print(f"✓ Task {task_id} assigned to: {person}")
            return
    
    print(f"Error: Task {task_id} not found.")

def add_subtask(task_id, description):
    """Add a subtask to a task."""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            if 'subtasks' not in task:
                task['subtasks'] = []
            
            subtask = {
                'description': description,
                'completed': False,
                'created': datetime.now().isoformat()
            }
            
            task['subtasks'].append(subtask)
            save_tasks(tasks)
            print(f"✓ Subtask added to task {task_id}: {description}")
            return
    
    print(f"Error: Task {task_id} not found.")

def complete_subtask(task_id, subtask_number):
    """Mark a subtask as completed."""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            if 'subtasks' not in task or not task['subtasks']:
                print(f"Error: Task {task_id} has no subtasks.")
                return
            
            if subtask_number < 1 or subtask_number > len(task['subtasks']):
                print(f"Error: Subtask number must be between 1 and {len(task['subtasks'])}")
                return
            
            task['subtasks'][subtask_number - 1]['completed'] = True
            save_tasks(tasks)
            print(f"✓ Subtask {subtask_number} of task {task_id} marked as completed")
            return
    
    print(f"Error: Task {task_id} not found.")

def show_help():
    """Display help information."""
    help_text = """
Task Manager - Enhanced Command Line Task Management Tool

USAGE:
    python tasks.py <command> [arguments]

BASIC COMMANDS:
    add <description>           Add a new task
    list                        List all incomplete tasks
    list --all                  List all tasks (including completed)
    search <keyword>            Search tasks by keyword
    complete <id>               Mark a task as completed
    delete <id>                 Delete a task

PRIORITY COMMANDS:
    priority <id> <level>       Set task priority (low/medium/high)
    list --priority <level>     Filter tasks by priority level

DUE DATE COMMANDS:
    due <id> <date>             Set due date (format: YYYY-MM-DD)

ASSIGNMENT COMMANDS:
    assign <id> <person>        Assign task to someone
    list --assigned <person>    Filter tasks by assignee

SUBTASK COMMANDS:
    subtask <id> <description>  Add a subtask to a task
    subcomplete <id> <number>   Mark a subtask as completed

GENERAL:
    help                        Show this help message

EXAMPLES:
    # Basic usage
    python tasks.py add "Buy groceries"
    python tasks.py list
    
    # With priority
    python tasks.py add "Fix critical bug"
    python tasks.py priority 1 high
    
    # With due date
    python tasks.py due 1 2025-11-20
    
    # Assign to someone
    python tasks.py assign 1 "John"
    
    # Add subtasks
    python tasks.py subtask 1 "Buy milk"
    python tasks.py subtask 1 "Buy eggs"
    python tasks.py subcomplete 1 1
    
    # Filter tasks
    python tasks.py list --priority high
    python tasks.py list --assigned John
"""
    print(help_text)

def main():
    """Main entry point for the application."""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'add':
        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
            print("Usage: python tasks.py add <description>")
            return
        description = ' '.join(sys.argv[2:])
        add_task(description)
    
    elif command == 'list':
        show_all = False
        filter_priority = None
        filter_assigned = None
        
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == '--all':
                show_all = True
            elif sys.argv[i] == '--priority' and i + 1 < len(sys.argv):
                filter_priority = sys.argv[i + 1].lower()
                i += 1
            elif sys.argv[i] == '--assigned' and i + 1 < len(sys.argv):
                filter_assigned = sys.argv[i + 1]
                i += 1
            i += 1
        
        list_tasks(show_all, filter_priority, filter_assigned)
    
    elif command == 'search':
        if len(sys.argv) < 3:
            print("Error: Please provide a search keyword.")
            print("Usage: python tasks.py search <keyword>")
            return
        query = ' '.join(sys.argv[2:])
        search_tasks(query)
    
    elif command == 'complete':
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID.")
            print("Usage: python tasks.py complete <id>")
            return
        try:
            task_id = int(sys.argv[2])
            complete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number.")
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID.")
            print("Usage: python tasks.py delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number.")
    
    elif command == 'priority':
        if len(sys.argv) < 4:
            print("Error: Please provide task ID and priority level.")
            print("Usage: python tasks.py priority <id> <low/medium/high>")
            return
        try:
            task_id = int(sys.argv[2])
            priority = sys.argv[3]
            set_priority(task_id, priority)
        except ValueError:
            print("Error: Task ID must be a number.")
    
    elif command == 'due':
        if len(sys.argv) < 4:
            print("Error: Please provide task ID and due date.")
            print("Usage: python tasks.py due <id> <YYYY-MM-DD>")
            return
        try:
            task_id = int(sys.argv[2])
            due_date = sys.argv[3]
            set_due_date(task_id, due_date)
        except ValueError:
            print("Error: Task ID must be a number.")
    
    elif command == 'assign':
        if len(sys.argv) < 4:
            print("Error: Please provide task ID and person name.")
            print("Usage: python tasks.py assign <id> <person>")
            return
        try:
            task_id = int(sys.argv[2])
            person = ' '.join(sys.argv[3:])
            assign_task(task_id, person)
        except ValueError:
            print("Error: Task ID must be a number.")
    
    elif command == 'subtask':
        if len(sys.argv) < 4:
            print("Error: Please provide task ID and subtask description.")
            print("Usage: python tasks.py subtask <id> <description>")
            return
        try:
            task_id = int(sys.argv[2])
            description = ' '.join(sys.argv[3:])
            add_subtask(task_id, description)
        except ValueError:
            print("Error: Task ID must be a number.")
    
    elif command == 'subcomplete':
        if len(sys.argv) < 4:
            print("Error: Please provide task ID and subtask number.")
            print("Usage: python tasks.py subcomplete <id> <subtask_number>")
            return
        try:
            task_id = int(sys.argv[2])
            subtask_number = int(sys.argv[3])
            complete_subtask(task_id, subtask_number)
        except (ValueError, IndexError):
            print("Error: Task ID and subtask number must be numbers.")
    
    elif command == 'help':
        show_help()
    
    else:
        print(f"Error: Unknown command '{command}'")
        print("Run 'python tasks.py help' for usage information.")

if __name__ == '__main__':
    main()