from db import TaskDatabase
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.db = TaskDatabase()

    def add_task(self, title, category, priority, due_date):
        """Validate and add a new task."""
        try:
            datetime.strptime(due_date, "%Y-%m-%d")  # Validate date format
        except ValueError:
            return "Invalid date format. Use YYYY-MM-DD."
        
        if priority not in ["Urgent", "High", "Medium", "Low"]:
            return "Invalid priority. Choose from: Urgent, High, Medium, Low."
        
        self.db.add_task(title, category, priority, due_date)
        return "Task added successfully."

    def get_tasks(self, status=None):
        """Retrieve tasks, optionally filtered by status, sorted by priority & due date."""
        priority_order = {"Urgent": 1, "High": 2, "Medium": 3, "Low": 4}
        tasks = self.db.get_tasks(status)
        sorted_tasks = sorted(tasks, key=lambda x: (priority_order[x[3]], x[4]))
        return sorted_tasks

    def update_task(self, task_id, title=None, category=None, priority=None, due_date=None):
        """Update an existing task."""
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                return "Invalid date format."

        self.db.update_task(task_id, title, category, priority, due_date)
        return "Task updated successfully."

    def mark_completed(self, task_id):
        """Mark a task as completed."""
        self.db.mark_completed(task_id)
        return "Task marked as completed."

    def delete_task(self, task_id):
        """Delete a task."""
        self.db.delete_task(task_id)
        return "Task deleted successfully."



# Ensure the module can be imported correctly
if __name__ == "__main__":
    tm = TaskManager()
    print("TaskManager initialized successfully.")