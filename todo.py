import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = load_tasks()
    print("📝 Welcome to the To-Do List App!")
    while True:
        print("\nOptions: [1] Add Task  [2] View Tasks  [3] Delete Task  [4] Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()
            tasks.append(task)
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
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
