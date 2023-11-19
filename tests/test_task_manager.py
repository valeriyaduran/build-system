import unittest

from src.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.extracted_data = {
            "builds":
                [
                    {
                        "name": "build1",
                        "tasks": ["task1", "task2", "task3", "task4"]
                    },
                    {
                        "name": "build2",
                        "tasks": []
                    },
                ],
            "tasks": [
                {"name": "task1", "dependencies": ""},
                {"name": "task2", "dependencies": ""},
                {"name": "task3", "dependencies": ""},
                {"name": "task4", "dependencies": ""}
            ]
        }

    def test_get_tasks_by_build_name_success(self):
        task_manager = TaskManager(build_name="build1", extracted_data=self.extracted_data)
        self.assertEqual(task_manager.get_tasks_by_build_name(), ["task1", "task2", "task3", "task4"])

    def test_get_tasks_by_build_name_build_not_found(self):
        task_manager = TaskManager(build_name="buildnotfound", extracted_data=self.extracted_data)
        with self.assertRaises(IndexError):
            task_manager.get_tasks_by_build_name()

    def test_get_tasks_by_build_name_empty_build(self):
        task_manager = TaskManager(build_name="", extracted_data=self.extracted_data)
        with self.assertRaises(IndexError):
            task_manager.get_tasks_by_build_name()

    def test_create_graph_for_sorting_success(self):
        task_manager = TaskManager(build_name="build1", extracted_data=self.extracted_data)
        task_manager.create_graph_for_sorting(tasks=["task1", "task2", "task3", "task4"])
        self.assertIsInstance(task_manager.graph, dict)
        self.assertEqual(all([isinstance(key, str) for key in task_manager.graph.keys()]), True)
        self.assertEqual(all([isinstance(value, set) for value in task_manager.graph.values()]), True)


if __name__ == '__main__':
    unittest.main()
