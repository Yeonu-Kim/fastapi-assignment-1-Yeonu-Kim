from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    username: int
    email: str
    password: str