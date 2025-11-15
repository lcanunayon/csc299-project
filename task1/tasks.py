#!/usr/bin/env python3
"""
Simple command-line task management application.
Stores tasks in a JSON file with add, list, and search functionality.
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

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'created': datetime.now().isoformat(),
        'completed': False
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print(f"✓ Task added: {description} (ID: {task['id']})")

def list_tasks(show_all=False):
    """List all tasks or only incomplete tasks."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n" + "="*60)
    print("TASKS")
    print("="*60)
    
    for task in tasks:
        if not show_all and task['completed']:
            continue
            
        status = "✓" if task['completed'] else "○"
        print(f"{status} [{task['id']}] {task['description']}")
        print(f"   Created: {task['created'][:10]}")
        
        if task['completed']:
            print(f"   Completed")
        
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
    print("="*60)
    
    for task in matches:
        status = "✓" if task['completed'] else "○"
        print(f"{status} [{task['id']}] {task['description']}")
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

def show_help():
    """Display help information."""
    help_text = """
Task Manager - Command Line Task Management Tool

USAGE:
    python tasks.py <command> [arguments]

COMMANDS:
    add <description>       Add a new task
    list                    List all incomplete tasks
    list --all              List all tasks (including completed)
    search <keyword>        Search tasks by keyword
    complete <id>           Mark a task as completed
    delete <id>             Delete a task
    help                    Show this help message

EXAMPLES:
    python tasks.py add "Buy groceries"
    python tasks.py list
    python tasks.py search groceries
    python tasks.py complete 1
    python tasks.py delete 2
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
        show_all = len(sys.argv) > 2 and sys.argv[2] == '--all'
        list_tasks(show_all)
    
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
    
    elif command == 'help':
        show_help()
    
    else:
        print(f"Error: Unknown command '{command}'")
        print("Run 'python tasks.py help' for usage information.")

if __name__ == '__main__':
    main()