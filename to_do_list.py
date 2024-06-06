import os
import json
from datetime import datetime

# File to store tasks
TASK_FILE = 'tasks.json'

# Load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks, description, priority, due_date):
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{description}" added.')

# Remove a task
def remove_task(tasks, task_id):
    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f'Task "{task["description"]}" removed.')
    else:
        print('Invalid task ID.')

# Mark a task as completed
def complete_task(tasks, task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_id]["description"]}" marked as completed.')
    else:
        print('Invalid task ID.')

# Display the list of tasks
def list_tasks(tasks):
    if not tasks:
        print('No tasks available.')
        return

    for i, task in enumerate(tasks):
        status = 'Completed' if task['completed'] else 'Pending'
        print(f'{i}. {task["description"]} | Priority: {task["priority"]} | Due Date: {task["due_date"]} | Status: {status}')

def main():
    tasks = load_tasks()
    while True:
        print('\nTo-Do List Application')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. Mark Task as Completed')
        print('4. List Tasks')
        print('5. Exit')

        choice = input('Choose an option: ')
        if choice == '1':
            description = input('Task Description: ')
            priority = input('Priority (high, medium, low): ')
            due_date = input('Due Date (YYYY-MM-DD): ')
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
                add_task(tasks, description, priority, due_date)
            except ValueError:
                print('Invalid date format. Please use YYYY-MM-DD.')
        elif choice == '2':
            task_id = int(input('Task ID to remove: '))
            remove_task(tasks, task_id)
        elif choice == '3':
            task_id = int(input('Task ID to mark as completed: '))
            complete_task(tasks, task_id)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
