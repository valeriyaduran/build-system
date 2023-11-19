# import pytest
# from httpcore import request
# from fastapi import Response
#
# from handlers.exception_handler import BuildNotFoundException
# from src.main import get_tasks
# from src.task_manager import TaskManager
#
#
# # @pytest.mark.parametrize("build, expected_result", [({}, )])
# # def test_task_sorting_empty_build_object(build, expected_result):
# #     with pytest.raises(HTTPException):
# #     task_manager = TaskManager(build_name=build_name, extracted_data=builds_and_tasks["data"]())
# #     assert task_manager.get_tasks_by_build_name() == expected_result
#
#
# @pytest.mark.parametrize("build, expected_result", [({}, Response(status_code=400, content="Message: Empty build name"))])
# def test_task_sorting_empty_build_name(build, expected_result):
#     assert get_tasks(build) == expected_result
#
#
# def test_task_sorting_incorrect_build_name_type():
#     build = {
#         "build": 123
#     }
#
#
# def test_task_sorting_build_absent_in_builds():
#     build = {
#         "build": "testnameabsent"
#     }
#     with pytest.raises(BuildNotFoundException):
#         pass
#
# def test_task_sorting_no_dependencies():
#     tasks = ["task1", "task2", "task3"]
#     dependencies = [{"name": "task1", "dependencies": []},
#                     {"name": "task2", "dependencies": []},
#                     {"name": "task3", "dependencies": []}]
#
#
# def test_task_sorting_with_diamond_dependencies():
#     tasks = ["task1", "task2", "task3", "task4"]
#     dependencies = [{"name": "task1", "dependencies": ["task2", "task3"]},
#                     {"name": "task2", "dependencies": ["task4"]},
#                     {"name": "task3", "dependencies": ["task4"]},
#                     {"name": "task4", "dependencies": []}]
#
#
# def test_task_sorting_line_dependencies():
#     tasks = ["task1", "task2", "task3"]
#     dependencies = [{"name": "task1", "dependencies": ["task2"]},
#                     {"name": "task2", "dependencies": ["task3"]},
#                     {"name": "task3", "dependencies": []}]


import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
