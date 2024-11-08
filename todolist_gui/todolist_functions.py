import json
import os
import tkinter as tk
from tkinter import messagebox


def load_tasks(saved_tasks="tasks_list.json"):
    """
    Function to load a list of tasks from a json file
        :param saved_tasks: path to saved tasks
        :return: list of tasks or empty list if tasks wasn't saved previously
    """
    # Check if file with saved tasks exists
    if os.path.exists(saved_tasks):
        with open(saved_tasks, "r") as f:
            tasks = json.load(f)
        return tasks
    else:
        return []


def save_tasks(tasks: list):
    """
    Function to save a list of tasks to a json file
        :param tasks: list of tasks
    """
    with open("tasks_list.json", "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(entry, listbox, tasks):
    """
    Adds a new task to the task list if the entry is not empty.

    Parameters:
    entry (tk.Entry): The entry widget to get the task from.
    listbox (tk.Listbox): The listbox widget to display tasks.
    tasks (list): The list of task dictionaries.
    """
    task = entry.get().strip()
    if not task:
        messagebox.showwarning("Attention!", "Please enter a task.")
        return

    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    messagebox.showinfo("Success!", "Task added successfully!")
    entry.delete(0, tk.END)
    show_tasks(listbox, tasks)


def delete_task(listbox, tasks):
    """
    Deletes a task from the task list if a task is selected.

    Parameters:
    listbox (tk.Listbox): The listbox widget to display tasks.
    tasks (list): The list of task dictionaries.
    """

    selected_index = listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        if 0 <= index <= len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            messagebox.showinfo("Success!", "Task deleted!")
            show_tasks(listbox, tasks)
        else:
            messagebox.showwarning("Warning!", "Invalid index of task!")
    else:
        messagebox.showwarning("Warning!", "Please select a task you want to delete.")


def complete_task(listbox, tasks: list):
    """
    Marks a task as completed from the task list if a task is selected.

    Parameters:
    listbox (tk.Listbox): The listbox widget to display tasks.
    tasks (list): The list of task dictionaries.
    """
    selected_index = listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        if 0 <= index <= len(tasks):
            task = tasks[index]
            task["completed"] = True
            save_tasks(tasks)
            messagebox.showinfo("Success!", "Task marked as completed!")
            show_tasks(listbox, tasks)
        else:
            messagebox.showwarning("Warning!", "Invalid index of task!")
    else:
        messagebox.showwarning(
            "Warning!", "Please select a task you want to mark as completed."
        )


def incomplete_task(listbox, tasks: list):
    """
    Marks a task as uncompleted from the task list if a task is selected.

    Parameters:
    listbox (tk.Listbox): The listbox widget to display tasks.
    tasks (list): The list of task dictionaries.
    """
    selected_index = listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        if 0 <= index <= len(tasks):
            task = tasks[index]
            task["completed"] = False
            save_tasks(tasks)
            messagebox.showinfo("Success!", "Task marked as uncompleted!")
            show_tasks(listbox, tasks)
        else:
            messagebox.showwarning("Warning!", "Invalid index of task!")
    else:
        messagebox.showwarning(
            "Warning!", "Please select a task you want to mark as uncompleted."
        )


def show_tasks(listbox, tasks: list):
    """
    Displays the tasks in a listbox widget.

    Parameters:
    listbox (tk.Listbox): The listbox widget to display tasks.
    tasks (list): The list of task dictionaries.
    """
    listbox.delete(0, tk.END)
    if not tasks:
        listbox.insert(tk.END, "Tasks list is empty!")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "In progress"
            listbox.insert(tk.END, f"{i}. {task['task']} - {status}")
