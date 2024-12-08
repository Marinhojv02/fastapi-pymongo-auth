from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime

class CreateProductPayload(BaseModel):
    name: str
    price: float
    discount_price: float
    type: str
    description: str
    expiry_date: datetime

    class Config:
        # Isso vai garantir que o Pydantic converta para o formato correto no MongoDB
        orm_mode = True

class UpdateProductPayload(BaseModel):
    name: Optional[str]
    price: Optional[float]
    discount_price: Optional[float]
    type: Optional[str]
    description: Optional[str]
    expiry_date: Optional[datetime]
    
class Product(BaseModel):
    name: str
    price: float
    discount_price: Optional[float] = None
    type: str
    description: str
    expiry_date: datetime