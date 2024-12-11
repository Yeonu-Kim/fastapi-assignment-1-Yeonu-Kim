from fastapi import Depends
from typing import Annotated

from wapang.apps.user.service.AuthService import AuthService
from wapang.apps.user.models import User
from wapang.apps.user.dto import UserCreateRequest
from wapang.apps.user.repositories import UserRepository

class UserService:
    def __init__(
        self,
        user_repository: Annotated[UserRepository, Depends()],
        auth_service: Annotated[AuthService, Depends()]
    ) -> None:
        self.user_repository=user_repository
        self.auth_service=auth_service

    def create_user(
        self,
        request: UserCreateRequest
    ) -> bool:
        hashed_password = self.auth_service.hash_password(request.password)    
        user = User(
            username=request.username,
            password=hashed_password,
            email=request.email,
        )

        return self.user_repository.create_user(user)
        