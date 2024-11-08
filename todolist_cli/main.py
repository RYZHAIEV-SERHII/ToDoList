from ToDoList import (
    show_tasks,
    add_task,
    delete_task,
    complete_task,
    incomplete_task,
    load_tasks,
    save_tasks,
)


def main():
    todolist = load_tasks()
    while True:
        print("\n")
        print("=========== Todolist ===========")
        print("Menu:")
        print("1. View the list of tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Mark a task as done")
        print("5. Mark a task as undone")
        print("0. Quit")
        print("--------------------------------")

        choice = input("Choose an option (1-5) \n" "Or enter '0' to quit: ")

        if choice == "1":
            show_tasks(todolist)
        elif choice == "2":
            add_task(todolist, input("Enter task you want to add!\n"))
        elif choice == "3":
            try:
                delete_task(
                    todolist, int(input("Enter index of task you want to delete!\n"))
                )
            except ValueError:
                print(
                    "Invalid index of task!\nPlease select a correct index of task you want to delete"
                )

        elif choice == "4":
            complete_task(
                todolist,
                int(
                    input(
                        "Please enter index of task you want to mark as completed!?\n"
                    )
                ),
            )
        elif choice == "5":
            incomplete_task(
                todolist,
                int(
                    input(
                        "Please enter index of task you want to mark as uncompleted!?\n"
                    )
                ),
            )
        elif choice == "0":
            save_tasks(todolist)
            print("Exiting Todolist. Thank you for using Todolist!")
            break
        else:
            print("Invalid choice. Please choose an option from the list.")


if __name__ == "__main__":
    main()
