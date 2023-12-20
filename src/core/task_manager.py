from typing import Dict

from src.handlers.exception_handler import BuildNotFoundException


class TaskManager:
    def __init__(self, build_name: str, extracted_data: dict) -> None:
        self.build_name = build_name
        self.extracted_data = extracted_data
        self.graph: Dict[str, set] = {}
        self.max_len_of_cached_tasks: int = 50

    def get_tasks_by_build_name(self) -> list:
        tasks = [build["tasks"] for build in self.extracted_data["builds"] if build["name"] == self.build_name]
        if not tasks:
            raise BuildNotFoundException(message=f"No build '{self.build_name}' found",
                                         status_code=400)
        return tasks[0]

    def create_graph_for_sorting(self, tasks: list) -> None:
        for task in tasks:
            for task_info in self.extracted_data["tasks"]:
                if task_info["name"] == task:
                    self.graph[task] = set(task_info['dependencies'])

    def sort_tasks_by_dependencies(self) -> list:
        task_sorting = TaskSorting(self.graph)
        sorted_tasks = task_sorting.run_task_sorting()
        return sorted_tasks

    def check_if_tasks_were_cached(self, cached_tasks) -> list:
        if self.build_name in cached_tasks:
            return cached_tasks[self.build_name]

    def add_task_to_cached(self, cached_tasks, sorted_data) -> None:
        if len(cached_tasks) >= self.max_len_of_cached_tasks:
            cached_tasks.pop(next(iter(cached_tasks)))
        cached_tasks[self.build_name] = sorted_data

    def get_sorted_tasks(self, cached_tasks) -> list:
        sorted_data = self.check_if_tasks_were_cached(cached_tasks=cached_tasks)
        if not sorted_data:
            tasks = self.get_tasks_by_build_name()
            self.create_graph_for_sorting(tasks=tasks)
            sorted_data = self.sort_tasks_by_dependencies()
            self.add_task_to_cached(cached_tasks=cached_tasks, sorted_data=sorted_data)
        return sorted_data


class TaskSorting:
    def __init__(self, graph: dict) -> None:
        self.graph = graph
        self.tasks = list(graph.keys())
        self.visited_nodes = {task: False for task in self.tasks}
        self.stack_tasks_in_graph_keys = []
        self.stack_tasks_not_in_graph_keys = []

    def add_node_to_stack(self, task: str) -> None:
        self.visited_nodes[task] = True
        if task in self.graph:
            for dependency in list(self.graph[task]):
                if dependency not in self.visited_nodes or not self.visited_nodes[dependency]:
                    self.add_node_to_stack(dependency)
            self.stack_tasks_in_graph_keys.append(task)
        else:
            self.stack_tasks_not_in_graph_keys.append(task)

    def run_task_sorting(self) -> list:
        for task in self.tasks:
            if not self.visited_nodes[task]:
                self.add_node_to_stack(task)
        return self.stack_tasks_not_in_graph_keys + self.stack_tasks_in_graph_keys
