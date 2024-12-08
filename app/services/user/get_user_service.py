from typing import Optional, List, Union
from bson import ObjectId
from app.utils.database import user_collection


class GetUserService:
    def __init__(self):
        self.user_collection = user_collection

    def get_users(
        self,
        cpf: Optional[str] = None,
        username: Optional[str] = None,
        email: Optional[str] = None,
        id: Optional[str] = None,
        page: int = 1,
        page_size: int = 10,
    ) -> Union[dict, List[dict]]:
        # Filtrar por CPF, Username, Email ou ID
        query = {}
        if cpf:
            query["cpf"] = cpf
        if username:
            query["username"] = username
        if email:
            query["email"] = email
        if id:
            try:
                query["_id"] = ObjectId(id)
            except Exception:
                raise ValueError("ID inválido.")

        # Se houver filtros, buscar apenas um usuário
        if query:
            user = self.user_collection.find_one(query)
            if user:
                user["_id"] = str(user["_id"])
                return user
            raise ValueError("Usuário não encontrado.")

        # Caso contrário, buscar todos os usuários com paginação
        skip = (page - 1) * page_size

        users = list(self.user_collection.find({}).skip(skip).limit(page_size))
        
        for user in users:
            user["_id"] = str(user["_id"])
        
        return {"total": len(users), "page": page, "page_size": page_size, "users": users}