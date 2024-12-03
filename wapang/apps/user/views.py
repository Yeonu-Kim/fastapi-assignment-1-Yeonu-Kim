from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from wapang.apps.user.dto import UserCreateRequest, UserCreateResponse
from wapang.apps.user.service import UserService

router = APIRouter(prefix='/user', tags=['user'])

@router.post('/signup')
def create_user(
    request: UserCreateRequest,
    user_service: Annotated[UserService, Depends()]
) -> UserCreateResponse:
    return user_service.create_user(request)
