import os
import json

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Show the main menu
def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. Delete task")
    print("3. List tasks")
    print("4. Mark task as done/undone")
    print("5. Edit task")
    print("6. Search tasks")
    print("7. Clear all tasks")
    print("8. Exit")

# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. {task['text']} [{status}]")

# Add a new task
def add_task(tasks):
    text = input("Enter task: ").strip()
    if text:
        tasks.append({"text": text, "done": False})
        print("✅ Task added.")
    else:
        print("❌ Task cannot be empty.")

# Delete a task
def delete_task(tasks):
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Deleted: {removed['text']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Mark a task as done/undone
def mark_task(tasks):
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to toggle done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = not tasks[num - 1]["done"]
            state = "done" if tasks[num - 1]["done"] else "not done"
            print(f"🔄 Task marked as {state}.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Edit a task's text
def edit_task(tasks):
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            new_text = input("Enter new task text: ").strip()
            if new_text:
                tasks[num - 1]["text"] = new_text
                print("✏️ Task updated.")
            else:
                print("❌ Task cannot be empty.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Search for tasks by keyword
def search_tasks(tasks):
    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
        print("❌ Keyword cannot be empty.")
        return
    found = [ (i, t) for i, t in enumerate(tasks, 1) if keyword in t["text"].lower() ]
    if not found:
        print("🔍 No tasks found with that keyword.")
    else:
        print("\nSearch results:")
        for idx, task in found:
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. {task['text']} [{status}]")

# Clear all tasks
def clear_tasks(tasks):
    confirm = input("Are you sure you want to delete all tasks? (y/n): ").strip().lower()
    if confirm == "y":
        tasks.clear()
        print("🗑️ All tasks deleted.")
    else:
        print("Cancelled.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            mark_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            clear_tasks(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print("👋 Goodbye! Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        save_tasks(tasks)

if __name__ == "__main__":
    main()