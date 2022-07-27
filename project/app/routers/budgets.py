from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from app.models.pydantic import BudgetPayloadSchema, BudgetResponseSchema
from app.models.tortoise import BudgetSchema
from app.utils.crud.budgets_crud import get, post

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/", response_model=BudgetResponseSchema, status_code=201)
async def create_budget(
    payload: BudgetPayloadSchema, token: str = Depends(oauth2_scheme)
) -> BudgetResponseSchema:
    budget_id = await post(payload)

    response_object = {
        "id": budget_id,
        "month": payload.month,
        "year": payload.year,
        "user_id": payload.user_id,
    }
    return response_object


@router.get("/{id}/", response_model=BudgetSchema)
async def read_budget(id: int, token: str = Depends(oauth2_scheme)) -> BudgetSchema:
    budget = await get(id)

    return budget
