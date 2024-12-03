from pydantic import BaseModel

class UserCreateRequest(BaseModel):
    username: str
    password: str
    email: str

class UserCreateResponse(BaseModel):
    user_id: str
    token: str
    username: str
    email: str