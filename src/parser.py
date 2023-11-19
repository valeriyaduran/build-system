import yaml


class YamlParser:
    _build_file_path = 'builds/builds.yaml'
    _tasks_file_path = 'builds/tasks.yaml'

    @classmethod
    def parse_build_and_tasks_yaml_files(cls) -> dict:
        print("----------------parse_build_and_tasks_yaml_files--------------------")
        with open(cls._build_file_path, 'r') as builds_file, open(cls._tasks_file_path, 'r') as tasks_file:
            builds = yaml.safe_load(builds_file)
            tasks = yaml.safe_load(tasks_file)
            merged_data = {**builds, **tasks}
            print("After yaml merging")
        return merged_data


