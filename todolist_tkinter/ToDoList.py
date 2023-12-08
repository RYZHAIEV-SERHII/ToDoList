# Creating list to store a tasks
tasks = []


# example task
# new_task = {
#     'task': 'Write your task here!',
#     'completed': False
# }
# tasks.append(new_task)
# print(tasks)


def add_task(tasks: list, task: str):
    """
Function to add a task to the list of tasks.
    :param tasks: List of tasks to add new task
    :param task: Description of the task to be added
    """
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print('Task added!')


def show_tasks(tasks: list):
    """
Function to display all available tasks in the list of tasks
    :param tasks: List of tasks to display
    """
    if not tasks:
        print("Tasks list is empty!")
    else:
        print("Tasks list:")
        for i, task in enumerate(tasks):
            status = 'Completed' if task['completed'] else 'Uncompleted'
            print(f'{i}. {task['task']} - {status}')


# add_task(tasks, 'Make shopping')
# add_task(tasks, 'Write a code')
# print(tasks)
# show_tasks(tasks)


def complete_task(tasks: list, index: int):
    """
Function to mark specific task in the list of tasks as completed
    :param tasks: List of tasks
    :param index: Index of task to be marked as completed
    """
    if 0 <= index <= len(tasks):
        task = tasks[index]
        task['completed'] = True
        save_tasks(tasks)
        print(f'Task "{task['task']}" marked as completed!')
    else:
        print("Invalid index of task!\n"
              "Please select a correct index of task you want to mark as completed")


# complete_task(tasks, 1)
# print(tasks)
# show_tasks(tasks)


def save_tasks(tasks: list):
    """
Function to save a list of tasks to a json file
    :param tasks: list of tasks
    """
    import json
    with open('tasks_list.json', 'w') as f:
        json.dump(tasks, f, indent=4)
    print('Tasks saved!')


def load_tasks(saved_tasks='tasks_list.json'):
    """
Function to load a list of tasks from a json file
    :param saved_tasks: path to saved tasks
    :return: list of tasks
    """
    import json
    import os

    # Check if file with saved tasks exists
    if os.path.exists(saved_tasks):
        with open(saved_tasks, 'r') as f:
            data = json.load(f)
        print('Tasks loaded!')
        return data
    else:
        print('Tasks loaded!')
        return []

# save_tasks(tasks)
# tasks = load_tasks()
# print(tasks)
