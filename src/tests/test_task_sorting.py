from unittest import TestCase, main
from unittest.mock import Mock

from src.task_manager import TaskManager, TopologicalSorting


class TestTaskManager(TestCase):
    def setUp(self) -> None:
        self.extracted_data = {
            "builds":
                [
                    {
                        "name": "build1",
                        "tasks": ["task1", "task2", "task3"]
                    },
                    {
                        "name": "build2",
                        "tasks": ["task4", "task5"]
                    },
                    {
                        "name": "build3",
                        "tasks": []
                    },
                    {
                        "name": "build4",
                        "tasks": ["task6", "task7", "task9", "task10"]
                    },
                ],
            "tasks": [
                {"name": "task1", "dependencies": ["task2"]},
                {"name": "task2", "dependencies": ["task3"]},
                {"name": "task3", "dependencies": []},
                {"name": "task4", "dependencies": []},
                {"name": "task5", "dependencies": []},
                {"name": "task6", "dependencies": ["task5", "task7"]},
                {"name": "task7", "dependencies": ["task9"]},
                {"name": "task9", "dependencies": []},
                {"name": "task10", "dependencies": ["task9"]}, ]
        }

    def test_get_tasks_by_build_name_success(self):
        task_manager = TaskManager(build_name="build1", extracted_data=self.extracted_data)
        self.assertEqual(task_manager.get_tasks_by_build_name(), ["task1", "task2", "task3"])

    def test_get_tasks_by_build_name_build_not_found(self):
        task_manager = TaskManager(build_name="not_existing_build_name", extracted_data=self.extracted_data)
        with self.assertRaises(IndexError):
            task_manager.get_tasks_by_build_name()

    def test_get_tasks_by_build_name_empty_build(self):
        task_manager = TaskManager(build_name="", extracted_data=self.extracted_data)
        with self.assertRaises(IndexError):
            task_manager.get_tasks_by_build_name()

    def test_create_graph_for_sorting_check_types(self):
        task_manager = TaskManager(build_name="build1", extracted_data=self.extracted_data)
        task_manager.create_graph_for_sorting(tasks=["task1", "task2", "task3"])
        self.assertIsInstance(task_manager.graph, dict)
        self.assertEqual(all([isinstance(key, str) for key in task_manager.graph.keys()]), True)
        self.assertEqual(all([isinstance(value, set) for value in task_manager.graph.values()]), True)

    def test_create_graph_for_sorting_filled_graph(self):
        task_manager = TaskManager(build_name="build1", extracted_data=self.extracted_data)
        task_manager.create_graph_for_sorting(tasks=["task1", "task2", "task3"])
        self.assertEqual(task_manager.graph, {"task1": {"task2"}, "task2": {"task3"}, "task3": set()})

    def test_create_graph_for_sorting_empty_graph(self):
        task_manager = TaskManager(build_name="build3", extracted_data=self.extracted_data)
        task_manager.create_graph_for_sorting(tasks=[])
        self.assertEqual(task_manager.graph, {})

    def test_sort_tasks_by_dependencies_no_tasks(self):
        task_manager = TaskManager(build_name="build3", extracted_data=self.extracted_data)
        task_manager.create_graph_for_sorting(tasks=[])
        self.assertEqual(task_manager.sort_tasks_by_dependencies(), [])

    def test_sort_tasks_by_dependencies_no_dependencies(self):
        task_manager = TaskManager(build_name="build2", extracted_data=self.extracted_data)
        task_manager.create_graph_for_sorting(tasks=["task4", "task5"])
        self.assertEqual(task_manager.sort_tasks_by_dependencies(), ["task4", "task5"])

    def test_sort_tasks_by_dependencies_line_dependencies(self):
        task_manager = TaskManager(build_name="build1", extracted_data=self.extracted_data)
        task_manager.create_graph_for_sorting(tasks=["task1", "task2", "task3"])
        self.assertEqual(task_manager.sort_tasks_by_dependencies(), ["task3", "task2", "task1"])

    def test_sort_tasks_by_dependencies_diamond_dependencies(self):
        task_manager = TaskManager(build_name="build4", extracted_data=self.extracted_data)
        task_manager.create_graph_for_sorting(tasks=["task6", "task7", "task9", "task10"])
        self.assertEqual(task_manager.sort_tasks_by_dependencies(),
                         ['task5', 'task9', 'task7', 'task6', 'task10'])

    def test_get_sorted_tasks_called_all_inside_methods(self):
        task_manager = TaskManager(build_name="build1", extracted_data=self.extracted_data)
        task_manager.get_tasks_by_build_name = Mock()
        task_manager.create_graph_for_sorting = Mock()
        task_manager.sort_tasks_by_dependencies = Mock()
        task_manager.get_sorted_tasks()
        task_manager.get_tasks_by_build_name.assert_called_once()
        task_manager.create_graph_for_sorting.assert_called_once()
        task_manager.sort_tasks_by_dependencies.assert_called_once()


class TestTopologicalSorting(TestCase):
    def setUp(self) -> None:
        self.graph = {'task1': [],
                      'task2': ['task3', 'task1'],
                      'task4': ['task3'],
                      'task5': ['task4']}

    def test_add_node_to_stack_tasks_not_in_graph_keys(self):
        topological_sorting = TopologicalSorting(self.graph)
        topological_sorting.add_node_to_stack(task="task3")
        self.assertEqual(topological_sorting.stack_tasks_not_in_graph_keys, ["task3"])

    def test_add_node_to_stack_tasks_in_graph_keys(self):
        topological_sorting = TopologicalSorting(self.graph)
        topological_sorting.add_node_to_stack(task="task4")
        self.assertEqual(topological_sorting.stack_tasks_in_graph_keys, ["task4"])

    def test_add_node_to_stack_called(self):
        topological_sorting = TopologicalSorting(self.graph)
        topological_sorting.add_node_to_stack = Mock()
        topological_sorting.run_topological_sorting()
        topological_sorting.add_node_to_stack.assert_called()


if __name__ == "__main__":
    main()
