from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class UserModel(Base):
    __tablename__='user'
    
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name=Column(String(20))
    email=Column(String(20))
    password=Column(String(100))
    created_at=Column(DateTime)