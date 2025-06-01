from models import Task
from file_manager import save_tasks, load_tasks

def print_menu():
    print("\n==== Task Manager ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks):
                    status = "✓" if task.completed else "✗"
                    print(f"{i}. {task.title} [{status}] - Due: {task.due_date}")

        elif choice == '2':
            title = input("Enter task title: ")
            desc = input("Enter task description: ")
            due = input("Enter due date (YYYY-MM-DD): ")
            new_task = Task(title, desc, due)
            tasks.append(new_task)
            print("Task added!")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark complete.")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i}. {task.title} [{ '✓' if task.completed else '✗' }]")
                idx = int(input("Enter task number to mark complete: "))
                if 0 <= idx < len(tasks):
                    tasks[idx].mark_complete()
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")

        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid option! Please enter 1–4.")

if __name__ == "__main__":
    main()
