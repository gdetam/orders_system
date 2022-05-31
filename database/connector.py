"""Database connector."""

import os

from dotenv import load_dotenv

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


load_dotenv()

Base = declarative_base()
engine = create_engine(os.getenv('POSTGRES_DNS'))
meta = MetaData(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    return db
