from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from src.api.v1.get_tasks import router
from src.config import builds_file_path, tasks_file_path
from src.handlers.exception_handler import add_exception_handlers
from src.dependencies import verify_api_key
from src.parser import YamlParser


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.builds_and_tasks = YamlParser.parse_build_and_tasks_yaml_files(builds_data_file_path=builds_file_path,
                                                                             tasks_data_file_path=tasks_file_path)
    yield


def create_app() -> FastAPI:
    application = FastAPI(dependencies=[Depends(verify_api_key)], lifespan=lifespan)
    add_exception_handlers(app=application)
    return application


app = create_app()
app.include_router(router=router)
