from fastapi import FastAPI

from wapang.apps.router import api_router

app = FastAPI()

app.include_router(api_router)
