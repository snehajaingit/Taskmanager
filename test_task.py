import unittest
from models import Task

class TestTask(unittest.TestCase):
    def test_mark_complete(self):
        task = Task("Test", "Test Desc", "2025-12-31")
        task.mark_complete()
        self.assertTrue(task.completed)

if __name__ == '__main__':
    unittest.main()
