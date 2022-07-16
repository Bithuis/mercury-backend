from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import BudgetPayloadSchema, BudgetResponseSchema
from app.models.tortoise import BudgetSchema


router = APIRouter()


@router.post("/", response_model=BudgetResponseSchema, status_code=201)
async def create_budget(payload: BudgetPayloadSchema) -> BudgetResponseSchema:
    budget_id = await crud.post(payload)

    response_object = {
        "id": budget_id,
        "month": payload.month,
        "year": payload.year,
        "user_id": payload.user_id,
    }
    return response_object


@router.get("/{id}/", response_model=BudgetSchema)
async def read_budget(id: int) -> BudgetSchema:
    budget = await crud.get(id)

    return budget
