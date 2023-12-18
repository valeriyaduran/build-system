import json
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response, Depends

from src.handlers.exception_handler import add_exception_handlers
from src.dependencies import verify_api_key
from src.models import Build
from src.config import builds_and_tasks, cached_tasks
from src.parser import YamlParser

from src.task_manager import TaskManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    builds_and_tasks["data"] = YamlParser.parse_build_and_tasks_yaml_files
    yield
    builds_and_tasks.clear()


def create_app() -> FastAPI:
    application = FastAPI(dependencies=[Depends(verify_api_key)], lifespan=lifespan)
    add_exception_handlers(app=application)
    return application


app = create_app()


@app.post("/get_tasks")
async def get_tasks(build_data: Build, request: Request) -> Response:
    build_name = build_data.build
    task_manager = TaskManager(build_name=build_name, extracted_data=builds_and_tasks["data"]())
    sorted_tasks = task_manager.get_sorted_tasks(cached_tasks=cached_tasks)
    return Response(status_code=200, content=json.dumps(sorted_tasks))