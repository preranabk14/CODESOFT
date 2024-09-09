# To-Do List Application by PRERANA B K
def display_todo_list(todo_list):
    if not todo_list:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def delete_task(todo_list):
    display_todo_list(todo_list)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    todo_list = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            delete_task(todo_list)
        elif choice == '4':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
