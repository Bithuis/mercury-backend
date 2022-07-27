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


class RegisterPayloadSchema(BaseModel):
    username: str
    email: str
    password: str
    full_name: str


class RegisterResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    full_name: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int = None
    username: str | None = None
    email: str | None = None
    full_name: str | None = None
