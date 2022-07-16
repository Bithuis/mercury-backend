from typing import Optional

from fastapi import HTTPException
from app.models.pydantic import BudgetPayloadSchema
from app.models.tortoise import Budget


async def post(payload: BudgetPayloadSchema) -> int:
    budget = Budget(
        month=payload.month,
        year=payload.year,
        amount=0.0,
        user_id=payload.user_id,
    )
    await budget.save()
    return budget.id


async def get(id: int) -> Optional[dict]:
    budget = await Budget.filter(id=id).first().values()
    if not budget:
        raise HTTPException(status_code=404, detail="budget not found")
    return budget
