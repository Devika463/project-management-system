from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str
    created_by: int

class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        from_attributes = True

class ProjectUpdate(BaseModel):
    name: str
    description: str