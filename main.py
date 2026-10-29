
tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks yet!")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['name']} - {status}")


def add_task():
    name = input("Enter task name: ").strip()

    if name:
        tasks.append({"name": name, "done": False})
        print("Task added successfully!")
    else:
        print("Task name cannot be empty.")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n=== Student Task Manager ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
