from unittest.mock import Mock

import pytest

from src.handlers.exception_handler import BuildNotFoundException, EmptyBuildNameException
from src.task_manager import TaskManager, TaskSorting


class TestTaskManager:
    @pytest.mark.parametrize("build_name, expected_result",
                             [("build1", ["task1", "task2", "task3"])])
    def test_get_tasks_by_build_name_success(self, build_name, expected_result, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        assert task_manager.get_tasks_by_build_name() == expected_result

    @pytest.mark.parametrize("build_name, expected_exception",
                             [("not_existing_build_name", BuildNotFoundException)])
    def test_get_tasks_by_build_name_build_not_found(self, build_name, expected_exception, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        with pytest.raises(expected_exception):
            task_manager.get_tasks_by_build_name()

    # @pytest.mark.parametrize("build_name, expected_exception",
    #                          [("", EmptyBuildNameException)])
    # def test_get_tasks_by_build_name_empty_build(self, build_name, expected_exception, create_test_data):
    #     task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
    #     with pytest.raises(expected_exception):
    #         task_manager.get_tasks_by_build_name()

    @pytest.mark.parametrize("build_name, tasks",
                             [("build1", ["task1", "task2", "task3"])])
    def test_create_graph_for_sorting_check_types(self, build_name, tasks, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        task_manager.create_graph_for_sorting(tasks=tasks)
        assert type(task_manager.graph) is dict
        assert all([isinstance(key, str) for key in task_manager.graph.keys()]) is True
        assert all([isinstance(value, set) for value in task_manager.graph.values()]) is True

    @pytest.mark.parametrize("build_name, tasks, expected_result",
                             [("build1", ["task1", "task2", "task3"],
                               {"task1": {"task2"}, "task2": {"task3"}, "task3": set()})])
    def test_create_graph_for_sorting_check_graph_is_filled(self, build_name, tasks, expected_result, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        task_manager.create_graph_for_sorting(tasks=tasks)
        assert task_manager.graph == expected_result

    @pytest.mark.parametrize("build_name, tasks, expected_result",
                             [("build3", [], {})])
    def test_create_graph_for_sorting_check_graph_is_empty(self, build_name, tasks, expected_result, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        task_manager.create_graph_for_sorting(tasks=tasks)
        assert task_manager.graph == expected_result

    @pytest.mark.parametrize("build_name, tasks, expected_result",
                             [("build3", [], [])])
    def test_sort_tasks_by_dependencies_no_tasks(self, build_name, tasks, expected_result, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        task_manager.create_graph_for_sorting(tasks=tasks)
        assert task_manager.sort_tasks_by_dependencies() == expected_result

    @pytest.mark.parametrize("build_name, tasks, expected_result",
                             [("build2", ["task4", "task5"], ["task4", "task5"])])
    def test_sort_tasks_by_dependencies_no_dependencies(self, build_name, tasks, expected_result, create_test_data):
        task_manager = TaskManager(build_name="build2", extracted_data=create_test_data)
        task_manager.create_graph_for_sorting(tasks=tasks)
        assert task_manager.sort_tasks_by_dependencies() == expected_result

    @pytest.mark.parametrize("build_name, tasks, expected_result",
                             [("build1", ["task1", "task2", "task3"], ["task3", "task2", "task1"])])
    def test_sort_tasks_by_dependencies_line_dependencies(self, build_name, tasks, expected_result, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        task_manager.create_graph_for_sorting(tasks=tasks)
        assert task_manager.sort_tasks_by_dependencies() == expected_result

    @pytest.mark.parametrize("build_name, tasks, expected_result",
                             [("build4", ["task6", "task7", "task9", "task10"],
                               ["task5", "task9", "task7", "task6", "task10"])])
    def test_sort_tasks_by_dependencies_diamond_dependencies(self, build_name, tasks, expected_result,
                                                             create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        task_manager.create_graph_for_sorting(tasks=tasks)
        assert task_manager.sort_tasks_by_dependencies() == expected_result

    @pytest.mark.parametrize("build_name, cached_tasks, expected_result",
                             [("build4", [], None)])
    def test_tasks_were_cached_empty_cache(self, build_name, cached_tasks, expected_result, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        assert task_manager.check_if_tasks_were_cached(cached_tasks=cached_tasks) is None

    @pytest.mark.parametrize("build_name, cached_tasks, expected_result",
                             [("build4", {"build4": ["task5", "task9", "task7", "task6", "task10"]},
                               ["task5", "task9", "task7", "task6", "task10"])])
    def test_tasks_were_cached_build_name_in_cache(self, build_name, cached_tasks, expected_result, create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        assert task_manager.check_if_tasks_were_cached(cached_tasks=cached_tasks) == expected_result

    @pytest.mark.parametrize("build_name, cached_tasks, expected_result",
                             [("build2", {"build4": ["task5", "task9", "task7", "task6", "task10"]}, None)])
    def test_tasks_were_cached_build_name_not_in_cache(self, build_name, cached_tasks, expected_result,
                                                       create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        assert task_manager.check_if_tasks_were_cached(cached_tasks=cached_tasks) is None

    @pytest.mark.parametrize("build_name, cached_tasks, sorted_data, expected_result",
                             [("build2", {"build4": ["task5", "task9", "task7", "task6", "task10"]},
                               ["task4", "task5"],
                               {"build4": ["task5", "task9", "task7", "task6", "task10"],
                                "build2": ["task4", "task5"]})])
    def test_add_task_to_cached_enough_space_in_cache(self, build_name, cached_tasks, sorted_data, expected_result,
                                                      create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        task_manager.add_task_to_cached(cached_tasks=cached_tasks, sorted_data=sorted_data)
        assert cached_tasks == expected_result

    @pytest.mark.parametrize("build_name, cached_tasks, sorted_data, expected_result",
                             [("build1", {key: ["task1"] for key in range(50)},
                               ["task3", "task2", "task1"],
                               {key: ["task1"] for key in range(1, 50)} | {"build1": ["task3", "task2", "task1"]})])
    def test_add_task_to_cached_not_enough_space_in_cache(self, build_name, cached_tasks, sorted_data, expected_result,
                                                          create_test_data):
        task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
        task_manager.add_task_to_cached(cached_tasks=cached_tasks, sorted_data=sorted_data)
        assert cached_tasks == expected_result

    # @pytest.mark.parametrize("build_name, cached_tasks",
    #                          [("build1", {"build4": ["task5", "task9", "task7", "task6", "task10"]})])
    # def test_get_sorted_tasks_called_all_inside_methods(self, build_name, cached_tasks, create_test_data):
    #     task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
    #     task_manager.check_if_tasks_were_cached = Mock()
    #     task_manager.get_tasks_by_build_name = Mock()
    #     task_manager.create_graph_for_sorting = Mock()
    #     task_manager.sort_tasks_by_dependencies = Mock()
    #     task_manager.add_task_to_cached = Mock()
    #     task_manager.get_sorted_tasks(cached_tasks=cached_tasks)
    #     task_manager.check_if_tasks_were_cached.assert_called_once()
    #     task_manager.get_tasks_by_build_name.assert_called_once()
    #     task_manager.create_graph_for_sorting.assert_called_once()
    #     task_manager.sort_tasks_by_dependencies.assert_called_once()
    #     task_manager.add_task_to_cached.assert_called_once()
    #
    # @pytest.mark.parametrize("build_name, cached_tasks",
    #                          [("build4", {"build4": ["task5", "task9", "task7", "task6", "task10"]})])
    # def test_get_sorted_tasks_called_only_check_if_tasks_were_cached_method(self, build_name, cached_tasks,
    #                                                                         create_test_data):
    #     task_manager = TaskManager(build_name=build_name, extracted_data=create_test_data)
    #     task_manager.check_if_tasks_were_cached = Mock()
    #     task_manager.get_tasks_by_build_name = Mock()
    #     task_manager.create_graph_for_sorting = Mock()
    #     task_manager.sort_tasks_by_dependencies = Mock()
    #     task_manager.add_task_to_cached = Mock()
    #     task_manager.get_sorted_tasks(cached_tasks=cached_tasks)
    #     task_manager.check_if_tasks_were_cached.assert_called_once()
    #     task_manager.get_tasks_by_build_name.assert_not_called()
    #     task_manager.create_graph_for_sorting.assert_not_called()
    #     task_manager.sort_tasks_by_dependencies.assert_not_called()
    #     task_manager.add_task_to_cached.assert_not_called()


class TestTaskSorting:
    @pytest.mark.parametrize("task, expected_result", [("task3", ["task3"])])
    def test_add_node_to_stack_task_not_in_graph_keys(self, create_graph, task, expected_result):
        task_sorting = TaskSorting(graph=create_graph)
        task_sorting.add_node_to_stack(task=task)
        assert task_sorting.stack_tasks_not_in_graph_keys == expected_result

    @pytest.mark.parametrize("task, expected_result", [("task4", ["task4"])])
    def test_add_node_to_stack_tasks_in_graph_keys(self, create_graph, task, expected_result):
        task_sorting = TaskSorting(graph=create_graph)
        task_sorting.add_node_to_stack(task=task)
        assert task_sorting.stack_tasks_in_graph_keys == expected_result

    @pytest.mark.parametrize("expected_result", [(["task3", "task1", "task2", "task4", "task5"])])
    def test_run_task_sorting_check_return_value(self, create_graph, expected_result):
        task_sorting = TaskSorting(graph=create_graph)
        assert task_sorting.run_task_sorting() == expected_result

    def test_add_node_to_stack_called_inside_run_task_sorting(self, create_graph):
        task_sorting = TaskSorting(graph=create_graph)
        task_sorting.add_node_to_stack = Mock()
        task_sorting.run_task_sorting()
        task_sorting.add_node_to_stack.assert_called()

    @pytest.mark.parametrize("graph, expected_result", [({}, [])])
    def run_task_sorting_empty_graph(self, graph, expected_result):
        task_sorting = TaskSorting(graph=graph)
        assert task_sorting.run_task_sorting() == expected_result
