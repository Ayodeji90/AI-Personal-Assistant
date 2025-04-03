import argparse
from task_manager import TaskManager

tm = TaskManager()

parser = argparse.ArgumentParser(description="Task Manager CLI")

parser.add_argument("--add", nargs=3, metavar=("TITLE", "CATEGORY", "PRIORITY"), help="Add a new task")
parser.add_argument("--due", type=str, help="Due date (YYYY-MM-DD)")
parser.add_argument("--view", choices=["all", "pending", "completed"], help="View tasks")
parser.add_argument("--update", type=int, help="Update task ID")
parser.add_argument("--priority", type=str, help="New priority")
parser.add_argument("--complete", type=int, help="Mark task as completed")
parser.add_argument("--delete", type=int, help="Delete task ID")

args = parser.parse_args()

if args.add:
    title, category, priority = args.add
    print(tm.add_task(title, category, priority, args.due))
elif args.view:
    status = None if args.view == "all" else args.view.capitalize()
    for task in tm.get_tasks(status):
        print(task)
elif args.update:
    print(tm.update_task(args.update, priority=args.priority, due_date=args.due))
elif args.complete:
    print(tm.mark_completed(args.complete))
elif args.delete:
    print(tm.delete_task(args.delete))
