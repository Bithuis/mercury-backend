from pydantic import BaseModel


class BudgetPayloadSchema(BaseModel):
    month: int
    year: int
    user_id: int


class BudgetResponseSchema(BaseModel):
    id: int
    month: int
    year: int
    user_id: int
