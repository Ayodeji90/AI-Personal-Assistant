import unittest
from task_manager import TaskManager

#from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()
        self.tm.db.conn.execute("DELETE FROM tasks")  # Clear database before each test

    def test_add_task(self):
        response = self.tm.add_task("Test Task", "Work", "High", "2025-04-10")
        self.assertEqual(response, "Task added successfully.")

    def test_get_tasks(self):
        self.tm.add_task("Task 1", "Work", "Urgent", "2025-04-10")
        self.tm.add_task("Task 2", "Personal", "Low", "2025-04-12")
        tasks = self.tm.get_tasks()
        self.assertEqual(len(tasks), 2)

    def test_update_task(self):
        self.tm.add_task("Old Task", "Work", "Medium", "2025-04-10")
        task_id = self.tm.get_tasks()[0][0]
        response = self.tm.update_task(task_id, priority="High")
        self.assertEqual(response, "Task updated successfully.")

    def test_mark_completed(self):
        self.tm.add_task("Task to Complete", "Work", "High", "2025-04-10")
        task_id = self.tm.get_tasks()[0][0]
        response = self.tm.mark_completed(task_id)
        self.assertEqual(response, "Task marked as completed.")

    def test_delete_task(self):
        self.tm.add_task("Task to Delete", "Work", "Low", "2025-04-10")
        task_id = self.tm.get_tasks()[0][0]
        response = self.tm.delete_task(task_id)
        self.assertEqual(response, "Task deleted successfully.")

if __name__ == "__main__":
    unittest.main()
