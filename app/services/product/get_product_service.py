from typing import Optional, List, Union
from datetime import datetime
from bson import ObjectId
from app.utils.database import product_collection

class GetProductService:
    def __init__(self):
        self.product_collection = product_collection

    def get_products(
        self,
        name: Optional[str] = None,
        type: Optional[str] = None,
        max_price: Optional[float] = None,
        min_price: Optional[float] = None,
        max_discount_price: Optional[float] = None,
        min_discount_price: Optional[float] = None,
        id: Optional[str] = None,
        page: int = 1,
        page_size: int = 10,
    ) -> Union[dict, List[dict]]:
        # Filtro de busca
        query = {}
        
        # Aplicando filtros se fornecidos
        if name:
            query["name"] = {"$regex": name, "$options": "i"}  # Pesquisa por nome com case-insensitive
        if id:
            try:
                query["_id"] = ObjectId(id)
            except Exception:
                raise ValueError("ID inválido.")
        # Se houver filtros, busca apenas um produto
        if query:
            product = self.product_collection.find_one(query)
            if product:
                return product
            raise ValueError("Produto não encontrado.")
        
        if type:
            query["type"] = {"$regex": type, "$options": "i"}  # Pesquisa por tipo com case-insensitive
        if max_price is not None:
            query["price"] = {"$lte": max_price}
        if min_price is not None:
            query["price"] = {"$gte": min_price}
        if max_discount_price is not None:
            query["discount_price"] = {"$lte": max_discount_price}
        if min_discount_price is not None:
            query["discount_price"] = {"$gte": min_discount_price}

        # Caso contrário, buscar todos os produtos com paginação
        skip = (page - 1) * page_size
        products = list(self.product_collection.find(query).skip(skip).limit(page_size))

        for product in products:
            product["_id"] = str(product["_id"])
        
        return {"total": len(products), "page": page, "page_size": page_size, "products": products}