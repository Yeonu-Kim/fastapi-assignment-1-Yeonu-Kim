from fastapi import Depends
from typing import Annotated

from wapang.apps.user.dto import UserCreateRequest, UserCreateResponse
from wapang.apps.user.repositories import UserRepository

class UserService:
    def __init__(
        self,
        user_repository: Annotated[UserRepository, Depends()]
    ) -> None:
        self.user_repository= user_repository

    def create_user(
        self,
        request: UserCreateRequest
    ) -> UserCreateResponse:
        return self.user_repository.create_user(request)