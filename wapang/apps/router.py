from fastapi import APIRouter

from wapang.apps.user import user_router

api_router = APIRouter(prefix="/api")

api_router.include_router(user_router)
