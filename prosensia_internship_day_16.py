import argparse
from colorama import init, Fore
import os

init(autoreset=True)

TASK_FILE = "tasks.txt"

def add_task(task):
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
    print(Fore.GREEN + f"Task added: {task}")

def view_tasks():
    if not os.path.exists(TASK_FILE) or os.path.getsize(TASK_FILE) == 0:
        print(Fore.YELLOW + "No tasks found.")
        return
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()
    print(Fore.CYAN + "Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

def delete_task(index):
    if not os.path.exists(TASK_FILE):
        print(Fore.RED + "No tasks file found.")
        return
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()
    if index < 1 or index > len(tasks):
        print(Fore.RED + "Invalid task number.")
        return
    removed = tasks.pop(index - 1)
    with open(TASK_FILE, "w") as file:
        file.writelines(tasks)
    print(Fore.RED + f"Deleted task: {removed.strip()}")

def export_tasks():
    if not os.path.exists(TASK_FILE):
        print(Fore.YELLOW + "No tasks to export.")
        return
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()
    with open("exported_tasks.txt", "w") as file:
        file.writelines(tasks)
    print(Fore.GREEN + "Tasks exported to 'exported_tasks.txt'.")

def main():
    parser = argparse.ArgumentParser(description="📝 CLI To-Do List Manager")
    parser.add_argument('--add', type=str, help='Add a new task')
    parser.add_argument('--view', action='store_true', help='View all tasks')
    parser.add_argument('--delete', type=int, help='Delete task by its number')
    parser.add_argument('--export', action='store_true', help='Export tasks to txt')

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.view:
        view_tasks()
    elif args.delete:
        delete_task(args.delete)
    elif args.export:
        export_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
