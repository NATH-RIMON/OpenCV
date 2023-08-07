import json
import datetime

tasks = []

def add_task():
    description = input("Enter task description: ")
    task = {"description": description, "completed": False, "priority": None, "due_date": None}
    tasks.append(task)
    print("Task added successfully!")

def complete_task():
    task_number = int(input("Enter the task number to mark as complete: "))
    if task_number > 0 and task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def view_todo_list():
    sorted_tasks = sorted(tasks, key=lambda x: (x["priority"] is None, x["priority"], x["due_date"] is None, x["due_date"]))
    print("To-Do List:")
    for i, task in enumerate(sorted_tasks, 1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['description']}")

def remove_task():
    task_number = int(input("Enter the task number to remove: "))
    if task_number > 0 and task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

def save_tasks():
    filename = input("Enter the filename to save the tasks: ")
    with open(filename, "w") as file:
        json.dump(tasks, file)
    print("Tasks saved successfully!")

def add_priority():
    task_number = int(input("Enter the task number to add priority: "))
    if task_number > 0 and task_number <= len(tasks):
        priority = int(input("Enter the priority number: "))
        tasks[task_number - 1]["priority"] = priority
        print("Priority added successfully!")
    else:
        print("Invalid task number.")

def add_due_date():
    task_number = int(input("Enter the task number to add due date: "))
    if task_number > 0 and task_number <= len(tasks):
        due_date_str = input("Enter the due date (YYYY-MM-DD): ")
        try:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            tasks[task_number - 1]["due_date"] = due_date
            print("Due date added successfully!")
        except ValueError:
            print("Invalid date format.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("------------------")
        print("1. Add a task")
        print("2. Complete a task")
        print("3. View to-do list sorted by due date")
        print("4. Remove a task")
        print("5. Save the task list to file")
        print("6. Add priority to task")
        print("7. Add due date to task")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            complete_task()
        elif choice == "3":
            view_todo_list()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            add_priority()
        elif choice == "7":
            add_due_date()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
