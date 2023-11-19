from fastapi import Request, Response


class BuildNotFoundException(Exception):
    def __init__(self, build_name: str):
        self.build_name = build_name


async def build_not_found_exception_handler(request: Request, exc: BuildNotFoundException):
    return Response(
        status_code=400,
        content=f"Build name '{exc.build_name}' not found",
    )
