# Task Manager CLI - Enhanced Edition

A comprehensive command-line task management application with priorities, due dates, assignments, and subtasks. All data is stored persistently in a JSON file.

## Features

- ✅ Add and manage tasks
- 📝 List and filter tasks
- 🔍 Search tasks by keyword
- 🎯 **Set priorities** (low, medium, high)
- 📅 **Set due dates**
- 👤 **Assign tasks to people**
- 📋 **Create subtasks** for complex tasks
- ✓ Mark tasks and subtasks as completed
- 🗑️ Delete tasks
- 💾 Persistent storage using JSON

## Installation

No installation required! Just Python 3.6+ is needed.

## Basic Usage

### Add a Task

```bash
python tasks.py add "Task description"
```

Example:
```bash
python tasks.py add "Buy groceries"
python tasks.py add "Finish homework"
```

### List Tasks

List incomplete tasks only:
```bash
python tasks.py list
```

List all tasks (including completed):
```bash
python tasks.py list --all
```

### Search Tasks

```bash
python tasks.py search "keyword"
```

### Complete a Task

```bash
python tasks.py complete <task_id>
```

### Delete a Task

```bash
python tasks.py delete <task_id>
```

## Advanced Features

### Priority Management

Set task priority (low, medium, or high):
```bash
python tasks.py priority <task_id> <level>
```

Examples:
```bash
python tasks.py priority 1 high
python tasks.py priority 2 low
python tasks.py priority 3 medium
```

Filter tasks by priority:
```bash
python tasks.py list --priority high
python tasks.py list --priority medium
python tasks.py list --priority low
```

**Visual indicators:**
- 🔴 High priority
- 🟡 Medium priority
- 🟢 Low priority

### Due Dates

Set a due date for a task (format: YYYY-MM-DD):
```bash
python tasks.py due <task_id> <date>
```

Examples:
```bash
python tasks.py due 1 2025-11-20
python tasks.py due 2 2025-12-01
```

### Task Assignment

Assign a task to someone:
```bash
python tasks.py assign <task_id> <person_name>
```

Examples:
```bash
python tasks.py assign 1 "Alice"
python tasks.py assign 2 "Bob Smith"
```

Filter tasks by assignee:
```bash
python tasks.py list --assigned Alice
```

### Subtasks

Add subtasks to break down complex tasks:
```bash
python tasks.py subtask <task_id> <subtask_description>
```

Examples:
```bash
python tasks.py subtask 1 "Buy milk"
python tasks.py subtask 1 "Buy eggs"
python tasks.py subtask 1 "Buy bread"
```

Complete a subtask (use the subtask number shown in list):
```bash
python tasks.py subcomplete <task_id> <subtask_number>
```

Example:
```bash
python tasks.py subcomplete 1 1   # Completes first subtask
python tasks.py subcomplete 1 2   # Completes second subtask
```

## Complete Workflow Example

```bash
# Create a project task
python tasks.py add "Complete CSC299 project"

# Set it as high priority
python tasks.py priority 1 high

# Set a due date
python tasks.py due 1 2025-11-30

# Assign it to yourself
python tasks.py assign 1 "Your Name"

# Add subtasks to break it down
python tasks.py subtask 1 "Write code"
python tasks.py subtask 1 "Write tests"
python tasks.py subtask 1 "Write documentation"
python tasks.py subtask 1 "Submit to GitHub"

# View your task with all details
python tasks.py list

# Complete subtasks as you go
python tasks.py subcomplete 1 1
python tasks.py subcomplete 1 2

# When everything is done
python tasks.py complete 1
```

## Advanced Filtering

Combine multiple filters:

```bash
# Show all high-priority tasks
python tasks.py list --priority high

# Show all tasks assigned to Alice
python tasks.py list --assigned Alice

# Show all tasks (including completed) with high priority
python tasks.py list --all --priority high
```

## Data Storage

Tasks are stored in `tasks.json` in the same directory. The file is created automatically.

### Enhanced Task Structure

Each task now contains:
- `id`: Unique identifier
- `description`: Task description
- `created`: Timestamp when created
- `completed`: Completion status
- `priority`: low, medium, or high (default: medium)
- `due_date`: Optional due date
- `assigned_to`: Optional assignee name
- `subtasks`: Array of subtasks, each with:
  - `description`: Subtask description
  - `completed`: Subtask completion status
  - `created`: Timestamp when created

## Help Command

View all available commands:
```bash
python tasks.py help
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## File Structure

```
tasks1/
├── tasks.py        # Main application
├── README.md       # This file
└── tasks.json      # Created automatically (task data)
```

## Tips

1. **Use priorities wisely**: Reserve high priority for truly urgent tasks
2. **Set realistic due dates**: This helps with planning
3. **Break down large tasks**: Use subtasks for complex projects
4. **Review regularly**: Use `python tasks.py list` to stay organized
5. **Filter effectively**: Use priority and assignment filters to focus

## Notes

- Task IDs are assigned sequentially starting from 1
- Subtask numbers start at 1 and are displayed in order
- The JSON file stores all data and is human-readable
- Priorities use emoji indicators for quick visual scanning
- You can combine multiple filters when listing tasks

-
add a few commands like priorities, due dates, assignments, submodules

error: unknown command "priority" and all the new commands