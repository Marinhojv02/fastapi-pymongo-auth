# GENERIC LIB
from datetime import datetime
# CONTROLLERS
from app.controllers.create_user_controller import CreateUserController
# MODEL
from app.models.users_model import CreateUserPayload
# UTILS


class UserService:
    def create(self, user_info: CreateUserPayload) -> bool:
        user_controller = CreateUserController(user_info)
        return user_controller.create()