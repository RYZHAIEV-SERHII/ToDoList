import tkinter as tk

from todolist_functions import (
    show_tasks,
    add_task,
    complete_task,
    incomplete_task,
    delete_task,
    load_tasks,
)


def main():
    tasks = load_tasks()

    root = tk.Tk()
    root.title("Tasks manager")

    label = tk.Label(root, text="Enter a new task:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    add_button = tk.Button(
        root,
        text="Add task",
        command=lambda: add_task(entry, listbox, tasks),
    )
    add_button.pack(pady=10)

    listbox = tk.Listbox(root, width=60, height=15)
    listbox.pack(pady=10)

    show_tasks(listbox, tasks)

    complete_button = tk.Button(
        root,
        text="Mark as complete",
        command=lambda: complete_task(listbox, tasks),
    )
    complete_button.pack(pady=10)

    incomplete_button = tk.Button(
        root,
        text="Mark as incomplete",
        command=lambda: incomplete_task(listbox, tasks),
    )
    incomplete_button.pack(pady=10)

    delete_button = tk.Button(
        root,
        text="Delete task",
        command=lambda: delete_task(listbox, tasks),
    )
    delete_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
