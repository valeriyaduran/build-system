from fastapi import Request, Response, FastAPI


class BaseCustomException(Exception):
    def __init__(self, message: str, status_code: int) -> None:
        self.message = message
        self.status_code = status_code


class EmptyBuildNameException(BaseCustomException):
    pass


class BuildNotFoundException(BaseCustomException):
    pass


def empty_build_name_exception_handler(app: FastAPI):
    @app.exception_handler(EmptyBuildNameException)
    async def exception_handler(request: Request, exc: EmptyBuildNameException) -> Response:
        return Response(status_code=exc.status_code, content=exc.message)


def build_not_found_exception_handler(app: FastAPI):
    @app.exception_handler(BuildNotFoundException)
    async def exception_handler(request: Request, exc: BuildNotFoundException) -> Response:
        return Response(status_code=exc.status_code, content=exc.message)


def add_exception_handlers(app: FastAPI) -> None:
    empty_build_name_exception_handler(app=app)
    build_not_found_exception_handler(app=app)
