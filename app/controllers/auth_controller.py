# GENERIC LIB
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
# CONTROLLERS
from app.services.auth_service import AuthService
# MODEL
from app.pydantic_models.auth_model import LoginRequest
from app.pydantic_models.token_model import Token
# UTILS
from app.utils.validate_user import get_current_user

auth_router = APIRouter(
    prefix='/api/auth',
    tags=['auth'],
)

@auth_router.post("/login", response_model=Token)
async def login(data: LoginRequest):
    token = AuthService.authenticate_user(data.email, data.password)
    return {'access_token': token, 'token_type':'bearer'}

@auth_router.get("/me")
async def read_item(user: Annotated[dict, Depends(get_current_user)]):
    if user is None:
       raise HTTPException(status_code=404, detail="Item not found")
    return {"user": user}