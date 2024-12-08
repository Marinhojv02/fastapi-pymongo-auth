from bson import ObjectId
from app.utils.database import user_collection

class DeactivateUserService:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def execute(self):
        """
        Marca o usuário como inativo.
        """
        if not self.user_id:
            raise Exception("USER_ID_REQUIRED")

        result = user_collection.update_one(
            {'_id': ObjectId(self.user_id)},
            {'$set': {'is_active': False}}
        )

        if result.modified_count == 0:
            raise Exception("USER_NOT_FOUND_OR_ALREADY_INACTIVE")

        return {"message": "USER_DEACTIVATED"}
