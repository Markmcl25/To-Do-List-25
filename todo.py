import json

# Load tasks from a file (or use an empty list if the file doesn't exist)
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

# View all tasks
def view_tasks(tasks):
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{idx}. {task['task']} - {status}")

# Mark a task as done
def mark_done(tasks, task_id):
    tasks[task_id - 1]["done"] = True
    save_tasks(tasks)

# Remove a task
def remove_task(tasks, task_id):
    tasks.pop(task_id - 1)
    save_tasks(tasks)

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "3":
            task_id = int(input("Enter task number to mark as done: "))
            mark_done(tasks, task_id)
        elif choice == "4":
            task_id = int(input("Enter task number to remove: "))
            remove_task(tasks, task_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
