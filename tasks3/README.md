# Tasks3 - Task Manager with Testing

A Python task management application built with pytest testing framework.

## Setup Instructions

### 1. Install uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Project Structure

This project was created with:
```bash
cd csc299-project
uv init tasks3 --vcs none --package tasks3
cd tasks3
uv add --dev pytest
```

The structure is:
```
tasks3/
├── src/
│   └── tasks3/
│       └── __init__.py       # Main application code
├── tests/
│   ├── test_inc.py           # Basic test example
│   └── test_tasks.py         # Task manager tests
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

## Running Tests

Run all tests:
```bash
uv run pytest
```

Run tests with verbose output:
```bash
uv run pytest -v
```

Run specific test file:
```bash
uv run pytest tests/test_tasks.py
```

Run specific test:
```bash
uv run pytest tests/test_tasks.py::TestTask::test_task_creation
```

Show test coverage:
```bash
uv run pytest --cov=tasks3
```

## Using the Application

### Basic Commands

Add a task:
```bash
uv run tasks3 add "Buy groceries"
```

List tasks:
```bash
uv run tasks3 list
```

Complete a task:
```bash
uv run tasks3 complete 1
```

Delete a task:
```bash
uv run tasks3 delete 1
```

Search tasks:
```bash
uv run tasks3 search "groceries"
```

### Advanced Commands

Set priority:
```bash
uv run tasks3 priority 1 high
```

Set due date:
```bash
uv run tasks3 due 1 2025-12-31
```

Assign task:
```bash
uv run tasks3 assign 1 "Alice"
```

## Test Coverage

The test suite includes **25+ tests** covering:

### 1. Basic Functionality Tests
- `test_inc()` - Increment function
- `test_inc_negative()` - Negative numbers
- `test_inc_zero()` - Zero handling

### 2. Task Class Tests
- `test_task_creation()` - Basic task creation
- `test_task_with_priority()` - Priority setting
- `test_task_with_due_date()` - Due date setting
- `test_task_with_assignment()` - Task assignment
- `test_add_subtask()` - Adding subtasks
- `test_complete_subtask()` - Completing subtasks
- `test_task_to_dict()` - Serialization
- `test_task_from_dict()` - Deserialization

### 3. TaskManager Class Tests
- `test_add_task()` - Adding tasks
- `test_add_multiple_tasks()` - Multiple task handling
- `test_get_task()` - Task retrieval
- `test_delete_task()` - Task deletion
- `test_complete_task()` - Task completion
- `test_list_tasks_incomplete_only()` - Filtering incomplete
- `test_list_tasks_all()` - Listing all tasks
- `test_list_tasks_by_priority()` - Priority filtering
- `test_list_tasks_by_assignment()` - Assignment filtering
- `test_search_tasks()` - Keyword search
- `test_search_tasks_case_insensitive()` - Case-insensitive search
- `test_set_priority()` - Priority updates
- `test_set_due_date()` - Due date updates
- `test_assign_task()` - Task assignment
- `test_persistence()` - Data persistence across sessions
- `test_empty_task_list()` - Empty state handling

## Key Features Tested

✅ **Task CRUD Operations** - Create, Read, Update, Delete
✅ **Priority Management** - Low, medium, high priorities
✅ **Due Date Tracking** - Set and display due dates
✅ **Task Assignment** - Assign tasks to people
✅ **Subtask Support** - Break down complex tasks
✅ **Search & Filter** - Find tasks by keyword or criteria
✅ **Data Persistence** - Tasks saved to JSON file
✅ **Error Handling** - Invalid inputs and edge cases

## Example Test Session

```bash
$ uv run pytest -v

tests/test_inc.py::TestIncFunction::test_inc PASSED
tests/test_inc.py::TestIncFunction::test_inc_negative PASSED
tests/test_inc.py::TestIncFunction::test_inc_zero PASSED
tests/test_tasks.py::TestTask::test_task_creation PASSED
tests/test_tasks.py::TestTask::test_add_subtask PASSED
tests/test_tasks.py::TestTaskManager::test_add_task PASSED
tests/test_tasks.py::TestTaskManager::test_search_tasks PASSED
tests/test_tasks.py::TestTaskManager::test_persistence PASSED
...

======================== 25 passed in 0.15s ========================
```

## Development Workflow

1. **Make changes** to `src/tasks3/__init__.py`
2. **Write tests** in `tests/test_tasks.py`
3. **Run tests** with `uv run pytest`
4. **Fix issues** until all tests pass
5. **Commit changes** to git

## Testing Best Practices Used

- ✅ Use `pytest.fixture` for test setup/teardown
- ✅ Temporary files for isolated testing
- ✅ Descriptive test names
- ✅ Test both success and failure cases
- ✅ Test edge cases (empty lists, invalid inputs)
- ✅ Test data persistence
- ✅ Group related tests in classes

## Resources

- [Python Testing with pytest, 2nd Edition](https://www.oreilly.com/library/view/python-testing-with/9781680509427/) - Available via DePaul Library
- [pytest documentation](https://docs.pytest.org/)
- Example repositories:
  - https://github.com/bcdroid/demo-pytest
  - https://github.com/bcdroid/demo-typer-pytest

## Requirements

- Python 3.8+
- uv package manager
- pytest (automatically installed with `uv add --dev pytest`)

## Data Storage

Tasks are stored in `tasks.json` in the working directory. The file is created automatically when you add your first task.

**Note:** Add `tasks.json` to `.gitignore` to avoid committing personal task data.

-
install uv
from your csc299-project directory, run uv init tasks3 --vcs none --package tasks3 to create a new tasks3 directory and initialize it is a Python package
add pytest by running uv add --dev pytest inside the tasks3 directory
add this Python code to the top of tasks3/src/__init__.py
def inc(n: int) -> int:
    return n + 1
create a file tests/test_inc.py with this Python code:
from tasks3 import inc

def test_inc():
    assert inc(5) == 6
run uv run pytest to verify that your test setup is working correctly (it should say "1 passed")
now incorporate some (at least 2) tests (using the pytest framework) into your PKMS/task software
call your code from the main method in tasks3/src/__init__.py
then your code can be started using uv run tasks3, which calls the main method in tasks3/src/__init__.py
you can copy your existing tasks2 code into tasks3 and then add tests, or you can start with new code for tasks3, whichever you prefer
precisely what you test is up to you, and depends upon what you have implemented so far
remember that you can access the book Python Testing with pytest, 2nd Edition for free via the DePaul library E-book collections and O'Reilly for Higher Education
here are some example repositories to help you get something working (the README.md in each one documents how the repository was created):
https://github.com/bcdroid/demo-pytest
https://github.com/bcdroid/demo-stdin-stdout-pytest
https://github.com/bcdroid/demo-typer
https://github.com/bcdroid/demo-typer-pytest
https://github.com/bcdroid/demo-chat
https://github.com/bcdroid/demo-chat-completions

uv : The term 'uv' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ uv init tasks3 --vcs none --package tasks3
+ ~~
    + CategoryInfo          : ObjectNotFound: (uv:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

error: unexpected argument 'tasks3' found
Usage: uv.exe init [OPTIONS] [PATH]
For more information, try '--help'.

Built tasks3 @ file:///C:/commandline/tasks3
Installed 1 package in 52ms
error: Failed to spawn: pytest
  Caused by: program not found