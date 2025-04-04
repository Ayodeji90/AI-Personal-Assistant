import argparse
from task_manager import TaskManager

manager = TaskManager()

parser = argparse.ArgumentParser(description="Task Manager CLI")

parser.add_argument('--add', type=str, help='Task title')
parser.add_argument('--category', type=str, help='Task category')
parser.add_argument('--priority', type=str, help='Urgent, High, Medium, Low')
parser.add_argument('--due', type=str, help='Due date in YYYY-MM-DD')

parser.add_argument('--view', type=str, help='View all or by status (all, pending, completed)')
parser.add_argument('--complete', type=int, help='Mark task as completed')
parser.add_argument('--delete', type=int, help='Delete a task by ID')
parser.add_argument('--sort', type=str, help='Sort by priority or due_date')

args = parser.parse_args()

if args.add:
    manager.add_task(args.add, args.category, args.priority, args.due)
    print("Task added.")

if args.view:
    status = None if args.view == 'all' else args.view.capitalize()
    tasks = manager.get_tasks(status)
    for task in tasks:
        print(task)

if args.complete:
    manager.complete_task(args.complete)
    print(f"Task {args.complete} marked as complete.")

if args.delete:
    manager.delete_task(args.delete)
    print(f"Task {args.delete} deleted.")

if args.sort:
    tasks = manager.get_sorted_tasks(by=args.sort)
    for task in tasks:
        print(task)
