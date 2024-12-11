from fastapi import APIRouter, Depends
from typing import Annotated
from wapang.apps.user.dto import UserCreateRequest
from wapang.apps.user.service.UserService import UserService

router = APIRouter(prefix='/user', tags=['user'])

@router.post('/signup')
def create_user(
    request: UserCreateRequest,
    user_service: Annotated[UserService, Depends()]
):
    user_service.create_user(request)
    return None
