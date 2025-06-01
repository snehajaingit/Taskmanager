from models import Task, Project
from file_manager import save_projects, load_projects

def print_menu():
    print("\nTask Manager")
    print("1. View Projects")
    print("2. Add Project")
    print("3. Add Task to Project")
    print("4. Mark Task as Complete")
    print("5. Save and Exit")

def main():
    projects = load_projects()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project.name}")
                for j, task in enumerate(project.tasks):
                    status = "✓" if task.completed else "✗"
                    print(f"   {j + 1}. {task.title} [{status}] - Due: {task.due_date}")

        elif choice == '2':
            name = input("Enter project name: ")
            projects.append(Project(name))
            print("Project added!")

        elif choice == '3':
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project.name}")
            idx = int(input("Select project by number: ")) - 1
            title = input("Task title: ")
            desc = input("Task description: ")
            due = input("Due date (YYYY-MM-DD): ")
            task = Task(title, desc, due)
            projects[idx].add_task(task)
            print("Task added!")

        elif choice == '4':
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project.name}")
            p_idx = int(input("Select project: ")) - 1
            for j, task in enumerate(projects[p_idx].tasks):
                print(f"{j + 1}. {task.title}")
            t_idx = int(input("Select task: ")) - 1
            projects[p_idx].tasks[t_idx].mark_complete()
            print("Task marked complete!")

        elif choice == '5':
            save_projects(projects)
            print("Saved! Goodbye.")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
