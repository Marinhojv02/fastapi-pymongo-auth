from bson import ObjectId
from app.utils.database import user_collection

class UpdateUserService:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def execute(self, updated_data: dict):
        """
        Atualiza os dados de um usuário.
        """
        if not self.user_id:
            raise Exception("USER_ID_REQUIRED")

        result = user_collection.update_one(
            {'_id': ObjectId(self.user_id), 'is_active': True},
            {'$set': updated_data}
        )

        if result.modified_count == 0:
            raise Exception("USER_NOT_FOUND_OR_NOT_UPDATED")

        return user_collection.find_one({'_id': ObjectId(self.user_id)})
