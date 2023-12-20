import json
from fastapi import Request, Response, APIRouter

from src.config import cached_tasks
from src.core.task_manager import TaskManager
from src.schemas.models import Build

router = APIRouter()


@router.post("/get_tasks")
async def get_tasks(build_data: Build, request: Request) -> Response:
    build_name = build_data.build
    task_manager = TaskManager(build_name=build_name, extracted_data=request.app.state.builds_and_tasks)
    sorted_tasks = task_manager.get_sorted_tasks(cached_tasks=cached_tasks)
    return Response(status_code=200, content=json.dumps(sorted_tasks))