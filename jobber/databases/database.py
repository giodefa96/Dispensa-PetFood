from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
import os


class Database:
    Base = declarative_base()

    def __init__(self):
        DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        self.engine = create_engine(DATABASE_URL)
        self.SessionLocal = AsyncSession(autocommit=False, autoflush=False, bind=self.engine)
