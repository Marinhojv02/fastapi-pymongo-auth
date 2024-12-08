# GENERIC LIB
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
# SERVICES
from app.services.user.create_user_service import CreateUserService
from app.services.user.update_user_service import UpdateUserService
from app.services.user.deactivate_user_service import DeactivateUserService
from app.services.user.recover_user_service import ReactivateUserService
from app.services.user.get_user_service import GetUserService
# MODEL
from app.pydantic_models.users_model import User, CreateUserPayload, UpdateUserPayload

user_router = APIRouter(
    prefix='/api/users',
    tags=['user'],
)

@user_router.post("/register", response_model=User)
async def create_user(user_data: CreateUserPayload):
    """
    Endpoint para criar um novo usuário.
    """
    try:
        new_user = CreateUserService(user_data).create()
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.post("/create/{role}", response_model=User)
async def create_user(user_data: CreateUserPayload, role:str):
    """
    Endpoint para criar um novo usuário.
    """
    try:
        new_user = CreateUserService(user_data, role).create()
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.put("/{id}", response_model=User)
async def update_user(id: str, update_data: UpdateUserPayload):
    """
    Endpoint para atualizar um usuário.
    """
    try:
        updated_user = UpdateUserService(id).execute(update_data.model_dump(exclude_unset=True))
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.patch("/{id}/deactivate")
async def deactivate_user(id: str):
    """
    Endpoint para desativar um usuário.
    """
    try:
        response = DeactivateUserService(id).execute()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.patch("/{id}/reactivate")
async def reactivate_user(id: str):
    """
    Endpoint para reativar um usuário.
    """
    try:
        response = ReactivateUserService(id).execute()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.get("/")
async def get_users(
    cpf: Optional[str] = Query(None),
    username: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    id: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
):
    try:
        service = GetUserService()
        result = service.get_users(cpf, username, email, id, page, page_size)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro no servidor.")