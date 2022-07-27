from typing import Optional

from fastapi import HTTPException

from app.models.pydantic import RegisterPayloadSchema
from app.models.tortoise import User


async def post(payload: RegisterPayloadSchema) -> int:
    user = User(
        username=payload.username,
        password=payload.password,
        email=payload.email,
        full_name=payload.full_name,
    )
    await user.save()
    return user.id


async def get(username: str) -> Optional[dict]:
    user = await User.filter(username=username).first().values()
    if not user:
        raise HTTPException(status_code=404, detail="budget not found")
    return user
