from fastapi import APIRouter, Depends, HTTPException
from wapang.apps.user.schemas import UserCreateRequest, UserCreateResponse

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/signup')
def create_user(
    request: UserCreateRequest,
) -> UserCreateResponse:
    return {"text": "Hello World!"}
