from app.pydantic_models.products_model import CreateProductPayload
from app.utils.database import product_collection
from pymongo.errors import DuplicateKeyError

class CreateProductService:
    def __init__(self):
        self.product_collection = product_collection

    def add_product(self, product_data: CreateProductPayload):
        # Verificar se o produto já existe no banco de dados com o mesmo nome e tipo
        existing_product = self.product_collection.find_one({
            "name": product_data.name,
            "type": product_data.type
        })

        if existing_product:
            raise ValueError({"message": "Produto com o mesmo nome e tipo já existe."})

        # Criar o produto com base nos dados validados pelo Pydantic
        new_product = product_data.dict()  # Converte o modelo Pydantic para um dicionário
        new_product["is_active"] = True

        # Inserir o produto na coleção do banco de dados
        result = self.product_collection.insert_one(new_product)

        return {"message": "Produto adicionado com sucesso!", "product_id": str(result.inserted_id)}
