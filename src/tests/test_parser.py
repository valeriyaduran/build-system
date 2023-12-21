from src.config import test_builds_file_path, test_tasks_file_path
from src.parser import YamlParser


class TestParser:
    def test_parse_builds_and_tasks_yaml_files(self, create_test_data):
        assert YamlParser.parse_build_and_tasks_yaml_files(builds_data_file_path=test_builds_file_path,
                                                           tasks_data_file_path=test_tasks_file_path) == \
               create_test_data
