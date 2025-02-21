#To_do_List
def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                description, due_date, completed = line.strip().split("|")
                tasks.append({
                    "description": description,
                    "due_date": due_date,
                    "completed": completed == "True"
                })
    except FileNotFoundError:
        pass
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['description']}|{task['due_date']}|{task['completed']}\n")

# Add a task
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    task = {"description": description, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i+1}. {task['description']} (Due: {task['due_date']}) - {status}")

# Mark a task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()