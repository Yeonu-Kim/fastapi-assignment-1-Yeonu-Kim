from wapang.apps.user.dto import UserCreateRequest
from wapang.apps.user.models import User

class UserRepository:
    def create_user(
        self,
        request: UserCreateRequest
    ) -> User:
        return {
            "user_id": "aaa",
            "token": "bbb",
            "username": request.username,
            "email": request.email,
        }