from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
def hello_world():
    return {"text": "Hello World!"}
