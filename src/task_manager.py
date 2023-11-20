from typing import Dict


class TaskManager:
    def __init__(self, build_name: str, extracted_data: dict):
        self.build_name = build_name
        self.extracted_data = extracted_data
        self.graph: Dict[str, set] = {}

    def get_tasks_by_build_name(self) -> list:
        tasks = [build["tasks"] for build in self.extracted_data["builds"] if build["name"] == self.build_name]
        return tasks[0]

    def create_graph_for_sorting(self, tasks: list) -> None:
        for task in tasks:
            for task_info in self.extracted_data["tasks"]:
                if task_info["name"] == task:
                    self.graph[task] = set(task_info['dependencies'])

    def sort_tasks_by_dependencies(self) -> list:
        topological_sorting = TopologicalSorting(self.graph)
        sorted_tasks = topological_sorting.run_topological_sorting()
        return sorted_tasks

    def get_sorted_tasks(self) -> list:
        tasks = self.get_tasks_by_build_name()
        self.create_graph_for_sorting(tasks=tasks)
        sorted_data = self.sort_tasks_by_dependencies()
        return sorted_data


class TopologicalSorting:
    def __init__(self, graph: dict):
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

    def run_topological_sorting(self) -> list:
        for task in self.tasks:
            if not self.visited_nodes[task]:
                self.add_node_to_stack(task)
        return self.stack_tasks_not_in_graph_keys + self.stack_tasks_in_graph_keys
