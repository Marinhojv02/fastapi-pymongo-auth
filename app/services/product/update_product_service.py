from bson import ObjectId
from app.utils.database import product_collection

class UpdateProductService:
    def __init__(self, product_id: str):
        self.product_id = product_id

    def execute(self, updated_data: dict):
        """
        Atualiza os dados de um usuário.
        """
        if not self.product_id:
            raise Exception("product_id_REQUIRED")

        result = product_collection.update_one(
            {'_id': ObjectId(self.product_id)},
            {'$set': updated_data}
        )

        if result.modified_count == 0:
            raise Exception("USER_NOT_FOUND_OR_NOT_UPDATED")

        return product_collection.find_one({'_id': ObjectId(self.product_id)})
