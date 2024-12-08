# GENERIC LIB
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
# SERVICES
from app.services.product.create_product_service import CreateProductService
from app.services.product.update_product_service import UpdateProductService
from app.services.product.deactivate_product_service import DeactivateProductService
from app.services.product.recover_product_service import ReactivateProductService
from app.services.product.get_product_service import GetProductService
# MODEL
from app.pydantic_models.products_model import Product, CreateProductPayload, UpdateProductPayload

product_router = APIRouter(
    prefix='/api/product',
    tags=['product'],
)

@product_router.post("")
async def create_product(product_data: CreateProductPayload):
    """
    Endpoint para criar um novo usuário.
    """
    try:
        new_product = CreateProductService().add_product(product_data)
        return new_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@product_router.put("/{id}", response_model=Product)
async def update_product(id: str, update_data: UpdateProductPayload):
    """
    Endpoint para atualizar um usuário.
    """
    try:
        updated_product = UpdateProductService(id).execute(update_data.model_dump(exclude_unset=True))
        return updated_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@product_router.patch("/{id}/deactivate")
async def deactivate_product(id: str):
    """
    Endpoint para desativar um usuário.
    """
    try:
        response = DeactivateProductService(id).execute()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@product_router.patch("/{id}/reactivate")
async def reactivate_product(id: str):
    """
    Endpoint para reativar um usuário.
    """
    try:
        response = ReactivateProductService(id).execute()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@product_router.get("/")
async def get_products(
    name: str = Query(None),
    type: str = Query(None),
    max_price: str = Query(None),
    min_price: str = Query(None),
    max_discount_price: str = Query(None),
    min_discount_price: str = Query(None),
    id: str = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
):
    try:
        service = GetProductService()
        result = service.get_products(name,type,max_price,min_price,max_discount_price,min_discount_price, id, page, page_size)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro no servidor.")