import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file or return empty list."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(title, description):
    """Add a new task."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title.strip(),
        "description": description.strip(),
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added: '{title}'")


def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return

    print("\n📋 Your Tasks:")
    for t in tasks:
        status = "✅" if t["completed"] else "🕓"
        print(f"[{t['id']}] {status} {t['title']} - {t['description']}")


def mark_task_done(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            save_tasks(tasks)
            print(f"🎯 Task #{task_id} marked as completed.")
            return
    print("❌ Task not found.")


def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    updated = [t for t in tasks if t["id"] != task_id]
    if len(updated) == len(tasks):
        print("❌ Task not found.")
    else:
        # Reassign IDs
        for i, t in enumerate(updated, start=1):
            t["id"] = i
        save_tasks(updated)
        print(f"🗑️ Deleted task #{task_id}.")


def search_tasks(keyword):
    """Search for tasks containing a keyword."""
    tasks = load_tasks()
    matches = [t for t in tasks if keyword.lower() in t["title"].lower() or keyword.lower() in t["description"].lower()]

    if not matches:
        print(f"🔍 No tasks found matching '{keyword}'.")
        return

    print(f"\n🔍 Search results for '{keyword}':")
    for t in matches:
        print(f"[{t['id']}] {t['title']} - {t['description']}")


def load_example_data():
    """Load example data if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        example_tasks = [
            {"id": 1, "title": "Finish homework", "description": "Complete math and CS assignments", "completed": False},
            {"id": 2, "title": "Read book", "description": "Read 20 pages of 'Clean Code'", "completed": False},
        ]
        save_tasks(example_tasks)
        print("📘 Example tasks created.")


def main():
    """Main command loop."""
    load_example_data()

    while True:
        print("\n--- 🧠 Task Manager ---")
        print("Commands:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Search tasks")
        print("6. Exit")

        choice = input("\nEnter choice (1–6): ").strip()

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            add_task(title, desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                tid = int(input("Enter task ID: "))
                mark_task_done(tid)
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
        elif choice == "4":
            try:
                tid = int(input("Enter task ID to delete: "))
                delete_task(tid)
            except ValueError:
                print("❌ Invalid input.")
        elif choice == "5":
            keyword = input("Enter search keyword: ")
            search_tasks(keyword)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
