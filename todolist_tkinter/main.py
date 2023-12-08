from ToDoList import *


def main():
    todolist = load_tasks()
    while True:
        print("Menu:")
        print("1. Add a task")
        print("2. View the list of tasks")
        print("3. Mark a task as done")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task(todolist, input('Enter task you want to add!\n'))
        elif choice == '2':
            show_tasks(todolist)
        elif choice == '3':
            complete_task(todolist, int(input('Please enter index of task you want to mark as completed!?\n')))
        elif choice == '4':
            save_tasks(todolist)
            print("Exiting Todolist. Thank you for using Todolist!")
            break
        else:
            print("Invalid choice. Please choose an option from the list.")


if __name__ == "__main__":
    main()
