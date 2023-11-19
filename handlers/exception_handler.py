from fastapi import Request, Response

from src.main import app


class BuildNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(BuildNotFoundException)
async def build_not_found_exception_handler(request: Request, exc: BuildNotFoundException):
    return Response(
        status_code=400,
        content={"message": f"Build name '{exc.name}' not found"},
    )
