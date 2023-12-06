tasks = []

new_task = {
    'task': 'Write your task here!',
    'completed': False
}
tasks.append(new_task)
print(tasks)


def add_task(tasks: list, task: str):
    tasks.append({"task": task, "completed": False})
    print('Task added!')


def show_task(tasks: list):
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
    task = tasks[index]
    task['completed'] = True
    print(f' Task "{task['task']}" marked as completed!')


complete_task(tasks, 1)
print(tasks)
show_task(tasks)
