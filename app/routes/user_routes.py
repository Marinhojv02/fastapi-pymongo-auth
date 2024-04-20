# GENERIC LIB
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from bson import ObjectId
from typing import Annotated
# CONTROLLERS
from app.controllers.create_user_controller import UsersControllers
from app.services.user_service import UserService
# MODEL
from app.models.users_model import User, CreateUserPayload
# UTILS
from app.utils.database import user_collection
from app.utils.validate_user import get_current_user

auth_router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@auth_router.post("/register")
async def create_user(user_data: CreateUserPayload):
    res, err = UserService().create(user_data)
    if(err):
        print(err)
        raise HTTPException(status_code=400, detail="Missing information")
    return {'message': 'SUCCESS_CREATE'}
    
@auth_router.get("/{id}", response_model=User)
async def read_item(id: str):
    item = await user_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")