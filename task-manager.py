# My Simple Task Manager App

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu
def display_menu():
    print("\nTask Manager Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task():
    task = input("\nEnter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

# Function to update an existing task
def update_task():
    if not tasks:
        print("\nNo tasks available to update.")
        return
    view_tasks()
    task_num = int(input("\nEnter the task number to update: "))
    if 0 < task_num <= len(tasks):
        new_task = input("Enter the new task description: ")
        tasks[task_num - 1] = new_task
        print(f"Task {task_num} has been updated to '{new_task}'.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    if not tasks:
        print("\nNo tasks available to delete.")
        return
    view_tasks()
    task_num = int(input("\nEnter the task number to delete: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' has been deleted.")
    else:
        print("Invalid task number.")

# Main function to run the task manager
def run_task_manager():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the task manager
if __name__ == "__main__":
    run_task_manager()
