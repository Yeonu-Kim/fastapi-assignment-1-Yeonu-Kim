from pydantic import BaseModel

class UserCreateRequest:
    username: str
    password: str
    email: str

class UserCreateResponse:
    user_id: str
    token: str
    username: str
    password: str
    email: str