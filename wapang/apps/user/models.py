from typing import Annotated
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from wapang.database.base import DeclarativeBase
from wapang.database.base import intpk
from wapang.database.base import str20
from wapang.database.base import str63
from wapang.database.base import str255

class User(DeclarativeBase):
    __tablename__ = "user"

    id: Mapped[intpk]
    username: Mapped[str20]
    email: Mapped[str255] = mapped_column(unique=True)
    password: Mapped[str63]

    def __str__(self) -> str:
        return f"<User id={self.id}, name={self.username}, email={self.email}>"