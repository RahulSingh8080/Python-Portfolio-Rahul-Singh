import json 
import os 

TASKS_FILE = "tasks.json"

tasks = []

def load_taks():
    """Load taks from the JSON file if it exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE,"r") as file:
            try:
                global tasks
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

def save_tasks():
    """save tasks  to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = input("Enter the task description: ")
    task_dict = {
        "task": task,
        "completed": False
    }
    tasks.append(task_dict)
    save_tasks()
    print(f"✅ Task '{task}' added successfully!\n")

def view_tasks():
    if not tasks:
        print("🚫 No tasks available.\n")
        return
    print("\n📋 Your Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅ Completed" if task['completed'] else "❌ Not Completed"
        print(f"{idx}. {task['task']} [{status}]")
    print()

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            save_tasks()
            print(f"🎯 Task {task_num} marked as completed!\n")
        else:
            print("🚫 Invalid task number.\n")
    except ValueError:
        print("🚫 Please enter a valid number.\n")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            save_tasks()
            print(f"🗑️ Task '{deleted['task']}' deleted successfully!\n")
        else:
            print("🚫 Invalid task number.\n")
    except ValueError:
        print("🚫 Please enter a valid number.\n")

def main():
    load_taks()
    while True:
        print("=== 📝 To-Do List App ===")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete a Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        print()

        if choice == '1':
            add_task()  
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Exiting the app. Goodbye!")
            break
        else:
            print("🚫 Invalid choice. Please select from 1 to 5.\n")

if __name__ == "__main__":
    main()