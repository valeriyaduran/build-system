import os
from unittest import mock

import pytest


class TestAPIGetTasks:
    @mock.patch("src.parser.YamlParser.parse_build_and_tasks_yaml_files")
    def test_get_tasks_lifespan_called(self, mocked_builds_and_tasks, create_test_data, test_client):
        mocked_builds_and_tasks.return_value = create_test_data
        with test_client:
            mocked_builds_and_tasks.assert_called()

    @pytest.mark.parametrize("build_name, api_key, url",
                             [("build1", "incorrect_key", "/get_tasks")])
    @mock.patch("src.parser.YamlParser.parse_build_and_tasks_yaml_files")
    def test_get_tasks_incorrect_api_key(self, mocked_builds_and_tasks, build_name, api_key, url, create_test_data,
                                         test_client):
        mocked_builds_and_tasks.return_value = create_test_data
        with test_client:
            response = test_client.post(url=url,
                                        headers={"API-Key": api_key},
                                        json={"build": build_name})
            assert response.status_code == 401
            assert response.json() == {"detail": "API-Key is invalid"}

    @pytest.mark.parametrize("build_name, api_key, url",
                             [("build1", "", "/get_tasks")])
    @mock.patch("src.parser.YamlParser.parse_build_and_tasks_yaml_files")
    def test_get_tasks_no_api_key(self, mocked_builds_and_tasks, build_name, api_key, url, create_test_data,
                                  test_client):
        mocked_builds_and_tasks.return_value = create_test_data
        with test_client:
            response = test_client.post(url=url,
                                        headers={"API-Key": api_key},
                                        json={"build": build_name})
            assert response.status_code == 400
            assert response.json() == {"detail": "No API-Key provided"}

    @pytest.mark.parametrize("build_name, url, expected_result",
                             [("build1", "/get_tasks", ["task3", "task2", "task1"])])
    @mock.patch("src.parser.YamlParser.parse_build_and_tasks_yaml_files")
    def test_get_tasks_success_response(self, mocked_builds_and_tasks, build_name, url, expected_result,
                                        create_test_data,
                                        test_client):
        mocked_builds_and_tasks.return_value = create_test_data
        with test_client:
            response = test_client.post(url=url,
                                        headers={"API-Key": os.getenv("API_KEY")},
                                        json={"build": build_name})
            assert response.status_code == 200
            assert response.json() == expected_result

    @pytest.mark.parametrize("build_name, url, expected_result",
                             [("not_existing_build_name", "/get_tasks", "No build 'not_existing_build_name' found")])
    @mock.patch("src.parser.YamlParser.parse_build_and_tasks_yaml_files")
    def test_get_tasks_build_not_found(self, mocked_builds_and_tasks, build_name, url, expected_result,
                                       create_test_data,
                                       test_client):
        mocked_builds_and_tasks.return_value = create_test_data
        with test_client:
            response = test_client.post(url=url,
                                        headers={"API-Key": os.getenv("API_KEY")},
                                        json={"build": build_name})
            assert response.status_code == 400
            assert response.text == expected_result

    @pytest.mark.parametrize("build_name, url, expected_result",
                             [("", "/get_tasks", "Build name must not be empty")])
    @mock.patch("src.parser.YamlParser.parse_build_and_tasks_yaml_files")
    def test_get_tasks_empty_build_name(self, mocked_builds_and_tasks, build_name, url, expected_result,
                                        create_test_data,
                                        test_client):
        mocked_builds_and_tasks.return_value = create_test_data
        with test_client:
            response = test_client.post(url=url,
                                        headers={"API-Key": os.getenv("API_KEY")},
                                        json={"build": build_name})
            assert response.status_code == 400
            assert response.text == expected_result

    @pytest.mark.parametrize("build_name, url",
                             [(2, "/get_tasks")])
    @mock.patch("src.parser.YamlParser.parse_build_and_tasks_yaml_files")
    def test_get_tasks_build_name_not_str(self, mocked_builds_and_tasks, build_name, url, create_test_data,
                                          test_client):
        mocked_builds_and_tasks.return_value = create_test_data
        with test_client:
            response = test_client.post(url=url,
                                        headers={"API-Key": os.getenv("API_KEY")},
                                        json={"build": build_name})
            assert response.status_code == 422
