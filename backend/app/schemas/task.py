from pydantic import BaseModel
from datetime import date

class TaskCreate(BaseModel):
    title: str
    description: str
    project_id: int
    assigned_to: int
    due_date: date


class TaskStatusUpdate(BaseModel):
    status: str


class TaskAssign(BaseModel):
    assigned_to: int
    
class TaskStatusUpdate(BaseModel):
    status: str