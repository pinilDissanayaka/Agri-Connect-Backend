from database.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Text


class Resource(Base):
    __tablename__="resource"
    
    id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer)
    contex=Column(Text)