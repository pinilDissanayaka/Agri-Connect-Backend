from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr
from datetime import datetime


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    user_name: str
    email:EmailStr
    password: str
    created_at: Optional[datetime]=datetime.now()
    
    
class Resource(BaseModel):
    id: Optional[UUID]=uuid4
    user_id: UUID