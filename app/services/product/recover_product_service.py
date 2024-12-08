from bson import ObjectId
from app.utils.database import product_collection

class ReactivateProductService:
    def __init__(self, product_id: str):
        self.product_id = product_id

    def execute(self):
        """
        Marca o usuário como ativo.
        """
        if not self.product_id:
            raise Exception("PRODUCT_ID_REQUIRED")

        result = product_collection.update_one(
            {'_id': ObjectId(self.product_id)},
            {'$set': {'is_active': True}}
        )

        if result.modified_count == 0:
            raise Exception("PRODUCT_NOT_FOUND_OR_ALREADY_ACTIVE")

        return {"message": "PRODUCT_REACTIVATED"}
