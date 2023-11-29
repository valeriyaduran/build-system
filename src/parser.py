from yaml import safe_load

from src.config import build_file_path, tasks_file_path


class YamlParser:
    @staticmethod
    def parse_build_and_tasks_yaml_files() -> dict:
        with open(build_file_path, "r") as builds_file, open(tasks_file_path, "r") as tasks_file:
            builds = safe_load(builds_file)
            tasks = safe_load(tasks_file)
            merged_data = {**builds, **tasks}
        return merged_data
