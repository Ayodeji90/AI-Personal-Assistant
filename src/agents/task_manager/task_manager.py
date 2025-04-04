from .db import TaskDatabase
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.db = TaskDatabase()

    def add_task(self, title, category, priority, due_date):
        if not self._validate_date(due_date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        self.db.add_task(title, category, priority, due_date)

    def get_tasks(self, status=None):
        return self.db.get_tasks(status)

    def update_task(self, task_id, **kwargs):
        self.db.update_task(task_id, **kwargs)

    def delete_task(self, task_id):
        self.db.delete_task(task_id)

    def complete_task(self, task_id):
        self.db.mark_task_completed(task_id)

    def get_sorted_tasks(self, by='priority'):
        return self.db.get_sorted_tasks(by=by)

    def _validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
