from pytest import fixture
from fastapi.testclient import TestClient

from src.main import app


@fixture()
def create_test_data() -> dict:
    extracted_data = {
        "builds":
            [
                {"name": "build1",
                 "tasks": ["task1", "task2", "task3"]},
                {"name": "build2",
                 "tasks": ["task4", "task5"]},
                {"name": "build3",
                 "tasks": []},
                {"name": "build4",
                 "tasks": ["task6", "task7", "task9", "task10"]},
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
            {"name": "task10", "dependencies": ["task9"]}
        ]
    }
    return extracted_data


@fixture()
def create_graph() -> dict:
    graph = {'task1': [],
             'task2': ['task3', 'task1'],
             'task4': ['task3'],
             'task5': ['task4']}
    return graph


@fixture()
def mock_builds_and_tasks(mocker, create_test_data) -> dict:
    mocked_builds_and_tasks = mocker.patch(
        "src.parser.YamlParser.parse_build_and_tasks_yaml_files",
    )
    mocked_builds_and_tasks.return_value = create_test_data
    return mocked_builds_and_tasks.return_value

@fixture()
def test_client():
    yield TestClient(app)
