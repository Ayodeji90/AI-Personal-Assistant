import unittest
from src.agents.task_manager.task_manager import TaskManager  # ✅ Use full path
#from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Test task", "Work", "High", "2025-04-10")
        tasks = self.manager.get_tasks()
        self.assertTrue(any(task[1] == "Test task" for task in tasks))

    def mark_complete(self):
        self.manager.add_task("Temp Task", "Work", "Low", "2025-04-10")
        tasks = self.manager.get_tasks()
        task_id = tasks[-1][0]
        self.manager.complete_task(task_id)
        updated_task = [t for t in self.manager.get_tasks("Completed") if t[0] == task_id]
        self.assertTrue(len(updated_task) == 1)

    def test_delete_task(self):
        self.manager.add_task("To Delete", "Work", "Low", "2025-04-10")
        task_id = self.manager.get_tasks()[-1][0]
        self.manager.delete_task(task_id)
        task_ids = [t[0] for t in self.manager.get_tasks()]
        self.assertNotIn(task_id, task_ids)

if __name__ == "__main__":
    unittest.main()
