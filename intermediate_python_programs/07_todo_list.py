
import json
from pathlib import Path


FILE_PATH = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not FILE_PATH.exists():
        return []

    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            print("Invalid task file format. Starting with an empty list.")
            return []

        return tasks

    except (json.JSONDecodeError, OSError):
        print("Could not read saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    print("\n" + "=" * 40)
    print("               YOUR TASKS")
    print("=" * 40)

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. [{status}] {task['title']}")


def add_task(tasks):
    title = input("Enter task description: ").strip()

    if not title:
        print("Task description cannot be empty.")
        return

    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")


def complete_task(tasks):
    display_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if not 1 <= number <= len(tasks):
            print("Invalid task number.")
            return

        if tasks[number - 1]["completed"]:
            print("This task is already completed.")
            return

        tasks[number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid whole number.")


def delete_task(tasks):
    display_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if not 1 <= number <= len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['title']}")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 40)
        print("             TO-DO LIST")
        print("=" * 40)
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        try:
            if choice == "1":
                display_tasks(tasks)
            elif choice == "2":
                add_task(tasks)
            elif choice == "3":
                complete_task(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-5.")

        except OSError as error:
            print(f"Could not save changes: {error}")
            tasks = load_tasks()


if __name__ == "__main__":
    main()
