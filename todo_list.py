def add_task(task_list):
    """Prompts user for a task description and adds it to the list."""
    task = input("Enter task: ")
    task_list.append(task)
    print(f'Task added: "{task}"')

def view_tasks(task_list):
    """Displays all tasks currently in the list numbered from 1."""
    if not task_list:
        print("Your to-do list is currently empty.")
        return
        
    print("Your Tasks:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

def delete_task(task_list):
    """Displays tasks, asks for a target number, and removes it safely if valid."""
    if not task_list:
        print("There are no tasks to delete.")
        return
        
    view_tasks(task_list)
    try:
        task_num = int(input("Enter task number to delete: "))
        target_idx = task_num - 1
        
        if 0 <= target_idx < len(task_list):
            removed_task = task_list.pop(target_idx)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid numerical choice.")

def display_menu():
    """Prints the structured selection menu layout."""
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


if _name_ == "_main_":
    todo_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            delete_task(todo_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid selection. Please choose a value from 1 to 4.")
