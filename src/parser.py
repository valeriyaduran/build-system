from yaml import safe_load


class YamlParser:
    _build_file_path = "builds/builds.yaml"
    _tasks_file_path = "builds/tasks.yaml"

    @classmethod
    def parse_build_and_tasks_yaml_files(cls) -> dict:
        with open(cls._build_file_path, "r") as builds_file, open(cls._tasks_file_path, "r") as tasks_file:
            builds = safe_load(builds_file)
            tasks = safe_load(tasks_file)
            merged_data = {**builds, **tasks}
        return merged_data


