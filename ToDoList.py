
# Creating list to store a tasks
tasks = []

# example task
new_task = {
    'task': 'Write your task here!',
    'completed': False
}
tasks.append(new_task)
print(tasks)


def add_task(tasks: list, task: str):
    """
Function to add a task to the list of tasks.
    :param tasks: List of tasks to add new task
    :param task: Description of the task to be added
    """
    tasks.append({"task": task, "completed": False})
    print('Task added!')


def show_task(tasks: list):
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


add_task(tasks, 'Make shopping')
add_task(tasks, 'Write a code')
print(tasks)
show_task(tasks)


def complete_task(tasks: list, index: int):
    """
Function to mark specific task in the list of tasks as completed
    :param tasks: List of tasks
    :param index: Index of task to be marked as completed
    """
    task = tasks[index]
    task['completed'] = True
    print(f' Task "{task['task']}" marked as completed!')


complete_task(tasks, 1)
print(tasks)
show_task(tasks)
