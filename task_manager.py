
"""
SWYNEX Internship - Task 1
Python CLI Task Manager
"""

import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    """Load saved tasks from the JSON file."""
    try:
        if DATA_FILE.exists():
            with DATA_FILE.open("r", encoding="utf-8") as file:
                tasks = json.load(file)
                if isinstance(tasks, list):
                    return tasks
                print("Warning: Invalid task data. Starting empty.")
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not load tasks: {error}")
    return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Could not save tasks: {error}")
        return False


def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "completed": False})

    if save_tasks(tasks):
        print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")


def get_task_number(tasks, prompt):
    if not tasks:
        print("No tasks available.")
        return None

    try:
        number = int(input(prompt))
        if 1 <= number <= len(tasks):
            return number - 1
        print(f"Enter a number from 1 to {len(tasks)}.")
    except ValueError:
        print("Please enter a valid whole number.")

    return None


def complete_task(tasks):
    view_tasks(tasks)
    index = get_task_number(tasks, "Task number to complete: ")

    if index is not None:
        tasks[index]["completed"] = True
        if save_tasks(tasks):
            print("Task marked as completed!")


def delete_task(tasks):
    view_tasks(tasks)
    index = get_task_number(tasks, "Task number to delete: ")

    if index is not None:
        removed = tasks.pop(index)
        if save_tasks(tasks):
            print(f"Deleted task: {removed['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== PYTHON TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using Task Manager!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
