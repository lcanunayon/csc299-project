# Task Manager CLI

A simple command-line task management application that stores tasks in a JSON file.

## Features

- ✅ Add new tasks
- 📝 List all tasks (or only incomplete ones)
- 🔍 Search tasks by keyword
- ✓ Mark tasks as completed
- 🗑️ Delete tasks
- 💾 Persistent storage using JSON

## Installation

No installation required! Just Python 3.6+ is needed.

## Usage

### Add a Task

```bash
python tasks.py add "Task description"
```

Example:
```bash
python tasks.py add "Buy groceries"
python tasks.py add "Finish homework"
python tasks.py add "Call dentist"
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

Search for tasks containing a keyword:
```bash
python tasks.py search "keyword"
```

Example:
```bash
python tasks.py search "homework"
```

### Mark Task as Completed

```bash
python tasks.py complete <task_id>
```

Example:
```bash
python tasks.py complete 1
```

### Delete a Task

```bash
python tasks.py delete <task_id>
```

Example:
```bash
python tasks.py delete 2
```

### Help

Display help information:
```bash
python tasks.py help
```

## Data Storage

Tasks are stored in `tasks.json` in the same directory as the script. This file is created automatically when you add your first task.

### Task Structure

Each task contains:
- `id`: Unique identifier
- `description`: Task description
- `created`: Timestamp when task was created
- `completed`: Boolean indicating completion status

## Example Workflow

```bash
# Add some tasks
python tasks.py add "Read chapter 5"
python tasks.py add "Write essay"
python tasks.py add "Study for exam"

# List tasks
python tasks.py list

# Complete a task
python tasks.py complete 1

# Search for tasks
python tasks.py search "essay"

# Delete a task
python tasks.py delete 2

# List all tasks including completed ones
python tasks.py list --all
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## File Structure

```
tasks1/
├── tasks.py        # Main application
├── README.md       # This file
└── tasks.json      # Created automatically (task data storage)
```

## Notes

- Task IDs are assigned sequentially starting from 1
- The `tasks.json` file will be created in the same directory as `tasks.py`
- If the JSON file becomes corrupted, the application will start with an empty task list