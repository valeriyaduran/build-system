from pydantic import BaseModel, field_validator

from src.handlers.exception_handler import EmptyBuildNameException


class Build(BaseModel):
    build: str

    @field_validator("build")
    def build_name_must_not_be_empty(cls, build_name: str) -> str:
        if not build_name:
            raise EmptyBuildNameException(message="Build name must not be empty", status_code=400)
        return build_name
