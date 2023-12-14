from sqlalchemy import Column, Integer, String
from .database import Database



class User(Database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    username = Column(String, unique=True, index=True)
    mail = Column(String, unique=True, index=True)
    hashed_password = Column(String)