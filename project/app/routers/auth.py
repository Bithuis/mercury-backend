from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models.pydantic import RegisterPayloadSchema, RegisterResponseSchema
from app.utils.auth_utils import (authenticate_user, create_access_token,
                                  get_password_hash)
from app.utils.crud.auth_crud import post

router = APIRouter()


@router.post("/register/", response_model=RegisterResponseSchema, status_code=201)
async def read_users_me(payload: RegisterPayloadSchema) -> RegisterResponseSchema:
    payload.password = get_password_hash(payload.password)
    user_id = await post(payload)

    response_object = {
        "id": user_id,
        "username": payload.username,
        "email": payload.email,
        "full_name": payload.full_name,
    }
    return response_object


@router.post("/login/")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
