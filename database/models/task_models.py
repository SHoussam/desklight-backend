from sqlmodel import  SQLModel 
from datetime import date
from typing import Optional



class TaskCreate(SQLModel):
    title: str
    module: str
    due_date: date


class TaskRead(SQLModel):
    title: str
    module: str
    due_date: date
    completed: bool



class TaskUpdate(SQLModel):
    title: Optional[str] = None
    module: Optional[str] = None
    due_date: Optional[date] = None
    completed: Optional[bool] = None
# ======================