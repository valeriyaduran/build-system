import graphlib
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
        ts = graphlib.TopologicalSorter(self.graph)
        return list(ts.static_order())

    def get_sorted_tasks(self) -> list:
        tasks = self.get_tasks_by_build_name()
        self.create_graph_for_sorting(tasks=tasks)
        sorted_data = self.sort_tasks_by_dependencies()
        return sorted_data
