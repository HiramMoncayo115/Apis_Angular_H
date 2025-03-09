from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "Pending"
    creationDate: Optional[datetime] = None
    dueDate: Optional[datetime] = None