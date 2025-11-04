import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file, or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(title, description):
    """Add a new task to the task list."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: '{title}'")


def list_tasks():
    """List all existing tasks."""
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return

    print("\n📋 Your Tasks:")
    for task in tasks:
        print(f"\n[{task['id']}] {task['title']}\n    {task['description']}")


def main():
    """Main CLI loop."""
    while True:
        print("\n--- Task Manager ---")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()