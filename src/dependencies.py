import os

from fastapi import Header, HTTPException
from typing_extensions import Annotated


async def verify_api_key(api_key: Annotated[str, Header()]):
    if not api_key:
        raise HTTPException(status_code=400, detail="No API-Key provided")
    elif api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="API-Key is invalid")
