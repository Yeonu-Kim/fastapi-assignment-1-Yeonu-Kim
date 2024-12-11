from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session

from wapang.apps.user.dto import UserCreateRequest
from wapang.apps.user.models import User
from wapang.database.connect import get_db_session

class UserRepository:
    def __init__(
        self,
        session: Annotated[Session, Depends(get_db_session)],
    ):
        self.session = session

    def create_user(
        self,
        user: User
    ) -> True:
        self.session.add(user)
        return True