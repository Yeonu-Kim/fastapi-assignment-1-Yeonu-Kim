from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase as Base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column

DeclarativeBase: type[Base] = declarative_base()

intpk = Annotated[int, mapped_column(primary_key=True)]
str20 = Annotated[str, mapped_column(String(20))]
str63 = Annotated[str, mapped_column(String(63))]
str255 = Annotated[str, mapped_column(String(255))]