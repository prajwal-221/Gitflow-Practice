import os

TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return [line.rstrip('\n') for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = load_tasks()
    print("📝 Welcome to the To-Do List App!")
    while True:
        print("\nOptions: [1] Add Task  [2] View Tasks  [3] Delete Task  [4] Mark as Done  [5] Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()
            tasks.append("[ ] " + task)
            save_tasks(tasks)
            print(f"✅ Task added: {task}")

        elif choice == "2":
            if not tasks:
                print("📭 No tasks yet.")
            else:
                print("🧾 Your Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        elif choice == "3":
            if not tasks:
                print("🚫 No tasks to delete.")
                continue
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                index = int(input("Enter task number to delete: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Deleted: {removed}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a number.")

        elif choice == "4":
            if not tasks:
                print("🚫 No tasks to mark.")
                continue
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                index = int(input("Enter task number to mark as done: "))
                if 1 <= index <= len(tasks):
                    if tasks[index - 1].startswith("[ ]"):
                        tasks[index - 1] = tasks[index - 1].replace("[ ]", "[x]", 1)
                        save_tasks(tasks)
                        print("✅ Task marked as done.")
                    else:
                        print("⚠️ Task is already done.")
                else:
                    print("❌ Invalid number.")
            except ValueError:
                print("❌ Please enter a number.")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
