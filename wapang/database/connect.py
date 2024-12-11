import os
from typing import Iterator
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

class DBSessionFactoy:
    def __init__(self):
        self._engine: Engine = create_engine(
            SQLALCHEMY_DATABASE_URL
        )
        self._session_maker = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    def get_engine(self) -> Engine:
        return self._engine
    
    def make_session(self) -> Session:
        return self._session_maker()

def get_db_session() -> Iterator[Session]:
    session = DBSessionFactoy().make_session()
    try:
        yield session

    finally:
        session.commit()
        session.close()