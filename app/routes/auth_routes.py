# GENERIC LIB
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
# CONTROLLERS
from app.services.auth_service import AuthService
# MODEL
from app.models.token_model import Token
# UTILS
from app.utils.validate_user import get_current_user

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)

@auth_router.post("/login", response_model=Token)
async def login(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user, err = AuthService.authenticate_user(data.username, data.password)
    if err:
        raise HTTPException(status_code=401, detail=err)
    token = AuthService.create_access_token(user.get('username', ''), user.get('_id', ''), user.get('role', ''))
    return {'access_token': token, 'token_type':'bearer'}

@auth_router.get("/me")
async def read_item(user: Annotated[dict, Depends(get_current_user)]):
    if user is None:
       raise HTTPException(status_code=404, detail="Item not found")
    return {"user": user}